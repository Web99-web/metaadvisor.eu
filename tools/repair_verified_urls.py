"""Repair verified URL attributes in generated HTML; never edit article sources.

Only explicitly checked URLs are eligible. Existing original images win over a
temporary fallback if an editor later restores the missing file.
"""
import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import unquote, urljoin, urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
DOMAIN = 'https://metaadvisor.eu'
ATTR = re.compile(r'''\s+(?P<name>[^\s=/>]+)(?:\s*=\s*(?P<value>"[^"]*"|'[^']*'|[^\s>]+))?''', re.S)
JSON_STRING = re.compile(r'"(?:\\.|[^"\\])*"')

def url_key(value, base):
    try: p = urlsplit(urljoin(base, html.unescape(value)))
    except ValueError: return ''
    return unquote(p.path) if p.hostname == 'metaadvisor.eu' else urlunsplit((p.scheme, p.netloc, p.path, '', ''))

class Head(HTMLParser):
    def __init__(self, fallback):
        super().__init__(); self.base = fallback
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'link' and a.get('rel') == 'canonical': self.base = a.get('href') or self.base

class Repair(HTMLParser):
    def __init__(self, text, base, present, plan):
        super().__init__(convert_charrefs=False)
        self.text, self.base, self.present, self.plan = text, base, present, plan
        self.offsets = [0]
        for m in re.finditer('\n', text): self.offsets.append(m.end())
        self.edits = []; self.events = []; self.anchors = []; self.json_script = False
    def position(self):
        line, column = self.getpos(); return self.offsets[line - 1] + column
    def available(self, value):
        try: p = urlsplit(urljoin(self.base, value))
        except ValueError: return False
        return p.hostname == 'metaadvisor.eu' and unquote(p.path).lstrip('/') in self.present
    def replace_url(self, value, kind, attrs=None):
        key = url_key(value, self.base); target = None; reason = None
        if kind == 'link' and key in self.plan['links']:
            target = self.plan['links'][key]; reason = 'verified_link_target'
        elif kind == 'image' and (key in self.plan['images'] or key in self.plan['missing_images']):
            if self.available(value): return value
            if key in self.plan['images']:
                target = self.plan['images'][key]; reason = 'existing_image_path'
            else:
                fallback = None
                if attrs:
                    m = re.search(r'''this\.src\s*=\s*['"]([^'"]+)''', attrs.get('onerror', ''))
                    if m and self.available(m.group(1)): fallback = m.group(1)
                if not fallback:
                    fallback = self.plan['default_image'] if not attrs or 'post-hero-img' in attrs.get('class', '') else self.plan['card_fallback']
                target = fallback; reason = 'declared_image_fallback_missing_original'
            if not self.available(target): raise ValueError('Replacement image is absent: ' + target)
        if not target: return value
        old = urlsplit(html.unescape(value)); new = urlsplit(target)
        # Affiliate destination query parameters are copied verbatim from the source registry.
        query = new.query or old.query
        fragment = new.fragment or old.fragment
        if target.startswith('/') and old.scheme:
            target = DOMAIN + target; new = urlsplit(target)
        result = urlunsplit((new.scheme, new.netloc, new.path, query, fragment))
        if result != value: self.events.append({'old': key, 'target': result, 'reason': reason})
        return result
    def handle_starttag(self, tag, attrs):
        a = dict(attrs); raw = self.get_starttag_text(); pos = self.position(); edits = []
        disabled = tag == 'a' and a.get('href') and url_key(a['href'], self.base) in self.plan.get('disabled_links', [])
        if tag == 'a': self.anchors.append(bool(disabled))
        if tag == 'script': self.json_script = a.get('type', '').lower() == 'application/ld+json'
        for match in ATTR.finditer(raw, re.match(r'<\s*[^\s/>]+', raw).end()):
            name = match['name'].lower(); token = match['value']
            if disabled and name in ('href', 'target', 'rel', 'onclick', 'role', 'tabindex'):
                edits.append((match.start(), match.end(), '')); continue
            if not token: continue
            quote = token[0] if token[0] in ('"', "'") else '"'
            value = html.unescape(token[1:-1] if token[0] in ('"', "'") else token)
            if name=='onerror' and tag=='img':
                def repair_fallback(match):
                    return match.group(1)+self.replace_url(match.group(2),'image',{'class':a.get('class','')})+match.group(3)
                changed=re.sub(r'''(this\.src\s*=\s*['"])([^'"]+)(['"])''',repair_fallback,value)
                if changed!=value:edits.append((match.start('value'),match.end('value'),quote+html.escape(changed,quote=True)+quote))
            kind = None
            if name == 'href' and not (tag == 'link' and (a.get('rel') == 'canonical' or a.get('hreflang'))): kind = 'link'
            if name in ('src', 'poster') and tag != 'script': kind = 'image'
            if name=='href' and tag=='link' and a.get('rel') in ('icon','apple-touch-icon'): kind='image'
            if tag == 'meta' and name == 'content' and a.get('property', a.get('name', '')).lower() in ('og:image', 'og:image:url', 'og:image:secure_url', 'twitter:image', 'twitter:image:src'): kind = 'image'
            if kind:
                new = self.replace_url(value, kind, None if tag=='meta' else a)
                if new != value:
                    edits.append((match.start('value'), match.end('value'), quote + html.escape(new, quote=True) + quote))
        for start, end, value in sorted(edits, reverse=True): raw = raw[:start] + value + raw[end:]
        if disabled:
            raw = re.sub(r'^<a\b', '<span', raw, count=1, flags=re.I)
            raw = raw[:-1] + ' aria-disabled="true">'
            self.events.append({'old': url_key(a['href'], self.base), 'target': None, 'reason': 'disabled_confirmed_dead_affiliate_preserve_text'})
        if edits or disabled: self.edits.append((pos, pos + len(self.get_starttag_text()), raw))
    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag == 'a' and self.anchors: self.anchors.pop()
    def handle_endtag(self, tag):
        if tag == 'script': self.json_script = False
        if tag == 'a' and self.anchors and self.anchors.pop():
            pos = self.position(); end = self.text.find('>', pos) + 1
            self.edits.append((pos, end, '</span>'))
    def handle_data(self, data):
        if not self.json_script: return
        def patch(match):
            try: value = json.loads(match.group())
            except ValueError: return match.group()
            if not isinstance(value, str): return match.group()
            key = url_key(value, self.base)
            if key not in self.plan['images'] and key not in self.plan['missing_images']: return match.group()
            new = self.replace_url(value, 'image')
            return json.dumps(new, ensure_ascii=False).replace('<', '\\u003c').replace('>', '\\u003e') if new != value else match.group()
        new = JSON_STRING.sub(patch, data)
        if new != data:
            pos = self.position(); self.edits.append((pos, pos + len(data), new))
    def result(self):
        text = self.text; end_limit = len(text)
        for start, end, value in sorted(self.edits, reverse=True):
            if end > end_limit: raise ValueError('Overlapping HTML edits')
            text = text[:start] + value + text[end:]; end_limit = start
        return text

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--output', type=Path, required=True); ap.add_argument('--report', type=Path, required=True)
    ap.add_argument('--backup-dir',type=Path)
    args = ap.parse_args(); out = args.output.resolve()
    backup=args.backup_dir.resolve() if args.backup_dir else None
    if backup and (backup==out or out in backup.parents): raise SystemExit('Backup must be outside the published output')
    if not (out / 'sitemap.xml').is_file(): raise SystemExit('Expected a built output; refusing a source directory')
    plan = json.loads((ROOT / 'migration/verified-url-repairs.json').read_text(encoding='utf8'))
    paths = [p for p in out.rglob('*') if p.is_file()]; present = {p.relative_to(out).as_posix() for p in paths}
    def patch(p):
        if p.suffix != '.html': return None
        raw = p.read_bytes(); text = raw.decode('utf8')
        if not any(needle in text for needle in plan['prefilter']): return None
        rel = p.relative_to(out).as_posix(); head = Head(DOMAIN + '/' + rel.removesuffix('index.html'))
        head.feed(text[:text.lower().find('</head>') + 7]); parser = Repair(text, head.base, present, plan)
        parser.feed(text); parser.close(); result = parser.result()
        if result == text: return None
        if backup:
            original=backup/rel
            if original.exists(): raise ValueError('Refusing to overwrite an earlier HTML backup: '+str(original))
            original.parent.mkdir(parents=True,exist_ok=True);original.write_bytes(raw)
        p.write_bytes(result.encode('utf8'))
        return {'file': rel, 'events': parser.events, 'bytes_before': len(raw), 'bytes_after': len(result.encode('utf8'))}
    with ThreadPoolExecutor(max_workers=8) as pool: changed = [r for r in pool.map(patch, paths) if r]
    result = {'files_changed': len(changed), 'counts': dict(Counter(e['reason'] for r in changed for e in r['events'])),
              'files': changed, 'source_article_files_written': 0, 'redirects_activated': 0}
    args.report.parent.mkdir(parents=True, exist_ok=True); args.report.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf8')
    print(json.dumps({k:v for k,v in result.items() if k!='files'}, ensure_ascii=False))

if __name__ == '__main__': main()

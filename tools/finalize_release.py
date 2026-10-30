"""Output-only policy. Never edits sources or activates edge rules."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, urlunsplit, urljoin, unquote
import argparse, json, re, html, concurrent.futures, hashlib, os
ROOT = Path(__file__).resolve().parents[1]
DOMAIN = 'https://metaadvisor.eu'
ATTR = re.compile(r"""(?P<name>[\w:-]+)\s*=\s*(?P<q>["'])(?P<value>.*?)(?P=q)""")
class Policy(HTMLParser):
    def __init__(self, text, url, primary, mapping):
        super().__init__(convert_charrefs=False)
        self.text, self.url, self.primary, self.mapping = text, url, primary, mapping
        self.edits = []; self.robot = False; self.insert = None; self.scriptJSON = False
        self.offsets = [0] + [m.end() for m in re.finditer('\n', text)]
    def position(self):
        line, col = self.getpos()
        return self.offsets[line - 1] + col
    def mapped(self, value):
        try:
            u = urlsplit(urljoin(self.url, html.unescape(value)))
            if u.hostname != 'metaadvisor.eu': return value
            target = self.mapping.get(unquote(u.path))
            if not target: return value
            t = urlsplit(target if target.startswith('http') else DOMAIN + target)
            return urlunsplit((t.scheme, t.netloc, t.path, t.query or u.query, u.fragment))
        except ValueError:
            return value
    def handle_starttag(self, tag, attrs):
        a = dict(attrs); raw = self.get_starttag_text(); new = raw
        if tag == 'head': self.insert = self.position() + len(raw)
        if tag == 'script': self.scriptJSON = a.get('type') == 'application/ld+json'
        if tag == 'meta' and a.get('name', '').lower() in ('robots', 'googlebot'):
            self.robot = True
            if not self.primary: new = '<meta name="robots" content="noindex, follow">'
        if not self.primary and tag == 'link' and a.get('hreflang'): new = ''
        def fix(m):
            if m['name'].lower() not in ('href', 'src', 'poster', 'content'): return m[0]
            value = self.mapped(m['value'])
            if value == m['value']: return m[0]
            return m['name'] + '=' + m['q'] + html.escape(value, quote=True) + m['q']
        if new == raw: new = ATTR.sub(fix, new)
        if tag == 'script' and a.get('src') and any(x in a['src'] for x in ('googletagmanager.com', 'google-analytics.com', 'infolinks.com')):
            new = re.sub(r'\bsrc\s*=', 'data-ma-legacy-src=', new)
            new = re.sub(r"""\btype\s*=\s*(["']).*?\1""", '', new)
            new = new[:-1] + ' type="text/plain">'
        if tag == 'iframe' and a.get('src', '').startswith('https://ad.a-ads.com/'):
            new = new.replace('src=', 'data-ma-ad-src=', 1)
            new = new[:-1] + ' src="about:blank">'
        if new != raw: self.edits.append((self.position(), self.position() + len(raw), new))
    def handle_endtag(self, tag):
        if tag == 'script': self.scriptJSON = False
    def handle_data(self, data):
        if not self.scriptJSON: return
        def fix(m):
            try: value = json.loads(m[0])
            except ValueError: return m[0]
            new = self.mapped(value) if isinstance(value, str) else value
            return json.dumps(new, ensure_ascii=False).replace('<', '\\u003c') if new != value else m[0]
        new = re.sub(r'"(?:\\.|[^"\\])*"', fix, data)
        if new != data: self.edits.append((self.position(), self.position() + len(data), new))
    def result(self):
        if not self.primary and not self.robot:
            if self.insert is None: raise ValueError('Auxiliary HTML has no head: ' + self.url)
            self.edits.append((self.insert, self.insert, '<meta name="robots" content="noindex, follow">'))
        text = self.text; limit = len(text)
        for a, b, value in sorted(self.edits, reverse=True):
            if b > limit: raise ValueError('Overlapping final-policy edits')
            text = text[:a] + value + text[b:]; limit = a
        return text
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', type=Path, required=True)
    ap.add_argument('--report', type=Path, required=True)
    args = ap.parse_args(); out = args.output.resolve()
    if out == ROOT or ROOT in out.parents: raise SystemExit('Use an output outside the active repository')
    if not (out / 'sitemap.xml').is_file(): raise SystemExit('Expected Hugo output')
    expected = json.loads((ROOT / 'migration/expected-primary-pages.json').read_text(encoding='utf-8'))
    def file_key(url):
        parts=unquote(urlsplit(url).path).strip('/').split('/')
        if os.name=='nt': parts=[p.rstrip('. ') for p in parts]
        return '/'.join(parts)+'/index.html'
    primary_files = {file_key(r['url']) for r in expected}
    mapping = {unquote(urlsplit(u).path): t for u, t in json.loads((ROOT / 'data/article_routes.json').read_text(encoding='utf-8'))['aliases'].items()}
    mime = json.loads((ROOT / 'migration/bundle-mime-migrations.json').read_text(encoding='utf-8'))
    for x in mime: mapping[unquote(urlsplit(x['old_url']).path)] = x['new_url']
    def paths(directory):
        with os.scandir(directory) as entries:
            for entry in entries:
                if entry.is_dir(follow_symlinks=False): yield from paths(Path(entry.path))
                elif entry.is_file() and entry.name.endswith(('.html', '.json')): yield Path(entry.path)
    files = list(paths(out))
    def patch(p):
        rel = p.relative_to(out).as_posix(); raw = p.read_text(encoding='utf-8'); new = raw
        url = DOMAIN + '/' + rel.removesuffix('index.html')
        if p.suffix == '.html':
            parser = Policy(raw, url, rel in primary_files, mapping)
            parser.feed(raw); parser.close(); new = parser.result()
            if rel == '_backup/index.static.html':
                new = re.sub(r'(<time\b[^>]*>)(\d{4})-(\d{2})-(\d{2})(</time>)', lambda m: m[1] + m[4] + '.' + m[3] + '.' + m[2] + '.' + m[5], new)
        elif p.name == 'index.json':
            obj = json.loads(raw)
            def walk(x):
                if isinstance(x, str):
                    u = urlsplit(urljoin(url, x))
                    target = mapping.get(unquote(u.path)) if u.hostname == 'metaadvisor.eu' else None
                    return target if target else x
                if isinstance(x, list): return [walk(v) for v in x]
                if isinstance(x, dict): return {k: walk(v) for k, v in x.items()}
                return x
            changed = walk(obj)
            if changed != obj: new = json.dumps(changed, ensure_ascii=False, separators=(',', ':'))
        if new != raw:
            p.write_text(new, encoding='utf-8')
            return rel
        return None
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        changed = [x for x in pool.map(patch, files) if x]
    removed = []
    for x in mime:
        old = out / unquote(urlsplit(x['old_url']).path).lstrip('/')
        new = out / unquote(urlsplit(x['new_url']).path).lstrip('/')
        assert old.resolve().is_relative_to(out) and new.resolve().is_relative_to(out)
        assert new.is_file() and hashlib.sha256(new.read_bytes()).hexdigest() == x['sha256']
        if old.exists():
            assert hashlib.sha256(old.read_bytes()).hexdigest() == x['sha256']
            old.unlink(); removed.append(old.relative_to(out).as_posix())
    result = {'files_scanned': len(files), 'HTML_JSON_changed': len(changed), 'changed_files': changed, 'generated_wrong_extension_copies_removed': removed, 'original_source_images_removed': 0, 'source_files_written': 0, 'redirects_activated': 0}
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k != 'changed_files'}, ensure_ascii=False))
if __name__ == '__main__': main()

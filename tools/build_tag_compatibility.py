"""Post-build, meaningful noindex navigation; no redirect activation or empty 200s.

Only writes new files beneath an explicitly supplied output directory. Pending
legacy/empty/feed decisions deliberately block --release-check before any upload.
"""
import argparse
import collections
import concurrent.futures
import html
import json
import os
from pathlib import Path
import re
import time
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]

def read(name):
    return json.loads((ROOT / 'migration' / name).read_text(encoding='utf8'))

def path_for(url):
    raw = unquote(urlsplit(url).path)
    if urlsplit(url).netloc != 'metaadvisor.eu' or '\\' in raw:
        raise ValueError(url)
    parts = raw.strip('/').split('/')
    if any(p in ('', '.', '..') for p in parts): raise ValueError(url)
    return Path(*parts) / 'index.html'

def document(title, lang, canonical, articles, main_topic=''):
    assert articles, 'Never generate a content-free 200 page'
    text = {
        'hr': ('Članci povezani s oznakom', 'Sve vijesti', 'Objedinjena tema'),
        'de': ('Artikel zu diesem Schlagwort', 'Alle Nachrichten', 'Gemeinsames Thema'),
        'en': ('Articles associated with this tag', 'All news', 'Combined topic'),
    }[lang]
    esc = html.escape; prefix = '' if lang == 'en' else lang + '/'
    links = ''.join(f'<li><a href="{esc(a["url"], quote=True)}">{esc(a["title"])}</a></li>' for a in articles)
    topic = f'<p><a href="{esc(main_topic, quote=True)}">{text[2]}</a></p>' if main_topic else ''
    return (f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<meta name="robots" content="noindex,follow">'
        f'<title>{esc(title)} — MetaAdvisor</title><link rel="canonical" href="{esc(canonical, quote=True)}">'
        '<style>body{font:18px/1.6 system-ui,sans-serif;margin:0;background:#fafafa;color:#17212b}'
        'main{max-width:780px;margin:auto;padding:24px;overflow-wrap:anywhere}'
        'a{color:#125ca8}li{margin:14px 0}h1{line-height:1.2}nav{margin:24px 0}</style>'
        f'</head><body><main><a href="/{prefix}">MetaAdvisor</a><h1>{esc(title)}</h1>'
        f'<p>{text[0]}.</p>{topic}<ul>{links}</ul><nav><a href="/{prefix}news/">{text[1]}</a></nav>'
        '</main></body></html>').encode('utf8')

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--output', type=Path, required=True)
    ap.add_argument('--report', type=Path, required=True); ap.add_argument('--release-check', action='store_true')
    args = ap.parse_args(); out = args.output.resolve(); start = time.perf_counter()
    if args.release_check:
        import subprocess,sys
        subprocess.run([sys.executable,str(ROOT/'tools/check_release_readiness.py')],check=True)
    if not (out / 'sitemap.xml').is_file(): raise SystemExit('Expected an existing Hugo output, not a source directory')
    entries = read('tag-compatibility.json'); legacy = read('legacy-route-plan.json')
    byurl = {unquote(e['url']): e for e in entries}; jobs = []; pending = []; decisions = []; routes = set()
    for e in entries:
        if not e['articles']:
            pending.append({'url': e['url'], 'reason': 'EMPTY_LOCAL_TERM: retirement requires approval'})
            for feed in e['feed_routes']:
                decisions.append({'url':feed,'action':'FEED_RETIREMENT_REQUIRES_APPROVAL','proposed_301':'','activated':False})
                pending.append({'url':feed,'reason':'Feed transition not approved; no B/C RSS regenerated','proposed_301':''})
            continue
        for route in e['html_routes']:
            page = route['page']; members = e['articles'][(page - 1) * 96:page * 96]
            if not members: raise ValueError(f'Pagination has no verified members: {route["url"]}')
            jobs.append((route['url'], document(e['title'], e['language'], route['canonical'], members, e['proposed_301'])))
            decisions.append({'url': route['url'], 'action': 'NOINDEX_COMPAT', 'proposed_301': e['proposed_301'], 'activated': False})
        for feed in e['feed_routes']:
            target = e['proposed_301'] + 'index.xml' if e['proposed_301'] else ''
            decisions.append({'url': feed, 'action': 'DRAFT_FEED_301' if target else 'FEED_RETIREMENT_REQUIRES_APPROVAL', 'proposed_301': target, 'activated': False})
            pending.append({'url': feed, 'reason': 'Feed transition not approved; no B/C RSS regenerated', 'proposed_301': target})
    for e in legacy:
        decisions.append(e)
        if not e['emit_200']:
            pending.append({'url': e['url'], 'reason': e['action']}); continue
        target = byurl.get(unquote(e['proposed_301']))
        if not target or not target['articles']: raise ValueError('Legacy normalization target has no verified articles')
        # Windows normalizes trailing-dot components; production Linux must check them literally.
        rel = path_for(e['url'])
        if os.name == 'nt' and any(p.endswith(('.', ' ')) for p in rel.parts):
            pending.append({'url': e['url'], 'reason': 'WINDOWS_PATH_LIMITATION: literal trailing-dot route needs Linux QA'})
            continue
        title = unquote(urlsplit(e['url']).path.strip('/').split('/')[-1])
        jobs.append((e['url'], document(title, e['language'], e['url'], target['articles'], e['proposed_301'])))
    for url, data in jobs:
        rel = path_for(url); key = str(rel) if os.name != 'nt' else os.path.normcase(str(rel))
        if key in routes or (out / rel).exists(): raise ValueError(f'Collision; refusing overwrite: {url}')
        routes.add(key)
    for parent in sorted({(out/path_for(url)).parent for url,data in jobs},key=lambda p:(len(p.parts),str(p))):
        parent.mkdir(parents=True,exist_ok=True)
    def write(job):
        url, data = job; p = out / path_for(url); p.write_bytes(data)
        return {'url': url, 'file': p.relative_to(out).as_posix(), 'bytes': len(data)}
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool: emitted = list(pool.map(write, jobs))
    result = {'platform': os.name, 'files_added': len(emitted), 'bytes_added': sum(x['bytes'] for x in emitted),
        'seconds': time.perf_counter() - start, 'files': emitted, 'pending': pending,
        'pending_counts': dict(collections.Counter(x['reason'] for x in pending)), 'route_decisions': decisions,
        'redirects_activated': 0, 'BC_RSS_generated': 0, 'empty_200_generated': 0}
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf8')
    print(json.dumps({k: v for k, v in result.items() if k not in ('files', 'pending', 'route_decisions')}, ensure_ascii=False), flush=True)
    if args.release_check and pending:
        raise SystemExit('RELEASE BLOCKED: unresolved old-route/feed decisions; see report. No upload is authorized.')

if __name__ == '__main__': main()

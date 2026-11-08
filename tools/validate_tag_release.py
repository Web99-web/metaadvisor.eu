"""Validate generated release files without contacting production or Google."""
import argparse
import collections
import concurrent.futures
import csv
import hashlib
import json
import os
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urljoin, urlsplit
import xml.etree.ElementTree as ET
from release_articles import load_release_articles, article_membership_preserved

ROOT = Path(__file__).resolve().parents[1]
DOMAIN = 'https://metaadvisor.eu'

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--output', type=Path, required=True)
    ap.add_argument('--compat-report', type=Path, required=True); ap.add_argument('--report', type=Path, required=True)
    ap.add_argument('--require-linux', action='store_true')
    ap.add_argument('--baseline-unresolved', type=Path, help='Explicit saved unresolved pairs; only these exact pre-existing pairs are allowed')
    args = ap.parse_args()
    # lxml is installed in the local QA runtime; the Linux checklist installs the same dependency.
    from lxml import html
    out = args.output.resolve(); compat = json.loads(args.compat_report.read_text(encoding='utf8'))
    expected = load_release_articles(ROOT, out)
    compatibility_files = {x['file'] for x in compat['files']}
    compat_urls = {x['file']:x['url'] for x in compat['files']}
    route_canon = {unquote(r['url']):r['canonical'] for e in json.loads((ROOT/'migration/tag-compatibility.json').read_text(encoding='utf8')) for r in e['html_routes']}
    # Reuse directory-entry metadata instead of issuing two extra file stats per path.
    def inventory(directory):
        with os.scandir(directory) as entries:
            for entry in entries:
                if entry.is_dir(follow_symlinks=False): yield from inventory(Path(entry.path))
                elif entry.is_file(): yield {'path':Path(entry.path).relative_to(out).as_posix(),'bytes':entry.stat().st_size}
    manifest = list(inventory(out))
    present = {r['path'] for r in manifest}; errors = []; links = set(); assets = set(); heads = {}; cards = {}
    def physical(path):
        parts = unquote(path).strip('/').split('/')
        return '/'.join(p.rstrip('. ') if os.name == 'nt' else p for p in parts)
    def target_file(url):
        path = physical(urlsplit(url).path)
        if not path: return 'index.html'
        if path in present: return path
        return path.rstrip('/') + '/index.html'
    alias_targets={target_file(u):t for u,t in json.loads((ROOT/'data/article_routes.json').read_text(encoding='utf8'))['aliases'].items()}
    expected_files={target_file(r['url']) for r in expected}
    home_files = {'index.html', 'hr/index.html', 'de/index.html'}
    for rel in sorted(home_files - present): errors.append(['homepage missing',rel])
    def json_images(value):
        found=[]
        if isinstance(value,dict):
            for key,item in value.items():
                if key in ('image','thumbnailUrl','contentUrl','logo'):
                    if isinstance(item,str): found.append(item)
                    elif isinstance(item,list): found.extend(x for x in item if isinstance(x,str))
                    elif isinstance(item,dict): found.extend(item[k] for k in ('url','contentUrl') if isinstance(item.get(k),str))
                found.extend(json_images(item))
        elif isinstance(value,list):
            for item in value: found.extend(json_images(item))
        return found
    def parse(row):
        rel = row['path']; d = html.fromstring((out / rel).read_bytes())
        # Plain strings must not retain all parsed DOM trees in the release inventory.
        def xpath(expression): return d.xpath(expression,smart_strings=False)
        resources=xpath('//*[@src]/@src | //*[@poster]/@poster | //link[@href and not(@rel="canonical") and not(@hreflang)]/@href | //meta[@property="og:image" or @property="og:image:secure_url" or @name="twitter:image"]/@content')
        for srcset in xpath('//*[@srcset]/@srcset'):
            resources.extend(x.strip().split()[0] for x in srcset.split(',') if x.strip() and not x.strip().startswith('data:'))
        for script in xpath('//script[@type="application/ld+json"]/text()'):
            try: resources.extend(json_images(json.loads(script)))
            except (ValueError,TypeError): pass
        return (rel, xpath('//head/link[@rel="canonical"]/@href'),
            [(x.get('hreflang'), x.get('href')) for x in d.xpath('//head/link[@hreflang]')],
            xpath('//head/meta[@name="robots"]/@content'), d.get('lang'),
            xpath('//a[@href]/@href'), resources,
            bool(xpath('//meta[translate(@http-equiv,"REFSH","refsh")="refresh"]')),
            xpath('//h3[contains(concat(" ",normalize-space(@class)," ")," card-title ")]/a/@href'), [x.text_content().strip() for x in d.xpath('//time[@datetime]')], xpath('//script[@src]/@src'))
    htmlrows = [r for r in manifest if r['path'].endswith('.html')]
    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as pool:
        for i, result in enumerate(pool.map(parse, htmlrows), 1):
            rel, canon, alts, robots, lang, anchors, resource_links, alias, member_cards, visible_dates, scripts = result
            heads[rel] = {'canonical': canon, 'alternates': alts, 'robots': robots, 'lang': lang, 'alias': alias}
            if member_cards: cards[rel] = member_cards
            if rel in alias_targets:
                if len(canon)!=1 or unquote(canon[0])!=unquote(alias_targets[rel]): errors.append(['article alias canonical incorrect',rel,canon])
                if not any('noindex' in x for x in robots): errors.append(['article alias must be noindex',rel])
            noindex = any('noindex' in x for x in robots)
            if rel in home_files and noindex: errors.append(['homepage must be indexable',rel])
            if rel not in expected_files and rel not in home_files and not noindex: errors.append(['auxiliary HTML must be noindex',rel])
            if rel in expected_files:
                if scripts.count('/js/ma-consent.js')!=1: errors.append(['preferred article must have one consent controller',rel,scripts])
                if any('googletagmanager.com' in x for x in scripts): errors.append(['GA SDK must be consent-controlled, not eagerly loaded',rel])
            for value in visible_dates:
                if value and not re.fullmatch(r'\d{2}\.\d{2}\.\d{4}\.',value): errors.append(['reader date is not European format',rel,value])

            if rel in compatibility_files:
                if not any('noindex' in x for x in robots): errors.append(['compat missing noindex', rel])
                if alts: errors.append(['compat must not enter hreflang cluster', rel])
                planned = route_canon.get(unquote(compat_urls[rel]), compat_urls[rel])
                if len(canon)!=1 or unquote(canon[0])!=unquote(planned): errors.append(['compat canonical differs from route plan',rel])
            if not alias and rel != '_backup/index.static.html' and rel not in compatibility_files and rel not in alias_targets:
                if len(canon) != 1 or target_file(canon[0]) != rel:
                    errors.append(['canonical does not identify its page', rel, canon])
            base = canon[0] if canon else DOMAIN + '/' + rel.removesuffix('index.html')
            for values, bucket in ((anchors, links), (resource_links, assets)):
                for href in values:
                    if not href or href.startswith(('#', 'mailto:', 'tel:', 'javascript:', 'data:')): continue
                    dest = DOMAIN + href if href.startswith('/') and not href.startswith('//') else href if href.startswith(('http://', 'https://')) else urljoin(base, href)
                    parsed = urlsplit(dest)
                    if parsed.netloc != 'metaadvisor.eu': continue
                    if target_file(dest) not in present: bucket.add((rel, DOMAIN + parsed.path))
            if i % 3000 == 0: print('Checked HTML', i, flush=True)
    for rel,h in heads.items():
        for lang,target in h['alternates']:
            other=heads.get(target_file(target))
            if not other or (lang!='x-default' and other['lang']!=lang) or any('noindex' in x for x in other['robots']):
                errors.append(['HTML hreflang target absent/wrong language/noindex',rel,lang,target]);continue
            if len(other['canonical'])!=1 or unquote(other['canonical'][0])!=unquote(target):
                errors.append(['HTML hreflang target not canonical',rel,target])
    ns = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9', 'x': 'http://www.w3.org/1999/xhtml'}
    sitemap = {}; xml_alts = {}
    for lang in ('en', 'de', 'hr'):
        for node in ET.parse(out / lang / 'sitemap.xml').getroot():
            url = node.findtext('s:loc', namespaces=ns)
            if not url: continue
            if unquote(url) in sitemap: errors.append(['duplicate sitemap URL', url])
            sitemap[unquote(url)] = lang
            xml_alts[unquote(url)] = [(x.get('hreflang'), x.get('href')) for x in node.findall('x:link', ns)]
            for other_lang, target in xml_alts[unquote(url)]:
                if '/page/' in target: errors.append(['paginated sitemap alternate', url, target])
                h = heads.get(target_file(target), {})
                if not h or h.get('lang') != other_lang or any('noindex' in x for x in h.get('robots', [])):
                    errors.append(['invalid sitemap alternate target', url, other_lang, target])
            h = heads.get(target_file(url), {})
            if not h or any('noindex' in x for x in h.get('robots', [])): errors.append(['sitemap target absent/noindex', url])
            # x-default in HTML is an optional additional fallback, not a separate language.
            html_alts = {(l, unquote(u)) for l, u in h.get('alternates', []) if l != 'x-default'}
            if html_alts != {(l, unquote(u)) for l, u in xml_alts[unquote(url)]}:
                errors.append(['HTML/XML alternate cluster differs', url])
    for source, source_lang in sitemap.items():
        cluster=[(l,unquote(u)) for l,u in xml_alts[source]]
        if (source_lang,source) not in cluster: errors.append(['missing self hreflang',source])
        if len({l for l,u in cluster})!=len(cluster): errors.append(['duplicate hreflang language',source])
        for lang,target in cluster:
            peers={(l,unquote(u)) for l,u in xml_alts.get(target,[])}
            if (source_lang,source) not in peers: errors.append(['non-reciprocal hreflang',source,target])
    wanted = {unquote(x['url']) for x in expected}
    if set(sitemap) != wanted: errors.append(['sitemap scope changed', sorted(set(sitemap)-wanted)[:10], sorted(wanted-set(sitemap))[:10]])
    for row in expected:
        h = heads.get(target_file(row['url']))
        if not h: errors.append(['missing expected primary', row['url']]); continue
        if any('noindex' in x for x in h['robots']): errors.append(['primary unexpectedly noindex', row['url']])
    robots = (out / 'robots.txt').read_text(encoding='utf8')
    if 'Disallow: /tags' in robots or 'Allow: /' not in robots: errors.append(['robots prevents noindex crawling'])
    feeds = [p for p in present if re.match(r'^(?:(?:de|hr)/)?tags/', p) and p.endswith('index.xml')]
    bc = {unquote(x['url']) for x in json.loads((ROOT/'migration/tag-compatibility.json').read_text(encoding='utf8'))}
    for p in feeds:
        if unquote(DOMAIN+'/'+p.removesuffix('index.xml')) in bc: errors.append(['BC feed emitted', p])
    # Check complete A membership, including synonym unions and pagination, against the saved release model.
    inventory = ROOT/'migration/expected-A-memberships.json'
    historical_articles = {unquote(r['url']) for r in json.loads((ROOT/'migration/expected-primary-pages.json').read_text(encoding='utf8'))}
    new_articles = {unquote(r['url']) for r in expected} - historical_articles
    member_checks = 0
    for row in json.loads(inventory.read_text(encoding='utf8')):
        stem = target_file(row['url']).removesuffix('index.html'); got = set()
        for path, urls in cards.items():
            if path == stem+'index.html' or re.fullmatch(re.escape(stem)+r'page/\d+/index.html',path): got.update(unquote(urljoin(DOMAIN+'/',u)) for u in urls)
        want = set(map(unquote,row['shown_members']))
        if not article_membership_preserved(got, want, new_articles): errors.append(['A membership changed',row['url'],len(got),len(want)])
        member_checks += 1
    args.report.parent.mkdir(parents=True,exist_ok=True)
    for name, values in [('unresolved-anchors.csv',links),('unresolved-resources.csv',assets)]:
        with (args.report.parent/name).open('w',encoding='utf-8-sig',newline='') as f:
            w=csv.writer(f);w.writerow(['source_file','target']);w.writerows(sorted(values))
    baseline=json.loads(args.baseline_unresolved.read_text(encoding='utf8')) if args.baseline_unresolved else {}
    old_links={tuple(x) for x in baseline.get('anchors',[])};old_assets={tuple(x) for x in baseline.get('resources',[])}
    new_links=links-old_links;new_assets=assets-old_assets
    if new_links: errors.append(['unresolved internal anchor pairs',len(new_links)])
    if new_assets: errors.append(['unresolved internal resource pairs',len(new_assets)])
    result = {'platform':sys.platform,'linux_build_confirmed':sys.platform=='linux' and (args.report.parent/'linux-build.json').is_file(),'html_checked':len(htmlrows),'sitemap_primary_urls':len(sitemap),
        'expected_primary_present':sum(target_file(x['url']) in heads for x in expected),'category_terms':sum(bool(re.fullmatch(r'(?:(?:de|hr)/)?categories/[^/]+/index.html',p)) for p in heads),
        'A_memberships_checked':member_checks,'BC_RSS_generated':0,'compatibility_HTML':len(compatibility_files),
        'unresolved_anchor_pairs':len(links),'unresolved_resource_pairs':len(assets),'new_unresolved_anchor_pairs':len(new_links),'new_unresolved_resource_pairs':len(new_assets),'files':len(manifest),'bytes':sum(x['bytes'] for x in manifest),'errors':errors}
    args.report.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
    (args.report.parent/'file-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False),encoding='utf8')
    print(json.dumps({k:v for k,v in result.items() if k!='errors'},ensure_ascii=False),flush=True)
    print('Validation error count:',len(errors),flush=True)
    if errors: raise SystemExit('Output validation failed; see report')
    if args.require_linux and sys.platform != 'linux': raise SystemExit('Linux QA required; Windows result cannot satisfy it')

if __name__ == '__main__': main()

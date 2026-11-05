"""Notify changed public article URLs only, after the existing successful Pages deploy.

Default is a local dry run. --send is the only network submission switch.
Uses the last successful push deployment, not event.before (which misses skipped commits).
No sitemap-wide submissions, scheduler, third-party packages or private API keys.
"""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote, quote
import argparse, datetime, json, os, re, subprocess, urllib.request

HOST = 'metaadvisor.eu'
ORIGIN = 'https://' + HOST
ENDPOINT = 'https://api.indexnow.org/indexnow'
ARTICLE = re.compile(r'^content/(?:(hr|de)/)?news/(?:[^/]+/)*([^/]+)\.md$')

def git(*args):
    return subprocess.check_output(['git', *args])

def github(path):
    headers = {'Accept': 'application/vnd.github+json', 'User-Agent': 'MetaAdvisor-IndexNow'}
    token = os.environ.get('GITHUB_TOKEN')
    if token:
        headers['Authorization'] = 'Bearer ' + token
    url = 'https://api.github.com/repos/Web99-web/metaadvisor.eu' + path
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=20) as r:
        return json.load(r)

def previous_deploy():
    current = os.environ.get('GITHUB_RUN_ID', '')
    # Normally the first page suffices; fail closed rather than resubmit the whole site.
    for page in range(1, 6):
        rows = github('/actions/runs?branch=main&status=completed&per_page=100&page=' + str(page))['workflow_runs']
        for run in rows:
            if (str(run['id']) == current or run.get('path') != '.github/workflows/hugo.yml'
                    or run.get('event') != 'push' or run.get('conclusion') != 'success'):
                continue
            jobs = github('/actions/runs/' + str(run['id']) + '/jobs')['jobs']
            if any(j['name'] == 'deploy' and j.get('conclusion') == 'success' for j in jobs):
                return run['head_sha']
        if len(rows) < 100:
            break
    raise ValueError('No verified previous successful deployment; no bulk bootstrap allowed')

def blob(ref, path):
    # A missing side of an addition/deletion is expected, not an arbitrary read failure.
    exists = subprocess.run(['git', 'cat-file', '-e', ref + ':' + path], capture_output=True)
    if exists.returncode:
        return None
    return git('show', ref + ':' + path).decode('utf-8-sig')

def scalar(text, key, default=None):
    match = re.search(r'^' + re.escape(key) + r':\s*(.*?)\s*$', text, re.M)
    if not match:
        return default
    value = match[1]
    if value.startswith('"'):
        return json.loads(value)
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1].replace("''", "'")
    if value.lower() in ('true', 'false'):
        return value.lower() == 'true'
    if value in ('|', '>'):
        raise ValueError('Multiline route scalar requires review: ' + key)
    return value.split(' #', 1)[0].strip()

def source_url(path, text, aliases):
    match = ARTICLE.fullmatch(path)
    if not match or match[2] == '_index' or text is None:
        return None
    if not text.startswith('---'):
        raise ValueError('Unsupported article front matter: ' + path)
    fields = text.split('---', 2)[1]
    if scalar(fields, 'draft', False) is True:
        return None
    slug = scalar(fields, 'slug', match[2])
    if not isinstance(slug, str) or not slug or '/' in slug or slug in ('.', '..'):
        raise ValueError('Unsupported article slug: ' + path)
    prefix = '/' + match[1] if match[1] else ''
    route = scalar(fields, 'url', prefix + '/news/' + slug + '/')
    if not isinstance(route, str) or not route.startswith('/') or route.startswith('//'):
        raise ValueError('Unsupported article URL override: ' + path)
    url = ORIGIN + quote(route, safe='/%-._~')
    parts = urlsplit(url)
    if parts.netloc != HOST or parts.query or parts.fragment or '..' in unquote(parts.path).split('/'):
        raise ValueError('Unsafe article URL: ' + path)
    # Legacy aliases have their own canonical target and must not be promoted.
    return None if url in aliases else url

class Metadata(HTMLParser):
    def __init__(self):
        super().__init__(); self.canonicals = []; self.noindex = False
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'link' and 'canonical' in a.get('rel', '').split():
            self.canonicals.append(a.get('href'))
        if tag == 'meta' and a.get('name', '').lower() in ('robots', 'googlebot'):
            self.noindex |= 'noindex' in a.get('content', '').lower()

def is_public(public, url):
    route = unquote(urlsplit(url).path).lstrip('/')
    file = public / route / 'index.html' if route.endswith('/') else public / route
    if not file.resolve().is_relative_to(public.resolve()):
        raise ValueError('Output traversal')
    if not file.is_file():
        return False
    meta = Metadata(); meta.feed(file.read_text(encoding='utf-8'))
    return meta.canonicals == [url] and not meta.noindex

def collect(base, head, public):
    if not all(re.fullmatch(r'[a-f0-9]{40}', ref) for ref in (base, head)):
        raise ValueError('Exact commit SHAs required')
    aliases = {}
    for ref in (base, head):
        raw = blob(ref, 'data/article_routes.json')
        aliases[ref] = json.loads(raw)['aliases'] if raw else {}
    paths = git('diff', '--no-renames', '--name-only', '-z', base, head, '--', 'content').decode().split('\0')
    urls = set()
    for path in paths:
        if not ARTICLE.fullmatch(path):
            continue
        old = source_url(path, blob(base, path), aliases[base])
        new = source_url(path, blob(head, path), aliases[head])
        if new and is_public(public, new):
            urls.add(new)
        if old and (old != new or not new or not is_public(public, new)):
            urls.add(old)
    if len(urls) > 10000:
        raise ValueError('Unexpectedly large delta; manual review required')
    return sorted(urls)

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--public', type=Path, required=True)
    p.add_argument('--base')
    p.add_argument('--report', type=Path, required=True)
    p.add_argument('--send', action='store_true')
    args = p.parse_args()
    report = {'status': 'not-sent', 'deployment_already_completed': True}
    try:
        if args.send and (os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('GITHUB_EVENT_NAME') != 'push'):
            raise ValueError('Submission is restricted to the post-deploy push step')
        base = args.base or previous_deploy()
        if not re.fullmatch(r'[a-f0-9]{40}', base):
            raise ValueError('Invalid deployment baseline')
        if subprocess.run(['git', 'cat-file', '-e', base + '^{commit}'], capture_output=True).returncode:
            subprocess.run(['git', 'fetch', '--no-tags', '--depth=1', 'origin', base], check=True)
        head = git('rev-parse', 'HEAD').decode().strip()
        urls = collect(base, head, args.public)
        key = json.loads(Path('data/indexnow.json').read_text())['key']
        if not re.fullmatch(r'[a-f0-9]{32}', key):
            raise ValueError('Invalid shared IndexNow key')
        if (args.public / (key + '.txt')).read_text().strip() != key:
            raise ValueError('IndexNow key missing from verified deployment')
        payload = {'host': HOST, 'key': key, 'keyLocation': ORIGIN + '/' + key + '.txt', 'urlList': urls}
        report.update(base=base, head=head, urls=urls, count=len(urls), status='dry-run' if urls else 'no-changes')
        if args.send and urls:
            # One participating endpoint shares notifications with other participants.
            request = urllib.request.Request(ENDPOINT, data=json.dumps(payload).encode(),
                headers={'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'MetaAdvisor-IndexNow'})
            with urllib.request.urlopen(request, timeout=20) as response:
                report.update(http_status=response.status, status='accepted')
                if response.status not in (200, 202):
                    raise ValueError('Unexpected IndexNow response: ' + str(response.status))
    except Exception as error:
        report.update(status='failed', error=str(error))
        raise
    finally:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report))

if __name__ == '__main__':
    main()

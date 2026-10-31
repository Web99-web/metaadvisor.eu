"""Read-only URL-to-artifact validation; writes only its JSON report outside public."""
import argparse,json,sys
from pathlib import Path
from urllib.parse import urlsplit,unquote
ap=argparse.ArgumentParser();ap.add_argument('--repo',type=Path,required=True);ap.add_argument('--build-dir',type=Path,required=True);ap.add_argument('--require-linux',action='store_true');a=ap.parse_args();r=a.repo.resolve();d=a.build_dir.resolve();manifest=json.loads((d/'file-manifest.json').read_text(encoding='utf-8'));files={x['path'] for x in manifest};errors=[]
def exists(url):
 path=unquote(urlsplit(url).path).lstrip('/');return (path+'index.html' in files) if url.endswith('/') else (path in files or path+'/index.html' in files)
primary=json.loads((r/'migration/expected-primary-pages.json').read_text(encoding='utf-8'))
for x in primary:
 if not exists(x['url']):errors.append(['exact primary path missing',x['url']])
routes=json.loads((r/'migration/http-redirects.json').read_text(encoding='utf-8'))
for x in routes:
 if not exists(x['target']):errors.append(['exact redirect target missing',x['source'],x['target']])
legacy=['/de/tags/eu-inc./','/hr/tags/%C4%8Dlanak-50./','/hr/tags/eu-inc./','/tags/eu-inc./','/tags/%C4%8Dlanak-50./']
for path in legacy:
 if not exists('https://metaadvisor.eu'+path):errors.append(['exact legacy trailing-dot route missing',path])
if a.require_linux and sys.platform!='linux':errors.append(['actual Linux execution required',sys.platform])
result={'platform':sys.platform,'primary_checked':len(primary),'redirect_targets_checked':len(routes),'specific_legacy_paths_checked':len(legacy),'errors':errors,'exceptions':[],'production_changes':0};(d/'exact-url-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(result,ensure_ascii=False));raise SystemExit(2 if errors else 0)

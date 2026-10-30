"""Rebuild the last successful production commit on disposable Linux; never deploy."""
from pathlib import Path
import subprocess,os,sys,json,hashlib,tarfile,threading,http.server,urllib.request,xml.etree.ElementTree as ET
assert sys.platform=='linux'
sha='ec5206ea964d5ecad2e626465abe9dd8a9f80966';r=Path('rollback-source').resolve();out=Path(os.environ['RUNNER_TEMP'])/'verified-rollback';assert not out.exists();out.mkdir();public=out/'public'
def git(*args):return subprocess.check_output(['git','-C',str(r),*args])
assert git('rev-parse','HEAD').decode().strip()==sha
tree={}
for line in git('ls-tree','-r','-z','HEAD').split(b'\0'):
 if not line:continue
 meta,p=line.split(b'\t',1);mode,kind,digest=meta.decode().split()
 if kind=='blob':tree[p.decode()]=digest
def verify_source():
 for rel,digest in tree.items():
  p=r/rel;data=os.readlink(p).encode() if p.is_symlink() else p.read_bytes()
  assert hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==digest,rel
verify_source();assert len(tree)==10027
(out/'resource-overlay.toml').write_text('resourceDir = '+json.dumps(str(out/'resources'))+'\n')
cmd=['hugo','--source',str(r),'--config',str(r/'config.toml')+','+str(out/'resource-overlay.toml'),'--destination',str(public),'--cacheDir',str(out/'cache'),'--ignoreCache','--minify','--environment','production','--baseURL','https://metaadvisor.eu/','--clock','2026-10-22T21:17:50Z','--noBuildLock']
with (out/'hugo.log').open('w') as f:subprocess.run(cmd,check=True,stdout=f,stderr=subprocess.STDOUT,env={**os.environ,'GOMAXPROCS':'2'})
verify_source();assert not git('diff','--name-only')
for prefix in ('','de/','hr/'):
 assert (public/prefix/'index.html').is_file();assert (public/prefix/'news/index.html').is_file()
maps=list(public.glob('**/sitemap.xml'));assert maps
for p in maps:ET.parse(p)
class Handler(http.server.SimpleHTTPRequestHandler):
 def __init__(self,*a,**kw):super().__init__(*a,directory=str(public),**kw)
 def log_message(self,*a):pass
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),Handler);threading.Thread(target=server.serve_forever,daemon=True).start();http=[]
try:
 for path in ['/','/de/','/hr/','/news/','/de/news/','/hr/news/']:
  with urllib.request.urlopen('http://127.0.0.1:'+str(server.server_port)+path) as res:assert res.status==200 and res.headers.get_content_type()=='text/html';http.append({'path':path,'status':res.status,'MIME':res.headers.get_content_type()})
finally:server.shutdown();server.server_close()
rows=[]
for p in sorted(public.rglob('*')):
 if not p.is_file():continue
 assert not p.is_symlink() and p.stat().st_nlink==1
 with p.open('rb') as f:digest=hashlib.file_digest(f,'sha256').hexdigest()
 rows.append({'path':p.relative_to(public).as_posix(),'bytes':p.stat().st_size,'sha256':digest})
archive=out/'rollback-site.tar.gz'
with tarfile.open(archive,'w:gz',format=tarfile.GNU_FORMAT) as t:
 for row in rows:t.add(public/row['path'],arcname='./'+row['path'],recursive=False)
expected={x['path']:x for x in rows};seen=set()
with tarfile.open(archive,'r:gz') as t:
 for member in t:
  assert member.isfile();rel=member.name.removeprefix('./');row=expected[rel];assert member.size==row['bytes'];f=t.extractfile(member);assert hashlib.file_digest(f,'sha256').hexdigest()==row['sha256'];seen.add(rel)
assert seen==set(expected)
with archive.open('rb') as f:archive_sha=hashlib.file_digest(f,'sha256').hexdigest()
result={'PASS':True,'platform':sys.platform,'source_commit':sha,'source_blobs_verified_before_and_after':len(tree),'Hugo_version':subprocess.check_output(['hugo','version'],text=True).strip(),'build_clock_UTC':'2026-10-22T21:17:50Z','HTTP_tests':http,'sitemap_XML_files_parsed':len(maps),'web_files':len(rows),'web_bytes':sum(x['bytes'] for x in rows),'archive_bytes':archive.stat().st_size,'archive_sha256':archive_sha,'archive_entries_hash_verified':len(seen),'production_deploy_executed':False,'scope':'Reproducible rebuild of previous deployed source, not byte-identity with expired original Pages artifact; preserves previous SEO behavior rather than applying new SEO fixes.'}
(out/'ROLLBACK-RESULT.json').write_text(json.dumps(result,indent=2));(out/'file-manifest.json').write_text(json.dumps(rows));print(json.dumps(result),flush=True)

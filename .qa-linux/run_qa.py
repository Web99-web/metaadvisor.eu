from pathlib import Path
import sys,os,json,subprocess,datetime,tarfile,hashlib
r=Path.cwd();q=r/'.qa-linux';d=Path(os.environ['MA_QA_OUTPUT']).resolve();assert sys.platform=='linux';assert not d.exists();assert not d.is_relative_to(r);d.mkdir(parents=True)
wrapper='import concurrent.futures,runpy,sys; Original=concurrent.futures.ThreadPoolExecutor\nclass Limited(Original):\n def __init__(self,max_workers=None,*a,**k): super().__init__(max_workers=min(max_workers or 2,2),*a,**k)\nconcurrent.futures.ThreadPoolExecutor=Limited\nsys.argv=sys.argv[1:];runpy.run_path(sys.argv[0],run_name="__main__")'
results=[]
def run(name,cmd):
 with (d/(name+'.log')).open('w',encoding='utf-8') as f:p=subprocess.run(cmd,stdout=f,stderr=subprocess.STDOUT)
 results.append({'name':name,'returncode':p.returncode});(d/'qa-state.json').write_text(json.dumps({'actual_platform':sys.platform,'commit':os.environ.get('GITHUB_SHA'),'results':results,'deployment':False},indent=2));print(name,p.returncode,flush=True)
 if p.returncode:raise SystemExit(p.returncode)
def py(name,file,*args):run(name,[sys.executable,'-u','-B','-c',wrapper,str(file),*map(str,args)])
py('source-before',q/'verify_snapshot.py','--repo',r,'--report',d/'source-before.json')
index=subprocess.check_output(['git','ls-files','--stage','-z']);version=subprocess.check_output(['hugo','version'],text=True);assert 'v0.128.0' in version and 'extended' in version and 'linux' in version
py('migration-gate-unit',r/'tools/test_migration_gate.py')
py('controls',r/'tools/prepare_tag_archives.py','--check')
run('consent-unit',['node',str(q/'test-memory.cjs')])
(d/'resource-overlay.toml').write_text('resourceDir = '+json.dumps(str(d/'resources'))+'\n',encoding='utf-8');manifest=json.loads((q/'source-manifest.json').read_text(encoding='utf-8'))
run('hugo',['hugo','--source',str(r),'--config',str(r/'config.toml')+','+str(d/'resource-overlay.toml'),'--destination',str(d/'public'),'--cacheDir',str(d/'cache'),'--ignoreCache','--minify','--environment','production','--baseURL','https://metaadvisor.eu/','--clock',manifest['captured_at_UTC']])
(d/'linux-build.json').write_text(json.dumps({'platform':sys.platform,'hugo_version':version.strip(),'returncode':0,'deployment':False}),encoding='utf-8')
py('repairs',r/'tools/repair_verified_urls.py','--output',d/'public','--report',d/'repairs.json')
# QA intentionally reports pending publication decisions; it never authorizes a release.
py('compatibility',r/'tools/build_tag_compatibility.py','--output',d/'public','--report',d/'compatibility.json')
py('final-policy',r/'tools/finalize_release.py','--output',d/'public','--report',d/'final-policy.json')
py('validate',r/'tools/validate_tag_release.py','--output',d/'public','--compat-report',d/'compatibility.json','--report',d/'validation.json','--require-linux')
py('exact-paths',q/'verify_exact_paths.py','--repo',r,'--build-dir',d,'--require-linux')
py('http-MIME',q/'http_qa.py')
py('source-after',q/'verify_snapshot.py','--repo',r,'--report',d/'source-after.json')
assert index==subprocess.check_output(['git','ls-files','--stage','-z'])
rows=json.loads((d/'file-manifest.json').read_text(encoding='utf-8'));archive=d/'qa-site.tar.gz'
with tarfile.open(archive,'w:gz',format=tarfile.GNU_FORMAT) as tar:
 for row in rows:
  p=d/'public'/row['path'];assert not p.is_symlink() and p.stat().st_nlink==1;tar.add(p,arcname='./'+row['path'],recursive=False)
with archive.open('rb') as f:sha=hashlib.file_digest(f,'sha256').hexdigest()
(d/'QA-PACKAGE.json').write_text(json.dumps({'file':archive.name,'bytes':archive.stat().st_size,'sha256':sha,'files':len(rows),'actual_platform':sys.platform,'source_commit':os.environ.get('GITHUB_SHA'),'deployment':False,'production_approval_changed':False},indent=2));print('Linux QA complete. No deploy.',flush=True)

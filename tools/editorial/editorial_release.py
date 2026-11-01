"""Unactivated candidate engine. Reuses existing critical validators unchanged."""
from pathlib import Path
import argparse,concurrent.futures,hashlib,json,os,subprocess,sys,time,datetime
from release_policy import mode_for_changes
WRAPPER='import concurrent.futures,runpy,sys;Original=concurrent.futures.ThreadPoolExecutor\nclass Limited(Original):\n def __init__(self,max_workers=None,*a,**k):super().__init__(max_workers=min(max_workers or 2,2),*a,**k)\nconcurrent.futures.ThreadPoolExecutor=Limited\nsys.argv=sys.argv[1:];from pathlib import Path;sys.path.insert(0,str(Path(sys.argv[0]).resolve().parent));runpy.run_path(sys.argv[0],run_name="__main__")'
CRITICAL=('release-readiness','source-before','migration-gate-unit','approved-route-tests','controls','consent-unit','hugo','repairs','compatibility','final-policy','stable-generated-anchors','stylesheet-cache-key','validate','exact-paths','http-MIME','native-migration-gate','article-search','article-search-worker','future-article-guards','source-inventory','source-after')
def save(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def execute(root,out,context,mode='AUTO'):
 assert sys.platform=='linux','Actual Linux required'
 root=Path(root).resolve();out=Path(out).resolve();assert not out.exists() and not out.is_relative_to(root)
 baseline=dict(context['full_baseline'])
 finished=datetime.datetime.fromisoformat(baseline['finished_at_utc'].replace('Z','+00:00'))
 assert finished.tzinfo is not None
 baseline['age_hours']=(datetime.datetime.now(datetime.timezone.utc)-finished).total_seconds()/3600
 selected=mode_for_changes(context['changes'],baseline)
 if mode=='FAST' and selected!='FAST':raise ValueError('FAST forbidden: '+selected)
 selected='FULL' if mode=='FULL' else selected
 if selected=='BLOCKED':raise ValueError('Newer FULL failure blocks publication')
 env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','GIT_OPTIONAL_LOCKS':'0','GOMAXPROCS':'2','MA_QA_OUTPUT':str(out)}
 if selected=='FULL':
  # The exact already-tested FULL reference is retained, including the second fixture build.
  ref=root/'.qa-linux/bench/full_reference_runner.py'
  assert hashlib.sha256(ref.read_bytes()).hexdigest()==context['full_reference_runner_sha256']
  return subprocess.run([sys.executable,'-u','-B',str(ref)],cwd=root,env=env,check=True)
 out.mkdir(parents=True);results=[];start=time.perf_counter()
 index=subprocess.check_output(['git','ls-files','--stage','-z'],cwd=root)
 q=root/'.qa-linux'
 def run(name,args):
  begin=time.perf_counter();resource=out/(name+'.resources.txt')
  with (out/(name+'.log')).open('w',encoding='utf-8') as log:
   p=subprocess.run(['/usr/bin/time','-v','-o',str(resource),*map(str,args)],cwd=root,env=env,stdout=log,stderr=subprocess.STDOUT)
  row={'name':name,'returncode':p.returncode,'seconds':round(time.perf_counter()-begin,3)}
  for line in resource.read_text(encoding='utf-8').splitlines():
   if 'Maximum resident set size (kbytes)' in line:row['peak_RSS_KiB']=int(line.rsplit(':',1)[1])
   if 'User time (seconds)' in line:row['user_CPU_seconds']=float(line.rsplit(':',1)[1])
   if 'System time (seconds)' in line:row['system_CPU_seconds']=float(line.rsplit(':',1)[1])
  results.append(row);save(out/'fast-state.json',{'mode':'FAST','results':results,'deployment':False})
  print(name,p.returncode,row['seconds'],flush=True)
  if p.returncode:raise RuntimeError(name+' failed; no deploy')
 def py(name,file,*args):run(name,[sys.executable,'-u','-B','-c',WRAPPER,file,*args])
 py('release-readiness',root/'tools/check_release_readiness.py')
 py('source-before',q/'verify_snapshot.py','--repo',root,'--report',out/'source-before.json')
 for path,digest in context['protected_files'].items():assert hashlib.sha256((root/path).read_bytes()).hexdigest()==digest,'Protected code/policy changed: '+path
 py('migration-gate-unit',root/'tools/test_migration_gate.py');py('approved-route-tests',q/'test_approved_routes.py');py('controls',root/'tools/prepare_tag_archives.py','--check');run('consent-unit',['node',q/'test-memory.cjs'])
 (out/'resources.toml').write_text('resourceDir = '+json.dumps(str(out/'resources'))+'\n',encoding='utf-8')
 # Always a complete build into a fresh directory. A cache hit cannot skip it.
 run('hugo',['hugo','--source',root,'--config',str(root/'config.toml')+','+str(out/'resources.toml'),'--destination',out/'public','--cacheDir',env.get('HUGO_CACHEDIR',str(out/'cache')),'--minify','--environment','production','--baseURL','https://metaadvisor.eu/','--clock',context['clock']])
 save(out/'linux-build.json',{'platform':sys.platform,'returncode':0,'deployment':False})
 py('repairs',root/'tools/repair_verified_urls.py','--output',out/'public','--report',out/'repairs.json')
 py('compatibility',root/'tools/build_tag_compatibility.py','--output',out/'public','--report',out/'compatibility.json','--release-check')
 py('final-policy',root/'tools/finalize_release.py','--output',out/'public','--report',out/'final-policy.json')
 py('stable-generated-anchors',q/'bench/stable_generated_anchors.py','--output',out/'public','--report',out/'stable-generated-anchors.json')
 py('stylesheet-cache-key',q/'bench/stable_stylesheet.py','--output',out/'public','--report',out/'stylesheet-cache-key.json')
 py('validate',root/'tools/validate_tag_release.py','--output',out/'public','--compat-report',out/'compatibility.json','--report',out/'validation.json','--require-linux')
 py('exact-paths',q/'verify_exact_paths.py','--repo',root,'--build-dir',out,'--require-linux');py('http-MIME',q/'http_qa.py');py('native-migration-gate',q/'verify_native_gate.py')
 run('article-search',['node',q/'test-search.cjs']);run('article-search-worker',['node',q/'test-search-worker.cjs']);py('future-article-guards',q/'test-article-guards.py')
 # Independent source inventory is checked even in FAST; only synthetic second build moves to FULL.
 py('source-inventory',q/'bench/check_source_inventory.py',root,out,context['clock'])
 py('source-after',q/'verify_snapshot.py','--repo',root,'--report',out/'source-after.json')
 assert index==subprocess.check_output(['git','ls-files','--stage','-z'],cwd=root)
 assert tuple(r['name'] for r in results)==CRITICAL and all(r['returncode']==0 for r in results)
 receipt={'status':'PASS','linux':True,'mode':'FAST','commit':context['production_commit'],'tree':context['production_tree'],'policy_fingerprint':context['policy_fingerprint'],'all_critical_checks_passed':True,'source_changed':False,'seconds':round(time.perf_counter()-start,3),'results':results,'deployment':False}
 save(out/'release-receipt.json',receipt)
 return receipt
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--source',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--context',type=Path,required=True);ap.add_argument('--mode',choices=('AUTO','FAST','FULL'),default='AUTO');a=ap.parse_args();execute(a.source,a.output,json.loads(a.context.read_text(encoding='utf-8')),a.mode)

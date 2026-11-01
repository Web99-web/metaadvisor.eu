"""Sequential Linux FULL and FAST, identical application bytes and clock; no deploy."""
from pathlib import Path
import sys,os,json,hashlib,subprocess,time,tarfile
r=Path.cwd();q=r/'.qa-linux/bench';base=Path(os.environ['MA_QA_OUTPUT']);assert sys.platform=='linux' and not base.exists();base.mkdir(parents=True);sys.path.insert(0,str(q))
from editorial_release import execute
from release_policy import verify_artifact
def save(name,v):(base/name).write_text(json.dumps(v,ensure_ascii=False,indent=2),encoding='utf-8')
context=json.loads((q/'benchmark-context.json').read_text(encoding='utf-8'))
for name in ('test_release_policy.py','test_stable_stylesheet.py'):
 with (base/(name+'.log')).open('w',encoding='utf-8') as log:subprocess.run([sys.executable,'-B',str(q/name)],stdout=log,stderr=subprocess.STDOUT,check=True)
start=time.perf_counter();execute(r,base/'full',context,'FULL');full_seconds=round(time.perf_counter()-start,3)
save('PAIR-PROGRESS.json',{'FULL':'PASS','FULL_seconds_including_archive':full_seconds,'FAST':'PENDING','activation':False})
start=time.perf_counter();receipt=execute(r,base/'fast',context,'FAST');fast_seconds=round(time.perf_counter()-start,3)
def manifest(folder):return [{'path':p.relative_to(folder).as_posix(),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(folder.rglob('*')) if p.is_file()]
full=manifest(base/'full/public');fast=manifest(base/'fast/public');fa={x['path']:x for x in full};fb={x['path']:x for x in fast}
missing=sorted(set(fa)-set(fb));extra=sorted(set(fb)-set(fa));different=[p for p in fa.keys()&fb.keys() if fa[p]!=fb[p]]
result={'FULL':'PASS','FAST':'PASS','FULL_seconds_including_ordinary_QA_archive':full_seconds,'FAST_seconds_before_archive':fast_seconds,'same_clock':context['clock'],'same_application_commit':context['production_commit'],'FULL_files':len(full),'FAST_files':len(fast),'changed_files':sorted(different),'missing_files':missing,'extra_files':extra,'exact_byte_equivalence':not(different or missing or extra),'critical_validators_unchanged':True,'templates_and_articles_unchanged':True,'activation':False,'production_modified':False}
save('PAIRED-COMPARISON.json',result);save('paired-verified-manifest.json',fast)
for mode in ('full','fast'):
 for name in ('validation.json','NATIVE-MIGRATION-GATE.json','stylesheet-cache-key.json','source-inventory.json','fast-state.json','FUTURE-ARTICLES-LINUX.json','qa-state.json'):
  p=base/mode/name
  if p.is_file():(base/(mode+'-'+name)).write_bytes(p.read_bytes())
assert result['exact_byte_equivalence'],{'different':different[:20],'missing':missing[:20],'extra':extra[:20]}
verify_artifact(base/'fast/public',fast)
archive=base/'qa-site.tar.gz';start=time.perf_counter()
with tarfile.open(archive,'w:gz',format=tarfile.GNU_FORMAT) as tar:
 for row in fast:tar.add(base/'fast/public'/row['path'],arcname='./'+row['path'],recursive=False)
result['FAST_archive_seconds']=round(time.perf_counter()-start,3);save('PAIRED-COMPARISON.json',result)
print(json.dumps(result),flush=True)

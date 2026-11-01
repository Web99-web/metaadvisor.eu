"""Isolated QA benchmark only; compare FAST to the successful FULL artifact."""
from pathlib import Path
import sys,os,json,hashlib,subprocess,time,tarfile,difflib
r=Path.cwd();q=r/'.qa-linux/bench';base=Path(os.environ['MA_QA_OUTPUT']);assert sys.platform=='linux' and not base.exists();base.mkdir(parents=True)
start=time.perf_counter();sys.path.insert(0,str(q))
from editorial_release import execute
from release_policy import verify_receipt,verify_artifact
context=json.loads((q/'benchmark-context.json').read_text(encoding='utf-8'))
with (base/'policy-tests.log').open('w',encoding='utf-8') as f:subprocess.run([sys.executable,'-B',str(q/'test_release_policy.py')],stdout=f,stderr=subprocess.STDOUT,check=True)
receipt=execute(r,base/'fast',context,'FAST')
public=base/'fast/public';expected=json.loads((q/'full-file-hashes.json').read_text(encoding='utf-8'))
rows=[];differences=[]
for p in sorted(public.rglob('*')):
 if not p.is_file():continue
 rel=p.relative_to(public).as_posix();digest=hashlib.sha256(p.read_bytes()).hexdigest();rows.append({'path':rel,'bytes':p.stat().st_size,'sha256':digest})
 if expected.get(rel)!=digest:differences.append(rel)
found={x['path'] for x in rows};missing=sorted(set(expected)-found);extra=sorted(found-set(expected))
comparison={'FAST_checks':'PASS','FULL_reference_run':41291038170,'same_application_commit':context['production_commit'],'expected_files':len(expected),'actual_files':len(rows),'changed_files':differences,'missing_files':missing,'extra_files':extra,'exact_byte_equivalence':not(differences or missing or extra),'FAST_pipeline_seconds':receipt['seconds'],'activation':False,'production_modified':False,'policy_tests':'PASS'}
(base/'COMPARISON.json').write_text(json.dumps(comparison,ensure_ascii=False,indent=2),encoding='utf-8')
samples=json.loads((q/'full-html-samples.json').read_text(encoding='utf-8'))
diagnostics={}
for name,old in samples.items():
 new=(public/name).read_text(encoding='utf-8')
 if old!=new:
  matcher=difflib.SequenceMatcher(None,old,new,autojunk=False)
  diagnostics[name]=[{'old':old[i:j][:2000],'new':new[k:l][:2000]} for op,i,j,k,l in matcher.get_opcodes() if op!='equal'][:12]
(base/'HTML-DIFFERENCES.json').write_text(json.dumps(diagnostics,ensure_ascii=False,indent=2),encoding='utf-8')
for name in ('validation.json','NATIVE-MIGRATION-GATE.json','source-inventory.json','fast-state.json'):
 p=base/'fast'/name
 if p.is_file():(base/('fast-'+name)).write_bytes(p.read_bytes())
assert comparison['exact_byte_equivalence'],{'changed':differences[:20],'missing':missing[:20],'extra':extra[:20]}
manifest=base/'verified-file-manifest.json';manifest.write_text(json.dumps(rows,ensure_ascii=False),encoding='utf-8');receipt['file_manifest_sha256']=hashlib.sha256(manifest.read_bytes()).hexdigest();(base/'release-receipt.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
verify_receipt(receipt,{k:receipt[k] for k in ('commit','tree','policy_fingerprint','file_manifest_sha256')});verify_artifact(public,rows)
# Use the ordinary existing QA artifact upload, never Pages. No production workflow changes.
archive=base/'qa-site.tar.gz';begin=time.perf_counter()
with tarfile.open(archive,'w:gz',format=tarfile.GNU_FORMAT) as tar:
 for row in rows:tar.add(public/row['path'],arcname='./'+row['path'],recursive=False)
comparison.update(archive_seconds=round(time.perf_counter()-begin,3),benchmark_seconds=round(time.perf_counter()-start,3),verified_files=len(rows));(base/'COMPARISON.json').write_text(json.dumps(comparison,ensure_ascii=False,indent=2),encoding='utf-8')
for name in ('validation.json','native-migration-gate.log','NATIVE-MIGRATION-GATE.json','source-inventory.json','fast-state.json'):
 p=base/'fast'/name
 if p.is_file():(base/('fast-'+name)).write_bytes(p.read_bytes())
print(json.dumps(comparison,ensure_ascii=True),flush=True)

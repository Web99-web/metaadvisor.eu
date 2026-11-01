"""Pre-push Linux FULL test of the exact activation commit and artifact transport."""
from pathlib import Path
import os,sys,json,subprocess,hashlib,shutil
r=Path.cwd();q=r/'.qa-linux';out=Path(os.environ['MA_QA_OUTPUT']);assert sys.platform=='linux' and not out.exists();out.mkdir(parents=True)
plan=json.loads((q/'activation-plan.json').read_text(encoding='utf-8'));source=out/'application';source.mkdir()
def git(*a,data=None):return subprocess.check_output(['git','-C',str(source),*a],input=data)
subprocess.run(['git','init','--quiet',str(source)],check=True)
objects=(r/'.git/objects').resolve();(source/'.git/objects/info/alternates').write_bytes((str(objects)+'\n').encode())
index=[]
for name,row in plan['application_files'].items():
 raw=(r/name).read_bytes();assert hashlib.sha256(raw).hexdigest()==row['sha256'];p=source/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(raw);index.append((row['mode']+' '+row['git_blob']+'\t'+name+'\n').encode())
git('update-index','--index-info',data=b''.join(index));tree=git('write-tree').decode().strip();assert tree==plan['production_tree']
commit=git('hash-object','-t','commit','-w','--stdin',data=(q/'activation-commit-object.txt').read_bytes()).decode().strip();assert commit==plan['production_commit'];git('update-ref','refs/heads/snapshot',commit);git('symbolic-ref','HEAD','refs/heads/snapshot')
tools=source/'tools/editorial';sys.path.insert(0,str(tools))
from workflow_driver import plan as make_plan,build,verify_bundle,digest
from publication_layout import check_new_paths
from artifact_bundle import unpack
for test in ('test_release_policy.py','test_stable_stylesheet.py','test_artifact_bundle.py','test_workflow_driver.py'):
 with (out/(test+'.log')).open('w',encoding='utf-8') as log:subprocess.run([sys.executable,'-B',str(tools/test)],cwd=source,stdout=log,stderr=subprocess.STDOUT,check=True)
checked=check_new_paths(source,plan['changes']);assert set(checked)==set(x['to'] for x in plan['moves'])
context=out/'context.json';value=make_plan(source,'','workflow_dispatch','FULL',context);value['clock']=plan['comparison_clock'];context.write_text(json.dumps(value),encoding='utf-8')
result=build(source,out/'isolated-source',out/'build',context);assert result['mode']=='FULL' and result['status']=='PASS'
manifest=json.loads((out/'build/verified-file-manifest.json').read_text(encoding='utf-8'));actual={x['path']:x['sha256'] for x in manifest};expected=json.loads((q/'activation-expected-hashes.json').read_text(encoding='utf-8'))
differences=sorted(p for p in actual.keys()&expected.keys() if actual[p]!=expected[p]);missing=sorted(set(expected)-set(actual));extra=sorted(set(actual)-set(expected))
comparison={'PASS':not(differences or missing or extra),'production_commit':commit,'tree':tree,'files':len(actual),'changed_files':differences,'missing_files':missing,'extra_files':extra,'six_moves_byte_exact':True,'date_layout':'PASS','all_previous_public_output_identical':not(differences or missing or extra),'activation_not_pushed_yet':True}
(out/'ACTIVATION-PRE-PUSH.json').write_text(json.dumps(comparison,ensure_ascii=False,indent=2),encoding='utf-8');assert comparison['PASS']
# Round-trip the actual archive with exactly the production deploy verifier.
bundle=out/'transport';bundle.mkdir()
for name in ('qa-site.tar.gz','verified-file-manifest.json','release-receipt.json'):shutil.copy2(out/'build'/name,bundle/name)
import workflow_driver
original_api=workflow_driver.api
def main_fixture(path):
 assert path=='/git/ref/heads/main';return {'object':{'sha':commit}}
workflow_driver.api=main_fixture
try:verify_bundle(source,bundle,context,digest(bundle/'release-receipt.json'))
finally:workflow_driver.api=original_api
comparison['archive_roundtrip_and_exact_deploy_verifier']='PASS';(out/'ACTIVATION-PRE-PUSH.json').write_text(json.dumps(comparison,ensure_ascii=False,indent=2),encoding='utf-8')
for name in ('validation.json','NATIVE-MIGRATION-GATE.json','FUTURE-ARTICLES-LINUX.json','qa-state.json','release-receipt.json','verified-file-manifest.json','full-proof.json'):
 p=out/'build'/name
 if p.exists():shutil.copy2(p,out/name)
shutil.copy2(out/'build/qa-site.tar.gz',out/'qa-site.tar.gz')
print(json.dumps(comparison),flush=True)

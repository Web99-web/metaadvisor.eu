"""Candidate workflow control plane. Not installed or activated in production."""
from pathlib import Path
import argparse,base64,datetime,hashlib,io,json,os,shutil,subprocess,sys,urllib.request,urllib.error,zipfile
from release_policy import ARTICLE,IMAGE,mode_for_changes,verify_receipt,verify_artifact
from publication_layout import check_new_paths
from artifact_bundle import create as create_bundle,unpack as unpack_bundle
HERE=Path(__file__).resolve().parent
REPOSITORY='Web99-web/metaadvisor.eu'
def save(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def git(root,*args):return subprocess.check_output(['git','-C',str(root),*args])
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def api(path):
 assert path.startswith('/')
 headers={'Accept':'application/vnd.github+json','User-Agent':'MetaAdvisor-editorial-CI'}
 if os.environ.get('GITHUB_TOKEN'):headers['Authorization']='Bearer '+os.environ['GITHUB_TOKEN']
 with urllib.request.urlopen(urllib.request.Request('https://api.github.com/repos/'+REPOSITORY+path,headers=headers),timeout=40) as r:return json.load(r)
class NoRedirect(urllib.request.HTTPRedirectHandler):
 def redirect_request(self,*a,**k):return None
def proof_file(artifact):
 headers={'User-Agent':'MetaAdvisor-editorial-CI','Accept':'application/vnd.github+json'}
 if os.environ.get('GITHUB_TOKEN'):headers['Authorization']='Bearer '+os.environ['GITHUB_TOKEN']
 request=urllib.request.Request(artifact['archive_download_url'],headers=headers)
 try:
  with urllib.request.build_opener(NoRedirect).open(request,timeout=40) as r:data=r.read(10485761)
 except urllib.error.HTTPError as e:
  if e.code not in (301,302,303,307):raise
  url=e.headers['Location'];e.close();assert url.startswith('https://')
  # Never forward GitHub authentication to artifact storage.
  with urllib.request.urlopen(url,timeout=40) as r:data=r.read(10485761)
 assert len(data)<=10485760
 if artifact.get('digest'):assert 'sha256:'+hashlib.sha256(data).hexdigest()==artifact['digest']
 with zipfile.ZipFile(io.BytesIO(data)) as z:
  names=[n for n in z.namelist() if Path(n).name=='full-proof.json'];assert len(names)==1
  info=z.getinfo(names[0]);assert info.file_size<=1048576
  return json.loads(z.read(names[0]))
def recent_runs():
 """Read additional pages only when the existing proof is not on the first page."""
 for page in range(1,11):
  batch=api('/actions/runs?branch=main&per_page=100&page='+str(page))['workflow_runs']
  yield from batch
  if len(batch)<100:return
def latest_full(fingerprint):
 """Only successful same-repository main workflow receipts may authorize FAST."""
 empty={'success':False,'protected_fingerprint_matches':False,'age_hours':1e9,'finished_at_utc':'1970-01-01T00:00:00+00:00','newer_matching_full_failed':False}
 try:
  # Include interrupted FULL runs; do not lose the proof after 30 article pushes.
  newer_failure=False
  for run in recent_runs():
   if run.get('path')!='.github/workflows/hugo.yml' or run.get('head_branch')!='main':continue
   if str(run['id'])==os.environ.get('GITHUB_RUN_ID'):continue
   if run.get('conclusion')!='success':
    jobs=api('/actions/runs/'+str(run['id'])+'/jobs')['jobs']
    if run.get('event') in ('workflow_dispatch','schedule') or any(j['name'].startswith('FULL') and j.get('conclusion')!='success' for j in jobs):newer_failure=True
    continue
   artifacts=api('/actions/runs/'+str(run['id'])+'/artifacts')['artifacts']
   for a in artifacts:
    if a.get('expired') or a['name']!='editorial-full-proof-'+run['head_sha']:continue
    p=proof_file(a)
    if not (p.get('status')=='PASS' and p.get('mode')=='FULL' and p.get('linux') is True and p.get('all_critical_checks_passed') is True and p.get('source_changed') is False and p.get('commit')==run['head_sha'] and p.get('run_id')==run['id'] and p.get('policy_fingerprint')==fingerprint):continue
    finished=datetime.datetime.fromisoformat(p['finished_at_utc'].replace('Z','+00:00'));assert finished.tzinfo
    age=(datetime.datetime.now(datetime.timezone.utc)-finished).total_seconds()/3600
    return {'success':True,'protected_fingerprint_matches':True,'age_hours':age,'finished_at_utc':p['finished_at_utc'],'newer_matching_full_failed':newer_failure,'run_id':run['id']}
 except (OSError,ValueError,KeyError,AssertionError):pass
 return empty
def application_files(root):
 rows={}
 for row in git(root,'ls-tree','-rz','--full-tree','HEAD').split(b'\0'):
  if not row:continue
  header,path=row.split(b'\t',1);mode,kind,sha=header.decode().split();name=path.decode('utf-8')
  if kind!='blob' or mode not in ('100644','100755'):raise ValueError('Unsupported source object: '+name)
  p=root/name;assert p.is_file() and not p.is_symlink();b=p.read_bytes()
  assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha,'Working source differs from Git tree: '+name
  rows[name]={'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
 return rows
def plan(root,base,event,requested,output):
 root=root.resolve();files=application_files(root);protected={p:v['sha256'] for p,v in files.items() if not ARTICLE.fullmatch(p) and not IMAGE.fullmatch(p)};fingerprint=hashlib.sha256(json.dumps(protected,sort_keys=True).encode()).hexdigest()
 changes=[]
 if event=='push':
  try:
   assert len(base)==40 and all(c in '0123456789abcdef' for c in base)
   try:git(root,'cat-file','-e',base+'^{commit}')
   except subprocess.CalledProcessError:git(root,'fetch','--no-tags','--depth=1','origin',base)
   changes=[{'status':s,'path':p} for s,p in (x.split('\t',1) for x in git(root,'diff','--no-renames','--name-status',base,'HEAD').decode('utf-8').splitlines())]
  except (AssertionError,ValueError,subprocess.CalledProcessError):raise ValueError('Cannot verify exact changed files; refuse release')
 baseline=latest_full(fingerprint) if event=='push' and requested!='FULL' else {'success':False,'protected_fingerprint_matches':False,'finished_at_utc':'1970-01-01T00:00:00+00:00','age_hours':1e9}
 selected='FULL' if requested=='FULL' or event!='push' else mode_for_changes(changes,baseline)
 layout_checked=check_new_paths(root,changes)
 value={'clock':datetime.datetime.now(datetime.timezone.utc).isoformat(),'changes':changes,'full_baseline':baseline,'protected_files':protected,'policy_fingerprint':fingerprint,'production_commit':git(root,'rev-parse','HEAD').decode().strip(),'production_tree':git(root,'rev-parse','HEAD^{tree}').decode().strip(),'application_files':files,'selected_mode':selected,'publish':event=='push','repository':REPOSITORY}
 save(output,value)
 if os.environ.get('GITHUB_OUTPUT'):
  with open(os.environ['GITHUB_OUTPUT'],'a',encoding='utf-8') as f:f.write('mode='+selected+'\npublish='+str(value['publish']).lower()+'\n')
 if selected=='BLOCKED':raise ValueError('A newer failed FULL blocks FAST; a successful FULL is required')
 return value
def snapshot(root,target,context):
 assert not target.exists() and not target.resolve().is_relative_to(root.resolve());target.mkdir(parents=True)
 for rel,row in context['application_files'].items():
  p=root/rel;assert digest(p)==row['sha256'];dest=target/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest)
 git_dir=Path(git(root,'rev-parse','--git-path','objects').decode().strip());git_dir=git_dir if git_dir.is_absolute() else root/git_dir
 subprocess.run(['git','init','--quiet',str(target)],check=True)
 (target/'.git/objects/info/alternates').write_bytes((str(git_dir.resolve())+'\n').encode())
 git(target,'read-tree',context['production_commit']);git(target,'update-ref','refs/heads/snapshot',context['production_commit']);git(target,'symbolic-ref','HEAD','refs/heads/snapshot')
 qa=target/'.qa-linux';shutil.copytree(HERE/'qa-tests',qa)
 test=qa/'tools/test_migration_gate.py';dest=target/'tools/test_migration_gate.py'
 if dest.exists():assert digest(dest)==digest(test),'Fixture/tool drift requires review'
 else:dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(test,dest)
 (qa/'bench').mkdir(exist_ok=True)
 for name in ('check_source_inventory.py','stable_stylesheet.py','stable_generated_anchors.py','legacy-generated-anchors.json'):shutil.copy2(HERE/name,qa/'bench'/name)
 extras=[p.relative_to(target).as_posix() for p in qa.rglob('*') if p.is_file()]
 if 'tools/test_migration_gate.py' not in context['application_files']:extras.append('tools/test_migration_gate.py')
 extras+=['.qa-linux/source-manifest.json','.qa-linux/source-approval.json']
 save(qa/'source-manifest.json',{'captured_at_UTC':context['clock'],'source_files':context['application_files'],'extra_allowed':sorted(set(extras))})
 (qa/'source-approval.json').write_bytes((target/'migration/release-approvals.json').read_bytes())
 context['full_reference_runner_sha256']=digest(qa/'bench/full_reference_runner.py')
 return target
def build(root,source,out,context_file):
 context=json.loads(context_file.read_text(encoding='utf-8'));assert git(root,'rev-parse','HEAD').decode().strip()==context['production_commit']
 subprocess.run([sys.executable,'-B',str(root/'tools/check_release_readiness.py')],cwd=root,check=True)
 work=snapshot(root,source,context)
 from editorial_release import execute
 result=execute(work,out,context,context['selected_mode'])
 subprocess.run([sys.executable,'-B',str(work/'tools/check_release_readiness.py')],cwd=work,check=True)
 if context['selected_mode']=='FULL':
  assert json.loads((out/'FUTURE-ARTICLES-LINUX.json').read_text())['PASS']
  assert not json.loads((out/'validation.json').read_text())['errors']
  result={'status':'PASS','linux':True,'mode':'FULL','commit':context['production_commit'],'tree':context['production_tree'],'policy_fingerprint':context['policy_fingerprint'],'all_critical_checks_passed':True,'source_changed':False}
 rows=[]
 for p in sorted((out/'public').rglob('*')):
  if p.is_symlink():raise ValueError('Artifact symlink')
  if p.is_file():
   if p.stat().st_nlink!=1:raise ValueError('Artifact hardlink')
   rows.append({'path':p.relative_to(out/'public').as_posix(),'bytes':p.stat().st_size,'sha256':digest(p)})
 save(out/'verified-file-manifest.json',rows);result.update(file_manifest_sha256=digest(out/'verified-file-manifest.json'),finished_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),run_id=int(os.environ['GITHUB_RUN_ID']))
 result['site_archive_sha256']=create_bundle(out/'public',rows,out/'qa-site.tar.gz')
 save(out/'release-receipt.json',result)
 if result['mode']=='FULL':save(out/'full-proof.json',result)
 if os.environ.get('GITHUB_OUTPUT'):
  with open(os.environ['GITHUB_OUTPUT'],'a') as f:f.write('receipt_sha256='+digest(out/'release-receipt.json')+'\n')
 return result
def verify_bundle(root,bundle,context_file,receipt_hash):
 context=json.loads(context_file.read_text(encoding='utf-8'));receipt=json.loads((bundle/'release-receipt.json').read_text(encoding='utf-8'));manifest=bundle/'verified-file-manifest.json'
 assert digest(bundle/'release-receipt.json')==receipt_hash and digest(manifest)==receipt['file_manifest_sha256']
 verify_receipt(receipt,{'commit':context['production_commit'],'tree':context['production_tree'],'policy_fingerprint':context['policy_fingerprint'],'file_manifest_sha256':digest(manifest)})
 if receipt['mode']=='FAST':assert mode_for_changes(context['changes'],latest_full(context['policy_fingerprint']))=='FAST','FULL proof must still be current and valid before deployment'
 current=api('/git/ref/heads/main')['object']['sha'];assert current==context['production_commit'],'Main advanced; refuse stale deployment'
 rows=json.loads(manifest.read_text(encoding='utf-8'))
 unpack_bundle(bundle/'qa-site.tar.gz',bundle/'public',rows,receipt['site_archive_sha256'])
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('command',choices=('plan','build','verify-bundle'));p.add_argument('--root',type=Path,default=Path.cwd());p.add_argument('--base',default='');p.add_argument('--event',default='push');p.add_argument('--requested',default='AUTO',choices=('AUTO','FULL'));p.add_argument('--context',type=Path,required=True);p.add_argument('--source',type=Path);p.add_argument('--output',type=Path);p.add_argument('--bundle',type=Path);p.add_argument('--receipt-hash');a=p.parse_args()
 if a.command=='plan':plan(a.root,a.base,a.event,a.requested,a.context)
 elif a.command=='build':build(a.root,a.source,a.output,a.context)
 else:verify_bundle(a.root,a.bundle,a.context,a.receipt_hash)

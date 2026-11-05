"""Integration checks for candidate source isolation and deployment refusals."""
from pathlib import Path
import hashlib,json,os,shutil,subprocess,sys,tempfile,unittest
from unittest.mock import patch
import workflow_driver as d
G='C:/Users/User/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/git/cmd/git.exe'
if Path(G).exists():os.environ['PATH']=str(Path(G).parent)+os.pathsep+os.environ['PATH']
BASE=Path(os.environ.get('RUNNER_TEMP',str(Path(__file__).resolve().parent/'test-temp'))).resolve();BASE.mkdir(parents=True,exist_ok=True)
GOOD={'success':True,'protected_fingerprint_matches':True,'age_hours':1,'newer_matching_full_failed':False,'finished_at_utc':'2026-11-01T09:10:42+00:00'}
class DriverTests(unittest.TestCase):
 def setUp(self):
  self.temp=Path(tempfile.mkdtemp(prefix='driver-',dir=BASE)).resolve();self.assertTrue(self.temp.is_relative_to(BASE));self.root=self.temp/'repo';self.root.mkdir()
  subprocess.run(['git','init','--quiet',str(self.root)],check=True);d.git(self.root,'config','core.autocrlf','false')
  for name,value in {'config.toml':'baseURL="https://metaadvisor.eu/"\n','migration/release-approvals.json':'{}','content/news/old.md':'old'}.items():
   p=self.root/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(value.encode())
  self.commit();self.base=d.git(self.root,'rev-parse','HEAD').decode().strip()
  new=self.root/'content/news/2026/11/01/new.md';new.parent.mkdir(parents=True);new.write_bytes(b'---\nslug: "new"\ndate: "2026-11-01T07:00:00Z"\n---\nnew');self.commit()
 def tearDown(self):
  self.assertTrue(self.temp.resolve().is_relative_to(BASE))
  def remove_readonly(fn,path,error):
   self.assertTrue(Path(path).resolve().is_relative_to(self.temp));os.chmod(path,0o700);fn(path)
  shutil.rmtree(self.temp,onexc=remove_readonly)
 def commit(self):
  d.git(self.root,'add','.');d.git(self.root,'-c','user.name=Local QA','-c','user.email=qa@example.invalid','commit','--quiet','-m','fixture')
 def plan(self,baseline=GOOD,event='push'):
  with patch.object(d,'latest_full',return_value=baseline):return d.plan(self.root,self.base,event,'AUTO',self.temp/'context.json')
 def test_new_article_fast_and_isolated_snapshot(self):
  context=self.plan();self.assertEqual(context['selected_mode'],'FAST');snapshot=d.snapshot(self.root,self.temp/'snapshot',context)
  subprocess.run([sys.executable,'-B',str(snapshot/'.qa-linux/verify_snapshot.py'),'--repo',str(snapshot),'--report',str(self.temp/'snapshot-check.json')],check=True,capture_output=True)
  self.assertFalse((self.root/'.qa-linux').exists());self.assertEqual(d.git(snapshot,'rev-parse','HEAD'),d.git(self.root,'rev-parse','HEAD'))
  self.assertTrue((snapshot/'.qa-linux/future-fixtures.json').exists());self.assertTrue((snapshot/'.qa-linux/special-urls.json').exists())
 def test_changed_source_rejected(self):
  (self.root/'config.toml').write_text('unreviewed',encoding='utf-8')
  with self.assertRaises(AssertionError):d.application_files(self.root)
 def test_stale_baseline_full(self):self.assertEqual(self.plan({**GOOD,'age_hours':2400})['selected_mode'],'FAST')
 def test_newer_full_failure_blocks(self):
  self.assertEqual(self.plan({**GOOD,'newer_matching_full_failed':True})['selected_mode'],'FULL')
 def test_scheduled_full_never_publishes(self):
  c=self.plan(event='schedule');self.assertEqual(c['selected_mode'],'FULL');self.assertFalse(c['publish'])
 def test_bundle_requires_current_full_proof(self):
  c=self.plan();bundle=self.temp/'bundle';(bundle/'public').mkdir(parents=True);d.save(bundle/'verified-file-manifest.json',[])
  receipt={k:c[k] for k in ('policy_fingerprint',)};receipt.update(commit=c['production_commit'],tree=c['production_tree'],file_manifest_sha256=d.digest(bundle/'verified-file-manifest.json'),mode='FAST',status='PASS',linux=True,all_critical_checks_passed=True,source_changed=False)
  d.save(bundle/'release-receipt.json',receipt)
  with patch.object(d,'latest_full',return_value={'success':False}):
   with self.assertRaises(AssertionError):d.verify_bundle(self.root,bundle,self.temp/'context.json',d.digest(bundle/'release-receipt.json'))
 def test_bundle_refuses_advanced_main(self):
  c=self.plan();bundle=self.temp/'bundle';(bundle/'public').mkdir(parents=True);d.save(bundle/'verified-file-manifest.json',[])
  receipt=dict(commit=c['production_commit'],tree=c['production_tree'],policy_fingerprint=c['policy_fingerprint'],file_manifest_sha256=d.digest(bundle/'verified-file-manifest.json'),mode='FULL',status='PASS',linux=True,all_critical_checks_passed=True,source_changed=False);d.save(bundle/'release-receipt.json',receipt)
  with patch.object(d,'api',return_value={'object':{'sha':'different'}}):
   with self.assertRaises(AssertionError):d.verify_bundle(self.root,bundle,self.temp/'context.json',d.digest(bundle/'release-receipt.json'))
if __name__=='__main__':unittest.main()

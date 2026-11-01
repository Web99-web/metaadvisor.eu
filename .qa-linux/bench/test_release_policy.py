import copy,tempfile,unittest,hashlib,os,contextlib
from pathlib import Path
from release_policy import mode_for_changes,verify_receipt,verify_artifact
FULL={'success':True,'protected_fingerprint_matches':True,'age_hours':1,'newer_matching_full_failed':False}
GOOD=[{'path':'content/news/article.md','status':'A'},{'path':'content/hr/news/clanak.md','status':'A'},{'path':'content/de/news/artikel.md','status':'A'},{'path':'static/images/editorial/cover.png','status':'A'}]
TEMP_ROOT=Path(os.environ.get('RUNNER_TEMP',str(Path(__file__).resolve().parent/'test-temp')))/'metaadvisor-policy-tests'
@contextlib.contextmanager
def test_directory():
 TEMP_ROOT.mkdir(parents=True,exist_ok=True)
 with tempfile.TemporaryDirectory(dir=TEMP_ROOT) as t:
  assert Path(t).resolve().is_relative_to(TEMP_ROOT.resolve())
  yield t
class Policy(unittest.TestCase):
 def test_articles(self):self.assertEqual(mode_for_changes(GOOD,FULL),'FAST')
 def test_batch(self):self.assertEqual(mode_for_changes([{'path':x['path'].replace('.md',str(i)+'.md').replace('.png',str(i)+'.png'),'status':'A'} for i in range(10) for x in GOOD],FULL),'FAST')
 def test_duplicate_changes(self):self.assertEqual(mode_for_changes(GOOD+GOOD,FULL),'FULL')
 def test_protected(self):
  for p in ('layouts/a.html','tools/a.py','data/tag_policy.json','migration/x.json','config.toml','.github/workflows/hugo.yml','i18n/hr.yaml'):
   with self.subTest(path=p):self.assertEqual(mode_for_changes([{'path':p,'status':'M'}],FULL),'FULL')
 def test_unknown_image(self):self.assertEqual(mode_for_changes([{'path':'static/images/evil.js','status':'A'}],FULL),'FULL')
 def test_delete_or_edit(self):
  for status in ('D','M','R100'):
   self.assertEqual(mode_for_changes([{'path':'content/news/article.md','status':status}],FULL),'FULL')
 def test_traversal(self):self.assertEqual(mode_for_changes([{'path':'content/news/../x.md','status':'A'}],FULL),'FULL')
 def test_stale(self):self.assertEqual(mode_for_changes(GOOD,{**FULL,'age_hours':25}),'FULL')
 def test_failed(self):self.assertEqual(mode_for_changes(GOOD,{**FULL,'success':False}),'FULL')
 def test_newer_failure(self):self.assertEqual(mode_for_changes(GOOD,{**FULL,'newer_matching_full_failed':True}),'BLOCKED')
 def test_policy_change(self):self.assertEqual(mode_for_changes(GOOD,{**FULL,'protected_fingerprint_matches':False}),'FULL')
 def test_section_file(self):self.assertEqual(mode_for_changes([{'path':'content/news/_index.md','status':'A'}],FULL),'FULL')
 def test_receipt(self):
  expected=dict(commit='a',tree='b',policy_fingerprint='c',file_manifest_sha256='d');receipt={**expected,'status':'PASS','linux':True,'all_critical_checks_passed':True,'source_changed':False}
  self.assertTrue(verify_receipt(receipt,expected))
  for k in expected:
   with self.assertRaises(ValueError):verify_receipt({**receipt,k:'wrong'},expected)
  for change in ({'linux':False},{'status':'FAIL'},{'all_critical_checks_passed':False},{'source_changed':True}):
   with self.assertRaises(ValueError):verify_receipt({**receipt,**change},expected)
 def test_tampered_artifact(self):
  with test_directory() as t:
   p=Path(t)/'index.html';p.write_bytes(b'approved');rows=[{'path':'index.html','bytes':8,'sha256':hashlib.sha256(b'approved').hexdigest()}];self.assertTrue(verify_artifact(t,rows));p.write_bytes(b'tampered')
   with self.assertRaises(ValueError):verify_artifact(t,rows)
 def test_extra_or_missing(self):
  with test_directory() as t:
   rows=[{'path':'index.html','bytes':0,'sha256':hashlib.sha256(b'').hexdigest()}]
   with self.assertRaises(ValueError):verify_artifact(t,rows)
   (Path(t)/'extra').write_bytes(b'')
   with self.assertRaises(ValueError):verify_artifact(t,[])
if __name__=='__main__':unittest.main()

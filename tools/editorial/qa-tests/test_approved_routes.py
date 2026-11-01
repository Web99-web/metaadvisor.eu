from pathlib import Path
import sys,json,tempfile,hashlib,unittest,os
W=Path.cwd();sys.path.insert(0,str(W/'tools'))
from migration_gate import resolve_pending,require_resolved,key,document,windows_literal_limit

class ApprovedTests(unittest.TestCase):
 def setUp(self):
  self.t=tempfile.TemporaryDirectory(dir=Path(os.environ['RUNNER_TEMP']));self.r=Path(self.t.name);(self.r/'migration').mkdir();self.out=self.r/'out';self.out.mkdir();self.url='https://metaadvisor.eu/tags/old/';self.article='https://metaadvisor.eu/news/one/';self.topic='https://metaadvisor.eu/de/tags/topic/'
  rows=[{'source':'https://metaadvisor.eu/tags/b%C3%B6rse/index.xml','target':self.topic+'index.xml','status':301}];raw=json.dumps(rows).encode();(self.r/'migration/http-redirects.json').write_bytes(raw)
  for rel,data in [('tag-compatibility.json',[]),('legacy-route-plan.json',[]),('expected-primary-pages.json',[{'url':self.article}])]:(self.r/'migration'/rel).write_text(json.dumps(data))
  self.p={'schema':2,'http_plan_sha256':hashlib.sha256(raw).hexdigest(),'input_sha256':{str(p.relative_to(self.r)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in (self.r/'migration').glob('*.json') if p.name!='http-redirects.json'},'resolutions':{self.url:{'action':'APPROVED_404','status':404}}};self.save()
 def tearDown(self):self.t.cleanup()
 def save(self):(self.r/'migration/approved-route-resolutions.json').write_text(json.dumps(self.p))
 def test_approved_404_absent(self):self.assertEqual(len(resolve_pending(self.r,self.out,[{'url':self.url}])[1]),1)
 def test_404_present_file_fails(self):
  p=self.out/'tags/old/index.html';p.parent.mkdir(parents=True);p.write_text('still here')
  with self.assertRaises(ValueError):resolve_pending(self.r,self.out,[{'url':self.url}])
 def test_article_cannot_be_retired(self):
  self.p['resolutions']={self.article:{'action':'APPROVED_404','status':404}};self.save()
  with self.assertRaises(ValueError):resolve_pending(self.r,self.out,[{'url':self.article}])
 def test_unicode_redirect_uses_exact_encoding(self):
  p=self.out/'de/tags/topic/index.xml';p.parent.mkdir(parents=True);p.write_text('feed');self.p['resolutions']={'https://metaadvisor.eu/tags/börse/index.xml':{'action':'APPROVED_SPECIFIC_301','target':self.topic+'index.xml'}};self.save();self.assertEqual(len(resolve_pending(self.r,self.out,[{'url':'https://metaadvisor.eu/tags/b%C3%B6rse/index.xml'}])[1]),1)
 def test_input_fingerprint_fails_closed(self):
  (self.r/'migration/legacy-route-plan.json').write_text('[1]')
  with self.assertRaises(ValueError):resolve_pending(self.r,self.out,[{'url':self.url}])
 def test_unknown_stays_blocked(self):
  pending,_=resolve_pending(self.r,self.out,[{'url':'https://metaadvisor.eu/tags/unknown/'}])
  with self.assertRaises(SystemExit):require_resolved(pending)
 def test_schema2_rejects_wildcard(self):
  self.p['resolutions']={'*':{'action':'APPROVED_404','status':404}};self.save()
  with self.assertRaises(ValueError):resolve_pending(self.r,self.out,[{'url':self.url}])
 def test_empty_compat_fails(self):
  with self.assertRaises(ValueError):document(self.url,{'language':'en','title':'old','themes':[]})
 def test_dot_url_is_not_the_dotless_url(self):
  dot='https://metaadvisor.eu/tags/old./';self.assertNotEqual(key(dot),key(self.url));self.assertTrue(windows_literal_limit(dot));self.assertFalse(windows_literal_limit(self.url))
 @unittest.skipUnless(os.name=='nt','Windows-specific physical path ambiguity')
 def test_windows_never_accepts_normalized_dot_file_as_literal(self):
  dot='https://metaadvisor.eu/tags/old./';d={'action':'APPROVED_NOINDEX_COMPAT','language':'en','title':'old','themes':[{'url':self.topic,'language':'de','title':'Topic','articles':[{'url':self.article,'title':'Article'}]}]};self.p['resolutions']={dot:d};self.save();p=self.out/'tags/old/index.html';p.parent.mkdir(parents=True);p.write_bytes(document(dot,d));pending,resolved=resolve_pending(self.r,self.out,[{'url':dot}]);self.assertFalse(resolved);self.assertEqual(len(pending),1);self.assertTrue(pending[0]['reason'].startswith('WINDOWS_PATH_LIMITATION'));self.assertEqual(p.read_bytes(),document(dot,d))
 def test_compat_requires_actual_approved_bytes_and_links(self):
  d={'action':'APPROVED_NOINDEX_COMPAT','language':'en','title':'old','themes':[{'url':self.topic,'language':'de','title':'Topic','articles':[{'url':self.article,'title':'Article'}]}]};self.p['resolutions']={self.url:d};self.save()
  for path in ['de/tags/topic/index.html','news/one/index.html']:
   p=self.out/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text('real existing content')
  p=self.out/'tags/old/index.html';p.parent.mkdir(parents=True);p.write_bytes(document(self.url,d));self.assertEqual(len(resolve_pending(self.r,self.out,[{'url':self.url}])[1]),1);p.write_text('<html>empty</html>')
  with self.assertRaises(ValueError):resolve_pending(self.r,self.out,[{'url':self.url}])
if __name__=='__main__':unittest.main()

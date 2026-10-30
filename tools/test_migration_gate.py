import unittest,tempfile,json,hashlib
from pathlib import Path
from migration_gate import resolve_pending

class GateTests(unittest.TestCase):
 def setUp(self):
  self.t=tempfile.TemporaryDirectory();self.r=Path(self.t.name);(self.r/'migration').mkdir();self.out=self.r/'out';(self.out/'tags/topic').mkdir(parents=True);(self.out/'tags/topic/index.html').write_text('real content')
  self.source='https://metaadvisor.eu/tags/old/';self.target='https://metaadvisor.eu/tags/topic/';self.row={'source':self.source,'target':self.target,'status':301};self.pending=[{'url':self.source,'reason':'review'},{'url':'https://metaadvisor.eu/tags/unknown/','reason':'review'}];self.write()
 def tearDown(self):self.t.cleanup()
 def write(self,action='APPROVED_SPECIFIC_301'):
  raw=json.dumps([self.row]).encode();(self.r/'migration/http-redirects.json').write_bytes(raw);self.policy={'schema':1,'http_plan_sha256':hashlib.sha256(raw).hexdigest(),'resolutions':{self.source:{'action':action,'target':self.target}}};self.save()
 def save(self):(self.r/'migration/approved-route-resolutions.json').write_text(json.dumps(self.policy))
 def test_exact_and_unknown(self):
  pending,resolved=resolve_pending(self.r,self.out,self.pending);self.assertEqual(len(pending),1);self.assertEqual(len(resolved),1)
 def test_no_blanket_waiver(self):
  self.policy['resolutions']={'*':{'action':'APPROVED_SPECIFIC_301','target':self.target}};self.save();self.assertEqual(len(resolve_pending(self.r,self.out,self.pending)[0]),2)
 def test_plan_mutation(self):
  (self.r/'migration/http-redirects.json').write_text('[]')
  with self.assertRaises(ValueError):resolve_pending(self.r,self.out,self.pending)
 def test_missing_target(self):
  (self.out/'tags/topic/index.html').unlink()
  with self.assertRaises(ValueError):resolve_pending(self.r,self.out,self.pending)
 def test_unapproved_action(self):
  self.write('IGNORE_ALL')
  with self.assertRaises(ValueError):resolve_pending(self.r,self.out,self.pending)
 def test_target_change(self):
  self.policy['resolutions'][self.source]['target']='https://metaadvisor.eu/';self.save()
  with self.assertRaises(ValueError):resolve_pending(self.r,self.out,self.pending)
if __name__=='__main__':unittest.main()

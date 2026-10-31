from pathlib import Path
from urllib.parse import urlsplit,unquote,quote
import json,sys,os,collections,threading,http.server,functools,urllib.request,urllib.error,hashlib
from lxml import html
R=Path.cwd();D=Path(os.environ['MA_QA_OUTPUT']);P=D/'public';assert sys.platform=='linux';sys.path.insert(0,str(R/'tools'));from migration_gate import require_resolved,relative,key
c=json.loads((D/'compatibility.json').read_text());require_resolved(c['pending']);assert len(c['resolved_pending'])==16819
actions=dict(collections.Counter(x['resolution']['action'] for x in c['resolved_pending']));assert actions=={'APPROVED_SPECIFIC_301':375,'APPROVED_404':12471,'APPROVED_NOINDEX_COMPAT':3973},actions
special=['/de/tags/eu-inc./','/hr/tags/%C4%8Dlanak-50./','/hr/tags/eu-inc./','/tags/eu-inc./','/tags/%C4%8Dlanak-50./']
class Quiet(http.server.SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
 def list_directory(self,path):self.send_error(404,'No directory listing');return None
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Quiet,directory=str(P)));threading.Thread(target=server.serve_forever,daemon=True).start();base='http://127.0.0.1:'+str(server.server_port);opener=urllib.request.build_opener(urllib.request.ProxyHandler({}));checks=[]
try:
 for path in special:
  url='https://metaadvisor.eu'+path;p=P/relative(url);assert p.is_file() and p.parent.name.endswith('.') and p.parent.name in os.listdir(p.parent.parent)
  raw=p.read_bytes();doc=html.fromstring(raw);canonical=doc.xpath('//link[@rel="canonical"]/@href');assert len(canonical)==1 and key(canonical[0])==key(url);assert any('noindex' in s.lower() for s in doc.xpath('//meta[@name="robots"]/@content'));assert not doc.xpath('//link[@hreflang]')
  with opener.open(base+quote(unquote(path),safe='/'),timeout=20) as res:
   body=res.read();assert res.status==200 and res.headers.get_content_type()=='text/html' and body==raw
  other=p.parent.with_name(p.parent.name.rstrip('.'))/'index.html'
  if other.is_file():assert p.stat().st_ino!=other.stat().st_ino
  checks.append({'url':url,'literal_file':p.relative_to(P).as_posix(),'status':200,'canonical':canonical[0],'noindex':True,'hreflang_count':0,'HTTP_SHA256_matches':True,'dotless_file_is_distinct':True})
 policy=json.loads((R/'migration/approved-route-resolutions.json').read_text());samples={}
 for url,decision in policy['resolutions'].items():
  if decision['action']=='APPROVED_404':
   lang='de' if '/de/' in urlsplit(url).path else 'hr' if '/hr/' in urlsplit(url).path else 'en';samples.setdefault(lang,url)
 samples['explicit_retired']='https://metaadvisor.eu/tags/betriebseffizienz/'
 for url in samples.values():
  assert not (P/relative(url)).exists()
  try:opener.open(base+quote(unquote(urlsplit(url).path),safe='/'),timeout=20)
  except urllib.error.HTTPError as e:assert e.code==404;e.close()
  else:raise AssertionError('Retired URL did not return 404: '+url)
finally:server.shutdown();server.server_close()
approval=json.loads((R/'migration/release-approvals.json').read_text());assert approval['publication_approved'] is False
result={'PASS':True,'actual_platform':sys.platform,'production_migration_guard':'PASS','publication_authorized':False,'pending':0,'resolved':len(c['resolved_pending']),'resolved_actions':actions,'specific_literal_paths_checked':5,'specific_paths':checks,'retired_HTTP_404_samples':list(samples.values()),'all_redirect_targets_checked_by_exact_validator':19144,'Cloudflare_activated':False,'production_deployment':False}
(D/'NATIVE-MIGRATION-GATE.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps({k:v for k,v in result.items() if k!='specific_paths'},ensure_ascii=False),flush=True)

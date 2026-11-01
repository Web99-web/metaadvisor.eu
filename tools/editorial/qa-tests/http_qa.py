from pathlib import Path
import json,threading,http.server,functools,urllib.request,urllib.parse,hashlib,collections
from PIL import Image
from lxml import html
import os
w=Path.cwd();o=Path(os.environ['MA_QA_OUTPUT']);p=o/'public';v=json.loads((o/'validation.json').read_text());assert not v['errors']
class Quiet(http.server.SimpleHTTPRequestHandler):
 extensions_map={**http.server.SimpleHTTPRequestHandler.extensions_map,".webp":"image/webp"}
 def log_message(self,*a):pass
srv=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Quiet,directory=str(p)));threading.Thread(target=srv.serve_forever,daemon=True).start();base='http://127.0.0.1:'+str(srv.server_port);opener=urllib.request.build_opener(urllib.request.ProxyHandler({}));tests=[];errors=[]
prim=json.loads((w/'migration/expected-primary-pages.json').read_text());urls=['/','/de/','/hr/','/privacy/','/de/privacy/','/hr/privacy/']
for lang in ['en','de','hr']:urls += [urllib.parse.urlsplit(x['url']).path for x in prim if x['lang']==lang][:4]
urls += [urllib.parse.urlsplit(x).path for x in json.loads((w/'.qa-linux/special-urls.json').read_text())]
for url in urls:
 with opener.open(base+urllib.parse.quote(urllib.parse.unquote(url),safe='/'),timeout=15) as res:
  b=res.read();assert res.status==200 and 'text/html' in res.headers['Content-Type'];doc=html.fromstring(b);expected=('Ablehnen','Akzeptieren') if url.startswith('/de/') else ('Odbij','Prihvati') if url.startswith('/hr/') else ('Reject','Accept');assert '/tags/' in url or tuple(doc.xpath('string(//*[@id="'+k+'"])').strip() for k in ['ma-decline','ma-accept'])==expected;tests.append({'url':url,'status':res.status,'MIME':res.headers['Content-Type']})
counts=collections.Counter();images=[]
for f in p.rglob('*'):
 if f.suffix.lower() in ['.jpg','.png','.webp'] and f.is_file() and counts[f.suffix.lower()]<5:
  images.append(f);counts[f.suffix.lower()]+=1
for f in images:
 url='/'+f.relative_to(p).as_posix()
 with opener.open(base+urllib.parse.quote(url),timeout=15) as res:
  b=res.read();assert res.status==200 and res.headers['Content-Type'].startswith('image/'), (url,res.status,res.headers['Content-Type']);assert hashlib.sha256(b).digest()==hashlib.sha256(f.read_bytes()).digest()
  with Image.open(f) as im:fmt=im.format;im.verify()
  tests.append({'url':url,'status':res.status,'MIME':res.headers['Content-Type'],'decoded_format':fmt,'SHA256_matches':True})
srv.shutdown();srv.server_close();(o/'LOCAL-HTTP-TESTS.json').write_text(json.dumps({'tests':tests,'passed':len(tests),'errors':errors,'scope':'Local origin HTTP only; production cache and Cloudflare edge headers are not verified by localhost','external_requests':0,'explicit_local_server_WebP_MIME_registered':True,'production_Cloudflare_MIME_not_tested':True},indent=2));print('Local HTTP PASS',len(tests),flush=True)

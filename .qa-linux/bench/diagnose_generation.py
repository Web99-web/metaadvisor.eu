"""Read-only Linux render diagnostic; never a release approval or deployment."""
from pathlib import Path
import os,sys,json,subprocess,hashlib,time,difflib
from lxml import html
r=Path.cwd();q=r/'.qa-linux';out=Path(os.environ['MA_QA_OUTPUT']);assert sys.platform=='linux' and not out.exists();out.mkdir(parents=True)
clock=json.loads((q/'source-manifest.json').read_text(encoding='utf-8'))['captured_at_UTC']
def save(name,v):(out/name).write_text(json.dumps(v,ensure_ascii=False,indent=2),encoding='utf-8')
def render(name,ignore):
 d=out/name;d.mkdir();(d/'overlay.toml').write_text('resourceDir = '+json.dumps(str(d/'resources'))+'\n',encoding='utf-8')
 args=['hugo','--source',str(r),'--config',str(r/'config.toml')+','+str(d/'overlay.toml'),'--destination',str(d/'public'),'--cacheDir',str(d/'cache'),'--minify','--environment','production','--baseURL','https://metaadvisor.eu/','--clock',clock]
 if ignore:args+=['--ignoreCache']
 start=time.perf_counter()
 with (out/(name+'.log')).open('w',encoding='utf-8') as log:subprocess.run(args,stdout=log,stderr=subprocess.STDOUT,check=True)
 return d/'public',round(time.perf_counter()-start,3)
a,ta=render('cold-full-render',True);b,tb=render('fast-render',False)
diffs=[];samples={};classes={'SEO':0,'reader_text':0,'link_order':0,'DOM_or_attributes':0,'bytes_only':0}
def view(s):
 d=html.fromstring(s)
 return {'SEO':d.xpath('//title/text()|//head/meta/@content|//head/link/@href|//head/link/@hreflang'),'reader_text':[' '.join(x.split()) for x in d.xpath('//body//text()[not(ancestor::script) and not(ancestor::style)]') if x.strip()],'link_order':d.xpath('//body//a/@href'),'DOM_or_attributes':html.tostring(d,encoding='unicode')}
aa={p.relative_to(a).as_posix():p for p in a.rglob('*') if p.is_file()};bb={p.relative_to(b).as_posix():p for p in b.rglob('*') if p.is_file()};assert set(aa)==set(bb)
for name,p in aa.items():
 x=p.read_bytes();y=bb[name].read_bytes()
 if x==y:continue
 row={'path':name,'full_bytes':len(x),'fast_bytes':len(y)}
 if name.endswith('.html'):
  xv=view(x);yv=view(y);row['differences']=[k for k in xv if xv[k]!=yv[k]] or ['bytes_only']
  for k in row['differences']:classes[k]+=1
  if len(samples)<15:
   sx=x.decode('utf-8');sy=y.decode('utf-8');matcher=difflib.SequenceMatcher(None,sx,sy,autojunk=True)
   samples[name]=[{'full':sx[max(0,i-80):min(len(sx),j+80)],'fast':sy[max(0,k-80):min(len(sy),l+80)]} for op,i,j,k,l in matcher.get_opcodes() if op!='equal'][:8]
 diffs.append(row)
save('GENERATION-DIAGNOSTIC.json',{'diagnostic_only':True,'release_approved':False,'clock':clock,'hugo_full_seconds':ta,'hugo_fast_seconds':tb,'files':len(aa),'differences':diffs,'classes':classes,'samples':samples})
print(json.dumps({'diagnostic_only':True,'differences':len(diffs),'classes':classes}),flush=True)
# Deliberately refuse release status: this probe does not run the release validators.
raise SystemExit('Diagnostic saved. Not a release QA PASS; no deploy.')

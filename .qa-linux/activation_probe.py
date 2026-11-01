"""Diagnostic only: preserve the single unexpected rendered page for exact comparison."""
from pathlib import Path
import os,sys,json,subprocess,hashlib
r=Path.cwd();q=r/'.qa-linux';out=Path(os.environ['MA_QA_OUTPUT']);assert not out.exists();out.mkdir(parents=True)
plan=json.loads((q/'activation-plan.json').read_text(encoding='utf-8'));public=out/'public';overlay=out/'resources.toml';overlay.write_text('resourceDir = '+json.dumps(str(out/'resources'))+'\n')
subprocess.run(['hugo','--source',str(r),'--config',str(r/'config.toml')+','+str(overlay),'--destination',str(public),'--cacheDir',str(out/'cache'),'--ignoreCache','--minify','--environment','production','--baseURL','https://metaadvisor.eu/','--clock',plan['comparison_clock']],check=True)
name='hr/news/eu-ai-act-90-posto-ai-neusklađeno-siva-zona-ai-moderacije/index.html';p=public/name;raw=p.read_text(encoding='utf-8');sys.path.insert(0,str(r/'tools'))
from repair_verified_urls import Head,Repair
from finalize_release import Policy
from urllib.parse import unquote,urlsplit
base='https://metaadvisor.eu/'+name.removesuffix('index.html');repair_plan=json.loads((r/'migration/verified-url-repairs.json').read_text(encoding='utf-8'));present={x.relative_to(public).as_posix() for x in public.rglob('*') if x.is_file()}
head=Head(base);head.feed(raw[:raw.lower().find('</head>')+7]);parser=Repair(raw,head.base,present,repair_plan);parser.feed(raw);parser.close();raw=parser.result()
mapping={unquote(urlsplit(u).path):t for u,t in json.loads((r/'data/article_routes.json').read_text(encoding='utf-8'))['aliases'].items()}
for x in json.loads((r/'migration/bundle-mime-migrations.json').read_text(encoding='utf-8')):mapping[unquote(urlsplit(x['old_url']).path)]=x['new_url']
parser=Policy(raw,base,True,mapping);parser.feed(raw);parser.close();raw=parser.result();sys.path.insert(0,str(r/'tools/editorial'));from stable_stylesheet import normalize_bytes
data,n=normalize_bytes(raw.encode('utf-8'),'573eb988ccaac51af141');(out/'UNEXPECTED-PAGE.json').write_text(json.dumps({'diagnostic_only':True,'path':name,'sha256':hashlib.sha256(data).hexdigest(),'html':data.decode('utf-8')},ensure_ascii=False),encoding='utf-8')
raise SystemExit('Diagnostic page captured; deliberately not a release PASS. No deploy.')

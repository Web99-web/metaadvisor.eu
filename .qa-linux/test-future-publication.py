from pathlib import Path
import os,sys,json,shutil,subprocess
from lxml import html
r=Path.cwd(); d=Path(os.environ['MA_QA_OUTPUT']); test=d/'future-test'; src=test/'source'; out=test/'public'
assert sys.platform=='linux' and not test.exists()
shutil.copytree(r,src,ignore=shutil.ignore_patterns('.git','.hugo_build.lock'))
for rel,text in json.loads((r/'.qa-linux/future-fixtures.json').read_text()).items():
 p=src/rel; assert not p.exists();p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text,encoding='utf-8')
def run(name,args):
 with (d/('future-'+name+'.log')).open('w') as f:p=subprocess.run(args,cwd=src,stdout=f,stderr=subprocess.STDOUT)
 assert p.returncode==0,(name,p.returncode)
clock=json.loads((r/'.qa-linux/source-manifest.json').read_text())['captured_at_UTC']

sys.path.insert(0,str(r/'.qa-linux'))
sys.path.insert(0,str(r/'tools'))
from article_source_inventory import source_article_inventory
from release_articles import load_release_articles
from migration_gate import key
base_source=source_article_inventory(r,clock)
expected_source=source_article_inventory(src,clock)
fixture_urls={'https://metaadvisor.eu/'+prefix+'news/qa-future-publication-2026-10-31/' for prefix in ('','de/','hr/')}
assert set(base_source)<=set(expected_source)
assert set(expected_source)-set(base_source)==fixture_urls
assert {key(x['url']) for x in load_release_articles(r,d/'public')}==set(base_source),'Baseline output/source article inventory mismatch'

overlay=test/'resources.toml';overlay.write_text('resourceDir = '+json.dumps(str(test/'resources'))+'\n')
run('hugo',['hugo','--config',str(src/'config.toml')+','+str(overlay),'--destination',str(out),'--cacheDir',str(test/'cache'),'--minify','--environment','production','--baseURL','https://metaadvisor.eu/','--clock',clock])
def py(name,file,*args):run(name,[sys.executable,'-B',str(src/'tools'/file),*map(str,args)])
py('repairs','repair_verified_urls.py','--output',out,'--report',test/'repairs.json')
py('gate','build_tag_compatibility.py','--output',out,'--report',test/'compatibility.json','--release-check')
py('final','finalize_release.py','--output',out,'--report',test/'final.json')
(test/'linux-build.json').write_text('{"platform":"linux","returncode":0}')
py('validate','validate_tag_release.py','--output',out,'--compat-report',test/'compatibility.json','--report',test/'validation.json','--require-linux')
v=json.loads((test/'validation.json').read_text());assert not v['errors'] and v['expected_primary_present']==len(expected_source)
assert {key(x['url']) for x in load_release_articles(src,out)}==set(expected_source),'Fixture output/source exact URL set mismatch'
for lang,prefix in [('en',''),('de','de/'),('hr','hr/')]:
 rel=prefix+'news/qa-future-publication-2026-10-31/'
 doc=html.fromstring((out/rel/'index.html').read_bytes())
 assert doc.xpath('//link[@rel="canonical"]/@href')==['https://metaadvisor.eu/'+rel]
 assert not any('noindex' in x for x in doc.xpath('//meta[@name="robots"]/@content'))
 assert len(set(doc.xpath('//link[@hreflang]/@href')))>=3
 assert not (out/prefix/'tags/qa-never-generate-this-tag-20261031/index.html').exists()
 assert not (out/prefix/'tags/qa-never-generate-this-tag-20261031/index.xml').exists()
for name in ('qa-draft-excluded-fixture','qa-future-excluded-fixture'):assert not (out/'news'/name/'index.html').exists()
(d/'FUTURE-ARTICLES-LINUX.json').write_text(json.dumps({'PASS':True,'platform':sys.platform,'new_articles':3,'articles':len(expected_source),'baseline_articles':len(base_source),'source_output_URL_sets_equal':True,'draft_future_excluded':True,'unknown_tag_HTML_RSS_absent':True,'validation':v,'fixture_source_outside_release':True,'deployment':False},indent=2))
print('PASS Linux future EN/DE/HR publication; fixture output excluded from production artifact')

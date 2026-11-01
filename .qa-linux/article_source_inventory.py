"""Expected public article URLs derived from Hugo source metadata, not built HTML."""
from pathlib import Path
import csv,io,json,subprocess,sys

def source_article_inventory(root,clock,hugo='hugo'):
 root=Path(root).resolve()
 sys.path.insert(0,str(root/'tools'))
 from migration_gate import key
 historical={key(x['url']) for x in json.loads((root/'migration/expected-primary-pages.json').read_text(encoding='utf-8'))}
 aliases={key(x) for x in json.loads((root/'data/article_routes.json').read_text(encoding='utf-8'))['aliases']}
 result=subprocess.run([hugo,'list','published','--source',str(root),'--environment','production','--clock',clock],capture_output=True,text=True,encoding='utf-8',check=True)
 rows=csv.DictReader(io.StringIO(result.stdout.lstrip('\ufeff')))
 assert {'path','permalink','kind','section','draft'}<=set(rows.fieldnames or []),'Unexpected Hugo source inventory schema'
 articles={}
 for row in rows:
  url=key(row['permalink'])
  if row['kind']!='page' or url in aliases or (row['section']!='news' and url not in historical):continue
  assert row['draft'].lower()=='false'
  assert url not in articles,'Duplicate source article URL: '+url
  articles[url]=row['path']
 assert historical<=set(articles),'Historical source articles missing'
 return articles

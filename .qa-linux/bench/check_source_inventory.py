from pathlib import Path
import sys,json
r=Path(sys.argv[1]);out=Path(sys.argv[2]);clock=sys.argv[3]
sys.path.insert(0,str(r/'.qa-linux'));sys.path.insert(0,str(r/'tools'))
from article_source_inventory import source_article_inventory
from release_articles import load_release_articles
from migration_gate import key
expected=set(source_article_inventory(r,clock));actual={key(x['url']) for x in load_release_articles(r,out/'public')}
assert expected==actual,{'missing':sorted(expected-actual)[:10],'extra':sorted(actual-expected)[:10]}
(out/'source-inventory.json').write_text(json.dumps({'PASS':True,'source_articles':len(expected),'output_articles':len(actual),'exact_URL_sets_equal':True}),encoding='utf-8')
print('Independent source and output URL sets match:',len(expected))

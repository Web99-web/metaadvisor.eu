"""New articles follow the publication calendar date; public routing stays slug-based."""
from pathlib import PurePosixPath
from datetime import datetime,date
import re,json
def article_path(language,slug,published_at):
 if language not in ('hr','de','en') or not re.fullmatch(r'[a-z0-9-]+',slug):raise ValueError('Unsafe language or slug')
 value=str(published_at);day=datetime.fromisoformat(value.replace('Z','+00:00')).date() if 'T' in value or ' ' in value else date.fromisoformat(value)
 base='content/news' if language=='en' else f'content/{language}/news'
 return PurePosixPath(base)/f'{day.year:04d}'/f'{day.month:02d}'/f'{day.day:02d}'/(slug+'.md')
def check_new_paths(root,changes):
 checked=[]
 for row in changes:
  path=row['path']
  if row['status'] not in ('A','R100') or not re.match(r'^content/(?:(?:hr|de)/)?news/',path) or not path.endswith('.md'):continue
  if PurePosixPath(path).name=='_index.md':continue
  text=(root/path).read_text(encoding='utf-8');assert text.startswith('---\n') or text.startswith('---\r\n'),'YAML front matter required'
  fields=text.split('---',2)[1]
  def value(key):
   matches=re.findall(r'^'+key+r':\s*(.*?)\s*$',fields,re.M);assert len(matches)==1,'One explicit '+key+' required'
   raw=matches[0]
   if raw.startswith('"'):return json.loads(raw)
   return raw.strip("'")
  language='hr' if path.startswith('content/hr/') else 'de' if path.startswith('content/de/') else 'en'
  assert article_path(language,value('slug'),value('date')).as_posix()==path,'Article requires YYYY/MM/DD matching its unchanged front matter date: '+path
  checked.append(path)
 return checked

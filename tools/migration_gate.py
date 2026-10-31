"""Validate explicit migration decisions against source fingerprints and actual output."""
from pathlib import Path,PureWindowsPath
from urllib.parse import urlsplit,unquote,quote
from html.parser import HTMLParser
import hashlib,json,re,html,os

def key(url):
 u=urlsplit(url)
 if u.scheme!='https' or u.netloc!='metaadvisor.eu' or u.query or u.fragment or not u.path.startswith('/') or '\\' in u.path:raise ValueError('Unsafe URL: '+url)
 if re.search(r'%(?![0-9a-fA-F]{2})',u.path) or any(x in ('.','..') for x in unquote(u.path).split('/')):raise ValueError('Unsafe path')
 return 'https://metaadvisor.eu'+re.sub(r'%[0-9a-fA-F]{2}',lambda m:m[0].upper(),quote(u.path,safe='/%'))

def relative(url):
 path=unquote(urlsplit(key(url)).path).lstrip('/')
 return path+'index.html' if path.endswith('/') else path

def load_policy(root):
 root=Path(root);policy=json.loads((root/'migration/approved-route-resolutions.json').read_text(encoding='utf8'));raw=(root/'migration/http-redirects.json').read_bytes()
 if policy.get('schema') not in (1,2) or hashlib.sha256(raw).hexdigest()!=policy['http_plan_sha256']:raise ValueError('Approved migration fingerprint mismatch')
 if policy['schema']==2:
  for rel in ('migration/tag-compatibility.json','migration/legacy-route-plan.json','migration/expected-primary-pages.json'):
   if hashlib.sha256((root/rel).read_bytes()).hexdigest()!=policy.get('input_sha256',{}).get(rel):raise ValueError('Approved input changed: '+rel)
 rows=json.loads(raw);mapping={key(r['source']):r for r in rows}
 if len(mapping)!=len(rows):raise ValueError('Duplicate canonical migration source')
 approved={}
 for url,decision in policy['resolutions'].items():
  k=key(url) if url!='*' else '*'
  if k=='*' and policy['schema']==2:raise ValueError('Wildcard approval prohibited')
  if k in approved and approved[k]!=decision:raise ValueError('Conflicting approval encodings')
  approved[k]=decision
 p=root/'migration/expected-primary-pages.json';primary={key(x['url']) for x in json.loads(p.read_text(encoding='utf8'))} if p.exists() else set()
 return policy,mapping,approved,primary

def auxiliary(url):
 return bool(re.fullmatch(r'/(?:de/|hr/)?tags/.+/(?:index\.xml)?',urlsplit(key(url)).path))

def document(url,decision):
 if not auxiliary(url) or decision.get('language') not in ('en','de','hr'):raise ValueError('Not an approved auxiliary HTML page')
 lang=decision['language'];labels={'en':('Explore related articles in the languages shown below.','All news'),'de':('Weitere Artikel in den unten angegebenen Sprachen.','Alle Nachrichten'),'hr':('Povezani članci na jezicima navedenima u nastavku.','Sve vijesti')}[lang];esc=html.escape;sections=[]
 for theme in decision.get('themes',[]):
  language=theme['language'];assert language in ('en','de','hr')
  if not theme.get('articles'):raise ValueError('Empty topic is not meaningful compatibility')
  links=''.join('<li><a lang="'+language+'" href="'+esc(a['url'],quote=True)+'">'+esc(a['title'])+'</a></li>' for a in theme['articles'])
  sections.append('<section><h2><a lang="'+language+'" href="'+esc(theme['url'],quote=True)+'">'+esc(theme['title'])+'</a> — '+language.upper()+'</h2><ul>'+links+'</ul></section>')
 if not sections:raise ValueError('Never emit an empty HTTP 200 page')
 prefix='' if lang=='en' else lang+'/'
 return ('<!doctype html><html lang="'+lang+'"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,follow"><link rel="canonical" href="'+esc(url,quote=True)+'"><title>'+esc(unquote(decision['title']).replace('-',' '))+' — MetaAdvisor</title><style>body{font:18px/1.6 system-ui;background:#fafafa;color:#17212b;margin:0}main{max-width:850px;padding:24px;margin:auto;overflow-wrap:anywhere}a{color:#125ca8}li{margin:12px 0}</style></head><body><main><a href="/'+prefix+'">MetaAdvisor</a><h1>'+esc(unquote(decision['title']).replace('-',' '))+'</h1><p>'+esc(labels[0])+'</p>'+''.join(sections)+'<nav><a href="/'+prefix+'news/">'+labels[1]+'</a></nav></main></body></html>').encode('utf8')

def windows_literal_limit(url):
 return any(part.endswith(('.', ' ')) or PureWindowsPath(part).is_reserved() or re.search(r'[<>:"|?*\x00-\x1f]',part) for part in relative(url).split('/'))

def approved_documents(root,include_windows_unsafe=False):
 policy,mapping,approved,primary=load_policy(root);jobs=[]
 for url,decision in policy['resolutions'].items():
  if decision['action']!='APPROVED_NOINDEX_COMPAT':continue
  if key(url) in primary:raise ValueError('Cannot reclassify an article')
  for theme in decision['themes']:
   key(theme['url'])
   for article in theme['articles']:
    if key(article['url']) not in primary:raise ValueError('Unproven preferred article: '+article['url'])
  if include_windows_unsafe or os.name!='nt' or not windows_literal_limit(url):jobs.append((url,document(url,decision)))
 return jobs

class Head(HTMLParser):
 def __init__(self):super().__init__();self.robots=[];self.canon=[];self.alternates=0;self.links=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='meta' and a.get('name')=='robots':self.robots.append(a.get('content','').lower())
  if tag=='link' and a.get('rel')=='canonical':self.canon.append(a.get('href',''))
  if tag=='link' and a.get('hreflang'):self.alternates+=1
  if tag=='a' and a.get('href'):self.links.append(a['href'])

def resolve_pending(root,output,pending):
 root=Path(root);output=Path(output).resolve();policy,mapping,approved,primary=load_policy(root);unresolved=[];resolved=[]
 targets={key(r['target']) for r in mapping.values()}
 def actual(url):
  p=output/relative(url)
  if not p.resolve().is_relative_to(output):raise ValueError('Destination escapes output')
  return p
 for item in pending:
  url=item['url'];k=key(url);decision=approved.get(k)
  if decision is None:unresolved.append(item);continue
  if os.name=='nt' and windows_literal_limit(url):
   unresolved.append({**item,'reason':'WINDOWS_PATH_LIMITATION: approved literal route requires Linux verification'});continue
  action=decision.get('action');record={**item,'resolution':decision}
  if action=='APPROVED_SPECIFIC_301':
   row=mapping.get(k)
   if not row or row.get('status')!=301 or key(row['target'])!=key(decision['target']):raise ValueError('Unproven redirect: '+url)
   if key(row['target']) in mapping:raise ValueError('Migration chain/cycle')
   target=actual(row['target'])
   if not target.is_file():raise ValueError('Approved target missing: '+row['target'])
   record['target_file']=target.relative_to(output).as_posix()
  elif action=='APPROVED_404':
   if policy['schema']!=2 or decision.get('status')!=404 or not auxiliary(url) or k in primary or k in targets or k in mapping:raise ValueError('Unsafe retirement: '+url)
   if actual(url).exists():raise ValueError('Retired URL still has an output file: '+url)
   record['expected_status']=404
  elif action=='APPROVED_NOINDEX_COMPAT':
   if policy['schema']!=2 or not auxiliary(url) or k in primary:raise ValueError('Unsafe compatibility route')
   p=actual(url)
   if not p.is_file() or p.read_bytes()!=document(url,decision):raise ValueError('Unverified compatibility document: '+url)
   head=Head();head.feed(p.read_text(encoding='utf8'))
   if head.canon!=[url] or not any('noindex' in r.split(',') for r in head.robots) or head.alternates:raise ValueError('Wrong compatibility SEO policy')
   for theme in decision['themes']:
    if not actual(theme['url']).is_file():raise ValueError('Related archive missing')
    for article in theme['articles']:
     if key(article['url']) not in primary or not actual(article['url']).is_file():raise ValueError('Related article missing')
   record['target_file']=p.relative_to(output).as_posix()
  else:raise ValueError('Unapproved action: '+str(action))
  resolved.append(record)
 return unresolved,resolved

def require_resolved(pending):
 if pending:raise SystemExit('RELEASE BLOCKED: '+str(len(pending))+' unresolved migration decisions; no upload is authorized.')

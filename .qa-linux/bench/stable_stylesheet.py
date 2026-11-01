"""Content-address the existing stylesheet cache key in rendered output only."""
from pathlib import Path
import argparse,hashlib,json,re
LINK=re.compile(rb'<link\b[^>]*>',re.I)
REL=re.compile(rb'\brel\s*=\s*(?:"stylesheet"|\x27stylesheet\x27|stylesheet)(?=[\s>])',re.I)
HREF=re.compile(rb'\bhref\s*=\s*(["\x27])(/css/style\.css\?v=)([0-9]+|[0-9a-f]{20})\1',re.I)
def normalize_bytes(raw,key):
 if not re.fullmatch(r'[0-9a-f]{20}',key):raise ValueError('Expected actual stylesheet SHA-256 prefix')
 count=0
 def link(m):
  nonlocal count
  tag=m.group()
  if not REL.search(tag) or b'/css/style.css' not in tag:return tag
  h=HREF.search(tag)
  if not h:raise ValueError('Unexpected local stylesheet URL; refuse broad rewriting')
  count+=1
  return tag[:h.start(3)]+key.encode('ascii')+tag[h.end(3):]
 return LINK.sub(link,raw),count
def apply(output,report):
 root=Path(output).resolve();css=root/'css/style.css'
 if not css.is_file() or css.is_symlink():raise ValueError('Actual output stylesheet required')
 digest=hashlib.sha256(css.read_bytes()).hexdigest();key=digest[:20];changed=links=0
 for p in root.rglob('*.html'):
  if p.is_symlink():raise ValueError('Rendered symlink forbidden')
  raw=p.read_bytes();new,n=normalize_bytes(raw,key);links+=n
  if new!=raw:p.write_bytes(new);changed+=1
 if not links:raise ValueError('Expected stylesheet links absent')
 result={'PASS':True,'stylesheet_sha256':digest,'cache_key':key,'links_checked':links,'files_changed':changed,'scope':'Only version query of the existing local stylesheet link. Source files, content and SEO links untouched.'}
 Path(report).write_text(json.dumps(result,indent=2),encoding='utf-8');return result
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--report',required=True);a=p.parse_args();print(json.dumps(apply(a.output,a.report)))

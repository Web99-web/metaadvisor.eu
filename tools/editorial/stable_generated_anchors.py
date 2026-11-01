"""Preserve verified legacy fragment URLs leaked from Hugo shortcode placeholders."""
from pathlib import Path
import re,json,argparse
ID=re.compile(rb'(?<=\s)id\s*=\s*(["\x27]?)(hahahugoshortcode[0-9]+s[0-9]+hbhb)\1(?=[\s>])',re.I)
HREF=re.compile(rb'(?<=\s)href\s*=\s*(["\x27]?)#(hahahugoshortcode[0-9]+s[0-9]+hbhb)\1(?=[\s>])',re.I)
def normalize_bytes(name,raw,mapping):
 matches=list(ID.finditer(raw));expected=mapping.get(name)
 if not matches:
  if expected:raise ValueError('Legacy fragment identifiers disappeared: '+name)
  return raw,0
 if not expected:raise ValueError('Unreviewed generated fragment identifiers: '+name)
 assert len(matches)==len(expected) and len(set(expected))==len(expected),'Legacy fragment count changed'
 replacement={}
 for match,old in zip(matches,expected):
  current=match[2];old=old.encode('ascii')
  assert re.search(rb's[0-9]+hbhb$',current).group()==re.search(rb's[0-9]+hbhb$',old).group(),'Shortcode order changed'
  replacement[current]=old
 def rewrite(match):return match[0][:match.start(2)-match.start()]+replacement[match[2]]+match[0][match.end(2)-match.start():]
 changed=sum(m[2]!=replacement[m[2]] for m in matches);new=ID.sub(rewrite,raw)
 def link(match):
  if match[2] not in replacement:return match[0]
  return rewrite(match)
 new=HREF.sub(link,new);assert [m[2].decode('ascii') for m in ID.finditer(new)]==expected
 return new,changed
def apply(output,report):
 root=Path(output).resolve();mapping=json.loads((Path(__file__).resolve().parent/'legacy-generated-anchors.json').read_text(encoding='utf-8'));seen=set();changed=0
 for p in root.rglob('*.html'):
  assert not p.is_symlink();name=p.relative_to(root).as_posix();raw=p.read_bytes()
  if name not in mapping and b'hahahugoshortcode' not in raw:continue
  new,n=normalize_bytes(name,raw,mapping)
  if name in mapping:seen.add(name)
  if new!=raw:p.write_bytes(new)
  changed+=n
 assert seen==set(mapping),'A protected legacy page disappeared'
 value={'PASS':True,'protected_pages':sorted(seen),'legacy_fragment_IDs_preserved':sum(map(len,mapping.values())),'IDs_restored':changed,'source_articles_and_templates_changed':False};Path(report).write_text(json.dumps(value,ensure_ascii=False,indent=2),encoding='utf-8');return value
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--report',required=True);a=p.parse_args();print(json.dumps(apply(a.output,a.report)))

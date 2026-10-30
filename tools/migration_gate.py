"""Resolve only explicitly approved, fingerprinted migrations; never blanket-waive routes."""
from pathlib import Path
from urllib.parse import urlsplit,unquote
import hashlib,json

def resolve_pending(root, output, pending):
 root=Path(root);output=Path(output).resolve();policy=json.loads((root/'migration/approved-route-resolutions.json').read_text(encoding='utf8'))
 raw=(root/'migration/http-redirects.json').read_bytes()
 if policy.get('schema')!=1 or hashlib.sha256(raw).hexdigest()!=policy['http_plan_sha256']:raise ValueError('Approved migration fingerprint mismatch')
 rows=json.loads(raw);mapping={r['source']:r for r in rows}
 if len(mapping)!=len(rows):raise ValueError('Duplicate migration source')
 approved=policy['resolutions'];unresolved=[];resolved=[]
 for item in pending:
  decision=approved.get(item['url'])
  if decision is None:unresolved.append(item);continue
  row=mapping.get(item['url'])
  if decision.get('action')!='APPROVED_SPECIFIC_301' or not row or row.get('status')!=301 or row['target']!=decision['target']:raise ValueError('Unproven migration resolution: '+item['url'])
  u=urlsplit(row['target']);path=unquote(u.path)
  if u.scheme!='https' or u.netloc!='metaadvisor.eu' or u.query or u.fragment or '\\' in path or any(x in ('.','..') for x in path.split('/')):raise ValueError('Unsafe destination')
  if row['target'] in mapping:raise ValueError('Migration chain/cycle')
  target=output/path.lstrip('/')
  if path.endswith('/'):target=target/'index.html'
  if not target.resolve().is_relative_to(output) or not target.is_file():raise ValueError('Approved target is missing: '+row['target'])
  resolved.append({**item,'resolution':decision,'target_file':target.relative_to(output).as_posix()})
 return unresolved,resolved

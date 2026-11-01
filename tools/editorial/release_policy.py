"""Fail-closed FAST/FULL policy; cache never constitutes validation proof."""
import datetime,hashlib,json,re
from pathlib import Path,PurePosixPath
ARTICLE=re.compile(r'^content/(?:(?:hr|de)/)?news/(?:[^/]+/)*[^/]+\.md$')
IMAGE=re.compile(r'^static/(?:images/.*|[^/]+)\.(?:png|webp|jpg|jpeg)$',re.I)
def mode_for_changes(changes,full):
 if not full.get('success'):return 'FULL'
 if not full.get('protected_fingerprint_matches'):return 'FULL'
 if full.get('age_hours',float('inf'))>24 or full.get('age_hours',-1)<0:return 'FULL'
 if full.get('newer_matching_full_failed'):return 'BLOCKED'
 if not changes:return 'FULL'
 if len({x['path'] for x in changes})!=len(changes):return 'FULL'
 for row in changes:
  path=row['path'];parts=PurePosixPath(path).parts
  if row['status']!='A' or '..' in parts or path.startswith('/') or '\\' in path:return 'FULL'
  if not (ARTICLE.fullmatch(path) or IMAGE.fullmatch(path)):return 'FULL'
  if Path(path).name=='_index.md':return 'FULL'
 return 'FAST'
def verify_receipt(receipt,expected):
 for key in ('commit','tree','policy_fingerprint','file_manifest_sha256'):
  if not isinstance(expected.get(key),str) or not expected[key]:raise ValueError('Missing expected provenance: '+key)
  if receipt.get(key)!=expected.get(key):raise ValueError('Artifact provenance mismatch: '+key)
 if receipt.get('status')!='PASS' or receipt.get('linux') is not True:raise ValueError('Successful Linux validation required')
 if not receipt.get('all_critical_checks_passed'):raise ValueError('Critical checks missing')
 if receipt.get('source_changed'):raise ValueError('Source changed during validation')
 if expected.get('newer_matching_full_failed'):raise ValueError('Newer FULL failure blocks deploy')
 return True
def verify_artifact(directory,rows):
 root=Path(directory).resolve();wanted={r['path']:r for r in rows}
 if len(wanted)!=len(rows):raise ValueError('Duplicate artifact path')
 found={}
 for p in root.rglob('*'):
  if p.is_symlink():raise ValueError('Artifact symlink forbidden')
  if not p.is_file():continue
  if p.stat().st_nlink!=1:raise ValueError('Artifact hardlink forbidden')
  rel=p.relative_to(root).as_posix()
  if rel not in wanted:raise ValueError('Unexpected artifact file: '+rel)
  row=wanted[rel]
  if p.stat().st_size!=row['bytes'] or hashlib.sha256(p.read_bytes()).hexdigest()!=row['sha256']:raise ValueError('Artifact content mismatch: '+rel)
  found[rel]=True
 if set(found)!=set(wanted):raise ValueError('Missing artifact files')
 return True

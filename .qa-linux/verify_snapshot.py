import argparse,hashlib,json
from pathlib import Path
ap=argparse.ArgumentParser();ap.add_argument('--repo',type=Path,required=True);ap.add_argument('--report',type=Path,required=True);a=ap.parse_args();r=a.repo.resolve();m=json.loads((r/'.qa-linux/source-manifest.json').read_text(encoding='utf-8'));errors=[];seen=set()
for p in r.rglob('*'):
 if not p.is_file() or '.git' in p.relative_to(r).parts:continue
 rel=p.relative_to(r).as_posix()
 if rel=='.hugo_build.lock':continue
 seen.add(rel)
 if rel in m['source_files']:
  z=m['source_files'][rel]
  if p.stat().st_size!=z['bytes'] or hashlib.sha256(p.read_bytes()).hexdigest()!=z['sha256']:errors.append(['changed snapshot file',rel])
 elif rel not in m['extra_allowed']:errors.append(['unreviewed extra file',rel])
for rel in set(m['source_files'])-seen:errors.append(['missing snapshot file',rel])
z={'source_files_checked':len(m['source_files']),'errors':errors,'byte_exact_snapshot':not errors};a.report.parent.mkdir(parents=True,exist_ok=True);a.report.write_text(json.dumps(z,indent=2),encoding='utf-8');print(json.dumps(z));raise SystemExit(2 if errors else 0)

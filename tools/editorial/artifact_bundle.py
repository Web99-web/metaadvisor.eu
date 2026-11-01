"""Preserve literal Linux paths while transporting only the verified site."""
from pathlib import Path,PurePosixPath
import hashlib,tarfile
from release_policy import verify_artifact
def create(public,rows,archive):
 public,archive=Path(public),Path(archive)
 verify_artifact(public,rows)
 if not archive.exists():
  with tarfile.open(archive,'w:gz',format=tarfile.GNU_FORMAT) as tar:
   for row in rows:tar.add(public/row['path'],arcname='./'+row['path'],recursive=False)
 with archive.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def unpack(archive,public,rows,expected_sha):
 archive,public=Path(archive),Path(public)
 with archive.open('rb') as f:assert hashlib.file_digest(f,'sha256').hexdigest()==expected_sha,'Archive digest mismatch'
 assert not public.exists(),'Refuse existing extraction directory'
 public.mkdir(parents=True);root=public.resolve();wanted={x['path'] for x in rows};seen=set()
 assert len(wanted)==len(rows)
 with tarfile.open(archive,'r:gz') as tar:
  for member in tar:
   name=member.name.removeprefix('./');parts=PurePosixPath(name).parts
   assert member.isfile() and not member.issym() and not member.islnk(),'Non-regular archive member'
   assert name in wanted and name not in seen and not name.startswith('/') and '..' not in parts,'Unexpected archive path'
   dest=root/name;assert dest.resolve().is_relative_to(root);dest.parent.mkdir(parents=True,exist_ok=True)
   with tar.extractfile(member) as source,dest.open('xb') as target:
    import shutil
    shutil.copyfileobj(source,target)
   seen.add(name)
 assert seen==wanted,'Incomplete archive'
 verify_artifact(public,rows)

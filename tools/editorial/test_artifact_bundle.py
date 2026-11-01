from pathlib import Path
import unittest,tempfile,os,hashlib,tarfile,io
from artifact_bundle import create,unpack
BASE=Path(os.environ.get('RUNNER_TEMP',str(Path(__file__).resolve().parent/'test-temp')));BASE.mkdir(parents=True,exist_ok=True)
class Bundle(unittest.TestCase):
 def test_exact_roundtrip(self):
  with tempfile.TemporaryDirectory(dir=BASE) as td:
   root=Path(td);site=root/'public';site.mkdir();(site/'index.html').write_bytes(b'correct');rows=[{'path':'index.html','bytes':7,'sha256':hashlib.sha256(b'correct').hexdigest()}];sha=create(site,rows,root/'site.tar.gz');unpack(root/'site.tar.gz',root/'restored',rows,sha);self.assertEqual((root/'restored/index.html').read_bytes(),b'correct')
 def test_wrong_archive_digest(self):
  with tempfile.TemporaryDirectory(dir=BASE) as td:
   root=Path(td);(root/'archive').write_bytes(b'bad')
   with self.assertRaises(AssertionError):unpack(root/'archive',root/'out',[], 'wrong')
 def test_unsafe_member_refused(self):
  for name,kind in [('../escape',tarfile.REGTYPE),('link',tarfile.SYMTYPE),('hard',tarfile.LNKTYPE)]:
   with tempfile.TemporaryDirectory(dir=BASE) as td:
    root=Path(td);archive=root/'site.tar.gz'
    with tarfile.open(archive,'w:gz') as tar:
     info=tarfile.TarInfo(name);info.type=kind;info.linkname='../escape' if kind!=tarfile.REGTYPE else '';info.size=1 if kind==tarfile.REGTYPE else 0;tar.addfile(info,io.BytesIO(b'x') if info.size else None)
    sha=hashlib.sha256(archive.read_bytes()).hexdigest()
    with self.assertRaises(AssertionError):unpack(archive,root/'out',[{'path':name,'bytes':1,'sha256':'x'}],sha)
if __name__=='__main__':unittest.main()

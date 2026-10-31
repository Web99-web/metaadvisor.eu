"""Plan physical static image replacements. Content hashes never identify paths."""
from pathlib import Path
from urllib.parse import urlsplit, unquote, quote
import hashlib
import os

def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def static_file(root, url):
    root=Path(root).resolve(); parsed=urlsplit(url)
    if parsed.scheme or parsed.netloc or parsed.query or parsed.fragment:
        raise ValueError('Expected an exact site-relative image path')
    path=unquote(parsed.path)
    if not path.startswith('/') or '\\' in path or any(x in ('.','..') for x in path.split('/')):
        raise ValueError('Unsafe image path')
    static=(root/'static').resolve(); result=(static/path.lstrip('/')).resolve()
    if not result.is_relative_to(static): raise ValueError('Image leaves static root')
    return result

def plan_static_images(root, choices):
    rows=[]; sources=set(); targets=set()
    for old_url,candidate in choices:
        source=static_file(root,old_url); candidate=Path(candidate).resolve()
        if not source.is_file() or not candidate.is_file(): raise ValueError('Missing physical file')
        ext=candidate.suffix.lower()
        if ext not in ('.jpg','.jpeg','.webp','.png'): raise ValueError('Unsupported output format')
        target=source if source.suffix.lower() in ('.jpg','.jpeg') and ext in ('.jpg','.jpeg') else source.with_suffix(ext)
        sk=os.path.normcase(str(source));tk=os.path.normcase(str(target))
        if sk in sources or tk in targets: raise ValueError('Duplicate physical source or destination')
        if target!=source and target.exists(): raise ValueError('Existing destination: '+str(target))
        sources.add(sk);targets.add(tk)
        public='/'+target.relative_to((Path(root)/'static').resolve()).as_posix()
        rows.append({'source':str(source),'target':str(target),'old_url':quote(unquote(old_url),safe='/'),'new_url':quote(public,safe='/'),'candidate':str(candidate),'source_sha256':sha256(source),'candidate_sha256':sha256(candidate),'original_bytes':source.stat().st_size,'candidate_bytes':candidate.stat().st_size})
    return rows

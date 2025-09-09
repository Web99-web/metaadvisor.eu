#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, os, datetime, time, hashlib, yaml
from pathlib import Path
import requests, frontmatter
from googletrans import Translator
from urllib.parse import urlparse

# ---------- IMAGE POLICY ----------
USE_OG_IMAGE = False
OG_WHITELIST = {"unsplash.com","images.unsplash.com","pexels.com","pixabay.com",
                "upload.wikimedia.org","commons.wikimedia.org"}

# ---------- OPCIJE ----------
ADD_ALIASES_FROM_INBOX     = False
DELETE_INBOX_AFTER_PUBLISH = False
PUBLISH_LIMIT              = 5

# ---------- KONFIG ----------
INBOX   = Path("content/_inbox")
USER_AGENT = "MetaAdvisorBot/2.0 (+https://metaadvisor.eu)"
TIMEOUT    = 15
HEADERS    = {"User-Agent": USER_AGENT}

TRANSLIT = {
    "ä":"ae","ö":"oe","ü":"ue","ß":"ss",
    "č":"c","ć":"c","š":"s","ž":"z","đ":"dj",
    "Ä":"ae","Ö":"oe","Ü":"ue","Č":"c","Ć":"c","Š":"s","Ž":"z","Đ":"dj"
}

translator = Translator()
LIB_DIR = Path("static/images")
IMAGE_MAP_YAML = Path("data/image_map.yaml")

def translit(s: str) -> str:
    return "".join(TRANSLIT.get(ch, ch) for ch in s)

def url_slug(title: str) -> str:
    s = translit(title or "").lower()
    s = re.sub(r"[^a-z0-9 _-]", "", s)
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return (s[:120] or "post")

def bundle_dir(lang: str, dt: datetime.datetime, slug: str) -> Path:
    base = Path("content") if lang == "en" else Path("content")/lang
    return base/"news"/f"{dt:%Y}"/f"{dt:%m}"/f"{dt:%d}"/slug

def clean_body(md: str) -> str:
    if not md: return ""
    return re.sub(r":contentReference\[[^\]]*\]\{index=\d+\}", "", md)

def dl(url: str) -> bytes | None:
    if not url: return None
    try:
        host = urlparse(url).netloc
        if not USE_OG_IMAGE and host not in OG_WHITELIST:
            return None
        r = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        r.raise_for_status()
        return r.content
    except Exception:
        return None

def load_image_map():
    try:
        with IMAGE_MAP_YAML.open("r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
            mapping = data.get("mapping") or {}
            for k,v in list(mapping.items()):
                if isinstance(v,str): mapping[k]=[v]
            data["mapping"] = mapping
            data.setdefault("default","placeholder.jpg")
            return data
    except Exception:
        return {"mapping": {}, "default": "placeholder.jpg"}

def _det_pick(files: list[str], seed: str) -> str:
    if not files: return ""
    h = hashlib.md5((seed or "").encode("utf-8")).hexdigest()
    return files[int(h,16) % len(files)]

def pick_library_image(tags, title, body, seed: str) -> bytes | None:
    conf = load_image_map()
    mapping: dict = conf.get("mapping", {})
    default_name: str = conf.get("default", "placeholder.jpg")
    keys = [str(t).lower() for t in (tags or [])]
    keys += re.findall(r"[a-z0-9\-]+", (title or "").lower())
    if body: keys += re.findall(r"[a-z0-9\-]+", body.lower())
    for k in keys:
        if k in mapping:
            f = LIB_DIR / _det_pick(mapping[k], seed or title or "")
            if f.exists(): return f.read_bytes()
    f = LIB_DIR / default_name
    return f.read_bytes() if f.exists() else None

def get_hero_bytes(image_url, tags, title, body, seed: str) -> bytes | None:
    return dl(image_url) or pick_library_image(tags, title, body, seed)

def write_bundle(lang: str, dt: datetime.datetime, title: str, body: str,
                 tkey: str, src: str, src_url: str, tags, aliases=None, hero_bytes=None):
    slug_clean = url_slug(title)
    d = bundle_dir(lang, dt, slug_clean)
    if d.exists():
        short = hashlib.md5(f"{title}{dt}".encode()).hexdigest()[:6]
        slug_clean = f"{slug_clean}-{short}"
        d = bundle_dir(lang, dt, slug_clean)
    d.mkdir(parents=True, exist_ok=True)
    if hero_bytes: (d/"hero.jpg").write_bytes(hero_bytes)

    fm = [
        "---",
        f'title: "{title}"',
        f'slug: "{slug_clean}"',
        f"date: {dt.strftime('%Y-%m-%dT%H:%M:%SZ')}",
        'category: "news"',
        f'translationKey: "{tkey}"',
        f'source: "{src}"',
        f'source_url: "{src_url}"',
        'image: "hero.jpg"',                         # ← pomaže list kartici
        "tags: [" + ", ".join([f'\"{t}\"' for t in (tags or [])]) + "]",
    ]
    if aliases:
        fm.append("aliases:")
        fm += [f'  - "{a}"' for a in aliases]
    fm.append("---")
    (d/"index.md").write_text("\n".join(fm)+"\n\n"+(body or "")+"\n", encoding="utf-8")
    return d

def auto_translate(text: str, lang: str) -> str:
    if not text: return text
    for _ in range(2):
        try:
            return translator.translate(text, dest=lang).text.strip()
        except Exception:
            time.sleep(0.8)
    return text

def publish_one(inbox_file: Path, also_hr=True, also_de=True):
    # SKIP: _index.md i sve što počinje sa "_"
    if inbox_file.name.startswith("_"): 
        print(f"[skip] {inbox_file}")
        return

    post = frontmatter.load(inbox_file)
    title_en = post.get("title","Untitled")
    if title_en.strip().lower().startswith("inbox (drafts)"):
        print(f"[skip] drafts page: {inbox_file}")
        return

    src      = post.get("source","")
    src_url  = post.get("source_url","")
    tkey     = post.get("translationKey","")
    tags     = post.get("tags",[])

    date_val = post.get("date")
    if isinstance(date_val, str):
        try: dt = datetime.datetime.fromisoformat(date_val.replace("Z","+00:00"))
        except Exception: dt = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
    elif isinstance(date_val, datetime.datetime):
        dt = date_val if date_val.tzinfo else date_val.replace(tzinfo=datetime.timezone.utc)
    else:
        dt = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)

    body_en  = clean_body(post.content)
    image_url= post.get("image_url","")

    old_segment = inbox_file.stem if ADD_ALIASES_FROM_INBOX else None
    hero = get_hero_bytes(image_url, tags, title_en, body_en, seed=tkey or title_en)

    en_aliases = [f"/news/{old_segment}/"] if old_segment else None
    write_bundle("en", dt, title_en, body_en or f"Read the full article: {src_url}",
                 tkey, src, src_url, tags, aliases=en_aliases, hero_bytes=hero)

    if also_hr:
        write_bundle("hr", dt,
                     auto_translate(title_en,"hr"),
                     auto_translate(body_en or f"Read the full article: {src_url}", "hr"),
                     tkey, src, src_url, tags,
                     aliases=[f"/hr/news/{old_segment}/"] if old_segment else None,
                     hero_bytes=hero)

    if also_de:
        write_bundle("de", dt,
                     auto_translate(title_en,"de"),
                     auto_translate(body_en or f"Read the full article: {src_url}", "de"),
                     tkey, src, src_url, tags,
                     aliases=[f"/de/news/{old_segment}/"] if old_segment else None,
                     hero_bytes=hero)

    print(f"[publish] {inbox_file.name} → EN/HR/DE OK")
    if DELETE_INBOX_AFTER_PUBLISH:
        try:
            inbox_file.unlink()
        except Exception as e:
            print(f"[warn] Could not remove {inbox_file}: {e}")

def pick_inbox_files(limit=PUBLISH_LIMIT):
    files = [p for p in sorted(INBOX.rglob("*.md")) if not p.name.startswith("_")]
    return files[:limit]

def main(limit=PUBLISH_LIMIT, also_hr=True, also_de=True):
    files = pick_inbox_files(limit=limit)
    if not files:
        print("[i] Nema ničega u inboxu.")
        return
    for f in files:
        publish_one(f, also_hr=also_hr, also_de=also_de)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=PUBLISH_LIMIT)
    parser.add_argument("--no-hr", dest="no_hr", action="store_true")
    parser.add_argument("--no-de", dest="no_de", action="store_true")
    args = parser.parse_args()

    main(
        limit=args.limit,
        also_hr=not args.no_hr,
        also_de=not args.no_de,
    )


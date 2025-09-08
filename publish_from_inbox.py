#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, os, json, datetime, time, hashlib
from pathlib import Path
import requests
import frontmatter
from googletrans import Translator
import yaml, hashlib
from urllib.parse import urlparse

# ——— Image policy (sigurno po autorskim pravima) ———
USE_OG_IMAGE = False  # False = ne skidaj tuđe og:image; koristi našu biblioteku
OG_WHITELIST = {
    "unsplash.com", "images.unsplash.com",
    "pexels.com", "pixabay.com",
    "upload.wikimedia.org", "commons.wikimedia.org",
}

# ============ OPCIJE ============
ADD_ALIASES_FROM_INBOX     = False  # preusmjeri /news/2025-09-07-naslov/ → /news/cisti-slug/
DELETE_INBOX_AFTER_PUBLISH = False  # obriši inbox .md nakon uspješne objave
PUBLISH_LIMIT              = 5      # koliko inbox fajlova objaviti po runu
# ================================

# ============ KONFIG ============
INBOX  = Path("content/_inbox")  # EN draftovi iz scrape_inbox.py
USER_AGENT = "MetaAdvisorBot/2.0 (+https://metaadvisor.eu)"
TIMEOUT    = 15
HEADERS    = {"User-Agent": USER_AGENT}
# =================================

TRANSLIT = {
    # German
    "ä":"ae","ö":"oe","ü":"ue","ß":"ss",
    # Croatian
    "č":"c","ć":"c","š":"s","ž":"z","đ":"dj",
    "Ä":"ae","Ö":"oe","Ü":"ue","Č":"c","Ć":"c","Š":"s","Ž":"z","Đ":"dj"
}

translator = Translator()

def translit(s: str) -> str:
    return "".join(TRANSLIT.get(ch, ch) for ch in s)

def url_slug(title: str) -> str:
    """Lokalizirani slug bez datuma (za čisti URL)."""
    s = translit(title).lower()
    # makni sve osim slova, brojeva, razmaka i crtice
    s = re.sub(r"[^a-z0-9 _-]", "", s)
    # razmake u crtice
    s = re.sub(r"\s+", "-", s)
    # svedi višestruke crtice na jednu i poreži rubne
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s[:120]

def bundle_dir(lang: str, dt: datetime.datetime, slug: str) -> Path:
    """
    EN je default → content/news/YYYY/MM/DD/<slug>/index.md
    Ostali jezici → content/<lang>/news/YYYY/MM/DD/<slug>/index.md
    """
    base = Path("content") if lang == "en" else Path("content")/lang
    return base/"news"/f"{dt:%Y}"/f"{dt:%m}"/f"{dt:%d}"/slug

def clean_body(md: str) -> str:
    if not md: return ""
    md = re.sub(r":contentReference\[[^\]]*\]\{index=\d+\}", "", md)
    return md

def dl(url: str) -> bytes | None:
    if not url: return None
    try:
        r = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        r.raise_for_status()
        return r.content
    except Exception:
        return None

def write_bundle(lang: str, dt: datetime.datetime, title: str, body: str,
                 tkey: str, src: str, src_url: str, tags, aliases=None, hero_bytes=None):
    slug_clean = url_slug(title)
    d = bundle_dir(lang, dt, slug_clean)

    if d.exists():
        short = hashlib.md5(f"{title}{dt}".encode()).hexdigest()[:6]
        slug_clean = f"{slug_clean}-{short}"
        d = bundle_dir(lang, dt, slug_clean)

    d.mkdir(parents=True, exist_ok=True)

    if hero_bytes:
        (d/"hero.jpg").write_bytes(hero_bytes)

    fm = [
        "---",
        f'title: "{title}"',
        f'slug: "{slug_clean}"',
        f"date: {dt.strftime('%Y-%m-%dT%H:%M:%SZ')}",
        'category: "news"',
        f'translationKey: "{tkey}"',
        f'source: "{src}"',
        f'source_url: "{src_url}"',
        "tags: [" + ", ".join([f'\"{t}\"' for t in (tags or [])]) + "]",
    ]
    if aliases:
        fm.append("aliases:")
        fm += [f'  - "{a}"' for a in aliases]
    fm.append("---")

    (d/"index.md").write_text("\n".join(fm) + "\n\n" + (body or "") + "\n", encoding="utf-8")
    return d

def auto_translate(text: str, lang: str) -> str:
    if not text: return text
    for _ in range(2):
        try:
            return translator.translate(text, dest=lang).text.strip()
        except Exception:
            time.sleep(0.8)
    return text

LIB_DIR = Path("static/images")
IMAGE_MAP_YAML = Path("data/image_map.yaml")

def load_image_map():
    try:
        with IMAGE_MAP_YAML.open("r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
            mapping = data.get("mapping") or {}
            for k, v in list(mapping.items()):
                if isinstance(v, str):
                    mapping[k] = [v]
            data["mapping"] = mapping
            if "default" not in data:
                data["default"] = "placeholder.jpg"
            return data
    except Exception:
        return {"mapping": {}, "default": "placeholder.jpg"}

def _det_pick(files: list[str], seed: str) -> str:
    if not files:
        return ""
    h = hashlib.md5(seed.encode("utf-8")).hexdigest()
    idx = int(h, 16) % len(files)
    return files[idx]

def pick_library_image(tags, title, body, seed: str) -> bytes | None:
    conf = load_image_map()
    mapping: dict = conf.get("mapping") or {}
    default_name: str = conf.get("default") or "placeholder.jpg"

    keys = []
    for t in (tags or []):
        keys.append(str(t).lower())
    keys += re.findall(r"[a-z0-9\-]+", (title or "").lower())
    if body:
        keys += re.findall(r"[a-z0-9\-]+", body.lower())

    for k in keys:
        if k in mapping:
            candidates = mapping[k]
            chosen = _det_pick(candidates, seed)
            f = LIB_DIR / chosen
            if f.exists():
                return f.read_bytes()

    f = LIB_DIR / default_name
    return f.read_bytes() if f.exists() else None

def get_hero_bytes(image_url, tags, title, body, seed: str) -> bytes | None:
    b = dl(image_url) if image_url else None
    if b:
        return b
    return pick_library_image(tags, title, body, seed)

def publish_one(inbox_file: Path, also_hr=True, also_de=True):
    post = frontmatter.load(inbox_file)
    title_en = post.get("title","Untitled")
    src      = post.get("source","")
    src_url  = post.get("source_url","")
    tkey     = post.get("translationKey","")
    tags     = post.get("tags",[])

    # --- FIX za datum ---
    date_val = post.get("date")
    if isinstance(date_val, str):
        try:
            dt = datetime.datetime.fromisoformat(date_val.replace("Z", "+00:00"))
        except Exception:
            dt = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
    elif isinstance(date_val, datetime.datetime):
        dt = date_val if date_val.tzinfo else date_val.replace(tzinfo=datetime.timezone.utc)
    else:
        dt = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
    # -------------------

    body_en  = clean_body(post.content)
    image_url= post.get("image_url","")

    old_segment = inbox_file.stem if ADD_ALIASES_FROM_INBOX else None
    hero = get_hero_bytes(image_url, tags, title_en, body_en, seed=tkey or title_en)

    en_aliases = [f"/news/{old_segment}/"] if old_segment else None
    write_bundle("en", dt, title_en, body_en or f"Read the full article: {src_url}",
                 tkey, src, src_url, tags, aliases=en_aliases, hero_bytes=hero)

    if also_hr:
        title_hr = auto_translate(title_en, "hr")
        body_hr  = auto_translate(body_en or f"Read the full article: {src_url}", "hr")
        hr_aliases = [f"/hr/news/{old_segment}/"] if old_segment else None
        write_bundle("hr", dt, title_hr, body_hr, tkey, src, src_url, tags,
                     aliases=hr_aliases, hero_bytes=hero)

    if also_de:
        title_de = auto_translate(title_en, "de")
        body_de  = auto_translate(body_en or f"Read the full article: {src_url}", "de")
        de_aliases = [f"/de/news/{old_segment}/"] if old_segment else None
        write_bundle("de", dt, title_de, body_de, tkey, src, src_url, tags,
                     aliases=de_aliases, hero_bytes=hero)

    print(f"[publish] {inbox_file.name} → bundles OK")

    if DELETE_INBOX_AFTER_PUBLISH:
        try:
            inbox_file.unlink()
            print(f"[cleanup] Removed {inbox_file}")
        except Exception as e:
            print(f"[warn] Could not remove {inbox_file}: {e}")

def pick_inbox_files(limit=PUBLISH_LIMIT):
    files = sorted(INBOX.rglob("*.md"))
    return files[:limit]

def main():
    files = pick_inbox_files()
    if not files:
        print("[i] Nema ničega u inboxu.")
        return
    for f in files:
        publish_one(f, also_hr=True, also_de=True)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, os, datetime, time, hashlib
from pathlib import Path
from urllib.parse import urlparse

import requests
import frontmatter
from googletrans import Translator
import yaml

# ============== Image policy (sigurnije autorsko pravo) ==============
# True = preuzimamo og:image SAMO s domena u OG_WHITELIST
# False = ne skidamo tuđe og:image; koristimo biblioteku slika u static/images
USE_OG_IMAGE = False
OG_WHITELIST = {
    "unsplash.com", "images.unsplash.com",
    "pexels.com", "pixabay.com",
    "upload.wikimedia.org", "commons.wikimedia.org",
}
# =====================================================================

# =================== OPCIJE ===================
ADD_ALIASES_FROM_INBOX     = False  # npr. /news/2025-09-07-stari-slug/ → /news/novi-slug/
DELETE_INBOX_AFTER_PUBLISH = False  # obriši .md iz inboxa nakon objave
PUBLISH_LIMIT              = 5      # koliko inbox fajlova objaviti po runu
# ==============================================

# =================== KONFIG ===================
INBOX     = Path("content/_inbox")
USER_AGENT = "MetaAdvisorBot/2.0 (+https://metaadvisor.eu)"
TIMEOUT    = 15
HEADERS    = {"User-Agent": USER_AGENT}
LIB_DIR    = Path("static/images")            # tvoja biblioteka slika
IMAGE_MAP_YAML = Path("data/image_map.yaml")  # mapiranje ključnih riječi → slike
# ==============================================

TRANSLIT = {
    "ä":"ae","ö":"oe","ü":"ue","ß":"ss",
    "č":"c","ć":"c","š":"s","ž":"z","đ":"dj",
    "Ä":"ae","Ö":"oe","Ü":"ue","Č":"c","Ć":"c","Š":"s","Ž":"z","Đ":"dj"
}
translator = Translator()

# ---------- util ----------
def translit(s: str) -> str:
    return "".join(TRANSLIT.get(ch, ch) for ch in s)

def url_slug(title: str) -> str:
    s = translit(title).lower()
    s = re.sub(r"[^a-z0-9 _-]", "", s)
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s[:120]

def bundle_dir(lang: str, dt: datetime.datetime, slug: str) -> Path:
    base = Path("content") if lang == "en" else Path("content")/lang
    return base/"news"/f"{dt:%Y}"/f"{dt:%m}"/f"{dt:%d}"/slug

def clean_body(md: str) -> str:
    if not md: return ""
    return re.sub(r":contentReference\[[^\]]*\]\{index=\d+\}", "", md)

def dl(url: str) -> bytes | None:
    if not url: return None
    try:
        r = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        r.raise_for_status()
        return r.content
    except Exception:
        return None

def _host(url: str) -> str:
    try:
        return urlparse(url).netloc.lower()
    except Exception:
        return ""

def og_allowed(url: str) -> bool:
    h = _host(url)
    return any(h.endswith(d) for d in OG_WHITELIST)

def our_take_block(lang: str, title: str) -> str:
    hdr = {"en": "## Our take", "hr": "## Naš osvrt", "de": "## Unser Fazit"}[lang]
    txt = {
        "en": ("This is an automated summary compiled from public sources. "
               "We highlight key facts, but nuance can be lost. Treat this as a quick brief — "
               "not investment or legal advice."),
        "hr": ("Ovo je automatizirani sažetak iz javno dostupnih izvora. "
               "Ističemo bitne činjenice, ali nijanse se mogu izgubiti. "
               "Shvatite ovo kao brzi pregled — ne kao investicijski ili pravni savjet."),
        "de": ("Dies ist eine automatisierte Zusammenfassung aus öffentlichen Quellen. "
               "Wir heben zentrale Fakten hervor, jedoch können Nuancen verloren gehen. "
               "Dies ist ein schneller Überblick — keine Anlage- oder Rechtsberatung."),
    }[lang]
    return f"\n\n{hdr}\n\n{txt}\n"

# ---------- image map ----------
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
    if USE_OG_IMAGE and image_url and og_allowed(image_url):
        b = dl(image_url)
        if b:
            return b
    return pick_library_image(tags, title, body, seed)

# ---------- zapis ----------
def write_bundle(lang: str, dt: datetime.datetime, title: str, body: str,
                 tkey: str, src: str, src_url: str, tags, category: str,
                 aliases=None, hero_bytes=None):
    slug_clean = url_slug(title)
    d = bundle_dir(lang, dt, slug_clean)

    if d.exists():
        short = hashlib.md5(f"{title}{dt}".encode()).hexdigest()[:6]
        slug_clean = f"{slug_clean}-{short}"
        d = bundle_dir(lang, dt, slug_clean)

    d.mkdir(parents=True, exist_ok=True)
    if hero_bytes:
        (d/"hero.jpg").write_bytes(hero_bytes)

    tag_list = [str(t) for t in (tags or [])]

    fm = [
        "---",
        f'title: "{title}"',
        f'slug: "{slug_clean}"',
        f"date: {dt.strftime('%Y-%m-%dT%H:%M:%SZ')}",
        f'category: "{category or "news"}"',
        f'translationKey: "{tkey}"',
        f'source: "{src}"',
        f'source_url: "{src_url}"',
        "tags: [" + ", ".join([f'\"{t}\"' for t in tag_list]) + "]",
    ]
    if aliases:
        fm.append("aliases:")
        fm += [f'  - "{a}"' for a in aliases]
    fm.append("---")

    (d/"index.md").write_text("\n".join(fm) + "\n\n" + (body or "") + "\n", encoding="utf-8")
    return d

# ---------- prijevod ----------
def auto_translate(text: str, lang: str) -> str:
    if not text: return text
    for _ in range(2):
        try:
            return translator.translate(text, dest=lang).text.strip()
        except Exception:
            time.sleep(0.8)
    return text

# ---------- glavna obrada ----------
def publish_one(inbox_file: Path, also_hr=True, also_de=True):
    post = frontmatter.load(inbox_file)

    title_en = post.get("title", "Untitled")
    src      = post.get("source", "")
    src_url  = post.get("source_url", "")
    tkey     = post.get("translationKey", "")
    category = post.get("category", "news")
    tags     = list(post.get("tags", []) or [])
    image_url= post.get("image_url", "")

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

    body_en_src = clean_body(post.content) or f"Read the full article: {src_url}"

    old_segment = inbox_file.stem if ADD_ALIASES_FROM_INBOX else None
    hero = get_hero_bytes(image_url, tags, title_en, body_en_src, seed=tkey or title_en)

    # EN
    en_aliases = [f"/news/{old_segment}/"] if old_segment else None
    body_en = body_en_src + our_take_block("en", title_en)
    write_bundle("en", dt, title_en, body_en, tkey, src, src_url, tags, category,
                 aliases=en_aliases, hero_bytes=hero)

    # HR
    if also_hr:
        title_hr = auto_translate(title_en, "hr")
        body_hr  = auto_translate(body_en_src, "hr") + our_take_block("hr", title_hr)
        hr_aliases = [f"/hr/news/{old_segment}/"] if old_segment else None
        write_bundle("hr", dt, title_hr, body_hr, tkey, src, src_url, tags, category,
                     aliases=hr_aliases, hero_bytes=hero)

    # DE
    if also_de:
        title_de = auto_translate(title_en, "de")
        body_de  = auto_translate(body_en_src, "de") + our_take_block("de", title_de)
        de_aliases = [f"/de/news/{old_segment}/"] if old_segment else None
        write_bundle("de", dt, title_de, body_de, tkey, src, src_url, tags, category,
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

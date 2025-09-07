#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, os, json, datetime, time, hashlib
from pathlib import Path
from urllib.parse import urlparse
import requests
import frontmatter
from googletrans import Translator

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
    s = re.sub(r"[^a-z0-9\\- _]", "", s).strip().replace(" ", "-")
    s = re.sub(r"-{2,}", "-", s)
    return s[:120].strip("-")

def bundle_dir(lang: str, dt: datetime.datetime, slug: str) -> Path:
    """
    EN je default → content/news/YYYY/MM/DD/<slug>/index.md
    Ostali jezici → content/<lang>/news/YYYY/MM/DD/<slug>/index.md
    """
    base = Path("content") if lang == "en" else Path("content")/lang
    return base/"news"/f"{dt:%Y}"/f"{dt:%m}"/f"{dt:%d}"/slug

def clean_body(md: str) -> str:
    if not md: return ""
    # ukloni artefakte tipa :contentReference[...] {index=...}
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
    """
    Kreira page bundle s lokaliziranim slugom (bez datuma u URL-u).
    Rješava koliziju dodavanjem kratkog hash sufiksa.
    """
    slug_clean = url_slug(title)
    d = bundle_dir(lang, dt, slug_clean)

    # kolizija: isti slug isti dan → dodaj kratki hash sufiks
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
        f'slug: "{slug_clean}"',  # ključno: čisti URL bez datuma
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

def publish_one(inbox_file: Path, also_hr=True, also_de=True):
    post = frontmatter.load(inbox_file)
    title_en = post.get("title","Untitled")
    src      = post.get("source","")
    src_url  = post.get("source_url","")
    tkey     = post.get("translationKey","")
    tags     = post.get("tags",[])
    date_iso = post.get("date")
    dt       = datetime.datetime.fromisoformat(date_iso.replace("Z","+00:00"))
    body_en  = clean_body(post.content)
    image_url= post.get("image_url","")

    # preuzmi og:image kao hero.jpg (Hugo će iz toga raditi thumb/WebP)
    hero = dl(image_url)

    # EN (default, bez /en/ u URL-u)
    write_bundle("en", dt, title_en, body_en or f"Read the full article: {src_url}",
                 tkey, src, src_url, tags, aliases=None, hero_bytes=hero)

    # HR
    if also_hr:
        title_hr = auto_translate(title_en, "hr")
        body_hr  = auto_translate(body_en or f"Read the full article: {src_url}", "hr")
        write_bundle("hr", dt, title_hr, body_hr, tkey, src, src_url, tags, hero_bytes=hero)

    # DE
    if also_de:
        title_de = auto_translate(title_en, "de")
        body_de  = auto_translate(body_en or f"Read the full article: {src_url}", "de")
        write_bundle("de", dt, title_de, body_de, tkey, src, src_url, tags, hero_bytes=hero)

    print(f"[publish] {inbox_file.name} → bundles OK")

    # Po želji: nakon objave očisti inbox (spriječi dupli publish)
    # inbox_file.unlink()

def pick_inbox_files(limit=5):
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

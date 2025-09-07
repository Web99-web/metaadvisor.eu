#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, os, json, datetime, time
from pathlib import Path
from urllib.parse import urlparse
import requests
import frontmatter
from googletrans import Translator

# ============ KONFIG ============
OUT_EN = Path("content/en/news")
OUT_DE = Path("content/de/news")
OUT_HR = Path("content/hr/news")
INBOX  = Path("content/_inbox")

USER_AGENT = "MetaAdvisorBot/2.0 (+https://metaadvisor.eu)"
TIMEOUT    = 15
HEADERS    = {"User-Agent": USER_AGENT}
# =================================

TRANSLIT = {"ä":"ae","ö":"oe","ü":"ue","ß":"ss","č":"c","ć":"c","š":"s","ž":"z","đ":"dj",
            "Ä":"ae","Ö":"oe","Ü":"ue","Č":"c","Ć":"c","Š":"s","Ž":"z","Đ":"dj"}

translator = Translator()

def translit(s: str) -> str:
    return "".join(TRANSLIT.get(ch, ch) for ch in s)

def slugify_local(title: str) -> str:
    s = translit(title).lower()
    s = re.sub(r"[^a-z0-9\- _]", "", s).strip().replace(" ", "-")
    s = re.sub(r"-{2,}", "-", s)
    return s[:120].strip("-")

def dated_slug(dt: datetime.datetime, title: str) -> str:
    return f"{dt.strftime('%Y-%m-%d')}-{slugify_local(title)}"

def bundle_dir(lang: str, dt: datetime.datetime, slug: str) -> Path:
    return Path("content")/lang/"news"/f"{dt:%Y}"/f"{dt:%m}"/slug

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
    slug = dated_slug(dt, title)
    d = bundle_dir(lang, dt, slug)
    d.mkdir(parents=True, exist_ok=True)
    if hero_bytes:
        (d/"hero.jpg").write_bytes(hero_bytes)

    fm = [
        "---",
        f'title: "{title}"',
        f"date: {dt.strftime('%Y-%m-%dT%H:%M:%SZ')}",
        'category: "news"',
        f'translationKey: "{tkey}"',
        f'source: "{src}"',
        f'source_url: "{src_url}"',
        "tags: [" + ", ".join([f'"{t}"' for t in (tags or [])]) + "]",
    ]
    if aliases:
        fm.append("aliases:")
        fm += [f'  - "{a}"' for a in aliases]
    fm.append("---")

    (d/"index.md").write_text("\n".join(fm) + "\n\n" + body + "\n", encoding="utf-8")
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

    hero = dl(image_url)  # hero.jpg (thumb će Hugo raditi iz hero-a)

    # EN
    dir_en = write_bundle("en", dt, title_en, body_en or f"Read the full article: {src_url}",
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
    # po želji: nakon objave, premjesti ili izbriši inbox fajl:
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

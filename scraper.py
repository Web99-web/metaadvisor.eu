#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, re, json, hashlib, datetime, pathlib
import requests, feedparser
from bs4 import BeautifulSoup

# ====== KONFIG ======
OUT_DIR = os.path.join("content", "news")  # kod tebe je content/news
DB_FILE = ".scrape_seen.json"              # zapisujemo što je već viđeno

SOURCES = [
    {"name": "Reuters Tech", "rss": "https://feeds.reuters.com/reuters/technologyNews"},
    {"name": "CoinDesk",     "rss": "https://www.coindesk.com/arc/outboundfeeds/rss/"},
    # dodaš/obrišeš izvore po želji
]

MAX_ITEMS_PER_RUN = 6                     # koliko novih po jednom pokretanju
USER_AGENT = "MetaAdvisorBot/1.0 (+https://metaadvisor.eu)"
# =====================

def esc(s: str) -> str:
    if not s: return ""
    return s.replace('"', "'").replace("\n", " ").strip()

def slugify(s: str, max_len: int = 80) -> str:
    s = re.sub(r"[^a-zA-Z0-9\- ]", "", s or "").strip().lower()
    s = re.sub(r"\s+", "-", s)
    s = s[:max_len] or "post"
    return s

def load_db() -> dict:
    if os.path.exists(DB_FILE):
        try:
            return json.load(open(DB_FILE, "r", encoding="utf-8"))
        except Exception:
            pass
    return {"seen": []}

def save_db(db: dict) -> None:
    json.dump(db, open(DB_FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

def fetch_meta(url: str) -> dict:
    try:
        r = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=15)
        r.raise_for_status()
    except Exception:
        return {}
    soup = BeautifulSoup(r.text, "html.parser")
    def m(property_name=None, name=None):
        tag = None
        if property_name:
            tag = soup.find("meta", attrs={"property": property_name})
        if not tag and name:
            tag = soup.find("meta", attrs={"name": name})
        if tag and tag.get("content"):
            return tag["content"].strip()
        return None
    title = (m("og:title") or m(name="twitter:title") or (soup.title.string.strip() if soup.title else ""))
    desc  = (m("og:description") or m(name="description") or "")
    image = (m("og:image") or m(name="twitter:image") or "")
    return {"title": title, "description": desc, "image": image}

def guess_category(title: str) -> str:
    t = (title or "").lower()
    if any(k in t for k in ["bitcoin","btc","crypto","ethereum","eth","solana","token"]): return "crypto"
    if any(k in t for k in ["ai","artificial intelligence","openai","gpt","model"]):    return "ai"
    return "news"

def write_post(item: dict, meta: dict, source_name: str) -> str:
    pathlib.Path(OUT_DIR).mkdir(parents=True, exist_ok=True)

    title     = meta.get("title") or item.get("title") or "Untitled"
    summary   = meta.get("description") or item.get("summary", "")
    image_url = meta.get("image") or ""
    source_url = item.get("link")

    try:
        dt = datetime.datetime(*item.published_parsed[:6], tzinfo=datetime.timezone.utc)
    except Exception:
        dt = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
    date_iso = dt.isoformat().replace("+00:00", "Z")

    category = guess_category(title)
    tags = []
    if category == "crypto":
        if "bitcoin" in title.lower(): tags.append("bitcoin")
        tags.append("crypto")
    elif category == "ai":
        tags.append("ai")

    slug = f"{dt.date().isoformat()}-{slugify(title)}"
    out_path = os.path.join(OUT_DIR, f"{slug}.md")

    front = [
        "---",
        f'title: "{esc(title)}"',
        f"date: {date_iso}",
    ]
    if summary:
        front.append(f'summary: "{esc(summary)[:240]}"')
    front.append(f'category: "{category}"')
    if tags:
        front.append("tags: [" + ", ".join([f'"{esc(t)}"' for t in tags]) + "]")
    if image_url:
        front.append(f'image_url: "{image_url}"')
    front.append(f'source: "{esc(source_name)}"')
    if source_url:
        front.append(f'source_url: "{source_url}"')
    front.append("---")

    body = "Auto-imported summary based on publicly available sources."

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(front) + "\n\n" + body + "\n")

    print(f"[ok]  Wrote: {out_path}")
    return out_path

def scrape_feed(feed_url: str, source_name: str, db: dict, max_new: int) -> int:
    count = 0
    feed = feedparser.parse(feed_url)
    for entry in feed.entries:
        link = entry.get("link")
        if not link: continue
        uid = hashlib.md5(link.encode()).hexdigest()
        if uid in db["seen"]: continue
        meta = fetch_meta(link)
        write_post(entry, meta, source_name)
        db["seen"].append(uid)
        count += 1
        if count >= max_new: break
    return count

def main():
    db = load_db()
    total_new = 0
    for src in SOURCES:
        if total_new >= MAX_ITEMS_PER_RUN: break
        print(f"[i]  Scraping: {src['name']} ({src['rss']})")
        made = scrape_feed(src["rss"], src["name"], db, MAX_ITEMS_PER_RUN - total_new)
        total_new += made
    save_db(db)
    print(f"[done] Generated {total_new} post(s).")

if __name__ == "__main__":
    main()

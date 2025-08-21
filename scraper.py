#!/usr/bin/env python3
import hashlib, json, re, time, os, pathlib, textwrap, datetime
import feedparser, requests
from bs4 import BeautifulSoup

# ======= KONFIG =======
SOURCES = [
  # dodaš/mičeš kako želiš – počnimo s par crypto/tech vijesti s dobrim RSS-om
  {"name": "Reuters Crypto", "rss": "https://feeds.reuters.com/reuters/technologyNews"},
  {"name": "CoinDesk",       "rss": "https://www.coindesk.com/arc/outboundfeeds/rss/"}
]
OUT_DIR = "content/en/news"
DB_FILE = ".scrape_seen.json"
USER_AGENT = "MetaAdvisorBot/1.0 (+https://metaadvisor.eu)"
MAX_ITEMS_PER_RUN = 8  # da ne zatrpamo
TIMEZONE = "UTC"       # po želji promijeni

# jednostavna kategorizacija po ključnim riječima
def guess_category(title):
    t = title.lower()
    if any(k in t for k in ["bitcoin","btc","crypto","ethereum","eth","solana","token"]):
        return "crypto"
    if any(k in t for k in ["ai","artificial intelligence","openai","model","gpt"]):
        return "ai"
    return "news"

def slugify(s):
    s = re.sub(r"[^a-zA-Z0-9\- ]", "", s).strip().lower()
    s = re.sub(r"\s+", "-", s)
    return s[:80] or hashlib.md5(s.encode()).hexdigest()[:8]

def load_db():
    if os.path.exists(DB_FILE):
        return json.load(open(DB_FILE, "r", encoding="utf-8"))
    return {"seen": []}

def save_db(db):
    json.dump(db, open(DB_FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

def fetch_meta(url):
    try:
        resp = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=12)
        resp.raise_for_status()
    except Exception:
        return {}
    soup = BeautifulSoup(resp.text, "html.parser")
    def meta(property=None, name=None):
        if property:
            tag = soup.find("meta", attrs={"property": property})
            if tag and tag.get("content"): return tag["content"].strip()
        if name:
            tag = soup.find("meta", attrs={"name": name})
            if tag and tag.get("content"): return tag["content"].strip()
        return None
    og_title = meta(property="og:title") or meta(name="twitter:title")
    og_desc  = meta(property="og:description") or meta(name="description") or ""
    og_img   = meta(property="og:image") or meta(name="twitter:image")
    return {"title": og_title, "description": og_desc, "image": og_img}

def write_post(item, meta, source_name):
    pathlib.Path(OUT_DIR).mkdir(parents=True, exist_ok=True)
    title = meta.get("title") or item.get("title") or "Untitled"
    summary = meta.get("description") or item.get("summary","")
    image_url = meta.get("image") or ""
    source_url = item.get("link")
    date = item.get("published", "") or item.get("updated","")
    if not date:
        date = datetime.datetime.utcnow().isoformat() + "Z"
    # ISO format normalizacija
    try:
        dt = datetime.datetime(*item.published_parsed[:6], tzinfo=datetime.timezone.utc)
    except Exception:
        dt = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
    date_iso = dt.isoformat().replace("+00:00","Z")

    category = guess_category(title)
    tags = []
    if category == "crypto":
        if "bitcoin" in title.lower(): tags += ["bitcoin"]
        tags += ["crypto"]
    elif category == "ai":
        tags += ["ai"]

    slug = f"{dt.date().isoformat()}-{slugify(title)}"
    path = os.path.join(OUT_DIR, f"{slug}.md")

    fm = f"""---
title: "{title.replace('"','\\\"')}"
date: {date_iso}
summary: "{summary.replace('"','\\\"')[:240]}"
category: "{category}"
tags: {json.dumps(tags)}
image_url: "{image_url or ''}"
image_alt: "{title.replace('"','\\\"')}"
source: "{source_name}"
source_url: "{source_url}"
---
"""

    body = "Auto-generated summary based on publicly available sources."
    open(path, "w", encoding="utf-8").write(fm + "\n" + body + "\n")
    return path

def main():
    db = load_db()
    new_count = 0

    for src in SOURCES:
        feed = feedparser.parse(src["rss"])
        for entry in feed.entries[:12]:
            link = entry.get("link")
            if not link: continue
            uid = hashlib.md5(link.encode()).hexdigest()
            if uid in db["seen"]: continue
            meta = fetch_meta(link)
            path = write_post(entry, meta, src["name"])
            db["seen"].append(uid)
            new_count += 1
            if new_count >= MAX_ITEMS_PER_RUN:
                break
        if new_count >= MAX_ITEMS_PER_RUN:
            break

    save_db(db)
    print(f"Generated {new_count} posts.")

if __name__ == "__main__":
    main()

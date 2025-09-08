#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, re, json, time, hashlib, datetime
from pathlib import Path
from urllib.parse import urljoin, urlparse
import requests, feedparser
from bs4 import BeautifulSoup

# ============ KONFIG ============
BASE_URL    = "https://metaadvisor.eu"
USER_AGENT  = f"MetaAdvisorBot/2.0 (+{BASE_URL})"
TIMEOUT     = 15
OUT_INBOX   = Path("content/_inbox")
DB_FILE     = Path(".scrape_seen.json")

# Minimalni “editorial” filter (možeš proširiti)
MAX_ITEMS      = 1  # dnevni cap
ALLOW_SOURCES  = {"TechCrunch","The Guardian Tech","Reuters Tech","CoinDesk","Decrypt"}
BLOCK_TOPICS   = {"dogecoin","xrp","meme coin","shiba inu"}
REQUIRE_ANY    = {"bitcoin","ethereum","ai","web3","crypto"}

SOURCES = [
    {"name": "Reuters Tech",      "rss": "https://feeds.reuters.com/reuters/technologyNews", "limit": 2},
    {"name": "The Guardian Tech", "rss": "https://www.theguardian.com/uk/technology/rss",    "limit": 2},
    {"name": "TechCrunch",        "rss": "https://techcrunch.com/feed/",                     "limit": 2},
    {"name": "CoinDesk",          "rss": "https://www.coindesk.com/arc/outboundfeeds/rss/",  "limit": 3},
    {"name": "Decrypt",           "rss": "https://decrypt.co/feed",                          "limit": 1},
]
# =================================

HEADERS = {"User-Agent": USER_AGENT}
OUT_INBOX.mkdir(parents=True, exist_ok=True)

def load_db():
    if DB_FILE.exists():
        try: return json.load(DB_FILE.open("r", encoding="utf-8"))
        except: pass
    return {"seen": []}

def save_db(db): json.dump(db, DB_FILE.open("w", encoding="utf-8"), ensure_ascii=False, indent=2)

def esc(s): return (s or "").replace('"', "'").replace("\n", " ").strip()

def slugify_en(s, max_len=80):
    s = re.sub(r"[^a-zA-Z0-9\- ]", "", s or "").strip().lower()
    s = re.sub(r"\s+", "-", s)
    return (s[:max_len] or "post").strip("-")

def fetch_html(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        r.raise_for_status()
        r.encoding = r.apparent_encoding or "utf-8"
        return r.text
    except Exception:
        return None

def extract_meta(page_url):
    html = fetch_html(page_url)
    if not html: return {}
    soup = BeautifulSoup(html, "html.parser")

    def m(property_name=None, name=None):
        tag = soup.find("meta", attrs={"property": property_name}) if property_name else None
        if not tag and name: tag = soup.find("meta", attrs={"name": name})
        return tag["content"].strip() if tag and tag.get("content") else None

    title = (m("og:title") or m(name="twitter:title") or (soup.title.string.strip() if soup.title else ""))
    desc  = (m("og:description") or m(name="description") or "")
    image = (m("og:image") or m(name="twitter:image") or "")
    if image: image = urljoin(page_url, image)
    return {"title": title, "description": desc, "image": image, "html": html}

def extract_body(html, min_len=400, max_len=1800):
    if not html: return ""
    soup = BeautifulSoup(html, "html.parser")
    node = soup.find("article") or soup.select_one("main, [role=main], .article, .content, .article-content")
    if not node: node = soup
    paras = [p.get_text(" ", strip=True) for p in node.find_all("p")]
    text = "\n\n".join([p for p in paras if len(p) > 40])
    if len(text) < min_len:
        paras = [p.get_text(" ", strip=True) for p in soup.find_all("p")]
        text = "\n\n".join([p for p in paras if len(p) > 40])
    text = text[:max_len].rsplit(" ", 1)[0]
    return text or ""

def guess_category(title):
    t = (title or "").lower()
    if any(k in t for k in ["bitcoin","btc","crypto","ethereum","eth","solana","token"]): return "crypto"
    if any(k in t for k in ["ai","artificial intelligence","openai","gpt","model"]):      return "ai"
    return "news"

def inbox_path(dt, slug):
    return OUT_INBOX / f"{dt:%Y}" / f"{dt:%m}" / f"{dt:%Y-%m-%d}-{slug}.md"

def write_inbox(dt, payload):
    p = inbox_path(dt, payload["slug"])
    p.parent.mkdir(parents=True, exist_ok=True)
    front = [
        "---",
        f'title: "{esc(payload["title"])}"',
        f"date: {payload['date_iso']}",
        f'category: "{payload["category"]}"',
        f'translationKey: "{payload["tkey"]}"',
        f'source: "{esc(payload["source_name"])}"',
        f'source_url: "{payload["source_url"]}"',
        f'image_url: "{payload["image_url"]}"',
        "tags: [" + ", ".join([f'"{t}"' for t in payload["tags"]]) + "]",
        "_build:",
        "  publishResources: false",
        "  render: never",
        "  list: never",
        "---",
    ]
    body = payload["body"] or (f"Read the full article: {payload['source_url']}")
    p.write_text("\n".join(front) + "\n\n" + body + "\n", encoding="utf-8")
    return p

def passes_filters(title, summary):
    title_l = (title or "").lower()
    sum_l   = (summary or "").lower()
    if not any(k in title_l or k in sum_l for k in REQUIRE_ANY):
        return False
    if any(k in title_l or k in sum_l for k in BLOCK_TOPICS):
        return False
    return True

def process_entry(entry, source_name, db):
    if source_name not in ALLOW_SOURCES: return False
    link = entry.get("link")
    if not link: return False
    uid = hashlib.md5(link.encode()).hexdigest()
    if uid in db["seen"]: return False

    meta = extract_meta(link)
    title = meta.get("title") or entry.get("title") or "Untitled"
    desc  = meta.get("description") or entry.get("summary", "")
    if not passes_filters(title, desc): return False

    try:
        dt = datetime.datetime(*entry.published_parsed[:6], tzinfo=datetime.timezone.utc)
    except Exception:
        dt = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
    date_iso = dt.isoformat().replace("+00:00", "Z")

    body = extract_body(meta.get("html"))
    cat  = guess_category(title)
    tags = []
    if cat == "crypto":
        tags = ["crypto"] + (["bitcoin"] if "bitcoin" in title.lower() else [])
    elif cat == "ai":
        tags = ["ai"]

    slug = slugify_en(title)
    payload = {
        "slug": slug,
        "title": title,
        "date_iso": date_iso,
        "category": cat,
        "tkey": uid,
        "source_name": source_name,
        "source_url": link,
        "image_url": meta.get("image") or "",
        "tags": tags,
        "body": body,
    }
    write_inbox(dt, payload)
    db["seen"].append(uid)
    print(f"[inbox] {source_name} → {dt:%Y-%m-%d}-{slug}")
    return True

def scrape_feed(feed_url, source_name, db, limit):
    made = 0
    feed = feedparser.parse(feed_url)
    for e in feed.entries:
        if made >= limit: break
        if process_entry(e, source_name, db):
            made += 1
            time.sleep(0.5)
    return made

def main():
    db = load_db()
    total = 0
    for src in SOURCES:
        if total >= MAX_ITEMS: break
        left = min(src.get("limit", MAX_ITEMS-total), MAX_ITEMS-total)
        total += scrape_feed(src["rss"], src["name"], db, left)
    save_db(db)
    print(f"[done] Inboxed {total} item(s).")

if __name__ == "__main__":
    main()

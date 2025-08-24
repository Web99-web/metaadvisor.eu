#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, re, json, hashlib, datetime, time
from pathlib import Path
from urllib.parse import urljoin, urlparse
import requests, feedparser, frontmatter
from bs4 import BeautifulSoup

# --- besplatan prevoditelj ---
from googletrans import Translator

# ================== KONFIG ==================
BASE_URL       = "https://metaadvisor.eu"
USER_AGENT     = f"MetaAdvisorBot/1.0 (+{BASE_URL})"
TIMEOUT        = 15

# Gdje spremamo sadržaj (usklađeno s multilang Hugo postavkama)
OUT_EN         = Path("content/en/news")
OUT_DE         = Path("content/de/news")
OUT_HR         = Path("content/hr/news")

# Gdje spremamo lokalne slike (serviraju se s /news/...)
STATIC_NEWS    = Path("static/news")

DB_FILE        = Path(".scrape_seen.json")
MAX_ITEMS      = 12   # ukupno novih po jednoj vožnji (globalni “hard cap”)

SOURCES = [
    # Tehnologija / opći tech
    {"name": "Reuters Tech",      "rss": "https://feeds.reuters.com/reuters/technologyNews", "limit": 2},
    {"name": "The Guardian Tech", "rss": "https://www.theguardian.com/uk/technology/rss",    "limit": 2},
    {"name": "TechCrunch",        "rss": "https://techcrunch.com/feed/",                     "limit": 2},

    # Kripto i blockchain
    {"name": "CoinDesk",          "rss": "https://www.coindesk.com/arc/outboundfeeds/rss/",  "limit": 5},
    {"name": "CoinTelegraph",     "rss": "https://cointelegraph.com/rss",                    "limit": 2},
    {"name": "Decrypt",           "rss": "https://decrypt.co/feed",                          "limit": 2},

    # Financije / biznis (besplatni feedovi)
    {"name": "Guardian Business", "rss": "https://www.theguardian.com/uk/business/rss",      "limit": 1},
]
# ============================================

HEADERS = {"User-Agent": USER_AGENT}
STATIC_NEWS.mkdir(parents=True, exist_ok=True)
for p in (OUT_EN, OUT_DE, OUT_HR):
    p.mkdir(parents=True, exist_ok=True)

# ---------- util ----------
def esc(s: str) -> str:
    if not s: return ""
    return s.replace('"', "'").replace("\n", " ").strip()

def slugify(s: str, max_len: int = 80) -> str:
    s = re.sub(r"[^a-zA-Z0-9\- ]", "", s or "").strip().lower()
    s = re.sub(r"\s+", "-", s)
    return (s[:max_len] or "post").strip("-")

def load_db() -> dict:
    if DB_FILE.exists():
        try:
            return json.load(DB_FILE.open("r", encoding="utf-8"))
        except Exception:
            pass
    return {"seen": []}

def save_db(db: dict) -> None:
    json.dump(db, DB_FILE.open("w", encoding="utf-8"), ensure_ascii=False, indent=2)

def fetch_html(url: str) -> str | None:
    try:
        r = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        r.raise_for_status()
        r.encoding = r.apparent_encoding or "utf-8"
        return r.text
    except Exception:
        return None

def extract_meta(page_url: str) -> dict:
    html = fetch_html(page_url)
    if not html:
        return {}
    soup = BeautifulSoup(html, "html.parser")

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

    # apsolutni URL slike
    if image:
        image = urljoin(page_url, image)

    return {"title": title, "description": desc, "image": image, "html": html}

def extract_article_text(html: str, min_len=400, max_len=1800) -> str:
    if not html:
        return ""
    soup = BeautifulSoup(html, "html.parser")

    candidates = []
    art = soup.find("article")
    if art: candidates.append(art)

    if not candidates:
        for sel in ["main", "[role=main]", ".article", ".post", ".content", ".article-content", ".StoryBodyCompanionColumn"]:
            node = soup.select_one(sel)
            if node:
                candidates.append(node)
                break

    if not candidates:
        candidates.append(soup)

    def collect_paras(node):
        return [p.get_text(" ", strip=True) for p in node.find_all("p")]

    paras = collect_paras(candidates[0])
    text = "\n\n".join([p for p in paras if len(p) > 40])

    if len(text) < min_len:
        more = collect_paras(soup)
        text = "\n\n".join([p for p in more if len(p) > 40])

    text = text[:max_len].rsplit(" ", 1)[0]
    return text or "Auto-imported summary based on publicly available sources."

def guess_category(title: str) -> str:
    t = (title or "").lower()
    if any(k in t for k in ["bitcoin","btc","crypto","ethereum","eth","solana","token"]): return "crypto"
    if any(k in t for k in ["ai","artificial intelligence","openai","gpt","model"]):    return "ai"
    return "news"

# --- download slike u static/news ---
def download_image_to_static(image_url: str, slug: str) -> str | None:
    try:
        r = requests.get(image_url, headers=HEADERS, timeout=TIMEOUT)
        r.raise_for_status()
        # ekstenzija iz URL-a (default .jpg)
        path = urlparse(image_url).path
        ext = os.path.splitext(path)[-1].lower()
        if ext not in [".jpg", ".jpeg", ".png", ".webp"]:
            ext = ".jpg"
        filename = f"{slug}{ext}"
        out_path = STATIC_NEWS / filename
        if not out_path.exists():
            with open(out_path, "wb") as f:
                f.write(r.content)
        return f"/news/{filename}"
    except Exception:
        return None

# --- prijevod: Google Translate (besplatno) ---
translator = Translator()

def translate(text: str, dest_lang: str) -> str:
    """dest_lang: 'de' ili 'hr'"""
    if not text:
        return text
    try:
        # mali retry zbog povremenih blokada
        for _ in range(2):
            try:
                res = translator.translate(text, dest=dest_lang)
                return res.text.strip()
            except Exception:
                time.sleep(0.8)
        return text  # fallback: vrati ENG ako previše griješi
    except Exception:
        return text

# --- zapis .md ---
def write_markdown(out_dir: Path, slug: str, data: dict) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{slug}.md"

    fm = [
        "---",
        f'title: "{esc(data["title"])}"',
        f"date: {data['date_iso']}",
        f'category: "{data["category"]}"',
        f'translationKey: "{data["translationKey"]}"',
        f'source: "{esc(data["source_name"])}"',
        f'source_url: "{data["source_url"]}"',
    ]
    if data.get("summary"):
        fm.append(f'summary: "{esc(data["summary"])[:240]}"')
    if data.get("tags"):
        fm.append("tags: [" + ", ".join([f'"{esc(t)}"' for t in data["tags"]]) + "]")
    if data.get("image_url"):
        fm.append(f'image_url: "{data["image_url"]}"')  # zapisujemo image_url (jedna istina)
    fm.append("---")

    body = data.get("body", "")
    with path.open("w", encoding="utf-8") as f:
        f.write("\n".join(fm) + "\n\n" + body + "\n")
    return path

# --- obrada jednog feed entryja ---
def process_entry(entry: dict, source_name: str, db: dict) -> bool:
    link = entry.get("link")
    if not link:
        return False

    uid = hashlib.md5(link.encode()).hexdigest()
    if uid in db["seen"]:
        return False

    meta = extract_meta(link)
    title_en   = meta.get("title") or entry.get("title") or "Untitled"
    summary_en = meta.get("description") or entry.get("summary", "")
    image_url  = meta.get("image") or ""

    # datum
    try:
        dt = datetime.datetime(*entry.published_parsed[:6], tzinfo=datetime.timezone.utc)
    except Exception:
        dt = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
    date_iso = dt.isoformat().replace("+00:00", "Z")

    # tekst tijela
    body_en = extract_article_text(meta.get("html"))

    category = guess_category(title_en)
    tags = []
    if category == "crypto":
        if "bitcoin" in title_en.lower(): tags.append("bitcoin")
        tags.append("crypto")
    elif category == "ai":
        tags.append("ai")

    slug_base = f"{dt.date().isoformat()}-{slugify(title_en)}"
    tkey = uid  # stabilan ključ za povezivanje prijevoda

    # slika → pokušaj skinuti lokalno; ako ne uspije, ostavi remote URL
    local_img = download_image_to_static(image_url, slug_base) if image_url else None
    image_final = local_img or image_url or ""

    base_payload = {
        "date_iso": date_iso,
        "category": category,
        "tags": tags,
        "image_url": image_final,          # ključ standardiziran
        "source_name": source_name,
        "source_url": link,
        "translationKey": tkey,
    }

    # EN
    en_payload = {
        **base_payload,
        "title": title_en,
        "summary": summary_en,
        "body": body_en or f"Read the full article: {link}",
    }
    write_markdown(OUT_EN, slug_base, en_payload)

    # DE (besplatni prijevod)
    title_de   = translate(title_en, "de")
    summary_de = translate(summary_en, "de")
    body_de    = translate(body_en, "de") if body_en else translate(f"Read the full article: {link}", "de")
    de_payload = {
        **base_payload,
        "title": title_de,
        "summary": summary_de,
        "body": body_de,
    }
    write_markdown(OUT_DE, slug_base, de_payload)

    # HR (besplatni prijevod)
    title_hr   = translate(title_en, "hr")
    summary_hr = translate(summary_en, "hr")
    body_hr    = translate(body_en, "hr") if body_en else translate(f"Read the full article: {link}", "hr")
    hr_payload = {
        **base_payload,
        "title": title_hr,
        "summary": summary_hr,
        "body": body_hr,
    }
    write_markdown(OUT_HR, slug_base, hr_payload)

    db["seen"].append(uid)
    print(f"[ok] {source_name} → {slug_base} (EN/DE/HR)")
    return True

def scrape_feed(feed_url: str, source_name: str, db: dict, remaining: int) -> int:
    """remaining = per-source limit"""
    made = 0
    feed = feedparser.parse(feed_url)
    for entry in feed.entries:
        if made >= remaining:
            break
        try:
            if process_entry(entry, source_name, db):
                made += 1
                time.sleep(0.5)  # pristojno prema izvorima
        except Exception as e:
            print("[warn]", e)
    return made

def main():
    db = load_db()
    total_new = 0
    for src in SOURCES:
        if total_new >= MAX_ITEMS:
            break
        per_src_limit = src.get("limit", MAX_ITEMS - total_new)
        per_src_limit = min(per_src_limit, MAX_ITEMS - total_new)  # ne probij globalni cap
        print(f"[i]  {src['name']} ({src['rss']}) limit={per_src_limit}")
        total_new += scrape_feed(src["rss"], src["name"], db, per_src_limit)
    save_db(db)
    print(f"[done] Generated {total_new} post(s) (x3 languages).")

if __name__ == "__main__":
    main()

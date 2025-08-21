#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# scraper.py – minimalni scraper: uzme listu URL-ova, izvuče meta title/description/image
# i generira Hugo .md postove u content/news/

import os
import re
import datetime
import unicodedata
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

# Gdje pišemo .md
OUT_DIR = os.path.join("content", "news")

# URL-ovi za probu (STAVI STVARNE LINKOVE!)
URLS = [
    # Primjeri – zamijeni stvarnim i dostupnim URL-ovima
    # npr. s vijesti koje smiješ scrapati:
    # "https://www.reuters.com/technology/...", 
    # "https://www.coindesk.com/markets/2025/08/20/bitcoin-.../",
]

# ---------- helpers ----------

def slugify(value: str) -> str:
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^a-zA-Z0-9\\- ]+', '', value).strip().lower()
    value = re.sub(r'\\s+', '-', value)
    return value or "post"

def get_meta(soup, *names):
    # traži og:*, twitter:*, name=description...
    for name in names:
        tag = soup.find("meta", attrs={"property": name})
        if tag and tag.get("content"):
            return tag["content"].strip()
        tag = soup.find("meta", attrs={"name": name})
        if tag and tag.get("content"):
            return tag["content"].strip()
    return None

def pick_category(tags_lower):
    if any(t in tags_lower for t in ("bitcoin", "crypto", "blockchain", "eth", "btc")):
        return "crypto"
    return "news"

def guess_tags(text: str):
    text = text.lower()
    tags = []
    for kw in ["bitcoin", "crypto", "ethereum", "price", "market", "blockchain", "ai", "technology"]:
        if kw in text:
            tags.append(kw)
    return sorted(set(tags))[:6]

def fetch(url: str):
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MetaAdvisorBot/0.1)"}
    r = requests.get(url, headers=headers, timeout=20)
    r.raise_for_status()
    return r.text

# ---------- core ----------

def scrape_one(url: str):
    try:
        html = fetch(url)
        soup = BeautifulSoup(html, "html.parser")

        title = (get_meta(soup, "og:title", "twitter:title")
                 or (soup.title.string.strip() if soup.title else None)
                 or "Untitled")

        summary = get_meta(soup, "og:description", "description", "twitter:description") or ""
        image_url = get_meta(soup, "og:image", "twitter:image")

        host = urlparse(url).netloc

        joined_text = " ".join([title, summary, host])
        tags = guess_tags(joined_text)
        category = pick_category(" ".join(tags))

        today = datetime.date.today().isoformat()
        slug = slugify(title)
        filename = f"{today}-{slug}.md"
        out_path = os.path.join(OUT_DIR, filename)

        if not os.path.isdir(OUT_DIR):
            os.makedirs(OUT_DIR, exist_ok=True)

        if os.path.exists(out_path):
            print(f"[skip] Already exists: {out_path}")
            return

        # front matter (YAML)
        fm = []
        fm.append("---")
        fm.append(f'title: "{title.replace(\'"\', "\'")}"')
        fm.append(f"date: {today}")
        if summary:
            fm.append(f'summary: "{summary.replace(\'"\', "\'")}"')
        fm.append(f'category: "{category}"')
        if tags:
            fm.append("tags: [" + ", ".join([f'\"{t}\"' for t in tags]) + "]")
        if image_url:
            fm.append(f'image_url: "{image_url}"')
        fm.append(f'source: "{host}"')
        fm.append(f'source_url: "{url}"')
        fm.append("---")
        body = "Auto-imported summary from source. Edit/expand content if needed."

        with open(out_path, "w", encoding="utf-8") as f:
            f.write("\\n".join(fm) + "\\n\\n" + body + "\\n")

        print(f"[ok] Wrote: {out_path}")
    except Exception as e:
        print(f"[err] {url} -> {e}")

def main():
    for u in URLS:
        scrape_one(u)

if __name__ == "__main__":
    main()

# scraper.py
# Minimal scraper: uzme listu URL-ova, izvuče meta title/description/image
# i generira Hugo .md postove u content/news/

OUT_DIR = os.path.join("content", "news")


from bs4 import BeautifulSoup
import requests, re, os, datetime, unicodedata
from urllib.parse import urlparse

# 1) URL-ovi za probu (zamijeni/održi listu kakvu želiš)
URLS = [
    # Primjeri (stavi stvarne linkove koje smiješ scrapati):
    "https://www.reuters.com/markets/asia/bitcoin-surges-.../",     # zamijeni stvarnim
    "https://www.coindesk.com/markets/2025/08/20/bitcoin-.../",    # zamijeni stvarnim
]

# 2) Folder gdje pišemo .md fajlove
OUT_DIR = "content/news"

# 3) Pomoćne funkcije
def slugify(value: str) -> str:
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^a-zA-Z0-9\- ]+', '', value).strip().lower()
    value = re.sub(r'\s+', '-', value)
    return value or "post"

def get_meta(soup, *names):
    # traži og:*, twitter:*, name=description...
    for name in names:
        # property (og:title, og:description...)
        tag = soup.find("meta", attrs={"property": name})
        if tag and tag.get("content"):
            return tag["content"].strip()
        # name (description, twitter:title...)
        tag = soup.find("meta", attrs={"name": name})
        if tag and tag.get("content"):
            return tag["content"].strip()
    return None

def pick_category(tags_lower):
    # vrlo grubo: pogledaj riječi i predloži kategoriju
    if any(t in tags_lower for t in ("bitcoin", "crypto", "blockchain", "eth", "btc")):
        return "crypto"
    return "news"

def guess_tags(text: str):
    text = text.lower()
    tags = []
    for kw in ["bitcoin", "crypto", "ethereum", "price", "market", "blockchain", "ai", "technology"]:
        if kw in text:
            tags.append(kw)
    # unikati + max 6
    return sorted(list(set(tags)))[:6]

def fetch(url: str):
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MetaAdvisorBot/0.1)"}
    r = requests.get(url, headers=headers, timeout=20)
    r.raise_for_status()
    return r.text

def scrape_one(url: str):
    try:
        html = fetch(url)
        soup = BeautifulSoup(html, "html.parser")

        # title
        title = (get_meta(soup, "og:title", "twitter:title") 
                 or (soup.title.string.strip() if soup.title else None)
                 or "Untitled")
        # description/summary
        summary = get_meta(soup, "og:description", "description", "twitter:description") or ""
        # image
        image_url = get_meta(soup, "og:image", "twitter:image")

        # source host (npr. reuters.com)
        host = urlparse(url).netloc

        # guess tags/category
        joined_text = " ".join([title, summary, host])
        tags = guess_tags(joined_text)
        category = pick_category(" ".join(tags))

        # datum danas (možeš promijeniti na datum iz članka ako ga izvučeš)
        today = datetime.date.today().isoformat()
        slug = slugify(title)
        filename = f"{today}-{slug}.md"
        out_path = os.path.join(OUT_DIR, filename)

        if not os.path.isdir(OUT_DIR):
            os.makedirs(OUT_DIR, exist_ok=True)

        if os.path.exists(out_path):
            print(f"[skip] Already exists: {out_path}")
            return

        front_matter = []
        front_matter.append("---")
        front_matter.append(f'title: "{title.replace(\'"\', "\'")}"')
        front_matter.append(f"date: {today}")
        if summary:
            front_matter.append(f'summary: "{summary.replace(\'"\', "\'')}"')
        front_matter.append(f'category: "{category}"')
        if tags:
            front_matter.append("tags: [" + ", ".join([f'"{t}"' for t in tags]) + "]")
        if image_url:
            front_matter.append(f'image_url: "{image_url}"')
        front_matter.append(f'source: "{host}"')
        front_matter.append(f'source_url: "{url}"')
        front_matter.append("---\n")

        body = "Auto-imported summary from source. Edit/expand content if needed.\n"

        with open(out_path, "w", encoding="utf-8") as f:
            f.write("\n".join(front_matter))
            f.write(body)

        print(f"[ok] Wrote: {out_path}")
    except Exception as e:
        print(f"[err] {url} -> {e}")

def main():
    for u in URLS:
        scrape_one(u)

if __name__ == "__main__":
    main()

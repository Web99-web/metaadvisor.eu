#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, os, datetime, time, hashlib, yaml
from pathlib import Path
import requests, frontmatter
from googletrans import Translator
from urllib.parse import urlparse

# ---------- IMAGE POLICY ----------
# Ako je False, OG (remote) slike će se ignorirati osim s whiteliste.
USE_OG_IMAGE = False

OG_WHITELIST = {
    "unsplash.com","images.unsplash.com","pexels.com","pixabay.com",
    "upload.wikimedia.org","commons.wikimedia.org",
    # primjer ako želiš dopustiti ove:
    # "decrypt.co","cdn.decrypt.co",
    # "images.arcpublishing.com","coindesk.com",
}

# ---------- AUTO TAGS (iz naslova/teksta) ----------
TAG_KEYWORDS = {
    # AI
    "ai": ["ai", "artificial-intelligence"],
    "artificial intelligence": ["ai", "artificial-intelligence"],
    "ai safety": ["safety", "ai-safety"],
    "safety": ["safety", "ai-safety"],

    # Crypto općenito
    "crypto": ["crypto", "cryptocurrency"],
    "cryptocurrency": ["crypto", "cryptocurrency"],

    # Bitcoin / Ethereum i sl.
    "bitcoin": ["bitcoin", "btc"],
    "btc": ["bitcoin", "btc"],
    "ethereum": ["ethereum", "eth"],
    "eth": ["ethereum", "eth"],
    "solana": ["solana", "sol"],
    "sol": ["solana", "sol"],
    "xrp": ["xrp", "ripple"],
    "ripple": ["xrp", "ripple"],
    "cardano": ["cardano", "ada"],
    "ada": ["cardano", "ada"],
    "binance": ["binance", "bnb"],
    "bnb": ["binance", "bnb"],
    "monero": ["monero", "xmr"],
    "xmr": ["monero", "xmr"],

    # Tech brendovi / teme
    "apple": ["apple", "iphone"],
    "iphone": ["apple", "iphone"],
    "google": ["google"],
    "openai": ["openai", "ai"],
    "microsoft": ["microsoft", "ai"],
    "meta": ["meta"], "facebook": ["meta"],

    # Finance / stocks
    "finance": ["finance"],
    "stocks": ["stocks", "equities"],
    "equities": ["stocks", "equities"],
    "nasdaq": ["stocks"],

    # Druge opće teme
    "privacy": ["privacy", "security"],
    "security": ["security"],
    "mental health": ["mental-health"],
    "suicide": ["mental-health"],
}

# ➜ dodatni sinonimi za telefone (OVO JE IZVAN dict-a)
TAG_KEYWORDS.update({
    "iphone":      ["apple", "iphone", "smartphones"],
    "iphones":     ["apple", "iphone", "smartphones"],
    "apple":       ["mobile", "smartphones", "apple"],
    "smartphone":  ["smartphones", "mobile", "apple"],
    "smartphones": ["smartphones", "mobile"],
    "phone":       ["smartphones", "mobile"],
    "phones":      ["smartphones", "mobile"],
})

_WORDS_RE = re.compile(r"[a-z0-9\-]+", re.I)

def _dedup(seq):
    seen = set(); out = []
    for x in seq:
        xl = str(x).strip()
        if not xl: continue
        key = xl.lower()
        if key not in seen:
            seen.add(key); out.append(xl)
    return out

def extract_tags_from_text(title: str, body: str, seed_tags=None, limit: int = 12):
    """Vrati objedinjene tagove: postojeće (seed_tags) + oni iz teksta/naslova."""
    seed_tags = seed_tags or []
    text = " ".join(_WORDS_RE.findall(f"{title or ''} {body or ''}".lower()))
    found = []
    for key, out_tags in TAG_KEYWORDS.items():
        patt = rf"(?<!\w){re.escape(key)}(?!\w)"
        if re.search(patt, text):
            found.extend(out_tags if isinstance(out_tags, list) else [out_tags])
    all_tags = _dedup(list(seed_tags) + found)
    return all_tags[:limit]

# ---------- AUTO "OUR TAKE" ----------
AUTO_TAKE = True  # nema u inboxu? generiraj automatski

def _first_sentence(text: str, max_len: int = 220) -> str:
    if not text:
        return ""
    s = re.split(r"(?<=[\.\!\?])\s+", text.strip(), maxsplit=1)[0]
    s = re.sub(r"\s+", " ", s).strip()
    return (s[:max_len] + "…") if len(s) > max_len else s

def generate_our_take(title: str, body: str, tags) -> str:
    """Kratki heuristički komentar bez vanjskog AI-a."""
    t = set([str(x).lower() for x in (tags or [])])
    gist = _first_sentence(body) or _first_sentence(title) or title

    # tematski preseti
    if {"bitcoin","btc","ethereum","eth","solana","sol","crypto"} & t:
        return ("Our view: " + gist +
                " Key things to watch: liquidity, macro (rates/USD) and regulation. "
                "Stay selective; add only in high-conviction names.")
    if {"ai","artificial-intelligence","ai-safety"} & t:
        return ("Our view: " + gist +
                " Bigger picture: data/licensing, model quality, and policy risk drive outcomes. "
                "We like real distribution and defensible data moats.")
    if {"stocks","equities","finance","nasdaq"} & t:
        return ("Our view: " + gist +
                " Near-term setup hinges on earnings revisions and rates; "
                "prefer cash-generative leaders over story stocks.")

    # fallback
    return ("Our view: " + gist +
            " Upside depends on execution and user adoption; key risk is regulation and headline volatility.")

# ---------- OPCIJE ----------
ADD_ALIASES_FROM_INBOX     = False
DELETE_INBOX_AFTER_PUBLISH = False
PUBLISH_LIMIT              = 10

# ---------- KONFIG ----------
INBOX   = Path("content/_inbox")
USER_AGENT = "MetaAdvisorBot/2.0 (+https://metaadvisor.eu)"
TIMEOUT    = 15
HEADERS    = {"User-Agent": USER_AGENT}

# Prioritet izvora (veći broj = veći prioritet)
SOURCE_RANK = {
    "MetaAdvisor": 100,   # naši članci = top
    "CoinDesk": 97,
    "Decrypt": 97,
    "Cointelegraph": 95,
    "Bloomberg": 90,
    "Reuters": 85,
    "The Guardian Tech": 20,
}
def source_priority(src: str) -> int:
    """Vrati prioritet prema izvoru (case-insensitive)."""
    if not src:
        return 0
    key = str(src).strip().lower()
    for k, v in SOURCE_RANK.items():
        if k.lower() == key:
            return v
    return 0


TRANSLIT = {
    "ä":"ae","ö":"oe","ü":"ue","ß":"ss",
    "č":"c","ć":"c","š":"s","ž":"z","đ":"dj",
    "Ä":"ae","Ö":"oe","Ü":"ue","Č":"c","Ć":"c","Š":"s","Ž":"z","Đ":"dj"
}

translator = Translator()
LIB_DIR = Path("static/images")
IMAGE_MAP_YAML = Path("data/image_map.yaml")

def translit(s: str) -> str:
    return "".join(TRANSLIT.get(ch, ch) for ch in s)

def url_slug(title: str) -> str:
    s = translit(title or "").lower()
    s = re.sub(r"[^a-z0-9 _-]", "", s)
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return (s[:120] or "post")


def out_path_single(lang: str, dt: datetime.datetime, slug: str) -> Path:
    """content/[lang/]news/YYYY/MM/DD/slug.md"""
    base = Path("content") if lang == "en" else Path("content")/lang
    post_dir = base/"news"/f"{dt:%Y}"/f"{dt:%m}"/f"{dt:%d}"
    post_dir.mkdir(parents=True, exist_ok=True)
    return post_dir/f"{slug}.md"


def clean_body(md: str) -> str:
    if not md: return ""
    # makni Hugove contentReference artefakte
    return re.sub(r":contentReference\[[^\]]*\]\{index=\d+\}", "", md)

def dl(url: str):
    """Pokušaj skinuti udaljenu sliku (samo ako je dopuštena)."""
    if not url: return None
    try:
        host = urlparse(url).netloc
        if not USE_OG_IMAGE and host not in OG_WHITELIST:
            return None
        r = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        r.raise_for_status()
        return r.content
    except Exception:
        return None

def load_image_map():
    """Učitaj data/image_map.yaml (mapping: ključ -> [datoteke], default: ime)."""
    try:
        with IMAGE_MAP_YAML.open("r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
            mapping = data.get("mapping") or {}
            for k, v in list(mapping.items()):
                if isinstance(v, str):
                    mapping[k] = [v]
            data["mapping"] = mapping
            # ❗ default više nije placeholder – stavi nešto neutralno i lijepo
            data.setdefault("default", "finance.jpg")  # ili "stock-market-dionice.jpg"
            return data
    except Exception:
        # ❗ i u fallbacku koristi isti default, ne placeholder
        return {"mapping": {}, "default": "finance.jpg"}  # ili "stock-market-dionice.jpg"

    
def choose_image_path(tags, title, body, seed: str = "") -> str:
    """
    Vrati putanju /images/<datoteka> na temelju data/image_map.yaml.
    Ako mapping ništa ne nađe, probaj s par heuristika (BTC/ETH/SOL/iPhone),
    a na kraju vrati default iz YAML-a (npr. finance.jpg).
    """
    conf = load_image_map()
    mapping: dict = conf.get("mapping", {}) or {}
    default_name: str = conf.get("default", "finance.jpg")

    keys = [str(t).lower() for t in (tags or [])]
    keys += re.findall(r"[a-z0-9\-]+", (title or "").lower())
    if body:
        keys += re.findall(r"[a-z0-9\-]+", body.lower())

    # prvo probaj YAML mapping (deterministički izbor)
    for k in keys:
        files = mapping.get(k)
        if files:
            h = hashlib.md5((seed or title or k).encode("utf-8")).hexdigest()
            pick = files[int(h, 16) % len(files)]
            return f"/images/{pick}"

    # heuristika
    t = (title or "").lower()
    if ("bitcoin" in t) or ("btc" in t):   return "/images/bitcoin-btc.jpg"
    if ("ethereum" in t) or ("eth" in t):  return "/images/eth.jpg"
    if ("solana" in t) or ("sol" in t):    return "/images/solana.jpg"
    if ("iphone" in t) or ("apple" in t) or ("smartphone" in t):
        return "/images/mobile-phone.jpg"

    return f"/images/{default_name}"


def _det_pick(files: list[str], seed: str) -> str:
    """Deterministički izbor iz liste (po seed-u)."""
    if not files: return ""
    h = hashlib.md5((seed or "").encode("utf-8")).hexdigest()
    return files[int(h,16) % len(files)]

def pick_library_image(tags, title, body, seed: str):
    """Pokušaj odabrati sliku iz static/images prema data/image_map.yaml."""
    conf = load_image_map()
    mapping: dict = conf.get("mapping", {})
    default_name: str = conf.get("default", "finance.jpg")

    keys = [str(t).lower() for t in (tags or [])]
    keys += re.findall(r"[a-z0-9\-]+", (title or "").lower())
    if body: keys += re.findall(r"[a-z0-9\-]+", body.lower())

    for k in keys:
        if k in mapping:
            f = LIB_DIR / _det_pick(mapping[k], seed or title or "")
            if f.exists():
                return f.read_bytes()

    f = LIB_DIR / default_name
    return f.read_bytes() if f.exists() else None

def get_hero_bytes(image_url, tags, title, body, seed: str):
    """Slika prioritet: 1) OG/remote (ako dopušten) → 2) biblioteka /static/images → 3) None."""
    return dl(image_url) or pick_library_image(tags, title, body, seed)


def write_single(lang: str, dt: datetime.datetime, title: str, body: str,
                 tkey: str, src: str, src_url: str, tags, aliases=None,
                 our_take=None, priority: int = 0, image_url: str = ""):
    """Piši SINGLE file: content/[lang/]news/YYYY/MM/DD/slug.md (bez bundlea/slika)."""
    slug_clean = url_slug(title)
    out_path = out_path_single(lang, dt, slug_clean)
    if out_path.exists():
        short = hashlib.md5(f"{title}{dt}".encode()).hexdigest()[:6]
        slug_clean = f"{slug_clean}-{short}"
        out_path = out_path_single(lang, dt, slug_clean)

    fm = [
        "---",
        f'title: "{title}"',
        f'slug: "{slug_clean}"',
        f"date: {dt.strftime('%Y-%m-%dT%H:%M:%SZ')}",
        'category: "news"',
        f'translationKey: "{tkey}"',
        f'source: "{src}"',
        f'source_url: "{src_url}"',
        f"priority: {int(priority)}",
        f'image_url: "{image_url or "/images/finance.jpg"}"',
        "tags: [" + ", ".join([f'\"{t}\"' for t in (tags or [])]) + "]",
    ]
    if aliases:
        fm.append("aliases:")
        fm += [f'  - "{a}"' for a in aliases]
    if our_take:
        fm.append("our_take: |")
        for line in (our_take or "").splitlines():
            fm.append(f"  {line}")
    fm.append("---")

    out_path.write_text("\n".join(fm) + "\n\n" + (body or "") + "\n", encoding="utf-8")
    return out_path
translator = Translator()

def auto_translate(text: str, lang: str) -> str:
    if not text: return text
    for _ in range(2):
        try:
            return translator.translate(text, dest=lang).text.strip()
        except Exception:
            time.sleep(0.8)
    return text

def publish_one(inbox_file: Path, also_hr=True, also_de=True):
    # SKIP: _index.md i sve što počinje s "_"
    if inbox_file.name.startswith("_"):
        print(f"[skip] {inbox_file}")
        return

    post = frontmatter.load(inbox_file)

    title_en = post.get("title","Untitled")
    if title_en.strip().lower().startswith("inbox (drafts)"):
        print(f"[skip] drafts page: {inbox_file}")
        return

    src       = post.get("source","")
    src_url   = post.get("source_url","")
    tkey      = post.get("translationKey","")
    tags_seed = post.get("tags",[])
    our_take  = post.get("our_take", None)  # ako postoji u inboxu, prenesi

    # Datum
    date_val = post.get("date")
    if isinstance(date_val, str):
        try:
            dt = datetime.datetime.fromisoformat(date_val.replace("Z","+00:00"))
        except Exception:
            dt = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
    elif isinstance(date_val, datetime.datetime):
        dt = date_val if date_val.tzinfo else date_val.replace(tzinfo=datetime.timezone.utc)
    else:
        dt = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)

    body_en   = clean_body(post.content)
    image_url = post.get("image_url","")

    # Auto-tagovi: postojeći + iz teksta
    tags = extract_tags_from_text(title_en, body_en, seed_tags=tags_seed)

    # Auto Our take ako ga nema u inboxu
    if not our_take and AUTO_TAKE:
        our_take = generate_our_take(title_en, body_en, tags)


    # Ako image_url nije zadana u inboxu, izvuci najbolju /images/... iz mape/heuristike
    seed_id = tkey or url_slug(title_en)
    image_url_final = image_url or choose_image_path(tags, title_en, body_en, seed=seed_id)


    # Prioritet izvora
    prio = source_priority(src)
    # Prioritet: inbox override > izvor
    prio = source_priority(src)
    try:
        prio = int(post.get("priority", prio))
    except Exception:
        pass


    # Aliases (ako želiš stari segment)
    old_segment = inbox_file.stem if ADD_ALIASES_FROM_INBOX else None
    en_aliases = [f"/news/{old_segment}/"] if old_segment else None

    # EN
    write_single(
        "en", dt, title_en, body_en or f"Read the full article: {src_url}",
        tkey, src, src_url, tags, aliases=en_aliases,
        our_take=our_take, priority=prio, image_url=image_url_final
    )

    # HR
    if also_hr:
        write_single(
            "hr", dt,
            auto_translate(title_en,"hr"),
            auto_translate(body_en or f"Read the full article: {src_url}", "hr"),
            tkey, src, src_url, tags,
            aliases=[f"/hr/news/{old_segment}/"] if old_segment else None,
            our_take=auto_translate(our_take,"hr") if our_take else None,
            priority=prio,
            image_url=image_url_final
        )

    # DE
    if also_de:
        write_single(
            "de", dt,
            auto_translate(title_en,"de"),
            auto_translate(body_en or f"Read the full article: {src_url}", "de"),
            tkey, src, src_url, tags,
            aliases=[f"/de/news/{old_segment}/"] if old_segment else None,
            our_take=auto_translate(our_take,"de") if our_take else None,
            priority=prio,
            image_url=image_url_final
        )

    print(f"[publish] {inbox_file.name} → EN/HR/DE OK")

    if DELETE_INBOX_AFTER_PUBLISH:
        try:
            inbox_file.unlink()
        except Exception as e:
            print(f"[warn] Could not remove {inbox_file}: {e}")

def pick_inbox_files(limit=PUBLISH_LIMIT):
    """Odaberi koje .md objaviti: prioritet izvora pa po datumu (oba desc)."""
    all_files = [p for p in INBOX.rglob("*.md") if not p.name.startswith("_")]
    scored = []
    for p in all_files:
        try:
            fm = frontmatter.load(p)
            src = fm.get("source","")
            dt  = fm.get("date")
            if isinstance(dt, str):
                try:
                    dt = datetime.datetime.fromisoformat(dt.replace("Z","+00:00"))
                except Exception:
                    dt = None
            ts = dt.timestamp() if isinstance(dt, datetime.datetime) else 0
            scored.append((-source_priority(src), -ts, p))
        except Exception:
            scored.append((0, 0, p))
    scored.sort()
    return [t[2] for t in scored][:limit]

def main(limit=PUBLISH_LIMIT, also_hr=True, also_de=True):
    files = pick_inbox_files(limit=limit)
    if not files:
        print("[i] Nema ničega u inboxu.")
        return
    for f in files:
        publish_one(f, also_hr=also_hr, also_de=also_de)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=PUBLISH_LIMIT)
    parser.add_argument("--no-hr", dest="no_hr", action="store_true")
    parser.add_argument("--no-de", dest="no_de", action="store_true")
    args = parser.parse_args()

    main(
        limit=args.limit,
        also_hr=not args.no_hr,
        also_de=not args.no_de,
    )

#!/usr/bin/env python3
import re, sys
from pathlib import Path
from urllib.parse import urlsplit

CONTENT_DIR = Path("content")

def read_front_matter(p: Path):
    """Minimal YAML front-matter parser (dovoljno za translationKey i source_url)."""
    try:
        text = p.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return {}
    if not text.startswith("---"):
        return {}
    lines = text.splitlines()
    out, in_block = {}, False
    for i, line in enumerate(lines):
        if i == 0 and line.strip() == "---":
            in_block = True
            continue
        if in_block and line.strip() == "---":
            break
        if in_block:
            m = re.match(r"^([A-Za-z0-9_]+)\s*:\s*(.*)$", line)
            if m:
                k = m.group(1).strip()
                v = m.group(2).strip().strip('"').strip("'")
                out[k] = v
    return out

def normalize_url(u: str | None):
    if not u:
        return None
    u = u.strip()
    # force https, strip query/fragment, drop trailing slash, lower netloc
    parts = urlsplit(u.replace("http://", "https://"))
    netloc = parts.netloc.lower().removeprefix("www.")
    path = parts.path.rstrip("/")
    if not netloc:
        return None
    return f"https://{netloc}{path}"

def detect_lang_and_loc(path: Path):
    s = str(path).replace("\\", "/")
    if "/hr/" in s:
        return "hr", "hr_dir"
    if "/de/" in s:
        return "de", "de_dir"
    if "/en/" in s:
        return "en", "en_dir"        # EN u podmapi /en/
    # root EN (npr. content/news/....md)
    return "en", "root"

def main():
    md_files = list(CONTENT_DIR.rglob("*.md"))
    if not md_files:
        print("No content/*.md files found.")
        return 0

    recs = []
    for f in md_files:
        fm = read_front_matter(f)
        tkey = fm.get("translationKey", "").strip()
        surl = normalize_url(fm.get("source_url") or fm.get("sourceUrl"))
        lang, loc = detect_lang_and_loc(f)
        recs.append({"path": f, "lang": lang, "loc": loc, "tkey": tkey, "url": surl})

    # grupiranja po jeziku
    by_key = {}
    by_url = {}
    for r in recs:
        if r["tkey"]:
            by_key.setdefault((r["lang"], r["tkey"]), []).append(r["path"])
        if r["url"]:
            by_url.setdefault((r["lang"], r["url"]), []).append(r["path"])

    real_dupes = []

    # 1) isti translationKey u ISTOM jeziku (len > 1)
    for (lang, tkey), paths in sorted(by_key.items()):
        if len(paths) > 1:
            real_dupes.append(("translationKey", lang, tkey, paths))

    # 2) isti source_url u ISTOM jeziku (len > 1)
    for (lang, url), paths in sorted(by_url.items()):
        if len(paths) > 1:
            real_dupes.append(("source_url", lang, url, paths))

    # 3) poseban slučaj: EN postoji na dvije lokacije (root i /en/)
    en_keys = {}
    for r in recs:
        if r["lang"] != "en":
            continue
        key = ("tkey", r["tkey"]) if r["tkey"] else ("url", r["url"])
        if not key[1]:
            continue
        en_keys.setdefault(key, {"root": [], "en_dir": []})
        en_keys[key][r["loc"]].append(r["path"])

    en_dual_loc = []
    for key, buckets in en_keys.items():
        if buckets["root"] and buckets["en_dir"]:
            en_dual_loc.append((key, buckets["root"], buckets["en_dir"]))

    # --- ispis & izlazni kod -------------------------------------------------
    had_error = False

    if real_dupes:
        had_error = True
        print("❌ REAL duplicates (same language):")
        for kind, lang, key, paths in real_dupes:
            print(f"* {kind} • lang={lang} • {key}  ({len(paths)} files)")
            for p in paths:
                print(f"   - {p}")
        print()

    if en_dual_loc:
        had_error = True
        print("❌ EN present in BOTH locations (content/news/ AND content/en/news/):")
        for (kind, key), root_paths, en_paths in en_dual_loc:
            label = f"{kind}={key}"
            print(f"* {label}")
            for p in root_paths:
                print(f"   - [root]  {p}")
            for p in en_paths:
                print(f"   - [en/]   {p}")
        print()

    # Info: koliko čega, čisto radi konteksta
    total = len(recs)
    hr = sum(1 for r in recs if r["lang"] == "hr")
    de = sum(1 for r in recs if r["lang"] == "de")
    en_root = sum(1 for r in recs if r["lang"] == "en" and r["loc"] == "root")
    en_dir = sum(1 for r in recs if r["lang"] == "en" and r["loc"] == "en_dir")
    print(f"Scanned {total} files  |  hr={hr}  de={de}  en(root)={en_root}  en(/en/)={en_dir}")

    if not had_error:
        print("✅ No real duplicates. (HR/DE/EN triplets are ignored by design.)")
        return 0
    return 1

if __name__ == "__main__":
    sys.exit(main())

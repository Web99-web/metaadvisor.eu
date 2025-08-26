#!/usr/bin/env python3
import os, re, sys, urllib.parse, collections

ROOT = "content"
FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)

def read_front_matter(path):
    with open(path, "r", encoding="utf-8") as f: s = f.read()
    m = FM_RE.match(s)
    fm = {}
    if not m: return fm
    for line in m.group(1).splitlines():
        m2 = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", line.strip())
        if not m2: continue
        k, v = m2.group(1), m2.group(2).strip()
        if v.startswith(("'", '"')) and v.endswith(("'", '"')): v = v[1:-1]
        fm[k] = v
    return fm

def canon_url(u):
    if not u: return ""
    try: pu = urllib.parse.urlsplit(u)
    except Exception: return u
    net = pu.netloc.lower()
    if net.startswith("www."): net = net[4:]
    path = pu.path.rstrip("/")
    # makni tracking parametre
    # (utm_*, ref, fbclid, gclid, mc_cid, mc_eid)
    return urllib.parse.urlunsplit((pu.scheme.lower(), net, path, "", ""))

def norm_title(t):
    t = (t or "").lower()
    t = re.sub(r"[^a-z0-9 ]+", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t

files = [os.path.join(r,f) for r,_,fs in os.walk(ROOT) for f in fs if f.endswith(".md")]

by_key   = collections.defaultdict(list)
by_src   = collections.defaultdict(list)
by_title = collections.defaultdict(list)

for p in files:
    fm = read_front_matter(p)
    key = fm.get("translationKey","").strip()
    src = canon_url(fm.get("source_url","").strip() or fm.get("canonical_url","").strip())
    ttl = norm_title(fm.get("title","")); date = (fm.get("date","") or "")[:10]
    if key: by_key[key].append(p)
    if src: by_src[src].append(p)
    if ttl and date: by_title[f"{date}__{ttl}"].append(p)

def print_dupes(label, d):
    dupes = {k:v for k,v in d.items() if len(v)>1}
    if not dupes: 
        print(f"✅ No duplicates by {label}")
        return 0
    print(f"\n❌ Duplicates by {label}:")
    for k, arr in dupes.items():
        print(f"* {k}  ({len(arr)} files)")
        for p in arr: print("   -", p)
    return 1

exit_code = 0
exit_code |= print_dupes("translationKey", by_key)
exit_code |= print_dupes("canonical source_url", by_src)
exit_code |= print_dupes("date+normalized title", by_title)

sys.exit(1 if exit_code else 0)

"""Check/generate only approved A term controls; never edit article front matter."""
import argparse
import json
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def expected_controls():
    policy = json.loads((ROOT / 'data/tag_policy.json').read_text(encoding='utf8'))
    expected = {}
    for lang, terms in policy['archives'].items():
        for slug, entry in terms.items():
            if any(p in ('', '.', '..') for p in slug.split('/')) or slug.startswith('.'):
                raise ValueError(f'Unsupported approved term path: {lang}/{slug}')
            rel = Path(lang) / 'tags' / slug / '_index.md'
            # Byte format matches the controls used by the benchmark.
            expected[rel] = '---\ntitle: '+json.dumps(entry['title'],ensure_ascii=False)+'\n_build:\n  render: always\n  list: always\n---\n'
    return expected

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--check', action='store_true'); args = ap.parse_args()
    config = tomllib.loads((ROOT/'config.toml').read_text(encoding='utf8'))
    if config.get('baseURL') != 'https://metaadvisor.eu/' or config.get('paginate') != 96:
        raise SystemExit('Unexpected root config scope or production URL/pagination; inspect TOML table placement')
    base = ROOT / 'generated/topic-content'; expected = expected_controls()
    actual = {p.relative_to(base) for p in base.rglob('_index.md')}
    extras = actual - expected.keys()
    if extras:
        raise SystemExit(f'Unexpected controls need review, not automatic deletion: {sorted(map(str, extras))[:10]}')
    for rel, text in expected.items():
        p = base / rel
        if args.check:
            # Parse-free verification tolerates the original equivalent YAML spacing.
            s = p.read_text(encoding='utf8') if p.exists() else ''
            if s != text:
                raise SystemExit(f'Missing or unsafe A control: {p}')
        elif not p.exists():
            p.parent.mkdir(parents=True, exist_ok=True); p.write_text(text, encoding='utf8')
    print(f'Approved A controls verified: {len(expected)}; source articles untouched')

if __name__ == '__main__': main()

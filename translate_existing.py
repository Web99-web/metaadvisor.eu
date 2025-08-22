import frontmatter
from pathlib import Path
from deep_translator import GoogleTranslator

SRC_DIR = Path("content/news")
OUT_DE = Path("content/de/news")
OUT_HR = Path("content/hr/news")

# osiguraj mape
OUT_DE.mkdir(parents=True, exist_ok=True)
OUT_HR.mkdir(parents=True, exist_ok=True)

def tr(text: str, dest: str) -> str:
    if not text:
        return text
    # robustno: ako padne, vrati EN umjesto da ruši job
    try:
        return GoogleTranslator(source="en", target=dest).translate(text)
    except Exception as e:
        print(f"[warn] translate -> {dest} failed: {e}")
        return text

made_de = made_hr = 0
errors = 0

for md in sorted(SRC_DIR.glob("*.md")):
    try:
        post = frontmatter.load(md)
        title_en = post.get("title", "")
        body_en = post.content or ""

        # --- DE ---
        title_de = tr(title_en, "de")
        body_de  = tr(body_en, "de")
        post_de = frontmatter.Post(body_de, **post.metadata)
        post_de["title"] = title_de
        (OUT_DE / md.name).write_text(frontmatter.dumps(post_de), encoding="utf-8")
        made_de += 1

        # --- HR ---
        title_hr = tr(title_en, "hr")
        body_hr  = tr(body_en, "hr")
        post_hr = frontmatter.Post(body_hr, **post.metadata)
        post_hr["title"] = title_hr
        (OUT_HR / md.name).write_text(frontmatter.dumps(post_hr), encoding="utf-8")
        made_hr += 1

        print(f"[ok] {md.name} → DE+HR")
    except Exception as e:
        errors += 1
        print(f"[err] {md.name}: {e}")

print(f"[done] totals: DE={made_de}, HR={made_hr}, errors={errors}")

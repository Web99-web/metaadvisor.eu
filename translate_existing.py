import frontmatter
from pathlib import Path
from deep_translator import GoogleTranslator

SRC_DIR = Path("content/news")
OUT_DE = Path("content/de/news")
OUT_HR = Path("content/hr/news")

OUT_DE.mkdir(parents=True, exist_ok=True)
OUT_HR.mkdir(parents=True, exist_ok=True)

def tr(text: str, dest: str) -> str:
    if not text:
        return text
    try:
        return GoogleTranslator(source="en", target=dest).translate(text)
    except Exception as e:
        print(f"[warn] translate({dest}) failed: {e}")
        return text  # fallback na EN

made_de = made_hr = 0

for md in sorted(SRC_DIR.glob("*.md")):
    post = frontmatter.load(md)
    title_en = post.get("title", "")
    body_en = post.content

    # --- DE ---
    post_de = frontmatter.Post(
        tr(body_en, "de"),
        **post.metadata
    )
    post_de["title"] = tr(title_en, "de")
    out_de = OUT_DE / md.name
    out_de.write_text(frontmatter.dumps(post_de), encoding="utf-8")
    made_de += 1

    # --- HR ---
    post_hr = frontmatter.Post(
        tr(body_en, "hr"),
        **post.metadata
    )
    post_hr["title"] = tr(title_en, "hr")
    out_hr = OUT_HR / md.name
    out_hr.write_text(frontmatter.dumps(post_hr), encoding="utf-8")
    made_hr += 1

    print(f"[ok] {md.name} → DE+HR")

print(f"[done] files: DE={made_de}, HR={made_hr}")

import os
import frontmatter
from pathlib import Path
from googletrans import Translator

translator = Translator()

# 📂 Putanje
SRC_DIR = Path("content/news")
OUT_DE = Path("content/de/news")
OUT_HR = Path("content/hr/news")

OUT_DE.mkdir(parents=True, exist_ok=True)
OUT_HR.mkdir(parents=True, exist_ok=True)

def translate_text(text, dest):
    try:
        return translator.translate(text, dest=dest).text
    except Exception as e:
        print(f"❌ Translation error: {e}")
        return text

for md_file in SRC_DIR.glob("*.md"):
    post = frontmatter.load(md_file)

    title_en = post.get("title", "")
    body_en = post.content

    # ➡️ prijevod
    title_de = translate_text(title_en, "de")
    title_hr = translate_text(title_en, "hr")
    body_de = translate_text(body_en, "de")
    body_hr = translate_text(body_en, "hr")

    # ➡️ zapis u DE
    post_de = frontmatter.Post(body_de, **post.metadata)
    post_de["title"] = title_de
    out_file_de = OUT_DE / md_file.name
    with open(out_file_de, "w", encoding="utf-8") as f:
        f.write(frontmatter.dumps(post_de))

    # ➡️ zapis u HR
    post_hr = frontmatter.Post(body_hr, **post.metadata)
    post_hr["title"] = title_hr
    out_file_hr = OUT_HR / md_file.name
    with open(out_file_hr, "w", encoding="utf-8") as f:
        f.write(frontmatter.dumps(post_hr))

    print(f"✅ Translated {md_file.name}")

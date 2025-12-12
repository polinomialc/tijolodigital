from pathlib import Path

# ==============================
# CONFIG
# ==============================

BASE = Path(__file__).resolve().parent
ARTS_DIR = BASE / "images" / "arts"
PAGES_DIR = BASE / "pages"

IMAGE_EXTS = ("*.jpg", "*.jpeg", "*.png", "*.webp")

PAGES_DIR.mkdir(exist_ok=True)

# ==============================
# TEMPLATE HTML (TRABALHO)
# ==============================

def render_page(title: str, work_name: str, image_tags: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="pt">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    body {{
      margin:0;
      background:#dcd9ff;
      font-family: Verdana, Tahoma, sans-serif;
      color:#000;
    }}

    .header {{
      text-align:center;
      padding:40px 10px 20px;
    }}

    .logo {{
      max-width:90%;
      image-rendering: pixelated;
    }}

    .subtitle {{
      font-family: "Comic Sans MS", Comic Sans, cursive;
      font-style: italic;
      text-decoration: underline;
      margin-top:10px;
    }}

    .path {{
      text-align:center;
      margin:30px 0 20px;
      font-size:14px;
    }}

    .gallery {{
      display:flex;
      flex-direction:column;
      align-items:center;
      gap:40px;
      padding-bottom:80px;
    }}

    .gallery img {{
      max-width:90%;
      height:auto;
    }}

    a {{
      color:#0000ee;
    }}
  </style>
</head>

<body>

  <div class="header">
    <img src="../images/header_title.gif" class="logo" alt="Tijolo Digital">
    <div class="subtitle">Tijolo Digital</div>
  </div>

  <div class="path">
    C:\\tijolodigital\\photography\\{work_name}
  </div>

  <div class="gallery">
    {image_tags}
  </div>

</body>
</html>
"""

# ==============================
# BUILD PAGES
# ==============================

def build_pages():
    if not ARTS_DIR.exists():
        raise SystemExit(f"ERRO: pasta não encontrada: {ARTS_DIR}")

    for work_dir in sorted(p for p in ARTS_DIR.iterdir() if p.is_dir()):
        images = []

        for ext in IMAGE_EXTS:
            images.extend(work_dir.glob(ext))

        images = sorted(images)

        if not images:
            print(f"[WARN] {work_dir.name}: nenhuma imagem encontrada")
            continue

        # gera tags <img> com path correto
        tags = []
        for img in images:
            src = f"../images/arts/{work_dir.name}/{img.name}"
            tags.append(f'<img src="{src}" alt="">')

        html = render_page(
            title=f"Tijolo Digital — {work_dir.name}",
            work_name=work_dir.name,
            image_tags="\n    ".join(tags)
        )

        out = PAGES_DIR / f"{work_dir.name}.html"
        out.write_text(html, encoding="utf-8")
        print(f"[OK] gerado: pages/{out.name}")

# ==============================
# RUN
# ==============================

if __name__ == "__main__":
    build_pages()

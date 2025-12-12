import os
import random
from pathlib import Path

random.seed(42)  # mantém estável (sempre escolhe os mesmos a cada run)

BASE = Path(__file__).resolve().parent
ICONS_DIR = BASE / "images" / "icons"

if not ICONS_DIR.exists():
    raise SystemExit(f"ERRO: pasta não encontrada: {ICONS_DIR}\nCrie images/icons e coloque os PNG lá.")

# pega TODOS os PNGs reais do pack
icons = sorted([p for p in ICONS_DIR.rglob("*.png")])

if not icons:
    raise SystemExit(f"ERRO: nenhum .png encontrado em {ICONS_DIR}")

# tenta escolher por palavras-chave (se existir), senão cai no aleatório
def pick_icon(keywords, fallback_pool):
    keywords = [k.lower() for k in keywords]
    matches = []
    for p in icons:
        name = p.name.lower()
        if any(k in name for k in keywords):
            matches.append(p)
    if matches:
        return random.choice(matches)
    return random.choice(fallback_pool)

# pools
pool_any = icons

# escolhas (você NÃO precisa ter esses nomes; é só heurística)
ico_about   = pick_icon(["info", "help", "user", "person", "id", "profile"], pool_any)
ico_works   = pick_icon(["folder", "brief", "case", "docs", "file", "work"], pool_any)
ico_images  = pick_icon(["image", "photo", "pic", "paint", "art", "draw", "camera"], pool_any)
ico_video   = pick_icon(["video", "movie", "media", "play", "film"], pool_any)
ico_mail    = pick_icon(["mail", "email", "letter", "contact"], pool_any)
ico_youtube = pick_icon(["youtube", "yt", "play"], pool_any)
ico_insta   = pick_icon(["insta", "instagram", "camera"], pool_any)

# helper: caminho relativo com barras /
def rel(p: Path) -> str:
    return p.relative_to(BASE).as_posix()

chosen = {
    "About": rel(ico_about),
    "Works": rel(ico_works),
    "Images": rel(ico_images),
    "Video": rel(ico_video),
    "Contact": rel(ico_mail),
    "YouTube": rel(ico_youtube),
    "Instagram": rel(ico_insta),
}

print("ÍCONES ESCOLHIDOS (reais):")
for k, v in chosen.items():
    print(f" - {k}: {v}")

html = f"""<!DOCTYPE html>
<html lang="pt">
<head>
  <meta charset="UTF-8">
  <title>Tijolo Digital</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    body {{
      margin:0; background:#c0c0c0; color:#000;
      font-family: Verdana, Tahoma, sans-serif; font-size: 13px;
    }}
    a {{ color:#0000ee; text-decoration: underline; }}

    .window {{
      width: 960px; margin: 30px auto; background:#fff;
      border: 2px solid #000; box-shadow: 5px 5px 0 #555;
    }}
    .title-bar {{
      background: linear-gradient(to right, #000080, #0000ff);
      color:#fff; padding: 6px 10px; font-weight: bold;
      display:flex; justify-content: space-between; align-items:center;
    }}
    .title-buttons span {{
      display:inline-block; width:12px; height:12px; margin-left:4px;
      background:#c0c0c0; border:1px solid #000;
    }}

    .header-img {{
      border-bottom: 2px solid #000;
      padding: 10px; text-align:center; background:#fff;
    }}
    .header-img img {{
      max-width: 100%;
      image-rendering: pixelated;
    }}

    .content {{ display:flex; }}
    .sidebar {{
      width: 240px; background:#e0e0e0; border-right:2px solid #000;
      padding: 10px;
    }}
    .sidebar h3 {{
      font-size: 13px; margin: 0 0 8px 0; border-bottom: 1px solid #000;
      padding-bottom: 4px;
    }}

    /* ÍCONE INTEIRO (48x48) */
    .nav-item {{
      display:flex; align-items:center; gap:10px;
      margin: 10px 0;
    }}
    .nav-item img {{
      width: 48px; height: 48px;
      image-rendering: pixelated;
      border: 1px solid #000;
      background:#fff;
    }}

    .main {{ flex:1; padding: 15px; }}
    .section {{ margin-bottom: 28px; }}
    .section h2 {{
      font-size: 14px; background:#000080; color:#fff;
      padding: 4px 6px; margin: 0 0 10px 0;
    }}

    .grid {{
      display:grid;
      grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
      gap: 15px;
    }}
    .card {{
      border:2px solid #000; background:#f5f5f5; padding: 8px;
    }}
    .card img {{
      width:100%; border:1px solid #000; background:#fff;
    }}
    .card iframe {{ width:100%; height:160px; border:0; }}
    .card p {{ margin: 8px 0 0; font-size: 12px; }}

    .footer {{
      background:#e0e0e0; border-top:2px solid #000;
      padding: 10px; text-align:center; font-size: 11px;
    }}

    @media (max-width: 960px) {{
      .window {{ width: 95%; }}
      .content {{ flex-direction: column; }}
      .sidebar {{ width: auto; border-right:none; border-bottom:2px solid #000; }}
      .nav-item img {{ width: 40px; height: 40px; }}
    }}
  </style>
</head>
<body>

<div class="window">
  <div class="title-bar">
    <span>Tijolo Digital — Internet Explorer</span>
    <div class="title-buttons"><span></span><span></span><span></span></div>
  </div>

  <div class="header-img">
    <img src="images/header_title.gif" alt="Tijolo Digital">
  </div>

  <div class="content">
    <div class="sidebar">
      <h3>Navigation</h3>

      <div class="nav-item">
        <img src="{chosen['About']}" alt="">
        <a href="#about">About</a>
      </div>

      <div class="nav-item">
        <img src="{chosen['Works']}" alt="">
        <a href="#works">Works</a>
      </div>

      <div class="nav-item">
        <img src="{chosen['Images']}" alt="">
        <a href="#works">Images</a>
      </div>

      <div class="nav-item">
        <img src="{chosen['Video']}" alt="">
        <a href="#video">Video</a>
      </div>

      <div class="nav-item">
        <img src="{chosen['Contact']}" alt="">
        <a href="#contact">Contact</a>
      </div>

      <h3>External</h3>

      <div class="nav-item">
        <img src="{chosen['YouTube']}" alt="">
        <a href="#">YouTube</a>
      </div>

      <div class="nav-item">
        <img src="{chosen['Instagram']}" alt="">
        <a href="#">Instagram</a>
      </div>
    </div>

    <div class="main">
      <div class="section" id="about">
        <h2>About Tijolo Digital</h2>
        <p>
          Tijolo Digital é um portfólio artístico com estética retrô (web 1.0 / anos 2000).
          Conteúdo: imagem + vídeo. Sem tracking. Sem frescura.
        </p>
      </div>

      <div class="section" id="works">
        <h2>Selected Works (Image)</h2>
        <div class="grid">
          <div class="card">
            <img src="images/works/art01.webp" alt="">
            <p>Artwork 01 — Digital / Concept</p>
          </div>
          <div class="card">
            <img src="images/works/art02.webp" alt="">
            <p>Artwork 02 — Illustration</p>
          </div>
          <div class="card">
            <img src="images/works/art03.webp" alt="">
            <p>Artwork 03 — Visual Study</p>
          </div>
        </div>
      </div>

      <div class="section" id="video">
        <h2>Video / Motion</h2>
        <div class="grid">
          <div class="card">
            <iframe src="https://www.youtube.com/embed/VIDEO_ID_1" allowfullscreen></iframe>
            <p>Motion Piece 01</p>
          </div>
          <div class="card">
            <iframe src="https://www.youtube.com/embed/VIDEO_ID_2" allowfullscreen></iframe>
            <p>Experimental Video</p>
          </div>
        </div>
      </div>

      <div class="section" id="contact">
        <h2>Contact</h2>
        <p>Email: <a href="mailto:email@email.com">email@email.com</a><br>Location: Portugal</p>
      </div>
    </div>
  </div>

  <div class="footer">
    © 1999–2025 Tijolo Digital · Best viewed at 1024×768 · No cookies · No tracking
  </div>
</div>

</body>
</html>
"""

# escreve o index.html na raiz
out = BASE / "index.html"
out.write_text(html, encoding="utf-8")
print(f"\nOK: gerei {out}")

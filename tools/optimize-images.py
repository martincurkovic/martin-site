#!/usr/bin/env python3
"""Turn the originals in src-images/ into small WebP files in img/.

Run from the project root:  python3 tools/optimize-images.py
Needs Pillow (pip install pillow). Re-run whenever you add or swap an original.

Every <name>.jpg in src-images/ becomes img/<name>.webp at 480 px wide (cover art), except the two
page images below, which have their own sizes.
"""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src-images"
OUT = ROOT / "img"
OUT.mkdir(exist_ok=True)

# (source file, output name, width, quality)
SPECIAL = [
    ("hero-original.jpg", "hero-800.webp", 800, 72),
    ("hero-original.jpg", "hero-1200.webp", 1200, 72),
    ("label-header-original.jpg", "label.webp", 975, 80),
]
special_sources = {s for s, *_ in SPECIAL}
COVERS = [(p.name, p.stem + ".webp", 480, 78) for p in sorted(SRC.glob("*.jpg")) if p.name not in special_sources]

for src, name, width, quality in SPECIAL + COVERS:
    im = Image.open(SRC / src).convert("RGB")
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    dest = OUT / name
    im.save(dest, "WEBP", quality=quality, method=6)
    print(f"{name:26} {im.width}x{im.height}  {dest.stat().st_size / 1024:.0f} KB")

# Share-card images (og:image) as JPEG: WebP works on Facebook/WhatsApp/iMessage/X but some chat apps
# (Slack, Discord) reject it. Covers at 600 px, plus a 1200x630 crop of the hero for the home page.
OG = OUT / "og"
OG.mkdir(exist_ok=True)
for src, name, _, _ in COVERS:
    im = Image.open(SRC / src).convert("RGB")
    if im.width > 600:
        im = im.resize((600, round(im.height * 600 / im.width)), Image.LANCZOS)
    im.save(OG / (Path(name).stem + ".jpg"), "JPEG", quality=82, optimize=True, progressive=True)

hero = Image.open(SRC / "hero-original.jpg").convert("RGB")
band = round(hero.width * 630 / 1200)            # landscape band that keeps the face (about 38% down the photo)
top = max(0, min(hero.height - band, round(hero.height * 0.38 - band / 2)))
hero.crop((0, top, hero.width, top + band)).resize((1200, 630), Image.LANCZOS).save(
    OG / "home.jpg", "JPEG", quality=82, optimize=True, progressive=True
)
sizes = [p.stat().st_size for p in OG.glob("*.jpg")]
print(f"img/og: {len(sizes)} JPEGs, {sum(sizes) / 1024:.0f} KB total (largest {max(sizes) / 1024:.0f} KB)")

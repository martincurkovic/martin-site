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

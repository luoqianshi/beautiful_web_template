"""Generate webp display variants for the gallery screenshots and the hero artwork.

Usage:  python script/optimize_images.py

Originals stay untouched: assets/screenshots/*.png remain the crisp source files,
assets/screenshots/webp/*.webp are the lightweight copies the page loads first.
"""
import os
import sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHOTS = os.path.join(ROOT, "assets", "screenshots")
WEBP_DIR = os.path.join(SHOTS, "webp")
HERO_DIR = os.path.join(ROOT, "assets", "hero")

WEBP_QUALITY = 80


def convert(src, dst, quality=WEBP_QUALITY):
    with Image.open(src) as im:
        im.convert("RGB").save(dst, "WEBP", quality=quality, method=6)


def main():
    os.makedirs(WEBP_DIR, exist_ok=True)
    os.makedirs(HERO_DIR, exist_ok=True)

    pngs = sorted(f for f in os.listdir(SHOTS) if f.endswith(".png"))
    if not pngs:
        sys.exit("no screenshots found in " + SHOTS)

    before = after = 0
    for name in pngs:
        src = os.path.join(SHOTS, name)
        dst = os.path.join(WEBP_DIR, name[:-4] + ".webp")
        convert(src, dst)
        before += os.path.getsize(src)
        after += os.path.getsize(dst)
        print(f"  webp {name[:-4]}.webp  {os.path.getsize(dst) // 1024} KB")

    hero = os.path.join(HERO_DIR, "romantic-landscape.webp")
    if os.path.exists(hero):
        print(f"  hero romantic-landscape.webp  {os.path.getsize(hero) // 1024} KB")

    print(f"{len(pngs)} images: {before / 1048576:.1f} MB -> {after / 1048576:.1f} MB")


if __name__ == "__main__":
    main()

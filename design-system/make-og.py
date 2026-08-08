#!/usr/bin/env python3
"""Generate 1200x630 Open Graph cards in the 4BV system.

The four rings are drawn from the same geometry as the site's hero SVG so the
card and the page agree. Run from the repo root:

    python3 design-system/make-og.py
"""
import math
import pathlib
from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parent.parent
FONTS = ROOT / "design-system" / "fonts"
OUT = ROOT / "assets" / "og"

W, H = 1200, 630
SS = 3  # supersample factor; PIL has no antialiased stroke otherwise

PAPER = (250, 250, 247)
INK = (5, 10, 48)
SLATE = (0, 59, 115)
BLUE = (96, 163, 217)
SKY = (175, 221, 255)
TERTIARY = (106, 112, 136)

# cx, cy, r from the hero SVG viewBox "5 0 230 230"
RINGS = [
    ((132, 106, 82), SKY),
    ((106, 104, 82), BLUE),
    ((108, 123, 82), SLATE),
    ((125, 132, 82), INK),
]


def font(name, size):
    return ImageFont.truetype(str(FONTS / name), size)


def draw_rings(img, box_x, box_y, box_size):
    """Render the mark supersampled, then downscale for clean edges."""
    s = box_size * SS
    layer = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    scale = s / 230.0
    stroke = max(1, round(5 * scale))
    for (cx, cy, r), color in RINGS:
        # viewBox x starts at 5
        x, y = (cx - 5) * scale, cy * scale
        rr = r * scale
        d.ellipse([x - rr, y - rr, x + rr, y + rr], outline=color + (255,), width=stroke)
    layer = layer.resize((box_size, box_size), Image.LANCZOS)
    img.alpha_composite(layer, (box_x, box_y))


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def card(filename, eyebrow, title, kicker):
    img = Image.new("RGBA", (W, H), PAPER + (255,))
    d = ImageDraw.Draw(img)

    pad = 72
    draw_rings(img, W - 300 - pad, pad + 4, 300)

    f_eyebrow = font("FrutigerLTStd-Roman.otf", 22)
    f_title = font("CaeciliaLTStd-Light.otf", 62)
    f_kicker = font("CaeciliaLTStd-LightItalic.otf", 30)
    f_mark = font("CaeciliaLTStd-Light.otf", 34)
    f_url = font("FrutigerLTStd-Roman.otf", 22)

    text_w = W - pad * 2 - 300 - 40

    y = pad + 8
    d.text((pad, y), eyebrow.upper(), font=f_eyebrow, fill=TERTIARY)
    y += 52

    for line in wrap(d, title, f_title, text_w):
        d.text((pad, y), line, font=f_title, fill=INK)
        y += 74

    if kicker:
        y += 16
        for line in wrap(d, kicker, f_kicker, text_w):
            d.text((pad, y), line, font=f_kicker, fill=SLATE)
            y += 42

    # baseline: wordmark left, url right
    base_y = H - pad - 40
    d.line([(pad, base_y - 26), (pad + 44, base_y - 26)], fill=(230, 229, 222), width=2)
    d.text((pad, base_y), "4BV", font=f_mark, fill=INK)
    url = "4bv.ai"
    d.text((W - pad - d.textlength(url, font=f_url), base_y + 12), url, font=f_url, fill=TERTIARY)

    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / filename
    img.convert("RGB").save(path, "PNG", optimize=True)
    print(f"  {path.relative_to(ROOT)}  {path.stat().st_size // 1024} KB")


if __name__ == "__main__":
    card(
        "default.png",
        "Physician-owned consulting",
        "Four pillars. One practice.",
        "Medicine, technology, and contemplative practice.",
    )
    card(
        "decon.png",
        "Clinician Decon",
        "A naive scrubber makes clinical AI less safe.",
        "Why removing identifiers and preserving the medicine are two objectives, not one.",
    )

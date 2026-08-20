import base64
import io
import re
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "resource" / "assets" / "slogan橫式.svg"
OUTPUT = ROOT / "public" / "images" / "slogan-horizontal-white.webp"

# Crops follow the original two vertical calligraphy columns, then reassemble
# the phrase from right to left into one horizontal line without redrawing it.
GLYPHS = [
    (2380, 120, 3420, 760),   # 讓
    (2460, 840, 3370, 1400),  # 自
    (2460, 1480, 3370, 2050), # 己
    (2350, 2050, 3420, 2630), # 成
    (2450, 2750, 3440, 3330), # 為
    (2360, 3420, 3470, 4300), # 最
    (1350, 760, 2440, 1450),  # 溫
    (1320, 1450, 2450, 2200), # 暖
    (1450, 2200, 2440, 2850), # 的
    (1370, 2850, 2440, 3650), # 陽
    (1370, 3700, 2470, 4470), # 光
]


def embedded_png() -> Image.Image:
    svg = SOURCE.read_text(encoding="utf-8", errors="ignore")
    match = re.search(r'xlink:href="data:image/png;base64,([^"]+)', svg)
    if not match:
        raise RuntimeError("Embedded calligraphy PNG not found")
    return Image.open(io.BytesIO(base64.b64decode(match.group(1)))).convert("L")


def white_glyph(source: Image.Image, box: tuple[int, int, int, int]) -> Image.Image:
    luminance = source.crop(box)
    alpha = luminance.point(lambda value: 0 if value < 18 else min(255, (value - 18) * 2))
    alpha.paste(0, (0, 0, alpha.width, min(18, alpha.height)))
    alpha.paste(0, (0, max(0, alpha.height - 18), alpha.width, alpha.height))
    bounds = alpha.getbbox()
    if not bounds:
        raise RuntimeError(f"No glyph found in crop {box}")
    alpha = alpha.crop(bounds)
    alpha.thumbnail((150, 210), Image.Resampling.LANCZOS)
    glyph = Image.new("RGBA", alpha.size, "white")
    glyph.putalpha(alpha)
    return glyph


source = embedded_png()
canvas = Image.new("RGBA", (1870, 250), (255, 255, 255, 0))
for index, box in enumerate(GLYPHS):
    glyph = white_glyph(source, box)
    x = index * 170 + (170 - glyph.width) // 2
    y = (250 - glyph.height) // 2
    canvas.alpha_composite(glyph, (x, y))

canvas.save(OUTPUT, "WEBP", lossless=True, method=6)
print(f"Created {OUTPUT} ({canvas.width}x{canvas.height})")

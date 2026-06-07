# -*- coding: utf-8 -*-
"""
make_og_assets.py — Rasterize the social-share cover (og-image.png, 1200x630)
and the PWA/Apple icons (icon-512/192/180.png) from the project's brand design,
using Windows-bundled fonts (no cairosvg dependency).

Run:  python make_og_assets.py
Outputs into ./assets/
"""
import os
from PIL import Image, ImageDraw, ImageFont

ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
FONTS = r"C:\Windows\Fonts"

F_ZH   = os.path.join(FONTS, "msyhbd.ttc")   # Microsoft YaHei Bold (Simplified Chinese + Latin)
F_ZHH  = os.path.join(FONTS, "simhei.ttf")   # SimHei (heavy, for big headline)
F_KO   = os.path.join(FONTS, "malgunbd.ttf") # Malgun Gothic Bold (Korean)
F_LAT  = os.path.join(FONTS, "segoeuib.ttf") # Segoe UI Bold (Latin)

_cache = {}
def font(path, size):
    key = (path, size)
    if key not in _cache:
        _cache[key] = ImageFont.truetype(path, size)
    return _cache[key]

def lerp(c1, c2, t):
    return tuple(int(c1[k] + (c2[k] - c1[k]) * t) for k in range(3))

def grad3(colors, t):
    if t <= 0.5:
        return lerp(colors[0], colors[1], t / 0.5)
    return lerp(colors[1], colors[2], (t - 0.5) / 0.5)

def diag_gradient(size, c0, c1):
    """Smooth diagonal 2-colour gradient via 2x2 upscale."""
    cmid = lerp(c0, c1, 0.5)
    small = Image.new("RGB", (2, 2))
    small.putpixel((0, 0), c0)
    small.putpixel((1, 0), cmid)
    small.putpixel((0, 1), cmid)
    small.putpixel((1, 1), c1)
    return small.resize(size, Image.BILINEAR)

def font_for_char(ch):
    o = ord(ch)
    if 0xAC00 <= o <= 0xD7A3 or 0x1100 <= o <= 0x11FF or 0x3130 <= o <= 0x318F:
        return F_KO
    if 0x4E00 <= o <= 0x9FFF or 0x3400 <= o <= 0x4DBF:
        return F_ZH
    return F_LAT

def draw_mixed(draw, x, baseline_y, text, size, fill, default=None,
               stroke_width=0, stroke_fill=None, letter_spacing=0):
    """Draw a possibly mixed-script line, choosing a font per char run.
    Anchored to the left baseline (matches SVG text y)."""
    i = 0
    while i < len(text):
        fp = font_for_char(text[i]) if default is None else (
            default if font_for_char(text[i]) == F_LAT else font_for_char(text[i]))
        j = i + 1
        while j < len(text) and (font_for_char(text[j]) if default is None else (
                default if font_for_char(text[j]) == F_LAT else font_for_char(text[j]))) == fp:
            j += 1
        run = text[i:j]
        fnt = font(fp, size)
        if letter_spacing == 0:
            draw.text((x, baseline_y), run, font=fnt, fill=fill, anchor="ls",
                      stroke_width=stroke_width, stroke_fill=stroke_fill)
            x += draw.textlength(run, font=fnt)
        else:
            for ch in run:
                draw.text((x, baseline_y), ch, font=fnt, fill=fill, anchor="ls",
                          stroke_width=stroke_width, stroke_fill=stroke_fill)
                x += draw.textlength(ch, font=fnt) + letter_spacing
        i = j
    return x

def gradient_text(base, x, baseline_y, text, font_path, size, colors, stroke_width=0):
    """Render text filled with a horizontal 3-stop gradient."""
    fnt = font(font_path, size)
    mask = Image.new("L", base.size, 0)
    ImageDraw.Draw(mask).text((x, baseline_y), text, font=fnt, fill=255,
                              anchor="ls", stroke_width=stroke_width)
    bbox = mask.getbbox()
    if not bbox:
        return
    w = max(1, bbox[2] - bbox[0])
    grad_row = Image.new("RGB", (w, 1))
    for i in range(w):
        grad_row.putpixel((i, 0), grad3(colors, i / max(1, w - 1)))
    grad = grad_row.resize((w, base.size[1]))
    gfull = Image.new("RGB", base.size, (0, 0, 0))
    gfull.paste(grad, (bbox[0], 0))
    base.paste(gfull, (0, 0), mask)

def heartbeat(draw, pts, width, color):
    draw.line(pts, fill=color, width=width, joint="curve")
    # round the endpoints
    r = width // 2
    for (px, py) in (pts[0], pts[-1]):
        draw.ellipse([px - r, py - r, px + r, py + r], fill=color)

# ============================================================ OG IMAGE
def build_og():
    W, H = 1200, 630
    img = diag_gradient((W, H), (11, 17, 32), (30, 41, 59)).convert("RGBA")

    # subtle grid
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    gl = (148, 163, 184, 26)
    for y in range(80, H, 80):
        od.line([(0, y), (W, y)], fill=gl, width=1)
    for x in range(80, W, 80):
        od.line([(x, 0), (x, H)], fill=gl, width=1)
    # pulse / ECG line motif
    pulse = [(80, 410), (260, 410), (320, 290), (420, 540), (500, 250), (580, 410), (1120, 410)]
    od.line(pulse, fill=(239, 68, 68, 217), width=5, joint="curve")
    img = Image.alpha_composite(img, overlay)

    draw = ImageDraw.Draw(img)

    # brand badge (rounded gradient square) + white heartbeat
    badge = diag_gradient((84, 84), (239, 68, 68), (245, 158, 11)).convert("RGBA")
    bmask = Image.new("L", (84, 84), 0)
    ImageDraw.Draw(bmask).rounded_rectangle([0, 0, 83, 83], radius=20, fill=255)
    img.paste(badge, (80, 80), bmask)
    hb = [(94, 122), (108, 122), (114, 106), (128, 138), (134, 122), (160, 122)]
    heartbeat(draw, hb, 6, (255, 255, 255, 255))

    # brand wordmark
    draw_mixed(draw, 184, 118, "CARDIOGUARD INDUSTRIAL", 28, (248, 250, 252),
               default=F_LAT, letter_spacing=2)
    draw_mixed(draw, 184, 148, "工心守护 · 산업심장수호", 18, (148, 163, 184))

    # headline
    draw.text((80, 270), "工业场所心脏急救", font=font(F_ZHH, 64), fill=(248, 250, 252), anchor="ls")
    gradient_text(img, 80, 350, "智能响应平台", F_ZHH, 64,
                  [(239, 68, 68), (245, 158, 11), (59, 130, 246)])
    draw = ImageDraw.Draw(img)  # refresh after paste

    # subtitle
    draw.text((80, 412), "AI · IoT · CPR · AHA 2025 ECC Guidelines · Bilingual ZH / KR",
              font=font(F_LAT, 22), fill=(203, 213, 225), anchor="ls")

    # bottom badges
    badges = [
        (0,   260, (239, 68, 68),  (252, 165, 165), "数字健康医疗竞赛"),
        (280, 220, (59, 130, 246), (147, 197, 253), "主题: 产业安全"),
        (520, 200, (245, 158, 11), (252, 211, 77),  "中韩双语 · Open Source"),
    ]
    by = 490
    for (bx, bw, stroke, txt_c, label) in badges:
        x0 = 80 + bx
        fill_c = stroke + (46,)
        bd = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(bd).rounded_rectangle([x0, by, x0 + bw, by + 44], radius=22,
                                             fill=fill_c, outline=stroke + (128,), width=1)
        img.alpha_composite(bd)
        draw = ImageDraw.Draw(img)
        draw_mixed(draw, x0 + bw / 2 - draw.textlength(label, font=font(F_ZH, 16)) / 2,
                   by + 29, label, 16, txt_c)

    # footer
    draw.text((80, 588), "Wu Jingrui · Xi'an Medical College · Kyungwoon University · 2026",
              font=font(F_LAT, 14), fill=(100, 116, 139), anchor="ls")

    out = os.path.join(ASSETS, "og-image.png")
    img.convert("RGB").save(out, "PNG")
    print("wrote", out, img.size)

# ============================================================ ICONS
def build_icon(size):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    s = size / 64.0
    sq = diag_gradient((size, size), (244, 63, 94), (220, 38, 38)).convert("RGBA")
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, size - 1, size - 1],
                                           radius=int(14 * s), fill=255)
    img.paste(sq, (0, 0), mask)
    draw = ImageDraw.Draw(img)
    pts = [(8, 32), (18, 32), (23, 20), (33, 44), (38, 32), (56, 32)]
    pts = [(p[0] * s, p[1] * s) for p in pts]
    heartbeat(draw, pts, max(2, int(4.5 * s)), (255, 255, 255, 255))
    out = os.path.join(ASSETS, "icon-%d.png" % size)
    img.save(out, "PNG")
    print("wrote", out, img.size)

if __name__ == "__main__":
    build_og()
    for s in (512, 192, 180):
        build_icon(s)
    print("done")

# -*- coding: utf-8 -*-
"""
capture_screenshots.py
======================
Headless-Chrome 自动截图(中/韩 + 桌面/移动 + 不同章节)。

依赖: 系统已安装 Google Chrome (C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe)
前置: 本地 HTTP 服务在 http://localhost:8765 (或 SERVE_URL 环境变量)

运行:
    python capture_screenshots.py

产出:
    assets/screenshots/01_home_zh_desktop.png
    assets/screenshots/02_home_ko_desktop.png
    assets/screenshots/03_home_zh_mobile.png
    assets/screenshots/04_home_ko_mobile.png
"""
import os
import sys
import subprocess
import time
from pathlib import Path

HERE = Path(__file__).parent
SHOTS = HERE / "assets" / "screenshots"
SHOTS.mkdir(parents=True, exist_ok=True)

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
]
chrome_exe = next((p for p in CHROME_CANDIDATES if Path(p).exists()), None)
if not chrome_exe:
    sys.stderr.write("[!] Chrome not found. Skipping screenshots.\n")
    sys.exit(0)

SERVE_URL = os.environ.get("SERVE_URL", "http://localhost:8765")

# (name, viewport_w x h, url_path, full_page_height)
TARGETS = [
    ("01_home_zh_desktop", 1440, 900,  "/?lang=zh", 3200),
    ("02_home_ko_desktop", 1440, 900,  "/?lang=ko", 3200),
    ("03_home_zh_mobile",   430, 932,  "/?lang=zh", 5400),
    ("04_home_ko_mobile",   430, 932,  "/?lang=ko", 5400),
]


def shoot(name: str, w: int, h_view: int, path: str, h_full: int):
    """Render at (w x h_full) so Chrome captures the whole page in one frame."""
    out = SHOTS / f"{name}.png"
    cmd = [
        chrome_exe,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--no-sandbox",
        "--no-first-run",
        "--no-default-browser-check",
        "--disable-extensions",
        f"--window-size={w},{h_full}",
        "--virtual-time-budget=4000",
        f"--screenshot={out}",
        f"{SERVE_URL}{path}",
    ]
    print(f"[..] {name}  ({w}x{h_full})")
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if out.exists():
        kb = out.stat().st_size / 1024
        print(f"[OK] {name}.png  ({kb:.1f} KB)")
    else:
        print(f"[!!] {name} — Chrome did not produce a PNG")
        if res.stderr:
            print("     stderr:", res.stderr.strip()[:200])


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"[i] Chrome: {chrome_exe}")
    print(f"[i] Target: {SERVE_URL}")
    print(f"[i] Output: {SHOTS}")
    print()
    for name, w, hv, path, hf in TARGETS:
        shoot(name, w, hv, path, hf)
        time.sleep(0.3)
    print()
    print(f"[OK] {len(list(SHOTS.glob('*.png')))} screenshots saved to {SHOTS}")


if __name__ == "__main__":
    main()

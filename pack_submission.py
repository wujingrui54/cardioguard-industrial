# -*- coding: utf-8 -*-
"""
pack_submission.py
==================
一键打包参赛交付物为 ZIP,排除开发临时文件。

产出: submission_CardioGuard_Industrial_v1.0.0.zip (项目根目录)

包含:
- index.html, 404.html, manifest.json, robots.txt, sitemap.xml
- css/, js/, assets/ (含韩文PDF + icons + og-image + screenshots)
- PAPER_ZH.md, PAPER_KR.md, PAPER_EN.md (+ paper/*.docx 如已生成)
- README.md, SUBMISSION.md, CHANGELOG.md, CITATION.cff, LICENSE, .gitignore
- generate_pdf.py, convert_paper.py, pack_submission.py (脚本自身)

排除:
- __pycache__, .venv, node_modules, .vscode, .idea
- .claude, *.bak, *.tmp, submission_*.zip (避免嵌套打包)

运行:
    python pack_submission.py
"""
import os
import sys
import zipfile
import datetime
from pathlib import Path

VERSION = "1.0.0"
PROJECT_NAME = "CardioGuard_Industrial"
HERE = Path(__file__).parent.resolve()
OUT_NAME = f"submission_{PROJECT_NAME}_v{VERSION}.zip"
OUT_PATH = HERE / OUT_NAME

# 包内顶层目录名(防止解压时散文件污染用户桌面)
TOP_DIR = f"{PROJECT_NAME}_v{VERSION}"

# 排除模式 (glob-like, 简单字符串包含判断)
EXCLUDE_DIRS = {
    "__pycache__", ".venv", "venv", "env", "ENV",
    "node_modules", ".vscode", ".idea", ".claude",
    "dist", "build", ".cache", ".parcel-cache", ".next", ".vs",
    "$RECYCLE.BIN",
}
EXCLUDE_SUFFIXES = (".bak", ".tmp", ".log", ".pyc", ".pyo",
                    ".DS_Store",)
EXCLUDE_FILE_NAMES = {"Thumbs.db", "desktop.ini", "ehthumbs.db",
                      ".DS_Store"}

# 总是排除项目自身的 ZIP 输出和现有 ZIP 包(避免递归打包)
EXCLUDE_FILE_GLOB = ("submission_", )

INCLUDE_HIDDEN = {".gitignore"}   # 显式包含的隐藏文件


def should_skip_dir(name: str) -> bool:
    return name in EXCLUDE_DIRS or name.startswith(".") and name not in {".github"}


def should_skip_file(p: Path) -> bool:
    n = p.name
    if n in EXCLUDE_FILE_NAMES:
        return True
    if p.suffix.lower() in EXCLUDE_SUFFIXES:
        return True
    if any(n.startswith(g) for g in EXCLUDE_FILE_GLOB):
        return True
    if n.startswith(".") and n not in INCLUDE_HIDDEN:
        return True
    return False


def iter_files():
    """Yield (abs_path, arcname_in_zip)"""
    for root, dirs, files in os.walk(HERE):
        root_p = Path(root)
        # filter dirs in-place so os.walk doesn't descend
        dirs[:] = [d for d in dirs if not should_skip_dir(d)]
        for f in files:
            abs_p = root_p / f
            if should_skip_file(abs_p):
                continue
            rel = abs_p.relative_to(HERE).as_posix()
            arcname = f"{TOP_DIR}/{rel}"
            yield abs_p, arcname


def _human(n: int) -> str:
    for u in ("B", "KB", "MB", "GB"):
        if n < 1024:
            return f"{n:.1f} {u}"
        n /= 1024
    return f"{n:.1f} TB"


def build():
    if OUT_PATH.exists():
        OUT_PATH.unlink()

    files_added = []
    total_bytes = 0

    with zipfile.ZipFile(OUT_PATH, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for abs_p, arcname in iter_files():
            try:
                zf.write(abs_p, arcname)
                size = abs_p.stat().st_size
                total_bytes += size
                files_added.append((arcname, size))
            except OSError as e:
                print(f"  ! skip: {arcname}  ({e})", file=sys.stderr)

        # Embed a minimal manifest into the zip for review-time traceability
        manifest_lines = [
            f"CardioGuard Industrial — Submission Bundle",
            f"Project version : v{VERSION}",
            f"Packed at        : {datetime.datetime.now().isoformat(timespec='seconds')}",
            f"Total files      : {len(files_added)}",
            f"Total uncompressed : {_human(total_bytes)}",
            "",
            "Contents:",
        ] + [f"  {sz:>10}  {name}" for name, sz in sorted(files_added)]
        zf.writestr(f"{TOP_DIR}/_BUNDLE_MANIFEST.txt",
                    "\n".join(manifest_lines).encode("utf-8"))

    final_size = OUT_PATH.stat().st_size
    return files_added, total_bytes, final_size


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"[i] Packing submission bundle for {PROJECT_NAME} v{VERSION} ...")
    files_added, total_bytes, final_size = build()
    print()
    print(f"[OK] Bundle created: {OUT_PATH.name}")
    print(f"     Files included     : {len(files_added)}")
    print(f"     Uncompressed total : {_human(total_bytes)}")
    print(f"     ZIP file size      : {_human(final_size)}")
    print(f"     Path               : {OUT_PATH}")
    print()
    print("[i] Top-level layout inside ZIP:")
    seen_top = set()
    for name, _ in sorted(files_added):
        # show first 2 path components for overview
        parts = name.split("/", 2)
        key = "/".join(parts[:2]) if len(parts) >= 2 else parts[0]
        if key not in seen_top:
            seen_top.add(key)
            print(f"  - {key}/")

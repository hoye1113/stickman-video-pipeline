#!/usr/bin/env python3
"""
Base64 无感提取浏览器页面中最新生成的画格图片并写盘
- 自动过滤小图标与头像，精准定位 Google Flow / Nano Banana 2 生成的高清画格图片
- 兼容 blob:、googleusercontent.com 签名凭证 URL 与 data:image/png
- 自动落盘至项目的 04_raw_panels/ 目录并同步更新 meta.json
"""

import argparse
import base64
import os
import subprocess
import sys
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# 将仓库根目录加入 sys.path
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

try:
    from core.project_base import ProjectError, resolve_project
except ImportError:
    ProjectError = None
    resolve_project = None


def build_extract_js():
    """
    DOM 注入脚本：精确定位页面中生成的最新画格图像 URL
    """
    return """
(() => {
  const imgs = Array.from(document.querySelectorAll('img'));
  // 过滤小图标与头像，优先匹配大尺寸画格或带签名图片
  const validImgs = imgs.filter((img) => {
    const src = img.currentSrc || img.src || '';
    if (!src || src.startsWith('data:image/svg')) return false;
    const w = img.naturalWidth || img.width || 0;
    const h = img.naturalHeight || img.height || 0;
    return (
      w >= 256 ||
      h >= 256 ||
      src.includes('flow-content.google') ||
      src.includes('googleusercontent.com') ||
      src.startsWith('blob:')
    );
  });

  const target = validImgs.length ? validImgs[validImgs.length - 1] : null;
  if (!target) return 'no_image';
  return target.currentSrc || target.src;
})()
""".strip()


def fetch_image_bytes(session_id, tab_id=None):
    import urllib.request

    cmd = ["bsk", "evaluate", "--session", session_id]
    if tab_id:
        cmd += ["--tab-id", str(tab_id)]
    cmd.append(build_extract_js())

    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if res.returncode != 0:
        print("[错误] bsk evaluate 执行失败:", res.stderr, file=sys.stderr)
        return None

    src_or_data = res.stdout.strip()
    if not src_or_data or src_or_data == "no_image":
        print("[错误] 页面中未探测到符合条件的画格图片 (no_image)", file=sys.stderr)
        return None

    if src_or_data.startswith("http://") or src_or_data.startswith("https://"):
        req = urllib.request.Request(
            src_or_data,
            headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"},
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.read()

    if "base64," in src_or_data:
        _, b64_data = src_or_data.split("base64,", 1)
        return base64.b64decode(b64_data)

    print(f"[错误] 未预期的响应数据: {src_or_data[:150]}", file=sys.stderr)
    return None


def download_panel(session_id, out_path, project=None, out_filename=None, tab_id=None):
    out_path = Path(out_path).resolve()
    img_bytes = fetch_image_bytes(session_id, tab_id)
    if img_bytes is None:
        return False

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "wb") as f:
        f.write(img_bytes)

    print(f"[成功] 画格图片无感落盘: {out_path} ({len(img_bytes)} 字节)")

    if project is not None and out_filename:
        num = Path(out_filename).stem.replace("panel_", "")
        if num.isdigit():
            project.record_panel(int(num))
            print(f"[同步] meta.json 进度已更新: {project.meta_path}")

    return True


def main():
    parser = argparse.ArgumentParser(description="从已登录浏览器无感提取最新画格图片并写盘")
    parser.add_argument("--session", "-s", required=True, help="bsk 会话标识符 (session_id)")
    parser.add_argument("--filename", "-f", default="panel_01.png", help="输出图片文件名 (默认: panel_01.png)")
    parser.add_argument("--project", "-p", default=None, help="目标工程目录或标识符")
    parser.add_argument("--out", "-o", default=None, help="显式输出文件完整路径 (跳过项目元数据同步)")
    parser.add_argument("--tab-id", default=None, help="bsk tab id (默认活动标签)")

    args = parser.parse_args()

    if args.out:
        out_path = Path(args.out)
        ok = download_panel(args.session, out_path, tab_id=args.tab_id)
    else:
        try:
            project = resolve_project(args.project)
        except Exception as e:
            print(f"[错误] 无法定位项目: {e}", file=sys.stderr)
            sys.exit(1)

        print(f"[提示] 目标项目: {project.slug}")
        target_path = project.file("04_raw_panels", args.filename)
        ok = download_panel(
            session_id=args.session,
            out_path=target_path,
            project=project,
            out_filename=args.filename,
            tab_id=args.tab_id,
        )

    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()

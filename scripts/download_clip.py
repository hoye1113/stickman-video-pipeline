#!/usr/bin/env python3
"""
Base64 无损提取浏览器页面中最新生成的视频并写盘
- 自动跳过历史片段：优先选取最后一个 src 为 blob: 的 <video> 元素
- 兼容 Google Flow (Storyboard Studio) 与 Gemini 网页版（blob: 或带签名凭证 URL）
"""

import base64
import subprocess
import sys
import argparse
from pathlib import Path

try:
    from project_store import ProjectError, resolve_project
except ImportError:
    ProjectError = None
    resolve_project = None


def build_extract_js():
    return """
(async () => {
  const videos = Array.from(document.querySelectorAll('video'));
  const blobVideos = videos.filter((v) => (v.currentSrc || v.src || '').startsWith('blob:'));
  const video = blobVideos.length ? blobVideos[blobVideos.length - 1] : videos[videos.length - 1];
  if (!video) return 'no_video';
  const src = video.currentSrc || video.src;
  const res = await fetch(src, { credentials: 'include' });
  const blob = await res.blob();
  return new Promise((resolve) => {
    const reader = new FileReader();
    reader.onloadend = () => resolve(reader.result);
    reader.readAsDataURL(blob);
  });
})()
""".strip()


def fetch_video_base64(session_id, tab_id=None):
    cmd = ["bsk", "evaluate", "--session", session_id]
    if tab_id:
        cmd += ["--tab-id", str(tab_id)]
    cmd.append(build_extract_js())
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if res.returncode != 0:
        print("Error evaluating js via bsk:", res.stderr)
        return None
    data_url = res.stdout.strip()
    print("Data URL length:", len(data_url))
    if "base64," not in data_url:
        print("Unexpected response:", data_url[:150])
        return None
    _, b64_data = data_url.split("base64,", 1)
    return base64.b64decode(b64_data)


def download_video(session_id, out_path, project=None, out_filename=None, tab_id=None):
    out_path = Path(out_path)
    video_bytes = fetch_video_base64(session_id, tab_id)
    if video_bytes is None:
        return False

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "wb") as f:
        f.write(video_bytes)
    print(f"Successfully saved {out_path} ({len(video_bytes)} bytes)")

    if project is not None and out_filename:
        num = Path(out_filename).stem.replace("clip_", "")
        if num.isdigit():
            project.record_clip(int(num))
            print(f"meta.json 已更新：{project.meta_path}")

    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract the latest generated video from the browser via bsk evaluate")
    parser.add_argument("--session", "-s", default="uwym", help="bsk session id")
    parser.add_argument("--filename", "-f", default="clip_01.mp4", help="Output filename inside the project 04_raw_clips")
    parser.add_argument("--project", "-p", default=None, help="Target project directory name")
    parser.add_argument("--out", "-o", default=None, help="Explicit output file path (skips project/meta handling)")
    parser.add_argument("--tab-id", default=None, help="bsk tab id (defaults to the session's active tab)")
    args = parser.parse_args()

    if args.out:
        out_path = Path(args.out)
        ok = download_video(args.session, out_path, tab_id=args.tab_id)
    else:
        try:
            project = resolve_project(args.project)
        except ProjectError as e:
            print(f"[错误] {e}")
            sys.exit(1)
        print(f"[提示] 目标项目：{project.slug}")
        ok = download_video(
            args.session,
            project.file("04_raw_clips", args.filename),
            project=project,
            out_filename=args.filename,
            tab_id=args.tab_id,
        )

    sys.exit(0 if ok else 1)

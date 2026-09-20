#!/usr/bin/env python3
"""
Base64 无损提取 AI Studio 页面最新的 Blob 视频并写入目标项目
自动跳过历史片段：优先选取最后一个 src 为 blob: 的 <video> 元素
"""

import base64
import subprocess
import sys
import argparse
from pathlib import Path
from project_store import ProjectError, resolve_project


def download_video(session_id, out_filename, project):
    out_dir = project.file("04_raw_clips")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / out_filename

    js_code = """
(async () => {
  const videos = Array.from(document.querySelectorAll('video'));
  const blobVideos = videos.filter((v) => (v.currentSrc || v.src || '').startsWith('blob:'));
  const video = blobVideos.length ? blobVideos[blobVideos.length - 1] : videos[videos.length - 1];
  if (!video) return 'no_video';
  const src = video.currentSrc || video.src;
  const res = await fetch(src);
  const blob = await res.blob();
  return new Promise((resolve) => {
    const reader = new FileReader();
    reader.onloadend = () => resolve(reader.result);
    reader.readAsDataURL(blob);
  });
})()
""".strip()

    cmd = ["bsk", "evaluate", "--session", session_id, js_code]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")

    if res.returncode != 0:
        print("Error evaluating js via bsk:", res.stderr)
        return False

    data_url = res.stdout.strip()
    print("Data URL length:", len(data_url))

    if "base64," not in data_url:
        print("Unexpected response:", data_url[:150])
        return False

    _, b64_data = data_url.split("base64,", 1)
    video_bytes = base64.b64decode(b64_data)
    with open(out_path, "wb") as f:
        f.write(video_bytes)
    print(f"Successfully saved {out_path} ({len(video_bytes)} bytes)")

    num = Path(out_filename).stem.replace("clip_", "")
    if num.isdigit():
        project.record_clip(int(num))
        print(f"meta.json 已更新：{project.meta_path}")

    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download video from AI Studio via bsk evaluate")
    parser.add_argument("--session", "-s", default="uwym", help="bsk session id")
    parser.add_argument("--filename", "-f", default="clip_01.mp4", help="Output filename")
    parser.add_argument("--project", "-p", default=None, help="Target project directory name")
    args = parser.parse_args()

    try:
        project = resolve_project(args.project)
    except ProjectError as e:
        print(f"[错误] {e}")
        sys.exit(1)

    print(f"[提示] 目标项目：{project.slug}")
    sys.exit(0 if download_video(args.session, args.filename, project) else 1)

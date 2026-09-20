#!/usr/bin/env python3
"""
FFmpeg 视频无缝拼接脚本 (支持多项目目录)
"""

import subprocess
import sys
import argparse
from project_store import ProjectError, resolve_project


def concat_clips(project, output_filename="stitched_raw.mp4", crop_ratio=None):
    clips = project.clips()
    if not clips:
        print(f"[错误] {project.file('04_raw_clips')} 中未找到 clip_*.mp4 片段！")
        return False

    missing = project.missing_clip_indices()
    if missing:
        missing_str = ", ".join(f"clip_{i:02d}.mp4" for i in missing)
        print(f"[警告] 按 meta.json 应有 {project.total_clips} 段，当前缺失：{missing_str}")

    print(f"[提示] 项目 [{project.slug}] 找到 {len(clips)} 个视频片段：")
    for c in clips:
        print(f"  - {c}")

    output_file = project.file("06_final_video", output_filename)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    concat_list_path = project.file("04_raw_clips", "concat_list.txt")
    with open(concat_list_path, "w", encoding="utf-8") as f:
        for c in clips:
            f.write(f"file '{c.resolve().as_posix()}'\n")

    print(f"[提示] 正在使用 FFmpeg 拼接视频...")
    if crop_ratio == "4:3":
        vf_filter = ["-vf", "crop=ih*4/3:ih"]
        print("[提示] 启用 4:3 居中裁剪滤镜 (crop=ih*4/3:ih)...")
    elif crop_ratio:
        vf_filter = ["-vf", f"crop={crop_ratio}"]
    else:
        vf_filter = []

    if not vf_filter:
        cmd = [
            "ffmpeg", "-y",
            "-f", "concat",
            "-safe", "0",
            "-i", str(concat_list_path),
            "-c", "copy",
            str(output_file)
        ]
        try:
            subprocess.run(cmd, check=True)
            print(f"[成功] 拼接完成！输出路径：{output_file}")
            return True
        except subprocess.CalledProcessError:
            print("[警告] 直接流复制 (copy) 失败，可能存在编码或采样率微小差异，尝试重新编码拼接...")

    fallback_cmd = [
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", str(concat_list_path),
    ] + vf_filter + [
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "18",
        "-c:a", "aac",
        "-b:a", "192k",
        str(output_file)
    ]
    subprocess.run(fallback_cmd, check=True)
    print(f"[成功] 重新编码拼接完成！输出路径：{output_file}")
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Concat stickman clips using FFmpeg")
    parser.add_argument("--project", "-p", default=None, help="Target project directory name")
    parser.add_argument("--output", "-o", default="stitched_raw.mp4", help="Output filename inside 06_final_video")
    parser.add_argument("--crop-ratio", "-c", default=None, choices=["4:3", "16:9", "1:1"], help="Crop aspect ratio (e.g. 4:3 from 16:9)")
    args = parser.parse_args()

    try:
        project = resolve_project(args.project)
    except ProjectError as e:
        print(f"[错误] {e}")
        sys.exit(1)

    print(f"[提示] 目标项目：{project.summary()}")
    sys.exit(0 if concat_clips(project, args.output, crop_ratio=args.crop_ratio) else 1)

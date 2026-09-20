#!/usr/bin/env python3
"""
FFmpeg 字幕烧录与压制脚本 (支持多项目目录)
实现 embed-subtitles Skill 标准：
- RTL（从右至左语言，如希伯来语/阿拉伯语）自动检测与 Unicode 方向符（U+202B, U+202C）修复
- 规范的字幕字体、大小、边距、描边与阴影设置
- 支持指定项目目录自动推导路径，或显式指定输入输出
"""

import os
import re
import glob
import argparse
import subprocess
import sys
from project_store import ProjectError, resolve_project


def detect_and_fix_rtl(srt_path):
    with open(srt_path, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.split("\n")
    rtl_count = 0
    total_text_lines = 0

    # 匹配文本行（非编号，非时间轴）
    for line in lines:
        stripped = line.strip()
        if stripped and not re.match(r"^\d+$", stripped) and not re.match(r"^\d{2}:\d{2}:\d{2}", stripped):
            total_text_lines += 1
            if re.search(r"[\u0590-\u05FF\u0600-\u06FF\u0750-\u077F]", stripped):
                rtl_count += 1

    if total_text_lines > 0 and (rtl_count / total_text_lines) > 0.3:
        print("[提示] 检测到 RTL（从右至左语言）内容，正在应用 Unicode 换向标记 (U+202B / U+202C)...")
        fixed_lines = []
        for line in lines:
            stripped = line.strip()
            if stripped and not re.match(r"^\d+$", stripped) and not re.match(r"^\d{2}:\d{2}:\d{2}", stripped):
                line = "\u202B" + line + "\u202C"
            fixed_lines.append(line)

        fixed_path = str(srt_path).replace(".srt", ".rtl_fixed.srt")
        with open(fixed_path, "w", encoding="utf-8") as f:
            f.write("\n".join(fixed_lines))
        return fixed_path

    return srt_path


def probe_video_size(path):
    try:
        out = subprocess.run(
            ["ffprobe", "-v", "error", "-select_streams", "v:0",
             "-show_entries", "stream=width,height", "-of", "csv=p=0", path],
            capture_output=True, text=True, check=True,
        )
        w, h = out.stdout.strip().split(",")[:2]
        return int(w), int(h)
    except Exception:
        return None


def burn_subtitles(input_video, srt_path, output_video, font_size=22, font_name="Arial", margin=35):
    if not os.path.exists(input_video):
        print(f"[错误] 输入视频文件不存在: {input_video}")
        return False
    if not os.path.exists(srt_path):
        print(f"[错误] 字幕文件不存在: {srt_path}")
        return False

    processed_srt = detect_and_fix_rtl(srt_path)
    os.makedirs(os.path.dirname(os.path.abspath(output_video)), exist_ok=True)

    # Windows 路径转义用于 FFmpeg subtitles 过滤器
    escaped_srt = os.path.abspath(processed_srt).replace("\\", "/").replace(":", "\\:")

    # 构造 subtitles 过滤器参数 (Alignment: 2 = 底部居中)
    # PlayRes 必须与视频分辨率一致，否则 libass 会按默认 384x288 画布放大字号（竖屏会撑满全屏）
    size = probe_video_size(input_video)
    res_part = f",PlayResX={size[0]},PlayResY={size[1]}" if size else ""
    sub_style = f"FontSize={font_size},FontName={font_name}{res_part},PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,BorderStyle=1,Outline=2,Shadow=1,MarginV={margin},Alignment=2"
    filter_arg = f"subtitles='{escaped_srt}':force_style='{sub_style}'"

    cmd = [
        "ffmpeg", "-y",
        "-i", input_video,
        "-vf", filter_arg,
        "-c:v", "libx264",
        "-preset", "slow",
        "-crf", "18",
        "-c:a", "copy",
        output_video
    ]

    print(f"[提示] 正在压制字幕至视频...")
    try:
        subprocess.run(cmd, check=True)
        print(f"[成功] 成片输出完成: {output_video}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[错误] FFmpeg 执行失败: {e}")
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Burn subtitles into video using FFmpeg")
    parser.add_argument("--project", "-p", default=None, help="Target project directory name")
    parser.add_argument("-i", "--input", default=None, help="Input video file")
    parser.add_argument("-s", "--subtitles", default=None, help="SRT subtitle file")
    parser.add_argument("-o", "--output", default=None, help="Output video file")
    parser.add_argument("--font-size", type=int, default=None, help="Font size in pixels (default: auto 36 for vertical, 26 for horizontal)")
    parser.add_argument("--font-name", default="Arial", help="Font family name")
    parser.add_argument("--margin", type=int, default=None, help="Bottom margin in pixels (default: auto 350 for vertical, 50 for horizontal 4:3/16:9)")

    args = parser.parse_args()

    project = None
    if args.project or not (args.input and args.subtitles and args.output):
        try:
            project = resolve_project(args.project)
        except ProjectError as e:
            print(f"[错误] {e}")
            sys.exit(1)
        print(f"[提示] 目标项目：{project.summary()}")

    input_video = args.input
    srt_path = args.subtitles
    output_video = args.output

    if project:
        if not input_video:
            input_video = str(project.file("06_final_video", "stitched_raw.mp4"))
        if not srt_path:
            srts = sorted(glob.glob(str(project.file("05_subtitles", "*.srt"))))
            srt_path = srts[0] if srts else str(project.file("05_subtitles", "narration.srt"))
        if not output_video:
            output_video = str(project.file("06_final_video", "final_subtitled.mp4"))

    # 智能自适应分辨率与画幅比例
    size = probe_video_size(input_video) if input_video and os.path.exists(input_video) else None
    is_vertical = (size[1] > size[0]) if size else False

    if args.font_size is not None:
        font_size = args.font_size
    else:
        font_size = 36 if is_vertical else 26

    if args.margin is not None:
        margin = args.margin
    else:
        # 竖屏需抬高 350px 避让短视频底部 UI；横屏（4:3 或 16:9）置于底部安全边距 50px
        margin = 350 if is_vertical else 50

    print(f"[配置] 视频分辨率：{size or '未知'} | 模式：{'竖屏 9:16' if is_vertical else '横屏 4:3/16:9'} | 字号：{font_size} | 底部边距：{margin}px")

    sys.exit(0 if burn_subtitles(input_video, srt_path, output_video, font_size, args.font_name, margin) else 1)

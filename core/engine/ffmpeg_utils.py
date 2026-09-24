#!/usr/bin/env python3
"""
FFmpeg 通用工具与封装模块 (Core Engine)
集中处理：
1. 视频分辨率/画幅比探测 (probe_video_size)
2. RTL 从右至左语言文本检测与 Unicode 纠正 (detect_and_fix_rtl)
3. 智能字幕样式构建与压制 (burn_subtitles, build_subtitles_filter)
"""

import os
import re
import subprocess
from pathlib import Path


def probe_video_size(path):
    """
    探测视频分辨率 (宽, 高)。
    返回 (int(width), int(height)) 或 None。
    """
    if not path or not os.path.exists(path):
        return None
    try:
        out = subprocess.run(
            [
                "ffprobe", "-v", "error", "-select_streams", "v:0",
                "-show_entries", "stream=width,height", "-of", "csv=p=0", str(path)
            ],
            capture_output=True, text=True, check=True,
        )
        parts = out.stdout.strip().split(",")[:2]
        if len(parts) >= 2 and parts[0].isdigit() and parts[1].isdigit():
            return int(parts[0]), int(parts[1])
        return None
    except Exception:
        return None


def probe_media_duration(path):
    """
    探测音视频媒体文件的精确时长（秒）。
    返回 float(seconds) 或 None。
    """
    if not path or not os.path.exists(path):
        return None
    try:
        out = subprocess.run(
            [
                "ffprobe", "-v", "error",
                "-show_entries", "format=duration",
                "-of", "default=noprint_wrappers=1:nokey=1",
                str(path)
            ],
            capture_output=True, text=True, check=True,
        )
        val = out.stdout.strip()
        if val:
            return float(val)
        return None
    except Exception:
        return None



def detect_and_fix_rtl(srt_path):
    """
    检测并在必要时为从右至左语言（希伯来语、阿拉伯语等）注入 Unicode 换向标记 (U+202B, U+202C)。
    返回处理后的 SRT 文件路径。
    """
    if not os.path.exists(srt_path):
        return srt_path

    with open(srt_path, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.split("\n")
    rtl_count = 0
    total_text_lines = 0

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


def build_subtitles_filter(srt_path, font_size=54, font_name="Arial", margin=60, video_size=None):
    """
    构建 Windows / POSIX 兼容的 FFmpeg subtitles 滤镜参数。
    PlayRes 必须与视频分辨率对齐，避免 libass 在竖屏等非默认比例下字号缩放异常。
    采用纯白字、高对比度粗黑描边 (Outline=3, Shadow=0)、严格底部基线对齐 (Alignment=2)。
    """
    escaped_srt = os.path.abspath(srt_path).replace("\\", "/").replace(":", "\\:").replace("'", r"\'")
    res_part = f",PlayResX={video_size[0]},PlayResY={video_size[1]}" if video_size else ""
    sub_style = (
        f"FontSize={font_size},FontName={font_name}{res_part},"
        f"PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,"
        f"BorderStyle=1,Outline=3,Shadow=0,MarginV={margin},Alignment=2"
    )
    return f"subtitles='{escaped_srt}':force_style='{sub_style}'"


def burn_subtitles(input_video, srt_path, output_video, font_size=None, font_name="Arial", margin=None):
    """
    统一烧录字幕到视频并输出成片。
    自动探测视频画幅（横屏/竖屏），并设定符合移动端高可读性的工业级大字号与固定安全边距。
    """
    if not os.path.exists(input_video):
        print(f"[错误] 输入视频文件不存在: {input_video}")
        return False
    if not os.path.exists(srt_path):
        print(f"[错误] 字幕文件不存在: {srt_path}")
        return False

    processed_srt = detect_and_fix_rtl(srt_path)
    os.makedirs(os.path.dirname(os.path.abspath(output_video)), exist_ok=True)

    size = probe_video_size(input_video)
    is_vertical = (size[1] > size[0]) if size else False

    # 移动端横屏 4:3/16:9 字号提升至 54（原 26 的两倍以上，面积增大4倍），竖屏提升至 48
    actual_font_size = font_size if font_size is not None else (48 if is_vertical else 54)
    actual_margin = margin if margin is not None else (350 if is_vertical else 60)

    print(
        f"[配置] 视频分辨率：{size or '未知'} | 模式：{'竖屏 9:16' if is_vertical else '横屏 4:3/16:9'} | "
        f"字号：{actual_font_size} | 底部边距：{actual_margin}px"
    )

    filter_arg = build_subtitles_filter(
        processed_srt,
        font_size=actual_font_size,
        font_name=font_name,
        margin=actual_margin,
        video_size=size,
    )

    cmd = [
        "ffmpeg", "-y",
        "-i", str(input_video),
        "-vf", filter_arg,
        "-c:v", "libx264",
        "-preset", "slow",
        "-crf", "18",
        "-c:a", "copy",
        str(output_video)
    ]

    print(f"[提示] 正在压制字幕至视频...")
    try:
        subprocess.run(cmd, check=True)
        print(f"[成功] 成片输出完成: {output_video}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[错误] FFmpeg 执行失败: {e}")
        return False

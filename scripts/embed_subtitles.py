#!/usr/bin/env python3
"""
FFmpeg 字幕烧录与压制脚本 (支持多项目目录)
实现 embed-subtitles Skill 标准：
- RTL（从右至左语言，如希伯来语/阿拉伯语）自动检测与 Unicode 方向符（U+202B, U+202C）修复
- 规范的字幕字体、大小、边距、描边与阴影设置
- 支持指定项目目录自动推导路径，或显式指定输入输出
- 底层通用滤镜与探针统一由 core.engine.ffmpeg_utils 驱动
"""

import os
import glob
import argparse
import sys
from pathlib import Path

# 确保能定位并导入 core 模块
_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from core.engine.ffmpeg_utils import (
    probe_video_size,
    detect_and_fix_rtl,
    burn_subtitles,
    build_subtitles_filter,
)
from project_store import ProjectError, resolve_project


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
        # 根据不同题材规范自适应字幕与成片目录
        if project.genre == "comic_story":
            sub_stage = "05_voiceover_and_srt"
            out_stage = "07_final_video"
        else:
            sub_stage = "05_subtitles"
            out_stage = "06_final_video"

        if not input_video:
            candidates = [
                project.file(out_stage, "stitched_raw.mp4"),
                project.file(out_stage, "story_stitched.mp4"),
            ]
            for cand in candidates:
                if cand.exists():
                    input_video = str(cand)
                    break
            if not input_video:
                input_video = str(candidates[0])

        if not srt_path:
            srts = sorted(glob.glob(str(project.file(sub_stage, "*.srt"))))
            srt_path = srts[0] if srts else str(project.file(sub_stage, "narration.srt"))

        if not output_video:
            output_video = str(project.file(out_stage, "final_subtitled.mp4"))

    sys.exit(0 if burn_subtitles(input_video, srt_path, output_video, args.font_size, args.font_name, args.margin) else 1)

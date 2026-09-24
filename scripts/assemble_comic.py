#!/usr/bin/env python3
"""
动态漫画全片组装与成片压制工具 (Comic Story Assembler)
功能：
1. 自动排序并无损/高质拼接 06_animated_clips/ 中的所有运镜短切片；
2. 可选混入背景氛围音乐 (BGM / Ambient Sound)；
3. 调用 core.engine.ffmpeg_utils 统一压制白字黑边工业级字幕；
4. 交付 07_final_video/final_comic_story.mp4 高清成片。
"""

import argparse
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

from core.engine.ffmpeg_utils import burn_subtitles, probe_media_duration, probe_video_size
from core.project_base import resolve_project


def assemble_clips(
    clip_paths,
    output_stitched,
    bgm_path=None,
    bgm_volume=0.15
):
    """
    拼接多个运镜视频片段，并可选混合 BGM 氛围音
    """
    if not clip_paths:
        print("[错误] 未提供任何待拼接的视频切片！", file=sys.stderr)
        return False

    os.makedirs(os.path.dirname(os.path.abspath(output_stitched)), exist_ok=True)

    # 构造 concat 文件列表
    temp_list = output_stitched.parent / "_concat_list.txt"
    with open(temp_list, "w", encoding="utf-8") as f:
        for p in clip_paths:
            escaped = str(p.resolve()).replace("\\", "/")
            f.write(f"file '{escaped}'\n")

    # 基础 concat 命令
    if not bgm_path or not os.path.exists(bgm_path):
        cmd = [
            "ffmpeg", "-y",
            "-f", "concat",
            "-safe", "0",
            "-i", str(temp_list),
            "-c:v", "libx264",
            "-preset", "fast",
            "-crf", "18",
            "-c:a", "aac",
            "-b:a", "192k",
            str(output_stitched)
        ]
    else:
        # 有 BGM 时：混合主语音音轨与循环衰减的 BGM
        cmd = [
            "ffmpeg", "-y",
            "-f", "concat",
            "-safe", "0",
            "-i", str(temp_list),
            "-stream_loop", "-1",
            "-i", str(bgm_path),
            "-filter_complex",
            f"[1:a]volume={bgm_volume}[bgm];[0:a][bgm]amix=inputs=2:duration=first:dropout_transition=2[aout]",
            "-map", "0:v",
            "-map", "[aout]",
            "-c:v", "libx264",
            "-preset", "fast",
            "-crf", "18",
            "-c:a", "aac",
            "-b:a", "192k",
            "-shortest",
            str(output_stitched)
        ]

    try:
        print(f"[合成] 正在合并 {len(clip_paths)} 个动态切片...")
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        if temp_list.exists():
            temp_list.unlink()
        return True
    except subprocess.CalledProcessError as e:
        print(f"[错误] 片段拼接失败: {e.stderr.decode('utf-8', errors='ignore')}", file=sys.stderr)
        if temp_list.exists():
            temp_list.unlink()
        return False


def process_project_assembly(
    project_dir,
    output_filename="final_comic_story.mp4",
    bgm_path=None,
    bgm_volume=0.15,
    font_name="Microsoft YaHei",
    font_size=None,
    margin=None,
    no_subs=False
):
    """
    项目级端到端组装
    """
    project_path = Path(project_dir).resolve()
    clips_dir = project_path / "06_animated_clips"
    subs_dir = project_path / "05_voiceover_and_srt"
    final_dir = project_path / "07_final_video"
    final_dir.mkdir(parents=True, exist_ok=True)

    clips = sorted([f for f in clips_dir.iterdir() if f.is_file() and f.suffix.lower() == ".mp4"])
    if not clips:
        print(f"[错误] {clips_dir} 下未找到任何已渲染的 .mp4 切片，请先运行 animate_panels.py", file=sys.stderr)
        return False

    stitched_raw = final_dir / "_stitched_raw.mp4"
    final_output = final_dir / output_filename

    ok = assemble_clips(
        clip_paths=clips,
        output_stitched=stitched_raw,
        bgm_path=bgm_path,
        bgm_volume=bgm_volume
    )
    if not ok:
        return False

    total_duration = probe_media_duration(stitched_raw)
    size = probe_video_size(stitched_raw)
    print(f"[成功] 拼接切片完成！总时长: {total_duration:.2f}s | 分辨率: {size}")

    if no_subs:
        if stitched_raw.exists():
            if final_output.exists():
                final_output.unlink()
            stitched_raw.rename(final_output)
            print(f"[交付] 跳过字幕烧录，成片交付: {final_output}")
            return True

    # 寻找字幕文件（优先采用纯单行、基线绝对恒定的 single_line 字幕）
    srt_candidates = [
        subs_dir / "narration.single_line.srt",
        subs_dir / "narration.srt",
        subs_dir / "narration.bilingual.srt",
    ]
    srt_file = None
    for cand in srt_candidates:
        if cand.exists():
            srt_file = cand
            break

    if not srt_file:
        print(f"[警告] 未找到主字幕文件 (narration.srt)，直接交付无字幕成片")
        if stitched_raw.exists():
            if final_output.exists():
                final_output.unlink()
            stitched_raw.rename(final_output)
        return True

    print(f"[字幕] 正在烧录白字黑边字幕: {srt_file.name}")
    sub_ok = burn_subtitles(
        input_video=str(stitched_raw),
        srt_path=str(srt_file),
        output_video=str(final_output),
        font_size=font_size,
        font_name=font_name,
        margin=margin
    )

    if sub_ok and stitched_raw.exists():
        stitched_raw.unlink()  # 清理中间拼接大文件

    if sub_ok:
        print(f"\n=======================================================")
        print(f"[成功] 动态漫画最终成片压制成功！")
        print(f"[成片] 输出路径: {final_output}")
        print(f"[时长] 视频总长: {total_duration:.2f} 秒")
        print(f"=======================================================")
        return True
    return False


def main():
    parser = argparse.ArgumentParser(description="动态漫画全片组装与成片压制工具")
    parser.add_argument("--project", "-p", help="项目路径或标识符 (例如: 002_rainy_detective)")
    parser.add_argument("--output", "-o", default="final_comic_story.mp4", help="最终交付成片文件名")
    parser.add_argument("--bgm", help="可选环境音或背景音乐路径 (MP3/WAV)")
    parser.add_argument("--bgm-volume", type=float, default=0.15, help="BGM 相对音量 (默认: 0.15)")
    parser.add_argument("--font-name", default="Microsoft YaHei", help="中文字体名称 (默认: Microsoft YaHei)")
    parser.add_argument("--font-size", type=int, help="字幕字号 (留空自适应)")
    parser.add_argument("--margin", type=int, help="字幕底部安全边距 (留空自适应)")
    parser.add_argument("--no-subs", action="store_true", help="跳过字幕烧录")

    args = parser.parse_args()

    if args.project:
        proj = resolve_project(args.project)
        target_dir = proj.path if proj else Path(args.project).resolve()
        if not target_dir.exists():
            print(f"[错误] 无法定位项目目录: {args.project}", file=sys.stderr)
            sys.exit(1)

        ok = process_project_assembly(
            project_dir=target_dir,
            output_filename=args.output,
            bgm_path=args.bgm,
            bgm_volume=args.bgm_volume,
            font_name=args.font_name,
            font_size=args.font_size,
            margin=args.margin,
            no_subs=args.no_subs
        )
        sys.exit(0 if ok else 1)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

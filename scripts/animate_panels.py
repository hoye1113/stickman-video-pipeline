#!/usr/bin/env python3
"""
动态漫画代码运镜渲染引擎 (Ken Burns & Motion Comic Engine)
功能：
1. 单张静态画格生成高质量电影级运镜短切片 (slow_push, slow_pull, pan, breathing_drift, snap_zoom, shake)；
2. 批量扫描项目中的 04_raw_panels 与 05_voiceover_and_srt/durations.json，一键渲染 06_animated_clips。
3. 零云端调用、零大模型积分消耗、纯本地 FFmpeg 极速渲染。
"""

import argparse
import json
import math
import os
import re
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

from core.engine.ffmpeg_utils import probe_media_duration
from core.project_base import resolve_project

DEFAULT_RESOLUTION = "1440x1080"  # 4:3 默认高精
DEFAULT_FPS = 24


def build_motion_filter(motion, duration, width, height, fps=24):
    """
    根据运镜意图构建精确的 FFmpeg scale + crop + zoompan + supersample 滤镜链。
    采用 2X 超采样 (Supersampling) 抗亚像素阶梯抖动，并彻底剔除任何 sin/cos 周期性剧烈晃动，
    实现专业电影级丝滑、平稳、无抽搐的镜头推拉与横移。
    """
    total_frames = max(1, int(round(fps * duration)))
    motion_clean = motion.lower().replace("-", "_").strip()

    # 第一阶段：2X 超采样预缩放（2880x2160），在更高像素网格上计算位移，消除量化跳帧
    super_w = width * 2
    super_h = height * 2
    pre_filter = f"scale={super_w}:{super_h}:force_original_aspect_ratio=increase,crop={super_w}:{super_h}"

    # 第二阶段：构建纯线性、平稳平滑的 zoompan 坐标与缩放
    if motion_clean in ("slow_push", "zoom_in", "push"):
        # 匀速慢速推入 (1.0 -> 1.08)，沉浸聚焦
        zoom_step = 0.08 / total_frames
        z_expr = f"min(zoom+{zoom_step:.6f},1.08)"
        x_expr = "iw/2-(iw/zoom/2)"
        y_expr = "ih/2-(ih/zoom/2)"

    elif motion_clean in ("slow_pull", "zoom_out", "pull"):
        # 匀速慢速拉远 (1.08 -> 1.0)，营造疏离与唏嘘感
        zoom_step = 0.08 / total_frames
        z_expr = f"if(eq(on,1),1.08,max(1.0,zoom-{zoom_step:.6f}))"
        x_expr = "iw/2-(iw/zoom/2)"
        y_expr = "ih/2-(ih/zoom/2)"

    elif motion_clean in ("pan_left", "left"):
        # 放大 1.10x，从右向左匀速平稳横移
        z_expr = "1.10"
        x_expr = f"(iw-iw/zoom)*(1.0-on/{total_frames})"
        y_expr = "ih/2-(ih/zoom/2)"

    elif motion_clean in ("pan_right", "right"):
        # 放大 1.10x，从左向右匀速平稳横移
        z_expr = "1.10"
        x_expr = f"(iw-iw/zoom)*(on/{total_frames})"
        y_expr = "ih/2-(ih/zoom/2)"

    elif motion_clean in ("breathing_drift", "drift", "breathe"):
        # 彻底废除 sin/cos 周期晃动！重构为极度平缓、沉稳的微推 (1.00 -> 1.04)
        zoom_step = 0.04 / total_frames
        z_expr = f"min(zoom+{zoom_step:.6f},1.04)"
        x_expr = "iw/2-(iw/zoom/2)"
        y_expr = "ih/2-(ih/zoom/2)"

    elif motion_clean in ("snap_zoom", "snap", "impact"):
        # 前段平滑缓动推入至 1.10x，后段稳态慢推，彻底移除剧烈弹跳
        snap_f = max(6, int(total_frames * 0.35))
        rem_f = max(1, total_frames - snap_f)
        z_expr = f"if(lte(on,{snap_f}),1.0+0.08*(on/{snap_f}),1.08+0.02*((on-{snap_f})/{rem_f}))"
        x_expr = "iw/2-(iw/zoom/2)"
        y_expr = "ih/2-(ih/zoom/2)"

    else:
        # static / none: 稳态居中展示
        z_expr = "1.0"
        x_expr = "iw/2-(iw/zoom/2)"
        y_expr = "ih/2-(ih/zoom/2)"

    zoompan_arg = (
        f"zoompan=z='{z_expr}':x='{x_expr}':y='{y_expr}':d={total_frames}:"
        f"s={super_w}x{super_h}:fps={fps}"
    )

    # 第三阶段：高品质 Lanczos 降采样回目标画布，平滑边缘并消除微小像素锯齿
    post_filter = f"scale={width}:{height}:flags=lanczos"

    return f"{pre_filter},{zoompan_arg},{post_filter}"


def render_panel_clip(
    image_path,
    output_path,
    duration=3.0,
    motion="slow_push",
    audio_path=None,
    resolution=DEFAULT_RESOLUTION,
    fps=DEFAULT_FPS
):
    """
    渲染单张图片为动态视频切片
    """
    if not os.path.exists(image_path):
        print(f"[错误] 输入画格不存在: {image_path}", file=sys.stderr)
        return False

    width, height = [int(v) for v in resolution.split("x")]
    vf_arg = build_motion_filter(motion, duration, width, height, fps)

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)

    cmd = [
        "ffmpeg", "-y",
        "-loop", "1",
        "-i", str(image_path)
    ]

    if audio_path and os.path.exists(audio_path):
        cmd.extend(["-i", str(audio_path)])

    cmd.extend([
        "-vf", vf_arg,
        "-t", f"{duration:.3f}",
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "18",
        "-pix_fmt", "yuv420p"
    ])

    if audio_path and os.path.exists(audio_path):
        cmd.extend(["-c:a", "aac", "-ar", "44100", "-ac", "2", "-b:a", "192k", "-shortest"])
    else:
        # 如果没有传入音频，生成静音频轨以保证后续无缝拼接兼容性 (44100Hz stereo)
        cmd.extend([
            "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo",
            "-c:a", "aac", "-ar", "44100", "-ac", "2", "-b:a", "128k", "-shortest"
        ])

    cmd.append(str(output_path))

    try:
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError as e:
        print(f"[错误] FFmpeg 渲染画格失败: {e.stderr.decode('utf-8', errors='ignore')}", file=sys.stderr)
        return False


def process_project_panels(project_dir, resolution=DEFAULT_RESOLUTION, fps=DEFAULT_FPS):
    """
    批量渲染项目的所有画格
    """
    project_path = Path(project_dir).resolve()
    raw_panels_dir = project_path / "04_raw_panels"
    voice_dir = project_path / "05_voiceover_and_srt"
    output_dir = project_path / "06_animated_clips"
    output_dir.mkdir(parents=True, exist_ok=True)

    durations_file = voice_dir / "durations.json"
    panel_info = {}

    if durations_file.exists():
        with open(durations_file, "r", encoding="utf-8") as f:
            panel_info = json.load(f)

    # 扫描 raw_panels 下的所有图片
    valid_extensions = {".png", ".jpg", ".jpeg", ".webp"}
    raw_images = sorted([
        f for f in raw_panels_dir.iterdir()
        if f.is_file() and f.suffix.lower() in valid_extensions
    ])

    if not raw_images:
        print(f"[错误] 在 {raw_panels_dir} 中未发现任何画格图片！", file=sys.stderr)
        print("  提示: 请先在 Google Flow 中通过 Nano Banana 2 (0积分) 生成画格并存放于该目录下。")
        return False

    print(f"[批处理] 发现 {len(raw_images)} 个原始画格，分辨率目标: {resolution} (FPS: {fps})")

    # 默认交替运镜序列
    default_motions = ["slow_push", "breathing_drift", "pan_right", "slow_pull", "snap_zoom"]

    success_count = 0
    for idx, img in enumerate(raw_images):
        pid = img.stem
        info = panel_info.get(pid, {})

        duration = info.get("duration", 3.5)
        motion = info.get("motion", default_motions[idx % len(default_motions)])

        # 查找匹配的语音文件
        audio_candidate = voice_dir / f"{pid}.mp3"
        audio_path = str(audio_candidate) if audio_candidate.exists() else None

        output_clip = output_dir / f"{pid}.mp4"

        print(f"  -> 正在渲染 {pid} (时长: {duration:.2f}s | 运镜: {motion}) -> {output_clip.name}")
        ok = render_panel_clip(
            image_path=str(img),
            output_path=str(output_clip),
            duration=duration,
            motion=motion,
            audio_path=audio_path,
            resolution=resolution,
            fps=fps
        )
        if ok:
            success_count += 1

    print(f"\n[完成] 动态运镜渲染完成: 成功 {success_count}/{len(raw_images)} 个片段置于 {output_dir}")
    return success_count == len(raw_images)


def main():
    parser = argparse.ArgumentParser(description="动态漫画代码运镜渲染引擎 (Ken Burns Motion Engine)")
    parser.add_argument("--project", "-p", help="项目路径或标识符 (例如: 002_rainy_detective)")
    parser.add_argument("--image", "-i", help="单张输入画格图片路径")
    parser.add_argument("--output", "-o", default="panel_animated.mp4", help="输出视频切片路径")
    parser.add_argument("--duration", "-d", type=float, default=3.5, help="动画时长（秒）")
    parser.add_argument(
        "--motion", "-m", default="slow_push",
        choices=["slow_push", "slow_pull", "pan_left", "pan_right", "pan_up", "pan_down", "breathing_drift", "snap_zoom", "shake", "static"],
        help="运镜动作预设"
    )
    parser.add_argument("--audio", "-a", help="可选绑定的语音 MP3 音频路径")
    parser.add_argument("--resolution", "-r", default=DEFAULT_RESOLUTION, help=f"目标分辨率 (默认: {DEFAULT_RESOLUTION})")
    parser.add_argument("--fps", type=int, default=DEFAULT_FPS, help=f"视频帧率 (默认: {DEFAULT_FPS})")

    args = parser.parse_args()

    if args.project:
        proj = resolve_project(args.project)
        target_dir = proj.path if proj else Path(args.project).resolve()
        if not target_dir.exists():
            print(f"[错误] 无法定位项目目录: {args.project}", file=sys.stderr)
            sys.exit(1)

        ok = process_project_panels(target_dir, resolution=args.resolution, fps=args.fps)
        sys.exit(0 if ok else 1)

    elif args.image:
        print(f"[渲染] 正在对 {args.image} 施加运镜 [{args.motion}] (时长: {args.duration}s)...")
        ok = render_panel_clip(
            image_path=args.image,
            output_path=args.output,
            duration=args.duration,
            motion=args.motion,
            audio_path=args.audio,
            resolution=args.resolution,
            fps=args.fps
        )
        if ok:
            print(f"[成功] 动态切片输出完成: {args.output}")
        else:
            sys.exit(1)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

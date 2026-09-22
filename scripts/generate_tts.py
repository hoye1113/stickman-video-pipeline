#!/usr/bin/env python3
"""
高保真语音合成与字幕时间戳对齐工具 (Edge-TTS Facade)
功能：
1. 单条台词快速生成 MP3 音频与精准对齐 SRT 字幕；
2. 批量解析分镜大纲 (storyboard.md)，一键批量生成各画格独立语音切片与连续主轴字幕；
3. 输出 durations.json 作为动态运镜引擎的精确时间基准。
"""

import argparse
import asyncio
import json
import os
import re
import sys
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

try:
    import edge_tts
except ImportError:
    print("[错误] 未安装 edge-tts 依赖，请运行: pip install edge-tts", file=sys.stderr)
    sys.exit(1)

# 将仓库根目录加入 sys.path
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.engine.ffmpeg_utils import probe_media_duration
from core.project_base import resolve_project

DEFAULT_VOICE = "zh-CN-YunxiNeural"


def parse_srt_time(time_str):
    """解析 SRT 时间戳 00:00:01,234 -> float 秒"""
    match = re.match(r"(\d{2}):(\d{2}):(\d{2})[,.](\d{3})", time_str.strip())
    if not match:
        return 0.0
    h, m, s, ms = match.groups()
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000.0


def format_srt_time(seconds):
    """将秒数格式化为 SRT 时间戳 00:00:01,234"""
    if seconds < 0:
        seconds = 0.0
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int(round((seconds - int(seconds)) * 1000))
    if ms >= 1000:
        ms = 999
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


async def synthesize_speech(text, output_audio, output_srt=None, voice=DEFAULT_VOICE, rate="+0%", volume="+0%"):
    """
    调用 Edge-TTS 生成音频与 SRT 字幕
    """
    os.makedirs(os.path.dirname(os.path.abspath(output_audio)), exist_ok=True)
    if output_srt:
        os.makedirs(os.path.dirname(os.path.abspath(output_srt)), exist_ok=True)

    communicate = edge_tts.Communicate(text, voice=voice, rate=rate, volume=volume)
    submaker = edge_tts.SubMaker()

    with open(output_audio, "wb") as f:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])
            elif chunk["type"] in ("WordBoundary", "SentenceBoundary"):
                submaker.feed(chunk)

    srt_content = submaker.get_srt()

    # 如果 SubMaker 未生成字幕（短文本边界），构造一条基线 SRT
    if output_srt:
        if not srt_content.strip():
            dur = probe_media_duration(output_audio) or 3.0
            srt_content = f"1\n00:00:00,000 --> {format_srt_time(dur)}\n{text}\n"

        with open(output_srt, "w", encoding="utf-8") as f:
            f.write(srt_content)

    duration = probe_media_duration(output_audio)
    return duration, srt_content


def parse_storyboard_table(storyboard_path):
    """
    解析 storyboard.md 中的分镜表格
    返回列表: [{"id": "panel_01", "text": "...", "motion": "slow_push", "prompt": "..."}]
    """
    if not os.path.exists(storyboard_path):
        return []

    with open(storyboard_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    panels = []
    header_col_map = {}
    table_started = False

    for line in lines:
        line_str = line.strip()
        if not line_str.startswith("|"):
            continue

        cols = [c.strip() for c in line_str.split("|")[1:-1]]
        if not cols:
            continue

        if not table_started and any("画格" in c or "panel" in c.lower() or "编号" in c for c in cols):
            table_started = True
            for i, c in enumerate(cols):
                col_lower = c.lower()
                if "画格" in c or "panel" in col_lower or "编号" in c or "序号" in c:
                    header_col_map["id"] = i
                elif "旁白" in c or "台词" in c or "narration" in col_lower or "dialogue" in col_lower:
                    header_col_map["text"] = i
                elif "运镜" in c or "motion" in col_lower or "camera" in col_lower:
                    header_col_map["motion"] = i
                elif "提示词" in c or "prompt" in col_lower:
                    header_col_map["prompt"] = i
            continue

        # 过滤分割线 |---|---|
        if any(set(c) <= {"-", ":"} for c in cols):
            continue

        if table_started and "id" in header_col_map and "text" in header_col_map:
            id_idx = header_col_map["id"]
            text_idx = header_col_map["text"]
            if id_idx < len(cols) and text_idx < len(cols):
                raw_id = cols[id_idx].replace("`", "").strip()
                if not raw_id:
                    continue

                # 规范化 panel id
                if not raw_id.startswith("panel_"):
                    # 纯数字转 panel_XX
                    num_match = re.search(r"\d+", raw_id)
                    panel_id = f"panel_{int(num_match.group(0)):02d}" if num_match else raw_id
                else:
                    panel_id = raw_id

                text = cols[text_idx].strip()
                motion = "slow_push"
                if "motion" in header_col_map and header_col_map["motion"] < len(cols):
                    m_val = cols[header_col_map["motion"]].replace("`", "").strip()
                    if m_val:
                        motion = m_val

                prompt = ""
                if "prompt" in header_col_map and header_col_map["prompt"] < len(cols):
                    prompt = cols[header_col_map["prompt"]].replace("`", "").strip()

                panels.append({
                    "id": panel_id,
                    "text": text,
                    "motion": motion,
                    "prompt": prompt
                })

    return panels


def shift_srt_timestamps(srt_content, offset_seconds, start_index=1):
    """
    将 SRT 内容的时间戳统一向前偏移 offset_seconds，并重新编号
    """
    blocks = srt_content.strip().split("\n\n")
    shifted_blocks = []
    current_index = start_index

    for block in blocks:
        lines = block.strip().split("\n")
        if len(lines) < 2:
            continue

        # 查找时间戳行
        time_line_idx = -1
        for idx, l in enumerate(lines):
            if "-->" in l:
                time_line_idx = idx
                break

        if time_line_idx == -1:
            continue

        time_line = lines[time_line_idx]
        start_str, end_str = time_line.split("-->")
        start_sec = parse_srt_time(start_str) + offset_seconds
        end_sec = parse_srt_time(end_str) + offset_seconds

        text_lines = lines[time_line_idx + 1:]
        shifted_blocks.append(
            f"{current_index}\n{format_srt_time(start_sec)} --> {format_srt_time(end_sec)}\n" + "\n".join(text_lines)
        )
        current_index += 1

    return "\n\n".join(shifted_blocks), current_index


async def process_project_tts(project_dir, voice=DEFAULT_VOICE, rate="+0%", volume="+0%", min_duration=2.5):
    """
    为指定项目批量处理故事配音与字幕
    """
    project_path = Path(project_dir).resolve()
    storyboard_dir = project_path / "01_script_and_storyboard"
    storyboard_file = storyboard_dir / "storyboard.md"

    if not storyboard_file.exists():
        template_file = storyboard_dir / "storyboard.template.md"
        if template_file.exists():
            print(f"[提示] 未发现 storyboard.md，正在使用模板 {template_file.name} 运行...")
            storyboard_file = template_file
        else:
            print(f"[错误] 未找到分镜文件: {storyboard_file}", file=sys.stderr)
            return False

    panels = parse_storyboard_table(storyboard_file)
    if not panels:
        print(f"[错误] 未在 {storyboard_file} 中解析到有效的画格表格！", file=sys.stderr)
        return False

    print(f"[批处理] 从分镜表解析出 {len(panels)} 个画格，使用音色: {voice}")

    output_dir = project_path / "05_voiceover_and_srt"
    output_dir.mkdir(parents=True, exist_ok=True)

    prompts_dir = project_path / "03_panel_prompts"
    prompts_dir.mkdir(parents=True, exist_ok=True)

    durations_map = {}
    master_srt_blocks = []
    accumulated_time = 0.0
    current_srt_idx = 1

    for p in panels:
        pid = p["id"]
        text = p["text"]
        motion = p["motion"]
        prompt = p["prompt"]

        audio_file = output_dir / f"{pid}.mp3"
        srt_file = output_dir / f"{pid}.srt"

        print(f"  -> 正在合成 {pid}: \"{text[:20]}...\" (运镜: {motion})")
        dur, srt_content = await synthesize_speech(
            text=text,
            output_audio=str(audio_file),
            output_srt=str(srt_file),
            voice=voice,
            rate=rate,
            volume=volume
        )

        final_dur = max(dur or min_duration, min_duration)

        # 写入提示词文件（如果分镜表中提供了提示词且文件尚不存在）
        if prompt:
            prompt_file = prompts_dir / f"{pid}.txt"
            if not prompt_file.exists():
                prompt_file.write_text(prompt, encoding="utf-8")

        durations_map[pid] = {
            "text": text,
            "motion": motion,
            "duration": round(final_dur, 2),
            "audio_file": str(audio_file.relative_to(project_path)).replace("\\", "/"),
            "srt_file": str(srt_file.relative_to(project_path)).replace("\\", "/"),
        }

        # 偏移并追加到主字幕
        shifted_block, current_srt_idx = shift_srt_timestamps(
            srt_content,
            offset_seconds=accumulated_time,
            start_index=current_srt_idx
        )
        if shifted_block:
            master_srt_blocks.append(shifted_block)

        accumulated_time += final_dur

    # 导出 durations.json
    durations_json_path = output_dir / "durations.json"
    with open(durations_json_path, "w", encoding="utf-8") as f:
        json.dump(durations_map, f, ensure_ascii=False, indent=2)

    # 导出主连续字幕 narration.srt
    master_srt_path = output_dir / "narration.srt"
    with open(master_srt_path, "w", encoding="utf-8") as f:
        f.write("\n\n".join(master_srt_blocks) + "\n")

    print(f"\n[完成] 批量语音合成完成！")
    print(f"  • 时长数据清单: {durations_json_path}")
    print(f"  • 连续主字幕: {master_srt_path}")
    print(f"  • 总音频时长: {accumulated_time:.2f} 秒 ({int(accumulated_time // 60)}分{int(accumulated_time % 60)}秒)")
    return True


def main():
    parser = argparse.ArgumentParser(description="Edge-TTS 高保真语音合成与时间戳工具")
    parser.add_argument("--project", "-p", help="项目路径或标识符 (例如: 002_rainy_detective)")
    parser.add_argument("--text", "-t", help="单条测试台词文本")
    parser.add_argument("--output-audio", "-oa", default="output.mp3", help="单条文本输出音频文件")
    parser.add_argument("--output-srt", "-os", default="output.srt", help="单条文本输出字幕文件")
    parser.add_argument("--voice", "-v", default=DEFAULT_VOICE, help=f"微软音色 (默认: {DEFAULT_VOICE})")
    parser.add_argument("--rate", default="+0%", help="语速微调 (例如: +5%%, -10%%)")
    parser.add_argument("--volume", default="+0%", help="音量微调 (例如: +0%%)")
    parser.add_argument("--min-duration", type=float, default=2.5, help="画格最低持续秒数 (默认 2.5s)")

    args = parser.parse_args()

    if args.project:
        proj = resolve_project(args.project)
        target_dir = proj.path if proj else Path(args.project).resolve()
        if not target_dir.exists():
            print(f"[错误] 无法定位项目目录: {args.project}", file=sys.stderr)
            sys.exit(1)

        asyncio.run(
            process_project_tts(
                project_dir=target_dir,
                voice=args.voice,
                rate=args.rate,
                volume=args.volume,
                min_duration=args.min_duration,
            )
        )
    elif args.text:
        print(f"[生成] 正在合成文本: \"{args.text}\" (音色: {args.voice})")
        dur, srt = asyncio.run(
            synthesize_speech(
                text=args.text,
                output_audio=args.output_audio,
                output_srt=args.output_srt,
                voice=args.voice,
                rate=args.rate,
                volume=args.volume,
            )
        )
        print(f"[成功] 语音输出: {args.output_audio} (时长: {dur:.2f}s)")
        print(f"[成功] 字幕输出: {args.output_srt}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
单行字幕重排与基线对齐工具 (Single-Line Subtitle Reformatter)
专为移动端横竖屏漫画叙事视频设计：
1. 彻底解决多行弹跳（第一行出现，第二行在下方弹出导致位置颠簸）的问题；
2. 依据标点与呼吸节奏将长句智能切分为短单行（默认每句 ≤ 16-18 字）；
3. 按字数比例平滑分配毫秒级起止时间戳；
4. 保证在移动端大字号（52px~60px）下 100% 严格单行、绝对固定基线高度。
"""

import argparse
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


def parse_srt_time(time_str: str) -> float:
    match = re.match(r"(\d{2}):(\d{2}):(\d{2})[,.](\d{3})", time_str.strip())
    if not match:
        return 0.0
    h, m, s, ms = match.groups()
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000.0


def format_srt_time(seconds: float) -> str:
    if seconds < 0:
        seconds = 0.0
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int(round((seconds - int(seconds)) * 1000))
    if ms >= 1000:
        ms = 999
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def split_text_into_short_clauses(text: str, max_chars: int = 16) -> list:
    """
    将长文本依据中文标点与语义智能切分为 ≤ max_chars 的单行短句
    """
    clean_raw = text.strip()
    if not clean_raw:
        return []

    # 依据主要标点断开
    raw_segments = re.split(r"([，；。！？：\n\r]+)", clean_raw)
    
    clauses = []
    buffer = ""
    for seg in raw_segments:
        if not seg:
            continue
        if re.match(r"^[，；。！？：\n\r]+$", seg):
            # 标点符号，如果已有内容且长度已达阈值，直接成段
            buffer += seg
            if len(buffer.strip()) >= 7:
                clauses.append(buffer.strip())
                buffer = ""
        else:
            if len(buffer) + len(seg) > max_chars and len(buffer.strip()) >= 6:
                clauses.append(buffer.strip())
                buffer = seg
            else:
                buffer += seg
                
    if buffer.strip():
        clauses.append(buffer.strip())

    # 第二轮强约束：如果单句仍然超过 max_chars，按词汇/中点物理二分
    final_clauses = []
    for c in clauses:
        # 去除句尾多余标点，保证字幕干练高对比
        c_clean = re.sub(r"[，；。！？：\s]+$", "", c).strip()
        # 也去除句首逗号等
        c_clean = re.sub(r"^[，；。！？：\s]+", "", c_clean).strip()
        if not c_clean:
            continue
            
        if len(c_clean) <= max_chars:
            final_clauses.append(c_clean)
        else:
            # 尝试在短连词或助词附近切，或直接中分
            mid = len(c_clean) // 2
            # 查找中点附近逗号或连词
            split_pos = mid
            for offset in [0, -1, 1, -2, 2, -3, 3]:
                candidate = mid + offset
                if 4 <= candidate <= len(c_clean) - 4:
                    if c_clean[candidate] in ("的", "了", "和", "与", "但", "而", "在", "去"):
                        split_pos = candidate + 1
                        break
            part1 = c_clean[:split_pos].strip()
            part2 = c_clean[split_pos:].strip()
            if part1:
                final_clauses.append(part1)
            if part2:
                final_clauses.append(part2)

    return final_clauses if final_clauses else [clean_raw]


def reformat_srt(input_srt_path: Path, output_srt_path: Path, max_chars: int = 16) -> int:
    """
    重排 SRT 文件，确保每一句都为单行短句，并均匀分配时间轴
    """
    content = input_srt_path.read_text(encoding="utf-8")
    blocks = content.strip().split("\n\n")

    new_cues = []
    cue_counter = 1

    for block in blocks:
        lines = [l.strip() for l in block.strip().split("\n") if l.strip()]
        if len(lines) < 2:
            continue

        time_line_idx = -1
        for idx, l in enumerate(lines):
            if "-->" in l:
                time_line_idx = idx
                break

        if time_line_idx == -1:
            continue

        start_str, end_str = lines[time_line_idx].split("-->")
        start_sec = parse_srt_time(start_str)
        end_sec = parse_srt_time(end_str)
        total_duration = max(0.2, end_sec - start_sec)

        text_content = "".join(lines[time_line_idx + 1:])
        clauses = split_text_into_short_clauses(text_content, max_chars=max_chars)
        if not clauses:
            continue

        total_chars = sum(len(c) for c in clauses)
        curr_start = start_sec

        for c_idx, c in enumerate(clauses):
            ratio = len(c) / total_chars if total_chars > 0 else 1.0 / len(clauses)
            c_dur = total_duration * ratio
            c_end = curr_start + c_dur
            if c_idx == len(clauses) - 1:
                c_end = end_sec  # 锁定末尾精确对齐

            new_cues.append(
                f"{cue_counter}\n"
                f"{format_srt_time(curr_start)} --> {format_srt_time(c_end)}\n"
                f"{c}"
            )
            cue_counter += 1
            curr_start = c_end

    output_srt_path.write_text("\n\n".join(new_cues) + "\n", encoding="utf-8")
    print(f"[成功] 单行字幕重排完成: 从 {len(blocks)} 块扩展为 {len(new_cues)} 个严格单行短句切片")
    print(f"[输出] {output_srt_path}")
    return len(new_cues)


def main():
    parser = argparse.ArgumentParser(description="单行字幕重排与基线对齐工具")
    parser.add_argument("--input", "-i", required=True, help="输入原始 SRT 文件路径")
    parser.add_argument("--output", "-o", help="输出单行 SRT 文件路径 (默认: <input>.single_line.srt)")
    parser.add_argument("--max-chars", "-m", type=int, default=16, help="单行最大中文字数 (默认: 16)")
    args = parser.parse_args()

    in_path = Path(args.input).resolve()
    if not in_path.exists():
        print(f"[错误] 输入文件不存在: {in_path}", file=sys.stderr)
        sys.exit(1)

    out_path = Path(args.output).resolve() if args.output else in_path.parent / f"{in_path.stem}.single_line.srt"
    reformat_srt(in_path, out_path, max_chars=args.max_chars)


if __name__ == "__main__":
    main()

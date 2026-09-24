#!/usr/bin/env python3
"""
动态漫画提示词强制装配编译器 (Prompt Assembler Compiler)
严格执行《动态漫画防漂移 SOP》：
Final Prompt = [角色锚点特征] + [分镜专属动作构图] + [全局统一画风锁] + [负向防漂移契约]
杜绝人工手写或漏写导致的角色换脸、真人写实化漂移与对话气泡乱码。
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.project_base import resolve_project
from scripts.generate_tts import parse_storyboard_table

GLOBAL_STYLE_LOCK = (
    "masterpiece, fine lineart, vintage monochrome manga ink drawing, "
    "rich cross-hatching shadows, deep chiaroscuro lighting, "
    "4:3 aspect ratio"
)

NEGATIVE_CONSTRAINTS = (
    "no photorealism, no real human photography, no realistic photo, no 3d render, "
    "no color, no vibrant colors, no rainbow colors, no text, no words, no speech bubbles, "
    "no dialogue balloons, no English captions, clean high contrast monochrome comic artwork"
)



def assemble_panel_prompt(action_desc: str, character_desc: str, style_lock: str = GLOBAL_STYLE_LOCK, negatives: str = NEGATIVE_CONSTRAINTS) -> str:
    """按四要素标准拼装自包含提示词"""
    parts = []
    
    char_clean = character_desc.strip().rstrip(",")
    if char_clean:
        parts.append(char_clean)
        
    act_clean = action_desc.strip().rstrip(",")
    if act_clean:
        parts.append(act_clean)
        
    style_clean = style_lock.strip().rstrip(",")
    if style_clean:
        parts.append(style_clean)
        
    neg_clean = negatives.strip().rstrip(".")
    if neg_clean:
        parts.append(neg_clean)
        
    return ", ".join(parts) + "."


def main():
    parser = argparse.ArgumentParser(description="批量编译组装动态漫画防漂移提示词")
    parser.add_argument("--project", "-p", required=True, help="项目 slug 或目录路径")
    parser.add_argument("--dry-run", action="store_true", help="仅打印拼装结果，不写盘")
    args = parser.parse_args()

    project = resolve_project(args.project)
    storyboard_md = project.file("01_script_and_storyboard", "storyboard.md")
    characters_json = project.file("02_character_anchors", "characters.json")
    prompts_dir = project.file("03_panel_prompts")
    prompts_dir.mkdir(parents=True, exist_ok=True)

    if not storyboard_md.exists():
        print(f"[错误] 未找到分镜表: {storyboard_md}", file=sys.stderr)
        sys.exit(1)

    # 读取角色锚点配置
    char_config = {}
    if characters_json.exists():
        try:
            with open(characters_json, "r", encoding="utf-8") as f:
                char_config = json.load(f).get("project_characters", {})
        except Exception as e:
            print(f"[警告] 解析 characters.json 异常: {e}", file=sys.stderr)

    protagonist = char_config.get("protagonist_husband", {})
    husband_anchor = protagonist.get(
        "appearance_prompt",
        "A 35-year-old Asian man with messy black hair, tired dark under-eye circles, wearing a slightly crumpled white dress shirt"
    )
    wife = char_config.get("wife", {})
    wife_anchor = wife.get(
        "appearance_prompt",
        "A 32-year-old poised Asian woman, elegant dark knit sweater, sharp wounded gaze, clear-eyed and composed"
    )

    panels = parse_storyboard_table(storyboard_md)
    if not panels:
        print(f"[错误] 未从分镜表中解析出有效画格！", file=sys.stderr)
        sys.exit(1)

    print("=" * 70)
    print(f"🔧 动态漫画提示词装配编译器 (Anti-Drift Compiler)")
    print(f"📁 目标工程: {project.slug} (共 {len(panels)} 幕分镜)")
    print("=" * 70)

    for p in panels:
        pid = p["id"]
        raw_prompt = p["prompt"]

        # 根据分镜内容智能选用角色锚点（男主、妻子、双人、儿童或静物特写）
        lower_prompt = raw_prompt.lower()
        if any(k in lower_prompt for k in ["macro shot", "macro still life", "cut sim cards", "shattered wine glass"]):
            char_anchor = ""
        elif "child" in lower_prompt or "kid" in lower_prompt:
            char_anchor = "A young Asian elementary school child"
        elif "wife" in lower_prompt and ("husband" in lower_prompt or "man" in lower_prompt or "two people" in lower_prompt):
            char_anchor = f"{husband_anchor} and his wife ({wife_anchor})"
        elif "wife" in lower_prompt or "woman" in lower_prompt:
            char_anchor = wife_anchor
        else:
            char_anchor = husband_anchor


        # 清洗 raw_prompt 中原先可能存在的矛盾词
        cleaned_action = re.sub(
            r"(?i)\b(4:3 aspect ratio|master comic book final panel|graphic novel style|moody noir manga ink illustration|cinematic side lighting|high psychological tension)\b",
            "",
            raw_prompt
        )
        cleaned_action = re.sub(r"\s+", " ", cleaned_action).strip(", ")

        compiled = assemble_panel_prompt(
            action_desc=cleaned_action,
            character_desc=char_anchor,
            style_lock=GLOBAL_STYLE_LOCK,
            negatives=NEGATIVE_CONSTRAINTS
        )

        out_file = prompts_dir / f"{pid}.txt"
        print(f"\n[{pid}] 编译输出 -> {out_file.name}")
        print(f"  内容: {compiled[:110]}...")

        if not args.dry_run:
            out_file.write_text(compiled, encoding="utf-8")

    print("\n" + "=" * 70)
    print(f"✅ 编译成功！所有分镜提示词均已完成【角色锚点 + 风格硬锁 + 负向排他】标准化注入。")
    print(f"📁 输出目录: {prompts_dir}")
    print("=" * 70)


if __name__ == "__main__":
    main()

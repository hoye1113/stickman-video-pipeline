#!/usr/bin/env python3
"""
生成漫画角色定妆锚点图 (Character Anchor Generator)
基于 Google Flow (Nano Banana 2, 0 积分)
"""

import argparse
import json
import os
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.project_base import resolve_project
from scripts.auto_flow_generate import bsk_eval, get_flow_image_urls, is_page_thinking, fill_prompt_and_click


def generate_anchor(session_id: str, prompt: str, output_path: Path, max_wait: int = 60) -> bool:
    print(f"🎨 开始生成定妆锚点图...")
    print(f"  提示词: {prompt}")
    
    before_urls = set(get_flow_image_urls(session_id))
    print(f"  当前画板图片数: {len(before_urls)}")
    
    if not fill_prompt_and_click(session_id, prompt):
        print("  [错误] 触发生成失败！")
        return False
        
    print("  已触发生成，正在等待 Nano Banana 2 渲染...")
    time.sleep(3)
    
    start_t = time.time()
    while time.time() - start_t < max_wait:
        thinking = is_page_thinking(session_id)
        current_urls = set(get_flow_image_urls(session_id))
        new_urls = current_urls - before_urls
        
        if new_urls and not thinking:
            img_url = list(new_urls)[0]
            print(f"  🎉 捕获新生成锚点图: {img_url[:80]}...")
            output_path.parent.mkdir(parents=True, exist_ok=True)
            try:
                urllib.request.urlretrieve(img_url, str(output_path))
                print(f"  ✅ 锚点图已保存至: {output_path} ({output_path.stat().st_size} 字节)")
                return True
            except Exception as e:
                print(f"  [错误] 下载图片失败: {e}")
                return False
                
        time.sleep(2)
        print(f"  等待渲染中 ({int(time.time() - start_t)}s)...")
        
    print(f"  [超时] 超过 {max_wait} 秒未获取到新图片")
    return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="生成角色定妆锚点图")
    parser.add_argument("--session", "-s", required=True, help="bsk 会话 ID")
    parser.add_argument("--project", "-p", default="002_infidelity_and_torn_soul", help="项目 slug")
    parser.add_argument("--role", "-r", default="husband", help="角色名 (husband / wife)")
    parser.add_argument("--color", action="store_true", help="生成现代全彩条漫/Webtoon风格定妆图")
    args = parser.parse_args()
    
    project = resolve_project(args.project)
    out_dir = project.file("02_character_anchors")
    
    if args.role == "husband":
        if args.color:
            prompt = (
                "A 35-year-old Asian man, weary exhausted expression, messy natural black parted hair, "
                "prominent dark under-eye circles, wearing a slightly crumpled white dress shirt under an open charcoal navy overcoat, "
                "front view, masterpiece, clean crisp lineart, modern color webtoon comic style, rich cinematic color palette, "
                "dramatic moody chiaroscuro lighting, emotional warm and cool tones, solid soft background, "
                "no photorealism, no real human photography, no 3d render, no monochrome, no black and white, no text, "
                "no words, no speech bubbles, no dialogue balloons, 4:3 aspect ratio"
            )
            out_file = out_dir / "husband_color_anchor.png"
        else:
            prompt = (
                "A 35-year-old Asian man, weary exhausted expression, messy natural black parted hair, "
                "prominent dark under-eye circles, dressed in a slightly crumpled white dress shirt under an open charcoal coat, "
                "front view, masterpiece, fine lineart, vintage monochrome manga ink drawing, rich cross-hatching shadows, "
                "deep chiaroscuro lighting, solid white background, "
                "no photorealism, no real human photography, no 3d render, no color, no vibrant colors, no text, "
                "no words, no speech bubbles, no dialogue balloons, 4:3 aspect ratio"
            )
            out_file = out_dir / "husband_anchor.png"
    elif args.role == "wife":
        if args.color:
            prompt = (
                "A 32-year-old poised Asian woman, sharp wounded resolute gaze, shoulder-length straight black hair, "
                "wearing an elegant burgundy dark knit sweater, front view, "
                "masterpiece, clean crisp lineart, modern color webtoon comic style, rich cinematic color palette, "
                "dramatic moody chiaroscuro lighting, emotional warm and cool tones, solid soft background, "
                "no photorealism, no real human photography, no 3d render, no monochrome, no black and white, no text, "
                "no words, no speech bubbles, no dialogue balloons, 4:3 aspect ratio"
            )
            out_file = out_dir / "wife_color_anchor.png"
        else:
            prompt = (
                "A 32-year-old poised Asian woman, sharp wounded resolute gaze, shoulder-length straight black hair, "
                "wearing an elegant dark knit sweater, front view, "
                "masterpiece, fine lineart, vintage monochrome manga ink drawing, rich cross-hatching shadows, "
                "deep chiaroscuro lighting, solid white background, "
                "no photorealism, no real human photography, no 3d render, no color, no vibrant colors, no text, "
                "no words, no speech bubbles, no dialogue balloons, 4:3 aspect ratio"
            )
            out_file = out_dir / "wife_anchor.png"
    else:
        print(f"未知角色: {args.role}")
        sys.exit(1)
        
    success = generate_anchor(args.session, prompt, out_file)
    if not success:
        sys.exit(1)

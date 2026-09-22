#!/usr/bin/env python3
"""
一键脚手架：基于 presets/<genre>/template 或 projects/_template/ 初始化新视频项目
支持多题材 (stickman, comic_story 等)
"""

import sys
import argparse
from project_store import ProjectError, create_project, list_presets, DEFAULT_GENRE

if __name__ == "__main__":
    presets = list_presets()
    parser = argparse.ArgumentParser(description="Initialize a new video project from genre preset template")
    parser.add_argument("name", help="Project slug/directory name, e.g. 002_comic_mystery or 003_social_anxiety")
    parser.add_argument("--genre", "-g", default=DEFAULT_GENRE, choices=presets,
                        help=f"Genre preset to use (default: {DEFAULT_GENRE}, available: {', '.join(presets)})")
    parser.add_argument("--title-zh", default="未命名主题", help="Chinese title")
    parser.add_argument("--title-en", default="Untitled Project", help="English title")
    parser.add_argument("--ratio", default="4:3", choices=["4:3", "16:9", "9:16", "1:1"], help="Aspect ratio")
    parser.add_argument("--style", default=None,
                        help="Visual style (defaults: stickman -> 'Style 2B (Cinematic Story)', comic_story -> 'Manga Ink & Watercolor')")
    parser.add_argument("--source", default="", help="Path to source material file")

    args = parser.parse_args()

    try:
        project = create_project(
            args.name,
            genre=args.genre,
            title_zh=args.title_zh,
            title_en=args.title_en,
            ratio=args.ratio,
            style=args.style,
            source=args.source
        )
    except ProjectError as e:
        print(f"[错误] {e}")
        sys.exit(1)

    print(f"Created project folder: {project.dir}")
    print(f"Genre preset: {project.genre}")
    print(f"Initialized project metadata at {project.meta_path}")
    print(f"Project '{project.slug}' is ready for content production!")

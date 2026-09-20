#!/usr/bin/env python3
"""
一键脚手架：基于 projects/_template/ 初始化新视频项目
"""

import sys
import argparse
from project_store import ProjectError, create_project

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Initialize a new stickman video project from template")
    parser.add_argument("name", help="Project slug/directory name, e.g. 002_social_anxiety")
    parser.add_argument("--title-zh", default="未命名主题", help="Chinese title")
    parser.add_argument("--title-en", default="Untitled Project", help="English title")
    parser.add_argument("--ratio", default="4:3", choices=["4:3", "16:9", "9:16", "1:1"], help="Aspect ratio")
    parser.add_argument("--style", default="Style 2B (Cinematic Story)", help="Visual style")
    parser.add_argument("--source", default="", help="Path to source material file")

    args = parser.parse_args()

    try:
        project = create_project(args.name, args.title_zh, args.title_en, args.ratio, args.style, args.source)
    except ProjectError as e:
        print(f"[错误] {e}")
        sys.exit(1)

    print(f"Created project folder: {project.dir}")
    print(f"Initialized project metadata at {project.meta_path}")
    print(f"Project '{project.slug}' is ready for content production!")

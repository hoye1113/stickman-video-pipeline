#!/usr/bin/env python3
"""
拆分指定项目的 prompts_all.md 为独立提示词文件 (prompt_XX.txt)
"""

import sys
import argparse
from project_store import ProjectError, resolve_project


def split_prompts(project):
    md_path = project.file("03_gemini_prompts", "prompts_all.md")
    out_dir = project.file("03_gemini_prompts", "clips")
    out_dir.mkdir(parents=True, exist_ok=True)

    if not md_path.is_file():
        print(f"Error: {md_path} not found.")
        return 0

    with open(md_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    current_clip = None
    current_content = []
    in_code = False
    count = 0

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("## Clip "):
            parts = stripped.split()
            if len(parts) >= 3:
                current_clip = parts[2]
                current_content = []
        elif stripped == "```text":
            in_code = True
            current_content = []
        elif stripped == "```" and in_code:
            in_code = False
            if current_clip:
                out_path = out_dir / f"prompt_{current_clip}.txt"
                with open(out_path, "w", encoding="utf-8") as out_f:
                    out_f.write("".join(current_content).strip())
                print(f"Wrote {out_path}")
                count += 1
                current_clip = None
        elif in_code:
            current_content.append(line)

    print(f"Total prompt files created in {project.dir}: {count}")
    return count


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split prompts_all.md into individual clips")
    parser.add_argument("--project", "-p", default=None, help="Target project directory name")
    args = parser.parse_args()

    try:
        project = resolve_project(args.project)
    except ProjectError as e:
        print(f"[错误] {e}")
        sys.exit(1)

    print(f"[提示] 目标项目：{project.slug}")
    split_prompts(project)

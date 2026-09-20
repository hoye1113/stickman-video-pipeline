#!/usr/bin/env python3
"""
多项目矩阵统一存取模块
集中负责 projects/ 下的项目解析、meta.json 读写与各阶段路径推导，
所有脚本一律通过本模块定位项目，禁止自行猜测或回落到固定项目。
"""

import json
import shutil
from datetime import datetime
from pathlib import Path

EXCLUDED_PREFIX = "_"
TEMPLATE_NAME = "_template"


class ProjectError(Exception):
    pass


def repo_root():
    return Path(__file__).resolve().parent.parent


def projects_dir(root=None):
    return Path(root or repo_root()) / "projects"


def list_projects(root=None):
    base = projects_dir(root)
    if not base.is_dir():
        return []
    return sorted(
        d.name for d in base.iterdir()
        if d.is_dir() and not d.name.startswith(EXCLUDED_PREFIX)
    )


class Project:
    def __init__(self, path):
        self.dir = Path(path).resolve()
        self.slug = self.dir.name
        self.meta_path = self.dir / "meta.json"
        self.meta = self._load_meta()

    def _load_meta(self):
        if not self.meta_path.is_file():
            return {}
        try:
            with open(self.meta_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            raise ProjectError(f"meta.json 解析失败：{self.meta_path} ({e})")

    def save_meta(self):
        self.meta_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.meta_path, "w", encoding="utf-8") as f:
            json.dump(self.meta, f, ensure_ascii=False, indent=2)

    def file(self, stage, *parts):
        return self.dir.joinpath(stage, *parts)

    @property
    def total_clips(self):
        total = self.meta.get("total_clips")
        return total if isinstance(total, int) and total > 0 else None

    def clips(self):
        clips_dir = self.file("04_raw_clips")
        if not clips_dir.is_dir():
            return []

        def sort_key(p):
            num = p.stem.replace("clip_", "")
            return int(num) if num.isdigit() else 10 ** 9

        return sorted(clips_dir.glob("clip_*.mp4"), key=sort_key)

    def clip_indices(self):
        indices = []
        for p in self.clips():
            num = p.stem.replace("clip_", "")
            if num.isdigit():
                indices.append(int(num))
        return sorted(indices)

    def missing_clip_indices(self):
        if not self.total_clips:
            return []
        found = set(self.clip_indices())
        return [i for i in range(1, self.total_clips + 1) if i not in found]

    def record_clip(self, index):
        generated = self.meta.setdefault("clips_generated", [])
        if index not in generated:
            generated.append(index)
            generated.sort()
        self.meta["project_id"] = self.meta.get("project_id", self.slug)
        self.save_meta()

    def summary(self):
        total = self.total_clips or "?"
        title = self.meta.get("title_zh") or self.meta.get("title_en") or ""
        status = self.meta.get("status", "unknown")
        return f"[{self.slug}] {title} | clips {len(self.clips())}/{total} | status: {status}"


def resolve_project(slug=None, root=None):
    """
    解析目标项目。
    - slug 可为目标目录名（projects/ 下）、相对路径或绝对路径；
    - slug 为空时，唯一项目自动选中；无项目或多项目则报错并列出候选。
    """
    root = Path(root) if root else repo_root()

    if slug:
        base = projects_dir(root)
        target = base / slug
        if target.is_dir():
            return Project(target)
        candidate = Path(slug)
        if candidate.is_dir():
            return Project(candidate)
        available = list_projects(root)
        hint = "、".join(available) if available else "（暂无项目）"
        raise ProjectError(f"未找到项目 '{slug}'。可用项目：{hint}")

    available = list_projects(root)
    if not available:
        raise ProjectError("未找到任何项目，请先运行 new_project.py 创建新项目。")
    if len(available) > 1:
        raise ProjectError("存在多个项目，必须用 --project 显式指定。可用项目：" + "、".join(available))
    return Project(projects_dir(root) / available[0])


def create_project(slug, title_zh="未命名主题", title_en="Untitled Project",
                   ratio="9:16", style="Style 1 Dark", source="", root=None):
    root = Path(root) if root else repo_root()
    if not slug or any(sep in slug for sep in ("/", "\\")):
        raise ProjectError(f"非法项目名：{slug}")
    if slug.startswith(EXCLUDED_PREFIX):
        raise ProjectError(f"项目名不能以下划线开头：{slug}")

    target = projects_dir(root) / slug
    if target.exists():
        raise ProjectError(f"项目已存在：{target}")

    template = projects_dir(root) / TEMPLATE_NAME
    if not template.is_dir():
        raise ProjectError(f"模板目录不存在：{template}")

    shutil.copytree(template, target)
    project = Project(target)
    project.meta.update({
        "project_id": slug,
        "title_zh": title_zh,
        "title_en": title_en,
        "aspect_ratio": ratio,
        "style": style,
        "clips_generated": [],
        "status": "initialized",
        "created_at": datetime.now().isoformat(),
        "source_file": source,
    })
    project.save_meta()
    return project

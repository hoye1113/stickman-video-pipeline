#!/usr/bin/env python3
"""
多题材统一项目工程基类 (Core Base)
负责：
1. 项目定位与生命周期元数据 (meta.json) 读写
2. 跨题材套件解析 (presets: stickman, comic_story)
3. 向后兼容现有 projects/ 目录结构
"""

import json
import shutil
from datetime import datetime
from pathlib import Path

EXCLUDED_PREFIX = "_"
LEGACY_TEMPLATE_NAME = "_template"
DEFAULT_GENRE = "stickman"


class ProjectError(Exception):
    pass


def repo_root():
    """获取代码仓库根目录 (core/ 上级目录)"""
    return Path(__file__).resolve().parent.parent


def projects_dir(root=None):
    """获取所有实际项目的存储根目录 projects/"""
    return Path(root or repo_root()) / "projects"


def presets_dir(root=None):
    """获取所有题材套件的存储根目录 presets/"""
    return Path(root or repo_root()) / "presets"


def list_presets(root=None):
    """列出当前支持的所有题材套件"""
    base = presets_dir(root)
    if not base.is_dir():
        return [DEFAULT_GENRE]
    presets = [
        d.name for d in base.iterdir()
        if d.is_dir() and not d.name.startswith(EXCLUDED_PREFIX)
    ]
    return sorted(presets) if presets else [DEFAULT_GENRE]


def list_projects(root=None):
    """列出 projects/ 下的所有有效项目"""
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
    def path(self):
        """兼容性路径别名"""
        return self.dir

    @property
    def genre(self):
        """当前项目的题材分类 (默认为 stickman)"""
        return self.meta.get("genre", DEFAULT_GENRE)

    @property
    def total_clips(self):
        total = self.meta.get("total_clips")
        return total if isinstance(total, int) and total > 0 else None

    @property
    def total_panels(self):
        total = self.meta.get("total_panels")
        return total if isinstance(total, int) and total > 0 else None

    def clips(self):
        clips_dir = self.file("04_raw_clips")
        if not clips_dir.is_dir():
            return []

        def sort_key(p):
            num = p.stem.replace("clip_", "")
            return int(num) if num.isdigit() else 10 ** 9

        return sorted(clips_dir.glob("clip_*.mp4"), key=sort_key)

    def panels(self):
        panels_dir = self.file("04_raw_panels")
        if not panels_dir.is_dir():
            return []

        def sort_key(p):
            num = p.stem.replace("panel_", "")
            return int(num) if num.isdigit() else 10 ** 9

        extensions = ("*.png", "*.jpg", "*.jpeg", "*.webp")
        found = []
        for ext in extensions:
            found.extend(panels_dir.glob(ext))
        return sorted(found, key=sort_key)

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

    def record_panel(self, index):
        generated = self.meta.setdefault("panels_generated", [])
        if index not in generated:
            generated.append(index)
            generated.sort()
        self.meta["project_id"] = self.meta.get("project_id", self.slug)
        self.save_meta()

    def summary(self):
        title = self.meta.get("title_zh") or self.meta.get("title_en") or ""
        status = self.meta.get("status", "unknown")
        genre = self.genre
        if genre == "stickman":
            total = self.total_clips or "?"
            count_str = f"clips {len(self.clips())}/{total}"
        elif genre == "comic_story":
            total = self.total_panels or "?"
            count_str = f"panels {len(self.panels())}/{total}"
        else:
            count_str = f"status: {status}"
        return f"[{self.slug}] ({genre}) {title} | {count_str} | status: {status}"


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


def locate_template(genre=DEFAULT_GENRE, root=None):
    """
    定位指定题材的骨架模板。
    优先级：
    1. presets/{genre}/template
    2. 若 genre 为 stickman，向后兼容允许 fallback 到 projects/_template
    3. 其他非法或未知 genre 直接报错，禁止静默回退
    """
    root = Path(root) if root else repo_root()
    preset_template = presets_dir(root) / genre / "template"
    if preset_template.is_dir():
        return preset_template

    if genre == DEFAULT_GENRE:
        legacy_template = projects_dir(root) / LEGACY_TEMPLATE_NAME
        if legacy_template.is_dir():
            return legacy_template

    available = ", ".join(list_presets(root))
    raise ProjectError(f"未找到题材 '{genre}' 的模板目录。可用题材：{available}")


def create_project(slug, genre=DEFAULT_GENRE, title_zh="未命名主题", title_en="Untitled Project",
                   ratio="4:3", style=None, source="", root=None):
    """
    根据指定题材 (genre) 创建新项目并初始化元数据。
    """
    root = Path(root) if root else repo_root()
    if not slug or any(sep in slug for sep in ("/", "\\")):
        raise ProjectError(f"非法项目名：{slug}")
    if slug.startswith(EXCLUDED_PREFIX):
        raise ProjectError(f"项目名不能以下划线开头：{slug}")

    target = projects_dir(root) / slug
    if target.exists():
        raise ProjectError(f"项目已存在：{target}")

    template_dir = locate_template(genre, root=root)

    shutil.copytree(template_dir, target)
    project = Project(target)

    # 默认风格适配
    actual_style = style
    if not actual_style:
        if genre == "stickman":
            actual_style = "Style 2B (Cinematic Story)"
        elif genre == "comic_story":
            actual_style = "Manga Ink & Watercolor"
        else:
            actual_style = "Default"

    project.meta.update({
        "project_id": slug,
        "genre": genre,
        "title_zh": title_zh,
        "title_en": title_en,
        "aspect_ratio": ratio,
        "style": actual_style,
        "status": "initialized",
        "created_at": datetime.now().isoformat(),
        "source_file": source,
    })
    project.save_meta()
    return project

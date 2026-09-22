#!/usr/bin/env python3
"""
多项目矩阵统一存取门面模块 (Facade)
向后兼容：所有旧脚本 from project_store import ... 继续保持 100% 兼容工作，
底层逻辑统一委托至 core.project_base。
"""

import sys
from pathlib import Path

# 确保能定位并导入 core 模块
_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from core.project_base import (
    ProjectError,
    Project,
    repo_root,
    projects_dir,
    presets_dir,
    list_presets,
    list_projects,
    resolve_project,
    locate_template,
    create_project,
    EXCLUDED_PREFIX,
    DEFAULT_GENRE,
)

__all__ = [
    "ProjectError",
    "Project",
    "repo_root",
    "projects_dir",
    "presets_dir",
    "list_presets",
    "list_projects",
    "resolve_project",
    "locate_template",
    "create_project",
    "EXCLUDED_PREFIX",
    "DEFAULT_GENRE",
]

# 调研与提案管理规范 (Research & Proposals Governance)

本目录（`docs/research/`）用于集中管理所有**外部对标调研、平台机制探索、行业优秀开源案例拆解**，以及**新题材/新项目的创意策划方案（RFC / Proposals）**。

---

## 一、目录结构与职责划分

```text
docs/research/
├── README.md                      # 本管理规范
├── benchmarks/                    # 【外部对标与市场调研】
│   └── 2026-09-crazykaomei_short_video_playbook.md
│                                  # 行业对标账号、爆款拆解、开源项目评测、平台风控机制探索
└── proposals/                     # 【创意策划与新题材提案】
    ├── proposal_template.md       # 标准创意提案模板
    └── ...                        # 具体项目立项预案、题材试验 RFC、分镜新构架提案
```

### 1. `benchmarks/`（外部对标与方法论调研）
- **核心定位**：输入端。沉淀行业优秀实践、技术评测与爆款方法论。
- **收录范围**：
  - 优秀创作者/团队（如 `@CrazyKaomei`、Lucas Patiri、DeRonin 等）的生产流与爆款框架；
  - 核心开源工具与开源 Skill 评测（如 Remotion 故事流、分镜生成工具、TTS 工具链）；
  - 平台机制探索（Google Flow 隐藏特性、Veo 表现、Gemini Omni 边界、各社媒平台审核风控）；
  - 视觉艺术风格与提示词工程新发现。
- **命名规范**：`YYYY-MM-<source_or_topic>.md`（如 `2026-09-crazykaomei_short_video_playbook.md`）。

### 2. `proposals/`（策划方案与题材 RFC）
- **核心定位**：输出与孵化端。在正式启动 `projects/<slug>` 制作前，用于论证和细化创意设想。
- **收录范围**：
  - 新题材/新风格的技术可行性与生产流设计（如动态漫画故事流、科普 PPT 图文流、手绘讲解流）；
  - 重点项目的剧本大纲创意预案（在落盘到特定项目前的草案）；
  - 自动化脚本改造与工程架构升级提案（Pipeline RFC）。
- **命名规范**：`proposal_<编号>_<主题简写>.md`（如 `proposal_002_comic_story_pipeline.md`）。

---

## 二、生命周期流转机制 (Lifecycle)

从“外部灵感”到“最终成品”的标准推进闭环：

```text
┌──────────────────────┐
│ 1. 外部探索与对标调研 │ ──▶ 沉淀到 docs/research/benchmarks/
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ 2. 内部策划提案 (RFC) │ ──▶ 撰写到 docs/research/proposals/ (基于 proposal_template.md)
└──────────┬───────────┘
           │ 人类用户确认批准 / 方案定稿
           ▼
┌──────────────────────┐
│ 3. 题材套件内化建设  │ ──▶ 沉淀到 presets/<genre>/ 与 skills/
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ 4. 矩阵项目正式落地  │ ──▶ 运行 scripts/new_project.py <slug> --genre <genre>
└──────────────────────┘
```

---

## 三、协作守则 (Rules for AI Agents & Engineers)

1. **先调研/提案，后动工程**：涉及新题材、大画风调整或新工作流引入时，必须先在 `benchmarks/` 或 `proposals/` 沉淀文档，并经用户评审，严禁未经讨论直接改动生成脚本或破坏现有项目目录。
2. **注明出处与时效性**：外部调研文档必须标明信息来源（作者、Twitter/X 链接、GitHub 仓库、发布日期）。
3. **保护资产与零成本纪律**：任何调研与技术探索不得违背“零边际成本”与“零视频积分浪费”原则，严禁调用收费 API 进行试验。

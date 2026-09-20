# 🎬 3-Minute Stickman Video Generation Pipeline (火柴人科普视频自动化流水线)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Model](https://img.shields.io/badge/Model-Gemini%20Omni%201.1%20Flash-orange.svg)](https://aistudio.google.com/)
[![Video Automation](https://img.shields.io/badge/Pipeline-Browser%20Skill%20%2B%20FFmpeg-green.svg)](#)

这是一个面向 AI 智能体（Agent）的**3分钟火柴人短视频矩阵化端到端生产工作流**。项目完全自包含，内化了严谨的资料检索、导演级分镜契约、Google AI Studio 原生视频生成接管与后期音视频字幕硬编码压制能力。支持多主题、多视频项目物理隔离，永久杜绝素材覆盖。

---

## 🌟 核心特性 (Key Features)

1. **多主题矩阵架构 (Multi-Project Architecture)**：
   - 彻底告别单任务硬编码，采用 `projects/<slug>/` 项目隔离机制。每个视频项目独立拥有 `01_` 到 `06_` 阶段资产与 `meta.json`，多主题并行制作互不干扰。
2. **三幕式高密度分镜编排 (18 Clips / 3 Minutes)**：
   - 突破传统单分钟短视频限制，按三幕式结构（痛点共鸣 → 脑科学机制解构 → 认知重塑与微行动解脱）编排 18 个 10 秒片段。
   - 每段锁定 `[0–3s]`、`[3–7s]`、`[7–10s]` 三个动效节拍，每 2–3 秒产生视觉推进，确保镜头永不冷场。
3. **防形变与角色基因锁定 (Character DNA Lock)**：
   - 彻底解决 AI 视频模型中角色换装、变脸、外星人瞳孔畸变（Bug-eye）等常见痛点，严格约束角色设计与负面提示词。
4. **纯视觉零乱码契约 (Zero-Text Contract)**：
   - 视频生成阶段严禁在画面中出现任何文字或对话框，所有图标、时钟、通知完全图形化，台词 100% 由后期 FFmpeg 烧录，彻底杜绝 AI 乱码。
5. **Google AI Studio 原生接管 (Gemini Omni 1.1 Flash)**：
   - 针对 Google 最新的视频专属生成模型 `gemini-omni-1.1-flash` 进行深度适配，原生支持 10 秒时长控制、16:9/9:16 画幅与 24fps 帧率。
   - Agent 依托宿主机已登录会话，直接在网页前端调用执行，零 API 账单成本。
6. **无感提取与自动化脚本引擎**：
   - 突破传统浏览器下载弹窗死锁，通过 JavaScript 直接将 Blob 视频读取为 Base64 写盘，秒级存储。

---

## 📂 项目结构 (Directory Structure)

```text
stickman-videos/
├── .gitignore                     # Git 忽略配置（严格跨项目忽略大体积 MP4 二进制文件）
├── README.md                      # 项目说明文档
├── AGENT.md                       # Agent 自动化接手与操作总纲
├── docs/
│   ├── agent_notes.md             # 历史交接备忘录
│   └── workflow_spec.md           # 完整工作流规范与 Skill 契约说明
├── projects/                      # 视频项目矩阵目录
│   ├── _template/                 # 新建工程模板（包含标准 .gitkeep 与结构）
│   ├── 001_betrayal_and_split_soul/ # 第1期：背叛与撕裂
│   │   ├── 01_research/           # 阶段 1：科学事实检索成果归档
│   │   ├── 02_director_proposal/  # 阶段 2：Phase A 导演预案（中英台词、18 段分镜表）
│   │   ├── 03_gemini_prompts/     # 阶段 3：Phase B 生产提示词（18 条独立 Prompt）
│   │   ├── 04_raw_clips/          # 阶段 4：从 AI Studio 生成收录的 18 段原始视频 (Git忽略)
│   │   ├── 05_subtitles/          # 阶段 5：时间轴对齐的双语字幕文件 (.srt)
│   │   ├── 06_final_video/        # 阶段 6：最终 3 分钟高清成片 (Git忽略)
│   │   └── meta.json              # 项目元数据与生成进度追踪
│   └── 002_xxx/                   # 第2期及未来新主题项目
├── skills/                        # 项目内置核心技能库
│   ├── directing-stickman-videos/ # 火柴人导演分镜与 Omni Flash 提示词契约
│   ├── embed-subtitles/           # FFmpeg 字幕烧录与 RTL 自动修复规则
│   └── yichen-unified-search/     # 离线路由、事实核验与候选检索系统
└── scripts/                       # 参数化音视频后期处理自动化脚本
    ├── project_store.py           # 【核心模块】项目解析、meta.json 读写与路径统一
    ├── new_project.py             # 一键脚手架新建项目
    ├── split_prompts.py           # 拆分指定项目的提示词文件
    ├── download_clip.py           # Base64 直提浏览器当前生成的 Blob 视频
    ├── concat_clips.py            # FFmpeg 批量视频无缝拼接
    └── embed_subtitles.py         # FFmpeg 高清双语字幕烧录
```

---

## 🚀 快速上手 (Quick Start)

> 当 `projects/` 下存在多个项目时，除 `new_project.py` 外的所有脚本必须显式传 `--project <slug>`，否则脚本会报错并列出候选项目；项目唯一时可省略。

### 1. 一键创建新视频主题
```powershell
python scripts/new_project.py 002_social_anxiety --title-zh "克服社交焦虑" --title-en "Mastering Social Anxiety" --ratio 9:16
```

### 2. 准备分镜与生成提示词
在目标项目的 `03_gemini_prompts/prompts_all.md` 编写好 18 段提示词后，一键拆分：
```powershell
python scripts/split_prompts.py --project 002_social_anxiety
```

### 3. 生成与提取视频片段
通过 `bsk` 控制 Google AI Studio 生成后，一键提取视频至目标项目：
```powershell
python scripts/download_clip.py --session <session_id> --filename clip_01.mp4 --project 002_social_anxiety
```

### 4. 视频拼接与字幕压制
```powershell
# 18 段视频无缝拼接
python scripts/concat_clips.py --project 002_social_anxiety

# 烧录双语字幕成片
python scripts/embed_subtitles.py --project 002_social_anxiety
```

---

## 📄 许可证 (License)

[MIT License](LICENSE)

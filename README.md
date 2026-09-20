# 🎬 3-Minute Stickman Video Generation Pipeline (火柴人科普视频自动化流水线)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Google%20Flow-4285F4.svg)](https://labs.google/fx/tools/flow)
[![Video Automation](https://img.shields.io/badge/Pipeline-Browser%20Automation%20%2B%20FFmpeg-green.svg)](#)

这是一个面向 AI 智能体（Agent）与创作者的**3分钟火柴人短视频矩阵化全自动生产流水线**。

---

## 💡 为什么存在？(Philosophy & Why This Exists)

本项目源自推友 **“疯狂的烤妹儿 🩵”**（`@CrazyKaomei`）提出的 **“一人可落地的「AI + 自媒体」最小阻力路径”**：
- **痛点**：传统 AIGC 视频制作成本高昂（Midjourney、Runway、Kling 每月大几百），高心理门槛与金钱试错成本常常在计较中磨灭创作灵感；
- **破局**：依托极低成本的 Google One AI Premium PRO 会员（如 18 个月活动），利用官方每月 1,000 点额度打通**零边际成本的视频生产通道**；
- **核心认知**：
  > **“你占到了一个入口，不等于你拥有了作品。用不起来的便宜，依然是昂贵的浪费。别把会员当主角，它只是一声开门声。真正要做的是打磨出一套属于你自己的内容生产闭环。”**
- **使命**：将便宜的会员算力入口，通过 **浏览器自动化 + 工业级提示词契约 + 多项目矩阵管理 + 物理级平滑过渡**，沉淀为一套可全自动交付的自媒体内容飞轮。

---

## 🌟 核心特性 (Key Features)

1. **Google Flow 原生工业化流水线 (Storyboard Studio)**：
   - **Storyboard Studio**：原生分镜卡片流，完美契合三幕式 18 个镜头，每张卡片独立渲染，彻底根绝单会话累加超限崩溃；
   - **首尾帧连续性控制 (First & Last Frame Control)**：支持上一段尾帧作为下一段起始帧，实现模型级物理衔接，消灭画面突变；
   - **Nano Banana 2 零积分生图 (0 Credits)**：先用 0 积分无限生成 4 张关键帧测角色一致性，定稿后再以 15 积分渲染 10s 视频；
   - **合规消费级额度**：消耗官方每月 1,000 Pro 点数，告别开发者接口 403 封禁风险。
2. **多主题矩阵架构 (Multi-Project Architecture)**：
   - 彻底告别单任务硬编码，采用 `projects/<slug>/` 目录物理隔离。每个视频主题独立拥有 `01_` 到 `06_` 阶段资产与 `meta.json`，多主题并行制作杜绝素材覆盖。
3. **严格安全风控与隐喻替换 (Prompt Safety Policy)**：
   - 内置 [`docs/prompt_safety_policy.md`](docs/prompt_safety_policy.md)。针对勒颈、注射、危险坠落等平台敏感词进行隐喻转译（如红丝带缠绕肩部、光束接触注入能量、白色警戒线），改写版本沉淀至 `clips_safe/`，确保 100% 零拒签。
4. **三幕式高密度分镜编排 (18 Clips / 3 Minutes)**：
   - 痛点共鸣 (Clips 1–6) → 机制解构 (Clips 7–12) → 认知重塑与微行动 (Clips 13–18)。每段锁定 `[0–3s]`、`[3–7s]`、`[7–10s]` 节拍，镜头永不冷场。
5. **纯视觉零乱码契约 (Zero-Text Contract)**：
   - 视频生成阶段严禁在画面中出现任何文字或对话框，所有台词 100% 由后期 FFmpeg 压制烧录，彻底根绝 AI 乱码。
6. **无感提取与自动化脚本引擎**：
   - 突破传统浏览器下载弹窗死锁，通过 JavaScript DOM 注入直接将 `<video>` 的 Blob / 签名链接转为 Base64 写盘，秒级落盘并自动同步进度。

---

## 📂 项目结构 (Directory Structure)

```text
stickman-videos/
├── .gitignore                     # Git 忽略配置（严格跨项目忽略大体积 MP4 二进制文件）
├── README.md                      # 本说明文档
├── AGENT.md                       # Agent 自动化接手与操作总纲
├── docs/
│   ├── prompt_safety_policy.md    # 提示词安全风控手册与替换对照表
│   ├── workflow_spec.md           # 完整工作流规范与 Skill 契约说明
│   ├── lessons_learned.md         # ★ 跨项目经验教训总纲（配额/bsk/水印/字幕/备份）
│   └── agent_notes.md             # 历史交接备忘录
├── projects/                      # 视频项目矩阵目录
│   ├── _template/                 # 新建工程模板（包含标准 .gitkeep 与结构）
│   ├── 001_betrayal_and_split_soul/ # 第1期：背叛与撕裂
│   │   ├── 01_research/           # 阶段 1：科学事实检索成果归档
│   │   ├── 02_director_proposal/  # 阶段 2：Phase A 导演预案（分镜表）
│   │   ├── 03_gemini_prompts/     # 阶段 3：Phase B 提示词 (clips_safe/ 18镜4:3全集, _legacy_*)
│   │   ├── 04_raw_clips/          # 阶段 4：生成收录的 18 段原始视频 (Git忽略)
│   │   ├── 05_subtitles/          # 阶段 5：时间轴对齐的双语字幕文件 (narration.bilingual.srt)
│   │   ├── 06_final_video/        # 阶段 6：最终 3 分钟高清成片 (Git忽略)
│   │   └── meta.json              # 项目元数据与生成进度追踪
│   └── 002_xxx/                   # 第2期及未来新主题项目
├── skills/                        # 项目内置核心技能库
│   ├── directing-stickman-videos/ # 火柴人导演分镜与提示词契约
│   ├── embed-subtitles/           # FFmpeg 字幕烧录与 RTL 自动修复规则
│   └── yichen-unified-search/     # 离线路由、事实核验与候选检索系统
└── scripts/                       # 参数化音视频自动化脚本
    ├── project_store.py           # 项目解析、meta.json 读写与路径统一
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
python scripts/new_project.py 002_social_anxiety --title-zh "克服社交焦虑" --title-en "Mastering Social Anxiety" --ratio 4:3 --style "Style 2B (Cinematic Story)"
```

### 2. 准备分镜、生成提示词并做安全审查
1. 在 `projects/<slug>/02_director_proposal/proposal_phase_a.md` 编写 18 段分镜预案，**等待用户审核批准**；
2. 编写 `03_gemini_prompts/prompts_all.md`，执行安全词检查与改写；
3. 一键拆分：
   ```powershell
   python scripts/split_prompts.py --project 002_social_anxiety --md prompts_all.md --out-dir clips_safe
   ```

### 3. 生成与提取视频片段 (Google Flow)
在 Google Flow (Storyboard Studio) 中生成视频后，运行无感 Base64 提取脚本：
```powershell
python scripts/download_clip.py --session <session_id> --filename clip_01.mp4 --project 002_social_anxiety
```

### 4. 视频拼接与字幕压制
```powershell
# 18 段视频无缝拼接 (生成 stitched_raw.mp4，支持 4:3 居中裁切)
python scripts/concat_clips.py --project 002_social_anxiety --crop-ratio 4:3

# 自动探测画幅并压制双语字幕 (生成 final_subtitled.mp4)
python scripts/embed_subtitles.py --project 002_social_anxiety
```

---

## 📄 许可证 (License)

[MIT License](LICENSE)

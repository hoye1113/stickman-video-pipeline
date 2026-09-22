# 动态漫画故事题材套件 (Motion Comic Preset)

## 1. 题材定位与核心特征
* **题材代号**：`comic_story`
* **适用场景**：悬疑推理、都市传说、历史人物志、热血叙事、情感物语短剧。
* **用户体验**：“看了一场生动的漫画，听了一场引人入胜的故事”。
* **核心优势**：
  - **角色一致、画风稳定**：依赖 AI 生图而非视频抽卡，人物绝不畸变或漂移。
  - **极速低耗**：不需要消耗昂贵的视频大模型算力积分，由本地代码引擎全自动赋予运镜动效。
  - **声音驱动节奏**：每格停留时长严格匹配故事台词语音时长，叙事节奏自然天成。

## 2. 标准工程目录结构 (7 阶段)
```text
<project_name>/
├── meta.json                         # 元数据 (genre: "comic_story", aspect_ratio: "4:3")
├── 01_script_and_storyboard/         # 故事剧本、分镜画格设计、台词与镜头意图
├── 02_character_anchors/             # 【核心】主角与配角人设卡（固定特征词与参考图）
├── 03_panel_prompts/                 # 每一格漫画的高清生图 Prompt (panel_01.txt ...)
├── 04_raw_panels/                    # AI 生图工具生成的高清原始画格 (panel_01.png ...)
├── 05_voiceover_and_srt/             # 故事台词 TTS 配音与精准对齐字幕 (panel_01.mp3, narration.srt)
├── 06_animated_clips/                # 【代码自动渲染】加入运镜（慢推/平移/特写）后的短切片
└── 07_final_video/                   # 翻页转场 + BGM/拟声词 + 烧录字幕的成片
```

## 3. 标准工作流预留契约 (Workflow Contract)
待后续工作流工具补充时，将标准支持以下链路命令：
1. **创建项目**：
   ```powershell
   python scripts/new_project.py <project_slug> --genre comic_story --title-zh "故事标题"
   ```
2. **旁白配音与时间轴生成 (TTS)**：
   提取 `01_script_and_storyboard` 中的台词，自动生成 `05_voiceover_and_srt/` 语音与时长。
3. **漫画运镜渲染 (Motion Comic FX)**：
   读取 `04_raw_panels` 与 `05_voiceover_and_srt`，按指定镜头意图（Slow Push, Snap Zoom, Pan）输出 `06_animated_clips/`。
4. **翻页组装与字幕烧录 (Final Render)**：
   施加漫画翻页（`slideleft` / `wipeleft`）转场，混入环境音效并压制双语字幕，输出到 `07_final_video/`。

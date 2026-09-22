# 动态漫画故事题材套件 (Motion Comic Preset)

## 1. 题材定位与核心特征
* **题材代号**：`comic_story`
* **适用场景**：悬疑推理、都市传说、历史人物志、热血叙事、心理故事短剧。
* **用户体验**：“看了一场生动的漫画，听了一场引人入胜的故事”。
* **核心优势**：
  - **角色一致、画风稳定**：依赖 AI 生图而非视频抽卡，人物绝不畸变或漂移。
  - **0 积分无边际成本**：不消耗昂贵的生成式视频大模型积分，由本地 FFmpeg Ken Burns 运镜引擎极速赋予动效。
  - **声音驱动节奏**：每格停留时长严格匹配故事台词语音时长，叙事节奏自然天成。

---

## 2. 标准工程目录结构 (7 阶段)
```text
<project_name>/
├── meta.json                         # 元数据 (genre: "comic_story", aspect_ratio: "4:3")
├── 01_script_and_storyboard/         # 故事剧本、分镜画格设计、台词与镜头意图 (storyboard.md)
├── 02_character_anchors/             # 【核心】主角与配角人设卡（固定特征词与参考图）
├── 03_panel_prompts/                 # 每一格漫画的高清生图 Prompt (panel_01.txt ...)
├── 04_raw_panels/                    # Nano Banana 2 (0积分) 生成的高清原始画格 (panel_01.png ...)
├── 05_voiceover_and_srt/             # 故事台词 TTS 配音与精准对齐字幕 (panel_01.mp3, narration.srt, durations.json)
├── 06_animated_clips/                # 【代码自动渲染】加入运镜（慢推/平移/呼吸微漂）后的短切片
└── 07_final_video/                   # 拼接 + BGM/环境音 + 白字黑边字幕的成片
```

---

## 3. 标准端到端生产 SOP (Step-by-Step SOP)

### Step 1: 创建动态漫画项目
```powershell
python scripts/new_project.py 002_rainy_detective --genre comic_story --title-zh "雨夜侦探" --ratio 4:3
```

### Step 2: 编写剧本与分镜大纲
编辑 `01_script_and_storyboard/storyboard.md`，按表格填入画格编号、画面构图、旁白台词与运镜意图（`slow_push`, `slow_pull`, `pan_left`, `pan_right`, `breathing_drift`, `snap_zoom`）。

### Step 3: 一键批量生成配音与时间轴字幕 (Edge-TTS)
```powershell
python scripts/generate_tts.py --project 002_rainy_detective --voice "zh-CN-YunxiNeural"
```
*自动在 `05_voiceover_and_srt/` 生成各画格 MP3 语音、单格 SRT 字幕、连续主字幕 `narration.srt` 以及精确时长映射 `durations.json`。*

### Step 4: 零积分静态生图 (Nano Banana 2) 与无感落盘
在 **Google Flow (Storyboard Studio)** 中选用 **Nano Banana 2（0 积分无限量）**，基于 `03_panel_prompts/` 提示词生成画格图片：
- **自动化无感落盘（推荐）**：在页面中查看画格大图后直接运行：
  ```powershell
  python scripts/download_panel.py --session <session_id> --filename panel_01.png --project 002_rainy_detective
  ```
- **或手动另存**：下载并放入 `04_raw_panels/panel_01.png` ~ `panel_XX.png`。

### Step 5: 本地动态运镜批量渲染 (Ken Burns Engine)
```powershell
python scripts/animate_panels.py --project 002_rainy_detective --resolution 1440x1080 --fps 24
```
*根据 `durations.json` 与分镜意图，FFmpeg 本地自动为静态画格注入丝滑推拉摇移运镜，秒级批量生成 `06_animated_clips/` 切片。*

### Step 6: 全片组装混音与白字黑边字幕烧录
```powershell
python scripts/assemble_comic.py --project 002_rainy_detective [--bgm path/to/ambient.mp3]
```
*自动无缝拼接所有切片、混入背景氛围音，并烧录符合移动端/横屏工业标准的白字黑边字幕，成片导出至 `07_final_video/final_comic_story.mp4`！*

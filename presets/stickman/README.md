# 火柴人视频题材套件 (Stickman Video Preset)

## 1. 题材定位与核心链路
* **题材代号**：`stickman`
* **适用场景**：哲学自白、心理分析、情感叙事、高信息密度概念阐释。
* **核心生产逻辑**：基于 Google Flow (Storyboard Studio) / Veo 视频大模型，通过 10 秒一段的分镜提示词生成连续视频切片，拼接并压制双语字幕。

## 2. 标椎规格与契约
* **画幅比例**：`4:3` 横版（Classic Academy 1.33:1），主体居中，留白充裕。
* **分镜总数**：18 段（每段 10 秒，全长 180 秒）。
* **角色设定**：Style 2B（圆顶小红帽、黄T恤、黑短裤、极简火柴人黑线条）。
* **SSOT 提示词目录**：`03_gemini_prompts/clips_safe/prompt_01.txt` ~ `prompt_18.txt`。

## 3. 标准目录结构 (6 阶段)
```text
<project_name>/
├── meta.json                         # 元数据 (genre: "stickman", aspect_ratio: "4:3")
├── 01_research/                      # 原始素材研究与长文提炼
├── 02_director_proposal/             # 导演方案与 18 段分镜脚本
├── 03_gemini_prompts/
│   ├── clips_safe/                   # 【单一事实来源】自洽且全量 18 段提示词
│   └── prompts_all.md                # 完整提示词总汇表
├── 04_raw_clips/                     # 从 Google Flow 下载的原始切片 (clip_01.mp4 ~ 18)
├── 05_subtitles/                     # 毫秒级双语字幕轨 (narration.bilingual.srt)
└── 06_final_video/                   # 最终拼接成片 (stitched_raw.mp4, final_subtitled.mp4)
```

## 4. 专属执行命令
```powershell
# 1. 创建新火柴人项目
python scripts/new_project.py <project_slug> --genre stickman --title-zh "中文标题"

# 2. 拆分提示词
python scripts/split_prompts.py --project <project_slug>

# 3. 拼接切片 (含 4:3 居中裁剪支持)
python scripts/concat_clips.py --project <project_slug> --crop-ratio 4:3

# 4. 压制双语字幕 (自适应横竖屏探测与安全边距)
python scripts/embed_subtitles.py --project <project_slug>
```

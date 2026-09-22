---
name: directing-comic-story
description: Use when turning story outlines, novels, urban legends, mysteries, or scripts into structured motion comic storyboards, panel prompts, character consistency anchors, and narrated storytelling flows.
---

# Directing Motion Comic Stories (动态漫画故事导演规范)

## Core Contract (核心契约)

将故事大纲或小说剧本转化为：
1. **角色一致性锚点卡 (Character Consistency Anchors)**；
2. **分镜画格大纲矩阵 (Panel Storyboard Matrix)**（含画面构图、角色神态、旁白台词、预估时长与运镜意图）；
3. **高表现力独立生图提示词 (Panel Image Prompts)**，为后续代码级镜头推拉、翻页转场与配音合成提供精准输入。

---

## Setup Gate (前置确认门禁)

在策划与生成之前，必须明确以下基础属性：
* **故事源文本 (Source Story/Script)**：小说、悬疑短篇、都市传说或自述独白。
* **画幅比例 (Aspect Ratio)**：`4:3`（经典漫画黄金画格，推荐默认）或 `16:9`。
* **漫画画风基准 (Comic Art Style)**：
  - `Manga Ink & Dramatic Shadow`（黑白高对比墨线，极富张力的网点与阴影，推荐默认）
  - `Vintage Noir Graphic Novel`（复古美漫/侦探黑色电影风，低饱和水彩与暗调光影）
  - `Modern Webtoon Color`（全彩韩漫/现代数码条漫风格，明快线条与鲜艳氛围光）
* **核心角色锚点 (Character Anchors)**：主角固定长相、发型、代表性服装与显著特征。
* **讲故事音色与基调 (Narrator Persona)**：沉稳叙述、悬疑低语、情感起伏等。

---

## 生产工作流 (Workflow)

```text
阶段 1: 故事提炼与人设锚定 -> 阶段 2: 分镜画格矩阵设计 -> 阶段 3: 画格生图提示词生成 -> 阶段 4: 配音与运镜交接
```

### 1. 角色一致性锚点定义 (`02_character_anchors/characters.json`)
必须锁定主角的特征词，在后续所有画格提示词中强制注入：
* **固定服装与发型**：如 `a sharp-eyed detective in a dark crumpled trench coat, messy jet-black hair, visible scar across left temple`。
* **画风质量基准**：如 `masterpiece, professional manga illustration, dynamic ink lines, atmospheric cinematic lighting, 4:3 aspect ratio`。

### 2. 分镜画格矩阵设计 (`01_script_and_storyboard/storyboard.md`)
将故事拆解为 8~16 个连贯画格，每一格必须明确：
1. **视觉构图**：俯视特写、仰角全景、过肩镜头、斜角构图（Dutch Angle）；
2. **角色神态与动作**：避免呆板站立，捕捉情绪爆发瞬间（瞳孔收缩、紧握双拳、雨水从发梢滴落）；
3. **旁白/台词**：纯文案，无括号动作提示，便于直接送入 TTS 语音引擎；
4. **预估时长**：根据台词字数测算（中文约 3.5~4 字/秒）；
5. **镜头运镜意图 (Camera Motion Intent)**：
   - `Slow Push (慢速推进)`：从全景缓慢向前推 5%~10%，营造压抑或沉浸感；
   - `Snap Zoom (特写疾推)`：0.3 秒内快速推至角色眼神或关键道具；
   - `Pan Horizontal (平移扫镜)`：从背景环境平滑摇镜至人物侧脸；
   - `Breathing Drift (呼吸微晃)`：极微弱的镜头漂移，给画面生命力。

### 3. 生成独立画格提示词 (`03_panel_prompts/panel_XX.txt`)
* 每一格提示词均为**自包含（Self-contained）**，强制包含人设锚定词与画风标记。
* 严禁在生图提示词中放入文字排版、气泡对话框（保持纯画面，由后期字幕统一呈现）。

---

## 审查与交付准则 (Output Rules)

1. **画面纯净度**：画面中严禁出现文字、水印、对话气泡（Speech Bubbles）、翻译文本；
2. **转场动效契约**：画格之间的转场默认采用漫画翻页效果（`slideleft` 或 `wipeleft`），场景跨越采用黑场淡入（`fade`）；
3. **台词与画面强咬合**：每一句旁白都必须与对应画格传递的情绪完全共鸣，绝无音画割裂。

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
  - `Modern Webtoon Color & Atmospheric Lighting`（全彩韩漫/现代高精条漫风格，明朗线条、电影级情绪光影与冷暖氛围，推荐现代流行默认）
  - `Manga Ink & Dramatic Shadow`（黑白高对比墨线，极富张力的网点与阴影，适合纯悬疑短篇）
  - `Vintage Noir Graphic Novel`（复古美漫/侦探黑色电影风，低饱和水彩与暗调光影）
* **核心角色锚点 (Character Anchors)**：主角固定长相、发型、代表性服装与显著特征。
* **讲故事音色与基调 (Narrator Persona)**：沉稳叙述、悬疑低语、情感起伏等。

---

## 生产工作流 (Workflow)

```text
阶段 0: 角色与场景基准定妆 (Visual Anchors) 
  ➔ 阶段 1: 分镜大纲与台词设计 
  ➔ 阶段 2: 提示词编译器自动组装 (Prompt Assembler) 
  ➔ 阶段 3: 参考图/角色库驱动生图 (Image-to-Image / Characters)
  ➔ 阶段 4: 一致性预审门禁 (QA Gate)
  ➔ 阶段 5: TTS配音、运镜切片与字幕合成
```

### 0. 视觉定妆先行门禁 (Mandatory Pre-flight Visual Anchor Gate)
**在渲染任何正式分镜画格前，严禁直接跳到分镜生图！** 必须先完成视觉定妆：
1. **角色基准图 (`02_character_anchors/<role>_anchor.png`)**：
   - 使用 0 积分生图工具（如 Nano Banana 2）打磨出 1~2 张主角标准定妆图（正脸或半身）；
   - 锁定具体且鲜明的物理特征（如年龄、发型、肤色、标志性服装、疲惫黑眼圈、特定配饰）；
   - 保存至项目的 `02_character_anchors/` 目录作为全片视觉单一事实源（SSOT）。
2. **场景基准图 (`02_character_anchors/<scene>_anchor.png`)**：
   - 提取全片核心室内/室外主场景（如雨夜卧室、昏暗厨房、黎明走廊），生成光影基调参考图。
3. **【门禁】定妆图必须目视确认无形变且画风纯正后，方可启动分镜批量出图。**

### 1. 角色一致性锚点定义 (`02_character_anchors/characters.json`)
必须在配置文件中沉淀主角的核心特征词、固定服饰与画风基准：
```json
{
  "appearance_prompt": "A 35-year-old Asian man in a crumpled grey dress shirt, messy black hair, tired dark eye circles",
  "style_anchor": "masterpiece, cinematic noir graphic novel, vintage monochrome manga ink illustration, fine lineart cross-hatching, deep chiaroscuro lighting, 4:3 aspect ratio"
}
```

### 2. 分镜画格矩阵设计 (`01_script_and_storyboard/storyboard.md`)
将故事拆解为连贯画格，每一格必须明确：
1. **视觉构图**：俯视特写、仰角全景、过肩镜头、斜角构图（Dutch Angle）；
2. **角色神态与动作**：避免呆板站立，捕捉情绪爆发瞬间（瞳孔收缩、紧握双拳、雨水从发梢滴落）；
3. **旁白/台词**：纯文案，无括号动作提示，便于直接送入 TTS 语音引擎；
4. **预估时长**：根据台词字数测算（中文约 3.5~4 字/秒）；
5. **镜头运镜意图 (Camera Motion Intent)**：
   - `Slow Push (沉浸慢推)`：全景向主角面部或关键信息缓慢推进 5%~10%（严禁正弦振荡，保持单向超采样平滑）；
   - `Slow Pull (宏观拉远)`：从特写平稳拉远至环境全貌，营造疏离或唏嘘感；
   - `Pan Horizontal (平稳横移)`：水平方向匀速移动，扫视环境细节或双人对峙；
   - `Static Cut (纯净定格切换)`：**推荐叙事模式**。100% 绕过 `zoompan` 复杂滤镜，直接单步 scale+pad，零位移、零插值模糊、零亚像素抖动，使观众完全沉浸在构图张力与剧情中；
   - **【去抖铁律】**：严禁在叙事漫剧中引入 `sin/cos` 周期晃动（如呼吸抖动、震屏）；若使用运镜必须采用 2X 超采样抗抖，或优先采用纯静态切换（`--static`）。

### 3. 提示词编译器自动组装 (`03_panel_prompts/panel_XX.txt`)
**严禁人工手写各个分镜的自由提示词！**
所有分镜提示词必须由脚本（如 `scripts/assemble_prompts.py`）严格拼装：
$$\text{Final Prompt} = [\text{角色特征锚点}] + [\text{分镜核心动作与构图}] + [\text{全局统一画风锁}] + [\text{负向排他契约}]$$

- **负向排他契约 (Negative Constraints)** 必须全量注入：
  `no photorealism, no real human photography, no 3d render, no text, no words, no speech bubbles, no dialogue balloons, clean artwork.`

### 4. 平台角色库或参考垫图出图
在生图工具（如 Google Flow / Nano Banana 2）中：
1. 将 `_anchor.png` 添加为工作台角色（Character Casting `@tag`）或在提示框中添加素材作为垫图参考；
2. 模型基于确定性的骨骼和五官进行动作外推，彻底杜绝画风与种族突变。

---

## 审查与交付准则 (Quality & Consistency Gate)

1. **画风纯净与排他性**：严禁出现写实真人照片、彩色突变、3D 渲染质感；全片画风必须 100% 保持在统一美术风格（全彩或墨线漫画）；
2. **画面无文本契约 (No Visual Text)**：画面中严禁出现文字、水印、对话气泡（Speech Bubbles）、英文连环画标签；叙事台词全部由底部压制字幕呈现；
3. **移动端单行恒定基线大字幕规范 (Single-Line Fixed Baseline Subtitles)**：
   - **严禁双行折行**：所有字幕必须经过语气停顿拆分为单行（每行 ≤ 16 汉字），杜绝双行引发的上下基线窜动跳动；
   - **绝对恒定高度**：全片字幕必须固定在同一底部垂直高度（`MarginV=60`, `Alignment=2`）；
   - **移动端大字号**：字号必须 ≥ 54px，配合 `Outline=3` 纯黑描边与纯白文字，确保手机横屏/4:3 小尺寸下具备顶级辨识度；
4. **角色面容一致性**：主角在各分镜中的年龄、发型、五官特征、代表性衣着必须肉眼可辨为同一人；
5. **转场动效契约**：运镜平稳无抖动或直接采用纯净静态定格切换（`--static`），音画字幕精准对齐。

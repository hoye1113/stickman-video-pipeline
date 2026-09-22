# 提案 RFC 002：零积分动态漫/图文故事短视频生产流水线 (Zero-Credit Motion Comic Pipeline)

> **提案编号**：`RFC-002`  
> **提案日期**：2026年9月  
> **所属题材**：`comic_story`（动态漫/图文故事）  
> **核心目标**：彻底摆脱对生成式视频大模型（Runway/Veo/Flow Video）积分与 API 的依赖，依托“**0 积分 Nano Banana 2 静态生图 + Edge-TTS 微软真声配音 + 本地 FFmpeg Ken Burns 动态运镜引擎**”，实现 0 边际成本、高画面表现力、100% 角色一致性的人物故事短视频量产。

---

## 1. 提案概述 (Proposal Overview)

- **提案类型**：新题材生产管线重构 (Pipeline RFC)
- **目标题材套件**：`presets/comic_story`
- **预估单片时长与画幅**：1 ~ 3 分钟（10 ~ 18 画格） / `4:3` 横屏（1440×1080）
- **核心定位与受众**：悬疑推理、都市传说、心理疗愈、深度故事、历史奇闻等注重台词感染力与视觉信息密度的长短视频平台（B站、YouTube、抖音、小红书）。

---

## 2. 背景与核心破局点 (Background & Key Insights)

### 2.1 传统 AI 视频的致命痛点
1. **积分消耗快、试错代价昂贵**：生成式视频模型（如 10 秒消耗 15 积分）单月 1,000 积分仅能跑 60+ 片段，遇到抽风畸变，大量算力浪费在废片抽卡上；
2. **角色一致性难以维持（Face/Style Drifting）**：连续视频生成时，人物五官、服装细节每隔几秒便发生形变；
3. **节奏拖沓无力**：纯模型生成的视频动作常带有“果冻效应”与慢动作感，缺乏漫画特有的剪辑张力。

### 2.2 0 积分方案破局哲学
借鉴 `@CrazyKaomei` 与顶尖无露脸（0-face）短视频创作者（`@GeekCatX`、`@Hamburgerai`、Lucas Patiri）的成熟实践：
- **短视频完播率的核心驱动力不是 3D 动作，而是“戏剧冲突 + 视觉构图 + 镜头呼吸感 + 抓人配音”**；
- 静态画格使用 **Google Flow 内置 Nano Banana 2（0 积分无限量生成）**，挑出最优构图，100% 锁定人设长相；
- 动效交由**本地 FFmpeg 代码级运镜引擎**，以毫秒级精度配合旁白语速推拉摇移；
- 边际成本降为 **绝对零元（0 积分、0 API 费）**，每片渲染耗时从 30 分钟降至 1 分钟！

---

## 3. 叙事模型与分镜架构 (Narrative & Storyboard Blueprint)

### 3.1 叙事节奏（Lucas Patiri 2.6B 转化漏斗）
- **Act 1: 生死 Hook (0 ~ 3s)**：第一画格必须直击冲突中心（如狂风暴雨夜、桌上带血的信封、主角震惊睁大的双眼），配合 `snap_zoom`（疾推特写）与紧迫开场白；
- **Act 2: 痛点与情境推进 (3 ~ 30s)**：大白话展开背景，`slow_push`（慢推）增强心理沉浸；
- **Act 3: 转折与机制推演 (30 ~ 120s)**：多格并置或横向平移（`pan_left/right`），带出故事高潮；
- **Act 4: 升华与有力 CTA (120 ~ 180s)**：慢拉（`slow_pull`）展示全景，配以深沉金句。

### 3.2 角色与视觉锚点设计 (Avatar & Visual Lock)
- **固定人设卡**：`presets/comic_story/template/02_character_anchors/` 明确主角面部特征、发型、代表性服装色系；
- **画风基准（推荐默认）**：
  ```text
  masterpiece, cinematic graphic novel style, vintage manga ink lines, deep dramatic shadows, high contrast, atmospheric rim light, 4:3 ratio
  ```

---

## 4. 技术与资产生成路线 (Production Pipeline)

```text
01_script_and_storyboard/storyboard.md (分镜表)
                    │
                    ├───▶ scripts/generate_tts.py ──▶ 05_voiceover_and_srt/
                    │                                 (MP3语音 + SRT字幕 + durations.json)
                    │
                    ├───▶ Nano Banana 2 (0积分生图) ─▶ 04_raw_panels/
                    │                                 (panel_01.png ~ 18.png)
                    ▼
          scripts/animate_panels.py
          (FFmpeg zoompan/crop/fps 运镜引擎)
                    │
                    ▼
          06_animated_clips/ (clip_01.mp4 ~ 18.mp4)
                    │
                    ▼
          scripts/assemble_comic.py
          (多轨拼接 + 白字黑边字幕 + 环境音混音)
                    │
                    ▼
          07_final_video/final_comic_story.mp4
```

---

## 5. 运镜动效预设与数学表达 (Motion Presets)

在 `scripts/animate_panels.py` 中，采用高平滑度的 FFmpeg 表达式：
1. **`slow_push` (向内平推 15%)**：
   - 表达式：`zoom = 1.0 + 0.15 * (on / (fps * duration))`，居中锚点 `x = '(iw - iw/zoom)/2'`, `y = '(ih - ih/zoom)/2'`；
2. **`slow_pull` (向外拉远 15%)**：
   - 表达式：`zoom = 1.15 - 0.15 * (on / (fps * duration))`；
3. **`pan_left` / `pan_right` (横向平摇)**：
   - 预放大 `zoom = 1.2`，在 X 轴平滑移动 `x = '(iw - iw/zoom) * (on / (fps * duration))'`；
4. **`breathing_drift` (呼吸感微漂)**：
   - 轻微缩放 `zoom = 1.03 + 0.015 * sin(2 * PI * on / (fps * 3))`，赋予静态角色心跳与生命；
5. **`snap_zoom` (前 0.3s 冲击特写)**：
   - 前 30% 帧迅速放大至 1.25x，后 70% 极慢平推。

---

## 6. 成本与资源评估 (Cost & Resource Estimation)

| 资源项 | 消耗值 | 备注 |
|---|---|---|
| **Google Flow 视频积分** | **0 点** | 完全不触发 Video Generation，仅使用 0 积分 Nano Banana 2 挑图 |
| **云端 API 费用** | **0 元** | 不调用任何付费 API |
| **配音费用** | **0 元** | 使用开源 Edge-TTS 微软真声，音质堪比专业录音棚 |
| **渲染时间** | **约 30~60 秒** | 本地 FFmpeg 硬件加速直接输出 1080p |

---

## 7. 审批与实施状态 (Status)

- **提案状态**：已批准 (Approved)
- **执行分支**：`main`
- **实施计划**：编写 `generate_tts.py`、`animate_panels.py`、`assemble_comic.py` 并通过闭环验证。

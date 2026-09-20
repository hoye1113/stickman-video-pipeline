# 下游 Agent 执行任务书 (可以直接复制发送)

> **使用说明**：你可以将以下内容完整复制并直接发送给负责执行该工作流的 Agent（如 Claude、Cursor、Codegen 或本地智能体）。

---

```markdown
# 任务背景与执行指令：3分钟情感科普火柴人视频制作

你正在参与一个“火柴人情感科普视频”的全流程自动化/半自动化制作任务。
请严格按执行顺序阅读并遵守以下本地 Skill 规范，遵循严格的两阶段门禁约束：

---

## 1. 必读本地 Skill 目录及重点文件（按顺序阅读）

### 阶段一：资料检索 (Unified Search)
- **本地目录**：`D:/workSpace/hoye-skills-main/skill-collection/productivity/yichen-skills/yichen-unified-search`
- **重点阅读文件**：
  - `SKILL.md`（核心原则与访问边界）
  - `references/routes.md`（离线路由与后端参数契约）
  - `references/candidate-schema.md`（标准 Candidate Envelope 规范）
  - `references/access-boundaries.md`（凭证与访问权限边界）
- **职责**：
  围绕用户给定的情感科普主题（如焦虑内耗、情绪价值、破局行动、心理防御等），检索真实、有说服力的心理学/认知科学机制与科学比喻。检索结果整理至 `01_research/research_summary.md`。不捏造虚假论文、统计数据或未经证实的假想。

### 阶段二：火柴人分镜与提示词设计 (Directing Stickman Videos)
- **本地目录**：`D:/workSpace/hoye-skills-main/skill-collection/creative/directing-stickman-videos`
- **重点阅读文件**：
  - `SKILL.md`（核心契约、设定闸门与两阶段流程）
  - `references/storyboard-template.md`（Phase A 导演预案模板与密度规范）
  - `references/style-catalog.md`（视觉风格分类、角色防形变锁、动效节奏）
  - `references/omni-flash-prompt-contract.md`（Phase B 提示词契约与负面提示词）
  - `references/examples.md`（端到端完整参考范例）
- **核心规格扩展（3分钟视频要求）**：
  - 传统 Skill 为 1 分钟（6段），**本项目目标为约 3 分钟**。
  - 请设计三幕式结构，共 **18 个分镜头片段（Clips 1–18，每段约 10 秒）**，总时长约 180 秒。
  - 英文 VO 旁白总量约为 **400–450 词**（每段约 22–26 词），配有自然流畅的中文参考对照。
  - **三幕规划**：
    - **第一幕 (Clips 1–6)**：痛点共鸣与困境具象化（强 Hook、情绪陷入死循环隐喻）。
    - **第二幕 (Clips 7–12)**：机制深度解构（大脑神经机制、心理误区、冲突升级）。
    - **第三幕 (Clips 13–18)**：认知重构与微行动解脱（打破循环、动作爆发、升华总结与 CTA）。
- **必须遵循的视觉与提示词铁律**：
  - 每段划分为 `[0–3s]`、`[3–7s]`、`[7–10s]` 三个时钟拍点，视觉动态每 2-3 秒必须有变化。
  - 严禁画面中出现任何文字、字母、数字、字幕或对话框（纯图形表达，`strictly no speech bubbles, no dialogue boxes`）。
  - 锁定角色一致性（如选择 Style 2，严格锁定红冷帽+黄T恤，禁止画细致眼睛/瞳孔）。
  - BGM 连续性锁定（Clip 1 确立主题，Clip 2–18 显式继承 Clip 1 的乐器与节奏）。
  - 相邻片段首尾帧动作/镜头必须连续（Visual Continuity Interface）。

### 阶段三：Gemini 网页版视频生成 (Gemini Web Generation)
- **目标平台**：[https://gemini.google.com](https://gemini.google.com/)
- **说明**：Gemini 网页版无本地目录。
- **职责**：
  - 在 Phase B 提示词通过后，将 18 条 Prompt 依次提交给 Gemini 网页版（手动或通过浏览器自动化）。
  - 生成 18 段约 10 秒的视频，下载并统一保存在本地 `04_raw_clips/clip_01.mp4` 至 `clip_18.mp4`。

### 阶段四：字幕处理与拼接 (Embed Subtitles)
- **本地目录**：`D:/workSpace/hoye-skills-main/skill-collection/creative/embed-subtitles`
- **重点阅读文件**：
  - `SKILL.md`（FFmpeg 字幕压制参数、样式规则、RTL 自动检测修复）
- **职责**：
  - 使用 FFmpeg 将 `04_raw_clips/` 中的 18 个视频按顺序无缝拼接为完整视频。
  - 提取或对齐 18 段台词制作 `narration.en.srt`（与 `narration.zh.srt`）。
  - 按照标准样式（字号 22–24px、底边距 35–45px、描边 2）将字幕压制烧录进最终成片 `06_final_video/final_stickman_video.mp4`。

---

## 2. 核心工作流与当前门禁执行指令 (Gate Rules)

### 【极其重要：当前只执行到 Phase A，禁止提前生成视频】

请严格按以下步骤推进：
1. **执行阶段一**：进行资料检索与科学论证，形成核心心理学科普事实提炼（保存在 `01_research/`）。
2. **确认设定闸门 (Setup Gate)**：
   若用户未指定，请与用户明确：
   - 视频尺寸（`16:9`、`9:16` 或 `1:1`）；
   - 视觉风格（`Style 1 极简黑白灰`、`Style 2A 现代极简科技白底青蓝UI`、`Style 2B 全彩电影叙事风`）。
3. **输出 Phase A 导演预案**：
   - 产出包含中英文标题、核心论点、Hook、视觉调色盘/环境、BGM 情绪曲线。
   - 包含完整的 **18 行分镜头表格（Time, 叙事目的, 火柴人场景, 动作/镜头/转场, 英文VO, 中文参考, BGM/SFX）**。
4. **【停止并等待用户审批 (Review Gate)】**：
   - **完成 Phase A 后立即停止响应，向用户呈报预案并等待用户明确批准！**
   - **在用户没有明确说“确认/通过”当前 Phase A 之前，绝对不要编写 Phase B 的 18 条生成提示词，绝对不要尝试生成视频！**
```

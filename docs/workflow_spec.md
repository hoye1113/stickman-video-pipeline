# 3分钟火柴人视频项目规范与搭建清单 (Workflow Specification)

本规范定义了从“主题检索”到“最终压制字幕成片”的完整端到端执行标准。各执行 Agent 在运行任务时必须严格遵照本规范及所引用的本地内化 Skill 契约。

---

## 零、多项目矩阵管理规范 (Multi-Project Governance)

项目采用**矩阵化工程隔离体系**：
- 每一个独立视频主题保存在 `projects/<project_slug>/`（如 `projects/001_betrayal_and_split_soul/`）；
- 每个项目拥有独立的 `01_research/` 至 `06_final_video/` 6大阶段目录与 `meta.json` 状态记录；
- 创建新项目时统一运行脚手架：
  ```powershell
  python scripts/new_project.py <slug> --title-zh "<中文标题>" --title-en "<英文标题>" --ratio 9:16
  ```
- 严禁在根目录直接堆放临时多媒体文件，所有中间产物严格归集在对应项目目录下。

---

## 一、各阶段详细任务与本地 Skill 契约解析

### 1. 资料检索阶段 (Research Phase)
- **依赖 Skill 项目内路径**：
  `./skills/yichen-unified-search`
- **重点读取文件**：
  - `SKILL.md`（核心原则与固定边界）
  - `references/routes.md`（离线路由与平台选择机制）
  - `references/candidate-schema.md`（标准 Candidate Envelope 格式规范）
  - `references/access-boundaries.md`（凭证安全、只读公共访问边界）
- **核心执行规则**：
  1. **离线路由优先**：执行前通过 `scripts/route_search.py` 生成确定性计划，不得盲目联网或遍历无关平台。
  2. **科普事实严谨性**：检索科学心理学机制（如多巴胺、杏仁核、内耗循环、认知行为疗法 CBT 微动作等），不得捏造虚假论文、统计数据或未经证实的伪科学。
  3. **输出规范**：将检索与事实核验结果保存在目标项目的 `01_research/research_summary.md`，提炼出 3 分钟视频的核心叙事逻辑与事实支撑点。

---

### 2. 火柴人分镜与提示词设计阶段 (Directing & Storyboarding Phase)
- **依赖 Skill 项目内路径**：
  `./skills/directing-stickman-videos`
- **重点读取文件**：
  - `SKILL.md`（两阶段工作流与门禁规则）
  - `references/storyboard-template.md`（Phase A 导演预案标准模板与要求）
  - `references/style-catalog.md`（视觉风格分类、角色防形变锁、动效节奏）
  - `references/omni-flash-prompt-contract.md`（Phase B 生产级提示词契约）
  - `references/examples.md`（端到端完整范例）
- **扩展要求（1分钟扩展至3分钟）**：
  - 原 Skill 标准为 1 分钟（6 个片段，约 130–150 词英文 VO）。
  - **本项目目标为约 3 分钟**：扩展为 **18 个片段（约 180 秒，每段约 10 秒）**，英文旁白控制在 **400–450 词**（每段约 22–25 词）。
  - **三幕式结构 (18 Clips Structure)**：
    - **第一幕（Act 1: Clips 1–6，0–60s）**：痛点共鸣与现象引入（强烈 Hook、灾难化思维/情感困境具象化、被困隐喻）。
    - **第二幕（Act 2: Clips 7–12，60–120s）**：机制科普与认知剖析（大脑杏仁核反应、情绪循环机制、认知盲区拆解）。
    - **第三幕（Act 3: Clips 13–18，120–180s）**：认知重构与微行动解脱（微行动破坏内耗循环、能量爆发、升华总结与有力 Call-to-Action）。
- **Phase A 必备闸门 (Setup Gate & Review Gate)**：
  - 必须在规划前明确：**画面比例**（16:9 / 9:16 / 1:1）、**视觉风格**（Style 1 极简黑白灰 / Style 2A 科技白底青蓝玻璃 / Style 2B 全彩电影叙事）。
  - 输出到目标项目的 `02_director_proposal/proposal_phase_a.md`。
  - **必须严格停止并请求用户批准 Phase A**，未经用户确认，**绝对不得提前生成 Phase B 提示词或视频**！
- **Phase B 生产提示词铁律**：
  - 对应底层模型：**`Gemini Omni 1.1 Flash` (`gemini-omni-1.1-flash`)**。
  - 输出到目标项目的 `03_gemini_prompts/prompts_all.md`，并通过 `scripts/split_prompts.py --project <slug>` 自动拆解到 `clips/prompt_01.txt` ~ `prompt_18.txt`。
  - 每段划分为 `[0–3s]`、`[3–7s]`、`[7–10s]` 三个时钟拍点，至少 4 个明确视觉装置。
  - 严禁画面中出现任何文字、字母、数字、字幕或对话框（`strictly no speech bubbles, no dialogue boxes`）。
  - 旁白纯音频驱动，使用双引号包裹精确英文文本。
  - 角色一致性锚点锁定。
  - BGM 连续性锁定（Clip 1 确立主题，Clip 2–18 显式继承 Clip 1 的配器与节拍）。
  - 相邻片段首尾帧动作/镜头必须连续（Visual Continuity Interface）。

---

### 3. Google AI Studio 视频生成与资产收录 (Omni Flash Video Generation)
- **平台位置**：[Google AI Studio Playground](https://aistudio.google.com/prompts/new_chat)
- **底层模型**：`Gemini Omni 1.1 Flash` (`gemini-omni-1.1-flash`)
- **关键视频参数**：
  - `Video duration`：10 秒（与提示词契约一致）
  - `Aspect ratio`：16:9 / 9:16 / 1:1
  - `Frame rate`：24fps
  - `Resolution`：360p / 720p / 1080p
- **执行方式（Agent 自动化接管）**：
  - 复用宿主机已登录 Google Pro 会话的浏览器窗口，保持会话常驻连接。
  - Agent 依次将各片段提示词填入输入框，触发 `Run Ctrl ↵`。
  - 渲染完成后调用 `scripts/download_clip.py --session <id> --filename clip_XX.mp4 --project <slug>` 自动以 Base64 读取并保存在该项目的 `04_raw_clips/clip_XX.mp4`。
  - 质量校验：检查各片段时长、画面比例是否一致，有无明显的文字混入或肢体崩坏。

---

### 4. 字幕处理与视频拼接 (Post-Production & Subtitle Embedding)
- **依赖 Skill 项目内路径**：
  `./skills/embed-subtitles`
- **重点读取文件**：
  - `SKILL.md`（FFmpeg 字幕压制参数、样式控制、RTL 自动检测修复）
- **核心执行规则**：
  1. **无缝拼接**：运行 `python scripts/concat_clips.py --project <slug>`（FFmpeg），自动对目标项目的 `04_raw_clips/` 中的所有片段按序无损拼接，生成 `06_final_video/stitched_raw.mp4`。
  2. **时间轴对齐**：在目标项目的 `05_subtitles/` 生成双语字幕。
  3. **样式与安全区**：字幕字号推荐 22–24px，底部边距 35–45px，添加黑色描边（outline 2）以防背景干扰。
  4. **压制生成成片**：运行 `python scripts/embed_subtitles.py --project <slug>` 将字幕硬编码烧录进成片，保存至 `06_final_video/final_subtitled.mp4`。

---

## 二、项目目录文件职责总表

| 目录/文件 | 责任角色 | 格式要求 | 状态流转 |
|---|---|---|---|
| `projects/<slug>/01_research/research_summary.md` | 资料检索 Agent | Markdown 结构化研究报告 | 收集整理 → 确认事实源 |
| `projects/<slug>/02_director_proposal/proposal_phase_a.md` | 导演 Agent | 完整 Phase A 提案（含18行分镜表） | 草稿 → **用户审核通过** |
| `projects/<slug>/03_gemini_prompts/prompts_all.md` | 编剧/Prompt Agent | 18条独立英文 Prompt + 拼接指南 | 仅在 Phase A 确认后生成 |
| `projects/<slug>/03_gemini_prompts/clips/prompt_01~18.txt` | 编剧/Prompt Agent | 纯文本 Prompt，方便批处理 | 就绪 |
| `projects/<slug>/04_raw_clips/clip_01~18.mp4` | 浏览器生成 Agent | 720p MP4 视频，每个约10秒 | 逐段生成并归档校验（Git忽略） |
| `projects/<slug>/05_subtitles/narration.en.srt` | 字幕处理 Agent | 严格符合 SRT 格式标准 | 基于实际时间轴对齐 |
| `projects/<slug>/06_final_video/final_subtitled.mp4` | 后期合成脚本/Agent | 最终交付成品视频 | 拼接+压制成片（Git忽略） |
| `projects/<slug>/meta.json` | 工程管理 Agent | JSON 结构化元数据 | 记录配置参数与生成进度 |

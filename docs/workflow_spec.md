# 3分钟火柴人视频项目规范与搭建清单 (Workflow Specification)

本规范定义了从“主题检索”到“最终压制字幕成片”的完整端到端执行标准。各执行 Agent 在运行任务时必须严格遵照本规范及所引用的本地内化 Skill 契约。

---

## 零、多项目矩阵管理规范 (Multi-Project Governance)

项目采用**矩阵化工程隔离体系**：
- 每一个独立视频主题保存在 `projects/<project_slug>/`（如 `projects/001_betrayal_and_split_soul/`）；
- 每个项目拥有独立的 `01_research/` 至 `06_final_video/` 6大阶段目录与 `meta.json` 状态记录；
- 创建新项目时统一运行脚手架：
  ```powershell
  python scripts/new_project.py <slug> --title-zh "<中文标题>" --title-en "<英文标题>" --ratio 4:3
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
  - 必须在规划前明确：**画面比例**（4:3 经典横屏推荐 / 16:9 / 9:16 / 1:1）、**视觉风格**（Style 2B 全彩电影叙事推荐 / Style 2A 科技白底青蓝玻璃 / Style 1 极简黑白灰）。
  - 输出到目标项目的 `02_director_proposal/proposal_phase_a.md`。
  - **必须严格停止并请求用户批准 Phase A**，未经用户确认，**绝对不得提前生成 Phase B 提示词或视频**！
- **Phase B 生产提示词铁律**：
  - 对应底层模型：**`Gemini Omni 1.1 Flash` (`gemini-omni-1.1-flash`)**。
  - 输出到目标项目的 `03_gemini_prompts/prompts_all.md`，并通过 `scripts/split_prompts.py --project <slug>` 自动拆解到 `clips_safe/prompt_01.txt` ~ `prompt_18.txt`。
  - 每段划分为 `[0–3s]`、`[3–7s]`、`[7–10s]` 三个时钟拍点，至少 4 个明确视觉装置。
  - 严禁画面中出现任何文字、字母、数字、字幕或对话框（`strictly no speech bubbles, no dialogue boxes`）。
  - 旁白纯音频驱动，使用双引号包裹精确英文文本。
  - 角色一致性锚点锁定。
  - BGM 连续性锁定（Clip 1 确立主题，Clip 2–18 显式继承 Clip 1 的配器与节拍）。
  - 相邻片段首尾帧动作/镜头必须连续（Visual Continuity Interface）。

---

### 3. Google Flow 视频生成与资产收录 (Google Flow Storyboard Studio)

#### 3.1 战略背景与核心哲学 (Philosophy & Strategy)
本项目源自推友 **“疯狂的烤妹儿 🩵”**（`@CrazyKaomei`）提出的 **“一人可落地的「AI + 自媒体」最小阻力路径”**：
- **核心认知**：“你占到了一个入口，不等于你拥有了作品。用不起来的便宜，依然是昂贵的浪费。别把会员当主角，它只是一声开门声。真正要做的是打磨出一套属于你自己的内容生产闭环。”
- 依托用户已订阅的 **Google One AI Premium PRO** 会员（每月 1,000 点官方积分），通过浏览器自动化打通**零边际成本的视频生产通道**，拒绝调用 Google Cloud 付费 API，将便宜的算力入口转化为工业化稳定交付的作品。

#### 3.2 平台生产架构与特性优势 (Platform Architecture)
生产唯一选用 **Google Flow (`https://labs.google/fx/tools/flow`)** 作为端到端视频工坊：
1. **Storyboard Studio 镜头卡片流**：
   - 原生提供故事板卡片（Shot Cards），完美映射 Phase A 的 18 段分镜结构；
   - 每张卡片独立生成与重绘，杜绝单会话连续多轮时长累加（超 30s 崩溃）的硬伤。
2. **首尾帧连续性控制 (First & Last Frame Control)**：
   - 将上一片段的尾帧无缝作为下一片段的起始帧，实现物理级平滑过渡，根绝纯文本生成中的角色动作突变。
3. **Nano Banana 2 零积分角色锁定 (0 Credits)**：
   - 生视频前先用 0 积分生成 4 张高清静态关键帧，校验角色的服装（如红色冷帽+黄色T恤）、配色与光影；确认无畸变后再消耗约 15 积分渲染 10 秒视频，大幅消除试错损耗。
4. **官方合规配额通道**：
   - 走 Google One Pro 官方消费级权益，每月 1,000 积分稳定可产出 60+ 个 10 秒片段（可支撑 3~4 条完整的 3 分钟大片），彻底杜绝权限限流与账号风控。

#### 3.3 生产前风控门禁：提示词安全审计 (Prompt Safety Gate)
- **执行规则**：所有提示词必须经过 [`docs/prompt_safety_policy.md`](prompt_safety_policy.md) 审查。
- **硬禁词拦截**：严禁出现 `throat`, `neck`, `choke`, `strangle`, `syringe`, `inject`, `narcotic`, `cliff edge`, `baby in chains` 等伤害或成瘾描写。
- **安全版本归档**：审查改写后的提示词保存在 `projects/<slug>/03_gemini_prompts/clips_safe/`。视频生成时**直接顺序调用 `clips_safe/`**（包含 1–18 镜全集自闭环，杜绝回退）。

#### 3.4 视频参数契约与无感落盘规范
- **视频标准参数**：
  - `Aspect Ratio`：4:3 横屏（默认推荐，Academy 经典故事比例）/ 16:9 横屏 / 9:16 竖屏
  - `Duration`：每片段精确 10 秒
  - `Frame Rate`：24fps
  - `Resolution`：720p（平衡质感与生成速度）
- **无感 Base64 提取与落盘**：
  - **严禁触发原生下载对话框**（避免阻塞自动化命令行）。
  - 生成完成后，运行：
    ```powershell
    python scripts/download_clip.py --session <session_id> --filename clip_XX.mp4 --project <slug>
    ```
  - 脚本自动通过 JavaScript 注入将页面 `<video>` 元素的 `blob:` 或带签名的资源直转 Base64 写入 `04_raw_clips/clip_XX.mp4`，并同步更新 `meta.json`。

---

### 4. 字幕处理与视频拼接 (Post-Production & Subtitle Embedding)
- **依赖 Skill 项目内路径**：
  `./skills/embed-subtitles`
- **重点读取文件**：
  - `SKILL.md`（FFmpeg 字幕压制参数、样式控制、RTL 自动检测修复）
- **核心执行规则**：
  1. **无缝拼接**：运行 `python scripts/concat_clips.py --project <slug>`（FFmpeg），自动对目标项目的 `04_raw_clips/` 中的所有片段按序无损拼接，生成 `06_final_video/stitched_raw.mp4`。
  2. **时间轴对齐**：在目标项目的 `05_subtitles/` 生成双语字幕（推荐文件名 `narration.bilingual.srt`，单文件内含"英文行 + 中文对照行"）。
  3. **移动端字幕规范（实战经验，2026-09 定稿）**：
     - **安全区（最重要）**：抖音/小红书的底部标题、账号信息与右侧按钮会遮挡画面下方约 25% 区域。字幕必须上移到**画面 55%–75% 高度区间**：720×1280 竖屏对应 `--margin 350`
     - **字号**：`--font-size 36`（720×1280 竖屏）；22/30 在移动端均偏小，勿用
     - **拆条原则**：长台词必须按语速拆成 **3–4 秒/条**的短句，每条英文不超过一行、中文不超过一行；用户没有耐心读长文本
     - **中文字体**：必须指定 CJK 字体，如 `--font-name "Microsoft YaHei"`，否则中文可能渲染为方框
     - **PlayRes 铁律**：libass 默认按 384×288 画布计算字号，竖屏视频会放大约 4 倍导致字幕铺满全屏；`embed_subtitles.py` 已内置 ffprobe 探测并按视频分辨率自动设置 `PlayResX/PlayResY`，不要绕过
  4. **压制生成成片**：运行 `python scripts/embed_subtitles.py --project <slug> --font-name "Microsoft YaHei"` 将字幕硬编码烧录进成片，保存至 `06_final_video/final_subtitled.mp4`。

---

## 二、项目目录文件职责总表

| 目录/文件 | 责任角色 | 格式要求 | 状态流转 |
|---|---|---|---|
| `projects/<slug>/01_research/research_summary.md` | 资料检索 Agent | Markdown 结构化研究报告 | 收集整理 → 确认事实源 |
| `projects/<slug>/02_director_proposal/proposal_phase_a.md` | 导演 Agent | 完整 Phase A 提案（含18行分镜表） | 草稿 → **用户审核通过** |
| `projects/<slug>/03_gemini_prompts/prompts_all.md` | 编剧/Prompt Agent | 18条独立英文 Prompt + 拼接指南 | 仅在 Phase A 确认后生成 |
| `projects/<slug>/03_gemini_prompts/_legacy_*/` | 编剧/Prompt Agent | 历史风格与旧画幅提示词 | 隔离归档 |
| `projects/<slug>/03_gemini_prompts/clips_safe/prompt_01~18.txt` | 安全审查 Agent | 完备 18 镜 Style 2B 4:3 生产提示词 | **唯一生产目录** |
| `projects/<slug>/04_raw_clips/clip_01~18.mp4` | 浏览器生成 Agent | 720p 4:3/9:16 MP4 视频，每个约10秒 | Google Flow 提取落盘（Git忽略） |
| `projects/<slug>/05_subtitles/narration.en.srt` | 字幕处理 Agent | 严格符合 SRT 格式标准 | 基于实际时间轴对齐 |
| `projects/<slug>/06_final_video/final_subtitled.mp4` | 后期合成脚本/Agent | 最终交付成品视频 | 拼接+压制成片（Git忽略） |
| `projects/<slug>/meta.json` | 工程管理 Agent | JSON 结构化元数据 | 记录画幅、风格、已生成片段列表 |

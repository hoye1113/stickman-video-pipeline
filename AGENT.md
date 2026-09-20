# AGENT 指南：火柴人视频矩阵化全自动生产工作流 (Agent Handover Guide)

> **目标**：本文档为后续接手本项目的任何 AI Agent（或人类工程师）提供完整的项目背景、环境配置、多项目矩阵管理架构、避坑经验与自动化生产操作手册。遵循本手册可实现 100% 零冲突、零覆盖的无人值守连续生产。

---

## 1. 架构总览：多项目矩阵架构 (Multi-Project Architecture)

为了防止不同主题的视频相互覆盖，本项目采用**内容矩阵工程模式**：
- 根目录为通用的**生产引擎与工具链中心**（包含通用脚本、共享 Skills、全局文档）；
- 每一个独立视频主题作为一个独立工程，存放在 `projects/<project_slug>/` 目录下；
- 每个子工程内部拥有专属的 `01_` 至 `06_` 阶段流转目录与 `meta.json` 元数据。

```text
stickman-videos/
├── projects/                                    # 视频项目矩阵目录
│   ├── _template/                              # 新建工程模板（包含标准 .gitkeep 与结构）
│   │   ├── 01_research/.gitkeep
│   │   ├── 02_director_proposal/.gitkeep
│   │   ├── 03_gemini_prompts/clips/.gitkeep
│   │   ├── 04_raw_clips/.gitkeep
│   │   ├── 05_subtitles/.gitkeep
│   │   ├── 06_final_video/.gitkeep
│   │   └── meta.json
│   │
│   ├── 001_betrayal_and_split_soul/            # 【第1期：背叛与撕裂】
│   │   ├── 01_research/ (research_summary.md)
│   │   ├── 02_director_proposal/ (proposal_phase_a.md)
│   │   ├── 03_gemini_prompts/ (prompts_all.md, clips/)
│   │   ├── 04_raw_clips/ (clip_01.mp4 ...)
│   │   ├── 05_subtitles/
│   │   ├── 06_final_video/
│   │   └── meta.json                           # 记录画幅、风格、已生成片段列表
│   │
│   └── 002_future_topic/                       # 【未来第2期、第N期，互不影响】
│       └── ...
│
├── scripts/                                    # 参数化通用引擎脚本
│   ├── new_project.py                          # 一键新建项目脚手架
│   ├── download_clip.py                        # 支持 --project 目标路径
│   ├── split_prompts.py                        # 支持 --project 目标路径
│   ├── concat_clips.py                         # 支持 --project 目标路径
│   └── embed_subtitles.py                      # 支持 --project 目标路径
│
├── skills/                                     # 全局共享 Skills 规范
├── docs/                                       # 核心技术规范与工作流文档
├── .gitignore                                  # 跨项目过滤所有 mp4/webm/mov
└── AGENT.md                                    # 多项目交接总纲
```

---

## 2. 账号与运行平台（严禁走 API 付费接口）

- **用户账号**：`hoyework@gmail.com`（已订阅 **Google One AI Premium PRO** 会员）。
- **零成本方案**：**严禁调用 Google Cloud 付费 API**（用户无 API 额度）。所有视频生成**必须通过浏览器自动化**在 Google AI Studio 网页版前端执行：
  - **URL**：`https://aistudio.google.com/prompts/new_chat?model=gemini-omni-1.1-flash`
  - **模型名称**：`Gemini Omni 1.1 Flash` (`gemini-omni-1.1-flash`)

---

## 3. 浏览器自动化环境 (`bsk` 工具链)

项目依赖本地安装的 `bsk` 浏览器自动化 CLI（版本 0.3.0）：
- **CLI 路径**：`C:\Users\38788\.local\bin\bsk.exe`
- **通信协议**：通过 Chrome 扩展与本地前台打开的 Google Chrome 通信。

### 核心操作守则与命令模式：
1. **环境变量**：所有 PowerShell 命令必须加上 `$env:BSK_AUTO_START="0"`，防止沙箱环境下触发守护进程启动冲突：
   ```powershell
   $env:BSK_AUTO_START="0"; bsk <command>
   ```
2. **会话管理**：
   - 检查现有会话：`bsk session list --json`
   - 若返回空列表（会话超时断开），启动新会话：`bsk session start --json`（获取 `session_id`，如 `uwym`）。
3. **标签页借用（Borrow）原则**：
   - 列出标签页：`bsk tab list --session <session_id> --json`
   - 借用 AI Studio 标签：`bsk tab borrow <tab_id> --session <session_id>`
   - **重要原则**：一旦借用标签，**绝对不要主动调用 `bsk tab return` 归还**，保持页面常驻于 Agent Window 中，以便持续多轮交互。

---

## 4. Google AI Studio 核心避坑指南 (Hard-won Experience)

在实际调用中，我们踩平了以下所有关键技术坑点，接手的 Agent 必须牢记：

### 坑点 1：Google Drive 强制绑定（Temporary Chat 不支持视频生成）
- **现象**：当第一次点击 `Run Ctrl` 时，AI Studio 会弹出模态框：
  > *"Temporary Chat is not supported: Video features are only available when saving conversations to Google Drive. Enable Google Drive to continue."*
- **原因**：Google AI Studio 生成视频的媒体文件体积较大，必须持久化到用户的个人 Google Drive。
- **解决方式**：
  - 点击弹出框的 `Allow Drive access`，完成一次性 Google OAuth 授权；
  - 授权完成后，当前会话自动保存为一个具有独立 ID 的 Prompt（如当前首个视频会话已持久化为：`https://aistudio.google.com/prompts/1FIfddPPJOLnI8r7BTnibSam0VJBBPxPY`，标题自动命名为 `Betrayal and the Fractured Soul`）；
  - **后续片段生成可直接在此持久化 Prompt 中连续对话**，避免重新授权。

### 坑点 2：右侧参数面板配置（每次开新会话必须检查）
- `Aspect ratio`：点击下拉框，从默认的 `Auto` 改选为 `9:16`。
- `Video duration`：保持滑块/数字框为 `10` 秒。
- `Resolution`：默认往往是 `360p`，**必须手动下拉选中 `720p`**（若算力允许可设 1080p，720p 出片最稳定快捷且画质极佳）。
- `Frame rate`：锁死 `24fps`。

### 坑点 3：OS 级保存文件弹窗死锁 $\to$ 采用 DOM Base64 无损直提
- **痛点**：如果使用浏览器常规的“点击下载”按钮，会触发操作系统的 Windows 文件保存对话框，阻塞 Agent 命令行执行。
- **终极解决方案**：AI Studio 生成完毕后，页面 DOM 会渲染一个 `<video>` 标签，其 `src` 为浏览器内存中的 `blob:https://aistudio.google.com/...`。脚本会自动选取页面中**最新的 blob 视频**（跳过历史片段），避免在持久化长对话中误提取旧片段。
- 我们编写了自动化提取脚本 [`scripts/download_clip.py`](file:///d:/workSpace/git_clone_test/hoye-git/stickman-videos/scripts/download_clip.py)：
  ```powershell
  python scripts/download_clip.py --session <session_id> --filename clip_01.mp4 --project <project_slug>
  ```
  该脚本通过 JavaScript 将 blob 读取为 base64，直接由 Python 在本地写盘存入目标项目的 `04_raw_clips/`，并自动更新该项目的 `meta.json`。**速度极快（~1秒）、零弹窗、零死锁、100% 可靠**。

---

## 5. 新建与管理视频项目 (Multi-Project Lifecycle)

### A. 一键创建新视频项目
当需要制作一个新主题时，运行：
```powershell
python scripts/new_project.py 002_social_anxiety --title-zh "克服社交焦虑的心理法则" --title-en "Mastering Social Anxiety" --ratio 9:16 --style "Style 1 Dark"
```
系统会自动基于 `projects/_template/` 初始化完整的 6 大阶段空目录，并生成规范的 `meta.json`。

> **项目定位规则**：所有脚本通过 `scripts/project_store.py` 解析项目。当 `projects/` 下存在多个项目时，必须显式传 `--project <slug>`，否则直接报错并列出候选项目（不会静默选中或回落到某个固定项目）；仅当项目唯一时可省略 `--project`。

### B. 在指定项目中拆分提示词
在项目的 `03_gemini_prompts/prompts_all.md` 写好后，运行：
```powershell
python scripts/split_prompts.py --project 001_betrayal_and_split_soul
```
会自动将该项目汇总的 18 条 Prompt 拆分为 `clips/prompt_01.txt` ~ `prompt_18.txt`。

### C. 批量生成与提取视频片段
对于项目中的片段 `N`（如 `02`）：
1. 观察输入框与 Run 按钮 ref；
2. 注入提示词：
   ```powershell
   $prompt_text = Get-Content "projects/001_betrayal_and_split_soul/03_gemini_prompts/clips/prompt_02.txt" -Raw
   $env:BSK_AUTO_START="0"; bsk fill --ref "@e42" --value "$prompt_text" --session <session_id>
   ```
3. 点击 Run 按钮：
   ```powershell
   $env:BSK_AUTO_START="0"; bsk click --ref "@e47" --session <session_id>
   ```
4. 渲染完成后提取落盘：
   ```powershell
   python scripts/download_clip.py --session <session_id> --filename clip_02.mp4 --project 001_betrayal_and_split_soul
   ```

### D. 视频合并与字幕烧录
全部片段生成完毕后：
1. **拼接为完整成片**：
   ```powershell
   python scripts/concat_clips.py --project 001_betrayal_and_split_soul
   ```
   （自动寻找 `04_raw_clips` 内的所有片段，合并输出到 `06_final_video/stitched_raw.mp4`）
2. **烧录字幕**：
   ```powershell
   python scripts/embed_subtitles.py --project 001_betrayal_and_split_soul
   ```
   （自动寻找该项目 `05_subtitles` 下的 SRT 字幕，输出最终带有双语字号边距的 `final_subtitled.mp4`）

---

## 6. 核心自动化脚本清单

| 脚本文件 | 作用与用法 |
|---|---|
| [`scripts/project_store.py`](file:///d:/workSpace/git_clone_test/hoye-git/stickman-videos/scripts/project_store.py) | **核心模块**：所有脚本共用的项目解析、meta.json 读写与阶段路径推导；多项目时必须显式定位 |
| [`scripts/new_project.py`](file:///d:/workSpace/git_clone_test/hoye-git/stickman-videos/scripts/new_project.py) | **一键新建项目**：从 `_template` 复制初始化新项目目录与 `meta.json` |
| [`scripts/split_prompts.py`](file:///d:/workSpace/git_clone_test/hoye-git/stickman-videos/scripts/split_prompts.py) | 拆分指定项目下的 `prompts_all.md` 为 18 个独立的 `prompt_01.txt` ~ `prompt_18.txt` |
| [`scripts/download_clip.py`](file:///d:/workSpace/git_clone_test/hoye-git/stickman-videos/scripts/download_clip.py) | **核心提取脚本**：无弹窗将浏览器当前的 Blob 视频以 Base64 提取保存为目标项目的 `04_raw_clips/clip_XX.mp4`，并自动更新 `meta.json` |
| [`scripts/concat_clips.py`](file:///d:/workSpace/git_clone_test/hoye-git/stickman-videos/scripts/concat_clips.py) | 批量调用 FFmpeg concat 将目标项目的所有片段拼接为 3 分钟成片，带自动 fallback 转码保障 |
| [`scripts/embed_subtitles.py`](file:///d:/workSpace/git_clone_test/hoye-git/stickman-videos/scripts/embed_subtitles.py) | 将 SRT 字幕无损压制到目标项目的成片视频中，内置 RTL 双向文本与中文换行支持 |

---

## 7. 常见紧急排查 (Troubleshooting)

- **Q: 为什么 `bsk` 显示 `session not registered or already stopped`？**  
  **A**: 会话闲置超过几分钟会自动停止。只需运行 `bsk session start --json` 创建新会话，然后重新借用（borrow）AI Studio 标签即可。
- **Q: 为什么提示词输入后 Run 按钮仍然是灰色？**  
  **A**: 确保 `bsk fill` 正确触发表单变更事件。如果变灰，可发送一次空格或用 JavaScript 触发 `input` / `change` 事件。
- **Q: 生成的视频画面不小心被截断了？**  
  **A**: 提示词已注入 `compose vertically with interface-safe margins, central 20% to 80%`，确保主体都在竖屏正中。

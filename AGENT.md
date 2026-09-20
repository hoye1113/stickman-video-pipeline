# AGENT 指南：火柴人视频矩阵化全自动生产工作流 (Agent Handover Guide)

> **目标**：本文档为后续接手本项目的任何 AI Agent（或人类工程师）提供完整的战略背景、核心价值目标、Google Flow 原生生成策略、提示词安全风控、多项目矩阵管理架构与自动化生产操作 SOP。遵循本手册可实现 100% 零冲突、零覆盖、零封禁的无人值守连续生产。

---

## 1. 项目核心背景与战略目标 (Why This Exists)

### 1.1 核心驱动力与自媒体闭环哲学
本项目源自推友 **“疯狂的烤妹儿 🩵”**（`@CrazyKaomei`）提出的 **“一人可落地的「AI + 自媒体」最小阻力路径”** 理念：
- **痛点**：传统 AIGC 视频制作成本高昂（Midjourney 每月上百，Runway/Kling 每月大几百），高心理与资金试错成本导致创作者在斤斤计较中磨灭了所有灵感；
- **破局**：借助极低成本的 Google One AI Premium PRO 会员（如 18 个月活动），打通了**零边际成本的视频生产通道**；
- **核心认知**：
  > **“你占到了一个入口，不等于你拥有了作品。用不起来的便宜，依然是昂贵的浪费。别把会员当主角，它只是一声开门声。真正要做的是打磨出一套属于你自己的内容生产闭环。”**
- **本项目的根本使命**：将这套零边际成本的生成通道，通过 **脚本自动化 + 提示词工业契约 + 多项目矩阵管理**，沉淀为一套可全自动量产 3 分钟高质量科普短视频的标准化流水线。

---

## 2. 账号体系与 Google Flow 生产架构 (Platform Architecture)

- **用户账号**：`hoyework@gmail.com`（已订阅 **Google One AI Premium PRO** 会员，拥有官方每月 1,000 点视频积分与 Gemini 完整权限）。
- **零成本原则**：**严禁调用 Google Cloud 付费 API**（无 API 额度）。所有图文与视频生成均通过浏览器自动化在 **Google Flow 前端页面**完成。

### 核心生产平台：Google Flow (`https://labs.google/fx/tools/flow`)

```text
┌────────────────────────────────────────────────────────────────────────┐
│               Google One AI Premium PRO (hoyework@gmail.com)           │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ 浏览器自动化 (bsk)
                                    ▼
       【唯一核心生产平台：Google Flow (Storyboard Studio)】
                   https://labs.google/fx/tools/flow
    ──────────────────────────────────────────────────────────────
    • Storyboard Studio：18 镜头分镜卡片流，独立渲染绝无多轮干扰
    • 首尾帧控制 (First & Last Frame Control)：实现物理级平滑过渡
    • Nano Banana 2 (0 Credits)：零积分无限量生成 4 张关键帧测角色
    • 官方消费级积分：每段 10s 约 15 点，月 1000 点可产出 60+ 镜头
    • 纯净合规：无开发者接口 403 限流风险，无单会话超长累加崩溃
```

### 为什么选择 Google Flow 作为唯一生产平台？
1. **Storyboard Studio 分镜架构**：Flow 原生提供故事板镜头卡片管理，与我们 Phase A 的 18 段分镜结构 1:1 完美映射；各卡片独立渲染，彻底根绝单会话连续生成时长累加（超 30s 崩溃）的问题；
2. **首尾帧控制 (First & Last Frame Control)**：可将前一段视频的尾帧作为下一段的起始帧，实现模型级平滑衔接，彻底根绝纯文本盲猜导致的画面突变；
3. **Nano Banana 2 免费垫底 (0 积分)**：在扣减视频积分前，可先用 0 积分无限量生成关键帧、测试角色一致性（每次出 4 张），定稿后再跑视频，大幅降低废片率；
4. **官方配额稳定合规**：每段 10 秒 720p 视频仅消耗约 15 积分，每月 1,000 积分足以产出 60+ 条片段（即 3~4 条完整的 3 分钟大片），走的是官方会员消费级产品通道，杜绝权限拦截风险。

---

## 3. 视觉风格选型与分支管理

本项目支持并维护两种主流视觉体系：

| 风格编号 | 风格名称 | 核心特征与适用场景 | 归档与现状 |
|---|---|---|---|
| **Style 1** | 极简黑底高反差 (Dark Minimalist) | 纯黑画布、纯白极简线条火柴人、中粗线宽、空心圆头、无五官服装；辅以三色高饱和隐喻色（暗红、冰紫、冷金）。视觉冲击极强，适合深度心理学剖析。 | 首批生成的 Style 1 素材已安全归档至 `projects/<slug>/04_raw_clips/_style1_archive/`，作为历史资产备份。 |
| **Style 2B** | 全彩电影叙事 (Cinematic Story) | 电影级光影环境（暖光卧室、雨夜车灯、昏黄窗台）、角色锁定（红色冷帽 + 黄色T恤 + 黑色四肢 + 无面部细节）、电影体积光与景深质感。代入感更强。 | **当前第一期项目（001_betrayal_and_split_soul）采用的主力风格**。旧平台测试片段已归档至 `_legacy_1min_archive/`，项目状态重置就绪，由 Google Flow 从 Clip 01 统一跑通。 |

---

### 4. 提示词安全风控规范 (Prompt Safety Policy)

> 详细规定见 [`docs/prompt_safety_policy.md`](file:///d:/workSpace/git_clone_test/hoye-git/stickman-videos/docs/prompt_safety_policy.md)。所有新 Prompt 必须在交付生成前执行安全自检！

视频生成平台（Google Flow / Veo / Gemini）具有严格的安全过滤机制。实测表明：写实性的危险、伤害、药物词汇会直接触发拒绝拦截。

### 硬禁词与安全替换标准表：
| 违禁类别 | 禁止出现的词汇 (Hard Forbidden) | 安全替代表达 (Safe Substitutions) |
|---|---|---|
| **身体伤害** | `throat`, `neck`, `strangle`, `choke`, `suffocate`, `gasp`, 勒颈, 窒息, 流血 | `freeze`, `stiffen`, `light dims`, `coiling around shoulders/arms` |
| **危险工具** | `rope/lasso around throat`, `whip snap`, `weapon`, `stab` | `glowing ribbon pulling backward`, `sharp snap` |
| **成瘾物** | `narcotic`, `drug`, `syringe`, `needle`, `inject`, `cocktail`, `wine` | `painkiller`, `illusion`, `glowing beam/probe of light`, `tilted glass of red liquid` |
| **自伤/危险** | `car dangling over cliff`, `plunge into abyss`, `fall from heights` | `car stopping at white warning line`, `drift into deep darkness` |
| **未成年人** | `baby/infant/child` 与哭泣、锁链、束缚组合 | `small fragile grey silhouette wrapped in heavy cool violet threads` |
| **色彩与技术** | 十六进制色彩 `#FF0000`、含危险词的颜色名（如 `saturated danger red`） | **普通描述性颜色词**：`vivid red`, `cool violet`, `warm gold` |

- **唯一生产目录**：经安全审查与 4:3 适配的 Prompt 存放于 `03_gemini_prompts/clips_safe/`；生成时直接调用 `clips_safe/` 中的 18 镜全量独立文件（自闭环，严禁跨目录回退）。

---

## 5. 项目矩阵目录架构 (Multi-Project Architecture)

所有视频项目均存放在 `projects/<slug>/`，各个主题物理隔离，杜绝覆盖：

```text
stickman-videos/
├── projects/                                    # 视频项目矩阵目录
│   ├── _template/                              # 新建工程模板（默认 4:3 横版与 Style 2B）
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
│   │   ├── 02_director_proposal/ (Style 2B 4:3 横版分镜预案)
│   │   ├── 03_gemini_prompts/ (prompts_all.md, clips_safe/ 18镜全集, _legacy_*)
│   │   ├── 04_raw_clips/ (_legacy_1min_archive/, _style1_archive/)
│   │   ├── 05_subtitles/ (narration.bilingual.srt, _legacy_1min_archive/)
│   │   ├── 06_final_video/ (_legacy_1min_archive/)
│   │   └── meta.json                           # 记录 4:3 横版、Style 2B、已生成片段列表与状态
│   │
│   └── 002_future_topic/                       # 【未来第2期、第N期，互不影响】
│       └── ...
│
├── scripts/                                    # 参数化通用引擎脚本
│   ├── new_project.py                          # 一键新建项目脚手架
│   ├── download_clip.py                        # 支持 --project / --out / --tab-id 无感提取
│   ├── split_prompts.py                        # 支持 --project / --md / --out-dir 拆分
│   ├── concat_clips.py                         # 支持 --project 视频拼接
│   └── embed_subtitles.py                      # 支持 --project 字幕压制
│
├── skills/                                     # 全局共享 Skills 规范
├── docs/                                       # 规范与安全风控文档
│   ├── prompt_safety_policy.md                 # 提示词安全风控手册与替换表
│   ├── workflow_spec.md                        # 完整业务规范
│   └── lessons_learned.md                      # ★ 跨项目经验教训总纲（配额/bsk/水印/字幕/备份）
├── .gitignore                                  # 跨项目过滤所有 mp4/webm/mov
└── AGENT.md                                    # 本交接总纲
```

---

## 6. 浏览器自动化与实战避坑指南 (`bsk` 工具链)

项目通过本地 `bsk` CLI（版本 0.3.0）控制已登录 Chrome：
- **CLI 路径**：`C:\Users\38788\.local\bin\bsk.exe`
- **环境变量**：所有 PowerShell 命令必须加上 `$env:BSK_AUTO_START="0"`：
  ```powershell
  $env:BSK_AUTO_START="0"; bsk <command>
  ```
- **会话机制**：`bsk session start --json` 获取 `session_id`。一旦借用标签，**切勿主动 return 归还**，保持页面常驻在 Agent Window。

### 实战硬核避坑总结 (Hard-won Experience)：

1. **坑点 1：OS 级文件保存对话框死锁**
   - 严禁触发点击浏览器的原生下载按钮（会导致 Windows 保存弹窗阻塞命令行）。
   - **统统使用 [`scripts/download_clip.py`](file:///d:/workSpace/git_clone_test/hoye-git/stickman-videos/scripts/download_clip.py)**：通过 JavaScript DOM 注入直接将 `<video>` 的 `blob:` 或带凭证的签名 URL 转为 Base64 写盘，1 秒无感落盘，零死锁。
2. **坑点 2：Nano Banana 2 零积分预检锁角色**
   - 不要在未确认画面构图前直接消耗 15 积分跑视频。利用 Flow 提供的 Nano Banana 2 免费生图（每次出 4 张），先校验火柴人的服装（红色冷帽 + 黄色T恤）与光影，确认没崩后再点击生成视频。
3. **坑点 3：首尾帧衔接防止画面突变**
   - 充分利用 Flow 的 **First & Last Frame Control** 特性：将前一个片段生成的最后关键帧作为下一个片段的起始帧输入，实现物理级平滑过渡，彻底解决人物姿态跳帧。
4. **坑点 4：页面分镜卡片独立性**
   - Flow 的 Storyboard Studio 采用镜头卡片流，每张卡片独立渲染 10 秒片段，避免在单会话内连续多轮延长导致超时报错。

---

## 7. 端到端生产操作 SOP (Step-by-Step Production SOP)

### Step 1: 一键新建主题项目
```powershell
python scripts/new_project.py 002_social_anxiety --title-zh "克服社交焦虑" --title-en "Mastering Social Anxiety" --ratio 4:3 --style "Style 2B (Cinematic Story)"
```

### Step 2: 资料检索与 Phase A 导演预案
1. 梳理心理学科学机制，保存在 `projects/<slug>/01_research/research_summary.md`；
2. 按照三幕式 18 段结构编写分镜表（画幅首选 `4:3` 横屏，兼顾 B站/知乎/微信公号/YouTube），保存至 `projects/<slug>/02_director_proposal/proposal_phase_a.md`；
3. **【门禁】在此必须暂停，等待人类用户审核批准分镜方案！**

### Step 3: Phase B 提示词生成与安全扫描
1. 编写 18 条生产级英文提示词（遵循零文字契约、4:3 横屏构图声明、角色防形变锁、动效三拍点）；
2. 依据 [`docs/prompt_safety_policy.md`](file:///d:/workSpace/git_clone_test/hoye-git/stickman-videos/docs/prompt_safety_policy.md) 排除敏感词，改写后生成完备的 18 镜全集置于 `clips_safe/`；
3. 主控文档 `prompts_all.md` 与 `prompts_all_2b.md` 保持与 `clips_safe/` 严格一致，严禁跨目录回退调用旧文件。

### Step 4: 视频生成与 Base64 提取落盘
- **在 Google Flow (Storyboard Studio) 中**：
  1. 设定 `4:3` 横屏（若页面无 4:3 选项则选横版 16:9，由后续脚本自动居中裁切）、`10s`、`720p`；
  2. 填入提示词，（可选前帧输入），点击生成；
  3. 待视频加载完成后，运行提取脚本：
     ```powershell
     python scripts/download_clip.py --session <session_id> --filename clip_01.mp4 --project <slug>
     ```
  4. 重复完成 18 个片段的提取（已生成的片段会自动同步进 `meta.json`）。

### Step 5: 视频无缝合并与字幕压制成片
```powershell
# 1. FFmpeg 18 段视频合并 (生成 stitched_raw.mp4，可选 --crop-ratio 4:3 居中裁切)
python scripts/concat_clips.py --project <slug> --crop-ratio 4:3

# 2. 对齐字幕并硬编码压制成片 (生成 final_subtitled.mp4)
python scripts/embed_subtitles.py --project <slug>
```

---

## 8. 核心自动化脚本清单与参数速查

| 脚本文件 | 核心参数与示例 | 功能作用 |
|---|---|---|
| [`scripts/new_project.py`](file:///d:/workSpace/git_clone_test/hoye-git/stickman-videos/scripts/new_project.py) | `<name> [--title-zh] [--title-en] [--ratio {4:3,16:9,9:16,1:1}] [--style]` | 自动克隆 `_template` 并生成专属 `meta.json`（默认 4:3 与 Style 2B） |
| [`scripts/split_prompts.py`](file:///d:/workSpace/git_clone_test/hoye-git/stickman-videos/scripts/split_prompts.py) | `[--project <name>] [--md <filename>] [--out-dir <dir>]` | 将提示词总包一键拆解为 `prompt_01.txt` ~ `18.txt` |
| [`scripts/download_clip.py`](file:///d:/workSpace/git_clone_test/hoye-git/stickman-videos/scripts/download_clip.py) | `[--session <id>] [--filename <name>] [--project <slug>] [--out <path>]` | 无弹窗 Base64 提取当前页面最新视频并更新 `meta.json` |
| [`scripts/concat_clips.py`](file:///d:/workSpace/git_clone_test/hoye-git/stickman-videos/scripts/concat_clips.py) | `[--project <slug>] [--output <filename>] [--crop-ratio {4:3,16:9,1:1}]` | 自动排序拼接 `04_raw_clips` 内的所有视频，支持 4:3 居中无损裁切 |
| [`scripts/embed_subtitles.py`](file:///d:/workSpace/git_clone_test/hoye-git/stickman-videos/scripts/embed_subtitles.py) | `[--project <slug>] [-i <video>] [-s <srt>] [-o <out>] [--font-size] [--margin]` | 烧录压制高清双语字幕，内置 RTL 自动修复与画幅探针：**横屏 4:3/16:9 默认 margin 50、字号 26；竖屏 9:16 默认 margin 350、字号 36**；内置 ffprobe 自动设置 PlayRes（防止字幕放大铺屏） |

---

## 9. 系列经验索引

- **跨项目通用经验教训总纲**（平台配额、多账号、bsk 避坑、水印去除、字幕规范、备份纪律、流程铁律）：[`docs/lessons_learned.md`](file:///d:/workSpace/git_clone_test/hoye-git/stickman-videos/docs/lessons_learned.md)
- **提示词安全风控手册**（危险词禁令与安全替换表）：[`docs/prompt_safety_policy.md`](file:///d:/workSpace/git_clone_test/hoye-git/stickman-videos/docs/prompt_safety_policy.md)
- **完整业务规范**（各阶段任务、门禁与目录职责）：[`docs/workflow_spec.md`](file:///d:/workSpace/git_clone_test/hoye-git/stickman-videos/docs/workflow_spec.md)

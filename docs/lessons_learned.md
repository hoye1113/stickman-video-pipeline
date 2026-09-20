# 经验教训与避坑总纲 (Lessons Learned & Operational Wisdom)

> **版本演进说明**：
> - **v1.0 (历史探索期)**：基于 Gemini 网页版 / AI Studio 的 1 分钟短版跑通测试，已沉淀归档至 `_legacy_1min_archive/`。
> - **v2.0 (当前生产标准)**：全面收敛并升级至 **Google Flow (Storyboard Studio)** 原生 3 分钟工业化生产线（18 个镜头，每段 10s，首尾帧物理过渡，3 个 Pro 账号 3,000 积分轮动）。

---

## 一、平台与配额认知演进（从旧平台踩坑到 Flow 工业化）

1. **彻底告别旧平台的两大硬伤**：
   - **旧伤 1（单会话自动累加超时）**：此前在单对话连续生图，模型会自动延长为 20s/30s 母片，超出 30s 必报 `Internal Error`。在 Google Flow 中，**每个分镜卡片（Shot Card）完全独立渲染**，彻底根除了上下文累加崩溃。
   - **旧伤 2（账号级 403 限流）**：AI Studio 开发者接口频发 `CreateInteractionStream 403`。Google Flow 直接走 Google One AI Pro 官方消费级产品通道，合规稳定，零 403 风险。
2. **Google Flow 官方权威扣费与配额铁律**：
   - **Pro 账号月度配额**：每个账号每月享有 **1,000 官方积分**（每月刷新，当月不结转）。3 个账号共 **3,000 积分/月**。
   - **生成单价**：`Omni 1.1 Flash (720p / 10s)` 精确扣除 **15 积分/段**；`Veo 3.1 Lite (10s)` 扣除 **10 积分/段**。
   - **防损神器**：**Nano Banana 2 免费生图 (0 积分)**。必须在生成视频前先出 4 张关键帧校验火柴人服装与光影，确认不崩后再点生成，实现零试错浪费。
3. **水印与成片画质**：
   - Google Flow 走官方 Pro 权益，素材原生纯净；若存在角标水印，可用 `ffmpeg -i in.mp4 -vf "delogo=x=570:y=1125:w=62:h=80" ...` 进行无损去除。

## 二、多账号与 bsk 浏览器自动化实战

4. **bsk 识别的是浏览器实例 (instance_id)，而非 Google 账号**：
   - 正确姿势：为每个 Google Pro 会员账号建立独立的 Chrome 配置文件（Profile），并各自安装 bsk 扩展；
   - 切换生产时，通过 `bsk browsers` 获取 `instance_id`，使用 `bsk session start --browser <instance_id>` 锁定生产环境。
5. **严禁在同一 Chrome 配置文件中混登多个 Google 账号**：
   - 避免 `/u/0`、`/u/1` 会话污染导致积分扣错账号。
6. **会话闲置与标签管理**：
   - bsk 会话闲置超时后报 `session not registered` 属正常安全机制；重新运行 `session start --browser <id>` 即可无缝连回。
   - 借用标签时切勿主动 `return`，保持常驻在 Agent Window。
7. **首次进入协议弹窗规避**：
   - 新账号首次进入 Google Flow 会弹出《体验并参与塑造 AI 创意工具》弹窗，无需勾选营销邮件和调研，直接点击“下一步”即可入驻控制台。

## 三、生成策略（省配额的关键）
## 三、生成策略（Google Flow 工业化高品质秘诀）

10. **首尾帧连续性控制 (First & Last Frame Control) 是平滑过渡的核心**：
    - 在 Flow 中，将前一段生成的尾帧作为下一段的起始帧（Start Frame）喂给模型；
    - 模型无需纯靠文本盲猜动作与构图，从根源消灭人物姿态、服装和光影的漂移跳变。
11. **单片段标准锁定 10 秒**：
    - Flow Storyboard Studio 原生采用镜头卡片流，每张卡片独立跑 10s；
    - 绝不再做 20s/30s 拼凑式提示词（容易触发拒签与画面乱码）。
12. **提示词安全净化是 100% 成功率的前提**：
    - 严格遵循 `docs/prompt_safety_policy.md`；
    - 严禁出现勒颈、针筒注射、自残深渊、毒药等具象词汇，改用光束、红丝带、警戒线等温和隐喻；
    - 被拒不会扣除积分，但需立即在 `clips_safe/` 沉淀改写版。
13. **标准产出规格**：
    - 9:16 竖屏（720×1280）、24fps、精准 10.00 秒、H.264 + AAC。
14. **每次生成完成后立即入库**：
    - 运行 `python scripts/download_clip.py --session <id> --filename clip_XX.mp4 --project <slug>`，Base64 DOM 直提，秒级落盘并自动同步进 `meta.json`。

## 四、素材管理与多项目矩阵（隔离与归档）

15. **所有 mp4/mov 视频文件严格由 `.gitignore` 跨项目全局忽略**：
    - 严禁提交大文件污染 Git 仓库。
16. **历史旧版本素材规范隔离**：
    - 旧测试片段严格归集在 `04_raw_clips/_legacy_1min_archive/` 或 `_style1_archive/`；
    - 正规生成的当前版本直接存放于 `04_raw_clips/clip_01.mp4` ~ `clip_18.mp4`，便于 `concat_clips.py` 自动化批量拼接。
17. **交付前建议做异地备份**（网盘/NAS），并保证 `meta.json` 中 `total_clips` 与实际片段数严格一致。

## 五、后期与交付（移动端标准）

18. **libass PlayRes 铁律**：设置字体前必须让 `PlayResX/PlayResY = 视频分辨率`，否则竖屏字幕按 384×288 画布被放大 ~4 倍铺满全屏（`embed_subtitles.py` 已内置 ffprobe 自动设置）。
19. **移动端字幕规范**（抖音/小红书/B站）：
    - 字幕置于画面 **55%–75% 高度**（720×1280 用 `--margin 350`），避开平台底部标题与右侧交互按钮；
    - 字号 **36**（22/30 偏小）；CJK 字体（`Microsoft YaHei`）；
    - 3 分钟视频配齐 18 段中英双语对齐字幕。
20. 成片参数基线：720×1280 / 24fps / CRF18 / AAC 192k；拼接优先 `-c copy`，失败自动重编码。

## 六、流程编排铁律（任何 Agent 直接照做）

1. **新建工程**：`python scripts/new_project.py <slug> ...`（自动建立 6 大阶段目录与标准模板）。
2. **Phase A 预案**：编写 18 段三幕式分镜（`02_director_proposal/proposal_phase_a.md`）→ **【门禁】停止并请求人类批准**。
3. **Phase B 提示词**：编写 18 条生产 Prompt → 经过 `prompt_safety_policy.md` 自检净化 → `split_prompts.py` 拆解为 `clips_2b/` 与 `clips_safe/`。
4. **Google Flow 连续生产**：
   - 确认 Chrome 实例 ID（`bsk browsers`）；
   - 使用 Nano Banana 2 免费生图锁定火柴人服装与光影；
   - 在 Storyboard Studio 中依次生成 18 张卡片，传递前一卡片尾帧为后一卡片起始帧；
   - 逐段运行 `download_clip.py` 提取至 `04_raw_clips/clip_XX.mp4`。
5. **自动化后期交付**：
   - `python scripts/concat_clips.py --project <slug>`（无缝拼接 18 段生成 `stitched_raw.mp4`）；
   - 制作双语字幕 `05_subtitles/narration.bilingual.srt`；
   - `python scripts/embed_subtitles.py --project <slug>`（烧录压制成片 `final_subtitled.mp4`）。
6. **收尾同步**：确认 `meta.json` 进度完备，关闭浏览器会话。

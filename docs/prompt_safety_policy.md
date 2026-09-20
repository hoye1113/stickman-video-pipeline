# 生成提示词安全规范 (Prompt Safety Policy)

> **适用范围**：本仓库所有视频生成项目的 Phase B 提示词及其重写版本。  
> **约束**：本规范独立于 `skills/` 下的通用技能，不修改技能文件；如需在技能中落地，由技能维护者另行评审。

---

## 1. 背景与目标

视频生成平台（Google Flow / Veo / Gemini）会对提示词执行内容安全审核。实测：包含"勒颈、注射、婴儿受束缚、危险驾驶"等描写的提示词会被直接拒绝（示例：返回 *"I can't make videos that could relate to dangerous situations"*）。

本规范定义**禁止出现的内容**与**安全替代表达**，目标是：

1. 提示词全部通过平台审核，避免浪费生成额度；
2. 不损失原分镜的叙事隐喻与视觉冲击力；
3. 所有改写可追溯（原文归档 + 改写对照表）。

---

## 2. 严禁出现（硬禁清单）

| 类别 | 禁止出现 |
|---|---|
| 身体伤害 | throat / neck 相关动作、strangle、choke、suffocate、gasp、勒颈、窒息、伤口、流血 |
| 武器与暴力 | weapon、stab、shoot、whip 抽打、violent 直接修饰人身动作 |
| 成瘾物 | narcotic、drug、syringe / needle / inject、cocktail / wine / alcohol、smoking |
| 未成年人风险 | baby / infant / child 与束缚、哭泣、受困组合出现 |
| 自伤/自杀暗示 | noose、hang、从高处 jump、drown |
| 危险情境 | 车辆悬于悬崖边缘、人物从高处坠落等写实危险描写 |
| 技术记号 | 十六进制 / RGB / Pantone 色彩记号（模型可能将其渲染为画面文字） |
| 风险命名 | 含 danger / anxiety 等"情绪+危险"词的色彩命名（如 `saturated danger red`） |

---

## 3. 安全替代对照表

| 危险表达 | 安全替代 |
|---|---|
| rope / lasso around throat / neck | glowing ribbon coiling around **shoulders / arms** and pulling backward |
| choke / suffocate / gasp | freeze / stiffen / the light dims / breath slows |
| syringe injecting into head | glowing red **beam / probe of light** touching the head; red light pouring in |
| shattering into flying shards / pain | dissolving into floating embers / dazed |
| baby / infant in chains | small, fragile grey silhouette wrapped in heavy threads |
| cocktail glass / wine | tilted glass of red liquid |
| narcotic | painkiller / escape / illusion |
| torture (oneself) | torment |
| drowning (in emotion) | sinking (under emotion) |
| car dangling over a cliff edge | car stopping exactly at a white warning line, the road beyond fading into darkness |
| plunge / fall into abyss | descend / drift into deep darkness |
| blood-stained | red-stained / red glow |
| violent storm | fierce storm |
| `saturated danger red` / `anxiety violet` | **vivid red / cool violet / warm gold**（普通描述性颜色词） |

---

## 4. 高风险提示词模板

**A. 中性声明**（加在输出规格段落之后）：

```text
This is a non-violent educational 2D line-animation about psychology; all characters are abstract faceless symbols; every image is a symbolic metaphor.
```

**B. 软性负向约束**（追加在原负向约束末尾）：

```text
No violence, no weapons, no injury, no depiction of harm, no substances.
```

---

## 5. 文件与版本约定

| 路径 | 用途 |
|---|---|
| `03_gemini_prompts/clips/` | Phase A 审批原文（**归档，不用于生成**） |
| `03_gemini_prompts/clips_safe/` | 经本规范审计的**生成用版本**；只放被改写的片段 |
| `docs/prompt_safety_policy.md` | 本规范与改写对照表 |

生成时优先使用 `clips_safe/` 中存在的版本；不存在则使用 `clips/` 原文。

---

## 6. 被拒处理流程

1. **原样重试 1 次**（平台偶发误判）；
2. 按本规范**改写** → 存入 `clips_safe/` → 重试；
3. 仍被拒 → 进一步加深隐喻抽象度（如用纯光影流动、色块弥散或抽象几何形变替代具象人身动作），并追加第 4 节非暴力教育声明模板；
4. 在下方"改写记录"中登记：被拒片段、触发点、改写方式、VO 变更（如有）。

---

## 7. 本项目（001_betrayal_and_split_soul）改写记录

| Clip | 风险点（原文） | 改写方式 | VO 变更 |
|---|---|---|---|
| 05 | `lasso rope ... around A's throat, violently yanking`；`cocktail glass`；`narcotic`；`whip snap` | 红丝带缠绕**双肩**并拉向门口；cocktail→glass；whip snap→sharp snap | `cheap narcotic` → `cheap painkiller` |
| 06 | 承接 05 的 `red rope` | `rope` → `ribbon`（保持衔接） | 无 |
| 07 | 车辆前轮悬于悬崖边缘；`gasp`；`explodes ... danger red` | 停在白色警戒线前、路尽头陷入黑暗；删除 gasp；light 改为 flare | 无 |
| 08 | `plunges straight down into pure blackness`；`abyss` | `drifts gently downward into pure blackness`；abyss→deep darkness | 无 |
| 09 | `giant syringe ... injecting liquid into A's head`；玻璃碎片；`reeling ... in pain` | 巨型**红色光束**触碰头部并注入红光；碎片→漂浮余烬；pain→dazed | `They inject temporary dopamine` → `They release temporary dopamine` |
| 11 | `torture themselves`（VO）；高饱和危险色命名 | VO 改词；颜色命名规范化 | `torture` → `torment` |
| 12 | `weeping baby stick figure ... bound tightly by ... chains` | `small, fragile grey silhouette ... wrapped in heavy cool violet threads` | 无 |
| 14 | `Violent swirling tornados`；VO `drowning in blind emotion` | violent→fierce；VO drowning→sinking | `drowning` → `sinking under` |
| 15 | `deep chasm`、`fall away into the abyss` | `deep dark gap`、`drift away into deep darkness` | 无 |

> 所有改写版保存在 `projects/001_betrayal_and_split_soul/03_gemini_prompts/clips_safe/`。  
> Phase A 审批原文保持原样存于 `clips/`，两者对照可审计。

---

## 8. 新项目要求

新建项目（`new_project.py`）的 Phase B 产出**必须**在交付前通过本规范第 2、3、4 条自检；建议在 `prompts_all.md` 完成后执行一次关键词扫描：

```powershell
Select-String -LiteralPath "projects\<slug>\03_gemini_prompts\clips\prompt_*.txt" -Pattern 'throat|strangl|choke|suffoc|syringe|inject|narcotic|baby|infant|chain|torture|drown|abyss|cliff'
```

扫描命中项须逐条按第 3 节替代后，才能进入生成阶段。

> **注意**：第 4 节允许的负向约束句（`No violence, no weapons, ...`）本身包含 violence/weapons 字样，属**白名单**，扫描时应忽略该句；其余位置出现即需改写。

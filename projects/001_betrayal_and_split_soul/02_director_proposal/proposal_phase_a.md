# Phase A 修订版 01 — 风格升级为 Style 2B (Cinematic Story)

> **修订说明**：本文档替代 `proposal_phase_a.md` 中的视觉风格设定。叙事结构、三幕编排、英文 VO 与中文对照、BGM 情绪曲线**保持不变**；角色设计与环境体系由 **Style 1 Dark（纯黑画布火柴人）** 全局升级为 **Style 2B（全彩电影叙事 + 红帽黄衫角色）**。
>
> **依据**：`skills/directing-stickman-videos/references/style-catalog.md` §3 Sub-Style 2B；风格变更按 SKILL.md 第 32 条"全局变更需重组 Phase A 并重新审批"执行。
>
> **安全**：所有提示词生成版本均遵循 `docs/prompt_safety_policy.md`。

---

## 一、规格设定（更新后）

| 项目 | 设定 |
|---|---|
| 画幅 / 时长 | **4:3 横屏（Academy 经典比例 1.33:1，960×720 / 1440×1080）**；18 × 10 秒，总计约 180 秒 |
| 视觉风格 | **Style 2B — Cinematic Story（全彩电影叙事）** |
| 画面技术 | 720p（目标 1080p 可选）、24fps、同步音频 |
| 旁白 | 成熟、沉稳、自省克制的年轻美式男声（逐字不变），语速 140–145 词/分钟，总词数约 425 词 |
| BGM 曲线 | 与初版一致：68 BPM 钢琴 → 大提琴张力 → 104 BPM 金色钢琴收束 |
| 后期叠字 | 与初版一致（Clip 2 / 9 / 16 / 17 顶部短句，单独列出，不进生成提示词） |

---

## 二、Style 2B 视觉体系定义

### 1. 角色锚点（Character DNA Lock）

**A（丈夫）— 全片统一锚点**：

```text
The same minimalist 2D animated stick figure in a bright red beanie (smooth rounded knit, no pom-pom) and a yellow t-shirt, with simple black stick limbs and shorts. Simple black lines, vibrant colors, smooth 2D animation style.
```

**B（妻子）— 差异化锚点**（导演选择，审批可调整）：

```text
The same minimalist 2D animated stick figure wearing a grey t-shirt, no beanie, with a hollow circular head and minimal dot eyes, simple black stick limbs. Simple black lines, vibrant colors, smooth 2D animation style.
```

> 说明：A = 红帽 + 黄衫；B = 无帽 + 灰衫。所有含 B 的镜头（14–18）显式写锚点，防止漂移。

### 2. 环境公式（每镜必写）

```text
in a rich full-color cinematic environment [具体场景 + 时间 + 光源]. Cinematic volumetric lighting, soft depth of field, atmospheric narrative mood. The character remains the same minimalist 2D stick figure with simple black lines and vibrant colors, composited naturally inside the photographic-feeling environment.
```

### 3. 负向约束（每镜必带）

```text
Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances.
```

### 4. 色彩与情绪弧光

| 幕 | 环境基调 | 强调色功能 |
|---|---|---|
| 第一幕 1–6（撕裂） | 夜/室内的冷蓝灰，孤立点光源（台灯、路灯、手机光） | 红灯＝诱惑与警报；冰紫＝焦虑与监视 |
| 第二幕 7–12（解构） | 暴雨夜、山道、暗室、聚光灯——饱和度降低、对比拉高 | 红＝麻醉与失控；紫＝内耗；暴雨灰＝耗竭 |
| 第三幕 13–18（重生） | 黎明/日出暖金，开阔石材与天空 | 暖金＝理性、边界与新生 |

### 5. 连续性策略

- 相邻片段首尾帧动作与镜头动量严格咬合（每镜首帧显式"继承"上镜末态，末帧显式"交出"给下镜）。
- 角色比例、线宽、色彩风格、旁白音色全片锁定，不做任何变化。
- 环境可由同一"叙事世界"进化：同一客厅 → 同一条走廊 → 同一段山路 → 同一片断崖，避免场景随机跳变。

### 6. 事实与内容安全

- 不做医学/统计断言；机制描述沿用 `01_research/research_summary.md`。
- VO 按 `docs/prompt_safety_policy.md` 第 7 节完成 4 处安全微调（见下表标注）。

---

## 三、18 段三幕式分镜表（Style 2B 重排）

| 时间 | 叙事目的 | 场景环境 (2B) | 动作、镜头与转场 (4:3 横版) | English VO | 中文参考对照 | BGM / SFX |
|---|---|---|---|---|---|---|
| **0–10s** (Clip 1) | **强 Hook：提出灵魂疑问** | 深夜单身公寓客厅：冷蓝灰主调，一盏暖色落地灯，窗外城市夜景虚化 | **0–3s：** 垂直微俯，A（红帽黄衫）独自坐在沙发边缘。**3–7s：** 上方降下一道红色面具虚影，A 抬头，面具眼眶亮起微光。**7–10s：** 面具正中裂开冰紫裂缝，裂隙向地板延伸，镜头顺紫光穿入。下一段承接裂缝。 | Can a man who betrayed his marriage ever truly love his wife again? When he holds her, who is really in his mind? | 背叛之后的男人，还会真心爱自己的妻子吗？当他抱住你的时候，脑海里到底在想什么？ | 68 BPM 极简低音钢琴、沉闷心跳一声、面具碎裂微响。 |
| **10–20s** (Clip 2) | **认知反转：不是享受是撕裂** | 同一客厅，落地灯变冷，茶几上散着文件与冷掉的咖啡；地板可见裂纹 | **0–3s：** 镜头穿出裂缝：A 双臂平举如天平。**3–7s：** 左手托白色微缩房屋（家庭），右手托跳动的红色光球（刺激），两端剧烈起伏。**7–10s：** A 身体沿中轴撕成半透明重影，地板碎成冰紫碎片，双影坠入下方黑暗。下一段承接下坠。 | The truth is far colder than you think. Most unfaithful men are not living in pleasure—they are trapped in a violent internal civil war. | 真实的答案比你想象的更冷酷。绝大多数背叛的男人并不是在享受，而是困在自我撕裂的内战中。 | 钢琴单音延音、金属天平晃动声、身体撕扯杂音。 |
| **20–30s** (Clip 3) | **案例一：意外曝光与失控恐惧** | 深夜卧室：床头灯昏黄，墙上有窗外车灯掠过的投影 | **0–3s：** A 落地跪坐，身旁是发光的手机。**3–7s：** 手机炸开刺目红光，墙上投出妻子巨大而冰冷的眼睛剪影，A 跌坐后退。**7–10s：** A 双手前伸，四周升起冰紫垂直栅影（百叶窗/门框光栅化），逐渐收拢。下一段栅影维持。 | Take Mr. Zhou. When a random notification exposed his three-year secret, his desperate kneel down was not pure guilt. It was sheer panic over losing control. | 周先生的秘密被一条弹窗意外曝光，那一刻他崩溃下跪认错，本质不是纯粹的愧疚，而是对失去控制的极端恐慌。 | 强烈的短促警报音、膝盖跪地钝响、金属栏影上升声。 |
| **30–40s** (Clip 4) | **假性回归：窒息的伪和平** | 客厅/卧室：冷蓝灰，窗帘紧闭，室内薄雾，一盏顶灯投下硬光 | **0–3s：** 冰紫栅影合拢成透明玻璃盒，A 在盒内戴上白色微笑面具。**3–7s：** 盒外多双冰紫眼光扫射（投影在雾上），A 机械擦桌、递手机。**7–10s：** 盒内空气混浊，A 扶墙缓缓滑坐，面具脱落碎裂。下一段自地面碎片平移。 | He deleted accounts and surrendered passwords, living as a daytime saint and nighttime prisoner. Pseudo-remorse creates a suffocating cage, turning marriage into chronic exhaustion. | 他删光账号上交密码，白天扮演好丈夫，夜晚彻夜难眠。恐惧驱动的假性回归，把婚姻变成了窒息的消耗战。 | 沉闷钟摆声、机械转动声、心率过速、低频蜂鸣。 |
| **40–50s** (Clip 5) | **案例二：平淡婚姻中的自恋代偿** | 黄昏的灰色长廊（家→办公室的走道）：单调、无表情，尽头发白 | **0–3s：** A 佝偻着背沿长廊木然前行。**3–7s：** 右侧悬浮一只倾斜玻璃杯，倾倒红色液体光，红光笼罩 A，身形瞬间拔高，周身浮起崇拜星芒。**7–10s：** 星芒骤缩为一条红丝带，缠绕双肩，将 A 向后拽向一扇白门。下一段白门前承接。 | Then there is Mr. Liu. Decades of flat routine made him feel invisible. The outside affair was not love—it was a cheap painkiller to resurrect his dying vanity. | 还有刘先生。数十年的平淡让他感到自我枯死。婚外的刺激根本不是爱，而是一剂重新唤醒脆弱虚荣的廉价麻醉药。 | 单调机械脚步、红酒荡漾声、虚幻高音合成器、丝带绷紧骤响。 |
| **50–60s** (Clip 6) | **顺从补偿：愧疚与贪婪的同谋** | 同一长廊尽头：一扇高大白门，门缝透出暖光，地面浮着暗红波纹 | **0–3s：** 红丝带将 A 拽停门前，A 立刻堆起谄媚的顺从姿态。**3–7s：** A 双手捧出跳动红光的心形图标送入门口，背后却藏着一把发光的红钥匙。**7–10s：** 门楣上方凝出巨大的冰紫问号缓慢旋转，地面暗红波纹向外扩散。下一段自波纹升起。 | Guilt and betrayal easily coexist. He acted extra obedient at home, using synthetic sweetness as emotional currency to buy temporary peace of mind. | 愧疚与背叛完全可以同时存在。他在家里加倍顺从体贴，不过是用虚伪的讨好，给自己买一份暂时的心安。 | 虚伪的轻柔提琴、门锁转动咔哒声、液体暗流翻滚。 |
| **60–70s** (Clip 7) | **案例三：惊魂电话与双面伪装** | 深夜盘山公路：车窗外红色路灯掠过，远处城市灯火在雾中模糊 | **0–3s：** 俯视车内，A 紧握方向盘，车道虚线快速后退。**3–7s：** 仪表台上巨型来电图标炸开红光，A 猛打方向，车辆侧滑。**7–10s：** A 双脚重刹，车身在白色警戒线前停稳，线外道路没入黑暗。下一段自车头前方俯视。 | Mr. Li ended the affair quickly, but lived in perpetual terror. One unexpected phone call from his wife forced a frantic three-hour midnight sprint. | 李先生主动断掉了关系，却活在无休止的恐惧中。一次妻子要钥匙的意外电话，逼得他深夜狂奔三小时回赶。 | 急促引擎、刺耳刹车、电话高频震鸣、紧绷呼吸。 |
| **70–80s** (Clip 8) | **警觉耗竭：精神电量的彻底归零** | 深夜暴雨的岩壁边缘：雨幕、冷光、湿岩反光 | **0–3s：** 高角度俯视，A 伏在岩台上，胸前浮起四格白色电量标尺。**3–7s：** 冰紫沉重石块图标从上方缓缓压下、堆叠在 A 背上，电量骤降、最后一格红光急闪。**7–10s：** 电量熄灭，A 肢体松垂如断线木偶，顺岩壁滑入黑暗。下一段自黑暗中点亮。 | He realized this double life was never romantic freedom. It was a brutal energy vampire, exhausting every drop of sanity until complete collapse. | 他终于看清，这种双重生活根本不是浪漫自由，而是一只残酷吸干他精力的吸血鬼，直到精神彻底枯竭。 | 电池枯竭警告蜂鸣、重物压击闷响、电灯短路断电音。 |
| **80–90s** (Clip 9) | **底层剖析：情绪麻醉剂的假象** | 全黑房间，仅一束顶光；空气中有微尘可见 | **0–3s：** 顶光下 A 坐在地上，一道巨型红色光束自上方垂落，轻触 A 的头顶，泛起柔和光环。**3–7s：** 光束扩大，红光倾注而下；一条红布条缠上 A 的头部遮眼，四周浮起虚幻爱心图标。**7–10s：** 光束碎散成漂浮余烬，红布条脱落，A 垂头失神。下一段自余烬聚集。 | Affairs are nothing more than emotional painkillers. They release temporary dopamine to numb aging and boredom, but they cure absolutely nothing. | 婚外情不过是短命的心理止痛药。它释放廉价的多巴胺来麻痹衰老和平庸，却治不好任何现实的溃烂。 | 液体滴落回声、虚假掌声回音、温柔的玻璃风铃。 |
| **90–100s** (Clip 10) | **人性的悖论：最背叛的人最怕崩盘** | 暴雨夜的居民区街口：一栋白墙小屋在风雨中倾斜，窗内透出暖光 | **0–3s：** 红色余烬在空中拼成小屋屋脊线框，A 用双臂死死顶住倾颓的屋架。**3–7s：** 红色暴雨倾泻，A 双腿颤抖下沉，仍不松手。**7–10s：** 镜头拉远：屋内是妻子与孩子的暖光剪影；A 投在墙上的影子却是一条红色蛇影。下一段蛇影升起。 | Here lies the paradox: the man who betrayed the home is often the most terrified of its collapse. Yet staying inside is not the same as healing. | 这就是最讽刺的悖论：背叛家庭的人，往往最害怕家庭解体。但留在原地，绝不等于伤口已经愈合。 | 狂风暴雨、木架断裂呻吟、压抑心跳重击。 |
| **100–110s** (Clip 11) | **击碎误区：她从来不是因为"更好"** | 半明半暗的卧室：床头灯将熄，空气中浮着红色烟尘 | **0–3s：** 蛇影盘旋升空，化作模糊的红色女性轮廓。**3–7s：** 轮廓退去红光，露出一个残缺的灰色线偶人（无脸）。**7–10s：** A 双手前伸穿过线偶，只抓到虚无红烟；红烟聚成环形。下一段自红烟成镜。 | Wives often torment themselves asking: "Does he love her more?" No. He didn't choose a superior woman; he chose a cowardly exit from reality. | 很多妻子最折磨自己的问题是："他是不是更爱她？"不，他从来不是选择了更好的女人，他只是选择了当一个逃兵。 | 烟雾呼啸、抓空风声、冷峻大提琴 solo。 |
| **110–120s** (Clip 12) | **终极审视：你到底在逃避什么？** | 昏暗房间：一面高大穿衣镜，镜面蒙着薄雾，逆光勾出轮廓 | **0–3s：** 红烟凝成巨镜，A 走到镜前。**3–7s：** 镜中映出的不是 A，而是一个缩在角落、微微发抖的灰影，身上缠着厚重的冰紫细线。**7–10s：** A 低头静立，镜面中央裂开一道发丝般温暖的金色裂隙。下一段金光横向展开。 | If you are a man in this crisis, look in the mirror. Did betrayal solve your marital void, or did it expose your complete inability to face hard truths? | 正在经历危机的男人，照照镜子吧。背叛真的解决了婚姻的空虚吗？还是它彻底撕开了你不敢直面现实的软弱无能？ | 提琴骤停、镜面微鸣、深沉心跳、金色能量裂变声。 |
| **120–130s** (Clip 13) | **认知反转：面对真实代价的重量** | 黎明前的采石场石阶：巨石台阶向上隐入金色晨光，两侧是石壁 | **0–3s：** 金色裂隙铺成陡峭石阶，阶上立着一块巨大的深色石碑。**3–7s：** A 咬牙以肩顶住石碑下方，肌肉紧绷，一级级向上推。**7–10s：** 石碑底部的暗红杂质被金光灼净，化为纯净白石。下一段承接迈步。 | True redemption requires the spine to carry real weight. Stop playing the victim. Pay the full price of your actions instead of demanding cheap forgiveness. | 真正的救赎需要一副能扛起重量的硬骨头。停止扮演受害者。为你犯下的错支付全部代价，而不是乞求廉价的原谅。 | **104 BPM 坚定原声钢琴切入**、巨石摩擦轰鸣、金色烈焰声。 |
| **130–140s** (Clip 14) | **女性的觉醒：从情绪风暴中抽离** | 黄昏天台/高台：远处天空压着紫黑色风暴云，地面被最后一线金光斜照 | **0–3s：** B（黄衫无帽）独立高台，左侧涌来狂暴的冰紫风云。**3–7s：** B 抬右臂，胸前展开垂直的温暖金盾，风暴被硬生生阻隔。**7–10s：** 风暴溃散，B 身旁浮现金色天平与标尺图标，稳定发光。下一段聚焦天平与标尺。 | And for the wife: your greatest enemy right now is not heartbreak, but sinking under blind emotion. Step back. Look at his structural capacity to change. | 而对妻子来说：此时最大的敌人不是心痛，而是溺死在盲目的情绪里。抽身退后一步。看清他是否具备重塑关系的真正能力。 | 琴音高扬、护盾抵挡重击、风暴平息、清澈光晕音。 |
| **140–150s** (Clip 15) | **打破假和平：不破不立的清醒** | 破晓的断崖：两侧为坚实岩台，中间是深不见底的黑暗峡口，天际一线金光 | **0–3s：** A 与 B 隔着脆弱的白纸桥望向彼此。**3–7s：** 一道金色闪电自天顶垂直劈下，纸桥瞬间气化为飘散的金色余烬，坠入深暗。**7–10s：** 二人分立坚硬岩台，一切遮蔽散尽，只余真相与磐石。下一段自断崖边拉起。 | Do not settle for fragile apologies to keep an illusion alive. Sometimes, the rotten bridge must burn completely before an honest foundation can be built. | 别为了维持一段虚幻的平静，而接受摇摇欲坠的道歉。有时，腐烂的危桥必须彻底烧毁，诚实的基石才能真正建立。 | 清脆雷鸣、燃烧纸屑嘶声、岩石重撞、钢琴坚定上升。 |
| **150–160s** (Clip 16) | **重构边界：建立可承受的铁律** | 日出时分的断崖：天空从冷蓝过渡到温暖金橙，岩面被照得清晰 | **0–3s：** 金色光柱自两侧地底升起，形成两根笔直的金色界碑。**3–7s：** 一道通透强韧的金色光缆在界碑间绷紧，构成一座光影之桥。**7–10s：** A 与 B 同时迈步踏上光桥，脚下荡开层层金色同心波纹。下一段随脚步前移。 | Healing is not rewinding to an innocent past. It is writing non-negotiable boundaries, forging clear rules, and making the relationship sustainable again. | 修复从不是回到天真的过去。而是立下不可侵犯的边界，铸造清醒透明的规则，让这段关系重新变得可承受、可持续。 | 庄严管弦合奏、光缆绷紧共振、坚实脚步、金色波纹声。 |
| **160–170s** (Clip 17) | **终极金句：停止自我耗竭** | 金色清晨的辽阔地貌：地平线日出，远处山脊被晨光镀金 | **0–3s：** 镜头拉远，整个金色世界展开，黑暗被晨光驱散。**3–7s：** 画面中央浮起一个金色循环符号，被一柄金色光刃垂直切断。**7–10s：** A 与 B 平等并肩立于金色地平线前，日光升起。下一段定格于地平线。 | The fatal poison in marriage was never just the mistake itself. It is both partners bleeding endlessly in the wrong cycle. Stop the bleeding. Choose radical truth. | 婚姻中最致命的毒药，从来不是错误本身，而是双方在错误的循环里流血至死。止住失血，选择赤裸的真相。 | 情绪最高潮和弦、利刃斩断锁链脆响、温暖壮丽的日出合成音。 |
| **170–180s** (Clip 18) | **收束与行动倡议 (CTA)** | 日出后的开阔高地：天空干净通透，顶部大面积留白安全区 | **0–3s：** 二人并肩在晨光中前行，身后的阴霾彻底消散。**3–7s：** 画面上方中央保留大片干净天空。**7–10s：** 末帧定格在两人坚定前行的背影，画面中央一道温暖金色光环轻微脉动。 | Real love is not flawless innocence; it is the courage to rebuild on solid rock. Confront the reality, set your boundaries, and take back your life. | 真正的爱不是未遭玷污的天真，而是在坚硬磐石上重建的勇气。直面现实，立下边界，拿回属于你的人生。 | 宏大深情的余音回荡、微风、温暖钢琴延音缓淡出。 |

---

## 四、与初版差异清单（供审批核对）

| 项目 | 初版 (Style 1 Dark) | 修订版 (Style 2B) |
|---|---|---|
| 角色 | 纯白线条火柴人，无脸/无衣 | 红帽+黄衫拟人角色（A）；黄衫无帽（B） |
| 画布 | 纯黑 + 三强调色 | 全彩电影场景（夜/雨/黄昏/日出） |
| 环境 | 抽象图形装置 | 具象场景：公寓、卧室、长廊、山路、断崖、采石场、天台 |
| 强调色 | 红/紫/金（语义映射不变） | 作为**光源与道具色**融入场景（语义映射不变） |
| 叙事 / VO | — | **完全不变**（仅 4 处安全微调：painkiller / release / torment / sinking） |
| 分镜节拍 | — | 108 个拍点结构、装置与语义全部保留 |

---

## 五、重渲范围与成本（重要）

- 已生成的 clip_01–04、16、17 以及候选 clip_05 全部为 **Style 1**，在 2B 下**全部作废**，需重渲 → **18 条全量重生成**。
- 生成渠道与成本：
  - **Google Flow (Storyboard Studio)**：使用 Google One AI Premium Pro 官方每月 1,000 积分额度（每 10s 约 15 积分，可产出 60+ 镜头），支持首尾帧衔接与 Nano Banana 2 零积分预览。
- 预计排期：18 条片段在 Google Flow 中连续生成，预计消耗约 270 积分。

---

## 六、审批门禁 (Review Gate)

依据 skill 规范，本阶段在此停止。请你确认：

1. 是否批准 **Style 2B** 全局风格（含 A/B 角色锚点与"红帽/无帽"区分方式）？
2. 18 段场景重排（公寓 → 长廊 → 山路 → 断崖 → 日出）是否接受？
3. 4 处 VO 安全微调是否确认？
4. 是否同意 18 条全量重渲（旧 Style 1 素材归档保留，不删除）？

确认后我将执行：更新 `meta.json` 风格字段 → 生成 Style 2B 版 `prompts_all.md` 与 `clips_safe/` 18 条安全提示词 → 按配额窗口排期重渲。

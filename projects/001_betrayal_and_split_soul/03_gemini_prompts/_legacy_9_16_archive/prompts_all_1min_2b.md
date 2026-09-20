# Phase B — 1 分钟版生产脚本总汇 (6 Clips / Style 2B)

**适用平台**：Google Flow (`https://labs.google/fx/tools/flow`)  
**画幅规格**：`9:16` 竖屏，约 10 秒/段，720p、24 FPS、同步音频  
**视觉风格**：Style 2B — Cinematic Story（全彩电影环境 + 极简线条角色）  
**角色设定**：A = 红帽 + 黄衫；B = 无帽 + 灰衫  
**旁白总量**：142 词（6 段）  
**安全合规**：遵循 `docs/prompt_safety_policy.md`

---

## 全局连续性契约 (Global Continuity Block)

- **角色**：极简 2D 线条角色（黑线、鲜亮色块）合成于全彩电影感环境；空心圆头、点状简眼；禁止写实皮肤/人脸/3D 拟真。
- **环境**：每段写明"具体场景 + 时间 + 光源"，电影感体积光与浅景深；场景链条：公寓夜 → 卧室/客厅 → 暗室镜前 → 天台/断崖 → 日出高地。
- **强调色语义**：vivid red＝诱惑与警报；cool violet＝焦虑与内耗；warm gold＝清醒与边界。
- **零文字契约**：画面严禁出现任何可见文字、字幕、对话框与界面文案。
- **音频双锁**：6 段逐字复用同一位旁白；Clip 1 确立 68 BPM 钢琴与心跳，后续显式继承，Clip 5 起进入 104 BPM。
- **动态拍点**：每段严格按 `[0–3s]`、`[3–7s]`、`[7–10s]` 组织；相邻片段首尾帧严格咬合。

---

## Clip 01 — The Question (灵魂疑问)

```text
Create an approximately 10-second 9:16 vertical cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: a dim city apartment living room at night, warm floor lamp beside a sofa, blurred city lights beyond the window, cool blue-grey tones. Cinematic volumetric lighting, soft depth of field, quiet melancholic mood.

Character: Stick Figure A — a minimalist 2D animated stick figure wearing a bright red beanie (smooth rounded knit, no pom-pom) and a yellow t-shirt, simple black stick limbs and shorts, hollow circular head with minimal dot eyes, simple black lines, vibrant colors. Compose vertically in 9:16 within the central safe area.

First frame: A sits alone at the edge of the sofa, motionless, in the dim room.

[0–3s] The camera slowly pushes in; a red mask silhouette descends from above, hovering over A.
[3–7s] A lifts its head toward the mask; faint red light pulses inside the mask's empty eye sockets.
[7–10s] The mask splits down the middle into a jagged cool violet fissure; violet light runs across the floor and the camera plunges toward the glowing crack for Clip 2.

Final frame: the violet fissure glows through the floor, camera diving in.

Audio-only dialogue, exactly once: "Can a man who betrayed his marriage ever truly love his wife again? When he holds her, who is really in his mind?" Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: 68 BPM quiet minor-key piano, one muffled heartbeat thud, subtle room tone; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

---

## Clip 02 — The Civil War (内外撕裂)

```text
Create an approximately 10-second 9:16 vertical cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: the same apartment living room, now colder; the floor lamp dims, papers and a cold coffee cup rest on the table, hairline cracks spread across the wooden floor. Cinematic volumetric lighting, soft depth of field, tense stillness.

Character: Stick Figure A — the same minimalist 2D animated stick figure wearing a bright red beanie and a yellow t-shirt, simple black stick limbs, hollow circular head with minimal dot eyes, simple black lines, vibrant colors.

First frame: the camera rises out of the violet fissure from Clip 1, revealing A standing with both arms outstretched like a scale balance.

[0–3s] A's left hand holds a small white house model; A's right hand carries a pulsing vivid red orb.
[3–7s] The two arms tilt sharply up and down; A's body splits along its centerline into two flickering semi-transparent ghost figures pulling in opposite directions.
[7–10s] The floor cracks into floating cool violet shards; both silhouettes drop into the darkness below for Clip 3.

Final frame: A's double silhouette falls into darkness, violet shards scattering above.

Audio-only dialogue, exactly once: "The truth is colder than you think. Most unfaithful men are not enjoying freedom—they are trapped in a painful civil war between guilt and desire." Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: the identical 68 BPM minor-key piano continues seamlessly, joined by metallic scale clinking and a low falling drone; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

---

## Clip 03 — The Prisoner (温柔的囚徒)

```text
Create an approximately 10-second 9:16 vertical cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: a dark bedroom at night with a warm bedside lamp, curtains half drawn; the space then shifts into a cold grey living area with thin haze, shutters closed, and one hard ceiling light. Cinematic volumetric lighting, soft depth of field, quiet pressure.

Character: Stick Figure A — the same minimalist 2D animated stick figure wearing a bright red beanie and a yellow t-shirt, simple black stick limbs, hollow circular head with minimal dot eyes, simple black lines, vibrant colors.

First frame: A crouches on the bedroom floor beside a small glowing phone.

[0–3s] The phone bursts into vivid red light, casting a huge cold pale eye silhouette across the wall; A sits back against the wall.
[3–7s] Cool violet light bars rise and close into a transparent glass box around A; inside it, A puts on a plain white smiling mask and mechanically wipes the table and offers the phone forward.
[7–10s] The haze thickens inside the box; A slides slowly down against the glass, and the white mask slips off and cracks on the floor for Clip 4.

Final frame: A sits collapsed in the glass box, the cracked white mask on the floor.

Audio-only dialogue, exactly once: "He deletes accounts, surrenders passwords, plays the perfect husband—yet lives like a prisoner, exhausted by a performance no one believes." Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: the same piano continues, with a muffled pendulum, mechanical ticking, quickened heartbeat, and a low room hum; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

---

## Clip 04 — The Painkiller and the Mirror (麻醉与镜中真相)

```text
Create an approximately 10-second 9:16 vertical cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: a completely dark room with one vertical spotlight from above, fine dust drifting through the beam; later a tall floor mirror with misted glass and cool rim light. Cinematic volumetric lighting, soft depth of field, solemn introspection.

Character: Stick Figure A — the same minimalist 2D animated stick figure wearing a bright red beanie and a yellow t-shirt, simple black stick limbs, hollow circular head with minimal dot eyes, simple black lines, vibrant colors.

First frame: the cracked white mask from Clip 3 dissolves into fine dust on the floor.

[0–3s] A glowing red beam of light descends from above and touches A's head; a red cloth band wraps over A's eyes, while illusory heart icons float upward.
[3–7s] The red beam dissolves into floating embers; A walks to the tall mirror, where the reflection shows, instead of A, a small trembling grey figure huddled in the corner, wrapped in heavy cool violet threads.
[7–10s] A lowers its head in deep thought; a hairline warm gold fissure cracks open straight down the center of the mirror for Clip 5.

Final frame: the golden fissure glows along the mirror's center line.

Audio-only dialogue, exactly once: "The affair was never love. It was a cheap painkiller for his fading vanity. The mirror shows not a better woman—but a man escaping himself." Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: a soft hollow liquid drop echo, faint illusory applause, the cello stopping for one beat, then a clean resonating golden hum; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

---

## Clip 05 — Her Awakening and the Burning Bridge (觉醒与破桥)

```text
Create an approximately 10-second 9:16 vertical cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: first a rooftop terrace at dusk with churning violet-black storm clouds and the last warm gold light raking the platform; then a high stone ridge at daybreak with two solid black stone platforms facing a deep dark gap. Cinematic volumetric lighting, soft depth of field, rising resolve.

Characters: Stick Figure B — a minimalist 2D animated stick figure wearing a grey t-shirt, no beanie, hollow circular head with minimal dot eyes, simple black stick limbs; Stick Figure A — the same style figure with a bright red beanie and a yellow t-shirt. Simple black lines, vibrant colors, smooth 2D animation.

First frame: warm gold light from the mirror crack spills upward and fades into the dusk sky above the rooftop where B stands.

[0–3s] Fierce swirling cool violet storm clouds rush in from the left; B deliberately raises its right arm and a vertical translucent warm gold shield expands from B's hand, holding the storm back completely.
[3–7s] The storm breaks apart and clears; beside B, an icon-only golden balance scale and ruler glow with calm steady light.
[7–10s] Match cut to the ridge: A and B face each other across a fragile white paper bridge above the deep dark gap; a vertical bolt of warm gold lightning strikes down from top center and vaporizes the bridge into glowing embers that drift away into the darkness for Clip 6.

Final frame: embers fade above the dark gap, both figures standing on solid stone.

Audio-only dialogue, exactly once: "For the wife, the enemy is not heartbreak but blind emotion. Burn the fragile bridge; only honest boundaries can carry real weight." Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: a firm 104 BPM acoustic piano enters, with a resonant crystalline shield chime, howling wind, a clean thunder crack, and sizzling paper burn; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

---

## Clip 06 — Rebuild and Take Back (重构与行动)

```text
Create an approximately 10-second 9:16 vertical cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: an open highland at sunrise, clean transparent sky, warm light across grass and stone, generous negative space in the upper frame. Cinematic volumetric lighting, soft depth of field, resolved and hopeful.

Characters: Stick Figure A — bright red beanie and yellow t-shirt; Stick Figure B — grey t-shirt, no beanie. Both are minimalist 2D animated stick figures with hollow circular heads, minimal dot eyes, simple black stick limbs, simple black lines and vibrant colors.

First frame: the last embers fade above the dark gap as dawn light fills the sky.

[0–3s] Golden pillars of light rise from the ground on both sides, and a translucent strong golden light-cable stretches between them and pulls taut into a glowing bridge.
[3–7s] A and B step onto the light bridge together; concentric golden ripples spread beneath their feet, and a large golden loop symbol at the center of the frame is cut vertically by a golden light blade.
[7–10s] The two walk side by side into the sunrise, the last haze dissolving behind them; the final frame holds on their backs as a warm golden halo pulses gently at the center.

Final frame: their backs walk toward the horizon, golden halo softly breathing.

Audio-only dialogue, exactly once: "Real love is not flawless innocence. It is the courage to rebuild on solid rock. Face the truth, set your boundaries, and take back your life." Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: a solemn orchestral swell with the 104 BPM piano, a clean golden blade-cut chime, firm footsteps, and a sustained warm piano note fading out; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

---

## 拼接指南 (Stitching Guide)

| 切点 | Clip N 末帧 | Clip N+1 首帧 |
|---|---|---|
| 01 → 02 | 冰紫裂缝贯穿地板，镜头下潜 | 镜头自裂缝升出，A 呈天平姿态 |
| 02 → 03 | 双影坠入黑暗，紫碎片上飘 | A 落于卧室地板、手机发光 |
| 03 → 04 | A 滑坐玻璃盒，白面具碎裂 | 面具化为尘埃 |
| 04 → 05 | 镜面中央金色裂缝发光 | 金光上溢、切入天台黄昏 |
| 05 → 06 | 纸桥余烬飘散，二人立于岩台 | 余烬熄灭、晨光初启 |

---

## 旁白与音乐连续性说明

1. 6 段逐字复用同一位旁白描述；Clip 1 确立 68 BPM 钢琴，Clip 5 起切换 104 BPM 金色钢琴。
2. 若平台支持参考音色，优先复用同一旁白音频；否则依赖逐字锁定的旁白描述。
3. 成片阶段保留统一配乐与 voice-first 混音校正选项。

---

## 安全自检 (Safety Checklist)

- [x] 无身体伤害/勒颈/窒息/注射描写（Clip 3 为光栅玻璃盒；Clip 4 为红色光束）
- [x] 无成瘾物词汇（painkiller 为比喻，非具名药物）
- [x] 无未成年人相关描写
- [x] 无危险情境特写（Clip 5 断崖为静态舞台，无坠落动作）
- [x] 零可见文字；色彩仅用普通描述词
- [x] 旁白与 BGM 锁定逐段复用

# Phase B — Style 2B 4:3 横版生产脚本总汇 (18 Clips Cinematic Package)

**适用平台**：Google Flow (`https://labs.google/fx/tools/flow`)  
**画幅规格**：`4:3` 横屏（Academy 经典比例 1.33:1），约 10 秒/段，720p（960×720）、24 FPS、同步音频  
**视觉风格**：**Style 2B — Cinematic Story**（全彩电影叙事环境 + 极简线条角色）  
**角色设定**：A = 红帽 + 黄衫；B = 无帽 + 灰衫  
**安全合规**：全部提示词 100% 遵循 `docs/prompt_safety_policy.md`（无暴力、无武器、无成瘾物、无危险伤害情境描写，全量隐喻转译）  
**生产目录**：`03_gemini_prompts/clips_safe/`（包含完整 18 个独立 prompt 文件，直接顺序调用，无外部依赖与回退）

---

## 全局连续性契约 (Global Continuity Block)

- **画幅与构图**：`4:3` 横向舞台构图，角色与关键视觉动作稳定置于画面水平及垂直居中安全区内，左右留有均衡呼吸空间。
- **角色**：极简 2D 线条角色（黑线、鲜亮色块）合成在全彩电影感环境中；空心圆头、点状简眼，严禁写实皮肤/人脸/3D 拟真模型。
- **环境**：每段写明“具体场景 + 时间 + 光源”，统一采用电影感体积光与浅景深；场景沿“同一叙事世界”演进（公寓 → 卧室 → 走廊 → 山路 → 岩壁 → 暗室 → 断崖 → 采石场 → 天台 → 日出高地）。
- **强调色语义**：Saturated Danger Red＝诱惑与警报；Anxiety Violet＝焦虑与内耗；Warm Gold＝清醒与边界。
- **零文字契约**：画面严禁出现任何可见文字、字母、数字、字幕、对话框与界面文案。
- **音频双锁**：18 段逐字复用同一位年轻美式沉稳男声旁白；Clip 1 确立 68 BPM 钢琴与心跳基调，Clips 2–18 显式继承并演进 BGM。
- **动态拍点**：每段严格按 `[0–3s]`、`[3–7s]`、`[7–10s]` 组织物理动作；相邻片段首尾帧镜头动量严格咬合。

---

## Clip 01 — The Soul Question (灵魂拷问)

```text
Create an approximately 10-second 4:3 horizontal cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: a dim city apartment living room at night, cool blue-grey tones, one warm floor lamp beside a sofa, blurred city lights beyond the wide window. Cinematic volumetric lighting, soft depth of field, quiet melancholic mood.

Character: Stick Figure A — a minimalist 2D animated stick figure wearing a bright red beanie (smooth rounded knit, no pom-pom) and a yellow t-shirt, simple black stick limbs and shorts, hollow circular head with minimal dot eyes, simple black lines, vibrant colors, smooth 2D animation style. Compose horizontally in 4:3 ratio with cinematic staging, keeping key subjects within the central safe area.

First frame: Stick Figure A sits alone at the edge of the sofa in the 4:3 frame, motionless, in the dim room.

[0–3s] The camera slowly pushes in horizontally; an ominous saturated danger red mask silhouette descends from above, hovering over A.
[3–7s] A lifts its head toward the mask; faint red light pulses inside the mask's empty eye sockets.
[7–10s] The mask splits down the middle into a jagged cool violet fissure; violet light runs across the floor and the camera plunges toward the glowing crack for Clip 2.

Final frame: the violet fissure remains open on the floor, camera diving into the violet fracture.

Audio-only dialogue, exactly once: "Can a man who betrayed his marriage ever truly love his wife again? When he holds her, who is really in his mind?" Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: 68 BPM quiet minor-key piano, one muffled heartbeat thud, subtle room tone; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

---

## Clip 02 — Internal Civil War (撕裂内战)

```text
Create an approximately 10-second 4:3 horizontal cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: the same apartment living room, cooler light, scattered documents and a cold coffee mug on the coffee table, violet floor fracture visible across the lower 4:3 frame. Cinematic soft focus, high contrast, tense atmosphere.

Character: Stick Figure A — a minimalist 2D animated stick figure wearing a bright red beanie (smooth rounded knit, no pom-pom) and a yellow t-shirt, simple black stick limbs and shorts, hollow circular head with minimal dot eyes, simple black lines, vibrant colors, smooth 2D animation style. Compose horizontally in 4:3 ratio with cinematic staging, keeping key subjects within the central safe area.

First frame: camera emerges from the floor fissure; Stick Figure A stands center stage with arms outstretched horizontally like a mechanical scale balance.

[0–3s] In A's left hand floats a clean white miniature house icon (representing family); in A's right hand pulses an intense red glowing sphere (representing thrill).
[3–7s] Both arms tilt and oscillate violently up and down, failing to find balance as the red sphere throbs erratically.
[7–10s] A's body splits down the center into a translucent double silhouette; the floor fractures into geometric violet shards as the dual silhouettes descend into the dark space below.

Final frame: the twin silhouettes sink downward into dark violet depth.

Audio-only dialogue, exactly once: "The truth is far colder than you think. Most unfaithful men are not living in pleasure—they are trapped in a violent internal civil war." Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: continues 68 BPM quiet piano, sustained single piano note, metallic balance rattle, subtle tearing static distortion; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

---

## Clip 03 — Sudden Exposure (意外曝光)

```text
Create an approximately 10-second 4:3 horizontal cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: a dim bedroom at night, warm yellow bedside lamp illuminating the right side of the 4:3 frame, shadows of passing headlights sweeping across the back wall. Dramatic atmospheric shadows, claustrophobic mood.

Character: Stick Figure A — a minimalist 2D animated stick figure wearing a bright red beanie (smooth rounded knit, no pom-pom) and a yellow t-shirt, simple black stick limbs and shorts, hollow circular head with minimal dot eyes, simple black lines, vibrant colors, smooth 2D animation style. Compose horizontally in 4:3 ratio with cinematic staging, keeping key subjects within the central safe area.

First frame: A lands in a kneeling position on the bedroom floor beside a glowing smartphone screen.

[0–3s] The smartphone screen pulses with a sudden burst of warning red light.
[3–7s] A giant cold silhouette of a wife's watchful eyes projects across the bedroom wall; A recoils backwards in shock and panic.
[7–10s] Vertical cool violet shadow slats rise from the floor like geometric prison bars, closing in around A.

Final frame: vertical violet slats fully surround A in the center frame.

Audio-only dialogue, exactly once: "Take Mr. Zhou. When a random notification exposed his three-year secret, his desperate kneel down was not pure guilt. It was sheer panic over losing control." Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: sharp brief electronic alert chime, knee impact thud, rising metallic slat whir; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

---

## Clip 04 — The Glass Cage (假性回归牢笼)

```text
Create an approximately 10-second 4:3 horizontal cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: an enclosed room bathed in cool blue-grey haze, harsh downward overhead spotlight illuminating dust particles in the 4:3 stage. Tense, sterile, exhausting atmosphere.

Character: Stick Figure A — a minimalist 2D animated stick figure wearing a bright red beanie (smooth rounded knit, no pom-pom) and a yellow t-shirt, simple black stick limbs and shorts, hollow circular head with minimal dot eyes, simple black lines, vibrant colors, smooth 2D animation style. Compose horizontally in 4:3 ratio with cinematic staging, keeping key subjects within the central safe area.

First frame: the violet slat cage solidifies into a transparent glass cube in the horizontal center; A stands inside wearing a white smiling mask.

[0–3s] A stands rigidly inside the glass box, wearing the clean white smiling mask.
[3–7s] Sweeping cool violet searchlights scan outside the glass box; A performs stiff mechanical actions, wiping the tabletop and offering a smartphone.
[7–10s] Air inside the box thickens with haze; A slides down against the glass wall exhausted, and the white smiling mask slips off, shattering on the floor.

Final frame: A sits slumped inside the box, mask fragments scattered on the floor.

Audio-only dialogue, exactly once: "He deleted accounts and surrendered passwords, living as a daytime saint and nighttime prisoner. Pseudo-remorse creates a suffocating cage, turning marriage into chronic exhaustion." Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: heavy pendulum ticking, subtle clockwork gear whir, accelerating heartbeat thrum; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

---

## Clip 05 — Narcissistic Compensation (自恋代偿)

```text
Create an approximately 10-second 4:3 horizontal cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: a long sterile grey office-to-home corridor at dusk, monotonous neutral walls stretching symmetrically across the 4:3 horizontal frame, a bright doorway glowing in the far distance. Cinematic depth of field, dull repetitive atmosphere.

Character: Stick Figure A — a minimalist 2D animated stick figure wearing a bright red beanie (smooth rounded knit, no pom-pom) and a yellow t-shirt, simple black stick limbs and shorts, hollow circular head with minimal dot eyes, simple black lines, vibrant colors, smooth 2D animation style. Compose horizontally in 4:3 ratio with cinematic staging, keeping key subjects within the central safe area.

First frame: camera pans from floor debris to A walking slowly down the grey hallway, posture slouched and wooden.

[0–3s] A walks with mechanical, lifeless steps along the monotonous corridor.
[3–7s] A large translucent decorative glass overhead tilts gently, pouring a cascade of warm glowing red light particles over A; A's posture instantly straightens, and floating golden star icons surround A's head.
[7–10s] The golden stars compress into a bright red ribbon wrapping comfortably around A's shoulders, gently pulling A backwards toward the doorway.

Final frame: A is pulled toward the white doorway, red ribbon glowing on shoulders.

Audio-only dialogue, exactly once: "Then there is Mr. Liu. Decades of flat routine made him feel invisible. The outside affair was not love—it was a cheap painkiller to resurrect his dying vanity." Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: monotonous slow mechanical footsteps, gentle ethereal synth shimmer, crisp ribbon tension resonance; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

---

## Clip 06 — Obedient Bargaining (顺从与同谋)

```text
Create an approximately 10-second 4:3 horizontal cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: the end of the corridor before a tall white door glowing with warm light, subtle dark crimson ripples expanding across the polished floor. High contrast, secretive and strained mood.

Character: Stick Figure A — a minimalist 2D animated stick figure wearing a bright red beanie (smooth rounded knit, no pom-pom) and a yellow t-shirt, simple black stick limbs and shorts, hollow circular head with minimal dot eyes, simple black lines, vibrant colors, smooth 2D animation style. Compose horizontally in 4:3 ratio with cinematic staging, keeping key subjects within the central safe area.

First frame: the red ribbon guides A to a stop directly before the white door; A assumes an excessively polite, obedient posture.

[0–3s] A stands carefully before the door, posture obedient and eager to please.
[3–7s] A presents a glowing red heart icon with both hands toward the open doorway, while hiding a luminous red key behind its back.
[7–10s] A giant glowing violet question mark condenses above the doorway, rotating slowly as red ripples expand across the floor plane.

Final frame: violet question mark hovers above the door as ripples spread outward.

Audio-only dialogue, exactly once: "Guilt and betrayal easily coexist. He acted extra obedient at home, using synthetic sweetness as emotional currency to buy temporary peace of mind." Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: polite gentle string phrase, soft door latch click, low ambient resonant hum; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

---

## Clip 07 — Midnight Sprint (午夜狂奔)

```text
Create an approximately 10-second 4:3 horizontal cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: a nighttime winding road seen through the windshield of a car, dashboard console illuminated in dim green, streetlights and dashed road markings streaking past in the 4:3 frame. Cinematic motion blur, suspenseful thriller atmosphere.

Character: Stick Figure A — a minimalist 2D animated stick figure wearing a bright red beanie (smooth rounded knit, no pom-pom) and a yellow t-shirt, simple black stick limbs and shorts, hollow circular head with minimal dot eyes, simple black lines, vibrant colors, smooth 2D animation style. Compose horizontally in 4:3 ratio with cinematic staging, keeping key subjects within the central safe area.

First frame: overhead angle looking into the vehicle, A gripping the steering wheel firmly with both hands as dashed center lines race backward.

[0–3s] The car speeds along the winding mountain road through the night.
[3–7s] A large incoming call icon flashes bright danger red on the dashboard; A reacts with sudden panic, wrenching the wheel as tires squeal in a sideways skid.
[7–10s] A hits the brakes hard; the car stops smoothly right before a glowing white safety line across the asphalt, darkness beyond.

Final frame: car headlights beam onto the white safety line, dust settling.

Audio-only dialogue, exactly once: "Mr. Li ended the affair quickly, but lived in perpetual terror. One unexpected phone call from his wife forced a frantic three-hour midnight sprint." Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: tense accelerating car engine, sudden tire brake screech, high-frequency phone vibration, sharp gasp; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

---

## Clip 08 — Energy Depletion (精神耗竭)

```text
Create an approximately 10-second 4:3 horizontal cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: a rainswept rocky ledge at night, glistening wet stone reflections, driving rain streaks illuminated by cool blue rim lighting across the 4:3 frame. Severe, heavy, exhausting atmosphere.

Character: Stick Figure A — a minimalist 2D animated stick figure wearing a bright red beanie (smooth rounded knit, no pom-pom) and a yellow t-shirt, simple black stick limbs and shorts, hollow circular head with minimal dot eyes, simple black lines, vibrant colors, smooth 2D animation style. Compose horizontally in 4:3 ratio with cinematic staging, keeping key subjects within the central safe area.

First frame: high angle looking down, A kneels exhausted on the wet rocky ledge; a four-bar white battery energy meter HUD floats horizontally above A's chest.

[0–3s] Rain streams over A as A struggles to stay upright on the rocky plateau.
[3–7s] Heavy geometric violet stone blocks descend slowly from above, stacking heavily onto A's back; the battery meter drains rapidly from four bars down to one flashing red bar.
[7–10s] The final red bar extinguishes; A's limbs loosen like a marionette with severed strings, slumping onto the ledge as darkness covers the scene.

Final frame: A lies motionless on the ledge in darkness, empty HUD fading out.

Audio-only dialogue, exactly once: "He realized this double life was never romantic freedom. It was a brutal energy vampire, exhausting every drop of sanity until complete collapse." Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: low battery warning beep, heavy stone impact thuds, power-down electrical hum; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

---

## Clip 09 — Emotional Painkiller (情绪麻醉剂)

```text
Create an approximately 10-second 4:3 horizontal cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: a dark minimalist studio space, a single soft warm spotlight illuminating a circular area in the horizontal center, subtle floating dust particles. Melancholic, hollow, introspective mood.

Character: Stick Figure A — a minimalist 2D animated stick figure wearing a bright red beanie (smooth rounded knit, no pom-pom) and a yellow t-shirt, simple black stick limbs and shorts, hollow circular head with minimal dot eyes, simple black lines, vibrant colors, smooth 2D animation style. Compose horizontally in 4:3 ratio with cinematic staging, keeping key subjects within the central safe area.

First frame: A sits quietly on the floor inside the warm spotlight circle.

[0–3s] The overhead spotlight warms slightly as A gazes forward.
[3–7s] A vertical cylindrical beam of soft red light descends from above, enveloping A; a decorative red ribbon drapes gently across A's eyes as floating heart outlines drift lazily into the dark.
[7–10s] The red light dissolves into floating red embers; the ribbon falls away to the floor, and A sits slumped with head bowed in silence.

Final frame: red embers slowly drift away into darkness around the still figure.

Audio-only dialogue, exactly once: "Affairs are nothing more than emotional painkillers. They release temporary dopamine to numb aging and boredom, but they cure absolutely nothing." Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: soft dripping chime echo, gentle hollow synth pad, delicate fading wind bell; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

---

## Clip 10 — Fear of Collapse (恐惧崩盘悖论)

```text
Create an approximately 10-second 4:3 horizontal cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: a rainswept suburban street corner at night, a white-walled cottage leaning precariously in the storm, warm amber light glowing from the cottage window in the 4:3 frame. Intense emotional turbulence and fragility.

Character: Stick Figure A — a minimalist 2D animated stick figure wearing a bright red beanie (smooth rounded knit, no pom-pom) and a yellow t-shirt, simple black stick limbs and shorts, hollow circular head with minimal dot eyes, simple black lines, vibrant colors, smooth 2D animation style. Compose horizontally in 4:3 ratio with cinematic staging, keeping key subjects within the central safe area.

First frame: floating red embers assemble into a wooden cottage roof framework; A uses both arms to brace and push up the collapsing roof beam.

[0–3s] A stands braced with trembling arms, holding up the tilting cottage structure in the gale.
[3–7s] Red-tinted rain lashes horizontally; A's legs shake and sink slightly, but A refuses to let go of the roof beam.
[7–10s] Camera widens horizontally: inside the cottage window are warm silhouettes of a wife and child; yet A's shadow cast onto the wet exterior wall is a winding red serpent silhouette.

Final frame: serpent shadow looms on the wall as A strains beneath the roof beam.

Audio-only dialogue, exactly once: "Here lies the paradox: the man who betrayed the home is often the most terrified of its collapse. Yet staying inside is not the same as healing." Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: howling wind and driving rain, creaking wood strain, muffled heavy heartbeat thrum; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

---

## Clip 11 — The Cowardly Exit (逃兵真相)

```text
Create an approximately 10-second 4:3 horizontal cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: a dimly lit bedroom at late night, bedside lamp fading out, atmospheric red haze drifting horizontally across the 4:3 frame. Somber, disorienting, deconstructive atmosphere.

Character: Stick Figure A — a minimalist 2D animated stick figure wearing a bright red beanie (smooth rounded knit, no pom-pom) and a yellow t-shirt, simple black stick limbs and shorts, hollow circular head with minimal dot eyes, simple black lines, vibrant colors, smooth 2D animation style. Compose horizontally in 4:3 ratio with cinematic staging, keeping key subjects within the central safe area.

First frame: the red serpent shadow on the wall curls upward, morphing into an abstract, glowing red female silhouette hovering in mid-air.

[0–3s] The red silhouette floats before A, radiating soft crimson light.
[3–7s] The red glow dissolves from the silhouette, revealing a hollow, fragmented grey wireframe mannequin with no facial features.
[7–10s] A reaches out with both hands through the mannequin, grasping only dissipating red mist; the mist swirls into a glowing circular ring.

Final frame: red mist gathers into a glowing circular ring in the center frame.

Audio-only dialogue, exactly once: "Wives often torment themselves asking: "Does he love her more?" No. He didn't choose a superior woman; he chose a cowardly exit from reality." Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: gentle wind whoosh through mist, empty grasping swoosh, somber cello solo phrase; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

---

## Clip 12 — Mirror of Hard Truths (硬核自审)

```text
Create an approximately 10-second 4:3 horizontal cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: a dim room with a tall full-length dressing mirror, rim-lit by a soft backlight, the mirror surface clouded with delicate mist. Quiet, piercing, transformative mood.

Character: Stick Figure A — a minimalist 2D animated stick figure wearing a bright red beanie (smooth rounded knit, no pom-pom) and a yellow t-shirt, simple black stick limbs and shorts, hollow circular head with minimal dot eyes, simple black lines, vibrant colors, smooth 2D animation style. Compose horizontally in 4:3 ratio with cinematic staging, keeping key subjects within the central safe area.

First frame: the red mist ring expands into the full-length mirror; A walks slowly toward the mirror in the horizontal 4:3 staging.

[0–3s] A approaches the mirror and stops before the clouded glass.
[3–7s] The mirror reflection does not mirror A's posture; instead, it shows a trembling grey figure huddled in the corner, tightly bound by dense violet threads.
[7–10s] A stands motionless facing the reflection; a fine, hairline crack glowing with warm golden light splits vertically down the center of the mirror.

Final frame: mirror crack radiates intense warm golden light horizontally across frame.

Audio-only dialogue, exactly once: "If you are a man in this crisis, look in the mirror. Did betrayal solve your marital void, or did it expose your complete inability to face hard truths?" Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: cello phrase pauses, resonant mirror hum, deep calm heartbeat, golden energy fracture chime; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

---

## Clip 13 — Carrying the Weight (扛起代价)

```text
Create an approximately 10-second 4:3 horizontal cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: a pre-dawn stone quarry with wide stone steps ascending into a warm golden morning sky, rugged granite walls framing the left and right in 4:3 composition. Monumental, resolute, heroic atmosphere.

Character: Stick Figure A — a minimalist 2D animated stick figure wearing a bright red beanie (smooth rounded knit, no pom-pom) and a yellow t-shirt, simple black stick limbs and shorts, hollow circular head with minimal dot eyes, simple black lines, vibrant colors, smooth 2D animation style. Compose horizontally in 4:3 ratio with cinematic staging, keeping key subjects within the central safe area.

First frame: golden mirror fracture widens into the steep stone steps; a massive dark stone tablet rests on the incline.

[0–3s] A stands at the foot of the stone stairway looking up at the summit.
[3–7s] A sets its shoulder against the heavy base of the stone tablet, muscles tensing, pushing the tablet upward step by step.
[7–10s] Dark crimson impurities on the tablet burn away in the morning light, leaving the tablet as pure white polished stone.

Final frame: A pushes the purified white stone onto a level landing bathed in sunlight.

Audio-only dialogue, exactly once: "True redemption requires the spine to carry real weight. Stop playing the victim. Pay the full price of your actions instead of demanding cheap forgiveness." Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: 104 BPM resolute acoustic piano enters with strength, heavy stone grinding rumble, warm golden light flare sound; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

---

## Clip 14 — Stepping Out of the Storm (抽离情绪风暴)

```text
Create an approximately 10-second 4:3 horizontal cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: a high open stone terrace at dusk, distant violet storm clouds rolling in from the left, warm golden twilight illuminating the terrace floor in the 4:3 frame. Majestic, empowering, poised atmosphere.

Character: Stick Figure B — a minimalist 2D animated stick figure wearing a grey t-shirt, no beanie, hollow circular head with minimal dot eyes, simple black stick limbs, simple black lines, vibrant colors, smooth 2D animation style.

First frame: Stick Figure B (grey t-shirt, no beanie) stands tall in the center of the terrace, facing the incoming winds with calm poise.

[0–3s] Stick Figure B stands resolute on the terrace looking toward the dark horizon.
[3–7s] B raises its right arm forward; a vertical translucent golden energy shield unfolds in front of B, deflecting the turbulent violet storm wind.
[7–10s] The storm clouds break and dissipate; glowing golden balance scale and ruler icons materialize steadily beside B, emitting stable clear light.

Final frame: B stands calmly beside the glowing golden scale and ruler icons.

Audio-only dialogue, exactly once: "And for the wife: your greatest enemy right now is not heartbreak, but sinking under blind emotion. Step back. Look at his structural capacity to change." Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: uplifting 104 BPM piano progression, resonant energy shield deflection tone, storm wind calming, clear luminous halo chime; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

---

## Clip 15 — Burning the Fragile Bridge (烧毁危桥)

```text
Create an approximately 10-second 4:3 horizontal cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: a dawn mountain cliff chasm, two solid granite platforms separated by a deep dark abyss, first horizontal rays of golden dawn on the horizon. Stark, honest, clean architectural atmosphere.

Character: Stick Figure A (bright red beanie and yellow t-shirt, simple black limbs) and Stick Figure B (grey t-shirt, no beanie, simple black limbs). Both are minimalist 2D animated stick figures with simple black lines and vibrant colors. Compose horizontally in 4:3 ratio with balanced staging.

First frame: Stick Figure A stands on the left platform, Stick Figure B on the right platform; a fragile white paper bridge connects the two across the chasm.

[0–3s] A and B look toward each other across the fragile paper bridge in the 4:3 frame.
[3–7s] A vertical beam of golden morning energy descends from the sky, striking the paper bridge and dissolving it into golden dust that drifts into the chasm.
[7–10s] Both figures remain firmly standing on their solid rock platforms; all illusions vanish, leaving only bedrock and open sky.

Final frame: both figures grounded on their respective rocky cliffs, chasm clear between them.

Audio-only dialogue, exactly once: "Do not settle for fragile apologies to keep an illusion alive. Sometimes, the rotten bridge must burn completely before an honest foundation can be built." Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: crisp energy clap, dissolving paper sizzle, deep bedrock vibration, piano rising with clarity and strength; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

---

## Clip 16 — Building the Boundary Bridge (立下铁律之桥)

```text
Create an approximately 10-second 4:3 horizontal cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: the cliff chasm at sunrise, sky transitioning from deep blue to luminous amber gold, rugged stone surfaces highlighted in crisp detail across the 4:3 frame. Solid, triumphant, orderly atmosphere.

Character: Stick Figure A (bright red beanie and yellow t-shirt, simple black limbs) and Stick Figure B (grey t-shirt, no beanie, simple black limbs). Both are minimalist 2D animated stick figures with simple black lines and vibrant colors. Compose horizontally in 4:3 ratio with balanced staging.

First frame: A and B stand on their solid rock platforms facing each other across the gap as dawn breaks.

[0–3s] Two luminous golden boundary pillars rise straight up from the bedrock on both sides of the chasm.
[3–7s] A brilliant, resilient golden light-cable pulls taut between the two boundary pillars, forming a solid, illuminated suspension bridge.
[7–10s] A and B simultaneously step forward onto the golden light-bridge; concentric golden ripples pulse across the bridge floor beneath their footsteps.

Final frame: A and B walking toward center of golden bridge, footsteps pulsing with light.

Audio-only dialogue, exactly once: "Healing is not rewinding to an innocent past. It is writing non-negotiable boundaries, forging clear rules, and making the relationship sustainable again." Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: majestic orchestral harmony, cable tension resonance, firm confident footsteps, golden ripple sound; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

---

## Clip 17 — Severing the Bleeding Cycle (斩断失血死循环)

```text
Create an approximately 10-second 4:3 horizontal cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: an expansive golden morning landscape, sun rising over a distant mountain ridge, bathing rolling hills and sky in rich warm light. Majestic, liberating, epic atmosphere.

Character: Stick Figure A (bright red beanie and yellow t-shirt, simple black limbs) and Stick Figure B (grey t-shirt, no beanie, simple black limbs). Both are minimalist 2D animated stick figures with simple black lines and vibrant colors. Compose horizontally in 4:3 ratio with balanced staging.

First frame: wide horizontal 4:3 camera view across the golden panorama, morning sunlight washing away all traces of shadow.

[0–3s] The sweeping golden vista expands under the morning sun.
[3–7s] A glowing golden infinity loop floats in the upper center sky; a vertical beam of golden light strikes through the loop, cleanly snapping the closed circle.
[7–10s] A and B stand side by side as equals on the golden ridge, gazing toward the sunrise together.

Final frame: two figures standing side by side on ridge looking at rising sun.

Audio-only dialogue, exactly once: "The fatal poison in marriage was never just the mistake itself. It is both partners bleeding endlessly in the wrong cycle. Stop the bleeding. Choose radical truth." Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: emotional climax chord, clean chime of snapping loop, radiant warm sunrise synthesizer swell; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

---

## Clip 18 — Radical Truth and Rebirth (终极重生与行动)

```text
Create an approximately 10-second 4:3 horizontal cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: an open high plateau in full bright morning sunlight, crystal clear golden-white sky, generous clean negative space in the upper half of the 4:3 frame. Calm, resolute, hopeful, peaceful atmosphere.

Character: Stick Figure A (bright red beanie and yellow t-shirt, simple black limbs) and Stick Figure B (grey t-shirt, no beanie, simple black limbs). Both are minimalist 2D animated stick figures with simple black lines and vibrant colors. Compose horizontally in 4:3 ratio with balanced staging.

First frame: A and B walking side by side forward across the plateau in the bright morning light, long clean shadows extending behind them.

[0–3s] The two figures walk steadily side by side across the plateau, past hardships receding into the distance.
[3–7s] The camera follows from behind at a comfortable distance, maintaining generous clear sky in the upper frame.
[7–10s] The final frame holds on the two figures walking steadily toward the golden horizon; a warm luminous golden ring pulses gently in the center sky.

Final frame: two figures walking into golden horizon, subtle golden ring pulsating gently above.

Audio-only dialogue, exactly once: "Real love is not flawless innocence; it is the courage to rebuild on solid rock. Confront the reality, set your boundaries, and take back your life." Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: warm poignant acoustic piano trailing off, gentle breeze, rich sustaining chord slowly fading to silence; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

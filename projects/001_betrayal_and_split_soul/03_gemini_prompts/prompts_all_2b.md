# Phase B — Style 2B 生产脚本总汇 (18 Clips Cinematic Package)

**适用平台**：Google Flow (`https://labs.google/fx/tools/flow`)  
**画幅规格**：`9:16` 竖屏，约 10 秒/段，720p、24 FPS、同步音频  
**视觉风格**：**Style 2B — Cinematic Story**（全彩电影叙事环境 + 极简线条角色）  
**角色设定**：A = 红帽 + 黄衫；B = 无帽 + 灰衫  
**安全合规**：全部提示词遵循 `docs/prompt_safety_policy.md`（无伤害、无成瘾物、无危险情境描写）

---

## 全局连续性契约 (Global Continuity Block)

- **角色**：极简 2D 线条角色（黑线、鲜亮色块）合成在全彩电影感环境中；空心圆头、点状简眼，禁止写实皮肤/人脸/3D 拟真。
- **环境**：每段写明"具体场景 + 时间 + 光源"，统一采用电影感体积光与浅景深；场景沿"同一叙事世界"演进（公寓 → 卧室 → 长廊 → 山路 → 岩壁 → 暗室 → 断崖 → 采石场 → 天台 → 日出高地）。
- **强调色语义**：vivid red＝诱惑与警报；cool violet＝焦虑与内耗；warm gold＝清醒与边界。
- **零文字契约**：画面严禁出现任何可见文字、字幕、对话框与界面文案。
- **音频双锁**：18 段逐字复用同一位旁白；Clip 1 确立 68 BPM 钢琴与心跳基调，Clips 2–18 显式继承并演进 BGM。
- **动态拍点**：每段严格按 `[0–3s]`、`[3–7s]`、`[7–10s]` 组织物理动作；相邻片段首尾帧镜头动量严格咬合。

---

## Clip 01 — The Soul Question (灵魂拷问)

```text
Create an approximately 10-second 9:16 vertical cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: a dim city apartment living room at night, cool blue-grey tones, one warm floor lamp beside a sofa, blurred city lights beyond the window. Cinematic volumetric lighting, soft depth of field, quiet melancholic mood.

Character: Stick Figure A — a minimalist 2D animated stick figure wearing a bright red beanie (smooth rounded knit, no pom-pom) and a yellow t-shirt, simple black stick limbs and shorts, hollow circular head with minimal dot eyes, simple black lines, vibrant colors, smooth 2D animation style. Compose vertically in 9:16, keeping the character within the central safe area.

First frame: A sits alone at the edge of the sofa, motionless, in the dim room.

[0–3s] The camera slowly pushes in; a red mask silhouette descends from above, hovering over A.
[3–7s] A lifts its head toward the mask; faint red light pulses inside the mask's empty eye sockets.
[7–10s] The mask splits down the middle into a jagged cool violet fissure; violet light runs down the floor and the camera plunges toward the glowing crack for Clip 2.

Final frame: the violet fissure remains open on the floor, camera diving into it.

Audio-only dialogue, exactly once: "Can a man who betrayed his marriage ever truly love his wife again? When he holds her, who is really in his mind?" Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: 68 BPM quiet minor-key piano, one muffled heartbeat thud, subtle room tone; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

---

## Clip 02 — The Internal Civil War (内在裂解)

```text
Create an approximately 10-second 9:16 vertical cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: the same apartment living room, now colder; the floor lamp dims, papers and a cold coffee cup rest on the table, hairline cracks spread across the wooden floor. Cinematic volumetric lighting, soft depth of field, tense stillness.

Character: Stick Figure A — the same minimalist 2D animated stick figure wearing a bright red beanie and a yellow t-shirt, simple black stick limbs, hollow circular head with minimal dot eyes, simple black lines, vibrant colors.

First frame: the camera rises out of the violet fissure from Clip 1, revealing A standing with both arms outstretched like a scale balance.

[0–3s] A's left hand holds a small white house model; A's right hand carries a pulsing vivid red orb.
[3–7s] The two arms tilt sharply up and down; A's body splits along its centerline into two flickering semi-transparent ghost figures pulling in opposite directions.
[7–10s] The floor cracks into floating cool violet shards; both silhouettes drop into the dark below for Clip 3.

Final frame: A's double silhouette falls into darkness, violet shards scattering above.

Audio-only dialogue, exactly once: "The truth is far colder than you think. Most unfaithful men are not living in pleasure—they are trapped in a violent internal civil war." Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: the identical 68 BPM minor-key piano continues seamlessly, joined by metallic scale clinking, static glitch buzz, and a low falling drone; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

---

## Clip 03 — Notification Shock (意外曝光)

```text
Create an approximately 10-second 9:16 vertical cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: a dark bedroom at night, warm bedside lamp, curtains half drawn, passing car headlights sweeping faint light across the wall. Cinematic volumetric lighting, soft depth of field, anxious mood.

Character: Stick Figure A — the same minimalist 2D animated stick figure wearing a bright red beanie and a yellow t-shirt, simple black stick limbs, hollow circular head with minimal dot eyes, simple black lines, vibrant colors.

First frame: A crouches on the bedroom floor beside a small glowing phone.

[0–3s] The phone suddenly bursts into vivid red light, casting long shadows across the room.
[3–7s] On the wall, a huge cold pale eye silhouette appears; A scrambles backward and sits against the wall, head lowered.
[7–10s] Cool violet vertical light bars rise around A like window blinds turning into light, closing in slowly for Clip 4.

Final frame: the violet light bars surround A, tightening their spacing.

Audio-only dialogue, exactly once: "Take Mr. Zhou. When a random notification exposed his three-year secret, his desperate kneel down was not pure guilt. It was sheer panic over losing control." Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: the same minor-key piano continues, with a sharp notification chime, a heavy thud, and rising metallic bar tones; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

---

## Clip 04 — Pseudo-Remorse (窒息的伪和平)

```text
Create an approximately 10-second 9:16 vertical cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: the same apartment interior, shutters closed, thin haze in the air, a single hard ceiling light, cool blue-grey palette. Cinematic volumetric lighting, soft depth of field, airless stillness.

Character: Stick Figure A — the same minimalist 2D animated stick figure wearing a bright red beanie and a yellow t-shirt, simple black stick limbs, hollow circular head with minimal dot eyes, simple black lines, vibrant colors.

First frame: the violet light bars from Clip 3 close into a transparent glass box around A.

[0–3s] Inside the box, A puts on a plain white smiling mask and sits very straight.
[3–7s] Outside, several cool violet eye-shapes drift through the haze, scanning the room; A mechanically wipes the table and hands a phone forward.
[7–10s] The haze thickens inside the box; A leans against the glass wall and slowly slides down, and the white mask slips off and cracks on the floor for Clip 5.

Final frame: A sits collapsed against the glass, the cracked white mask on the floor.

Audio-only dialogue, exactly once: "He deleted accounts and surrendered passwords, living as a daytime saint and nighttime prisoner. Pseudo-remorse creates a suffocating cage, turning marriage into chronic exhaustion." Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: the same piano continues, with a muffled pendulum, mechanical ticking, quickened heartbeat, and a low room hum; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

---

## Clip 05 — The Narcotic of Vanity (平淡中的代偿)

```text
Create an approximately 10-second 9:16 vertical cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: a long monotonous grey corridor at dusk, doors repeating along the walls, pale light at the far end, dust floating in the air. Cinematic volumetric lighting, soft depth of field, monotonous mood.

Character: Stick Figure A — the same minimalist 2D animated stick figure wearing a bright red beanie and a yellow t-shirt, simple black stick limbs, hollow circular head with minimal dot eyes, simple black lines, vibrant colors.

First frame: mask fragments from Clip 4 scatter and dissolve as A walks, hunched, along the grey corridor.

[0–3s] A walks with tired, dragging steps down the endless corridor.
[3–7s] A tilted glass floats in from the right and pours a glowing stream of vivid red light over A; A straightens unnaturally tall while faint star shapes drift upward around it.
[7–10s] The star shapes collapse into a glowing red ribbon that coils gently around A's shoulders and pulls A backward toward a tall white door for Clip 6.

Final frame: A is drawn backward toward the white door, red ribbon taut across the shoulders.

Audio-only dialogue, exactly once: "Then there is Mr. Liu. Decades of flat routine made him feel invisible. The outside affair was not love—it was a cheap painkiller to resurrect his dying vanity." Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: the same piano continues, with slow dragging footsteps, soft liquid pour, ethereal synth chord, and a taut ribbon snap; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

---

## Clip 06 — Guilt and Greed (愧疚与贪婪)

```text
Create an approximately 10-second 9:16 vertical cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: the end of the grey corridor; a tall white door glows with warm light through its seam; faint dark red ripples spread across the floor. Cinematic volumetric lighting, soft depth of field, uneasy warmth.

Character: Stick Figure A — the same minimalist 2D animated stick figure wearing a bright red beanie and a yellow t-shirt, simple black stick limbs, hollow circular head with minimal dot eyes, simple black lines, vibrant colors.

First frame: the red ribbon from Clip 5 brings A to a stop in front of the tall white door.

[0–3s] A immediately adopts an exaggerated, submissive bow toward the doorway.
[3–7s] With both hands, A offers a glowing vivid red heart icon forward, while its left hand quietly hides a small glowing red key behind its back.
[7–10s] Above the door frame, a large cool violet question mark forms and rotates slowly; dark red ripples spread outward across the floor for Clip 7.

Final frame: the violet question mark hovers above the door, ripples widening on the floor.

Audio-only dialogue, exactly once: "Guilt and betrayal easily coexist. He acted extra obedient at home, using synthetic sweetness as emotional currency to buy temporary peace of mind." Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: the same piano continues, adding a sweet false violin tremolo, a door latch click, and murky bubbling; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

---

## Clip 07 — Midnight Sprint (深夜惊魂)

```text
Create an approximately 10-second 9:16 vertical cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: a mountain road at midnight, wet asphalt reflecting vivid red streetlights, mist gathering ahead, distant city glow blurred below. Cinematic volumetric lighting, soft depth of field, tense night driving mood.

Character: Stick Figure A — the same minimalist 2D animated stick figure wearing a bright red beanie and a yellow t-shirt, simple black stick limbs, hollow circular head with minimal dot eyes, simple black lines, vibrant colors.

First frame: the dark red ripples from Clip 6 resolve into a top-down view of A gripping a steering wheel inside a dark moving car.

[0–3s] White lane-dash perspective lines rush downward beneath the car; vivid red streetlight rings flash past outside.
[3–7s] A large phone handset icon flares with vivid red light on the dashboard; A turns the wheel quickly back and forth as the car skids sideways.
[7–10s] A presses both feet on the brake pedal; the car screeches to a stop exactly at a white warning line as the road beyond fades into deep black for Clip 8.

Final frame: the car rests at the white warning line, darkness beyond the road edge.

Audio-only dialogue, exactly once: "Mr. Li ended the affair quickly, but lived in perpetual terror. One unexpected phone call from his wife forced a frantic three-hour midnight sprint." Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: BGM shifts to a tense cello pulse, with roaring engine, piercing tire screech, urgent phone vibration, and a tense breath; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

---

## Clip 08 — Battery Drained (警觉耗竭)

```text
Create an approximately 10-second 9:16 vertical cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: a rain-soaked rocky ledge at night, cold blue-grey light, glistening wet stone, rain streaks in the air. Cinematic volumetric lighting, soft depth of field, bleak exhaustion.

Character: Stick Figure A — the same minimalist 2D animated stick figure wearing a bright red beanie and a yellow t-shirt, simple black stick limbs, hollow circular head with minimal dot eyes, simple black lines, vibrant colors.

First frame: high-angle view looking down past the stopped car toward the rocky ledge, where A lies prone on the wet stone.

[0–3s] A vertical white battery meter with four glowing bars floats above A's back.
[3–7s] Heavy cool violet stone icons drift down and stack onto A's back; the battery bars drain rapidly to one blinking vivid red bar.
[7–10s] The last bar fizzles out with a spark; A's limbs go slack like a resting marionette and A slides gently down the rock face into darkness for Clip 9.

Final frame: A slides down into pure blackness, rain fading above.

Audio-only dialogue, exactly once: "He realized this double life was never romantic freedom. It was a brutal energy vampire, exhausting every drop of sanity until complete collapse." Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: the tense cello continues, with heavy rain, dull impacts, rapid battery-warning beeps, an electrical short spark, then silence; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

---

## Clip 09 — The Emotional Painkiller (情绪麻醉剂)

```text
Create an approximately 10-second 9:16 vertical cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: a completely dark room, one vertical spotlight from above, fine dust drifting through the beam. Cinematic volumetric lighting, soft depth of field, solemn isolation.

Character: Stick Figure A — the same minimalist 2D animated stick figure wearing a bright red beanie and a yellow t-shirt, simple black stick limbs, hollow circular head with minimal dot eyes, simple black lines, vibrant colors.

First frame: the spotlight illuminates A sitting on the floor, eyes lowered, in the darkness from Clip 8.

[0–3s] A giant glowing red beam of light descends from the top of the frame and touches A's head with a soft halo.
[3–7s] The beam widens and pours glowing vivid red light over A; a red cloth band wraps around A's head, dimming its sight, while illusory heart icons float upward.
[7–10s] The red beam dissolves into dozens of floating embers; the red band slips off and A lowers its head, dazed, as the embers gather for Clip 10.

Final frame: red embers gather and rise upward through the darkness.

Audio-only dialogue, exactly once: "Affairs are nothing more than emotional painkillers. They release temporary dopamine to numb aging and boredom, but they cure absolutely nothing." Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: minor-key piano returns with solemn weight, a soft hollow liquid drop echo, faint surreal reverb, and a gentle glass chime; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

---

## Clip 10 — The Paradox (人性的悖论)

```text
Create an approximately 10-second 9:16 vertical cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: a quiet residential street at night in heavy rain, a small white-walled house leaning in the wind, warm light glowing from its windows, wet street reflecting the glow. Cinematic volumetric lighting, soft depth of field, storm tension.

Character: Stick Figure A — a minimalist 2D animated stick figure wearing a bright red beanie and a yellow t-shirt, simple black stick limbs, hollow circular head with minimal dot eyes, simple black lines, vibrant colors.

First frame: the red embers from Clip 9 drift together and assemble into the peaked roofline of the small white house.

[0–3s] The house tilts sideways in the wind; A braces both arms under the beams, holding the structure up.
[3–7s] A torrent of vivid red rain pours down; A's knees tremble but A holds on.
[7–10s] The camera pulls back: inside the warm windows stand the peaceful silhouettes of a wife and child, while A's shadow on the wall stretches into a long red serpent shape for Clip 11.

Final frame: A's serpent-shaped shadow lengthens upward across the wet wall.

Audio-only dialogue, exactly once: "Here lies the paradox: the man who betrayed the home is often the most terrified of its collapse. Yet staying inside is not the same as healing." Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: the same piano continues, with howling wind, torrential rain, creaking timber, and a deep steady heartbeat; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

---

## Clip 11 — Not "Better" (从来不是因为更好)

```text
Create an approximately 10-second 9:16 vertical cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: a half-lit bedroom at night, the bedside lamp dimming, red dust motes drifting in the air, cold blue walls. Cinematic volumetric lighting, soft depth of field, hollow quiet.

Character: Stick Figure A — a minimalist 2D animated stick figure wearing a bright red beanie and a yellow t-shirt, simple black stick limbs, hollow circular head with minimal dot eyes, simple black lines, vibrant colors.

First frame: the serpent shadow from Clip 10 rises from the floor and coils in mid-air, morphing into a shimmering vivid red female silhouette.

[0–3s] A stands looking up at the glowing red silhouette with outstretched, longing hands.
[3–7s] The red glow evaporates, stripping away all vibrancy to reveal an incomplete, faceless grey wire mannequin.
[7–10s] A's hands pass right through the empty mannequin; it dissolves into thin red smoke that curls into a vertical ring for Clip 12.

Final frame: the red smoke forms a slowly rotating vertical ring in the dark.

Audio-only dialogue, exactly once: "Wives often torment themselves asking: 'Does he love her more?' No. He didn't choose a superior woman; he chose a cowardly exit from reality." Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: the same piano continues, with a sorrowful solo cello line, a dissolving wind rush, and a hollow empty whoosh; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

---

## Clip 12 — The Mirror (终极审视)

```text
Create an approximately 10-second 9:16 vertical cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: a dim room at night, one tall floor mirror with misted glass, cool rim light outlining its frame, floorboards faintly reflected. Cinematic volumetric lighting, soft depth of field, introspective silence.

Character: Stick Figure A — a minimalist 2D animated stick figure wearing a bright red beanie and a yellow t-shirt, simple black stick limbs, hollow circular head with minimal dot eyes, simple black lines, vibrant colors.

First frame: the red smoke ring from Clip 11 solidifies into a tall vertical mirror standing in the room.

[0–3s] A steps forward and stands directly before the mirror, looking into its reflection.
[3–7s] In the reflection, instead of A, a small trembling grey figure huddles in the corner, gently wrapped in heavy cool violet threads.
[7–10s] A lowers its head in deep thought; a hairline warm gold fissure cracks open straight down the center of the mirror for Clip 13.

Final frame: the golden fissure glows along the mirror's center line.

Audio-only dialogue, exactly once: "If you are a man in this crisis, look in the mirror. Did betrayal solve your marital void, or did it expose your complete inability to face hard truths?" Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: the cello cuts out; one beat of silence, then a deep heartbeat and a clean resonating golden hum; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

---

## Clip 13 — The Weight of Real Cost (面对真实代价)

```text
Create an approximately 10-second 9:16 vertical cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: a stone quarry stairway before dawn, wide stone steps ascending into warm golden morning light, quarry walls on both sides, dust glowing in the beam. Cinematic volumetric lighting, soft depth of field, solemn resolve.

Character: Stick Figure A — a minimalist 2D animated stick figure wearing a bright red beanie and a yellow t-shirt, simple black stick limbs, hollow circular head with minimal dot eyes, simple black lines, vibrant colors.

First frame: the golden fissure from Clip 12 spreads wide and settles into a steep stone stairway.

[0–3s] A large dark monolith stands on the steps; A sets its shoulder firmly under the base.
[3–7s] A drives the monolith upward step by step, body straining with steady effort.
[7–10s] Dark red impurities along the monolith's base burn away in the warm gold light, leaving pure white stone for Clip 14.

Final frame: the whitened stone rests on the upper step, golden light washing over it.

Audio-only dialogue, exactly once: "True redemption requires the spine to carry real weight. Stop playing the victim. Pay the full price of your actions instead of demanding cheap forgiveness." Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: a firm 104 BPM acoustic piano enters as the BGM foundation, with heavy stone friction, deep footsteps, and warm fire-like shimmer; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

---

## Clip 14 — Her Awakening (女性的觉醒)

```text
Create an approximately 10-second 9:16 vertical cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: a rooftop terrace at dusk, distant violet-black storm clouds churning, the last warm gold light raking low across the platform floor. Cinematic volumetric lighting, soft depth of field, calm rising resolve.

Character: Stick Figure B — the same minimalist 2D animated stick figure wearing a grey t-shirt, no beanie, hollow circular head with minimal dot eyes, simple black stick limbs, simple black lines, vibrant colors.

First frame: the camera pans to the right side of the frame, where B stands firmly on the raised platform.

[0–3s] Fierce swirling cool violet storm clouds rush in from the left, trying to envelop B.
[3–7s] B deliberately raises its right arm; a vertical translucent warm gold shield expands from B's hand and holds the storm back completely.
[7–10s] The storm breaks apart and clears; beside B, an icon-only golden balance scale and ruler glow with calm steady light for Clip 15.

Final frame: the golden scale and ruler stay lit beside B as the sky calms.

Audio-only dialogue, exactly once: "And for the wife: your greatest enemy right now is not heartbreak, but sinking under blind emotion. Step back. Look at his structural capacity to change." Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: the 104 BPM piano and warm synth continue, with howling wind deflected by a resonant crystalline shield chime, settling into a clear quiet melody; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

---

## Clip 15 — Burn the Bridge (不破不立)

```text
Create an approximately 10-second 9:16 vertical cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: a high stone ridge at daybreak, two solid black stone platforms facing each other across a deep dark gap, a thin line of warm gold light on the horizon. Cinematic volumetric lighting, soft depth of field, decisive clarity.

Characters: Stick Figure A on the left rock — bright red beanie and yellow t-shirt; Stick Figure B on the right rock — grey t-shirt, no beanie. Both are minimalist 2D animated stick figures with hollow circular heads, minimal dot eyes, simple black stick limbs, simple black lines and vibrant colors.

First frame: wide vertical view: A on the left rock and B on the right rock, connected by a fragile white paper bridge.

[0–3s] A and B look toward each other across the flimsy paper bridge above the deep dark gap.
[3–7s] A vertical bolt of warm gold lightning strikes down from top center, instantly vaporizing the paper bridge into glowing embers that drift away into the darkness.
[7–10s] A and B stand grounded on solid black stone on either side; all cover is gone and only truth and stone remain for Clip 16.

Final frame: the two stand firmly on their stone platforms, embers fading below.

Audio-only dialogue, exactly once: "Do not settle for fragile apologies to keep an illusion alive. Sometimes, the rotten bridge must burn completely before an honest foundation can be built." Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: the 104 BPM piano continues, with a clean thunder crack, sizzling paper burn, and solid stone impact; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

---

## Clip 16 — Rebuild the Boundaries (重构边界)

```text
Create an approximately 10-second 9:16 vertical cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: the same high stone ridge at sunrise, sky shifting from cool blue to warm gold-orange, rock faces lit clearly, calm open air. Cinematic volumetric lighting, soft depth of field, stable hopeful mood.

Characters: Stick Figure A — bright red beanie and yellow t-shirt; Stick Figure B — grey t-shirt, no beanie. Both are minimalist 2D animated stick figures with hollow circular heads, minimal dot eyes, simple black stick limbs, simple black lines and vibrant colors.

First frame: from the golden scale of Clip 15, both figures stand on their stone platforms facing each other.

[0–3s] Golden pillars of light rise from the ground on both sides, forming two straight boundary markers.
[3–7s] A translucent, strong golden light-cable stretches between the pillars and pulls taut into a glowing bridge.
[7–10s] A and B step onto the light bridge together; concentric golden ripples spread beneath their feet for Clip 17.

Final frame: the two stand on the glowing bridge, ripples widening outward.

Audio-only dialogue, exactly once: "Healing is not rewinding to an innocent past. It is writing non-negotiable boundaries, forging clear rules, and making the relationship sustainable again." Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: a solemn orchestral swell joins the piano, with a resonant cable tension tone, firm footsteps, and spreading golden ripples; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

---

## Clip 17 — Stop the Bleeding (停止自我耗竭)

```text
Create an approximately 10-second 9:16 vertical cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: a vast golden morning landscape, sunrise breaking on the horizon, distant ridges edged in warm light, clear sky. Cinematic volumetric lighting, soft depth of field, expansive release.

Characters: Stick Figure A — bright red beanie and yellow t-shirt; Stick Figure B — grey t-shirt, no beanie. Both are minimalist 2D animated stick figures with hollow circular heads, minimal dot eyes, simple black stick limbs, simple black lines and vibrant colors.

First frame: the camera pulls back from the light bridge of Clip 16, revealing the wide golden world.

[0–3s] The camera keeps pulling back as the golden world opens and the last darkness is driven away by morning light.
[3–7s] A large golden loop symbol floats at the center of the frame and is cut vertically by a golden light blade.
[7–10s] A and B stand side by side before the golden horizon as the sun rises for Clip 18.

Final frame: the two stand side by side, sunrise glowing along the horizon.

Audio-only dialogue, exactly once: "The fatal poison in marriage was never just the mistake itself. It is both partners bleeding endlessly in the wrong cycle. Stop the bleeding. Choose radical truth." Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: the emotional peak chord, a clean blade-cut chime, and a warm sunrise synth swell; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

---

## Clip 18 — CTA (收束与行动倡议)

```text
Create an approximately 10-second 9:16 vertical cinematic 2D animation clip targeting 720p at 24 FPS with synchronized audio.

This is a non-violent educational 2D line-animation about psychology; all characters are abstract minimalist symbols; every image is a symbolic metaphor.

Environment: an open highland after sunrise, clean and transparent sky, warm light across grass and stone, generous negative space in the upper frame. Cinematic volumetric lighting, soft depth of field, resolved and hopeful.

Characters: Stick Figure A — bright red beanie and yellow t-shirt; Stick Figure B — grey t-shirt, no beanie. Both are minimalist 2D animated stick figures with hollow circular heads, minimal dot eyes, simple black stick limbs, simple black lines and vibrant colors.

First frame: A and B stand side by side facing the sunrise, the landscape open before them.

[0–3s] The two walk forward together in the morning light; the last haze dissolves behind them.
[3–7s] The upper center of the frame stays as clean open sky, kept free for later text overlay in editing.
[7–10s] The final frame holds on their backs walking steadily onward, a warm golden halo pulsing gently at the center.

Final frame: their backs walk toward the horizon, golden halo softly breathing.

Audio-only dialogue, exactly once: "Real love is not flawless innocence; it is the courage to rebuild on solid rock. Confront the reality, set your boundaries, and take back your life." Do not display or transcribe dialogue visually.

Identical narrator: warm, articulate, mature young adult American male voice, calm analytical and deeply introspective tone, voice-first mix, audio voiceover only, strictly no speech bubbles or dialogue boxes. Audio: the grand warm outro, a light breeze, and a sustained piano note slowly fading; voice dominant.

Negative constraints: no photorealistic human skin or faces, no 3D humanoid CGI uncanny valley models, no chaotic line glitches, no speech bubbles, no dialogue text boxes, no visible text. No violence, no weapons, no injury, no depiction of harm, no substances. Do not alter dialogue.
```

---

## 拼接指南 (Stitching Guide)

| 切点 | 出画状态（Clip N 末帧） | 入画状态（Clip N+1 首帧） |
|---|---|---|
| 01 → 02 | 冰紫裂缝贯穿地板，镜头下潜 | 镜头从裂缝升出，A 双臂成天平 |
| 02 → 03 | 双影坠入黑暗，紫碎片上飘 | A 落地跪坐于卧室地板 |
| 03 → 04 | 冰紫光栅收拢包围 A | 光栅合拢为玻璃盒 |
| 04 → 05 | A 滑坐玻璃盒内，面具落地碎裂 | 面具碎片散落，A 在灰色长廊行走 |
| 05 → 06 | 红丝带缠绕双肩，A 被拉向白门 | 红丝带将 A 拽停白门前 |
| 06 → 07 | 冰紫问号悬于门楣，暗红波纹扩散 | 波纹化为俯视车内视角 |
| 07 → 08 | 车停于白色警戒线，路尽头黑暗 | 高角度俯视车头前方岩台 |
| 08 → 09 | A 顺岩壁滑入黑暗 | 黑暗中一束顶光点亮 A |
| 09 → 10 | 红色余烬聚集上升 | 余烬在空中拼成小屋屋脊 |
| 10 → 11 | 墙上红蛇影向上蔓延 | 蛇影盘旋升空化为红色女性轮廓 |
| 11 → 12 | 红烟聚成环形 | 环形红烟凝成巨镜 |
| 12 → 13 | 镜面中央裂开金色细缝 | 金光横向展开为石阶 |
| 13 → 14 | A 推石上行，脚步坚定 | 镜头拉远切至黄昏天台 B 独立 |
| 14 → 15 | 金色天平与标尺发光 | 断崖两端，A 与 B 隔纸桥相望 |
| 15 → 16 | 二人立于岩台，遮蔽散尽 | 金色界碑自地底升起 |
| 16 → 17 | 二人踏光桥前行 | 镜头拉远，金色世界展开 |
| 17 → 18 | 二人并肩立于地平线前 | 二人并肩在晨光中前行 |

---

## 旁白与音乐连续性说明 (Voice & Music Continuity)

1. 18 段提示词逐字复用同一位旁白描述；BGM 由 Clip 1 确立主题，后续显式声明"无缝延续"。
2. 若平台支持参考音频/角色音色，优先复用同一音色；否则依赖逐字锁定的旁白描述。
3. 最终成片阶段保留统一配乐与混音校正的选项（voice-first 混音）。

---

## 安全与合规检查 (Safety Checklist)

- [x] 无身体伤害/勒颈/窒息/针筒注射等描写（Clip 5 红丝带缠绕双肩；Clip 9 红色光束照射）
- [x] 无成瘾物词汇（narcotic 已替换为 painkiller；cocktail 已替换为 glass）
- [x] 无未成年人受困描写（Clip 12 为"灰色颤抖剪影 + 冰紫细线"）
- [x] 无危险情境特写（Clip 7 停于警戒线；Clip 8 沿岩壁滑落）
- [x] 全片零可见文字；色彩仅用普通描述词（vivid red / cool violet / warm gold / grey）
- [x] 旁白锁定与 BGM 连续性锁定逐段复用

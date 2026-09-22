# 动态漫画故事分镜表 (Storyboard Specification)

> **使用说明**：
> 1. 本表为动态漫画故事的标准分镜矩阵，各列支持自动化脚本精准提取（`generate_tts.py`、`animate_panels.py`）；
> 2. `运镜意图` 支持预设标签：
>    - `slow_push`（慢速推镜，强化心理沉浸）
>    - `slow_pull`（慢速拉镜，展现全景反转）
>    - `pan_left` / `pan_right`（横向扫视画格）
>    - `breathing_drift`（呼吸感微漂，赋予静态画格生命力）
>    - `snap_zoom`（疾推特写，用于高潮或冲突点）
> 3. `生图提示词` 用于在 Google Flow 中通过 Nano Banana 2（0 积分）生成高清原始画格。

---

## 故事分镜矩阵 (Panel Matrix)

| 画格编号 | 画面构图描述 | 旁白台词 (Narration) | 运镜意图 (Motion) | 生图提示词 (Nano Banana 2 Prompt) |
|---|---|---|---|---|
| `panel_01` | 雨夜窗台，侦探深色风衣背影，手机亮着微光，雨滴划过玻璃 | 雨夜的城市从不安静，尤其是当那个匿名电话在凌晨三点响起时。 | `snap_zoom` | `A sharp-eyed detective in a dark crumpled trench coat, messy jet-black hair, seen from behind at a rain-streaked window, glowing smartphone in hand, moody manga ink illustration, high contrast shadows, atmospheric rim light, 4:3 ratio` |
| `panel_02` | 侦探正面半身特写，眼神锐利凝重，桌面散落着神秘档案封套 | 对方只说了七个字：“他在旧港口等你。”随后便是一片盲音。 | `slow_push` | `Medium close-up of a weary detective, sharp eyes, slight stubble, holding a classic telephone receiver, desk scattered with Manila folders, dramatic noir lighting, vintage manga hatching, 4:3 ratio` |
| `panel_03` | 荒凉旧港口全景，生锈的吊机在浓雾中若隐若现，冷色调 | 潮湿的空气里混合着铁锈与海水的咸味，一切仿佛一个早被设好的圈套。 | `pan_right` | `Wide shot of an abandoned industrial dock at midnight, towering rusty cranes shrouded in heavy fog, puddles reflecting dim yellow streetlights, eerie silence, detailed graphic novel ink style, 4:3 ratio` |
| `panel_04` | 阴影中伫立的神秘黑影，指尖夹着未熄灭的香烟火星 | 黑暗中，一个熟悉的身影缓缓转过身来。 | `breathing_drift` | `A mysterious silhouette standing in the deep shadows of a shipping container, glowing red cigarette ember, dramatic chiaroscuro lighting, heavy ink cross-hatching, cinematic comic panel, 4:3 ratio` |
| `panel_05` | 两人对峙极度特写，雨水在半空中被路灯照得透亮 | “你果然还是来了，十年前的真相，今晚该做个了结了。” | `slow_pull` | `High tension confrontation between two men under a single flickering streetlight, pouring rain frozen in motion, intense eye contact, master graphic novel panel, cinematic depth of field, 4:3 ratio` |

# 题材套件开发与扩展指南 (Genre Presets Guide)

本代码库采用**“微内核底座（Core Engine） + 题材套件（Genre Presets）”**的插件化架构。
无论是现有的火柴人（`stickman`）、动态漫画故事（`comic_story`），还是未来想加入的任何新题材（例如 PPT 图文动效、3D 机械模型讲解、儿童有声绘本等），均可按照以下 3 步在 5 分钟内无缝接入。

---

## 3 步创建新题材套件

### 步骤 1：创建套件目录
在 `presets/<your_genre_name>/` 下创建基础目录，例如：
```text
presets/ppt_slideshow/
├── template/                         # 项目目录骨架
│   ├── meta.json                     # 预置元数据
│   └── ...各阶段工作区目录...
└── README.md                         # 题材说明与 SOP
```

### 步骤 2：定义 `template/meta.json`
在模板根目录提供 `meta.json`，声明题材代号与默认属性：
```json
{
  "project_id": "template",
  "genre": "ppt_slideshow",
  "title_zh": "项目中文标题",
  "title_en": "Project English Title",
  "aspect_ratio": "16:9",
  "style": "Modern Minimalist Card",
  "status": "draft"
}
```

### 步骤 3：直接使用脚手架启动项目
无需修改任何底层代码，脚手架 `new_project.py` 会自动探测并根据 `--genre` 生成项目：
```powershell
python scripts/new_project.py 003_ai_cards --genre ppt_slideshow --title-zh "AI效率工具卡片"
```

---

## 核心底座提供的共享能力 (Core Engine Provided)
任何新题材均可直接免费复用 `core/` 提供的开箱即用能力：
1. **`core.project_base.Project`**：统一的项目定位、元数据读写与生命周期跟踪。
2. **`core.engine.ffmpeg_utils.probe_video_size`**：视频宽高与横竖屏自动识别。
3. **`core.engine.ffmpeg_utils.detect_and_fix_rtl`**：多语言 RTL 文本自动纠偏。
4. **`core.engine.ffmpeg_utils.burn_subtitles`**：自适应分辨率、字体与边距的智能字幕压制。

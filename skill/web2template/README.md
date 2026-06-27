# web2template SKILL

从任意网站或 HTML demo 中逆向提取 UI/UX 设计特征，生成可复用的标准化风格提示词文档。

## 它做什么

给定一个网站 URL 或本地 HTML 文件，此 SKILL 会：

1. **页面解析** — 截取页面截图（顶部/中部/底部/全页），提取计算样式、CSS 变量、DOM 结构、字体、色彩、间距、圆角、阴影、动画等设计元素
2. **风格归纳** — 将提取的设计元素转化为结构化的 UI/UX 描述标签与规则
3. **提示词生成** — 输出一份可复用的、标准化的 UI/UX 风格提示词文档，可作为后续生成相似风格页面的 Prompt 输入

## 快速开始

### 1. 安装依赖

```bash
pip install playwright
playwright install chromium
```

### 2. 运行提取脚本

```bash
# 分析在线网站
python skill/web2template/scripts/extract_and_capture.py \
  --url "https://example.com" \
  --output "./web2template_output"

# 分析本地 HTML 文件
python skill/web2template/scripts/extract_and_capture.py \
  --file "./templates/Glassmorphism/Glassmorphism.html" \
  --output "./web2template_output"
```

### 3. 查看产出

运行后 `web2template_output/` 目录包含：

```
web2template_output/
├── screenshots/
│   ├── screenshot-01-top.png        # 首屏截图
│   ├── screenshot-02-middle.png     # 中部截图
│   ├── screenshot-03-bottom.png     # 尾部截图
│   └── screenshot-full.png          # 全页截图
└── design_data.json                 # 结构化设计数据
```

### 4. 生成提示词文档

将 `design_data.json` 与截图提供给 Agent，Agent 会：

- 视觉分析截图（配色、布局、字体、氛围）
- 结合 JSON 精确数据（色值、字号、间距、动画）
- 基于 `templates/prompt_template.md` 模板生成 `style_prompt.md`

## 在 CodeBuddy 中使用

直接对 Agent 说：

> "分析 https://stripe.com 的设计风格，生成一份提示词文档"

或：

> "分析 ./templates/SaaS/SaaS.html 的设计风格"

Agent 将自动执行完整的提取 → 分析 → 生成流程。

## 输出文档结构

生成的 `style_prompt.md` 遵循以下结构（与本项目现有模板格式对齐）：

| 章节 | 内容 |
|------|------|
| 基本信息 | 风格 ID、显示名称、明暗模式、字体类型、一句话描述 |
| 布局创意 | 每个页面区块的布局结构描述 |
| 完整提示词 | 完整的可复用设计系统文档 |
| ├ 设计哲学 | 核心原则、视觉气质、风格 DNA |
| ├ Token 系统 | 色彩、字体、间距、边框与阴影的具体数值表 |
| ├ 组件样式 | 按钮、卡片、输入框等组件的样式与交互 |
| ├ 大胆要素 | 使此风格独特的签名技巧 |
| ├ 效果与动画 | 运动哲学、过渡值、关键帧动画 |
| ├ 响应式策略 | 断点适配方案 |
| └ 可访问性 | 对比度、聚焦状态、触控目标 |

## design_data.json 字段说明

| 字段 | 类型 | 说明 |
|------|------|------|
| `page_info` | object | 页面标题、语言、描述、字符集 |
| `css_variables` | object | `:root` 中定义的 CSS 自定义属性 |
| `color_palette` | object | 背景色、文字色、边框色集合（计算样式） |
| `typography` | object | 字体族、已加载字体、标题信息、字号、字重、行高、字距 |
| `spacing` | object | 常见 padding、margin、gap 值 |
| `borders` | object | 圆角值、边框规格、边框样式 |
| `shadows` | array | box-shadow 值集合 |
| `layout` | object | 页面区块结构、容器信息、总高度 |
| `animations` | object | 过渡值、动画名、@keyframes 规则 |
| `gradients` | array | 背景渐变值集合 |
| `effects` | object | filter、backdrop-filter、transform 值 |
| `resources` | object | 外部字体、样式表、脚本链接 |

## 与 beautiful_web_template 项目的关系

此 SKILL 为 [beautiful_web_template](../../README.md) 项目的配套工具。项目中的 33 套模板每套都附有一份手写的设计提示词 Markdown 文档。此 SKILL 可自动化该流程——从任意网页逆向生成同样格式的提示词文档，扩展模板库的设计风格覆盖范围。

## 技术方案

采用**混合方案**：

- **Playwright 浏览器自动化**：获取真实渲染后的计算样式与截图，确保数据准确性
- **LLM 视觉分析**：Agent 通过多模态能力分析截图，补充数据无法捕捉的视觉氛围与设计意图
- **模板驱动生成**：基于结构化模板输出，确保文档格式一致性与可复用性

## 许可

随主项目许可。

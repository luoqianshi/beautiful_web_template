---
name: web2template
description: 从任意网站或本地 HTML demo 中逆向提取 UI/UX 设计特征，生成可复用的标准化风格提示词文档，并可进一步沉淀为组件库模板、注册进 beautiful_web_template 项目画廊（index.html + README）。当用户要求分析网站设计风格、提取页面视觉特征、生成设计提示词、沉淀为风格模板或基于现有页面复刻风格时，务必使用此 skill。
---

# web2template

> 从任意网站或 HTML demo 中逆向提取 UI/UX 设计特征，生成可复用的标准化风格提示词文档，并可沉淀为项目模板画廊中的正式模板。

## 触发条件

当用户执行以下操作之一时激活此 SKILL：

- 提交一个网站链接（URL），希望分析其设计风格
- 提供一个本地 HTML 文件路径，希望提取其设计特征
- 要求"分析这个网站的设计"、"提取这个页面的风格"、"生成设计提示词"
- 希望将某个网页的设计风格转化为可复用的 Prompt 文档
- 要求"沉淀为 XX 风格"、"生成组件库"、"把提取的风格加入模板画廊"（触发阶段 6-8）

## 前置依赖

此 SKILL 的核心提取脚本依赖 Playwright。首次使用前需安装：

```bash
pip install playwright
playwright install chromium
```

若环境中已有 Playwright（如本项目 `script/recapture_01_02_03.py` 已在使用），则无需重复安装。

## 工作流程

执行以下 8 个阶段。**阶段 1-5 为核心提取流程，严格按顺序执行，不可跳步；阶段 6-8 为模板沉淀流程，在用户要求"沉淀为风格 / 生成组件库 / 加入画廊"时执行。**

---

### 阶段 1：接收与预处理输入

1. 从用户消息中识别输入源：
   - **URL**：以 `http://` 或 `https://` 开头的网址
   - **本地文件**：以 `.html` 或 `.htm` 结尾的文件路径
2. 确定输出目录。默认为工作区下的 `web2template_output/`。若用户指定了输出路径则使用用户指定的。
3. 向用户简要确认：将分析 `{源}` 并输出到 `{输出目录}`。

---

### 阶段 2：数据提取（运行脚本）

运行提取脚本，生成截图与结构化设计数据。

**脚本路径**：`{SKILL_DIR}/scripts/extract_and_capture.py`

**命令**（根据输入类型选择）：

```bash
# 分析在线网站
python "{SKILL_DIR}/scripts/extract_and_capture.py" --url "https://example.com" --output "./web2template_output"

# 分析本地 HTML 文件
python "{SKILL_DIR}/scripts/extract_and_capture.py" --file "./path/to/template.html" --output "./web2template_output"
```

> `{SKILL_DIR}` 为此 SKILL 所在目录的绝对路径（本项目中级为 `d:\trae_projects\beautiful_web_template\.trae\skills\web2template`）。

**脚本产出**：

| 产物 | 路径 | 用途 |
|------|------|------|
| 截图 01（顶部） | `{output}/screenshots/screenshot-01-top.png` | 视觉分析-首屏 |
| 截图 02（中部） | `{output}/screenshots/screenshot-02-middle.png` | 视觉分析-内容区 |
| 截图 03（底部） | `{output}/screenshots/screenshot-03-bottom.png` | 视觉分析-尾部 |
| 全页截图 | `{output}/screenshots/screenshot-full.png` | 整体视觉参考 |
| 设计数据 | `{output}/design_data.json` | 精确设计 Token |

**若脚本执行失败**：
- 提示用户安装依赖：`pip install playwright && playwright install chromium`
- 若为 URL 且网络超时，提示用户检查链接可访问性
- 若为本地文件，确认路径正确

**重型 SPA 抓取要点（已内置于脚本，排障时参考）**：
- 脚本使用 `domcontentloaded` 导航 + 有界 `networkidle` 宽限（20s）。若目标站持续有后台请求（analytics、字体、流式内容），旧的 `networkidle` 直等法会超时——脚本已修复，勿改回。
- 若仍超时：用 `curl.exe -s -o NUL -w "%{http_code} %{time_total}s" --max-time 15 {URL}` 分别测试直连与代理。注意：Chromium 不一定遵循 `HTTP(S)_PROXY` 环境变量，代理不通时直连往往更可靠。
- 若截图为空白或布局崩坏：加大 `LOAD_WAIT`，或检查站点是否有反爬（需改用本地 HTML 文件）。

---

### 阶段 3：视觉分析（Agent 多模态能力）

使用 Read 工具读取 3 张截图（01-top、02-middle、03-bottom），进行视觉分析。

**视觉分析维度**——对每张截图记录以下观察：

**配色与氛围**：
- 主色调（背景色、文字色、点缀色）
- 色彩温度（暖/冷/中性）
- 对比度水平（高对比/柔和/低对比）
- 整体氛围关键词（如"奢华科技"、"粗野朋克"、"柔和自然"）

**布局与结构**：
- 整体布局类型（单列/多列/非对称/网格）
- 各区块的视觉层级与排列方式
- 留白策略（慷慨/紧凑/密集）
- 装饰性元素（几何形状、插图、图案纹理）

**字体与排印**：
- 字体类型感知（衬线/无衬线/等宽/手写）
- 标题尺寸与字重印象
- 文字处理技巧（大写、渐变文字、描边等）

**组件与交互迹象**：
- 按钮形状与样式
- 卡片风格（圆角/硬边/玻璃/拟态）
- 阴影类型（柔和弥散/硬偏移/霓虹辉光/无阴影）
- 动画痕迹（从静态截图推断可能的动态效果）

**签名特征**：
- 此设计最独特、最可辨识的 3-5 个视觉元素

---

### 阶段 4：数据综合与归纳

读取 `design_data.json`，将精确数据与阶段 3 的视觉分析结合，形成结构化的风格归纳。

**读取 design_data.json** 后，重点关注以下字段并归纳：

| JSON 字段 | 归纳目标 |
|-----------|----------|
| `css_variables` | 提取 CSS 自定义属性，识别设计 Token 体系 |
| `color_palette` | 归纳色彩策略：主色、点缀色、背景色、边框色 |
| `typography` | 归纳字体系统：字体配对、字号阶梯、字重策略 |
| `spacing` | 归纳间距体系：区块间距、容器宽度、网格间隙 |
| `borders` | 归纳圆角与边框策略 |
| `shadows` | 归纳阴影系统 |
| `layout.sections` | 识别页面区块结构，为"布局创意"章节提供素材 |
| `animations` | 归纳动画与过渡策略 |
| `gradients` | 识别签名渐变 |
| `effects` | 识别滤镜、毛玻璃、变换等特殊效果 |
| `resources` | 识别字体来源与外部依赖 |

**综合归纳规则**：

1. **精确优先**：当视觉分析与 JSON 数据冲突时，以 JSON 精确数据为准（如具体色值、字号）
2. **补充语境**：用视觉分析为精确数据补充使用场景与设计意图
3. **归纳而非罗列**：不要简单复制 JSON 中的所有值，而是归纳出设计体系的规律
4. **识别模式**：从分散的数据中识别出设计模式（如"所有卡片使用 16px 圆角 + 柔和阴影"）

---

### 阶段 5：提示词文档生成

基于归纳结果，使用模板生成最终提示词文档。

**模板路径**：`{SKILL_DIR}/templates/prompt_template.md`

**生成规则**：

1. 读取模板文件
2. 将所有 `{{PLACEHOLDER}}` 替换为实际内容
3. 保持模板的核心结构（基本信息表 → 布局创意 → 完整提示词）
4. **根据源页面特点灵活调整**：
   - 若页面无定价区块，则"布局创意"中不写 Pricing
   - 若页面无动画，则"效果与动画"章节简述为"以静态为主"
   - 若页面为单屏落地页，则"布局创意"仅描述现有区块
5. **内容要求**：
   - 设计哲学：用感官语言描述，包含情感关键词与"此设计不是什么"
   - Token 系统：必须包含具体的 hex 值、px 值，以表格形式呈现
   - 组件样式：按实际页面中出现的组件类型描述
   - 大胆要素：提炼 3-8 个使此设计独特的签名技巧
   - 所有 CSS 代码示例必须可执行

**输出文件**：

将生成的提示词文档保存为 Markdown 文件：

```
{output}/style_prompt.md
```

文件名可根据风格命名，如 `glassmorphism_style_prompt.md`。

**完成后向用户报告**：
- 输出文件路径
- 截图目录路径
- design_data.json 路径
- 一句话风格总结

---

### 阶段 6：组件库模板生成（沉淀流程）

当用户要求"沉淀为 XX 风格"、"生成组件库/模板"时，基于阶段 5 的风格文档，在项目的 `templates/` 下创建正式模板。

**目录约定**（与项目现有 30+ 模板保持一致）：

```
templates/{Style-Name}/
├── {Style-Name}.html    # 单文件组件库，零构建依赖
└── {Style-Name}.md      # 风格提示词文档（复制 {output}/style_prompt.md）
```

**HTML 组件库构建规则**：

1. **Token 层优先**：`:root` 中完整落地风格文档的色彩/圆角/阴影/字体/动效变量，页面中所有组件只引用变量，禁止散落硬编码色值
2. **组件覆盖面**：至少包含 Header、Hero、按钮体系（主/次/描边/禁用）、卡片、输入框、徽章/标签、页脚；风格文档中的"签名元素"必须有对应展示区块
3. **深浅双模式**（若风格支持）：用 `html[data-theme="dark"]` 覆盖 Token 实现翻转，页脚提供切换钮，验证两套底色下组件均可读
4. **图片资源**：一律使用 `https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt={prompt}&image_size={size}` 链接（URL-encode prompt），禁止占位图。**关键陷阱**：该接口对新 prompt 首次请求返回"生成中"占位图（约 176KB 正方形 JPEG），真实图片需等待异步生成完成。优先复用项目中已就绪的 URL（grep `text_to_image` 查 index.html 与既有模板）；确需新图时，用 JPEG SOF 标记解析宽高（横向比例 = 就绪）轮询确认，未就绪则回退到已就绪图片并以不同 `background-position` 裁切区分多处使用
5. **动效克制**：入场动画用 IntersectionObserver 触发（2-8px 位移级别），必须实现 `prefers-reduced-motion` 降级
6. **响应式**：至少覆盖 1024px / 768px 两档断点，规则从风格文档"响应式策略"章节落地

---

### 阶段 7：画廊注册

新模板必须同步注册进三处，缺一则画廊不完整：

1. **`index.html`**：在 `templates` 数组中按字母序插入条目（勿改动数组其余部分与业务逻辑）：

```json
{"name": "{Style-Name}", "display": "{Display Name}", "description": "{一句话中文描述}", "tags": ["Light|Dark", "sans-serif|serif|mono"], "htmlPath": "./templates/{Style-Name}/{Style-Name}.html", "mdPath": "./templates/{Style-Name}/{Style-Name}.md", "shots": ["./assets/screenshots/{Style-Name}-01.png", "./assets/screenshots/{Style-Name}-02.png", "./assets/screenshots/{Style-Name}-03.png"]}
```

2. **`README.md`**：画廊章节按字母序插入条目（三张截图 + `>` 引用块中文描述，格式对齐相邻条目）
3. **`README_en.md`**：同位置插入英文条目

---

### 阶段 8：运行时验证与清理

**验证**（静态代码分析不能替代运行时证据）：

1. 编写临时 Playwright 验证脚本（放于 `{output}/` 下）：起本地 `http.server`，以 1440×900 视口加载新模板，等待字体与图片就绪
2. **必须收集 JS 错误**：`page.on("pageerror", ...)` 在 `goto` 之前注册，结束时打印——空数组才算通过
3. 强制 `.reveal` 元素可见后截图三视图，保存为 `assets/screenshots/{Style-Name}-01/02/03.png`（阶段 7 注册的路径依赖此产物）
4. 用 Read 工具逐张检查截图：图片是否为占位图、组件是否溢出/重叠、文字对比度、深色模式（若实现）
5. 发现问题 → 修复 HTML 后重跑脚本，直至截图全部合格

**清理**（验证通过后执行）：

- 删除 `{output}/`（默认 `web2template_output/`）中的全部过程产物：临时脚本、探测图片、design_data.json、抓取截图、style_prompt.md（其正式副本已在 `templates/{Style-Name}/`）
- 用 `git status --short` 确认最终变更集只含：新模板目录、三张截图、index.html、两个 README

---

## 输出规范

最终产出的提示词文档必须满足以下标准，使其可作为后续生成同风格页面的 Prompt 输入：

1. **可复现性**：包含足够的具体数值（色值、字号、间距、圆角、阴影值），使另一个 Agent 仅凭此文档即可还原相近视觉
2. **结构化**：遵循模板的章节结构，便于检索与引用
3. **设计意图**：不只描述"是什么"，更要解释"为什么"——设计选择的意图与气质
4. **签名特征**：明确提炼此风格区别于其他风格的核心特征
5. **实现导向**：包含可执行的 CSS 代码片段与组件实现建议

---

## 使用示例

### 示例 1：分析在线网站

```
用户：帮我分析 https://stripe.com 的设计风格，生成一份提示词文档

Agent 执行：
1. 识别输入为 URL
2. 运行：python "{SKILL_DIR}/scripts/extract_and_capture.py" --url "https://stripe.com" --output "./web2template_output"
3. 读取 3 张截图进行视觉分析
4. 读取 design_data.json 进行数据归纳
5. 基于模板生成 style_prompt.md
6. 报告输出路径与风格总结
```

### 示例 2：分析本地 HTML

```
用户：分析 ./templates/Glassmorphism/Glassmorphism.html 的设计风格

Agent 执行：
1. 识别输入为本地文件路径
2. 运行：python "{SKILL_DIR}/scripts/extract_and_capture.py" --file "./templates/Glassmorphism/Glassmorphism.html" --output "./web2template_output"
3-5. 同上
```

### 示例 3：分析后直接生成同风格页面

```
用户：分析这个网站 https://example.com 然后用同样的风格帮我做一个产品落地页

Agent 执行：
1. 先完成 web2template 全流程，生成 style_prompt.md
2. 将 style_prompt.md 的内容作为设计提示词
3. 基于该提示词构建新的产品落地页
```

### 示例 4：提取风格并沉淀为画廊模板（完整流程）

```
用户：提取 https://cursor.com 的浅色风格，沉淀为 Cursor-Light-Warmth 风格，并生成组件库

Agent 执行：
1. 阶段 1-5：抓取 → 视觉分析 → 数据归纳 → 生成 Cursor-Light-Warmth_style_prompt.md
2. 阶段 6：创建 templates/Cursor-Light-Warmth/{Cursor-Light-Warmth.html, .md}
3. 阶段 7：注册 index.html 条目 + README.md/README_en.md 画廊章节
4. 阶段 8：Playwright 截图验证（三视图存入 assets/screenshots/），清理过程文件
```

---

## 目录结构

```
d:\trae_projects\beautiful_web_template\.trae\skills\web2template\
├── SKILL.md                          # 本文件 - SKILL 入口说明
├── scripts/
│   └── extract_and_capture.py        # 核心提取脚本（截图 + 设计数据）
├── templates/
│   └── prompt_template.md            # 提示词输出模板
└── README.md                         # 使用说明
```

## 注意事项

- 提取脚本使用 1440×900 视口，以桌面端视图为准。移动端适配策略由 Agent 从 CSS 媒体查询中归纳。
- 脚本会强制显示动画隐藏元素（reveal/fade-in 等），确保截图反映最终状态。
- `design_data.json` 中的颜色值为 `rgb()` 格式，Agent 在生成提示词时应转换为 `#hex` 格式以提升可读性。
- 对于使用 CSS-in-JS 或 Tailwind 等工具的页面，`css_variables` 可能为空，此时依赖 `color_palette` 等计算样式字段。
- 若页面需要登录或有反爬机制，脚本可能无法正常获取内容，应提示用户改用本地 HTML 文件。
- **Windows PowerShell 环境**：`curl` 是 `Invoke-WebRequest` 别名，参数不兼容，须显式使用 `curl.exe`；含 `&`、引号嵌套的 URL 或长脚本不要内联 `python -c`，写成临时 `.py` 文件再执行。
- 阶段 6-8 产出的模板必须与项目既有模板（`templates/` 下 30+ 套）保持同样的工程约定：单文件、零构建、`:root` Token、`{Style-Name}.html` + `{Style-Name}.md` 成对出现。

# Monochrome

> 来源：[Design Prompts](https://www.designprompts.dev/monochrome)

## 基本信息

| 属性 | 值 |
|------|-----|
| 风格ID | `monochrome` |
| 显示名称 | Monochrome |
| 模式 | ☀️ 浅色模式 (Light) |
| 字体类型 | serif |
| 描述 | 建立在纯黑白之上的冷峻编辑设计系统。无点缀色——唯有戏剧性对比、超大衬线字体与精准的几何布局。唤起高端时尚编辑与建筑作品集的质感。克制、精致、不妥协的大胆。 |

## 布局创意 (Layout Ideas)

### Hero

全宽单列：徽章配圆点指示器、超大号标题（9xl）、装饰性粗水平线配小型带边框方块、副标题、双 CTA、信任指标。无图片——纯字体作 Hero 元素。粗 4px 底边框。

### Stats

横向条带，反相（黑底白字）。桌面 4 列网格，移动 2 列。数据间垂直分隔符。超大号展示衬线数字、小型大写标签、趋势信息。含蓄垂直线纹理叠加增深度。

### Product Detail

双栏编辑跨页配区块标签。左：大标题。右：正文，首段含方框首字下沉（带边框方块含首字母）。网格图案叠加增纹理。粗 4px 底边框。

### Features

密集 3 列网格，1px 间隙填充黑色。每张特性卡片含带边框图标盒 + 编号标签、标题、描述。卡片悬停反相（100ms 过渡）。粗 4px 底边框。

### How It Works

3 列居中布局。带边框方块盒配大号步骤编号，由水平线连接。下方标题 + 描述。对角线纹理叠加。粗 4px 底边框。

### Benefits

清单格式配超大号勾选标记（自定义 SVG，非图标）。收益作粗体标题配支持文字。交替对齐以增视觉趣味。

### Pricing

3 列网格配 1px 间隙。高亮档位反相（黑底）且桌面端垂直抬升（-my-8, py-16）配含蓄阴影。非高亮档位悬停背景变化。徽章、名称、价格、描述、特性列表、CTA 按钮。粗 4px 底边框。

### Testimonials

3 列网格，中间列下偏（mt-8）。超大号引号（10% 不透明度，悬停增加）。大号斜体引文，下方作者信息配悬停加粗的顶边框。粗 4px 底边框。

### Faq

手风琴配 plus/minus 图标。问题用粗体衬线，回答用较轻字重。每项粗底边框。无背景——仅线条与字体。

### Blog

3 列网格。每篇文章：带边框图片（灰度 → 悬停彩色，边框 2px→4px 加粗，图片 105% 缩放）、日期/作者元信息、标题、描述、'Read' 链接。粗 4px 底边框。

### Footer

密集、报纸风格页脚。多列布局配小型大写区块标题。社交图标为简单轮廓圆。粗顶边框。

---

## 完整提示词 (Full Prompt)

# 设计风格：Minimalist Monochrome

## 设计哲学

### 核心原则

**还原至本质。** Minimalist Monochrome 将设计剥至最基本元素：黑、白与字体。无点缀色可藏身，无渐变可柔化边缘，无阴影可造虚假深度。每个设计决策都必须凭自身价值立足。这是设计即纪律——克制成为表达的终极形式。

### 视觉气质

**情感关键词**：冷峻、权威、永恒、编辑感、智识、戏剧性、精致、锐利、自信、不妥协

这是以下事物的视觉语言：
- 高端时尚编辑（Vogue、Harper's Bazaar 封面）
- 建筑专著与博物馆图录
- 奢侈品牌标识（Chanel、Celine、Bottega Veneta）
- 获奖书籍设计与精美字体
- 画廊展览物料

设计通过自信赢得尊重。它不需色彩来有趣——它用尺度、对比、节奏与留白创造视觉戏剧。

### 此设计不是什么

- 多彩或俏皮
- 柔软、圆润或友好
- 基于渐变或带点缀色
- 重阴影或"抬升"
- 通用或模板化
- 繁忙或拥挤
- 类似"Minimalist Modern"（无蓝点缀、无渐变、无圆角）

### Minimalist Monochrome 的 DNA

#### 1. 纯黑白调色板
主要元素无灰——用真黑（#000000）与真白（#FFFFFF）。灰仅保留给次要文字与边框。鲜明对比创造即时视觉冲击并迫使刻意的层级决策。

#### 2. 衬线字体即 Hero
不同于现代无衬线极简，此风格拥抱古典衬线字体。衬线增添精致、编辑份量与永恒优雅。字体不只是内容——它是主要视觉元素。

#### 3. 超大字号阶梯
标题不只传达信息——它们主导。期望 8xl、9xl 及更大自定义尺寸。词成为图形元素。单词或短语可填满整个视口宽度。

#### 4. 基于线的视觉系统
替代填充形状、阴影或背景，此设计用线：发丝线、粗水平线、边框、下划线、删除线。线创造结构而无质量。

#### 5. 锐利几何精准
处处零 border-radius。完美 90 度角。精准对齐。几何是建筑性的——想象 Bauhaus 遇上编辑印刷设计。

#### 6. 戏剧性留白
留白不是空的——它是活跃的。慷慨的边距与内边距创造呼吸空间，使黑色元素更具冲击力。页面呼吸。

#### 7. 反相作强调
替代点缀色，用色彩反相（黑底白字）高亮重要元素。这在打破单色规则的同时创造戏剧性。

### 与 Minimalist Modern 的区别

| 方面 | Minimalist Modern | Minimalist Monochrome |
|--------|-------------------|----------------------|
| 色彩 | 蓝点缀 + 渐变 | 纯黑白 |
| 字体 | 无衬线（Inter） | 衬线（Playfair Display） |
| 角 | 圆（lg, xl, 2xl） | 锐（处处 0px） |
| 深度 | 阴影、辉光、抬升 | 扁平、2D、无阴影 |
| 视觉元素 | 渐变填充、彩色图标 | 线、边框、字体 |
| 气质 | 当代科技 | 编辑奢华 |
| 个性 | 自信亲和 | 冷峻威严 |

---

## 设计 Token 系统

### 色彩（严格单色）

```
background:       #FFFFFF (纯白)
foreground:       #000000 (纯黑)
muted:            #F5F5F5 (近白作含蓄背景)
mutedForeground:  #525252 (深灰作次要文字)
accent:           #000000 (黑即点缀)
accentForeground: #FFFFFF (黑上白)
border:           #000000 (黑边框)
borderLight:      #E5E5E5 (浅灰作含蓄分隔符)
card:             #FFFFFF (白卡片)
cardForeground:   #000000 (黑文字)
ring:             #000000 (黑聚焦环)
```

**规则**：绝无其他色。调色板绝对。

### 字体

**字体栈**：
- **展示/标题**：`"Playfair Display", Georgia, serif` — 优雅、高对比衬线，美丽斜体
- **正文**：`"Source Serif 4", Georgia, serif` — 高可读衬线用于长文本
- **等宽/标签**：`"JetBrains Mono", monospace` — 用于日期、元信息、技术细节

**字号阶梯**（戏剧范围）：
```
xs:   0.75rem   (12px) - 小字、元信息
sm:   0.875rem  (14px) - 说明、标签
base: 1rem     (16px) - 正文最小
lg:   1.125rem (18px) - 正文首选
xl:   1.25rem  (20px) - 引导段
2xl:  1.5rem   (24px) - 区块引言
3xl:  2rem     (32px) - 副标题
4xl:  2.5rem   (40px) - 区块标题
5xl:  3.5rem   (56px) - 页面标题
6xl:  4.5rem   (72px) - Hero 副标题
7xl:  6rem     (96px) - Hero 标题
8xl:  8rem     (128px) - 展示标题
9xl:  10rem    (160px) - 超大陈述
```

**字距与行高**：
- 标题：`tracking-tight`（-0.025em）或 `tracking-tighter`（-0.05em）
- 正文：`tracking-normal`（0）
- 小型大写/标签：`tracking-widest`（0.1em）
- 行高：展示用 `leading-none`（1），正文用 `leading-relaxed`（1.625）

### 圆角

```
所有值：0px
```

无例外。每个元素都有锐利 90 度角。这不可妥协，定义了风格的建筑特质。

### 边框与线

```
hairline:  1px solid #E5E5E5  (含蓄分隔符)
thin:      1px solid #000000  (标准边框)
medium:    2px solid #000000  (强调边框)
thick:     4px solid #000000  (重水平线、区块分隔符)
ultra:     8px solid #000000  (最大冲击)
```

**用法**：
- 区块间水平线（thick 或 ultra）
- 列间垂直分隔符（thin）
- 卡片边框（thin 或 medium）
- 链接下划线（thin，悬停）

### 阴影

```
无
```

此设计零投影。深度通过以下创造：
- 色彩反相（黑白互换）
- 边框粗细变化
- 尺度对比
- 留白

### 纹理与图案

**关键**：这些纹理为防扁平设计所必需。跨区块战略性应用。

**主图案：水平线（全局）**
```css
background-image: repeating-linear-gradient(
  0deg,
  transparent,
  transparent 1px,
  #000 1px,
  #000 2px
);
background-size: 100% 4px;
opacity: 0.015;
```

**次图案：网格（用于编辑区块如 Product Detail）**
```css
background-image:
  linear-gradient(#00000008 1px, transparent 1px),
  linear-gradient(90deg, #00000008 1px, transparent 1px);
background-size: 40px 40px;
opacity: 0.015;
```

**对角线（用于流程/时间线区块）**
```css
background-image: repeating-linear-gradient(
  45deg,
  transparent,
  transparent 40px,
  #00000008 40px,
  #00000008 42px
);
opacity: 0.01;
```

**噪点纹理（全局，增纸张质感）**
```css
background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
opacity: 0.02;
```

**反相区块纹理**
深色背景（Stats、Final CTA）用白色纹理：
```css
/* Stats 垂直线 */
background-image: repeating-linear-gradient(
  90deg,
  transparent,
  transparent 1px,
  #fff 1px,
  #fff 2px
);
background-size: 4px 100%;
opacity: 0.03;

/* Final CTA 径向渐变 */
background-image: radial-gradient(
  circle at top center,
  #ffffff,
  transparent 70%
);
opacity: 0.05;
```

---

## 组件样式

### 按钮

**主按钮**：
```
- 背景：#000000（黑）
- 文字：#FFFFFF（白）
- 边框：无
- 内边距：px-8 py-4（慷慨）
- 字体：大写，tracking-widest，font-medium，text-sm
- 悬停：反相为白底、黑字、黑边框
- 过渡：即时（无缓动，0ms 或最大 100ms）
```

**次/描边按钮**：
```
- 背景：透明
- 文字：#000000
- 边框：2px solid #000000
- 悬停：填充黑，文字白
```

**幽灵按钮**：
```
- 背景：透明
- 文字：#000000
- 边框：无
- 文字装饰：悬停下划线
- 样式：看似文字链接
```

**按钮形状**：始终矩形，绝不圆。考虑为 CTA 加小箭头（→）。

### 卡片/容器

**标准卡片**：
```
- 背景：#FFFFFF
- 边框：1px solid #000000
- 内边距：p-6 或 p-8
- 无阴影，无圆角
```

**反相卡片**（作强调）：
```
- 背景：#000000
- 文字：#FFFFFF
- 边框：无
- 克制用于高亮内容
```

**无边框卡片**：
```
- 无边框，无背景
- 内容由慷慨留白分隔
- 需要时上下加水平线
```

### 输入框

**文本输入**：
```
- 背景：#FFFFFF
- 边框：2px solid #000000（仅底，或全）
- 无圆角
- 占位符：#525252 斜体
- 聚焦：边框加粗至 3px 或 4px
- 无彩色聚焦环——仅边框变化
```

**文本区**：同输入，带可见 resize 手柄。

---

## 布局策略

### 容器
```
max-width: max-w-6xl (72rem / 1152px)
padding: px-6 md:px-8 lg:px-12
```

### 区块间距
```
垂直内边距：py-24 md:py-32 lg:py-40
区块间：粗水平线（4px 或 8px 黑）
```

### 网格系统
- 用 CSS Grid 精准控制
- 12 列基础网格以增灵活
- 强对齐垂直节奏

---

## 效果与动画

**运动哲学**：**极简与即时**

此设计偏好静止与即时状态变化。动画存在时：
- **即时**：最大 0-100ms 过渡
- **二元**：锐利开关状态，非渐进
- **有目的**：仅用于状态变化（悬停、聚焦）

**悬停效果**（已应用）：
- **卡片/特性**：完整色彩反相（背景、文字、边框）配 100ms 过渡
- **按钮**：色彩反相配 transition-none 以即时反馈
- **博客图片**：边框加粗（2px → 4px），图片 105% 缩放并移除灰度（300ms）
- **链接**：下划线出现（即时）
- **证言**：引号不透明度增加，底边框加粗

**聚焦状态**（需可访问性）：
- **按钮**：3px solid outline 配 3px offset
- **输入框**：边框从 2px 加粗至 4px（仅底）
- **链接**：边框出现/加粗
- **交互元素**：3px solid outline 配 2px offset
- 所有 outline 用 `focus-visible` 以免鼠标点击轮廓

**具体实现**：
```tsx
// 特性卡片悬停
className="group bg-[var(--background)] p-8 transition-colors duration-100 hover:bg-[var(--foreground)] hover:text-[var(--background)]"

// 博客图片悬停
className="border-2 transition-all duration-100 group-hover:border-[4px]"
className="grayscale transition-all duration-300 group-hover:scale-105 group-hover:grayscale-0"

// 证言悬停
className="group-hover:opacity-20 transition-opacity duration-100" // 引号
className="transition-all duration-100 group-hover:border-t-[3px]" // 边框
```

**不要**：
- 弹跳动画
- 浮动元素
- 视差滚动
- 缓慢缓动函数
- 渐变动画

---

## 图标

**样式**：轮廓、细描边（strokeWidth：1 或 1.5）

**用法**：
- 图标置于黑描边白填充圆内
- 或独立无容器
- 尺寸：一致 20px 或 24px
- 颜色：始终黑（#000000）

**Lucide 图标设置**：
```tsx
<Icon size={20} strokeWidth={1.5} className="text-black" />
```

---

## 响应式策略

**移动端适配**：
- 保持锐角与黑白调色板
- 缩减超大标题（9xl → 移动 5xl）
- 列垂直堆叠
- 边框变全宽水平线
- 保持慷慨垂直间距

**关键原则**：单色戏剧必须在移动端存活。勿默认通用移动模式。

---

## 可访问性

**对比**：纯黑于白超过 WCAG AAA 要求（21:1 比例）。

**聚焦状态**（所有交互元素必需）：
```
按钮与主要交互元素：
- Outline：3px solid #000000
- Outline-offset：3px
- 用 focus-visible 以免鼠标点击轮廓

文本输入：
- 聚焦时边框从 2px 加粗至 4px
- 仅底边框
- 无 outline（边框变化足够）

导航链接：
- focus-visible 时边框出现/加粗
- 与悬停状态一致

次要交互元素（社交图标、FAQ 按钮）：
- Outline：3px solid #000000
- Outline-offset：2px
```

**实现**：
```tsx
// 按钮聚焦
focus-visible:outline focus-visible:outline-3 focus-visible:outline-[var(--foreground)] focus-visible:outline-offset-3

// 输入聚焦
focus:border-b-[4px] focus:outline-none focus-visible:border-b-[4px]

// 链接聚焦
focus-visible:border-[var(--foreground)] focus-visible:outline-none
```

**跳转链接**：页面顶部可见黑色按钮。

**触控目标**：移动端所有交互元素最小 44px×44px。

---

## 标志性选择（不可妥协）

1. **超大 Hero 字体**：至少一词 8xl 或更大（桌面 9xl）
2. **Hero 装饰元素**：粗水平线配小型带边框方块作视觉标点
3. **反相 Stats 区块**：黑底白字，配含蓄垂直线纹理
4. **无点缀色**：抵制诱惑——黑即点缀
5. **重水平线**：所有主要区块间 4px 黑线
6. **编辑引文**：证言作大号斜体衬线配超大引号
7. **处处锐利**：所有元素零 border-radius
8. **即时交互**：最大 100ms 过渡，大多即时
9. **字体即图形**：标题作视觉元素功能，非仅文字
10. **分层纹理**：多个含蓄图案增深度（非扁平设计）
11. **方框首字下沉**：Product Detail 首段有带边框方框首字下沉
12. **抬升定价档位**：高亮档位桌面端垂直延伸
13. **悬停反相**：特性卡片与定价档位悬停反相
14. **图片边框加粗**：博客图片悬停边框加粗配缩放效果

---

## 成功是什么样

成功实现的 Minimalist Monochrome 设计应感觉如：
- 翻开高端时尚杂志
- 漫步现代艺术画廊
- 阅读获奖建筑专著
- 浏览奢侈品牌网站

不应感觉如：
- 通用网站模板
- 科技初创落地页
- "需要一点色彩"之物
- Minimalist Modern 去色版

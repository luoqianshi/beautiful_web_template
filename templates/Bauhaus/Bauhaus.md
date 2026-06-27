# Bauhaus

> 来源：[Design Prompts](https://www.designprompts.dev/bauhaus)

## 基本信息

| 属性 | 值 |
|------|-----|
| 风格ID | `bauhaus` |
| 显示名称 | Bauhaus |
| 模式 | ☀️ 浅色模式 (Light) |
| 字体类型 | sans-serif |
| 描述 | 大胆的几何现代主义，以圆、方、三角为基本形。三原色（红/蓝/黄）调色板配以硬朗黑边和硬阴影。兼具功能性与构成主义不对称的艺术感。 |

## 布局创意 (Layout Ideas)

### Hero

分屏布局（50/50），白色背景上为文字，蓝色上为几何构图。超大号大写字体配左侧彩色点缀边框。

### Stats

等宽网格配分隔符。每个数据含几何形状图标（圆/方/菱形），编号 1-4。黄色背景区块配白色卡片。

### Features

三列网格，带角部装饰（圆/三角/方）的上浮卡片。每张卡片含带边框容器中的几何图标。悬停上浮效果。

### How It Works

横向时间线配粗连接线（仅桌面端）。步骤用交替的几何形状（圆/方/旋转方）作编号。移动端为双列网格。

### Benefits

红色背景上的白色卡片网格。每张卡片含带勾选标记的圆形黄色图标。干净边框与硬阴影。

### Pricing

三列布局，中间档位上浮并以黄色背景高亮。所有档位含几何标题与方形项目符号。

### Testimonials

三列网格，卡片含定位其上的圆形头像镂空。引号图标与带边框区块。装饰性角部元素。

### Faq

厚边框手风琴。激活项为红色背景白字。非激活项为白色。展开内容为黄色背景。

### Blog

蓝色背景上的三列白色卡片网格。图片在圆形与方形蒙版间交替。灰度图片，悬停时彩色。

### Footer

深色背景（近黑 #121212）配几何 logo。多列布局，社交图标为带边框方块。极简链接悬停状态。

---

## 完整提示词 (Full Prompt)

# 设计风格：Bauhaus

## 1. 设计哲学
Bauhaus 风格体现了"形式追随功能"的革命性原则，同时赞颂纯粹的几何之美与三原色理论。这是**构成主义现代主义**——每个元素都由圆、方、三角刻意构成。美学应唤起 1920 年代的 Bauhaus 海报：大胆、不对称、建筑化、毫不掩饰的图形感。

**气质**：构成主义、几何、现代主义、艺术而功能、大胆、建筑化

**核心概念**：界面不只是布局——它是一幅**几何构图**。每个区块是被构造而非被设计的。把页面想象成活过来的 Bauhaus 海报：形状重叠、边框厚重而刻意、色彩为纯三原色（红 #D02020、蓝 #1040C0、黄 #F0C020），一切由硬朗的黑（#121212）与干净的白奠定。

**关键特征**：
- **几何纯粹**：所有装饰元素源自圆、方、三角
- **硬阴影**：4px 与 8px 偏移阴影（绝不柔和/模糊）通过分层营造深度
- **色块**：整块区块使用纯三原色作背景
- **粗边框**：2px 与 4px 黑边界定每个主要元素
- **不对称平衡**：使用网格但刻意以重叠元素打破
- **构成主义字体**：超大号大写标题（text-6xl 至 text-8xl）配紧凑字距
- **功能诚实**：无渐变、无含蓄效果——一切直接而明确

## 2. 设计 Token 系统（DNA）

### 色彩（单一调色板 — 浅色模式）
调色板严格限于 Bauhaus 三原色，加上硬朗的黑白。
-   `background`：`#F0F0F0`（灰白画布）
-   `foreground`：`#121212`（硬朗黑）
-   `primary-red`：`#D02020`（Bauhaus 红）
-   `primary-blue`：`#1040C0`（Bauhaus 蓝）
-   `primary-yellow`：`#F0C020`（Bauhaus 黄）
-   `border`：`#121212`（厚重、分明的边框）
-   `muted`：`#E0E0E0`

### 字体
-   **字族**：**'Outfit'**（来自 Google Fonts 的几何无衬线）。该字体的圆形字形与干净几何完美体现 Bauhaus 原则。
-   **字体导入**：`Outfit:wght@400;500;700;900`
-   **字号阶梯**：展示与正文间极端对比
    -   展示：text-4xl（移动）→ text-6xl（平板）→ text-8xl（桌面）
    -   副标题：text-2xl → text-3xl → text-4xl
    -   正文：text-base → text-lg
-   **字重**：
    -   标题：font-black（900）配大写与 tracking-tighter
    -   副标题：font-bold（700）配大写
    -   正文：font-medium（500）以保可读性
    -   标签：font-bold（700）配大写与 tracking-widest
-   **行高**：标题紧凑（leading-[0.9]），正文宽松（leading-relaxed）

### 圆角与边框
-   **圆角**：二元极端——要么 `rounded-none`（0px）用于方/矩形，要么 `rounded-full`（9999px）用于圆。无中间圆角。
-   **边框宽度**：
    -   移动：`border-2`（2px）
    -   桌面：`border-4`（4px）
    -   导航/主要分割：`border-b-4`（4px 底边框）
-   **边框色**：始终 `#121212`（黑）以最大对比

### 阴影/效果
-   **硬偏移阴影**（受 Bauhaus 分层启发）：
    -   小：`shadow-[3px_3px_0px_0px_black]` 或 `shadow-[4px_4px_0px_0px_black]`
    -   中：`shadow-[6px_6px_0px_0px_black]`
    -   大：`shadow-[8px_8px_0px_0px_black]`
-   **按钮按下效果**：`active:translate-x-[2px] active:translate-y-[2px] active:shadow-none`（模拟物理按键）
-   **卡片悬停**：`hover:-translate-y-1` 或 `hover:-translate-y-2`（含蓄上浮）
-   **图案**：用 CSS 背景图案增添纹理
    -   点阵：`radial-gradient(#fff 2px, transparent 2px)` 配 `background-size: 20px 20px`
    -   不透明度叠加：10-20% 不透明度的大型几何形状作背景装饰

## 3. 组件样式

### 按钮
-   **变体**：
    -   **主**（红）：`bg-[#D02020] text-white border-2 border-black shadow-[4px_4px_0px_0px_black]`
    -   **次**（蓝）：`bg-[#1040C0] text-white border-2 border-black shadow-[4px_4px_0px_0px_black]`
    -   **黄**：`bg-[#F0C020] text-black border-2 border-black shadow-[4px_4px_0px_0px_black]`
    -   **描边**：`bg-white text-black border-2 border-black shadow-[4px_4px_0px_0px_black]`
    -   **幽灵**：`border-none text-black hover:bg-gray-200`
-   **形状**：要么 `rounded-none`（方）要么 `rounded-full`（胶囊）。刻意使用形状变体。
-   **状态**：
    -   悬停：轻微不透明度变化（`hover:bg-[color]/90`）
    -   激活：按钮"按下"（`active:translate-x-[2px] active:translate-y-[2px] active:shadow-none`）
    -   聚焦：2px offset ring
-   **字体**：大写，font-bold，tracking-wider

### 卡片
-   **基础样式**：白底，`border-4 border-black`，`shadow-[8px_8px_0px_0px_black]`
-   **装饰**：右上角小型几何形状（8px x 8px）：
    -   圆：`rounded-full bg-[primary-color]`
    -   方：`rounded-none bg-[primary-color]`
    -   三角：CSS clip-path `polygon(50% 0%, 0% 100%, 100% 100%)`
-   **悬停**：`hover:-translate-y-1`（含蓄上浮效果）
-   **内容层级**：大号粗体标题、中等正文、慷慨内边距

### 手风琴（FAQ）
-   **关闭状态**：白底，`border-4 border-black`，`shadow-[4px_4px_0px_0px_black]`
-   **打开状态**：红色背景（`bg-[#D02020]`），头部白字
-   **展开内容**：浅黄背景（`bg-[#FFF9C4]`），黑字，`border-t-4 border-black`
-   **图标**：ChevronDown，打开时 `rotate-180`

## 4. 布局与间距
-   **容器宽度**：主要内容区块用 `max-w-7xl`（营造海报般的宽阔感）
-   **区块内边距**：
    -   移动：`py-12 px-4`
    -   平板：`py-16 px-6`
    -   桌面：`py-24 px-8`
-   **网格系统**：
    -   数据：1 列（移动）→ 2 列（平板）→ 4 列（桌面），配 `divide-y` 与 `divide-x` 边框
    -   特性：1 列 → 2 列 → 3 列，8px 间隙
    -   定价：1 列 → 3 列（桌面端中间上浮）
-   **间距阶梯**：一致使用 4px、8px、12px、16px、24px
-   **区块分隔符**：每个区块有 `border-b-4 border-black`，创造强烈的横向节奏

## 5. 非通用性（标志性选择）

**此设计绝不可看起来像通用 Tailwind 或 Bootstrap。以下为强制要求：**

-   **色块**：整块区块使用纯三原色作背景：
    -   Hero 右面板：蓝（`bg-[#1040C0]`）
    -   数据区块：黄（`bg-[#F0C020]`）
    -   博客区块：蓝（`bg-[#1040C0]`）
    -   收益区块：红（`bg-[#D02020]`）
    -   最终 CTA：黄（`bg-[#F0C020]`）
    -   页脚：近黑（`bg-[#121212]`）

-   **几何 logo**：导航含三个几何形状（圆、方、三角），以三原色构成品牌标识

-   **几何构图**：使用重叠形状的抽象构图：
    -   Hero 右面板：重叠的圆、旋转方块与居中方块配三角
    -   Product Detail：由圆、方与对角线构造的抽象几何"面孔"
    -   最终 CTA：角落 50% 不透明度的大型装饰形状（圆与旋转方块）

-   **旋转元素**：刻意的 45° 旋转应用于：
    -   重复图案中每第 3 个形状
    -   "How It Works" 的步骤编号（内部内容反向旋转）
    -   装饰性背景形状

-   **图片处理**：
    -   博客图片：在 `rounded-full` 与 `rounded-none` 间交替，灰度滤镜配 `hover:grayscale-0`
    -   证言头像：圆形裁切配 `rounded-full` 与灰度滤镜

-   **独特装饰**：卡片角部小型几何形状（8px-16px），三原色轮换使用

## 6. 图标与图像
-   **图标库**：`lucide-react`（Circle, Square, Triangle, Check, Quote, ArrowRight, ChevronDown）
-   **图标样式**：
    -   描边宽度：2px（默认）或 3px（强调）
    -   尺寸：h-6 w-6 至 h-8 w-8
    -   颜色：匹配区块点缀色，或彩色背景上的白
-   **图标集成**：图标置于带边框几何容器内：
    -   特性：带阴影白色边框盒中的图标
    -   收益：黄色圆形徽章中的勾选图标
    -   数据：几何形状（圆/方/旋转方）中的数字
-   **图片处理**：所有图片默认灰度滤镜，悬停时彩色

## 7. 响应式策略
-   **移动优先方法**：从单列布局开始，在更大屏幕扩展为网格
-   **断点**：
    -   移动：< 640px（sm）
    -   平板：640px - 1024px（sm 至 lg）
    -   桌面：> 1024px（lg+）
-   **字体缩放**：所有文字使用响应式类（text-4xl sm:text-6xl lg:text-8xl）
-   **边框/阴影缩放**：移动端减小边框与阴影尺寸（border-2 → border-4，shadow-[3px] → shadow-[8px]）
-   **导航**：移动端（< 768px）汉堡菜单按钮，桌面端完整导航
-   **网格适配**：
    -   数据：1 列 → 2 列（sm）→ 4 列（lg）
    -   特性：1 列 → 2 列（md）→ 3 列（lg）
    -   How It Works：1 列 → 2 列（sm）→ 4 列（md），移动端隐藏连接线

## 8. 动画与微交互
-   **质感**：机械、利落、几何（无柔和有机运动）
-   **过渡时长**：`duration-200` 或 `duration-300`（快速而果断）
-   **缓动**：`ease-out`（机械感）
-   **交互**：
    -   按钮按下：位移并移除阴影（`active:translate-x-[2px] active:translate-y-[2px] active:shadow-none`）
    -   卡片悬停：向上抬升（`hover:-translate-y-1` 或 `hover:-translate-y-2`）
    -   手风琴：ChevronDown 旋转（`rotate-180`）与配 max-height 过渡的内容显现
    -   图标悬停：成组形状放大（`group-hover:scale-110`）
    -   链接悬停：色彩变为点缀色
-   **背景图案**：静态（图案无动画）

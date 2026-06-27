# Neo-brutalism

> 来源：[Design Prompts](https://www.designprompts.dev/neo-brutalism)

## 基本信息

| 属性 | 值 |
|------|-----|
| 风格ID | `neo-brutalism` |
| 显示名称 | Neo-brutalism |
| 模式 | ☀️ 浅色模式 (Light) |
| 字体类型 | sans-serif |
| 描述 | 模仿印刷设计与 DIY 朋克文化的原始高对比美学。奶油色背景、粗黑边框（4px）、零模糊硬偏移阴影、冲突的鲜艳色（热红、明黄、柔紫），以及重字重的 Space Grotesk 字体。拥抱不对称、旋转、贴纸式层叠与有组织的视觉混乱。 |

## 布局创意 (Layout Ideas)

### Hero

非对称分割配巨型旋转标题文字块。左侧含带边框文字块，不同色彩与旋转。右侧为"视觉混乱"容器，配重叠形状与徽章。CTA 用粗野阴影，悬停时位移。完全响应式，移动端堆叠布局。

### Stats

4 列粗野网格（平板 2 列，移动 1 列），黑底上粗白边框。悬停反相为点缀色。每个数据有超大号数字（text-7xl）、大写标签与装饰条。无图标，仅原始数字数据。

### Features

3 列网格（移动 1 列），卡片配粗黑边框与 8px 偏移阴影。图标置于带边框彩色点缀盒内。卡片头部有编号徽章与边框分隔符。悬停时卡片向上抬升配更深阴影。

### How It Works

3 个居中方框（移动堆叠），桌面端以虚线连接。每步顶部有大型旋转编号徽章配点缀背景与粗边框。悬停时徽章旋转更多。顶部有胶囊形流程徽章。

### Benefits

双栏分割（移动堆叠）。左：鲜艳红点缀配径向圆点图案叠加，巨型白字配文字阴影，旋转白卡片作副标题。右：干净奶油色背景配粗体列表项，方形项目符号悬停变色。

### Pricing

3 列卡片网格（移动 1 列）配巨型硬阴影（12-16px）。高亮方案轻微放大并用黑头白字。价格数字巨大（text-6xl）。特性用自定义勾选框项目符号。顶部装饰图案边框。

### Testimonials

无限横向跑马灯（react-fast-marquee）配渐变淡入边缘。卡片为白色配粗边框与大阴影。5 星评分作大号文字。作者区有带边框头像与独立背景。

### Faq

堆叠手风琴配 details/summary。每项为粗边框卡片配阴影。打开状态旋转 +/X 图标并显现边框分隔符。问题用粗体大写。回答在不同背景（neo-muted）。

### Blog

3 列网格（移动 1 列）。卡片配粗边框。图片灰度配日期徽章叠加。悬停恢复彩色并缩放图片。标题悬停下划线。作者区底部有边框分隔符。

### Footer

黄色背景配粗顶边框。logo 为旋转文字块。导航链接为粗体大写，悬停状态反相为黑底。社交图标为带边框方块配阴影。

---

## 完整提示词 (Full Prompt)

# 设计风格：Neo-brutalism

## 设计哲学

**Neo-brutalism（或 Neu-Brutalism）** 是数字朋克对主导 2010 年代的"Corporate Memphis"与精致"Clean SaaS"美学的反叛。传统粗野主义（建筑/早期网页）功利而单调，而 **Neo-brutalism** 鲜艳、表演性、刻意独特。它结合粗野主义原始未精炼的结构诚实与波普艺术的高饱和能量、早期互联网的"贴纸"文化，以及 DIY 杂志设计的叛逆精神。

**核心 DNA 与基本原则**：

1.  **毫不妥协的可见性（反含蓄）**：现代设计常试图隐形——漂浮于渐变上的无边框卡片、几乎不存在的柔和阴影、模糊结构的模糊效果。Neo-brutalism 完全拒绝这点。它要求被看见。结构非暗示；而是以**粗硬黑线强制**（处处 `border-4`）。阴影非模拟光弥散；而是**实心墨块**以 45 度角偏移（8px、12px、16px 偏移配零模糊）。每个元素都有**视觉重量与存在感**。

2.  **数字触感（贴纸效果）**：屏幕不被视为流畅玻璃表面，而是**拼贴板或公告板**。元素感觉如物理贴纸、纸剪纸或层叠印刷卡片。它们有"物理性"——按钮**机械下压**（translate X 与 Y 覆盖其阴影），卡片**物理抬起**（上移同时阴影增大），文字块**如贴纸般斜贴旋转**（`rotate-1`、`-rotate-2`）。这创造有形、近乎雕塑的界面。

3.  **有组织的混乱（受控的凌乱）**：设计拥抱"计划的凌乱"——看似自发实则精心编排。容器与文字用**轻微旋转**（`-rotate-2`、`rotate-1`、`rotate-3`）打破网格单调。元素**有意重叠**（浮动装饰形状、绝对定位徽章）。**鼓励非对称**——标题跨行分割配不同色彩与旋转，布局偏好 60/40 而非完美 50/50。然而底层结构保持**僵硬功能**以确保可用性。它是"丑酷"——按传统精致标准丑，按叛逆意图酷。

4.  **默认与原始（Web 1.0 致敬）**：美学赞颂 CSS3 平滑一切之前的"默认"网页外观。用**纯黑**（`#000000`）作所有边框与文字——无含蓄灰。用**高饱和原色**（热红 `#FF6B6B`、明黄 `#FFD93D`、柔紫 `#C4B5FD`）感觉如未混合颜料或荧光笔。字体**粗重**（仅 700 与 900 字重）。**奶油背景**（`#FFFDF5`）模仿陈年纸张或报纸，拒绝刺眼白。

5.  **极繁即声明**：现代设计趋向极简，neo-brutalism **刻意极繁**。更多边框。更多阴影。更多大写文字。更多视觉噪音（半调图案、网格叠加、噪点纹理）。这不是视觉杂乱——而是用于创造能量与紧迫感的**视觉密度**。

6.  **反讽与自信**：风格散发反讽与自我意识。它说："我知道这看起来不精致，而这正是它好的原因。"它需**自信**才能驾驭；Neo-brutalism 中无怯懦空间。它反企业、反平滑、反无聊。

7.  **机械交互**：交互感觉**机械且令人满足**，非流畅飘渺。按钮不淡入或发光——它们**咔嗒下压**如物理开关。悬停不柔化——它们**snap** 就位。过渡**快速**（`duration-100`、`duration-200`）且**直接**，创造利落、街机游戏般的响应。

**气质与情感基调**：
*   **怀旧与复古现代**：汲取 Y2K 能量、90 年代朋克杂志、DIY 传单、锐舞海报与早期网络论坛。
*   **能量与大声**：它**呐喊**而非低语。它激进地抓住注意。
*   **俏皮而功能**：用**游戏化交互**（弹跳悬停、硬点击、旋转徽章）使功利软件感觉如玩具或游戏。
*   **反企业真实**：拒绝企业设计系统的精致外衣，拥抱原始与不完美作诚实。
*   **自信大胆**：每个设计选择都**刻意且夸张**。无含蓄之物。

**视觉签名（即时可辨之处）**：
*   **硬黑描边**：统一视觉元素。**若无边框，即不存在。** `border-4` 是默认。所有边框为实心黑。
*   **偏移硬阴影**：阴影是**零模糊实心矩形**，以 45 度角偏移（右下）。小：`4px 4px 0px 0px #000`。中：`8px 8px 0px 0px #000`。大：`12px 12px 0px 0px #000`。巨：`16px 16px 0px 0px #000`。
*   **"波普"调色板**：奶油背景（`#FFFDF5`）作中性画布供**荧光色爆发**（红、黄、紫）。黑是结构色。白用于对比面板。
*   **字体即纹理**：巨型粗字体（**Space Grotesk 900 字重**）常配文字轮廓（`-webkit-text-stroke: 2px black` 配透明填充）或置于带边框彩色盒内高亮。**全大写**作强调。极端字距（标题 `tracking-tighter`，标签 `tracking-widest`）。
*   **贴纸层叠**：文字块、徽章与容器**旋转层叠**如笔记本上贴纸。元素向"下方"元素投射硬阴影。
*   **纹理与图案**：背景不扁平。用**半调圆点**（径向渐变）、**网格图案**（线性渐变线）、**噪点纹理**（SVG 滤镜）与**几何叠加**增添视觉丰富而无传统深度。
*   **非对称构图**：刻意**打破网格**。标题不均分割。区块用 60/40 或 70/30 分割。元素离轴浮动。

**Neo-brutalism 不是什么**：
*   **不极简**：它极繁且密集。
*   **不流畅**：它锯齿、锐利、棱角分明。
*   **不含蓄**：它大声、高对比、直击面门。
*   **不精致**：它赞颂粗糙与原始。
*   **不企业**：它美学 DNA 叛逆反建制。

## 设计 Token 系统（DNA）

### 色彩（高饱和浅色模式调色板）
Neo-brutalism 用**单一、明确的浅色模式调色板**。所有色彩高饱和且毫不妥协。

*   **Background（画布）**：`#FFFDF5`（奶油/近白）
    *   暖、纸般背景模仿陈年报纸或再生纸。比刺眼白更柔，更真实。
    *   用：主页面背景、卡片内部、对比面板。

*   **Foreground（墨）**：`#000000`（纯黑）
    *   结构色。用于所有文字、所有边框、所有阴影。无灰，无变化。
    *   用：文字、边框（`border-black`）、阴影、图标。

*   **Accent（热红）**：`#FF6B6B`
    *   主操作色。鲜艳、能量、吸睛。
    *   用：主按钮（`bg-neo-accent`）、悬停状态、重要徽章、CTA 背景。

*   **Secondary（明黄）**：`#FFD93D`
    *   次高亮色。明亮、欢快、高能量。
    *   用：次按钮、徽章、logo 背景、页脚背景、交替区块背景。

*   **Muted（柔紫）**：`#C4B5FD`
    *   三级色增深度与变化而不冲突。
    *   用：含蓄背景（`bg-neo-muted`）、卡片头部、FAQ 回答背景、装饰元素。

*   **White**：`#FFFFFF`
    *   用于深色背景上高对比文字（如黑区块、点缀按钮）。
    *   用：黑背景上文字、反相按钮、对比面板。

**用色规则**：
- **绝不用含蓄灰。** 是黑或色，绝非 #333 或 #666。
- **强制高对比。** 所有文字必须在其背景上达 WCAG AA。
- **色块：** 区块在奶油、次色、柔和与黑间交替以创视觉节奏。

### 字体
*   **字族**：`Space Grotesk`（Google Font：`font-family: 'Space Grotesk', sans-serif`）
    *   几何无衬线配古怪个性。现代但不冷漠。足够粗以承载重字重。
    *   通过 Google Fonts 加载：`https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700;900&display=block`

*   **字重**：**仅允许重字重。**
    *   **Black (900)**：所有标题（h1, h2, h3）。`font-black`
    *   **Bold (700)**：所有正文、标签、按钮。`font-bold`
    *   **Medium (500)**：克制，仅含蓄强调。`font-medium`
    *   **Regular (400)**：一般避免。neo-brutalism 中禁止轻盈。

*   **字号阶梯**：
    *   展示：`text-8xl` 至 `text-9xl`（96px 至 128px）作 Hero 标题。
    *   标题 2：`text-6xl` 至 `text-8xl`（60px 至 96px）作区块标题。
    *   标题 3：`text-4xl` 至 `text-5xl`（36px 至 48px）作子标题。
    *   大正文：`text-2xl` 至 `text-3xl`（24px 至 30px）作强调。
    *   正文：`text-lg` 至 `text-xl`（18px 至 20px）作可读文字。
    *   小：`text-sm` 至 `text-base`（14px 至 16px）作标签与元信息。

*   **样式技巧**：
    *   **文字描边（展示）**：用 `-webkit-text-stroke: 2px black` 配 `color: transparent` 作巨型空心轮廓文字。
    *   **大小写**：大量使用**大写**（`uppercase`）于标题、标签、按钮与强调。正文可小写。
    *   **字距**：
        *   标题：`tracking-tighter` 或 `tracking-tight` 以增密度。
        *   标签：`tracking-widest` 或 `tracking-[0.2em]` 以增强调。
    *   **行高**：紧凑行高。展示用 `leading-none` 或 `leading-[0.85]`。正文用 `leading-snug` 或 `leading-relaxed`。

### 圆角与边框
*   **圆角**：**默认 `0px`（锐利、棱角分明的角）。**
    *   例外：`rounded-full` 仅用于胶囊徽章、圆形贴纸或装饰形状元素。
    *   绝不用 `rounded-md` 或 `rounded-lg`。要么锐利要么全圆。

*   **边框**：**每个视觉元素强制。**
    *   默认：`border-4`（4px solid black）。这是签名粗细。
    *   细：`border-2`（2px）仅含蓄分隔符或幽灵按钮。
    *   粗：`border-8`（8px）作主要区块分隔符或 Hero 元素。
    *   所有边框：`border-black`（实心黑，无透明）。

### 阴影与效果
*   **硬阴影（签名）**：偏移、实心黑阴影配**零模糊**与**零扩散**。始终右下方向。
    *   **小**：`shadow-[4px_4px_0px_0px_#000]` 或 `box-shadow: 4px 4px 0px 0px #000`
    *   **中**：`shadow-[8px_8px_0px_0px_#000]` 或 `box-shadow: 8px 8px 0px 0px #000`
    *   **大**：`shadow-[12px_12px_0px_0px_#000]` 或 `box-shadow: 12px 12px 0px 0px #000`
    *   **巨**：`shadow-[16px_16px_0px_0px_#000]` 或 `shadow-[20px_20px_0px_0px_#fff]`（用于黑背景上元素）

*   **文字阴影**：用于彩色背景上文字。
    *   `text-shadow: 4px 4px 0px #000` 或 `text-shadow: 6px 6px 0px #000`

*   **背景图案与纹理**（对深度至关重要）：
    *   **半调圆点**：
        ```css
        background-image: radial-gradient(#000 1.5px, transparent 1.5px);
        background-size: 20px 20px;
        ```
    *   **网格图案**（方格纸）：
        ```css
        background-size: 40px 40px;
        background-image: linear-gradient(to right, rgba(0, 0, 0, 0.1) 1px, transparent 1px),
                          linear-gradient(to bottom, rgba(0, 0, 0, 0.1) 1px, transparent 1px);
        ```
    *   **噪点纹理**（SVG 滤镜）：
        ```css
        background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'%2F%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
        ```
    *   **径向圆点**（用于背景）：
        ```css
        background-image: radial-gradient(circle, #000 2px, transparent 2.5px);
        background-size: 30px 30px;
        ```

## 组件样式原则

### 按钮
*   **形状**：锐角矩形。默认高度：`h-12` 至 `h-14`。无圆角。
*   **样式**：
    *   主：`bg-neo-accent`（红）配 `border-4 border-black`。
    *   次：`bg-neo-secondary`（黄）配 `border-4 border-black`。
    *   描边：`bg-white` 配 `border-4 border-black`。
    *   幽灵：`border-2 border-transparent` 悬停变 `border-black`。
*   **字体**：`font-bold text-sm uppercase tracking-wide`（全大写、粗、间距）。
*   **阴影**：硬阴影 `shadow-[4px_4px_0px_0px_#000]` 或 `shadow-[6px_6px_0px_0px_#000]`。
*   **交互（关键）**：**"推"效果。** `:active` 时，位移按钮覆盖其阴影：
    ```css
    active:translate-x-[2px] active:translate-y-[2px] active:shadow-none
    ```
    这创造机械"咔嗒下压"感，如物理按钮。
*   **悬停**：轻微背景加深或阴影强化。快速过渡（`duration-100`）。

### 卡片/容器
*   **结构**：`bg-white` 配 `border-4 border-black` 与锐角（`rounded-none`）。
*   **阴影**：深硬阴影（`shadow-[8px_8px_0px_0px_#000]` 至 `shadow-[12px_12px_0px_0px_#000]`）。
*   **悬停（抬起效果）**：卡片**上移**并**增大阴影**：
    ```css
    hover:-translate-y-1 hover:shadow-[10px_10px_0px_0px_#000]
    ```
    或
    ```css
    hover:-translate-y-2 hover:shadow-[16px_16px_0px_0px_#000]
    ```
    这使卡片感觉物理抬离页面。
*   **头部**：常有彩色背景（`bg-neo-muted/20` 或 `bg-neo-secondary`）配 `border-b-4 border-black` 分隔符。

### 输入框
*   **样式**：粗黑边框（`border-4 border-black`）。锐角。默认 `bg-white`。
*   **字体**：大、粗文字（`font-bold text-lg` 或 `text-xl`）。占位符 `placeholder:text-black/40`。
*   **聚焦**：**背景色变化**替代环：
    ```css
    focus-visible:bg-neo-secondary focus-visible:shadow-[4px_4px_0px_0px_#000] focus-visible:outline-none focus-visible:ring-0
    ```
    聚焦时输入框变黄并获阴影。无柔光。
*   **高度**：`h-14` 至 `h-20` 以增触控友好尺寸。

### 导航
*   **Logo**：带边框盒（`border-4 border-black`）配点缀背景。大写、黑字。
*   **链接**：粗、大写文字。悬停状态加边框与背景：
    ```css
    hover:border-black hover:bg-neo-accent hover:px-2 hover:shadow-[4px_4px_0px_0px_#000]
    ```
*   **移动菜单**：汉堡按钮为带边框方块配阴影。菜单滑入配堆叠带边框按钮。

### 徽章
*   **形状**：胶囊（`rounded-full`）或方块（`border-4`）。
*   **样式**：彩色背景（`bg-neo-accent` 或 `bg-neo-secondary`）配粗边框与阴影。
*   **字体**：`font-black text-sm uppercase tracking-widest`。
*   **用法**：绝对定位覆盖元素（`:absolute top-4 left-4`）、旋转（`rotate-3`）或行内。

## 布局原则

*   **容器宽度**：用 `container mx-auto` 配 `max-w-7xl` 或 `max-w-6xl` 以聚焦内容宽度。
*   **间距**：密集 8px 基础网格。区块有 `py-16` 至 `py-32` 垂直内边距。内容间距：`gap-8` 至 `gap-12`。
*   **旋转（贴纸效果）**：容器与文字块用轻微旋转打破网格单调：
    *   `rotate-1`（1 度）、`-rotate-2`（-2 度）、`rotate-3`（3 度）。
    *   应用于标题 span、卡片、徽章与 CTA。
*   **跑马灯**：用横向滚动跑马灯（如 `react-fast-marquee`）作：
    *   页面顶部信任指标。
    *   证言轮播。
    *   重复文字区块分隔符。
*   **重叠**：用绝对定位允许元素重叠：
    *   浮动装饰形状（`absolute top-20 left-0`）。
    *   徽章定位于卡片角（`-top-6 -right-6`）。
    *   背景文字作纹理（`absolute opacity-10 text-9xl`）。
*   **视觉混乱区**：刻意创造"繁忙"区域（如 Hero 右侧）配：
    *   堆叠几何形状。
    *   多个旋转徽章。
    *   大型背景数字或文字。
*   **非对称**：避免完美对称。用 60/40 分割、偏移列与错落网格。

## "大胆要素"（非通用性）

这些技巧确保设计无可错认地 neo-brutalist 且绝不通用：

1.  **展示字体的文字描边**：用 `-webkit-text-stroke: 2px black` 配 `color: transparent` 作巨型空心轮廓标题。叠实心版本以增深度效果。

2.  **贴纸层叠**：元素感觉如物理贴纸：
    *   旋转文字块配边框与阴影。
    *   绝对定位徽章重叠内容。
    *   用阴影创造多"层"。

3.  **交互物理**：元素必须物理移动：
    *   按钮：点击时**下压**（`active:translate-x-[2px] active:translate-y-[2px]`）。
    *   卡片：悬停时**抬起**（`hover:-translate-y-2`）。
    *   徽章：悬停时**旋转更多**（`hover:rotate-12`）。

4.  **原始形状母题**：大量使用：
    *   **星形**（5 角，`<Star />` from lucide-react）。作装饰元素、评分与分隔符。
    *   **箭头**（`<ArrowRight />`）作方向暗示。
    *   **基本形状**：方、圆、矩形作浮动装饰。

5.  **处处粗边框**：若元素无可见边框，感觉不对。甚至留白也有边框。

6.  **色块**：大区块配纯色背景（红、黄、紫、黑）以创高对比节奏。

7.  **纹理叠加**：绝不留扁平背景。始终添加半调、网格或噪点。

## 反模式（应避免之事）

这些技巧会破坏 neo-brutalist 美学：

*   **模糊效果**：无 `blur()`、无 `backdrop-blur`、无带模糊半径的柔和 `box-shadow`。所有阴影必须硬。
*   **不透明/透明**：避免背景 alpha 透明（低不透明纹理叠加除外）。
*   **平滑渐变**：无 `bg-gradient-to-r` 渐变。改用硬色停或图案。
*   **圆角（中档）**：避免 `rounded-md`、`rounded-lg`、`rounded-xl`。要么 `rounded-none`（锐）要么 `rounded-full`（胶囊/圆）。
*   **含蓄灰**：无 `#333`、`#666`、`#999`。用纯黑或色。
*   **柔和动画**：无 `ease-in-out` 或慢时长。用 `ease-linear` 或 `ease-out` 配快时长。
*   **极简留白**：勿留大空区。以纹理、图案或装饰元素填充。

## 动画与运动

*   **质感**：弹跳、俏皮、机械、街机感。
*   **过渡速度**：快且利落。
    *   按钮：`duration-100`（100ms）。
    *   卡片/悬停：`duration-200` 或 `duration-300`（200-300ms）。
*   **缓动**：`ease-linear` 作机械感，`ease-out` 作自然减速。避免 `ease-in-out`。
*   **悬停交互**：
    *   按钮：背景加深，点击下压。
    *   卡片：上移（`-translate-y-2`）并阴影加深。
    *   链接：加边框与背景，snap 就位。
*   **循环动画**：
    *   装饰星形慢转（`animate-spin-slow`，自定义时长 10s）。
    *   CTA 元素脉动（`animate-pulse`）。
    *   吸睛徽章弹跳（`animate-bounce`）。
*   **自定义动画**（通过 CSS）：
    ```css
    @keyframes spin-slow {
      from { transform: rotate(0deg); }
      to { transform: rotate(360deg); }
    }
    .animate-spin-slow {
      animation: spin-slow 10s linear infinite;
    }
    ```

## 间距、布局与图标

*   **最大宽度**：主要内容 `max-w-7xl` 或 `max-w-6xl`。区块可全宽配包含内部内容。
*   **网格系统**：用 Tailwind 网格（`grid-cols-1 md:grid-cols-2 lg:grid-cols-3`）配响应式断点。
*   **间距阶梯**：密集。元素间 `gap-6` 至 `gap-12`。区块内边距 `py-16` 至 `py-32`。
*   **图标**：自 `lucide-react` 导入。
    *   样式：`stroke-[3px]` 或 `stroke-[4px]` 作粗描边。
    *   尺寸：`h-8 w-8` 或更大（`h-12 w-12`）以强调。
    *   放置：带边框盒内（`border-4 border-black bg-neo-accent p-4`）。
    *   填充：用 `fill-black` 或 `fill-white` 作实心图标。

## 响应式策略

*   **移动优先**：设计自移动（`base`）开始向上缩放。
*   **断点**：
    *   `sm:`（640px）- 小平板
    *   `md:`（768px）- 平板
    *   `lg:`（1024px）- 桌面
    *   `xl:`（1280px）- 大桌面
*   **移动适配**：
    *   **字体**：缩小（如 `text-4xl sm:text-6xl md:text-8xl`）。
    *   **间距**：减内边距（如 `p-8 sm:p-12 md:p-16`）。
    *   **网格**：堆叠为单列（`grid-cols-1 md:grid-cols-2 lg:grid-cols-3`）。
    *   **阴影**：移动端减尺寸（如 `shadow-[6px_6px_0px_0px_#000] sm:shadow-[8px_8px_0px_0px_#000]`）。
    *   **导航**：带边框按钮汉堡菜单。全屏或滑入抽屉。
    *   **按钮**：移动端全宽（`w-full sm:w-auto`）。
    *   **触控目标**：可点击元素最小 `h-14`。
*   **保持核心美学**：即使移动端也保持粗边框、硬阴影与粗字体。勿默认"通用移动"设计。

## 可访问性与最佳实践

*   **对比**：高对比内置（黑于奶油、白于黑、黑于黄）。确保所有色彩组合达 WCAG AA（正常文字 4.5:1，大文字 3:1）。
*   **聚焦状态**：用粗聚焦环：
    ```css
    focus-visible:ring-2 focus-visible:ring-black focus-visible:ring-offset-2
    ```
    或输入框用背景色变化（黄）。
*   **运动**：尊重 `prefers-reduced-motion`：
    ```css
    @media (prefers-reduced-motion: reduce) {
      .animate-spin-slow, .animate-bounce, .animate-pulse {
        animation: none;
      }
    }
    ```
*   **键盘导航**：确保所有交互元素键盘可访问。Tab 顺序应合逻辑。
*   **屏幕阅读器**：用语义 HTML（`<button>`、`<nav>`、`<header>`、`<main>`）。纯图标按钮加 `aria-label`。
*   **触控目标**：移动端所有可点击元素最小 44x44px（Tailwind 中约 `h-12` 或 `h-14`）。

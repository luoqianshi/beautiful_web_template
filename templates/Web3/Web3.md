# Crypto

> 来源：[Design Prompts](https://www.designprompts.dev/web3)

## 基本信息

| 属性 | 值 |
|------|-----|
| 风格ID | `web3` |
| 显示名称 | Crypto |
| 模式 | 🌙 深色模式 (Dark) |
| 字体类型 | sans-serif |
| 描述 | 受比特币与去中心化金融启发的大胆未来主义美学。深邃虚空背景配比特币橙点缀、金色高光、发光元素与精准数据可视化。 |

## 布局创意 (Layout Ideas)

### Hero

60/40 比例分割布局。左：巨型标题配比特币橙渐变文字与信任徽章。右：浮动动画 3D 球体配旋转轨道环与浮动数据卡片。背景含含蓄网格图案配径向渐变模糊效果。

### Stats

四个关键指标横向网格配等宽数字、大写标签与含蓄趋势指示器。深色表面背景配上下来边框以增滚动条感。

### Product Detail

双栏布局，左侧模型，右侧内容。抽象 UI 模型配玻璃拟态、网格背景与全息渐变。

### Features

三列抬升卡片网格配背景图标水印、悬停发光点缀边框与渐变背景图标容器。

### Blog

三列图片主导卡片网格。全幅图片配渐变叠加、日期徽章与悬停缩放效果增强对比。

### How It Works

垂直时间线配居中连接线。交替左右内容卡片配中线编号节点。卡片有角部点缀边框。

### Benefits

三列卡片网格配发光圆圈中勾选图标。悬停时渐变边框出现。

### Testimonials

三列玻璃拟态卡片网格配大号引号、橙色辉光头像环与点缀色角色徽章。

### Pricing

三列网格，中间卡片抬升并缩放。Popular 徽章悬浮于上方。高亮档位用渐变按钮。

### Faq

手风琴配 chevron 指示器。玻璃拟态背景配平滑高度过渡与内边距显现。

### Footer

多列网格，品牌左侧跨两列。等宽区块标题，含蓄链接悬停状态配橙色点缀。

---

## 完整提示词 (Full Prompt)

# 设计哲学："Bitcoin DeFi"美学

此风格体现比特币与去中心化金融的视觉 DNA——精密工程、密码学信任与数字黄金的精致融合。它**不是通用深色模式**；它是深邃宇宙虚空，数据结构以比特币橙的温暖与数字黄金的辉煌发光。

## 核心设计原则

1.  **发光能量**：光自交互元素本身发出。比特币橙发光、金色高光闪烁、数据点在真实虚空背景上脉动生命。阴影是彩色的（橙/金色调），非仅黑。

2.  **数学精准**：一切遵循严格几何规则。超细 1px 边框定义边界，等宽字体以技术准确显示数据，网格提供区块链美学的底层结构。

3.  **分层深度**：通过透明堆叠（玻璃拟态）、彩色辉光阴影与 backdrop blur 效果创造三维空间。元素在 Z 空间漂浮而无重拟物——这是数字深度，非物理。

4.  **纹理虚空**：背景绝不扁平。含蓄网格图案（代表区块链网络）、径向渐变模糊（代表能量场）与噪点纹理使虚空鲜活。黑暗呼吸。

5.  **通过设计建立信任**：高对比、清晰层级与技术精准传达安全与可靠。美学说"你的资产在此安全"。

气质是**安全、技术、有价值**。这是数字黄金——应感觉高端、前沿、工程完美。想象比特币矿机在黑暗中嗡鸣，以橙色热量发光。

# 设计 Token 系统

## 色彩（仅深色模式）
此调色板用"真虚空"基础配"Bitcoin Fire"能量——比特币橙的温暖与数字黄金的辉煌。

*   **Background**：`#030304`（真虚空）— 一切开始的深邃空间
*   **Surface**：`#0F1115`（暗物质）— 抬升表面、卡片与面板
*   **Foreground**：`#FFFFFF`（纯光）— 主要文字，最大对比
*   **Muted**：`#94A3B8`（星尘）— 次要文字、描述、元信息
*   **Border**：`#1E293B`（暗边界）— 静止含蓄边框（用白时常 10-20% 不透明度）
*   **Primary Accent**：`#F7931A`（比特币橙）— 去中心化的标志性色彩。主 CTA、链接、激活状态与信任指示器
*   **Secondary Accent**：`#EA580C`（焦橙）— 更深、更暖的橙作渐变、次级元素与视觉深度
*   **Tertiary Accent**：`#FFD600`（数字金）— 价值的色彩。用于与比特币橙的渐变、高亮与成功状态

**渐变公式**：签名外观是 `linear-gradient(to right, #EA580C, #F7931A)` 或 `linear-gradient(to right, #F7931A, #FFD600)` 用于文字与按钮。

## 字体
字体系统平衡技术精准与现代几何形态。

*   **标题**：`Space Grotesk`（Google Font）— 带古怪技术特色的几何 grotesque
    *   字重：400（Regular）、500（Medium）、600（Semibold）、700（Bold）
    *   用法：所有标题（h1-h6）、区块标题、卡片标题
    *   应用 `font-heading` 类

*   **正文**：`Inter`（Google Font）— 为屏幕优化的高可读无衬线
    *   字重：400（Regular）、500（Medium）、600（Semibold）
    *   用法：正文、描述、按钮
    *   应用 `font-body` 类

*   **等宽/数据**：`JetBrains Mono`（Google Font）— 精准技术等宽
    *   字重：400（Regular）、500（Medium）
    *   用法：数据、价格、徽章、技术标签、导航链接
    *   应用 `font-mono` 类

*   **尺度哲学**：展示与正文间戏剧性对比。Hero 巨大（`text-4xl` → `md:text-7xl`），正文舒适（`text-base` 或 `text-lg`）。移动优先缩放防止小屏过载。

*   **行高与字距**：标题紧凑行高（`leading-tight`），正文宽松（`leading-relaxed`）。大写等宽文字获慷慨字距（`tracking-wider`、`tracking-widest`）。

## 圆角与边框
几何精准配柔和曲线以增亲和。

*   **圆角 Token**：
    *   卡片/容器：`rounded-2xl`（16px）或 `rounded-xl`（12px）
    *   按钮：`rounded-full`（胶囊形）
    *   输入框：`rounded-lg`（8px）或仅底边框以增极简
    *   小元素（徽章、图标）：`rounded-lg` 或 `rounded-full`

*   **边框哲学**：超细 `1px` 边框创造精致边界而无视觉重量
    *   默认状态：`border border-white/10`（几乎不可见结构）
    *   悬停状态：`border-[#F7931A]/50`（橙色点缀，50% 不透明度）
    *   激活/聚焦：`border-[#F7931A]`（全强度）

*   **特殊边框技巧**：
    *   角部点缀：角落小型装饰边框段（见 How It Works 卡片）
    *   渐变边框：用内伪元素或含蓄 box-shadow 渐变模拟

## 阴影与效果（辉光）
此风格签名是**彩色发光**——比特币橙与金色调的阴影与辉光。

*   **橙色辉光**（主）：`shadow-[0_0_20px_-5px_rgba(234,88,12,0.5)]` 或 `shadow-[0_0_30px_-5px_rgba(247,147,26,0.6)]`
    *   用于按钮、悬停卡片、主 CTA 与交互元素

*   **金色辉光**（点缀）：`shadow-[0_0_20px_rgba(255,214,0,0.3)]`
    *   用于特殊高亮、成功状态、价值指示器

*   **含蓄卡片抬升**：`shadow-[0_0_50px_-10px_rgba(247,147,26,0.1)]`
    *   用于产品模型、主要区块

*   **玻璃拟态**：
    *   公式：`backdrop-blur-lg` + `bg-white/5` 或 `bg-black/40`
    *   创造漂浮、半透明面板以透出背景模糊
    *   用于浮动卡片（Hero）、证言、"How It Works" 卡片

*   **径向模糊背景**：大型柔和径向渐变配重度模糊作环境背景辉光
    *   示例：`bg-[#F7931A] opacity-10 blur-[120px]` 绝对定位

## 纹理与图案
背景以含蓄、不分散的图案呼吸，强化区块链/网络主题。

*   **网格图案**（签名）：
    ```css
    background-size: 50px 50px;
    background-image:
      linear-gradient(to right, rgba(30, 41, 59, 0.5) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(30, 41, 59, 0.5) 1px, transparent 1px);
    mask-image: radial-gradient(circle at center, black 40%, transparent 100%);
    ```
    *   创造向边缘消失的渐隐网格（暗角效果）
    *   用于 Hero 区块

*   **外部纹理叠加**：
    *   示例：`bg-[url('https://www.transparenttextures.com/patterns/cubes.png')] opacity-5`
    *   极含蓄、几乎不可见图案以增视觉趣味

*   **径向渐变模糊**：大型柔和色块作环境光
    *   绝对定位，用低不透明度（5-10%），应用 blur-[120px] 或 blur-[150px]
    *   创造深度并引导目光至焦点

# 组件样式

## 按钮
按钮大胆、胶囊形、发出彩色光。全部用 `rounded-full` 作签名加密胶囊形。

*   **主（默认）**：
    *   背景：`bg-gradient-to-r from-[#EA580C] to-[#F7931A]`
    *   文字：白、粗、大写配 `tracking-wider`
    *   阴影：`shadow-[0_0_20px_-5px_rgba(234,88,12,0.5)]`
    *   悬停：`scale-105` + 增强阴影 `shadow-[0_0_30px_-5px_rgba(247,147,26,0.6)]`
    *   最小高度：44px（触控友好）

*   **描边**：
    *   背景：透明
    *   边框：`border-2 border-white/20`
    *   文字：白
    *   悬停：`border-white` + `bg-white/10`

*   **幽灵**：
    *   背景：透明，无边框
    *   文字：白
    *   悬停：`bg-white/10` + `text-[#F7931A]`

*   **链接**：
    *   文字：`text-[#F7931A]`
    *   悬停：下划线

所有按钮含平滑 `transition-all` 以增响应微交互。

## 卡片（"区块"概念）
卡片是漂浮于虚空之上的抬升表面，代表链中区块。

*   **标准卡片**：
    *   背景：`bg-[#0F1115]`（暗物质表面）
    *   边框：`border border-white/10`（含蓄边界）
    *   圆角：`rounded-2xl`（16px）
    *   内边距：`p-8`（慷慨间距）
    *   悬停：`hover:-translate-y-1`（抬起）+ `hover:border-[#F7931A]/50` + `hover:shadow-[0_0_30px_-10px_rgba(247,147,26,0.2)]`
    *   过渡：`transition-all duration-300`

*   **玻璃卡片**（浮动/特殊）：
    *   背景：`bg-black/40` 或 `bg-white/5`
    *   Backdrop：`backdrop-blur-sm` 或 `backdrop-blur-lg`
    *   边框：`border border-white/10`
    *   创造半透明、浮动效果

*   **定价卡片**：
    *   高亮档位：`scale-105`、`border-[#F7931A]`、抬升 z-index、`shadow-[0_0_40px_-10px_rgba(247,147,26,0.15)]`
    *   其他：降低不透明度（`opacity-80`），悬停放大

*   **卡片层级**：
    *   头部：`p-8 pb-4`
    *   标题：`font-heading font-semibold text-2xl`
    *   描述：`text-[#94A3B8] text-sm`
    *   内容：`p-8 pt-0`
    *   页脚：`p-8 pt-0`

## 输入框
极简、精准输入字段配底边框样式以增技术美学。

*   **背景**：`bg-black/50`（半透明深）
*   **边框**：仅底边框 — `border-b-2 border-white/20`
*   **高度**：`h-12`（48px 以增触控目标）
*   **内边距**：`px-4 py-2`
*   **文字**：`text-white text-sm`
*   **占位符**：`placeholder:text-white/30`
*   **聚焦状态**：
    *   边框：`focus-visible:border-[#F7931A]`
    *   辉光：`focus-visible:shadow-[0_10px_20px_-10px_rgba(247,147,26,0.3)]`
    *   无 outline：`focus-visible:outline-none`
*   **禁用**：`disabled:opacity-50 disabled:cursor-not-allowed`

输入框感觉如数据录入终端——干净、精准、有目的。

## 图标
来自 `lucide-react` 的图标强化技术、精准美学。

*   **描边宽度**：默认（1.5-2px 以增干净技术线）
*   **颜色**：用点缀色创造层级
    *   橙：`text-[#F7931A]` 或 `text-[#EA580C]`
    *   金：`text-[#FFD600]`
    *   柔和：`text-[#94A3B8]`
    *   白：`text-white`

*   **图标容器**：包裹于彩色、发光容器中
    *   示例：`bg-[#EA580C]/20 border border-[#EA580C]/50 rounded-lg p-3`
    *   创造"全息节点"效果
    *   悬停：加辉光阴影 `hover:shadow-[0_0_20px_rgba(234,88,12,0.4)]`

*   **装饰图标**：卡片背景中大、水印风格图标
    *   悬停时高不透明度以增含蓄显现效果
    *   示例：`opacity-20 group-hover:opacity-100`

# 非通用"大胆"选择

此设计绝不可看起来像默认 Tailwind。这些大胆选择创造不可否认的个性：

1.  **标题渐变文字**：对 Hero 标题末 1-2 词应用 `bg-gradient-to-r from-[#F7931A] to-[#FFD600] bg-clip-text text-transparent`。创造即时视觉层级与比特币品牌关联。

2.  **旋转轨道环**：Hero 区块含动画 3D 风格球体配 CSS 旋转环（`animate-[spin_10s_linear_infinite]` 与反向）。浮动数据卡片以错峰延迟围绕弹跳。

3.  **角部边框点缀**："How It Works" 卡片用比特币橙装饰角边框（左上 `border-t border-l`，右下 `border-r border-b`），创造"选中节点"效果。

4.  **发光动画徽章**：信任指示器与状态标记上脉动圆点徽章（`animate-ping`）。暗示实时网络活动。

5.  **背景图标水印**：特性卡片背景中大、旋转、低不透明度图标，悬停显现（`opacity-20 group-hover:opacity-100`）。

6.  **时间线即区块链**："How It Works" 用垂直渐变线（橙至透明）配编号圆形节点，模仿区块链账本。

7.  **非对称定价缩放**：热门定价档位 `scale-105` 并抬升，其他 `opacity-80`，通过缩放操纵创造有意层级。

8.  **玻璃拟态配网格图案**：结合 `backdrop-blur` 与通过透明可见的背景网格图案，创造分层深度。

9.  **彩色阴影替代黑**：所有阴影用橙/金色调。此设计系统中无纯黑阴影。

# 布局与间距

*   **容器宽度**：`max-w-7xl`（1280px）— 宽阔宽广以展示数据与内容而不拥挤
*   **区块内边距**：慷慨垂直 `py-24`（96px）在主要区块间创造呼吸空间
*   **密度**：宽敞方法配网格项间 `gap-8`（32px）或 `gap-12`（48px）
*   **区块分隔符**：无硬线或 `<hr>` 元素。区块通过以下分隔：
    *   垂直间距（`py-24`）
    *   交替背景（`bg-[#030304]` → `bg-[#0F1115]` → `bg-[#030304]`）
    *   特定区块含蓄上/下边框（如数据滚动条有 `border-y`）

*   **响应式网格**：
    *   移动优先：默认单列
    *   平板：`md:grid-cols-2` 或 `md:grid-cols-3`
    *   桌面：保持 `md:grid-cols-3` 或特性 `lg:grid-cols-4`
    *   定价：始终 `md:grid-cols-3` 以作档位比较

# 动画与运动

运动应感觉**精准、利落、有目的**——如高性能交易终端。

*   **自定义浮动动画**：
    ```css
    @keyframes float {
      0%, 100% { transform: translateY(0px); }
      50% { transform: translateY(-20px); }
    }
    .animate-float {
      animation: float 8s ease-in-out infinite;
    }
    ```
    *   应用于 Hero 3D 球体图形
    *   缓慢、平滑、无尽浮动创造空灵品质

*   **旋转轨道**：
    *   外环 `animate-[spin_10s_linear_infinite]`
    *   内环 `animate-[spin_15s_linear_infinite_reverse]`（反向）
    *   创造迷人 3D 深度错觉

*   **弹跳卡片**：浮动数据卡片用 `animate-bounce` 配自定义时长（`3s`、`4s`）与延迟（`delay-1s`）以增错峰运动

*   **脉动指示器**：状态徽章用 `animate-ping` 作"实时"感

*   **交互速度**：快且响应（`duration-200` 或 `duration-300`）
    *   按钮悬停：`transition-all duration-300`
    *   卡片抬起：`transition-all duration-300`
    *   输入聚焦：即时（`duration-200`）

*   **悬停效果**：
    *   卡片：抬起（`-translate-y-1`）、边框色偏、辉光增强
    *   按钮：缩放（`scale-105`）、辉光扩散
    *   图片：缩放（`scale-110`）、对比增强（`contrast-125`）

运动设计传达**速度、精准与响应**——加密/金融中的关键价值。

# 响应式策略

设计必须在所有屏幕尺寸保持其大胆个性同时优雅适配。

*   **移动优先哲学**：从单列布局开始，更大屏幕放大
*   **断点**：
    *   `sm`：640px - 次要调整
    *   `md`：768px - 主要布局转变（2-3 列激活）
    *   `lg`：1024px - 完整桌面体验
    *   `xl`：1280px - 最大宽度容器（`max-w-7xl`）

*   **字体缩放**：所有标题用响应式类
    *   Hero：`text-4xl sm:text-5xl md:text-7xl`
    *   区块标题：`text-2xl md:text-4xl` 或 `md:text-5xl`
    *   正文：`text-base md:text-lg`
    *   保持移动可读，勿压倒小屏

*   **触控目标**：所有交互元素最小 44px（`min-w-[44px]`、`h-10+`）

*   **移动适配**：
    *   导航：移动端仅显示必要 CTA，隐藏次级导航
    *   Hero 3D 图形：移动端更小尺寸（`h-[300px] md:h-[450px]`）
    *   网格：单列 → `md` 处 2-3 列
    *   定价卡片：垂直堆叠，移动端移除缩放效果
    *   How It Works 时间线：移动端左对齐配更简布局

*   **保持核心美学**：网格图案、辉光与渐变在移动端持续——勿为小屏剥离个性

# 可访问性与最佳实践

*   **色彩对比**：白字于 `#030304` 超过 WCAG AAA（21:1 比例）。橙 `#F7931A` 于深背景对大文字达 AA。
*   **聚焦状态**：所有交互元素有可见聚焦环用 `focus-visible:ring-2 focus-visible:ring-[#F7931A]`
*   **语义化 HTML**：正确标题层级（h1 → h2 → h3）、`<nav>`、`<section>`、`<button>` 元素
*   **Alt 文本**：所有图片需描述性 alt 属性
*   **键盘导航**：所有交互元素可通过 Tab 访问，按钮以 Enter/Space 激活
*   **运动偏好**：考虑 `prefers-reduced-motion` 服务动画敏感用户（禁用浮动/旋转动画）

# 实现说明

*   **字体加载**：用 `fontImport()` 助手加载 Google Fonts
*   **自定义类**：在 style 块定义 `.font-heading`、`.font-body`、`.font-mono`
*   **网格图案**：在 style 块用 CSS-in-JS 定义 `.bg-grid-pattern`
*   **玻璃拟态**：定义 `.holographic-gradient` 助手类
*   **组件**：用 `cva`（class-variance-authority）构建 Button、Card 与 Input 组件，遵循 Shadcn 模式但配 Crypto 特定样式
*   **图标**：按需自 `lucide-react` 导入特定图标（Zap、Lock、Layers、Globe、Check 等）

这不是通用深色主题。这是 **Bitcoin DeFi 美学**——为精准、安全与数字价值而工程。

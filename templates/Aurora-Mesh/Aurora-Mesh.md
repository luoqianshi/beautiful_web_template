# Aurora Mesh

> 来源：[Design Prompts](https://www.designprompts.dev/aurora-mesh)

## 基本信息

| 属性 | 值 |
|------|-----|
| 风格ID | `aurora-mesh` |
| 显示名称 | Aurora Mesh |
| 模式 | 🌙 深色模式 (Dark) |
| 字体类型 | sans-serif |
| 描述 | 流动的网格渐变，极光效果，鲜明色彩过渡，受 Stripe 与 Vercel 启发的现代初创美学。 |

## 布局创意 (Layout Ideas)

### Hero

全高 Hero，配动画网格渐变背景。分割布局：左侧标题（巨型字体配渐变文字填充），右侧浮动 3D 感卡片模型，下方极光辉光。CTA 为渐变边框胶囊形。

### Stats

横向条带，玻璃拟态数据卡片浮于含蓄极光波之上。每个数据顶部有发光的点缀色条，标示其类别色。

### Features

非对称 bento 网格，卡片尺寸不一。卡片为深色玻璃背景，带彩色渐变边框，轻微脉动。图标置于渐变光球中。

### How It Works

垂直时间线，发光渐变线连接各步。每步卡片含网格渐变角部点缀。数字超大，配渐变填充。

### Benefits

双栏布局，收益卡片堆叠。每张卡片顶边有极光条纹。勾选图标配渐变填充。

### Pricing

三张卡片，精选卡片上浮并以动画渐变边框包裹。背景为缓慢移动的网格渐变。价格使用渐变文字。

### Testimonials

证言卡片轮播或瀑布流，头像图片带渐变环边框。引号超大，配极光渐变填充。

### Faq

手风琴样式，左侧渐变点缀线。展开项以柔和辉光效果显现回答。加减图标采用渐变处理。

### Blog

横向滚动卡片，图片叠加配渐变网格滤镜。日期徽章为渐变背景胶囊形。

### Footer

深色基底，顶边含蓄极光波。链接分列组织，悬停时渐变下划线。社交图标置于渐变光球中。

---

## 完整提示词 (Full Prompt)

# Aurora Mesh 设计系统

## 设计哲学

Aurora Mesh 捕捉了北极光空灵流动之美，与现代网格渐变技术相融。这是**高端 SaaS 产品**的美学——想象 Stripe 的宇宙深度、Vercel 的深色优雅与 Linear 的精致极简，但进一步推向**活的、呼吸的色彩**之境。

**核心原则**：
- **流动的色彩**：渐变永不静止。它们流动、变形、以有机运动呼吸
- **深色画布，明亮点缀**：深邃近黑的背景让鲜艳的极光色彩歌唱
- **维度深度**：模糊、辉光与透明的层次营造漂浮 UI 之感
- **高端打磨**：每个细节都经精炼——流畅曲线、完美间距、考究的微交互

**气质**：精致、未来感、高端、超凡脱俗。如同在穿越极光时操作宇宙飞船的界面。用户应感到自己在触摸未来。

**视觉签名**：
- 似在移动与变换的网格渐变
- 自元素溢出的彩色辉光效果
- 捕捉光线的玻璃般表面
- 标题上的渐变文字
- 带彩色阴影的浮动卡片
- 背景中的极光波纹图案

---

## 设计 Token 系统

### 色彩（深色模式 — 定义版）

```
Background:
  base: #09090b (近黑，略带暖意)
  elevated: #18181b (卡片背景)
  surface: #27272a (输入框背景、边框)

Foreground:
  primary: #fafafa (标题、重要文字)
  secondary: #a1a1aa (正文、描述)
  muted: #71717a (占位符、禁用)

Aurora Palette (主角):
  violet: #8b5cf6
  purple: #a855f7
  fuchsia: #d946ef
  pink: #ec4899
  cyan: #22d3ee
  teal: #2dd4bf

Gradient Stops (用于网格):
  aurora-1: #8b5cf6 (violet)
  aurora-2: #d946ef (fuchsia)
  aurora-3: #22d3ee (cyan)
  aurora-4: #2dd4bf (teal)

Accent (主要操作):
  DEFAULT: #a855f7
  hover: #c084fc

Border:
  subtle: #27272a
  DEFAULT: #3f3f46
  glow: rgba(168, 85, 247, 0.5)

Success: #34d399
Warning: #fbbf24
Error: #f87171
```

### 字体

**字体栈**：
- **标题**："Instrument Sans"（Google Fonts）— 干净、几何、现代。备选：Inter
- **正文**："Inter"（Google Fonts）— 高可读性、中性、专业
- **等宽/代码**："JetBrains Mono" 用于任何代码片段

**字号阶梯**：
- Hero 标题：`text-6xl md:text-7xl lg:text-8xl` 配 `font-bold tracking-tight`
- 区块标题：`text-4xl md:text-5xl` 配 `font-semibold`
- 卡片标题：`text-xl md:text-2xl` 配 `font-semibold`
- 大号正文：`text-lg` 配 `text-secondary`
- 正文：`text-base` 配 `leading-relaxed`
- 小号/说明：`text-sm` 配 `text-muted`

**渐变文字处理**：
```css
.gradient-text {
  background: linear-gradient(135deg, #a855f7 0%, #ec4899 50%, #22d3ee 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
```

### 圆角与边框

- **默认圆角**：`rounded-2xl`（16px）— 柔和、现代、亲和
- **按钮**：`rounded-full`（主要操作的胶囊形）
- **小元素**：`rounded-xl`（12px）
- **输入框**：`rounded-xl`
- **边框宽度**：`border`（1px）配半透明色

### 阴影与效果

**辉光阴影（签名元素）**：
```
glow-sm: 0 0 20px rgba(168, 85, 247, 0.15)
glow-md: 0 0 40px rgba(168, 85, 247, 0.2)
glow-lg: 0 0 60px rgba(168, 85, 247, 0.25), 0 0 120px rgba(34, 211, 238, 0.1)
glow-colored: 0 0 40px var(--glow-color, rgba(168, 85, 247, 0.3))
```

**抬升（分层）**：
```
elevation-1: 0 1px 2px rgba(0, 0, 0, 0.5)
elevation-2: 0 4px 12px rgba(0, 0, 0, 0.4)
elevation-3: 0 8px 30px rgba(0, 0, 0, 0.5), 0 0 40px rgba(168, 85, 247, 0.1)
```

### 纹理与图案（关键）

**网格渐变背景**：
使用多层径向渐变的 CSS 网格渐变：
```css
.aurora-mesh {
  background-color: #09090b;
  background-image:
    radial-gradient(at 40% 20%, rgba(139, 92, 246, 0.3) 0px, transparent 50%),
    radial-gradient(at 80% 0%, rgba(34, 211, 238, 0.2) 0px, transparent 50%),
    radial-gradient(at 0% 50%, rgba(217, 70, 239, 0.2) 0px, transparent 50%),
    radial-gradient(at 80% 50%, rgba(45, 212, 191, 0.15) 0px, transparent 50%),
    radial-gradient(at 0% 100%, rgba(236, 72, 153, 0.2) 0px, transparent 50%),
    radial-gradient(at 80% 100%, rgba(139, 92, 246, 0.15) 0px, transparent 50%);
}
```

**噪点叠加**：
2-5% 不透明度的含蓄颗粒纹理，增添深度并减少渐变中的条带。

**极光波（用于章节分隔符）**：
带渐变填充的 SVG 波纹图案，置于章节顶部/底部。

---

## 组件样式

### 按钮

**主按钮**：
- 背景：渐变 `from-violet-500 via-fuchsia-500 to-pink-500`
- 形状：`rounded-full` 胶囊
- 内边距：`px-8 py-3`
- 文字：`text-white font-semibold`
- 阴影：`shadow-lg shadow-violet-500/25`
- 悬停：轻微放大 `hover:scale-105`，增强辉光
- 按下：缩小 `active:scale-95`
- 过渡：`transition-all duration-200`

**次按钮**：
- 背景：`bg-white/5`（玻璃效果）
- 边框：`border border-white/10`
- 文字：`text-white`
- 悬停：`bg-white/10`，边框发光
- 背景：`backdrop-blur-sm`

**幽灵按钮**：
- 背景：透明
- 文字：`text-secondary`
- 悬停：`text-primary`，含蓄辉光下划线

### 卡片/容器

**标准卡片**：
- 背景：`bg-zinc-900/50` 配 `backdrop-blur-xl`
- 边框：`border border-zinc-800/50`
- 圆角：`rounded-2xl`
- 阴影：`shadow-2xl shadow-black/50`
- 悬停：边框提亮，出现含蓄辉光

**精选卡片**：
- 以渐变边框容器包裹
- 外层：用 `background: conic-gradient` 技巧的动画渐变边框
- 内层：深色实心背景
- 辉光：与主渐变色匹配的彩色阴影

**玻璃卡片**：
- 背景：`bg-white/5`
- 背景：`backdrop-blur-2xl backdrop-saturate-150`
- 边框：`border border-white/10`

### 输入框

- 背景：`bg-zinc-900`
- 边框：`border border-zinc-700`
- 圆角：`rounded-xl`
- 文字：`text-white`
- 占位符：`placeholder:text-zinc-500`
- 聚焦：`focus:border-violet-500 focus:ring-2 focus:ring-violet-500/20`
- 过渡：平滑边框色变化

### 图标

- 默认：`text-zinc-400` 配 `w-5 h-5`
- 渐变光球中：图标置于带渐变背景的 `rounded-xl` 容器内
- 交互：悬停时色彩转至点缀色
- 特性图标：更大 `w-8 h-8`，常配渐变背景或彩色辉光

---

## 布局策略

**容器**：`max-w-7xl mx-auto px-6 lg:px-8`

**区块间距**：主要区块间 `py-24 md:py-32`

**网格系统**：
- 特性：`grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8`
- Bento：变化的 `col-span` 与 `row-span` 以增视觉趣味
- 数据：`grid grid-cols-2 md:grid-cols-4 gap-6`

---

## 效果与动画

**运动质感**：流畅、优雅、略缓——如漂浮于水或太空。绝不突兀。

**过渡**：
- 默认：`transition-all duration-300 ease-out`
- 悬停效果：`duration-200`
- 页面元素：`duration-500` 用于淡入

**关键帧动画**：

```css
@keyframes aurora-shift {
  0%, 100% { opacity: 0.5; transform: translateY(0) scale(1); }
  50% { opacity: 0.8; transform: translateY(-20px) scale(1.1); }
}

@keyframes glow-pulse {
  0%, 100% { box-shadow: 0 0 20px rgba(168, 85, 247, 0.2); }
  50% { box-shadow: 0 0 40px rgba(168, 85, 247, 0.4); }
}

@keyframes gradient-rotate {
  0% { --gradient-angle: 0deg; }
  100% { --gradient-angle: 360deg; }
}
```

**滚动动画**：元素在滚动时淡入上滑（用 intersection observer 或 CSS scroll-driven 动画）。

---

## 图标

- 库：`lucide-react`
- 描边：默认描边宽度（2px）
- 尺寸：行内 `w-5 h-5`，独立 `w-6 h-6`，特性卡片 `w-8 h-8`
- 处理：常置于渐变光球内或赋予彩色背景
- 颜色：默认 `text-zinc-400`，点缀 `text-violet-400`

---

## 响应式策略

**移动端**：
- 所有网格堆叠为单列
- 标题尺寸缩减 1-2 级
- 网格渐变简化（更少层级以保性能）
- 卡片全宽，减少内边距
- 导航折叠为汉堡菜单
- 极光效果保留但强度降低

**平板**：
- 双列网格
- Hero 并排布局

**桌面**：
- 完整 3-4 列网格
- 所有效果全强度
- 最大视觉冲击

---

## 可访问性

**对比**：
- 主要文字（#fafafa）于深色背景（#09090b）= 18.4:1 比例 ✓
- 次要文字（#a1a1aa）于深色背景 = 7.1:1 比例 ✓
- 所有文字达 WCAG AAA

**聚焦状态**：
- 可见聚焦环：`focus-visible:ring-2 focus-visible:ring-violet-500 focus-visible:ring-offset-2 focus-visible:ring-offset-zinc-900`
- 绝不移除聚焦轮廓
- 聚焦环匹配极光点缀色

**运动**：
- 尊重 `prefers-reduced-motion`
- 为所有动画提供静态回退

---

## 实现说明

- 使用 Tailwind CSS v4 配任意值以指定色彩
- 为重复的渐变值创建 CSS 自定义属性
- 需要时用 `style` prop 作动态渐变背景
- 用 `cva` 与 `tailwind-merge` 本地构建所有组件
- 自 `lucide-react` 导入图标
- 网格渐变背景应置于 style.css 文件中，通过 className 应用

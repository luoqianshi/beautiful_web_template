# Brutalist Pixel

> 来源：原创设计（Original Design）— TRAE AI 创意大赛作品

## 基本信息

| 属性 | 值 |
|------|-----|
| 风格ID | `brutalist-pixel` |
| 显示名称 | Brutalist Pixel |
| 模式 | 🌙 深色模式 (Dark) |
| 字体类型 | mono |
| 描述 | 复古像素游戏 CRT 美学与粗野主义设计融合。近黑背景配 3px 硬白边框，零圆角，硬偏移阴影。 |

## 布局创意 (Layout Ideas)

### Nav

固定顶部导航栏，`z-index: 100`，`var(--bg)` 背景配 3px 白色底边框。左侧为 CSS 伪元素绘制的绿色像素方块 Logo + Press Start 2P 像素文字。中部为等宽字体导航链接，2px 边框分隔，hover 变绿并产生辉光。右侧为像素风 CTA 按钮（绿色底 + 黑色字）。

### Marquee

绿色背景 + 黑色像素文字的无限水平滚动条，`animation: marquee 20s linear infinite`，作为导航与 Hero 之间的公告带。

### Hero

全屏 `100vh` 高度。右上角装饰为 TRAE 与 2026 的二进制文字。左侧含绿色竖线 + `borderFlicker` 闪烁标签、`clamp(48px, 10vw, 120px)` 的超大标题（强调文字带 `text-shadow: 4px 4px 0 var(--accent-dim)` 硬阴影）、等宽字体副标题及三组 3px 白边框数据统计卡片。底部为双按钮组（主按钮绿色 + 次按钮白边）。

### Problem

3 列网格（共享边框，`gap: 0`），每格含 Press Start 2P 像素字体编号 `[01]`、正文标题与等宽描述。共享边框设计使三格融为一个整体面板。

### Features

2 列网格，`gap: 24px`。每张卡片 3px 白色边框 + 深色背景，右上角通过 CSS `attr()` 显示像素编号。48px 方形图标容器配 3px 绿色边框与 SVG 图标。Hover 时边框变绿、出现 `6px 6px 0 var(--accent-dim)` 硬阴影并位移 `translate(-3px, -3px)`。

### Tech Stack

4 列网格（共享边框，`gap: 0`），每格居中显示 Press Start 2P 像素字体技术名称与等宽字体角色描述。Hover 时背景加深。共享边框营造电路板般的紧凑网格感。

### Demo Preview

模拟窗口框架（3px 白色边框），标题栏含红/黄/绿圆点与等宽字体 URL，内容区为 16:9 比例的 iframe 预览占位区。

### CTA

居中排版，标题含 `glitch` 动画（`text-shadow` 在红/黄之间偏移闪烁）。双按钮组与 Hero 一致。

### Footer

居中排版，品牌信息使用 Press Start 2P 像素字体，链接使用等宽字体配底部边框 hover 效果。

---

## 完整提示词 (Full Prompt)

# 设计风格：Brutalist Pixel / 像素暴力主义

## 设计哲学

**核心设计理念**：复古像素游戏机 CRT 显示器美学 + 暴力设计（粗边框、硬阴影、无圆角）。

**参考氛围**：8-bit 游戏机、早期互联网终端、黑客终端。

**情感基调**：硬核、技术感、趣味性、极客文化。

Brutalist Pixel 并非简单的"像素风皮肤"。它是一场对早期数字时代美学的彻底致敬——将 CRT 显示器的扫描线、8-bit 游戏机的像素方块与粗野主义的 raw 视觉暴力融为一体。每一个元素都应让人觉得属于一台正在运行的复古终端：粗边框框定信息区块，硬阴影赋予物理重量，阶梯式过渡模拟像素动画的离散感，而霓虹绿则如终端光标般闪烁。

---

## 设计 Token 系统（DNA）

### 色彩系统（CRT 终端）

| 变量名 | 色值 | 用途 |
|--------|------|------|
| `--bg` | `#050505` | 主背景（近纯黑） |
| `--bg-elevated` | `#0a0a0a` | 提升层级背景 |
| `--surface` | `#111111` | 卡片/面板表面 |
| `--surface-2` | `#1a1a1a` | 二级表面（hover 状态） |
| `--border` | `#ffffff` | 主边框（纯白，粗 3px） |
| `--border-dim` | `rgba(255,255,255,0.25)` | 次级边框 |
| `--text` | `#ffffff` | 主文字 |
| `--text-dim` | `#888888` | 次要文字 |
| `--text-faint` | `#444444` | 弱化文字 |
| `--accent` | `#22c55e` | 主强调色（像素绿） |
| `--accent-dim` | `#166534` | 暗化强调色（用于阴影） |
| `--accent-glow` | `rgba(34,197,94,0.4)` | 强调色辉光（用于 glow 效果） |
| `--danger` | `#ef4444` | 危险/红色 |
| `--warning` | `#f59e0b` | 警告/黄色 |

**色彩策略**：极深暗色背景 + 高对比白色边框 + 绿色强调色点缀，整体营造 CRT 屏幕质感。绿色是唯一的交互语言——所有可交互元素在 hover 时变绿并产生辉光。

### 字体系统

**字族**：
```css
/* 像素风标题字体 —— 标签、数字、按钮、页脚 */
--pixel: "Press Start 2P", monospace;

/* 等宽正文字体 —— 副标题、描述、技术说明 */
--mono: "Space Mono", "VT323", monospace;

/* 正文/UI字体 —— 中文主体内容、标题 */
--body: "Noto Sans SC", "PingFang SC", "Microsoft YaHei", sans-serif;
```

**字号梯度**：

| 用途 | 字号 | 字重 |
|------|------|------|
| Hero 标题 | `clamp(48px, 10vw, 120px)` | 900 |
| Section 标题 | `clamp(32px, 5vw, 56px)` | 900 |
| 像素标签 | 8–10px | 400 |
| 正文描述 | 13–15px | 400 |
| 按钮 | 8–9px（像素字体，视觉面积大） | 400 |

**字重分布**：
- 像素字体（Press Start 2P）：仅 400，字重来自字形本身的粗壮感
- 等宽字体（Space Mono）：400/700，描述用常规、导航用粗体
- 正文字体（Noto Sans SC）：400/700/900，标题用极粗 900 营造冲击力

### 间距系统

| 属性 | 桌面端 | 移动端 |
|------|--------|--------|
| 页面内边距 | `100px 32px` | `64px 16px` |
| Hero 区域内边距 | `120px 32px 80px` | — |
| 内容最大宽度 | `1100px` | — |
| 主边框宽度 | `3px` | `3px` |
| 次边框宽度 | `2px` | `2px` |
| 卡片内边距 | `32–40px` | — |
| Grid 间距（Feature） | `24px` | — |
| Grid 间距（Problem、Tech） | `0`（共享边框） | — |

### 圆角

- **全局无圆角**（`border-radius: 0`），粗野设计核心特征。所有元素均为硬边直角。

### 阴影

| 类型 | 值 | 应用场景 |
|------|----|----------|
| 硬阴影（offset shadow，无模糊） | `6px 6px 0 var(--accent-dim)` | Feature 卡片 hover |
| 辉光效果（glow） | `0 0 20px var(--accent-glow)` / `0 0 24px var(--accent-glow)` | 按钮 hover |
| 文字阴影 | `4px 4px 0 var(--accent-dim)` | Hero 标题强调文字 |

**阴影哲学**：拒绝柔和模糊。所有阴影均为零模糊的硬偏移阴影，模拟像素游戏的实体投影。辉光效果仅用于交互态，模拟 CRT 屏幕的荧光发散。

---

## 交互与动效规范

### 过渡

- 所有过渡使用 **`step-end`** 时间函数，模拟像素动画的离散感
- 过渡时长：`0.1–0.15s`（极快响应）

**为何用 `step-end`**：这是本风格的灵魂。传统的 `ease` 或 `linear` 会产生平滑过渡，而 `step-end` 让属性值瞬间跳变，完美复现 8-bit 游戏机的帧动画质感。

### Hover 效果

| 元素 | Hover 行为 |
|------|------------|
| 按钮 | `translate(-2px, -2px)` 位移 + 辉光/颜色反转 |
| Feature 卡片 | `translate(-3px, -3px)` 位移 + 硬阴影 + 边框变色 |
| Tech 条目 | 背景色加深 |
| 导航链接 | 背景变色 + 文字辉光 |

### 动画

| 动画名称 | 时长 | 循环 | 说明 |
|----------|------|------|------|
| Marquee 滚动条 | 20s | 无限 | 线性循环，水平滚动 |
| `borderFlicker` | 4s | 无限 | 强调色/暗色交替闪烁 |
| `glitch` | 3s | 无限 | 红/黄偏移闪烁，CTA 区域标题 |
| 滚动揭示 | 0.6s | 单次 | `IntersectionObserver` 触发，`opacity: 0→1` + `translateY(30px→0)`，`step-end` 过渡 |

### 滚动

- `scroll-behavior: smooth` — 全局平滑滚动
- `cursor: crosshair` — 十字光标（全局），强化终端操作感

---

## 全局装饰层

| 装饰层 | 定位 | 说明 |
|--------|------|------|
| 像素网格背景 | `fixed` | 8×8px 网格线，`rgba(255,255,255,0.03)` 极淡 |
| 扫描线覆盖层 | `fixed`, `z-index: 9999` | 模拟 CRT 显示器扫描线，`opacity: 0.3` |
| 文字选中样式 | — | 绿色底 + 黑色字 |

这两个固定叠加层是营造 CRT 质感的关键。像素网格提供数字坐标系般的底层背景，扫描线则赋予整个页面"正在通过旧显示器观看"的幻觉。

---

## 组件规范

### 按钮

| 类型 | 类名 | 样式 |
|------|------|------|
| 主按钮 | `btn-brutal-primary` | 绿色背景 + 黑色文字 + 绿色边框 |
| 次按钮 | `btn-brutal-secondary` | 深色背景 + 白色文字 + 白色边框 |

**共同特征**：Press Start 2P 像素字体、3px 边框、hover 位移 `translate(-2px, -2px)` + 颜色反转。

```css
.btn-brutal {
  font-family: var(--pixel);
  font-size: 9px;
  padding: 16px 32px;
  transition: all 0.1s step-end;
  letter-spacing: 0.05em;
  line-height: 1.6;
}

.btn-brutal-primary {
  background: var(--accent);
  color: #000;
  border: 3px solid var(--accent);
}

.btn-brutal-primary:hover {
  background: var(--bg);
  color: var(--accent);
  box-shadow: 0 0 24px var(--accent-glow);
  transform: translate(-2px, -2px);
}
```

### 卡片与容器

**结构**：
- 背景：`var(--surface)`（`#111111`）
- 边框：`3px solid var(--border)`（纯白）
- 圆角：`0`（无圆角）
- 内边距：`32px` 至 `40px`

**共享边框模式**（Problem、Tech Stack）：
- `gap: 0`，相邻卡片共享 3px 白色边框
- 营造电路板/像素阵列般的紧凑网格感

**悬停行为**：
- 边框：过渡至 `var(--accent)`（绿色）
- 阴影：增加 `6px 6px 0 var(--accent-dim)` 硬偏移阴影
- 位移：`translate(-3px, -3px)` 向左上偏移
- 时长：`0.15s step-end`

---

## 布局原则

### 信息架构（页面结构）

页面从上到下依次为：

```
┌──────────────────────────────┐
│  1. Fixed Nav                │  ← 固定顶部导航
├──────────────────────────────┤
│  2. Marquee Bar              │  ← 滚动公告条
├──────────────────────────────┤
│  3. Hero（全屏 100vh）        │  ← 项目介绍 + 统计 + CTA
├──────────────────────────────┤
│  4. Problem                  │  ← 3 个痛点卡片（3列网格）
├──────────────────────────────┤
│  5. Features                 │  ← 6 个功能卡片（2×3 网格）
├──────────────────────────────┤
│  6. Tech Stack               │  ← 8 个技术条目（4×2 网格）
├──────────────────────────────┤
│  7. Demo Preview             │  ← iframe 模拟窗口
├──────────────────────────────┤
│  8. CTA                      │  ← 行动号召
├──────────────────────────────┤
│  9. Footer                   │  ← 品牌信息 + 链接
└──────────────────────────────┘
```

### 网格模式

- **3 列共享边框**：Problem 区，`grid-template-columns: repeat(3, 1fr)`，`gap: 0`
- **2 列间距网格**：Feature 区，`grid-template-columns: repeat(2, 1fr)`，`gap: 24px`
- **4 列共享边框**：Tech Stack 区，`grid-template-columns: repeat(4, 1fr)`，`gap: 0`

### 区块分隔

所有 `section` 均以 `border-bottom: 3px solid var(--border)` 分隔，形成清晰的硬切分。区块间无需多余间距装饰——3px 白线即是最好的分隔符。

---

## "大胆要素"（非通用性）

这些是定义 Brutalist Pixel 风格的**强制性标志性元素**。缺少这些，设计即不完整：

### 1. **全局零圆角**
所有元素 `border-radius: 0`。这是粗野设计的核心——无柔和曲线，唯有硬边直角。

### 2. **3px 纯白硬边框**
所有区块与卡片使用 `3px solid #ffffff` 边框。边框不是装饰，而是结构——它框定信息、区隔区块、赋予每个元素物理边界。

### 3. **`step-end` 过渡**
所有过渡使用 `step-end` 时间函数，时长 `0.1–0.15s`。这是像素动画的灵魂——属性值瞬间跳变，拒绝平滑插值。

### 4. **CRT 扫描线叠加**
固定全屏覆盖层，`repeating-linear-gradient` 模拟 CRT 扫描线，`opacity: 0.3`。这是"通过旧显示器观看"幻觉的关键。

### 5. **像素网格背景**
固定全屏 8×8px 网格线背景，极低不透明度。提供数字坐标系般的底层质感。

### 6. **Press Start 2P 像素字体**
所有标签、编号、按钮、页脚必须使用 Press Start 2P。这一字体即定义了整个风格的像素身份。

### 7. **硬偏移阴影**
卡片 hover 产生 `6px 6px 0 var(--accent-dim)` 零模糊硬阴影。模拟像素游戏的实体投影，拒绝柔和漫射。

### 8. **十字光标**
全局 `cursor: crosshair`。强化终端/瞄准器般的操作感。

### 9. **霓虹绿交互语言**
`#22c55e` 是唯一的交互色。所有 hover、聚焦、激活态均使用绿色或绿色辉光。

### 10. **故障动画**
CTA 标题使用 `glitch` 动画，`text-shadow` 在红/黄之间偏移闪烁。模拟 CRT 信号干扰，是风格的高潮时刻。

---

## 反模式（应避免之事）

### 切勿：
1. **使用任何圆角**——`border-radius` 永远为 0
2. **使用柔和阴影**——所有阴影必须为零模糊的硬偏移
3. **使用 `ease` 或 `linear` 过渡**——必须使用 `step-end`
4. **使用明亮多彩的调色板**——唯有黑/白/绿三色
5. **添加柔和渐变**——这是硬核像素风，不是柔和梦幻风
6. **忽略扫描线叠加**——它是 CRT 质感的核心
7. **用现代无衬线字体替代 Press Start 2P**——像素字体不可妥协
8. **使用过长的过渡时长**——0.15s 已是上限
9. **添加弹跳或弹性动画**——像素动画是离散的，不是弹性的
10. **使用圆点列表符号**——用像素编号 `[01]`、`[02]` 替代

---

## 响应式策略

### `max-width: 900px`

- Problem / Feature 切换为单列布局
- Tech 切换为 2 列布局
- 隐藏导航链接和装饰文字

### `max-width: 600px`

- 页面内边距缩小
- Tech 切换为单列布局
- 按钮尺寸缩小
- Stat 卡片切换为弹性布局

---

## 可访问性考量

### 对比度要求：
- **白色文字对黑色背景**：21:1（超过 WCAG AAA）
- **绿色强调色对黑色背景**：8.6:1（优秀）
- **次要文字（#888888）对黑色背景**：5.3:1（达 WCAG AA）

### 运动偏好：
- 尊重 `prefers-reduced-motion` 媒体查询
- 禁用 `glitch`、`borderFlicker` 等闪烁动画
- 保留功能，移除装饰性运动

### 语义化 HTML：
- 使用正确的标题层级（h1 → h2 → h3）
- 导航用 `<nav>`，内容用 `<main>`，页脚用 `<footer>`
- 装饰性二进制文字设 `pointer-events: none` 与 `user-select: none`

---

## 设计 Token 参考（快速复制）

```css
:root {
  --bg: #050505;
  --bg-elevated: #0a0a0a;
  --surface: #111111;
  --surface-2: #1a1a1a;
  --border: #ffffff;
  --border-dim: rgba(255,255,255,0.25);
  --text: #ffffff;
  --text-dim: #888888;
  --text-faint: #444444;
  --accent: #22c55e;
  --accent-dim: #166534;
  --accent-glow: rgba(34,197,94,0.4);
  --danger: #ef4444;
  --warning: #f59e0b;
  --pixel: "Press Start 2P", monospace;
  --mono: "Space Mono", "VT323", monospace;
  --body: "Noto Sans SC", "PingFang SC", "Microsoft YaHei", sans-serif;
}
```

---

## 总结

Brutalist Pixel / 像素暴力主义由其**CRT 终端质感**（扫描线、像素网格、十字光标）、**粗野结构**（3px 白边框、零圆角、硬偏移阴影）与**像素动画语言**（`step-end` 过渡、Press Start 2P 字体、故障闪烁）所定义。

当每个元素都仿佛运行在一台 8-bit 游戏机的 CRT 显示器上时，此风格即告成功。当它感觉只是套了像素字体的通用深色主题时，即告失败。

霓虹绿是交互的唯一语言。`step-end` 是运动的唯一节奏。3px 白边框是结构的唯一骨架。三者共同营造出硬核、极客、怀旧的终端体验，致敬早期数字时代的纯粹与暴力美学。

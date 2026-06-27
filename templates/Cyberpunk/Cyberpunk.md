# Cyberpunk

> 来源：[Design Prompts](https://www.designprompts.dev/cyberpunk)

## 基本信息

| 属性 | 值 |
|------|-----|
| 风格ID | `cyberpunk` |
| 显示名称 | Cyberpunk |
| 模式 | 🌙 深色模式 (Dark) |
| 字体类型 | mono |
| 描述 | 黑底高对比霓虹，故障动画，终端/等宽字体，科技感装饰。受 80 年代科幻与黑客文化启发的反乌托邦数字美学。 |

## 布局创意 (Layout Ideas)

### Hero

全幅深色画布，配巨型故障标题（text-5xl 至 text-8xl），具色差与霓虹辉光阴影。非对称 60/40 分割：左侧终端风格副标题配打字光标，右侧全息 HUD 显示配动画面板。网格背景配径向渐变蒙版。整页扫描线叠加。

### Stats

移动端横向 2x2 网格，桌面端 4 列。每个数据置于带边框区块，配等宽标签、大号展示数字与上升趋势指示器。含蓄背景辉光。数据间边框分隔符。

### Product Details

居中全息卡片，配电路网格背景。终端风格标签、大标题、以 >> 符号为前缀的段落。底部认证会话指示器配脉动圆点。

### Features

三列网格（移动端堆叠），配切角卡片。图标置于带边框方块中，悬停时过渡为点缀背景。卡片标题悬停变色。径向渐变背景点缀。区块标题配上划线标签与渐变点缀条。

### Blog

三列终端风格卡片网格，图片配 VHS 扫描线叠加。图片上 Stream ID 徽章。ISO 日期格式、作者名与带箭头的访问链接。整卡悬停上浮配边框辉光。

### How It Works

垂直时间线配中线。菱形步骤标记（旋转方块）配霓虹辉光。桌面端步骤左右交替，移动端左侧堆叠。终端风格步骤编号（STEP_01 等）。

### Benefits

双栏分割——左侧含悬停填充勾选框的收益列表，右侧含完整语法高亮代码编辑器模型，配终端窗口装饰（红黄绿圆点）、行号与闪烁光标。

### Testimonials

2x2 卡片网格，终端头部显示头像（带科技图案）、作者信息与 VERIFIED 徽章。引文配装饰性引号。传输完成页脚配脉动指示器。

### Pricing

三列网格，中间卡片缩放并以更粗点缀边框与霓虹辉光高亮。卡片显示档位名、大号等宽价格、带勾选的特性列表与 CTA 按钮。高亮档位配推荐徽章。

### Faq

切角手风琴项垂直堆叠。问题以 $ 符号为前缀。可折叠回答配虚线边框分隔符，以 > 为前缀。带旋转箭头的动画展开/收起。

### Footer

四列网格（移动端堆叠）。公司信息、带下划线悬停的导航链接、社交图标、版权。链接样式如终端命令。全程等宽字体。

---

## 完整提示词 (Full Prompt)

# Cyberpunk / Glitch 设计系统

## 1. 设计哲学

**核心原则**："高科技，低生活。"美学是数字反乌托邦与高科技黑色现实的碰撞。它捕捉先进技术与社会衰败之间的张力——地下黑客、霓虹浸透的巨型城市与损坏数据流的世界。这不是干净乌托邦式的未来；它粗粝、不完美、明显危险。每个像素都应感觉在被雨水浸透的东京小巷里一台故障 CRT 显示器上渲染，或在地下掩体的流氓终端上。

**气质**：危险、电气、叛逆、激进地未来复古。大量汲取 80 年代科幻（银翼杀手、阿基拉）与黑客文化（黑客帝国、攻壳机动队）的视觉语言。界面应感觉*活的*且易变——嗡嗡作响的数字能量、故障的数据损坏、脉动的原始力量。它不只是网站；它是被黑入的信号、禁忌界面、通往蔓延都市的窗口。

**触感体验**：
- **不完美技术**：拥抱模数转换的伪影。扫描线、色差（RGB 分裂）与信号噪点不是 bug，而是特性。UI 应感觉在努力容纳它显示的数据。
- **虚空 vs. 光**：背景不只是暗，而是虚空。在绝对黑暗之上，霓虹光（青、品红、酸绿）不只是为元素上色——它*照亮*它们。光源应感觉物理，投射定义层级的辉光与阴影。
- **工业粗野主义**：形状坚硬、棱角分明、功利。切角（45 度切割）取代友好的圆角矩形。边框技术而精准，像蓝图或 HUD（平视显示器）图解而非装饰画框。

**令此难忘的视觉签名**：
- **色差**：文字与元素上的 RGB 色彩分裂（红/青偏移阴影）模拟镜头畸变或信号干扰。
- **扫描线**：含蓄水平线叠加，模仿旧 CRT 显示器刷新率，增添纹理并统一构图。
- **故障效果**：通过 clip-path 动画、倾斜变换与闪烁文字实现的刻意"损坏"，暗示不稳定连接或被黑系统。
- **霓虹辉光**：字面发光的文字与边框，配强烈的、多层 box-shadow/text-shadow 堆叠，在深色背景上创造"光剑"或"霓虹招牌"效果。
- **切角**：卡片与按钮上的切角/裁切角，创造军事化、科技面板美学。
- **电路图案**：装饰性 SVG 背景，似 PCB 走线或数据高速公路，暗示底层硬件。

---

## 2. 设计 Token 系统（DNA）

### 色彩（深色模式 — 强制）

```
background:          #0a0a0f      // 深虚空黑，略带蓝底
foreground:          #e0e0e0      // 主要文字，非纯白（更柔和）
card:                #12121a      // 卡片背景，深紫黑
muted:               #1c1c2e      // UI 镀铬/抬升背景
mutedForeground:     #6b7280      // 次要文字，降低对比
accent:              #00ff88      // 主霓虹 - 电光绿（受 Matrix 启发）
accentSecondary:     #ff00ff      // 次霓虹 - 热品红/粉
accentTertiary:      #00d4ff      // 三级霓虹 - 青/电蓝
border:              #2a2a3a      // 含蓄边框
input:               #12121a      // 深输入背景
ring:                #00ff88      // 聚焦环匹配点缀色
destructive:         #ff3366      // 错误/危险红粉
```

### 字体

**字体栈**：
- **标题**：`"Orbitron", "Share Tech Mono", monospace` — 几何、未来、机器人感
- **正文**：`"JetBrains Mono", "Fira Code", "Consolas", monospace` — 干净等宽，终端感
- **点缀/标签**：`"Share Tech Mono", monospace` — 用于 UI 标签、时间戳、徽章

**字号与样式**：
- H1：`text-6xl` 至 `text-8xl`，`font-black`，`uppercase`，`tracking-widest`
- H2：`text-4xl` 至 `text-5xl`，`font-bold`，`uppercase`，`tracking-wide`
- H3：`text-xl` 至 `text-2xl`，`font-semibold`，`uppercase`
- 正文：`text-base`，`font-normal`，`tracking-wide`，`leading-relaxed`
- 代码/标签：`text-sm`，`font-mono`，`uppercase`，`tracking-[0.2em]`

### 圆角与边框

```
radius.none:     0px        // 锐利切割为默认
radius.sm:       2px        // 最小柔化
radius.base:     4px        // 罕见，仅用于输入框
radius.chamfer:  用 clip-path 作角部切割而非 border-radius
```

**边框宽度**：默认 `1px`，强调用 `2px`，边框常用渐变或辉光效果

**切角模式**（通过 clip-path 应用）：
```css
clip-path: polygon(
  0 10px, 10px 0,           /* 左上切割 */
  calc(100% - 10px) 0, 100% 10px,  /* 右上切割 */
  100% calc(100% - 10px), calc(100% - 10px) 100%,  /* 右下切割 */
  10px 100%, 0 calc(100% - 10px)   /* 左下切割 */
);
```

### 阴影与效果

**霓虹辉光（CSS 变量 Token）**：
```css
/* 主霓虹辉光 - 用于悬停状态、聚焦环、高亮元素 */
--box-shadow-neon: 0 0 5px #00ff88, 0 0 10px #00ff8840;

/* 小霓虹辉光 - 含蓄点缀 */
--box-shadow-neon-sm: 0 0 3px #00ff88, 0 0 6px #00ff8830;

/* 大霓虹辉光 - 强调状态、hero 元素 */
--box-shadow-neon-lg: 0 0 10px #00ff88, 0 0 20px #00ff8860, 0 0 40px #00ff8830;

/* 次霓虹（品红） */
--box-shadow-neon-secondary: 0 0 5px #ff00ff, 0 0 20px #ff00ff60;

/* 三级霓虹（青） */
--box-shadow-neon-tertiary: 0 0 5px #00d4ff, 0 0 20px #00d4ff60;
```

**深度文字阴影**：
```css
/* 故障效果文字阴影（用于 hero 标题） */
drop-shadow: 0 0 10px rgba(0, 255, 136, 0.5);

/* 渐变文字辉光 */
drop-shadow: 0 0 20px rgba(0, 255, 136, 0.3);
```

**色差（通过 .cyber-glitch 上的 CSS 动画）**：
通过 ::before 与 ::after 伪元素实现：
- text-shadow: -1px 0 #ff00ff（品红左）
- text-shadow: -1px 0 #00d4ff（青右）
- clip-path 动画作故障效果

### 纹理与图案（对深度至关重要）

1. **扫描线叠加**（CSS 伪元素）：
```css
background: repeating-linear-gradient(
  0deg,
  transparent,
  transparent 2px,
  rgba(0, 0, 0, 0.3) 2px,
  rgba(0, 0, 0, 0.3) 4px
);
pointer-events: none;
```

2. **网格/电路图案**（含蓄背景）：
```css
background-image:
  linear-gradient(rgba(0, 255, 136, 0.03) 1px, transparent 1px),
  linear-gradient(90deg, rgba(0, 255, 136, 0.03) 1px, transparent 1px);
background-size: 50px 50px;
```

3. **噪点纹理**：5-10% 不透明度的含蓄 CSS 噪点滤镜或 SVG 噪点叠加

4. **渐变网格**：角落极低不透明度的点缀色径向渐变

---

## 3. 组件样式

### 按钮

所有按钮使用：
- 字体：等宽
- 文字变换：大写
- 字距：更宽
- 过渡：all 以平滑效果
- 聚焦环：2px 点缀色

**默认变体**：
```
- 背景：透明
- 边框：2px solid accent (#00ff88)
- 文字：点缀色
- Clip-path：.cyber-chamfer-sm（较小切角）
- 悬停：背景填充点缀色，文字变背景色，霓虹辉光阴影
```

**次变体**：
```
- 边框：2px solid accentSecondary (#ff00ff)
- 文字：accentSecondary
- 悬停：填充品红，neon-secondary 辉光
```

**描边变体**：
```
- 边框：1px solid border (#2a2a3a)
- 背景：透明
- 悬停：边框变点缀色，文字变点缀色，出现霓虹辉光
```

**幽灵变体**：
```
- 无边框
- 悬停：背景 accent/10 不透明度，文字变点缀色
```

**故障变体**（CTA）：
```
- 背景：实心点缀色 (#00ff88)
- 文字：背景色（高对比）
- 使用 .cyber-glitch 类作色差效果
- 悬停：亮度提升（filter: brightness(1.1)）
```

### 卡片/容器

**默认卡片变体**：
```
- 背景：card (#12121a)
- 边框：1px solid border (#2a2a3a)
- Clip-path：通过 .cyber-chamfer 类切角
- 过渡：all 300ms 以平滑交互
- 悬停：translateY(-1px)，边框变点缀色，出现霓虹辉光（若 hoverEffect prop）
```

**终端变体**（variant="terminal"）：
```
- 背景：background (#0a0a0f) 而非 card
- 边框：1px solid border
- 自动装饰头部条，配红黄绿圆点
- 内容 padding-top 以容纳头部
- Clip-path：切角
- 用于：博客卡片、FAQ 项、部分定价档位
```

**全息变体**（variant="holographic"）：
```
- 背景：muted (#1c1c2e) 30% 不透明度
- 边框：1px solid accent 30% 不透明度
- Box-shadow：霓虹辉光
- Backdrop-filter：blur 作玻璃拟态效果
- 角部点缀：卡片边缘 4 个小型边框角，用绝对定位
- 用于：Product details 卡片、hero HUD 面板
```

### 输入框

```
- 包裹：relative 定位以容纳前缀图标
- 前缀：">" 符号点缀色，绝对定位左
- 背景：input (#12121a)
- 边框：1px solid border (#2a2a3a)
- Clip-path：.cyber-chamfer-sm
- 文字：等宽，点缀色
- 左内边距：8（以容纳前缀）
- 占位符：mutedForeground，样式如终端提示
- 聚焦：边框变点缀色，霓虹辉光阴影，移除 outline
- 过渡：all 200ms
```

---

## 4. 布局策略

**最大宽度**：主要内容 `max-w-7xl`，全幅区块配包含的内部内容

**网格模式**：
- 特性：`grid-cols-1 md:grid-cols-2 lg:grid-cols-3`，容器配 `-skew-y-1`
- 定价：`grid-cols-1 md:grid-cols-3`，中间卡片放大
- 数据：横向 flex 配 `divide-x divide-border`

**间距**：8px 基础网格。慷慨内边距（区块 `py-24` 至 `py-32`）。密集内部组件间距。

**不对称要求**：
- Hero：至少 60/40 分割
- 至少一个区块含重叠元素（负边距）
- 区块容器用 `rotate-1` 或 `skew-y-1` 变换
- 内容允许时在网格中错峰卡片高度

---

## 5. 非通用性（大胆要素）

**强制标志性选择**：

1. **故障标题**：Hero h1 必须有色差 text-shadow 且有偶尔"故障"的 CSS 动画（随机 skew/translate 闪烁）

2. **扫描线叠加**：整页有含蓄扫描线叠加（通过 body 或 main 的 ::after）

3. **终端美学**：至少一个区块必须感觉像终端（等宽、> 前缀、闪烁光标动画）

4. **真正发光的霓虹边框**：不只是彩色边框——堆叠 box-shadow 创造真实辉光效果

5. **切角**：卡片用 clip-path 作切角/裁切角，而非圆角

6. **动画元素**：
   - 闪烁光标（animation: blink 1s step-end infinite）
   - 含蓄悬停故障效果
   - 渐变边框动画（色相旋转）

7. **电路/网格背景**：至少一个区块背景有可见科技图案

8. **打字/打字机效果**：考虑用于副标题或至少样式为正在打字（尾部光标）

---

## 6. 效果与动画

**运动质感**：锐利、数字、略机械。快速 snaps 而非平滑缓动。

**过渡**：
```css
transition: all 150ms cubic-bezier(0.4, 0, 0.2, 1);
/* 或更数字感： */
transition: all 100ms steps(4);
```

**关键帧动画**：

```css
/* 闪烁光标 */
@keyframes blink {
  50% { opacity: 0; }
}

/* 故障效果 */
@keyframes glitch {
  0%, 100% { transform: translate(0); }
  20% { transform: translate(-2px, 2px); }
  40% { transform: translate(2px, -2px); }
  60% { transform: translate(-1px, -1px); }
  80% { transform: translate(1px, 1px); }
}

/* 扫描线滚动 */
@keyframes scanline {
  0% { transform: translateY(-100%); }
  100% { transform: translateY(100vh); }
}

/* RGB 偏移/色差脉动 */
@keyframes rgbShift {
  0%, 100% { text-shadow: -2px 0 #ff00ff, 2px 0 #00d4ff; }
  50% { text-shadow: 2px 0 #ff00ff, -2px 0 #00d4ff; }
}
```

---

## 7. 图标

**Lucide 图标配置**：
- 描边宽度：`1.5px`（细、技术感）
- 尺寸：通常 `h-5 w-5` 或 `h-6 w-6`
- 颜色：继承文字（通常点缀或前景）
- 样式：通过 filter 悬停时添加含蓄辉光：`drop-shadow(0 0 4px currentColor)`

**图标容器**：将图标置于带辉光效果的带边框方块/六边形中

---

## 8. 响应式策略

**移动端适配**（移动优先方法）：

**字体缩放**：
- Hero h1：text-5xl（移动）→ text-7xl（md）→ text-8xl（lg）
- 副标题：text-base → text-lg → text-xl
- 区块标题：text-4xl → text-5xl
- 所有尺寸保持大写与字距

**布局变化**：
- 导航：< lg 隐藏导航链接，< sm 显示缩写 CTA 文字
- 数据：2x2 网格仅顶部 2 项有边框（移动）→ 4 列带垂直边框（桌面）
- 所有特性/博客/证言网格：单列 → 2 列（md）→ 3 列（lg）
- 定价：垂直堆叠 → 3 列网格，高亮卡片缩放仅 md+
- Hero HUD：移动端隐藏（lg:block）
- 页脚：堆叠为单列 → 4 列网格

**保持元素**：
- 扫描线叠加（全页）
- 所有卡片切角
- 霓虹辉光效果（移动端可降低强度以保性能）
- 网格/电路背景
- 等宽字体
- 终端美学（>、$、前缀）
- 深色配色方案

**触控目标**：
- 所有交互元素最小 44px 高度
- 可点击项间充足间距
- FAQ 手风琴全宽点击区域

---

## 9. 可访问性

**对比**：所有文字达 WCAG AA（点缀绿于深背景 = 7.5:1 比例 — 优秀）

**聚焦状态**：
```css
focus-visible:outline-none
focus-visible:ring-2
focus-visible:ring-accent
focus-visible:ring-offset-2
focus-visible:ring-offset-background
```
加上匹配霓虹美学的辉光效果。

**减少运动**：尊重 `prefers-reduced-motion` — 禁用故障动画，保留静态色差

---

## 10. 实现说明

- 广泛使用 Tailwind 任意值 `[...]` 作自定义阴影与 clip-path
- 色彩用 CSS 变量以实现轻松主题化
- 扫描线通过 CSS 实现，非图片
- 故障动画应含蓄且不频繁（不分散注意）
- 在不同屏幕测试辉光效果（低对比显示器上可能显得泛白）
- 考虑多个 box-shadow 的 GPU 性能 — 谨慎使用 `will-change: transform`

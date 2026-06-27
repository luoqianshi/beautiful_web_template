# Bold Typography

> 来源：[Design Prompts](https://www.designprompts.dev/bold-typography)

## 基本信息

| 属性 | 值 |
|------|-----|
| 风格ID | `bold-typography` |
| 显示名称 | Bold Typography |
| 模式 | 🌙 深色模式 (Dark) |
| 字体类型 | sans-serif |
| 描述 | 字体驱动的设计，将巨型排版作为主要视觉元素。超大标题、极致对比与戏剧性留白，打造海报式构图，让文字成为艺术。 |

## 布局创意 (Layout Ideas)

### Hero

全视口 Hero，超大 H1（text-4xl 至 text-8xl 响应式）占据视口 60% 以上。堆叠布局，标题、副标题、CTA 严格遵循垂直节奏。背景中装饰性超大数字（移动端隐藏）。字体即 Hero。

### Stats

响应式网格（移动 1 列、平板 2 列、桌面 4 列），配巨型数字（text-4xl 至 text-7xl）与微型全大写标签。数字用点缀色以戏剧性跳出。区块用抬升背景营造深度。

### Product Detail

非对称双栏网格（1.2fr / 0.8fr）。左：标题 + 多段描述，配最大宽度约束。右：排印卡片，含评级展示（A+），采用分层文字阴影营造深度与点缀顶边框。

### Features

响应式网格（1-2-3 列），使用 gap-px 边框分隔技巧。每张特性卡片含图标、标题、描述。悬停状态改变背景。移动端紧凑（p-6），桌面端宽敞（p-8）。

### Blog

杂志风响应式网格（1-2-3 列）。每篇文章含图片（含蓄悬停缩放）、等宽字体元信息、悬停变色的超大标题。首篇文章带精选徽章。

### How It Works

垂直阶梯列表，配巨型步骤编号（text-6xl 至 text-8xl），边框色，悬停过渡为点缀色。桌面端三列网格（编号 | 标题 | 描述），移动端堆叠。

### Benefits

双栏布局（桌面端左标题右列表，移动端堆叠）。每项收益含超大点缀编号 + 标题/描述。项目间慷慨间距。

### Testimonials

响应式网格（1-2-3 列），带边框卡片。大号展示衬线引号（text-5xl 至 text-6xl），Playfair Display 斜体引文，灰度头像，紧凑作者信息。

### Pricing

响应式网格（1-2-3 定价档位）。价格为占主导的元素（text-4xl 至 text-6xl）。高亮档位用 2px 点缀边框。紧凑特性列表配小型勾选标记。底部全宽 CTA 按钮。

### Faq

居中单列手风琴。粗体问题（text-lg 至 text-2xl），悬停变色。回答平滑高度/透明度动画，配最大宽度以保可读性。

### Final C T A

反色区块（前景作背景、背景作文字）配居中内容。响应式标题尺寸。平板及以上邮箱输入 + 订阅按钮 flex 行布局，移动端堆叠。背景中装饰性品牌名（移动端隐藏）。

### Footer

极简页脚，响应式 2-4-5 列网格。公司信息移动端跨 2 列。紧凑文字尺寸（text-xs 至 text-sm）。底行含版权 + 社交图标，配水平分隔线。

---

## 完整提示词 (Full Prompt)

# Bold Typography 设计系统

## 设计哲学

Bold Typography 是**海报设计转译为网页**。字体不是装饰——它是整个视觉语言。每个设计决策都服务于字体：色彩为创造对比而存在，空间为框定字形而存在，交互为揭示排印细节而存在。

### 核心原则

1. **字体即 Hero**：标题不只是标签——它们是视觉中心。一个精心排布的 80pt 标题比任何图库照片都更具说服力。

2. **极致尺度对比**：标题与正文之间的落差创造戏剧性。设想 H1 与段落文字之比为 6:1 或更大。

3. **刻意的留白**：白（或黑）空间不是空的——它是围绕字体的画框。慷慨的边距让标题显得有意为之，而非局促。

4. **严格层级**：每个元素有明确等级。没有两个元素争夺注意。视线自然流动：标题 → 副标题 → 正文 → 行动。

5. **克制的调色板**：黑、白、一种点缀色。或许两种。更多色彩会稀释排印冲击力。让字形来做功。

### 气质

**自信、编辑感、刻意**。这不是友好的 SaaS——这是一份设计宣言。页面感觉如画廊展览或奢华杂志跨页。每个字都名副其实。

视觉签名：
- 让你想滚动的大标题
- 展示文字的紧凑字距（`-0.04em` 至 `-0.06em`）
- 标签的宽字距（`0.1em` 至 `0.2em`）
- 移动端文字溢出至边缘
- 下划线作为主要交互暗示
- 无圆角——锐利边缘匹配锐利字体

---

## 设计 Token 系统

### 色彩（深色模式）

```
background:        #0A0A0A    // 近黑，非纯黑
foreground:        #FAFAFA    // 暖白
muted:             #1A1A1A    // 含蓄表面抬升
mutedForeground:   #737373    // 次要文字（深色上达 WCAG AA）
accent:            #FF3D00    // 朱砂——温暖、紧迫、可见
accentForeground:  #0A0A0A    // 点缀上的深色文字
border:            #262626    // 几乎不可见的分隔符
input:             #1A1A1A    // 输入框背景
card:              #0F0F0F    // 略高于背景的抬升
cardForeground:    #FAFAFA
ring:              #FF3D00    // 聚焦状态匹配点缀色
```

点缀色是刻意的：朱砂/红橙对冷暗背景创造紧迫感与温度。使用克制——仅用于标题、关键 CTA 与下划线。

### 字体

**主字体栈**：`"Inter Tight", "Inter", system-ui, sans-serif`
- Inter Tight 用于标题（默认字距更紧）
- 干净、几何、专业

**展示字体栈**：`"Playfair Display", Georgia, serif`
- 仅用于引文与证言
- 与无衬线标题创造优雅对比

**等宽字体栈**：`"JetBrains Mono", "Fira Code", monospace`
- 标签、数据、技术细节

**字号系统**：
```
xs:    0.75rem    // 12px - 小字
sm:    0.875rem   // 14px - 说明
base:  1rem       // 16px - 正文
lg:    1.125rem   // 18px - 引导段
xl:    1.25rem    // 20px - 副标题
2xl:   1.5rem     // 24px - 区块引言
3xl:   2rem       // 32px - H3
4xl:   2.5rem     // 40px - H2
5xl:   3.5rem     // 56px - H1 移动端
6xl:   4.5rem     // 72px - H1 平板端
7xl:   6rem       // 96px - H1 桌面端
8xl:   8rem       // 128px - Hero 陈述
9xl:   10rem      // 160px - 装饰性数字
```

**字距**：
```
tighter:  -0.06em   // 展示标题
tight:    -0.04em   // 大号标题
normal:   -0.01em   // 正文（略收紧）
wide:     0.05em    // 小标签
wider:    0.1em     // 全大写标签
widest:   0.2em     // 稀疏强调
```

**行高**：
```
none:     1         // 单行标题
tight:    1.1       // 多行标题
snug:     1.25      // 副标题
normal:   1.6       // 正文
relaxed:  1.75      // 长篇阅读
```

### 圆角与边框

```
radius:   0px       // 任何地方都无 border-radius。仅锐利边缘。
border:   1px       // 细而精准的分隔符
borderThick: 2px    // 点缀下划线
```

### 阴影与效果

无传统阴影。深度来自：
- **分层文字**：大号柔和文字在小号明亮文字之后
- **下划线**：交互元素下 2-3px 点缀线
- **分隔符**：全宽水平线

```
shadow: none
textShadow: none
```

### 纹理与图案

**含蓄噪点颗粒纹理**：极含蓄的分形噪点图案，1.5% 不透明度，覆盖整个页面，为深色背景增添触感而不突兀。通过内联 SVG data URL 与 feTurbulence 滤镜实现。

**排印分层营造深度**：
- 内容后方低不透明度的装饰性超大数字/文字
- 文字阴影技巧：以边框色偏移 1-2px 的重复文字创造深度，无需传统阴影
- 点缀条：关键元素上含点缀色的细水平条（h-1, w-16）作视觉锚点

---

## 组件样式

### 按钮

主按钮为**纯文字配动画下划线**：
```
- 无背景填充
- 点缀色文字
- 动画下划线：绝对定位 span，h-0.5，bg-accent
- 基础状态：scale-x-100，悬停：scale-x-110
- 大写，宽字距（tracking-wider: 0.1em）
- 字重：600（semibold）
- 内边距：py-2/3/4 视尺寸（sm/default/lg），px-0
- 子元素间隙：gap-2/2.5/3
- 激活状态：translate-y-px 作按压反馈
- 过渡：150ms all
```

次/描边按钮：
```
- 边框：1px solid foreground
- 文字：foreground
- 初始无背景填充
- 悬停：bg-foreground，文字变为背景色（完全反相）
- 锐角（0px 圆角）
- 内边距：px-6（与主按钮不同，需水平内边距）
- 大写，tracking-wider
```

幽灵按钮：
```
- 无边框，无填充
- 文字：mutedForeground
- 内边距：px-4
- 悬停：文字变为 foreground
- 下划线通过 scale-x-0 至 scale-x-100 过渡出现
- 下划线为 h-px（比主按钮更细）
```

所有按钮：
```
- Focus-visible：2px 点缀环，2px offset
- 禁用：pointer-events-none，opacity-50
- inline-flex 以正确对齐
- whitespace-nowrap 防止换行
```

### 卡片/容器

**极简使用卡片。** 内容主要靠以下区隔：
- 慷慨的区块内边距（py-20 至 py-40）
- 全宽水平边框（border-t/border-b）
- 字号阶梯变化
- 背景色交替（background ↔ muted）

当"卡片"必要时（定价、证言）：
```
- 边框：1px solid border（由 `bordered` prop 控制）
- 背景：透明（bg-transparent）
- 无圆角（0px，锐角）
- 无阴影
- 内边距：p-6（移动）至 p-8（桌面）
- 悬停过渡：border-hover 色（150ms）
```

高亮卡片（精选定价档位）：
```
- 边框：2px solid accent（覆盖默认 1px）
- 内容上方小型点缀徽章（bg-accent，px-3 py-1，大写等宽文字）
- 无背景变化，边框是区分器
```

特殊深度技巧（Product Detail 卡片）：
```
- 添加点缀顶边框：absolute h-1 w-16 bg-accent
- 分层文字：以 -z-10 与边框色偏移的重复文字元素
- 无阴影创造含蓄维度感
```

### 输入框

```
- 背景：input 色（#1A1A1A）
- 边框：1px solid border
- border-radius：0px（rounded-none，锐角）
- 高度：h-12（移动）至 h-14（桌面），响应式
- 字号：text-base（16px，防止 iOS 缩放）
- 内边距：px-4
- 文字色：foreground
- 占位符：mutedForeground
- 聚焦：border-accent，无 ring，无辉光，outline-none
- 过渡：colors 150ms
- 禁用：cursor-not-allowed，opacity-50
- 文件输入：文件上传元素的特殊样式
```

特殊情况（Final CTA 反色区块）：
```
- 背景：透明（以显示反色背景）
- 边框：border-background/30（半透明白）
- 文字：background 色（反相）
- 占位符：background/50（半透明）
- 聚焦边框：accent（白底上突出）
```

---

## 布局策略

### 容器
```
maxWidth: 1200px (max-w-5xl)
padding: 24px 移动，48px 平板，64px 桌面
```

### 区块间距
```
py-20 (80px) - 紧凑区块
py-28 (112px) - 标准区块
py-40 (160px) - hero/CTA 区块
```

### 网格哲学
- **非对称网格**：7/5 或 8/4 分割而非 6/6
- **错落对齐**：元素不总是顶部对齐
- **文字列**：max-w-2xl 以保可读性，但标题可全宽

---

## 效果与动画

### 运动哲学
**快速而果断。** 无弹跳缓动。无俏皮延迟。运动自信而直接。

```
duration: 150ms - 微交互（按钮、下划线）
duration: 200ms - 标准过渡（FAQ 手风琴、色彩）
duration: 500ms - 图片悬停效果
easing: cubic-bezier(0.25, 0, 0, 1) - 快出、利落停止
```

### 具体效果

**链接/按钮交互**：
- 下划线缩放动画（幽灵按钮 scale-x-0 至 scale-x-100，主按钮 scale-x-100 至 scale-x-110）
- 文字色过渡（150ms）
- 激活按压反馈：translate-y-px 作触感响应
- 无缩放、无辉光、无弹跳

**卡片悬停**：
- 边框色提亮（border-hover token）
- 特性卡片背景色变化（透明 → muted）
- 无抬升、无阴影、无缩放

**图片悬停**（博客文章）：
- 缩放变换（scale-105）持续 500ms
- 仅图片，非容器
- 容器 overflow hidden

**页面滚动动画**（Framer Motion）：
- 淡入 + 上滑（opacity 0→1，translateY 20px→0）持续 500ms
- 子元素错峰 80ms，首元素前 100ms 延迟
- 视口触发：仅一次，15% 阈值，-50px margin
- 容器错峰，单独 fadeInUp 变体

**FAQ 手风琴**：
- 高度自动动画配透明度淡入
- 200ms 时长配 ease-out
- 图标即时切换（Plus ↔ Minus）

**步骤编号悬停**（How It Works）：
- 从边框色至点缀色的色彩过渡（快速，150ms）
- 无位移，纯色彩变化

---

## 图标

来自 `lucide-react`：
```
- 描边宽度：1.5px（比默认 2px 更细以显优雅）
- 视语境尺寸：
  - 16px：与小文字行内（按钮中箭头）
  - 18px：FAQ 切换、页脚社交图标
  - 20px：标准导航栏图标
  - 24px：特性区块图标（桌面 28px）
- 颜色：currentColor（继承父元素文字色）
- 点缀图标：显式 text-[var(--accent)] 类
- 样式：克制使用——优先用文字标签
- 定位：按钮中图标在文字左，特性卡片中在文字上
- 切勿使用填充图标，始终用轮廓/描边样式
```

按区块的图标映射：
```
特性：Users, Zap, BarChart3, Link, Shield, Headphones, Globe（来自 data.icon 字段）
社交：Twitter, Linkedin, Github
UI 控件：Plus, Minus（FAQ），ArrowRight（CTA），Check（定价特性）
```

---

## 响应式策略

**移动优先字体缩放**：
- 标题：text-3xl（移动）→ text-4xl/5xl（平板）→ text-6xl/7xl/8xl（桌面）
- Hero 标题：text-4xl → text-5xl → text-6xl → text-7xl → text-8xl（渐进增强）
- 正文：text-base（16px）贯穿，关键区块 md:text-lg
- 所有尺寸保持层级比例
- 图标尺寸：16px-18px 行内，24px 标准，移动端缩小

**布局切换**：
- 数据：1 列 → 2 列（sm）→ 4 列（md）
- 特性：1 列 → 2 列（sm）→ 3 列（lg）
- 博客/证言/定价：1 列 → 2 列（sm）→ 3 列（lg）
- How It Works：堆叠 → 3 列网格（编号|标题|描述）（lg）
- 收益：堆叠 → 2 列并排（lg）
- 页脚：2 列 → 4 列（md）→ 5 列（lg）
- 非对称网格在移动端堆叠

**间距调整**：
- 区块内边距：py-20（移动）→ py-28（md）→ py-32/40（lg）
- 容器内边距：px-6（移动）→ px-12（md）→ px-16（lg）
- 间距阶梯：gap-4 → gap-6 → gap-8 渐进
- 卡片内边距：p-6（移动）→ p-8（md+）

**移动端专项修正**：
- 移动端隐藏装饰性溢出元素（大号"01"、"ACME"文字）以防水平滚动
- 减小装饰性数字尺寸以防布局破坏
- 确保触控目标最小 44x44px（按钮移动 h-12，桌面 h-14）
- 移动端堆叠邮箱输入 + 按钮，平板及以上并排
- 调整导航间距在更小屏幕上更紧凑

**字体完整性**：
- 标题用响应式类平滑缩放（绝不所有尺寸单一字号）
- 跨断点保持字距一致
- 确保下划线可见且可触（最小 2px）
- 更小屏幕略增行高以保可读性
- 正文最大宽度约束防止过长行（max-w-xl, max-w-2xl, max-w-3xl）

---

## 可访问性

**对比**：
- foreground（#FAFAFA）于 background（#0A0A0A）= 18.1:1 ✓
- mutedForeground（#737373）于 background = 5.3:1 ✓（AA）
- accent（#FF3D00）于 background = 5.4:1 ✓（大文字 AA）

**聚焦状态**：
- 2px 点缀轮廓
- 距元素 2px offset
- 无辉光、无填充变化
- 所有交互元素上可见

**字体**：
- 正文最小 16px
- 正文行高最小 1.5
- 无 400 以下细字重

**交互**：
- 触控目标最小 44x44px
- 下划线 2px+ 以保可见
- 色彩绝非唯一指示器

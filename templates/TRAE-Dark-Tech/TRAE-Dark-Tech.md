# TRAE 深色科技风格提示词文档

---

## 1. 基本信息

| 项目 | 内容 |
|------|------|
| 风格名称 | TRAE 深色科技风格 |
| 风格关键词 | 深色模式、科技感、赛博朋克、极简主义、荧光绿、粒子动画、开发者社区、高对比度、玻璃拟态、胶囊按钮、渐变光晕 |
| 主色调 | 纯黑 `#0a0a0a` / 荧光绿 `#22c55e` |
| 字体 | Inter / SF Pro Display / Noto Sans SC / PingFang SC |
| 等宽字体 | JetBrains Mono / SF Mono |
| 主要圆角 | 胶囊形 `9999px`、卡片 `16px`、输入框 `8px` |
| 核心动画 | Canvas 粒子连线背景、Hover 绿色光晕、滚动淡入上浮 |
| 目标场景 | 开发者社区、技术产品展示、SaaS 官网、作品展示墙 |
| 一句话风格 | 一个以纯黑为画布、荧光绿为画笔的科技感网站，通过流动的粒子网络背景、高对比度的视觉层级和精致的胶囊形 UI 组件，打造出专业、前沿、充满活力的现代开发者社区体验。 |

---

## 2. 设计哲学

这是一种**深色模式下的现代科技风格**，融合了赛博朋克的冷峻感与极简主义的克制感。它像一间深夜的实验室：黑色背景是安静的实验台，荧光绿是示波器上跳动的信号，白色文字是清晰的读数，灰色文字是辅助的标注。整个设计通过极高的对比度让信息一目了然，同时用微妙的绿色光晕和流动粒子营造出前沿、专业、充满活力的氛围。

此设计**不是**温暖柔和的消费级 UI，**不是**色彩斑斓的插画风格，**不是**厚重拟物的复古风格。它拒绝冗余装饰，强调功能优先、结构清晰、交互反馈即时。整体气质是冷静的、工程师的、未来感的，但又不至于冰冷——胶囊形按钮和圆角卡片带来恰到好处的亲和力。

---

## 3. Token 系统

### 3.1 色彩 Token

| 名称 | 色值 | 用途 |
|------|------|------|
| `--bg-base` | `#0a0a0a` | 主背景色 |
| `--bg-card` | `#18181b` | 卡片、面板、登录卡片背景 |
| `--bg-tag` | `#27272a` | 标签、输入框背景 |
| `--bg-tag-hover` | `#3f3f46` | 标签/输入框 Hover 背景 |
| `--border` | `#27272a` | 默认边框、分割线 |
| `--border-strong` | `#3f3f46` | 激活边框、Hover 边框 |
| `--accent` | `#22c55e` | 主强调色：按钮、高亮、进度条、选中态 |
| `--accent-deep` | `#16a34a` | 次强调色：Hover 状态、渐变终点 |
| `--accent-glow` | `rgba(34, 197, 94, 0.35)` | 绿色光晕阴影 |
| `--accent-soft` | `rgba(34, 197, 94, 0.12)` | 柔和绿色背景（如胶囊标签） |
| `--text-primary` | `#ffffff` | 主标题、关键文字 |
| `--text-secondary` | `#a1a1aa` | 副标题、次级文字 |
| `--text-tertiary` | `#d4d4d8` | 第三级文字、标签文字 |
| `--text-muted` | `#71717a` | 辅助说明、Placeholder、元信息 |
| `--gold` | `#fbbf24` | 排行榜第一名 |
| `--silver` | `#a1a1aa` | 排行榜第二名 |
| `--bronze` | `#b45309` | 排行榜第三名 |

### 3.2 排版 Token

| 层级 | 字号 | 字重 | 行高 | 字间距 | 颜色 |
|------|------|------|------|--------|------|
| Hero 标题 | `clamp(40px, 6vw, 64px)` | 800 | 1.1 | -1.5px | 白色，关键词渐变绿 |
| H1 / 页面标题 | 32-40px | 700 | 1.2 | normal | 白色 |
| H2 / 区块标题 | 28-36px | 700 | 1.2 | normal | 白色 |
| H3 / 卡片标题 | 18-20px | 600 | 1.3 | normal | 白色 |
| Body 正文 | 14-16px | 400 | 1.6-1.7 | normal | `#a1a1aa` |
| Caption / 标签 | 12-14px | 400-500 | 1.5 | 0.5px | `#71717a` |
| 等宽标注 | 12-14px | 500-600 | 1.5 | 1-2px | `#22c55e` 或 `#71717a` |

字体栈：

```css
--font-sans: "Inter", "SF Pro Display", -apple-system, BlinkMacSystemFont,
             "PingFang SC", "Microsoft YaHei", "Segoe UI", sans-serif;
--font-mono: "JetBrains Mono", "SF Mono", Menlo, Consolas, monospace;
```

### 3.3 间距与布局 Token

| 名称 | 值 | 用途 |
|------|------|------|
| 容器最大宽度 | 1200-1280px | 内容区居中 |
| 容器内边距 | 32px（桌面）/ 20px（移动端） | 左右留白 |
| 区块上下间距 | 80-120px / `100px 0` | section 之间 |
| 卡片网格间距 | 16-24px | grid gap |
| 导航栏高度 | 64px | 固定顶部导航 |
| Hero 高度 | `min-height: 100vh` | 首屏 |
| 响应式断点 | 1024px / 768px | 桌面 / 平板 / 手机 |

### 3.4 圆角与阴影 Token

| 名称 | 值 | 用途 |
|------|------|------|
| 胶囊圆角 | `9999px` | 按钮、标签、CTA |
| 卡片圆角 | 16px | 卡片、面板、色块 |
| 输入框圆角 | 8px | 表单输入框 |
| 排行榜条目圆角 | 12px | rank item |
| 主按钮 Hover 阴影 | `0 8px 24px rgba(34, 197, 94, 0.35)` | 绿色弥散光晕 |
| 卡片 Hover 阴影 | `0 0 24px rgba(34, 197, 94, 0.12)` | 柔和绿色辉光 |
| 登录卡片阴影 | `0 0 60px rgba(34, 197, 94, 0.08)` | 大面积弱光晕 |

---

## 4. 布局创意

### 4.1 全局结构

页面采用经典的**固定导航 + 全屏 Hero + 内容网格 + 页脚**结构，内容区最大宽度 1200-1280px 居中，区块之间保持 80-120px 的慷慨间距。整体为深色背景，所有内容浮于一层固定的 Canvas 粒子网络之上。

```
┌─────────────────────────────────────┐
│  Navbar (fixed, 64px, blur bg)      │
├─────────────────────────────────────┤
│                                     │
│  Hero (100vh, particle background)  │
│  [pill tag]                         │
│  [H1 headline]                      │
│  [subtitle]                         │
│  [Primary CTA] [Secondary CTA]      │
│                                     │
├─────────────────────────────────────┤
│  Section 1 · Color/Typography/...   │
│  ── Section header ──               │
│  [grid cards]                       │
├─────────────────────────────────────┤
│  Section 2 · Components             │
│  [component showcase blocks]        │
├─────────────────────────────────────┤
│  Section 3 · Motion / Responsive   │
│  [animation cards] [device mockups] │
├─────────────────────────────────────┤
│  Footer                             │
└─────────────────────────────────────┘
```

### 4.2 导航栏

- 固定顶部，高度 64px，全宽
- 初始状态：透明或半透明黑色 `rgba(10,10,10,0.55)`
- 滚动后：加深为 `rgba(10,10,10,0.85)`，并添加 `backdrop-filter: blur(12-14px)`
- 左侧：Logo（绿色渐变方块 + 字母）+ 站点名称
- 中间：导航链接，当前项有绿色下划线或绿色背景高亮
- 右侧：登录（次按钮）+ 开始构建/注册（主按钮）

### 4.3 Hero 区域

- 占满首屏 `min-height: 100vh`，内容居中偏左
- 顶部一个绿色边框的胶囊标签，内含脉冲小圆点
- 主标题使用大号白色文字，关键词使用荧光绿渐变文字
- 副标题为灰色，限制最大宽度
- CTA 按钮组：主按钮绿色填充 + 次按钮透明边框

### 4.4 内容网格

- 响应式网格：`grid-template-columns: repeat(auto-fill, minmax(280px, 1fr))`
- 卡片深灰背景 `#18181b`，1px 暗灰边框，Hover 时边框变绿并产生光晕
- 区块头部包含：绿色编号、标题（标题中关键词渐变）、等宽小字标注

### 4.5 响应式适配

- **桌面 > 1024px**：完整多列布局，导航链接全部显示
- **平板 768-1024px**：网格变为 2 列，导航可能收拢
- **手机 < 768px**：单列布局，导航变为汉堡菜单，Hero 标题缩小，按钮垂直排列全宽

---

## 5. 组件样式

### 5.1 按钮 Buttons

```css
.btn {
  display: inline-flex;
  align-items: center;
  gap: 6-8px;
  padding: 10px 20px;          /* 默认 */
  padding: 14px 28px;          /* 大号 */
  padding: 6px 14px;           /* 小号 */
  border-radius: 9999px;
  font-size: 14-15px;
  font-weight: 500-600;
  transition: all 0.2s ease;
}

.btn-primary {
  background: #22c55e;
  color: #000;
}
.btn-primary:hover {
  background: #16a34a;
  transform: translateY(-1px);
  box-shadow: 0 8px 24px rgba(34, 197, 94, 0.35);
}

.btn-secondary / .btn-ghost {
  background: transparent;
  border: 1px solid #3f3f46;
  color: #fff;
}
.btn-secondary:hover {
  border-color: #22c55e;
  color: #22c55e;
}
```

### 5.2 标签 Tags / Pills

```css
.tag {
  padding: 6px 16px;
  border-radius: 9999px;
  background: #27272a;
  color: #d4d4d8;
  font-size: 13px;
  transition: all 0.2s ease;
}
.tag:hover {
  border-color: #22c55e;
  color: #22c55e;
}
.tag.active {
  background: #22c55e;
  color: #000;
}
.tag.outline {
  background: transparent;
  border: 1px solid #3f3f46;
}
```

### 5.3 卡片 Cards

```css
.demo-card {
  background: #18181b;
  border: 1px solid #27272a;
  border-radius: 16px;
  overflow: hidden;
  transition: all 0.3s ease;
}
.demo-card:hover {
  border-color: #22c55e;
  box-shadow: 0 0 24px rgba(34, 197, 94, 0.12);
  transform: translateY(-4px);
}
```

卡片图片区域常用 16:9 比例，背景为深色渐变 + 绿色径向光晕 + 细网格线，中央放置一个带绿色边框和光晕的图标。

### 5.4 排行榜 Leaderboard

```css
.rank-item {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 14px 20px;
  background: rgba(24, 24, 27, 0.6);
  border-radius: 12px;
  margin-bottom: 10px;
}
.rank-num.gold   { background: #fbbf24; color: #000; }
.rank-num.silver { background: #a1a1aa; color: #000; }
.rank-num.bronze { background: #b45309; color: #fff; }
.rank-bar-fill {
  height: 4-6px;
  background: #22c55e;
  border-radius: 2px;
  transition: width 1.5s ease;
}
```

### 5.5 输入框 Inputs

```css
.form-input {
  width: 100%;
  padding: 12px 16px;
  background: #27272a;
  border: 1px solid #3f3f46;
  border-radius: 8px;
  color: #fff;
  font-size: 14px;
  transition: border-color 0.2s, box-shadow 0.2s;
}
.form-input::placeholder { color: #71717a; }
.form-input:focus {
  outline: none;
  border-color: #22c55e;
  box-shadow: 0 0 0 3px rgba(34, 197, 94, 0.1);
}
```

### 5.6 登录卡片 Auth Card

```css
.login-card {
  max-width: 420px;
  padding: 40px;
  background: #18181b;
  border: 1px solid #27272a;
  border-radius: 24px;
  box-shadow: 0 0 60px rgba(34, 197, 94, 0.08);
}
```

---

## 6. 效果与动画

### 6.1 背景动画：粒子网络（核心签名）

使用 Canvas 2D 实现固定全屏背景：

- 粒子颜色：`rgba(34, 197, 94, 0.3-0.6)`
- 粒子数量：80-120 个，根据屏幕面积动态调整
- 粒子大小：随机 0.6-2px
- 粒子速度：缓慢漂移，碰撞边界反弹
- 连线规则：粒子间距 < 120px 时绘制半透明连线
- 鼠标交互：鼠标靠近时粒子被吸引/排斥，并与鼠标产生连线
- 实现层：`position: fixed; z-index: 0; pointer-events: none;`

```js
const PARTICLE_COUNT = 80;
const CONNECTION_DIST = 120;
const MOUSE_DIST = 150;

// 粒子更新、绘制、连线逻辑
// 参考实现：canvas 2D + requestAnimationFrame
```

### 6.2 交互动效

| 元素 | 触发 | 效果 | 时长 | 缓动 |
|------|------|------|------|------|
| 主按钮 | Hover | 背景变深绿 + 上移 1-2px + 绿色阴影扩散 | 0.2s | ease |
| 次按钮 | Hover | 边框变绿 + 文字变绿 | 0.2s | ease |
| 卡片 | Hover | 边框变绿 + 上浮 4px + 绿色光晕 | 0.3s | ease |
| 标签 | Hover | 边框变绿 / 文字变绿 | 0.2s | ease |
| 输入框 | Focus | 绿色边框 + 绿色外发光 | 0.2s | ease |

### 6.3 滚动与入场动画

- 导航栏滚动：滚动超过 20-50px 后，背景从透明加深并添加模糊
- 元素入场：使用 IntersectionObserver 触发 `opacity: 0 -> 1` + `translateY(30px) -> 0`，持续 0.6s
- 进度条动画：进入视口时宽度从 0 过渡到目标值，持续 1.5-1.6s ease-out
- 胶囊标签小圆点：脉冲动画 `scale(1) -> scale(0.8)` + 透明度变化，2s infinite
- 滚动提示线：上下伸缩动画，2.4s infinite

### 6.4 图标动画

使用 SVG 图标替代 emoji，并为关键图标添加动画：

- 闪电图标：脉冲 + drop-shadow 绿色光晕
- 星星图标：填充透明 -> 绿色填充循环
- 齿轮图标：旋转
- 箭头图标：左右轻微移动
- 三角形：stroke-dashoffset 描边动画
- 菱形：旋转 + 缩放呼吸效果

---

## 7. 大胆要素 / 签名特征

1. **纯黑画布 + 荧光绿强调**：极高的对比度是第一眼识别特征，绿色仅作为点缀色出现，但足够强烈。
2. **流动的粒子网络背景**：全屏 Canvas 粒子连线动画，是此风格最具辨识度的视觉元素，营造出科技感和沉浸感。
3. **胶囊形 UI 组件**：从按钮到标签到 CTA 大量使用 `9999px` 圆角，形成统一、现代、亲和的组件语言。
4. **绿色光晕 Hover 反馈**：几乎所有可交互元素 Hover 时都会产生绿色边框或绿色阴影，反馈即时且一致。
5. **渐变绿色文字**：Hero 标题中的关键词使用 `background-clip: text` 绿色渐变，增加视觉焦点。
6. **金/银/铜排行榜徽章**：排行榜前三名使用金属色徽章，与整体深色科技风格形成对比，增加荣誉感。
7. **玻璃拟态导航栏**：滚动后导航栏背景加深并添加 `backdrop-filter: blur`，保持轻盈与高级感。
8. **等宽字体标注**：使用 JetBrains Mono 等字体显示编号、技术标注、元信息，强化开发者社区氛围。

---

## 8. 完整提示词

> 用于直接复制给代码生成 Agent，以生成同风格页面。

```markdown
请使用以下设计系统创建一个现代科技风格的网页/落地页：

## 整体风格
一个以纯黑为画布、荧光绿为画笔的深色科技风格网站。整体气质专业、前沿、充满活力，面向开发者社区或技术产品。融合赛博朋克与极简主义，强调高对比度、清晰的信息层级和精致的微交互。

## 色彩系统
- 主背景：#0a0a0a
- 卡片/面板背景：#18181b
- 标签/输入框背景：#27272a
- 边框：#27272a，激活/悬停边框：#3f3f46
- 主强调色：#22c55e（荧光绿）
- 次强调色/悬停：#16a34a
- 绿色光晕：rgba(34, 197, 94, 0.35)
- 柔和绿背景：rgba(34, 197, 94, 0.12)
- 主标题文字：#ffffff
- 副标题文字：#a1a1aa
- 第三级文字：#d4d4d8
- 辅助/占位文字：#71717a
- 排行榜金/银/铜：#fbbf24 / #a1a1aa / #b45309

## 字体
- 无衬线：Inter, "SF Pro Display", -apple-system, BlinkMacSystemFont, "PingFang SC", "Microsoft YaHei", "Segoe UI", sans-serif
- 等宽："JetBrains Mono", "SF Mono", Menlo, Consolas, monospace
- Hero 标题：clamp(40px, 6vw, 64px), weight 800, line-height 1.1, letter-spacing -1.5px
- 页面标题：32-40px, weight 700, line-height 1.2
- 卡片标题：18-20px, weight 600
- 正文：14-16px, weight 400, line-height 1.6-1.7, color #a1a1aa
- 标签/辅助：12-14px, weight 500

## 布局
- 固定导航栏：高度 64px，初始半透明，滚动后加深并加 blur(12-14px)
- Hero：占满首屏 100vh，内容居中偏左，包含胶囊标签、大标题、副标题、CTA 按钮组
- 内容区：最大宽度 1200-1280px 居中，section 间距 80-120px
- 响应式网格：grid-template-columns: repeat(auto-fill, minmax(280px, 1fr))
- 响应式断点：1024px（平板 2 列）、768px（手机单列 + 汉堡菜单）

## 组件
- 按钮：胶囊形（border-radius: 9999px）
  - 主按钮：绿色填充，黑色文字，悬停变深绿 + 上移 + 绿色阴影
  - 次按钮：透明背景，暗灰边框，悬停边框变绿 + 文字变绿
- 标签：胶囊形，暗灰背景，悬停/激活变绿色
- 卡片：16px 圆角，深灰背景，1px 暗灰边框，悬停变绿边框 + 上浮 + 绿色光晕
- 输入框：8px 圆角，暗灰背景，聚焦绿色边框 + 外发光
- 登录卡片：24px 圆角，大面积绿色弱光晕
- 排行榜：前三名金/银/铜徽章，绿色进度条

## 动画
- 背景：Canvas 2D 全屏粒子网络动画，绿色粒子 + 连线 + 鼠标交互
- 导航栏：滚动后背景加深 + 模糊
- 元素入场：滚动触发淡入上浮（opacity 0->1, translateY 30px->0），0.6s ease
- 进度条：进入视口时从 0 宽度过渡到目标值，1.5s ease-out
- 悬停反馈：按钮/卡片/标签悬停时产生绿色光晕或边框高亮
- 图标：SVG 细线图标，悬停时变为绿色；关键图标可添加脉冲/旋转/描边动画

## 技术栈建议
- React / Vue / Next.js
- Tailwind CSS
- Framer Motion（React）或 GSAP 用于复杂动画
- Canvas 2D API 用于粒子背景
- Lucide React / Heroicons 用于图标
- 所有 CSS 代码应可直接运行，使用 CSS 自定义属性管理 Token

## 设计关键词
深色模式、科技感、赛博朋克、极简主义、荧光绿、粒子动画、开发者社区、高对比度、玻璃拟态、胶囊按钮、圆角设计、渐变光晕
```

---

## 9. 文件与输出信息

- 分析源文件：
  - `d:/Data/Design/beautiful_web_template/raw/trae-design-system-Minimax-M3.html`
  - `d:/Data/Design/beautiful_web_template/raw/trae-style-guide.html`
  - `d:/Data/Design/beautiful_web_template/raw/TRAEDemoWall_风格提示词.md`
- 输出目录：`d:/Data/Design/beautiful_web_template/web2template_output/`
- 截图目录：
  - `d:/Data/Design/beautiful_web_template/web2template_output/trae-design-system/screenshots/`
  - `d:/Data/Design/beautiful_web_template/web2template_output/trae-style-guide/screenshots/`
- 设计数据：
  - `d:/Data/Design/beautiful_web_template/web2template_output/trae-design-system/design_data.json`
  - `d:/Data/Design/beautiful_web_template/web2template_output/trae-style-guide/design_data.json`
- 本提示词文档：`d:/Data/Design/beautiful_web_template/web2template_output/trae_dark_tech_style_prompt.md`

---

*一句话风格总结：纯黑画布、荧光绿画笔、流动粒子网络、胶囊形 UI、高对比度科技感的开发者社区风格。*

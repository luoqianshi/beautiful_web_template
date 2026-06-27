# Maximalism

> 来源：[Design Prompts](https://www.designprompts.dev/maximalism)

## 基本信息

| 属性 | 值 |
|------|-----|
| 风格ID | `maximalism` |
| 显示名称 | Maximalism |
| 模式 | 🌙 深色模式 (Dark) |
| 字体类型 | sans-serif |
| 描述 | 冲突的图案、密集的布局、过饱和的色彩、刻意的视觉杂乱。多多益善。 |

## 布局创意 (Layout Ideas)

### Hero

全视口爆炸式构图，配重叠元素、浮动动画形状（星、闪光、emoji）、溢出边缘的巨型背景字体、堆叠多色文字阴影，以及配图案叠加的混乱视觉层。

### Stats

全宽混乱马赛克网格（移动 2x2，桌面 4 列），每个数据在不同鲜艳背景色中。图案圆点叠加、旋转数字配分层文字阴影、悬停旋转的星形装饰。

### Product Details

双栏布局，左侧动画同心旋转圆圈（基点带浮动图标的视觉混乱）。右侧分层容器配偏移阴影层、多阴影卡片、交替色带边框段落。

### Features

3 列网格配交替垂直偏移（错落布局）。每张卡片有悬停旋转的彩色图标容器、透明彩色头部背景，以及悬停增强的多层硬阴影。

### Blog

3 列网格，中间卡片垂直偏移。重叠卡片堆叠配戏剧性悬停上浮效果、彩色日期徽章、渐变图片叠加与缩放/旋转过渡。

### How It Works

3 步布局配横向连接渐变线、不同点缀色的编号圆圈、交替步骤垂直偏移的卡片、居中内容。

### Benefits

双栏非对称布局，左列含标题/CTA，右列含堆叠收益卡片。每张卡片有彩色边框、图标圆圈，悬停时变换（位移 + 缩放）。

### Testimonials

3 列网格配旋转卡片（静止轻微旋转，悬停变正）、彩色星级评分、带点缀色边框的头像图片、中间列垂直偏移。

### Pricing

3 列网格，中间卡片上浮并放大。高亮档位有顶部徽章、发光边框阴影与彩色头部。特性列表配点缀色勾选图标。

### Faq

堆叠手风琴项配鲜艳彩色边框（打开时变化）。打开时旋转 180 度的 chevron 图标。打开状态显现彩色顶边框与透明图案背景。

### Footer

密集 5 列网格配 logo 列与 4 个导航列。渐变 logo、轮换点缀色的彩色区块标题、悬停填充的彩色边框社交图标。

---

## 完整提示词 (Full Prompt)

# 设计风格：Maximalism / 多巴胺

## 设计哲学

**核心原则**：多多益善。Maximalism/多巴胺设计拒绝极简克制，转而追求感官过载、视觉丰沛与毫不掩饰的过度。每个像素都应激发喜悦。空白是浪费空间。图案冲突、色彩尖叫、元素以混乱的意图重叠。

**情感目标**：狂喜、俏皮、压倒性、Y2K 遇上 Z 世代、hyperpop 美学、数字极繁主义。想象 Lisa Frank 的狂热梦境遇上 Nickelodeon 黏液时代遇上当代 hyperpop 专辑封面。它应感觉如边吃彩虹糖边看烟花。

**指导性问题**："这是否以愉悦的方式令人视觉过载？"若答案为否，加更多。

---

## 设计 Token 系统（DNA）

### 色彩调色板（深色模式基础）

**基础色**：
```
Background:    #0D0D1A    (深邃宇宙紫黑 - 让一切跳出的虚空)
Foreground:    #FFFFFF    (纯白 - 最大对比)
Muted:         #2D1B4E    (深紫 - 用于半透明容器)
Border Base:   #FF3AF2    (热品红 - 默认边框色)
```

**五种点缀色**（关键——始终有 5 种独立点缀）：
```
1. Accent (Magenta):    #FF3AF2    (热粉/品红 - 电气能量)
2. Secondary (Cyan):    #00F5D4    (电气青/蓝绿 - 数字辉光)
3. Tertiary (Yellow):   #FFE600    (尖叫黄 - 吸睛)
4. Quaternary (Orange): #FF6B35    (电气橙 - 温暖混乱)
5. Quinary (Purple):    #7B2FFF    (鲜艳紫 - 神秘深度)
```

**用色规则**：
- **区块轮换**：每个主要区块循环 5 种点缀色作主色。用模运算（index % 5）系统轮换。
- **重复元素**：网格中（数据、特性、证言），用相同模运算轮换点缀色。
- **不匹配**：边框应与背景冲突。若背景为品红，边框可能是黄或青。
- **对比比**：尽管混乱，所有关键文字保持白（#FFFFFF）于深（#0D0D1A）= 19.5:1 对比比（AAA）。
- **点缀文字**：仅用点缀色于装饰文字、标签或非关键内容。绝不用作正文。

### 字体系统

**字体栈**：
- **标题**："Outfit"（粗、几何、700-900 字重）或 "Unbounded"（Google Fonts）
- **正文**："DM Sans"（干净、混乱中可读、400-700 字重）
- **展示/点缀**："Bangers" 或 "Bungee"（漫画能量，克制用于特殊强调）

**字号阶梯**（激进尺寸）：
```
Hero 标题：     text-7xl to text-9xl  (72px-128px) - 巨型
区块标题：       text-5xl to text-7xl  (48px-72px) - 粗壮存在
副标题：         text-2xl to text-3xl  (24px-30px) - 突出
正文：           text-lg to text-xl    (18px-20px) - 比典型大
小文字：         text-sm to text-base  (14px-16px) - 标签、元信息
```

**字体样式模式**：
- **字重分布**：标题 = 800-900 字重，正文 = 400-500，标签 = 700 bold
- **字距**：标题 `tracking-tight` 或 `tracking-tighter`，标签 `tracking-widest`，正文正常
- **行高**：标题 = leading-none 或 leading-tight（0.9-1.1），正文 = leading-relaxed（1.625）
- **文字变换**：标题、标签、按钮大写。正文正常大小写。
- **混合字重**：同一标题内用变化字重作强调（一词粗、另一词更粗）

**文字阴影系统**（关键——始终使用）：
```
单阴影：     text-shadow: 2px 2px 0px #7B2FFF
双阴影：     text-shadow: 2px 2px 0px #7B2FFF, 4px 4px 0px #FF3AF2
三重堆叠：   text-shadow: 2px 2px 0px #7B2FFF, 4px 4px 0px #FF3AF2, 6px 6px 0px #00F5D4
巨型堆叠：   text-shadow: 4px 4px 0px #7B2FFF, 8px 8px 0px #FF3AF2, 12px 12px 0px #00F5D4
```
- 模式：偏移 2px 递增，轮换点缀色
- 标题用三重或巨型堆叠
- 副标题用双阴影
- 卡片标题用单或双阴影

**渐变文字**：
- 用于 20-30% 标题以增变化
- 模式：`background: linear-gradient(90deg, #FF3AF2, #00F5D4, #FFE600, #FF3AF2)`
- background-size 设 200-300% 并用 gradient shift 动画
- 用 `background-clip: text` 与 `-webkit-text-fill-color: transparent`

### 边框与圆角系统

**边框宽度**（大胆）：
```
标准：   border-4  (4px - 最常见)
重：     border-8  (8px - 区块分隔符、精选元素)
含蓄：   border-2  (2px - 仅内部分隔符)
```

**边框样式**（刻意混合）：
- **实线**：大多数容器与卡片默认
- **虚线**：30% 边框用于变化（`border-dashed`）
- **点线**：罕见，用于小型装饰元素
- **双线**：偶尔用于特殊容器（`border-double`）
- **关键规则**：单个区块内刻意用 2-3 种不同边框样式

**圆角值**：
```
按钮：       rounded-full     (9999px - 胶囊形)
卡片：       rounded-3xl      (24px - 慷慨曲线)
容器：       rounded-2xl      (16px - 适度曲线)
锐角点缀：   rounded-none     (0px - 克制用于对比)
混合：       不同角用不同圆角以增非对称
```

**边框色策略**：
- 主：与背景冲突的点缀色
- 绝不：中性或柔和边框
- 技巧：若背景用 accent-1，边框用 accent-2 或 accent-3

### 阴影与辉光系统（多层）

**辉光阴影**（彩色、柔和、发光）：
```
基础辉光：
  box-shadow: 0 0 20px rgba(255, 58, 242, 0.5),
              0 0 40px rgba(0, 245, 212, 0.3);

大辉光：
  box-shadow: 0 0 40px rgba(255, 58, 242, 0.6),
              0 0 80px rgba(255, 230, 0, 0.4),
              0 0 120px rgba(123, 47, 255, 0.3);
```
- 用于：按钮、图标、精选元素
- 悬停：不透明度增 0.1-0.2，扩散增 50%
- 结合 2-3 色以增丰富辉光

**硬阴影**（偏移、扁平、堆叠）：
```
双堆叠：
  box-shadow: 8px 8px 0 #FFE600,
              16px 16px 0 #FF3AF2;

三堆叠：
  box-shadow: 12px 12px 0 #00F5D4,
              24px 24px 0 #FF3AF2,
              36px 36px 0 #FFE600;
```
- 模式：每层偏移翻倍（8→16→24 或 12→24→36）
- 颜色：每层轮换不同点缀
- 用于：卡片、容器、突出按钮
- 悬停：偏移增 2-4px 以模拟上浮

**阴影混合**：
- Hero 元素结合辉光 + 硬阴影
- 示例：`box-shadow: 0 0 30px rgba(255,58,242,0.6), 8px 8px 0 #FFE600, 16px 16px 0 #FF3AF2`

### 纹理与图案系统（强制分层）

**图案类型**（始终最少分层 2-3）：

1. **点阵网格**：
```css
background-image: radial-gradient(circle, #FF3AF2 1px, transparent 1px);
background-size: 20px 20px;
```
- 变化点尺寸（1px-2px）与间距（20px-40px）
- 每区块用不同点缀色

2. **对角条纹**：
```css
background-image: repeating-linear-gradient(
  45deg,
  transparent,
  transparent 10px,
  rgba(255, 230, 0, 0.08) 10px,
  rgba(255, 230, 0, 0.08) 20px
);
```
- 保持低不透明度（0.05-0.1）以免过载
- 变化条纹宽（10-20px）与角度（30deg-60deg）

3. **棋盘格**：
```css
background-image: conic-gradient(
  from 90deg at 1px 1px,
  transparent 90deg,
  rgba(0, 245, 212, 0.05) 0
);
background-size: 40px 40px;
```
- 含蓄不透明度（0.03-0.07）
- 变化网格尺寸（30px-50px）

4. **渐变网格**（径向重叠）：
```css
background:
  radial-gradient(ellipse at 20% 30%, rgba(255,58,242,0.15) 0%, transparent 50%),
  radial-gradient(ellipse at 80% 70%, rgba(0,245,212,0.15) 0%, transparent 50%),
  radial-gradient(ellipse at 50% 50%, rgba(123,47,255,0.1) 0%, transparent 60%);
```
- 椭圆置于不同位置
- 用 2-4 个重叠渐变
- 保持低不透明度（0.1-0.2）

**图案分层策略**：
- **全局基础**：整页 2 个固定图案（点 + 条纹）
- **区块特定**：每个主要区块添加 1-2 个独特图案
- **实现**：用伪元素（::before、::after）配 `pointer-events: none`
- **混合模式**：部分层应用 `mix-blend-mode: overlay` 或 `screen` 以更深整合
- **不透明度范围**：每图案 0.05-0.3（堆叠相乘）

---

## 组件样式原则

### 按钮

**主按钮**（最大冲击）：
- 背景：跨 3 点缀的渐变 `bg-gradient-to-r from-[#FF3AF2] via-[#7B2FFF] to-[#00F5D4]`
- 边框：`border-4 border-[#FFE600]`（冲突黄）
- 圆角：`rounded-full`
- 阴影：结合辉光 + 硬阴影
- 文字：`font-black uppercase tracking-widest`
- 尺寸：`h-14 px-10`（默认），`h-16 px-12`（大）
- 悬停：缩放至 110%，增强阴影（不透明度增 0.2），偏移渐变位置
- 激活：缩放至 95%，减少阴影
- 聚焦：双环 `ring-4 ring-[color-1] ring-offset-4 ring-offset-[color-2]`

**次按钮**（反相处理）：
- 背景：透明
- 边框：`border-4 border-dashed border-[accent-color]`
- 悬停：填充实心点缀色，边框变实，缩放至 105%
- 文字全程保持对比

**描边按钮**（堆叠阴影样式）：
- 背景：半透明 `bg-max-muted/50`
- 边框：`border-4 border-[accent]`
- 阴影：硬堆叠阴影（8px/8px, 16px/16px）
- 悬停：按负阴影偏移位移，增加阴影深度
- 激活：位移至零，移除阴影（按压效果）

**幽灵按钮**（含蓄但俏皮）：
- 渐变下划线装饰
- 悬停：显现背景图案或浅填充
- 悬停缩放至 105%

### 卡片与容器

**基础卡片结构**：
- 背景：半透明 `bg-[#2D1B4E]/80` 配 `backdrop-blur-sm`
- 边框：`border-4` 点缀色（每卡轮换）
- 圆角：`rounded-3xl`（24px）
- 阴影：硬堆叠阴影（8px/8px + 16px/16px 双色）
- 内边距：`p-8` 至 `p-12`（慷慨内部空间）

**非对称技巧**：
- 用 `clip-path` 切一角：`polygon(0 0, 100% 0, 100% calc(100% - 24px), calc(100% - 24px) 100%, 0 100%)`
- 轻微旋转：`rotate-1` 或 `rotate-2`
- 偏移定位：应用负外边距 `-mt-4` 或 `-ml-2`

**卡片悬停状态**：
- 旋转更多：`hover:rotate-2`（从基础旋转增加）
- 放大：`hover:scale-[1.02]`
- 阴影偏移：偏移增 2-4px 并加第三色
- 过渡：`transition-all duration-300 ease-out`

**卡片内部结构**：
- 头部：底边框 `border-b-4 border-dashed` 不同点缀，可选背景色调
- 内容：标准内边距 `p-6`
- 标题：文字阴影、大写、font-black、text-2xl
- 描述：略柔和文字 `text-white/80`

**卡片上图案叠加**：
- 添加图案作背景或 ::before 伪元素
- 保持极低不透明度（0.1-0.2）以保内容可读
- 每卡轮换图案类型以增变化

### 表单输入

**输入字段**：
- 背景：半透明 `bg-[#2D1B4E]/50` 配 `backdrop-blur-sm`
- 边框：`border-4 border-[accent]` — 厚而彩色
- 圆角：单行输入 `rounded-full`，文本区 `rounded-2xl`
- 内边距：`px-6 py-4` — 慷慨以增舒适
- 文字：`text-lg font-bold text-white`
- 占位符：`text-white/40` — 可见但含蓄

**聚焦状态**（双环系统）：
- 边框色偏移：`focus:border-[accent-2]`（与默认不同）
- 内辉光：`focus:shadow-[0_0_20px_rgba(color,0.5)]`
- 环系统：`focus:ring-4 focus:ring-[color-1]/30 focus:ring-offset-2 focus:ring-offset-[color-2]`
- 背景增强：`focus:bg-[#2D1B4E]`（更不透明）
- 过渡：`transition-all duration-300`

**标签**：
- 位置：浮动于输入上方或行内
- 样式：展示字体、点缀色、轻微旋转 `rotate-1`
- 动画：聚焦时可脉动或发光

### 交互状态（通用模式）

**悬停**：
- 始终结合 2-3 变化：缩放 + 色彩 + 阴影
- 缩放：视元素尺寸 102%-110%
- 色彩：边框/背景偏移至不同点缀
- 阴影：增强强度（更高不透明度、更大扩散或更多层）
- 时长：大多数 300ms，小元素 200ms

**激活/按下**：
- 缩小：95%-98%
- 阴影减少：移除层或减偏移
- 轻微位移：沿阴影方向移动以模拟按压

**聚焦**（可访问性关键）：
- 始终双环系统：`ring-4 ring-[color-1] ring-offset-4 ring-offset-[color-2]`
- 环用对比点缀色
- 确保总环厚（环 + offset）最小 8px
- 绝不仅靠色彩——也含轮廓样式变化
- 考虑 `outline-dashed` 以增可见

**禁用**：
- 不透明度：50%
- 光标：`cursor-not-allowed`
- 移除所有悬停/激活状态
- 保持边框可见但降色彩饱和

---

## 布局原则

**间距系统**（慷慨而密集）：
- **基础单位**：4px（Tailwind 默认）
- **区块内边距**：`py-24` 至 `py-32`（96px-128px 垂直）— 区块间慷慨呼吸空间
- **容器内边距**：`px-6`（移动）至 `px-8`（桌面）— 一致水平边距
- **内部间距**：网格中 `gap-6` 至 `gap-12` — 刻意变化
- **卡片内边距**：`p-8` 至 `p-12` — 舒适内部空间
- **元素间隙**：堆叠内容 `space-y-4` 至 `space-y-6`

**密集打包策略**：
- 元素应感觉近但不拥挤
- 战略性用负外边距：`-mt-8`、`-ml-4` 创造重叠
- 卡片轻微偏移堆叠以增深度

**网格使用**（打破网格哲学）：
- **绝不完美**：避免对称、均匀间距网格
- **可变列**：用 `grid-cols-1 md:grid-cols-2 lg:grid-cols-3` 但以 `col-span-2` 混 `col-span-1` 打破
- **垂直偏移**：每隔一项应用 `translate-y-8` 或 `md:translate-y-12`（用模运算：`i % 2 === 1`）
- **变化高度**：让内容自然决定高度，不强制等高
- **间隙变化**：同区块内用不同间隙尺寸（`gap-4` 然后 `gap-8`）

**最大宽度策略**：
- **容器**：大多数区块 `max-w-7xl`（1280px）
- **全幅**：Hero 与部分特性区块用 `max-w-none` 或 `max-w-screen`
- **窄内容**：阅读内容用 `max-w-3xl`（768px）

**Z-Index 分层**（重叠关键）：
```
背景图案：   z-0
内容基础：   z-10
重叠卡片：   z-20
浮动装饰：   z-30
模态/叠加：  z-40
固定头部：   z-50
```
- 父级用 relative 定位建立上下文
- 应用负外边距 + 更高 z-index 创造有意重叠

---

## "大胆要素"（非通用签名）

这些是使 Maximalism 不可错认的**强制**元素：

### 1. 浮动装饰形状
- **什么**：散布布局的 SVG 图标（星、闪光、圆、方）与 emoji
- **放置**：绝对定位配特定坐标（`top-[10%] left-[5%]`）
- **尺寸**：从 `h-6 w-6` 至 `h-24 w-24` 变化 — 刻意不一致
- **样式**：点缀色填充，常带动画
- **动画**：应用 float、wiggle、spin-slow 或 bounce-subtle
- **密度**：每个全高区块最少 5-10 个形状
- **实现**：创建可复用组件，在 relative 父级内绝对定位

### 2. 巨型背景字体
- **什么**：内容后方超大文字，部分可见，溢出边缘
- **尺寸**：`text-[12rem]` 至 `text-[20rem]` — 刻意过大超视口
- **样式**：`opacity-20`，半透明点缀色或柔和
- **定位**：绝对，用 transform 居中，或自边缘溢出
- **内容**：单个有力词（WOW、YES、GO 等）或重复图案
- **目的**：增添深度并强化极繁混乱

### 3. 图案叠图案分层
- **最少**：每个区块必须至少 2 个重叠图案
- **常见组合**：点 over 条纹、棋盘 over 渐变、网格 over 点
- **全局 + 局部**：固定全局图案（2）+ 区块特定图案（1-2）
- **可见性**：保持单个图案不透明度低（0.05-0.15）但分层以累积效果
- **变化**：跨区块轮换图案类型（hero = 网格+点，特性 = 条纹+棋盘等）

### 4. 系统色彩轮换
- **规则**：每个主要区块高亮 5 种点缀色中的不同一种
- **模式**：Hero = 品红，数据 =（全 5），特性 = 青，收益 = 橙等
- **重复元素**：网格中用 index 模 5 循环色彩
- **实现**：色彩存数组，用 `colors[index % colors.length]` 访问
- **一致**：相同色不主导连续区块

### 5. 冲突边框色
- **绝不匹配**：边框色应与背景色冲突
- **示例**：
  - 品红背景 → 黄边框
  - 青背景 → 橙边框
  - 黄背景 → 品红边框
- **对比**：从调色板对侧选色
- **厚度**：始终 `border-4` 或 `border-8` — 使冲突可见

### 6. 多层阴影
- **绝不仅单层**：每个抬升元素最少 2-3 阴影层
- **类型**：结合辉光阴影（柔和、彩色）与硬阴影（偏移、扁平）
- **颜色**：每阴影层用不同点缀色
- **渐进**：硬阴影偏移 2x 递增（8px → 16px → 32px）
- **悬停**：添加层或增强强度，绝不仅改色

### 7. 非对称元素定位
- **无完美对齐**：同行元素处于不同垂直位置
- **技巧**：交替项应用 `translate-y-8` 或 `-translate-y-4`
- **旋转**：跨卡片混合 `rotate-1`、`rotate-2`、`-rotate-1`
- **倾斜**：偶尔容器 `skew-x-2`
- **重叠**：用负外边距使元素重叠区块边界

### 8. 区块内混合边框样式
- **规则**：同区块用 2-3 种不同边框样式
- **混合**：部分卡片实线边框、其他虚线、点缀点线
- **示例**：特性卡片实线边框、图标容器虚线、区块分隔符双线
- **目的**：增添受控混乱美学

### 9. Emoji 作装饰元素
- **使用**：散布全程（🚀✨💫🎯💬⚡💰🔥❓）
- **尺寸**：大 `text-6xl` 至 `text-7xl`
- **动画**：应用 bounce、float、wiggle
- **放置**：区块标题、装饰点缀、浮动元素
- **频率**：每个主要区块 1-2 个

### 10. 动画渐变文字
- **什么**：带动画多色渐变背景的标题
- **颜色**：线性渐变中 3-4 点缀色
- **动画**：背景位置持续偏移（4s 时长）
- **使用**：20-30% 主要标题
- **实现**：`background-clip: text`、`-webkit-text-fill-color: transparent`、动画 `background-position`

---

## 动画与运动

**运动哲学**：弹跳、俏皮、吸睛。无物应感觉静态或僵硬。

**时机关系**：
```
超快：    100-200ms   (小交互、图标旋转)
快：      200-300ms   (悬停状态、按钮按下)
标准：    300-500ms   (卡片过渡、布局位移)
慢：      1-2s        (摆动、脉动、弹跳动画)
很慢：    4-8s        (漂浮、渐变偏移)
超慢：    20s         (旋转、背景旋转)
```

**缓动函数**：
- 默认：`ease-out`（快起、缓终）
- 弹跳：`cubic-bezier(0.68, -0.55, 0.265, 1.55)`（过冲效果）
- 平滑：`ease-in-out`（两端渐进）

**关键帧动画**：

1. **Float**（轻柔垂直移动）：
```css
@keyframes float {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  50%      { transform: translateY(-20px) rotate(5deg); }
}
时长：6s ease-in-out infinite
```

2. **Float Reverse**（向上移动）：
```css
@keyframes float-reverse {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  50%      { transform: translateY(20px) rotate(-5deg); }
}
时长：5s ease-in-out infinite
```

3. **Pulse Glow**（阴影强度变化）：
```css
@keyframes pulse-glow {
  0%, 100% { box-shadow: 0 0 20px rgba(255, 58, 242, 0.5); }
  50%      { box-shadow: 0 0 40px rgba(255, 58, 242, 0.8), 0 0 60px rgba(0, 245, 212, 0.5); }
}
时长：2s ease-in-out infinite
```

4. **Gradient Shift**（背景位置动画）：
```css
@keyframes gradient-shift {
  0%   { background-position: 0% 50%; }
  50%  { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
时长：4s ease infinite
要求：background-size 设 200-300%
```

5. **Spin Slow**（持续旋转）：
```css
@keyframes spin-slow {
  from { transform: rotate(0deg); }
  to   { transform: rotate(360deg); }
}
时长：20s linear infinite
```

6. **Wiggle**（来回旋转）：
```css
@keyframes wiggle {
  0%, 100% { transform: rotate(-3deg); }
  50%      { transform: rotate(3deg); }
}
时长：1s ease-in-out infinite
```

7. **Bounce Subtle**（垂直弹跳）：
```css
@keyframes bounce-subtle {
  0%, 100% { transform: translateY(0); }
  50%      { transform: translateY(-10px); }
}
时长：2s ease-in-out infinite
```

**动画分配**：
- **浮动形状**：Float、float-reverse 或 float-slow
- **关键 CTA**：Pulse-glow
- **渐变文字/背景**：Gradient-shift
- **装饰环/边框**：Spin-slow
- **Emoji/图标**：Wiggle 或 bounce-subtle
- **Hero 元素**：组合（float + pulse-glow）

**性能优化**：
- 仅用 `transform` 与 `opacity`（GPU 加速）
- 动画元素加 `will-change: transform`
- 避免直接动画 width、height 或 color

**减少运动**：
- 尊重 `prefers-reduced-motion: reduce`
- 禁用关键帧动画
- 保留悬停/激活过渡但减时长至 150ms
- 保持所有视觉样式，仅移除持续运动

---

## 反模式（应避免之事）

这些选择将**破坏** Maximalism 美学：

### 1. 中性或柔和边框
- **错误**：`border-gray-300` 或 `border-white/20`
- **正确**：`border-[#FF3AF2]` 或 `border-[#FFE600]`
- **原因**：边框必须是跳出的鲜艳点缀色

### 2. 单层阴影
- **错误**：`shadow-lg` 或单色阴影
- **正确**：堆叠彩色阴影（辉光 + 硬，或硬 + 硬）
- **原因**：深度来自分层，非柔和

### 3. 完美对齐网格
- **错误**：等间距等高对称网格
- **正确**：配垂直偏移、旋转与变化尺寸的打破网格
- **原因**：Maximalism 拥抱受控混乱

### 4. 空背景区块
- **错误**：无图案或纹理的纯色背景
- **正确**：2-3 层图案（点、条纹、网格）
- **原因**：Maximalism 中空白是浪费空间

### 5. 含蓄或小字体
- **错误**：标题 `text-base` 或 `text-lg`
- **正确**：标题 `text-5xl` 至 `text-9xl`
- **原因**：Maximalism 大声且毫不掩饰

### 6. 单色配色
- **错误**：全程用一种点缀色
- **正确**：系统轮换所有 5 种点缀色
- **原因**：更多色彩 = 更多多巴胺

### 7. 极简或无悬停状态
- **错误**：悬停仅变色
- **正确**：缩放 + 旋转 + 阴影变化结合
- **原因**：交互应感觉愉悦且夸张

### 8. 细边框（1-2px）
- **错误**：`border` 或 `border-2`
- **正确**：`border-4` 或 `border-8`
- **原因**：边框是设计声明，非事后想法

### 9. 克制按钮样式
- **错误**：简单纯色按钮配含蓄阴影
- **正确**：渐变背景、冲突边框、堆叠阴影、悬停缩放
- **原因**：CTA 应要求注意

### 10. 标题无文字阴影
- **错误**：无阴影扁平文字
- **正确**：不同点缀色的 2-3 层文字阴影
- **原因**：深度与维度使文字跳出

### 11. 边框与背景色匹配
- **错误**：品红背景配品红边框
- **正确**：品红背景配黄或青边框
- **原因**：冲突创造视觉趣味

### 12. 静态元素（无动画）
- **错误**：所有元素仅 CSS 过渡静态
- **正确**：30-40% 元素有持续动画（float、wiggle、pulse）
- **原因**：运动增添生命与能量

---

## 可访问性与最佳实践

**色彩对比**（不可妥协）：
- **文字对比**：白（#FFFFFF）于深（#0D0D1A）保持 19.5:1 比例（AAA）
- **点缀色使用**：绝不用点缀色作正文或关键信息
- **可读背景**：文字在点缀色背景上时确保：
  - 深点缀（品红、紫、青）上白字
  - 浅点缀（黄、浅青）上深字（#0D0D1A）
- **测试**：用对比检查器验证所有文字达 WCAG AA 最低（正常文字 4.5:1，大文字 3:1）

**聚焦状态**（最大可见）：
- **双环系统**：`ring-4 ring-[color-1] ring-offset-4 ring-offset-[color-2]`
- **色彩对比**：环色应与元素与背景均对比
- **总厚度**：最小 8px（环 + offset 合计）
- **额外指示器**：结合色彩变化与轮廓样式（`outline-dashed`）
- **绝不**：仅靠色彩——始终含结构变化
- **键盘导航**：所有交互元素必须键盘可访问

**运动敏感**（尊重用户偏好）：
```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.15s !important;
  }
}
```
- 禁用所有关键帧动画（float、pulse、spin）
- 过渡时长减至最小（150ms）
- 保留悬停/激活状态但无夸张运动
- 保持所有视觉样式（色彩、边框、阴影）

**屏幕阅读器考量**：
- 装饰 emoji 与浮动形状应设 `aria-hidden="true"`
- 图案叠加应为纯 CSS，非内容
- 确保语义 HTML 结构（正确标题层级）
- 所有交互元素需可访问标签

**性能**：
- 动画用 `transform` 与 `opacity`（GPU 加速）
- 谨慎加 `will-change: transform` 于动画元素
- 优先 CSS 渐变图案而非图片
- 考虑 `backdrop-filter` 支持并提供回退

**触控目标**：
- 最小尺寸：所有交互元素 44x44px
- 按钮默认 `h-14`（56px）— 远超最小
- 确保触控目标间充足间距（最小 8px 间隙）

---

## 布局与间距节奏

**垂直节奏**（区块流）：
```
区块内边距：       py-24 to py-32   (区块间 96px-128px)
区块内边距：       mb-16 to mb-20   (标题与内容间 64px-80px)
内容分组：         space-y-8 to space-y-12 (内容块间 32px-48px)
元素堆叠：         space-y-4 to space-y-6  (元素间 16px-24px)
```

**水平节奏**：
```
容器内边距：       px-6（移动），px-8（桌面）
网格间隙：         gap-6 to gap-12（刻意变化）
卡片内边距：       p-8 to p-12
按钮内边距：       px-10 to px-12
输入内边距：       px-6
```

**响应式断点**：
- **移动**（`< 768px`）：
  - 所有网格垂直堆叠
  - 保持图案密度（减至 1-2 图案，非零）
  - 保持点缀色与边框（勿简化）
  - 缩小字体但保持大胆（Hero 最小 text-4xl）
  - 减少浮动形状（5-6 而非 10-12）
  - 保持旋转与偏移效果

- **平板**（`768px - 1024px`）：
  - 桌面 3 列处用 2 列网格
  - 完整图案处理回归
  - 所有动画激活

- **桌面**（`> 1024px`）：
  - 完整 3-4 列网格
  - 最大图案密度
  - 所有装饰元素可见

**移动端关键规则**：勿简化为"干净极简"。保持混乱，只是垂直堆叠。

---

## 图标指南

**图标来源**：Lucide React（或类似开源图标集）

**图标尺寸**：
```
小：      h-5 w-5     (20px)
默认：    h-10 w-10   (40px)
大：      h-16 w-16   (64px)
装饰：    h-24 w-24   (96px)
```

**图标样式**：
- **描边宽度**：厚 `stroke-[2.5px]` 至 `stroke-[3px]` 以保可见
- **颜色**：始终点缀色，绝不柔和
- **容器**：包裹于彩色形状：
  - 圆：`rounded-full`
  - 方：`rounded-xl`
  - 边框：`border-4 border-[accent]`
  - 背景：半透明点缀 `bg-[accent]/20`
- **动画**：图标悬停时可旋转、弹跳或脉动

**图标放置**：
- 特性卡片：顶部大图标
- 按钮：与文字行内小图标
- 浮动装饰：多样尺寸，绝对定位
- 导航：中等尺寸，悬停彩色

---

## 实现说明

**技术假设**：
- **CSS 框架**：Tailwind CSS v4（用任意值 `[]` 语法）
- **动画**：CSS 关键帧定义于样式表，通过工具类应用
- **图案**：CSS 渐变背景，非图片
- **组件**：用组件变体（CVA）构建以保一致
- **图标**：Lucide React 或类似 SVG 图标库

**配置文件结构**：
```typescript
export const config = {
  colors: { background, foreground, muted, accent, secondary, tertiary, quaternary, quinary, border },
  fonts: { heading, body, display },
  radius: { base, button, card },
  shadows: { glow, glowLg, multi, multiLg }
}
```

**可复用模式**：
- 为图案创建工具类（`.pattern-dots`、`.pattern-stripes`、`.pattern-checker`、`.pattern-mesh`）
- 创建阴影工具（`.shadow-multi`、`.shadow-multi-lg`、`.glow-accent`、`.glow-accent-lg`）
- 创建动画类（`.animate-float`、`.animate-pulse-glow` 等）
- 存色彩数组供轮换：`['accent', 'secondary', 'tertiary', 'quaternary', 'quinary']`

**组件方法**：
- 构建 Button 配 4 变体（default、secondary、outline、ghost）
- 构建 Card 配可组合部分（Card、CardHeader、CardTitle、CardDescription、CardContent、CardFooter）
- 构建 Input 配内置聚焦状态
- 所有组件用 `cn()` 工具合并类

---

**最终提醒**：若看起来"太多"——可能正好。Maximalism 关于丰沛、喜悦与视觉刺激。设计应让人立即有所感。克制在此不受欢迎。每个元素都是色彩、图案、阴影、动画与愉悦的机会。

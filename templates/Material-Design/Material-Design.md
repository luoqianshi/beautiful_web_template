# Material

> 来源：[Design Prompts](https://www.designprompts.dev/material-design)

## 基本信息

| 属性 | 值 |
|------|-----|
| 风格ID | `material-design` |
| 显示名称 | Material |
| 模式 | ☀️ 浅色模式 (Light) |
| 字体类型 | sans-serif |
| 描述 | 活泼、动感的色彩提取，胶囊形按钮与分明的层级状态。基于 Google Material Design 3，增强深度与微交互。 |

## 布局创意 (Layout Ideas)

### Hero

大圆角容器（48px 圆角）配装饰性有机模糊形状，桌面端分割布局配抽象几何形状，移动端居中

### Stats

圆角卡片网格（24px 圆角）配色调背景，悬停效果配阴影抬升，居中数字值配 primary 色点缀

### Product Detail

双栏分割布局配文字内容与抽象形状可视化，慷慨内边距，图片容器 shadow-inner

### Features

卡片网格配色调表面背景，图标容器用 secondary 色，悬停缩放与阴影效果，慷慨内边距

### Blog

卡片网格，图片宽高比 3:2，悬停图片缩放，色调表面背景，大写元信息文字配 primary 色

### How It Works

悬停时带辉光效果的编号圆形徽章位于圆角内容卡片上方，垂直步进器布局配阴影过渡

### Benefits

全宽彩色容器配径向渐变叠加与模糊形状，嵌套玻璃拟态卡片配边框、backdrop blur 与悬停效果

### Testimonials

色调表面容器背景上的卡片网格，头像 + 内容布局，primary 色星级评分，悬停阴影抬升

### Pricing

卡片网格，中间卡片上浮（-translate-y-4），精选档位 ring 高亮，胶囊形 CTA 徽章，列表项配勾选标记与悬停位移

### Faq

柔和背景上的简单堆叠圆角容器配悬停状态过渡，单列居中布局

### Final C T A

全宽彩色容器配多个模糊形状与径向渐变，居中邮箱输入配胶囊形按钮

### Footer

极简配顶边框，水平 flex 布局配链接与悬停色彩过渡

---

## 完整提示词 (Full Prompt)

# 设计风格：Material You（Material Design 3）

## 设计哲学

**核心原则**：个性化、自适应、有活力。Material You（MD3）代表从 Material Design 2 僵硬的"纸与墨"隐喻向更有机、更具表现力系统的转变。设计从种子色提取调色板（模拟基于壁纸的个性化），强调色调表面而非刺眼白，并使用有机形状配柔和曲线。

**气质**：友好、柔软、圆润、多彩、个性化。美学感觉现代而亲和，通过色调表面慷慨用色而非仅点缀高亮。运动平滑自信，绝不突兀。每次交互都感觉触感且响应，微动画提供令人满足的反馈。

**增强实现细节**：
此实现超越 Material Design 3 基线规范，融入：
- **分层深度**：多个模糊形状、径向渐变与阴影组合创造氛围背景
- **丰富微交互**：悬停状态含缩放变换、阴影抬升、辉光效果与平滑色彩过渡
- **非对称抬升**：精选卡片（如定价档位）用垂直位移创造视觉层级
- **渐进显现**：元素通过阴影过渡与背景不透明度变化在交互时显现深度
- **触感反馈**：所有交互元素含 active:scale-95 作按压反馈，增强物理感

**与 MD2 的关键区别**：
- 色调表面系统取代纯白背景
- 胶囊形按钮取代圆角矩形
- 有机形状与模糊效果取代扁平几何图案
- 状态层（不透明度叠加）取代实心色变化
- 多层氛围效果创造丰富视觉深度
- 每个交互元素的微交互增强感知品质

## 设计 Token 系统（DNA）

### 色彩（浅色模式）

Material You 使用从种子色衍生的精致色调调色板。此实现用 **Purple/Violet 种子**（#6750A4）。

**核心调色板结构**：
- **Background (Surface)**：`#FFFBFE` — 略暖近白，非纯白
- **Foreground (On Surface)**：`#1C1B1F` — 近黑略带暖意
- **Primary**：`#6750A4` — 浓郁紫（种子色）
- **On Primary**：`#FFFFFF` — Primary 上纯白文字
- **Secondary Container**：`#E8DEF8` — 浅薰衣草色调
- **On Secondary Container**：`#1D192B` — 次级表面深色文字
- **Tertiary**：`#7D5260` — 互补 mauve/灰玫瑰
- **Surface Container**：`#F3EDF7` — 含蓄着色表面，比背景深一级
- **Surface Container Low (Muted)**：`#E7E0EC` — 用于输入框与凹陷表面
- **Outline (Border)**：`#79747E` — 中灰边框
- **On Surface Variant**：`#49454F` — 用于次要文字与图标

**色彩关系规则**：
- 用表面色调创造深度层级：Background → Surface Container → Surface Container Low
- Primary 色应出现于 CTA、聚焦状态与关键交互元素
- Secondary Container 用于胶囊、芯片与较不突出的容器
- Tertiary 用于点缀元素与 FAB（浮动操作按钮）
- 绝不用纯白（#FFFFFF）作背景——始终用着色 Surface 色
- 彩色背景上（primary/tertiary），用透明白/黑叠加作状态

**状态层不透明度模式**：
- 实色上悬停：基色 90%（`bg-md-primary/90`）
- 实色上激活/按下：基色 80%（`bg-md-primary/80`）
- 透明表面上悬停：primary 10%（`bg-md-primary/10`）
- 透明表面上聚焦：primary 5%（`bg-md-primary/5`）
- 含蓄叠加效果：20% 不透明度配 backdrop-blur

### 字体

**字族**：**Roboto**（Google Fonts）— Material Design 规范字体
- 加载字重：400（Regular）、500（Medium）、700（Bold）
- 标题默认用 Medium（500）以保持友好亲和感
- 正文用 Regular（400）

**字号阶梯**（Material Design 3 阶梯）：
- **Display Large**：3.5rem / 56px（Hero 标题）
- **Headline Large**：3rem / 48px（区块标题）
- **Headline Medium**：2rem / 32px（子标题）
- **Title Large**：1.5rem / 24px（卡片标题）
- **Body Large**：1.25rem / 20px（引导段）
- **Body Medium**：1rem / 16px（标准正文）
- **Label Medium**：0.875rem / 14px（按钮文字）
- **Label Small**：0.75rem / 12px（说明、元信息）

**字距**：
- 标题：正常至紧（0 至 -0.01em）
- 正文：正常（0）
- 标签/按钮：略宽（0.01em）用于小尺寸 Medium 字重

**行高**：
- 展示/标题：1.2 至 1.3（紧凑以增冲击）
- 正文：1.5 至 1.6（宽松以保可读）
- 紧凑 UI 元素：1.4

### 圆角与边框

Material You 使用**有机、慷慨圆角**创造友好美学。

**圆角值**：
- **Extra Small**：`8px` — 最小 UI 元素、芯片
- **Small**：`12px` — 小卡片、紧凑元素
- **Medium**：`16px` — 默认卡片圆角
- **Large**：`24px` — 突出卡片、容器
- **Extra Large**：`28px` — 对话框、底部表、大表面
- **Extra Extra Large**：`32px` 至 `48px` — Hero 区块、主要容器
- **Full (Pills)**：`9999px` 或 `rounded-full` — 所有按钮、芯片、徽章、FAB

**何时使用**：
- 按钮、芯片、徽章：始终 `full`（胶囊形）
- 标准卡片：`24px`（Large）
- 特性卡片、FAQ 项：`24px`（Large）
- Hero 容器、主要区块：`48px`（Extra Extra Large）
- 嵌套内容卡片：`32px`
- 输入框：上角 `12px`，下角 `0px`（Material 3 填充文本字段样式）

**边框**：
- 克制使用——优先色调表面而非边框
- 需要时用 `#79747E`（Outline）色
- 厚度：标准 1px，聚焦状态 2px（输入框底边框）
- 彩色背景上用 `white/10` 或 `white/20` 作含蓄边框

### 阴影与效果

Material You 通过含蓄阴影结合色调表面使用**抬升**，非戏剧性投影。此实现以渐进阴影过渡增强基线。

**阴影哲学**：
- **抬升 0**（默认）：无阴影或 `shadow-sm` — 用色调表面差异作深度
- **抬升 1**：`shadow-sm` — 卡片静止时的含蓄抬升（大多数卡片默认状态）
- **抬升 2**：`shadow-md` — 交互卡片悬停状态，重要容器默认
- **抬升 3**：`shadow-lg` 至 `shadow-xl` — FAB、主要区块、悬停时抬起按钮
- **抬升 4+**：保留给模态、对话框（基础设计中不常见）

**增强阴影模式**：
- 所有交互卡片悬停时从 `shadow-sm` 过渡至 `shadow-md`
- 重要区块（Benefits、Final CTA）起始 `shadow-lg`
- 结合缩放变换（`hover:scale-[1.02]`）以增深度
- 阴影过渡用 300ms 时长以平滑自信运动

**阴影组合**：
- 柔和弥散阴影（大模糊、最小扩散）
- 阴影色应为近黑低不透明度（5-15%）
- 结合色调表面色以获最佳效果
- 用背景模糊形状分层阴影以增氛围丰富

**模糊效果**（签名技巧）：
- 大型有机形状：`blur-3xl`（64px+）
- 背景装饰元素：10-30% 不透明度彩色圆/形状配重度模糊
- 氛围效果：多个重叠模糊形状配径向渐变
- 玻璃拟态卡片：`backdrop-blur-sm` 配 `bg-white/10` 至 `bg-white/15` 与 `border-white/10` 至 `border-white/20` 边框
- Hero 区块：多个模糊形状用 transform 定位于画布外

**辉光/光环效果**：
- 用配透明度的径向渐变作环境光
- 颜色：Primary、Secondary 或 Tertiary 10-30% 不透明度
- 位置：Hero 内容后方、主要区块（Benefits、Final CTA）或悬停状态
- 动画辉光：`opacity-0 group-hover:opacity-30` 作渐进显现
- 示例：How It Works 区编号徽章有悬停显现的隐藏模糊

### 纹理与图案

**有机装饰形状**：
- 大型圆角矩形（`rounded-[100px]`）配一角较不圆（`rounded-tr-[20px]`）
- 正圆（`rounded-full`）
- 用 `mix-blend-multiply` 分层以增色彩丰富
- 用 primary、secondary 与 tertiary 色 80-90% 不透明度
- 应用 `blur-3xl` 以柔和氛围质感
- 部分定位于画布外（用负 translate 值）

**背景处理**：
- 绝不用纯白——始终用 Surface 色（#FFFBFE）
- 径向渐变作含蓄色彩渲染：`bg-[radial-gradient(circle_at_top_right,_var(--color-md-secondary)_0%,_transparent_40%)]`
- 不透明度：背景图案 10-20%

**分层策略**：
1. 基础表面（着色近白）
2. 装饰有机形状（模糊、multiply 混合）
3. Surface Container（内容背景）
4. 内容
5. 配状态层的交互元素

## 组件样式原则

### 按钮

Material You 按钮是**胶囊形**并使用状态层系统。

**变体**：
1. **Filled (Primary)**：
   - 背景：Primary 色
   - 文字：白
   - 形状：`rounded-full`（胶囊）
   - 阴影：静止无，悬停 `shadow-md`
   - 状态层：悬停 `bg-md-primary/90`，激活 `/80`
   - 缩放：`active:scale-95` 作触感反馈

2. **Tonal (Secondary)**：
   - 背景：Secondary Container 色
   - 文字：On Secondary Container 色
   - 形状：`rounded-full`
   - 状态层：类似 Filled
   - 用于较不突出的操作

3. **Outlined**：
   - 背景：透明
   - 边框：1px Outline 色
   - 文字：Primary 色
   - 形状：`rounded-full`
   - 状态层：悬停 `bg-md-primary/5`

4. **Text/Ghost**：
   - 背景：透明
   - 文字：Primary 色
   - 状态层：悬停 `bg-md-primary/10`
   - 形状：`rounded-full`

5. **FAB（浮动操作按钮）**：
   - 背景：Tertiary 色
   - 文字：白
   - 形状：方形 FAB 用 `rounded-2xl`（28px），圆形用 `rounded-full`
   - 阴影：静止 `shadow-md`，悬停 `shadow-xl`
   - 尺寸：56x56px（h-14 w-14）

**动画**：
- 过渡：300ms 时长
- 缓动：`cubic-bezier(0.2, 0, 0, 1)` — Material You 签名缓动
- 激活缩放：`scale-95` 作按压反馈
- 阴影应以同时机平滑动画

**尺寸**：
- 小：`h-9`（36px）
- 默认：`h-10`（40px）
- 大：`h-12`（48px）
- 水平内边距：慷慨（`px-6` 至 `px-8`）

### 卡片/容器

**视觉处理**：
- 背景：Surface Container（`#F3EDF7`），绝非纯白
- 圆角：标准卡片 `24px`（Large）
- 边框：默认无——用色调背景作分隔
- 阴影：静止 `shadow-sm`，悬停 `shadow-md`
- 内边距：慷慨（`p-6` 至 `p-8`）

**状态过渡**：
- 悬停：`hover:bg-md-surface-variant/20` 或 `hover:shadow-md`，结合变换
- 时长：300ms 配标准缓动（`transition-all duration-300`）
- 缩放：特性卡片与交互元素 `hover:scale-[1.02]`
- 阴影抬升：所有交互卡片悬停时 `shadow-sm` 至 `shadow-md`
- Group 模式：用 `group` 类与 `group-hover:` 修饰符作协调动画

**嵌套卡片**：
- 用更浅背景或透明配边框
- 示例：彩色容器上用 `bg-white/10` 配 `border-white/10`

**特殊容器**：
- Hero 区块：超大圆角（`rounded-[48px]`），surface container 背景
- 区块背景：色调填充配装饰模糊形状
- 玻璃拟态效果：`bg-white/10 backdrop-blur-sm border border-white/10`

### 输入框（Material 3 填充文本字段）

**独特样式**：
- 上角圆（`rounded-t-lg` / 12px）
- 下角方
- 底边框：2px solid Outline 色
- 背景：Muted（Surface Container Low）色
- 高度：高（`h-14` / 56px）
- 聚焦状态：底边框变 Primary 色

**结构**：
```
┌─────────────┐  ← 圆角顶
│   Input     │  ← Muted 背景填充
└─────────────┘  ← 方角底配 2px 边框
      ↑
  聚焦：Primary 色
```

**状态处理**：
- 静止：`border-md-border`（底）
- 聚焦：`border-md-primary`（底）
- 过渡：200ms 色彩过渡
- 标签：占位符用 `text-md-on-background/50`

### 交互状态

**状态层系统**（关键 Material You 概念）：
不改变基色，叠加半透明层：

1. **实色元素**（有 bg 的按钮）：
   - 悬停：基色 90%（`bg-md-primary/90`）
   - 激活：基色 80%（`bg-md-primary/80`）

2. **透明元素**（幽灵按钮、文字按钮）：
   - 悬停：Primary 10%（`bg-md-primary/10`）
   - 激活：Primary 5%（`bg-md-primary/5`）

3. **聚焦状态**：
   - 环：2px Primary 色配 2px offset
   - 额外：可与悬停状态结合

4. **禁用状态**：
   - 不透明度：整个元素 50%
   - 光标：`cursor-not-allowed`
   - 指针事件：无

**过渡时机**：
- 标准：`transition-all duration-300 ease-[cubic-bezier(0.2,0,0,1)]`
- 快速交互（点击）：`duration-200`
- 仅色彩过渡：`transition-colors duration-200`

## 布局原则

**网格使用**：
- 卡片布局用 CSS Grid：`grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3`
- 间隙：一致间距，通常 `gap-6`（24px）或 `gap-8`（32px）
- 容器：用 `.container` 配 `mx-auto` 作居中最大宽度布局

**间距节奏**：
- 基础单位：4px（Tailwind 默认）
- 组件内部内边距：`p-6`（24px）至 `p-8`（32px）
- 区块内边距：`py-12`（48px）至 `py-24`（96px）
- 区块间：`mb-12` 或 `mb-24`
- 鼓励慷慨留白——勿塞内容

**区块流**：
- 色调背景与默认背景交替
- Hero 在大圆角容器配 surface-container 背景
- 部分区块在默认背景，其他在 surface-container
- 克制用全宽彩色容器（primary/tertiary）作强调

**响应式行为**：
- 移动端圆角缩小（48px → 24px）
- 内边距按比例缩减
- 网格优雅折叠为单列
- 文字尺寸移动端降一级

## "大胆要素"（非通用性）

这些签名元素必须存在以实现真实 Material You 美学配增强视觉丰富：

1. **有机模糊形状配分层**：
   - 大型圆形或胶囊形 div 配重度模糊（`blur-3xl`）
   - 用 primary、secondary、tertiary 色 10-30% 不透明度
   - 在主要区块（Hero、Benefits、Final CTA）分层多个形状
   - 结合径向渐变以增氛围深度
   - 用 transform 部分定位于画布外（`-translate-x-1/4`、`translate-y-1/3`）
   - 创造感觉鲜活的大气动态背景

2. **色调表面系统配阴影渐进**：
   - 绝不用纯白背景
   - 分层表面：Background → Surface Container → Surface Container Low
   - 色彩差异含蓄但无需重阴影即创深度
   - 所有卡片默认用 surface-container 色
   - 渐进阴影：静止 `shadow-sm`，悬停 `shadow-md`，重要区块 `shadow-lg`

3. **胶囊形按钮配激活反馈**：
   - 所有按钮必须 `rounded-full`（FAB 用 rounded-2xl 除外）
   - 无矩形或轻圆角按钮
   - 激活状态：`active:scale-95` 作触感按压反馈
   - 这是 Material You 最即时可辨的特征

4. **大型有机圆角**：
   - Hero 区块与主要容器用 32px 至 48px 圆角
   - 常规卡片用 24px 圆角
   - 这不只是"圆角"——它是建筑性的，塑造整个布局
   - 创造友好亲和感，对比 MD2 的僵硬矩形

5. **状态层交互模型配微动画**：
   - 悬停/按下状态用不透明度叠加，非色彩偏移
   - 表现为 `bg-color/90` 或 `bg-color/10` 模式
   - 平滑 cubic-bezier 缓动：`cubic-bezier(0.2, 0, 0, 1)`
   - 以缩放变换、阴影抬升与辉光效果增强
   - Group 交互：用 `group` 与 `group-hover:` 作协调动画

6. **非对称抬升**（增强）：
   - 精选定价档位：`md:-translate-y-4` 以抬升于同级之上
   - 通过垂直定位创造视觉层级
   - 结合 ring 高亮（`ring-2 ring-md-primary`）以强调

7. **丰富微交互**（增强）：
   - 博客卡片：悬停图片缩放（`group-hover:scale-105`）
   - 特性卡片：悬停整卡缩放（`hover:scale-[1.02]`）
   - How It Works 徽章：悬停显现辉光效果
   - 定价特性：悬停列表项 translate-x
   - 每个交互元素都有平滑令人满足的反馈

## 反模式（应避免之事）

**不该做**：
- 用纯白（#FFFFFF）作背景——破坏色调系统
- 用矩形或略圆角按钮——必须胶囊形
- 用重投影——MD3 偏好配色调表面的含蓄抬升
- 悬停改按钮色——用状态层（不透明度叠加）替代
- 主要容器用锐角——慷慨圆角是关键
- 忽略有机模糊形状——它们是风格签名
- 用纯黑文字——用 On Surface 色（#1C1B1F）配暖意
- 扁平化输入框——用独特的填充文本字段样式配底边框
- 创造刺眼几何图案——形状应有机、柔软、流动
- 依赖边框作容器分隔——改用色调背景

**常见错误**：
- 圆角过小（卡片最小 16px，24px+ 更好）
- 忘记输入框圆顶角方底角
- 用悬停色变化而非状态层
- 色调表面更有效时过度用阴影
- 背景中分层有机形状不足
- 调色板过柔和——MD3 是表现力强且多彩的
- 缺失微交互——每个交互元素应有平滑反馈
- 忘记 `group` 模式作协调悬停效果
- 可点击元素不用 `active:scale-95` 作触感反馈
- 静态卡片无悬停状态——破坏交互响应感

## 动画与运动

**缓动函数**：
- 标准：`cubic-bezier(0.2, 0, 0, 1)` — Material You 签名缓动
- 这创造平滑自信的运动，既不机械也不弹跳
- Material 规范中也称"Emphasized Decelerate"

**时长**：
- 微交互（按钮悬停）：200ms
- 标准过渡（卡片、表面）：300ms
- 大表面（模态、底部表）：400-500ms
- UI 过渡绝不超过 500ms

**变换模式**：
- 按压缩放：`active:scale-95` 作触感反馈
- 悬停抬升：可用含蓄 `translate-y`（1-2px）结合阴影增加
- 入场动画：淡入 + 轻微缩放或滑动
- 退场动画：比入场快（200ms vs 300ms）

**什么动画**：
- 背景色（状态层）
- 阴影抬升
- 缩放（按压时）
- 不透明度（叠加、toast）
- 变换（FAB、特殊交互）

**什么不动画**：
- 圆角（保持恒定）
- 布局位移（用固定尺寸或平滑高度过渡）
- 色相偏移（状态层仅不透明度变化）

## 可访问性考量

**对比要求**：
- Surface 背景上文字：最低 4.5:1（On Surface 色：#1C1B1F）
- Primary 上文字：AAA 级（纯白 #FFFFFF）
- 边框用 Outline 色：对表面 3:1
- 确保色调表面差异可见（非仅装饰）

**聚焦状态**：
- 所有交互元素必须有可见聚焦环
- 用 `focus-visible:ring-2 focus-visible:ring-md-primary focus-visible:ring-offset-2`
- 环色：Primary
- 环 offset：2px 以与元素分隔

**触控目标**：
- 最小：44x44px（遵循 WCAG 指南）
- 默认按钮高度：40-48px（达最小）
- FAB：56x56px（慷慨触控目标）
- 小交互元素周围按需加内边距

**运动偏好**：
- 尊重 `prefers-reduced-motion` 服务前庭障碍用户
- 减少或移除缩放变换、位移动画
- 保留色彩过渡但移除运动
- 示例：`@media (prefers-reduced-motion: reduce) { * { animation: none; transition-duration: 0.01ms; } }`

**屏幕阅读器考量**：
- 装饰有机形状应设 `aria-hidden="true"`
- 确保色彩非状态唯一指示器
- 纯图标按钮必须有可访问标签
- 表单输入需关联标签（可见或 aria-label）

---

## 实现清单

为确保完整 Material You 合规配增强深度与交互性：

**核心 Material You 元素**：
- [ ] 用 Roboto 字体（400、500、700 字重）
- [ ] 所有按钮 `rounded-full`（胶囊形）
- [ ] 背景 #FFFBFE（非纯白）
- [ ] 卡片用 Surface Container（#F3EDF7）背景
- [ ] Hero/关键区块有有机模糊形状
- [ ] 悬停/激活状态用状态层（不透明度叠加）
- [ ] 过渡用 cubic-bezier(0.2, 0, 0, 1) 缓动
- [ ] 主要容器大圆角（32-48px）
- [ ] 输入框用填充文本字段样式（圆顶、方底边框）
- [ ] 所有交互元素有聚焦环
- [ ] 全程慷慨间距与内边距

**增强实现**：
- [ ] 渐进阴影系统：悬停 `shadow-sm` → `shadow-md`
- [ ] 主要区块多个模糊形状配径向渐变
- [ ] 所有可点击元素 `active:scale-95` 作触感反馈
- [ ] `group` 模式配协调悬停动画
- [ ] 特性卡片悬停缩放（`hover:scale-[1.02]`）
- [ ] 博客卡片悬停图片缩放（`group-hover:scale-105`）
- [ ] 精选定价档位非对称抬升（`md:-translate-y-4`）
- [ ] 悬停显现辉光效果（How It Works 徽章）
- [ ] Benefits 区玻璃拟态卡片配 backdrop-blur
- [ ] Product Detail 可视化容器 shadow-inner
- [ ] 头部配 border-bottom 与 backdrop-blur
- [ ] 所有过渡最低 300ms 时长
- [ ] FAQ 项悬停状态配色彩过渡
- [ ] 输入框聚焦状态含环以增强可见性

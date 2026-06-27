# Clay

> 来源：[Design Prompts](https://www.designprompts.dev/claymorphism)

## 基本信息

| 属性 | 值 |
|------|-----|
| 风格ID | `claymorphism` |
| 显示名称 | Clay |
| 模式 | ☀️ 浅色模式 (Light) |
| 字体类型 | sans-serif |
| 描述 | 超写实 3D 美学，模拟柔软可充气的黏土物件，多层阴影堆叠、糖果店般鲜艳色彩、触觉微交互与有机漂浮的环境元素，营造高级而趣味的数字玩具体验。 |

## 布局创意 (Layout Ideas)

### Hero

居中内容，配渐进缩放的巨型字体（text-5xl 至 text-8xl）。背景含大型缓慢漂移的彩色光斑配 blur-3xl。3D 形状以 clay-float-slow 动画环绕标题。信任徽章配动画脉动指示器。标题点缀色用多色停靠点的渐变文字。

### Stats

呼吸球体网格（clay-orb + clay-breathe），aspect-square 比例。数字用 Nunito Black 大字号。错峰动画延迟创造有机节奏。悬停缩放变换提供触感反馈。

### Features

Bento 瀑布流网格，配 col-span-2/row-span-2 的 hero 卡片。变化的背景不透明度创造深度层级。内部装饰面板绝对定位于卡片底部，配 translate-y 悬停显现。图标容器用鲜艳渐变背景配 rounded-2xl 形状。

### How It Works

三列网格配居中内容。连接的水平"管道"元素（rounded-full bg 配 shadow-inner）。每步用大号渐变圆（响应式 h-28 至 h-32）配粗体 Nunito 数字。Group-hover 缩放交互。

### Benefits

50/50 分割布局。左：抽象黏土构图，含嵌套圆角形状、分层背景（aspect-square 容器）。右：堆叠收益卡片（rounded-[24px]），配渐变勾选图标，悬停上浮与增强阴影。

### Pricing

三列网格。中间"热门"卡片仅桌面端缩放至 110%（md:scale-110）配增强阴影。所有卡片用一致的 rounded-[32px] 圆角配响应式内边距。绿色调粗体勾选图标。

### Testimonials

2-3 列响应式网格。卡片用白色背景配 shadow-clayCard。头像包裹于白色黏土环（shadow-clayButton）中。琥珀色五星评分。Group hover 上浮卡片配增强阴影。

### Faq

使用原生 details/summary 元素的手风琴。卡片 rounded-[24px] 圆角配 shadow-clayCard。打开状态显示凹陷内嵌阴影。Summary 含动画 rotate-180 chevron 指示器。

### Blog

拍立得风格卡片，外层 rounded-[32px]，图片容器 rounded-[24px]。厚内边距营造照片边框效果。图片在 group-hover 时缩放。元信息用小型大写字母配黏土胶囊徽章。

### Footer

玻璃拟态基底（bg-white/40 + backdrop-blur-lg）。社交图标为黏土按钮（rounded-xl 配 shadow-clayButton）。悬停上浮配阴影增强。网格布局，公司信息跨 2 列。

---

## 完整提示词 (Full Prompt)

# 高保真 Claymorphism 设计系统

## 设计哲学

**核心概念：数字黏土**
此设计系统不只是"柔软 UI"——它是对由**高级数字黏土**构成的有形物理世界的高保真模拟。屏幕上的每个元素都应唤起手握高端哑光乙烯基玩具或柔软充气硅胶物件的感受。它拒绝现代极简主义的扁平，转而追求体积、重量与触感。

**"高保真"之别**：
不同于 2020 年代早期的"Neumorphism"（感觉像挤出塑料）或基础"Claymorphism"（常感觉像扁平矢量艺术），**高保真 Claymorphism** 依赖使用 4 层阴影堆叠的复杂多层光照模拟。它渲染出感觉致密、实在、可交互的对象——而非空洞装饰。

*   **材质性**：想象软触哑光硅胶、棉花糖般泡沫或高级注塑塑料配高级饰面。表面吸收光线而非锐利反射，创造温暖、亲和的美学。
*   **光照**："世界"由位于左上方的柔和弥散顶光照亮，在物体下方创造深邃的环境光遮蔽阴影，在其上脊创造柔和镜面高光。这创造物理深度的错觉。
*   **阴影架构**：每个元素使用精心打磨的多层阴影：
    - **外阴影**：柔和的彩色投影，定义与表面的距离
    - **高光阴影**：左上高光，模拟光反射
    - **内阴影**：含蓄的彩色反射与边缘光，增添维度
    - **激活状态**：按下元素用内嵌阴影模拟物理凹陷

**感官气质**：
*   **俏皮与乐观**：界面通过"糖果店"色彩（鲜艳紫、热粉、天蓝、翡翠绿、琥珀橙）与弹跳有机的运动散发欢乐。它感觉安全、欢迎、不做作——如高端玩具店陈列。
*   **触感与响应**：元素交互时不只变色——它们以夸张的真实感物理反应。按钮主动"挤压"（scale-[0.92] + shadow-clayPressed）并在光标下压缩。卡片抬升并向用户漂浮（-translate-y-2 配增强阴影）。每次交互都提供令人满足的视觉反馈。
*   **友好与安全**：此宇宙中**零锐角**。每个边缘都激进圆角（最小 `rounded-[20px]`，大容器至 `rounded-[60px]`），潜意识地向用户传递安全与亲和。设计语言无需言语即说"友好"与"可访问"。
*   **高级工艺**：尽管俏皮，此美学通过对细节的精心关注保持品质感：一致的圆角、精准的阴影分层、和谐的色彩关系与流畅的微交互。

**"黏土"物理引擎**：
1.  **凸性（隆起）**：主要交互元素（按钮、数据球、特性卡片）以 `shadow-clayButton` 或 `shadow-clayCard` 向用户凸出。它们在左上边缘捕捉光，在下方投射柔和彩色阴影，创造漂浮于表面之上的错觉。
2.  **凹性（按压）**：次级表面（输入框、激活按钮状态、打开时的 FAQ 面板）以 `shadow-clayPressed` 压入黏土表面。它们在顶边投射内部阴影并在底唇捕捉光，使其感觉凹陷。
3.  **浮力（漂浮）**：界面存在于零重力、高空气阻力环境中。背景光斑缓慢漂移（8-12s 动画配 translateY 与 rotate）。卡片毫不费力地悬停，悬停状态放大漂浮效果。无物感觉静态"粘"在网格上——一切呼吸并微妙移动。
4.  **微物理**：悬停状态一致地将元素向上抬升（`hover:-translate-y-1` 至 `-translate-y-2`）同时增强其阴影，模拟元素向观察者漂浮。激活/按下状态则相反——向下压缩配减少的阴影。

---

## 设计 Token 系统

### 色彩（"糖果店"调色板）

**Background**：
*   **画布**：`#F4F1FA`（极浅冷薰衣草白）。这比暖米色提供更干净、现代的基底。切勿用纯白——轻微色调创造温暖。

**Foreground**：
*   **文字（主要）**：`#332F3A`（柔和炭灰）。高对比（达 WCAG AA）但比黑更柔和以增亲和感。
*   **柔和（次要）**：`#635F69`（深薰衣草灰）。对浅背景可读性至关重要。用于正文、标签与次要信息。切勿浅于此值。

**点缀（鲜艳饱和）**：
*   **主要点缀**：`#7C3AED`（鲜艳紫）。用于主要 CTA、链接与品牌强调的英雄色。
*   **次要点缀**：`#DB2777`（热粉）。用于渐变与次级强调。
*   **三级**：`#0EA5E9`（天蓝）。用于信息元素与背景光斑。
*   **成功/收益**：`#10B981`（翡翠绿）。用于勾选与正面指示。
*   **警告**：`#F59E0B`（琥珀）。用于提醒与星级评分。

**渐变策略**：
*   **主按钮**：`bg-gradient-to-br from-[#A78BFA] to-[#7C3AED]`（浅紫至主紫）。这创造深度并防止过深按钮。
*   **图标光球**：`bg-gradient-to-br` 自浅粉彩（400）至饱和色调（600），变化色彩以增视觉趣味（如 `from-blue-400 to-blue-600`、`from-purple-400 to-purple-600`、`from-pink-400 to-pink-600`）。
*   **文字高亮**：Hero 文字用多停靠点渐变（`clay-text-gradient`）：`from-clay-foreground 20%, to-clay-accent 60%, to-clay-accent-alt`。渐变文字保持大号（text-5xl+）以保可读性。
*   **背景光斑**：半透明点缀色，10% 不透明度配 blur-3xl 以柔和环境光。

### 字体

**字体选择**：
*   **标题**：**Nunito**（Google Fonts，字重：700/800/900）。圆润终端完美补充柔软黏土美学。通过内联样式应用于所有标题、数字与强调文字：`style={{ fontFamily: "Nunito, sans-serif" }}`。
*   **正文**：**DM Sans**（Google Fonts，字重：400/500/700）。几何、干净、高可读。通过 body font-family 全局应用。

**层级（移动优先配渐进增强）**：
*   **Hero 标题**：`text-5xl sm:text-6xl md:text-7xl lg:text-8xl`，Black 字重（font-black），紧凑字距（tracking-tight），行高 1.1。始终用 Nunito。
*   **区块标题**：`text-3xl sm:text-4xl md:text-5xl`，Extrabold（font-extrabold）或 Black。始终用 Nunito。
*   **卡片标题**：`text-xl` 至 `text-2xl`（hero 卡片更大：`text-3xl`），Bold（font-bold）至 Extrabold。用 Nunito。
*   **正文**：`text-base` 至 `text-lg`，Medium 字重（font-medium），宽松行高（leading-relaxed）。用 DM Sans。
*   **小文字**：`text-sm` 至 `text-xs`，Medium 至 Bold 字重。用于标签、元信息、大写 tracking-wide 处理。

**字体最佳实践**：
*   始终将 Nunito 标题与 DM Sans 正文配对以获最佳层级。
*   大标题与数字用 `font-black`（900 字重）以最大冲击。
*   确保行高慷慨：正文 `leading-relaxed`（1.625），紧凑展示标题 `leading-[1.1]`。
*   用 max-w-2xl 至 max-w-3xl 容器限制行长 60-75 字符以获最佳可读性。
*   大标题用 `tracking-tight` 保持视觉密度，小型大写/标签用 `tracking-wide` 或 `tracking-widest`。

### 形状与圆角

**"超圆角"规则（仅绝对值）**：
*   **大容器/Hero 区块**：`rounded-[48px]` 至 `rounded-[60px]`
*   **标准卡片**：`rounded-[32px]`（大多数卡片的默认）
*   **中等元素**（收益胶囊、博客卡片）：`rounded-[24px]`
*   **按钮与输入框**：`rounded-[20px]` 或 `rounded-2xl`
*   **图标容器**：方形图标 `rounded-2xl`（16px），圆形用 `rounded-full`
*   **小型徽章**：最小 `rounded-lg`（8px），首选 `rounded-full`
*   **数据球**：`rounded-full`（正圆）

**关键规则**：
*   切勿使用 `rounded-md`（4px）或 `rounded-sm`。它们对此美学显得过锐利与通用。
*   保持一致性：若卡片用 `rounded-[32px]`，其嵌套图片应用 `rounded-[24px]`（少 8px）以创视觉层级。
*   移动端可略减圆角（如 `rounded-[32px] sm:rounded-[40px]`）以最大化屏幕空间同时保持柔软美学。

### 阴影（黏土的引擎）

此系统使用**高保真阴影堆叠**模拟复杂光照。

**1. 深黏土（表面）**：
用于主背景元素或大容器。
```css
box-shadow: 
  30px 30px 60px #cdc6d9,           /* 深而柔和的环境光遮蔽 */
  -30px -30px 60px #ffffff,         /* 左上环境光 */
  inset 10px 10px 20px rgba(139, 92, 246, 0.05), /* 含蓄色彩反射 */
  inset -10px -10px 20px rgba(255, 255, 255, 0.8); /* 表面镜面 */
```

**2. 黏土卡片（漂浮）**：
用于标准内容卡片。
```css
box-shadow: 
  16px 16px 32px rgba(160, 150, 180, 0.2), /* 柔和紫灰投影 */
  -10px -10px 24px rgba(255, 255, 255, 0.9), /* 强左上高光 */
  inset 6px 6px 12px rgba(139, 92, 246, 0.03), /* 内彩色反弹光 */
  inset -6px -6px 12px rgba(255, 255, 255, 1); /* 内边缘光 */
```

**3. 黏土按钮（高凸性）**：
用于可点击元素。
```css
box-shadow: 
  12px 12px 24px rgba(139, 92, 246, 0.3), /* 强彩色投影 */
  -8px -8px 16px rgba(255, 255, 255, 0.4), /* 左上高光 */
  inset 4px 4px 8px rgba(255, 255, 255, 0.4), /* 内边缘 */
  inset -4px -4px 8px rgba(0, 0, 0, 0.1); /* 右下阴影 */
```

**4. 黏土按压（凹陷）**：
用于输入框与激活状态。
```css
box-shadow: 
  inset 10px 10px 20px #d9d4e3, /* 深内阴影左上 */
  inset -10px -10px 20px #ffffff; /* 内高光右下 */
```

---

## 组件架构

### 1. 通用卡片（`Card`）
*   **基础样式**：`relative overflow-hidden rounded-[32px] bg-clay-cardBg p-8 text-clay-foreground shadow-clayCard backdrop-blur-xl`
*   **交互状态**：
    *   默认：`shadow-clayCard`（4 层阴影配柔和深度）
    *   悬停：`hover:-translate-y-2 hover:shadow-[enhanced]`（抬升配更强阴影）
    *   过渡：`transition-all duration-500`（流畅、高级感）
*   **结构**：
    *   外层包裹处理定位、overflow、阴影
    *   **内层内容包裹**：`<div className="relative z-10 flex h-full flex-col">{children}</div>` 以支持绝对定位的装饰元素
*   **装饰**：用绝对定位面板配负边距（`-bottom-8 -left-8 -right-8`）创造自卡片底部探出的"窥视"UI 元素
*   **变体**：
    *   玻璃效果：`bg-white/60` 至 `bg-white/80`
    *   实心：`bg-white`
    *   特性 hero 卡片：`md:col-span-2 md:row-span-2` 配更大内边距

### 2. 黏土按钮（`Button`）
*   **基础形状**：`rounded-[20px]` 配厚实高度（默认 `h-14`，lg 用 `h-16`）
*   **基础样式**：`inline-flex items-center justify-center font-bold tracking-wide transition-all duration-200`
*   **变体**：
    *   **主/默认**：`bg-gradient-to-br from-[#A78BFA] to-[#7C3AED] text-white shadow-clayButton hover:shadow-clayButtonHover`
    *   **次**：`bg-white text-clay-foreground shadow-clayButton`
    *   **描边**：`border-2 border-clay-accent/20 bg-transparent text-clay-accent hover:border-clay-accent hover:bg-clay-accent/5`
    *   **幽灵**：`text-clay-foreground hover:bg-clay-accent/10 hover:text-clay-accent`
*   **交互状态**：
    *   悬停：`hover:-translate-y-1`（上浮 4px）+ 增强阴影
    *   激活：`active:scale-[0.92] active:shadow-clayPressed`（明显挤压效果）
    *   聚焦：`focus-visible:ring-4 focus-visible:ring-clay-accent/30 focus-visible:ring-offset-2`
*   **尺寸**：用 `size` prop：`sm`（h-11）、`default`（h-14）、`lg`（h-16）

### 3. 凹陷输入框（`Input`）
*   **基础形状**：`rounded-2xl` 配慷慨高度 `h-16`
*   **基础样式**：`flex w-full border-0 bg-[#EFEBF5] px-6 py-4 text-clay-foreground text-lg shadow-clayPressed`
*   **状态**：
    *   默认：以 `shadow-clayPressed` 凹陷（内嵌阴影）
    *   聚焦：`focus:bg-white focus:ring-4 focus:ring-clay-accent/20`（转化为抬升白色表面）
    *   占位符：`placeholder:text-clay-muted`
*   **可访问性**：`transition-all duration-200` 以平滑状态变化

### 4. 漂浮 3D 光斑（背景）
**切勿使用扁平背景。** 始终包含 3-4 个大型动画光斑。
*   **容器**：`<div className="pointer-events-none fixed inset-0 overflow-hidden -z-10">`
*   **单个光斑**：
    *   类：`absolute h-[60vh] w-[60vh] rounded-full blur-3xl`
    *   颜色：点缀色配 `/10` 不透明度（如 `bg-[#8B5CF6]/10`、`bg-[#EC4899]/10`、`bg-[#0EA5E9]/10`）
    *   定位：负边距溢出边缘（`-top-[10%] -left-[10%]`、`-right-[10%] top-[20%]`）
    *   动画：`clay-blob` 或 `clay-blob-alt` 配错峰 `animation-delay-2000` 或 `animation-delay-4000`
*   **目的**：创造透过玻璃拟态卡片显现的环境彩色光

---

## 动画系统

**1. 黏土漂浮（`clay-float`）**：
模拟背景光斑的零重力漂移。8 秒时长。
```css
@keyframes clay-float {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  50% { transform: translateY(-20px) rotate(2deg); }
}
```

**2. 黏土漂浮延迟（`clay-float-delayed`）**：
反向旋转的替代动画。10 秒时长。
```css
@keyframes clay-float-delayed {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  50% { transform: translateY(-15px) rotate(-2deg); }
}
```

**3. 黏土漂浮缓慢（`clay-float-slow`）**：
用于环绕标题的 Hero 装饰元素。12 秒时长，更显著运动。
```css
@keyframes clay-float-slow {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  50% { transform: translateY(-30px) rotate(5deg); }
}
```

**4. 黏土呼吸（`clay-breathe`）**：
模拟物体轻微膨胀/收缩。6 秒时长。用于数据球。
```css
@keyframes clay-breathe {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.02); }
}
```

**5. 悬停抬升**：
标准交互元素应在悬停时向上抬升：
*   卡片：`hover:-translate-y-2`（8px）配增强阴影
*   收益胶囊：`hover:-translate-y-1`（4px）
*   证言：`hover:-translate-y-2`（8px）
*   博客文章：`hover:-translate-y-3`（12px）以戏剧效果
*   按钮：`hover:-translate-y-1`（4px）配阴影增强

**6. 激活按压**：
按钮用 `active:scale-[0.92]` 结合 `active:shadow-clayPressed` 模拟点击时的物理挤压。时长应快（200ms）以即时反馈。

**7. 缩放变换**：
*   数据球：`hover:scale-110`（10% 增长）
*   How It Works 圆：`group-hover:scale-110` 配 300ms 时长
*   定价卡片（非高亮）：`hover:scale-105`（5% 含蓄增长）
*   Bento 网格精选卡片：`hover:scale-[1.02]`（因大尺寸而极小增长）

**8. 动画延迟**：
使用错峰动画以增视觉节奏：
*   `.animation-delay-2000`（2s 延迟）
*   `.animation-delay-4000`（4s 延迟）

**9. 减少运动**：
始终包含 `@media (prefers-reduced-motion: reduce)` 以禁用所有动画保证可访问性。

---

## 布局模式

**1. 瀑布流 / Bento 网格**：
*   勿用统一网格。混合 `col-span-1` 与 `col-span-2` 或 `row-span-2` 卡片。
*   大网格项用 `hover:scale-[1.02]` 增触感。

**2. 分割布局**：
*   "Product" 或 "Benefits" 区用 50/50 分割。
*   一侧文字，一侧**抽象 3D 构图**（嵌套黏土形状，不只是图片）。

**3. 重叠元素**：
*   允许元素突破容器（如"热门"徽章漂浮于定价卡片*之上*）。
*   用负边距将装饰元素拉至边缘。

---

## 响应式策略

**移动优先方法配渐进增强**

Clay 设计系统在所有屏幕尺寸上保持其俏皮、触感的个性，同时适配布局与尺寸以获最佳移动体验。

**字体缩放**：
*   Hero 标题：`text-5xl → sm:text-6xl → md:text-7xl → lg:text-8xl`
*   区块标题：`text-3xl → sm:text-4xl → md:text-5xl`
*   正文：`text-base → sm:text-lg → md:text-xl` 视情况
*   始终保持 `leading-relaxed` 与适当行长约束

**布局变换**：
*   **导航**：移动端紧凑（`h-16 rounded-[32px] px-4`）→ 桌面端更大（`sm:h-20 sm:rounded-[40px] sm:px-8`）。移动端隐藏非必要导航项。
*   **Hero**：CTA 垂直堆叠（`flex-col gap-6`）→ 桌面端水平（`sm:flex-row`）
*   **数据**：移动端 2 列网格（`grid-cols-2 gap-6`）→ 桌面端 4 列（`md:grid-cols-4 gap-8`）
*   **特性**：单列 → 桌面端带 span 的 Bento 布局（`md:grid-cols-2 lg:grid-cols-3` 配 hero 卡片 `md:col-span-2 md:row-span-2`）
*   **收益/Product Detail**：移动端垂直堆叠 → 桌面端并排分割（`lg:grid-cols-2`）
*   **定价**：移动端堆叠卡片 → 桌面端 3 列（`md:grid-cols-3`）。高亮卡片缩放效果仅桌面端（`md:scale-110`）

**组件调整**：
*   **卡片**：移动端减少内边距（`p-6 sm:p-8`）
*   **圆角**：移动端仍保持慷慨圆角（绝不少于 `rounded-[20px]`）
*   **按钮**：移动端主 CTA 全宽（`w-full sm:w-auto`）
*   **装饰元素**：移动端隐藏部分漂浮形状（`hidden lg:block`）
*   **阴影**：保持完整阴影堆叠——它们对美学至关重要

**触控目标**：
*   所有交互元素满足 44px 最小触控目标（按钮 `h-14+`）
*   增加移动导航间距以便点击
*   确保手风琴 FAQ 项有充足垂直间距

**性能**：
*   动画仍在移动端运行但尊重 `prefers-reduced-motion`
*   模糊效果（`backdrop-blur-xl`）保留——它们对玻璃黏土美学至关重要
*   背景光斑用视口单位（`vh`）缩放以自然适配

**移动端勿改**：
*   勿扁平化设计——保持阴影与深度
*   勿将圆角减至通用值
*   勿移除糖果店色彩或使其柔和
*   勿禁用所有动画（仅在性能问题时简化）

---

## 该做与不该做

*   **该做** 点击时使用明显"挤压"动画（`active:scale-[0.92]` 结合 `shadow-clayPressed`）。
*   **该做** 组件内使用变化圆角（如外容器 `rounded-[48px]`、卡片 `rounded-[32px]`、内图片 `rounded-[24px]`）。
*   **该做** 使用"玻璃黏土"混合（半透明白 `bg-white/60` 至 `/80` + `backdrop-blur-xl`）让卡片透出背景光斑。
*   **该做** 使用多层阴影堆叠（最少 4 层阴影）实现高保真深度。
*   **该做** 通过内联样式显式将 Nunito 字体应用于所有标题、数字与标签。
*   **该做** 为图标容器使用鲜艳渐变背景，变化色彩（蓝、紫、粉、绿、青、琥珀）。
*   **不该做** 使用浅于 `#635F69` 的灰文字。这是浅背景可访问性的最低值。
*   **不该做** 任何地方使用锐角。最小圆角为 `rounded-[20px]`，绝不用 `rounded-md` 或 `rounded-lg`。
*   **不该做** 背景使用扁平色。始终包含动画光斑或含蓄渐变。
*   **不该做** 小于 `text-5xl` 的字号使用渐变文字（可读性风险）。
*   **不该做** 按钮过小。最小高度 `h-11`（44px）以保可访问性。
*   **不该做** 跳过交互元素的悬停抬升效果——它是触感的核心。

---

## 实现清单
- [ ] **背景**：画布 `#F4F1FA` + 动画光斑。
- [ ] **阴影**：CSS 中定义 4 层 box-shadow。
- [ ] **字体**：Nunito Black（标题）+ DM Sans（正文）。
- [ ] **按钮**：渐变、rounded-2xl、点击挤压。
- [ ] **卡片**：White/60%、backdrop-blur、rounded-3xl。
- [ ] **文字**：高对比炭灰/石板灰，无浅灰。

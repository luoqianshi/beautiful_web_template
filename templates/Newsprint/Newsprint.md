# Newsprint

> 来源：[Design Prompts](https://www.designprompts.dev/newsprint)

## 基本信息

| 属性 | 值 |
|------|-----|
| 风格ID | `newsprint` |
| 显示名称 | Newsprint |
| 模式 | ☀️ 浅色模式 (Light) |
| 字体类型 | serif |
| 描述 | 纯黑白、高对比、紧凑网格、报纸美学、锐利线条、编辑深度。 |

## 布局创意 (Layout Ideas)

### Hero

8 列/4 列分割网格。主列含巨型标题（5xl → 9xl）、首字下沉引言段与 CTA 按钮。侧列含数据框与带边框广告占位符。

### Stats

全宽黑背景滚动条配横向跑马灯。等宽标签、粗体值、红色点缀徽章。

### Features

4 列顶部网格配带边框盒中图标，3 列底部网格配项目符号。所有单元格由黑边框分隔（折叠网格风格）。

### Blog

3 列网格配带边框卡片风格。灰度图片配 sepia 悬停，等宽字体日期/作者元信息，悬停下划线。

### How It Works

深色反相区块（黑底白字）。3 列网格配编号红框，横向连接线，垂直布局分解。

### Benefits

编辑 5 列/7 列分割。左侧插图占位符，右侧 2 列文字布局中的编号列表。

### Testimonials

2 列网格配大号引号、衬线引文、带边框作者卡片配灰度图片。

### Pricing

3 列表格网格配明确边框。高亮档位有独特背景、巨型衬线定价、特性勾选标记。

### Faq

4 列/8 列分割。侧边栏有帮助中心框。主区有手风琴配 plus/minus 图标旋转、可展开回答。

### Footer

多列站点地图配严格边框、公司描述、带边框盒中社交图标、版本/版权信息。

---

## 完整提示词 (Full Prompt)

# 设计风格：Newsprint

## 1. 设计哲学

**"All the News That's Fit to Print."**

此风格是对印刷新闻黄金时代的颂歌，为网页重新想象。它通过对高对比字体、基于网格的布局与锐利几何精准的不妥协承诺，体现**绝对的清晰、层级与结构**。

### 核心 DNA
新闻纸美学拒绝柔和阴影、模糊背景与圆角等现代网页趋势。相反，它拥抱：

- **鲜明几何**：零 border-radius。每个元素是完美矩形配锐利 90 度角。
- **高信息密度**：紧凑内边距、折叠网格边框与高效用空间模仿报纸列布局。
- **字体戏剧**：巨型衬线标题（桌面至 9xl）配较小、高可读正文创造极端层级。
- **可见结构**：网格线不被隐藏——它们被赞颂。列与区块间边框明确且突出。
- **编辑权威**：设计感觉严肃、永恒、可信赖——如权威出版物。
- **纸张纹理**：含蓄颗粒叠加与线图案模拟新闻纸触感而不过度拟物。

### 气质
权威、智识、紧迫、永恒。感觉如手持新鲜晨报——利落、有序、信息丰富。设计散发自信与可信。

## 2. 设计 Token 系统（DNA）

### 色彩（单一调色板）
**模式**：浅色（永久 — 无深色模式）

- **Background**：`#F9F9F7`（新闻纸近白）
  模仿陈年纸的暖近白。非纯白——增添含蓄暖意并减眼疲劳。

- **Foreground**：`#111111`（墨黑）
  极深黑，非纯 `#000`。用于所有文字与边框。

- **Muted**：`#E5E5E0`（分隔符灰）
  浅灰作次级边框与含蓄背景。

- **Accent**：`#CC0000`（编辑红）
  明亮、毫不妥协的红，极克制使用——仅用于突发新闻徽章、CTA 与悬停状态。99% 设计为黑白。

- **Border**：`#111111`（墨黑）
  主要结构元素。边框定义网格并创造视觉节奏。

- **中性色阶**：
  `neutral-100`：`#F5F5F5`（悬停背景）
  `neutral-200`：`#E5E5E5`（图片占位符）
  `neutral-400`：`#A3A3A3`（深色区块中柔和文字）
  `neutral-500`：`#737373`（元信息、说明）
  `neutral-600`：`#525252`（正文变化）
  `neutral-700`：`#404040`（次级标题）

### 字体

**字体栈**：
- **衬线（标题与展示）**：`'Playfair Display', 'Times New Roman', serif`
  高对比、优雅、权威。用于所有主要标题。

- **衬线（正文）**：`'Lora', Georgia, serif`
  高可读衬线作长篇阅读文字与段落。

- **无衬线（UI）**：`'Inter', 'Helvetica Neue', sans-serif`
  干净、现代无衬线作标签、按钮、导航与元信息。

- **等宽（数据）**：`'JetBrains Mono', 'Courier New', monospace`
  用于数据、日期、版本号与技术信息。

**字号策略**：
- **H1（Hero 标题）**：`text-5xl sm:text-6xl lg:text-9xl`（80px → 128px）
  巨型、主导视口。用 `leading-[0.9]` 作超紧行高。应用 `tracking-tighter` 以增紧凑感。

- **H2（区块标题）**：`text-4xl lg:text-5xl`（36px → 48px）
  粗、`font-black`、视上下文大写或句式。

- **H3（卡片标题）**：`text-2xl lg:text-3xl`（24px → 30px）
  `font-bold`、衬线。

- **正文**：`text-sm` 至 `text-lg`（14px → 18px）
  正文字体（Lora）、`leading-relaxed`（行高 1.625）。

- **元信息/标签**：`text-xs`（12px）
  大写、`tracking-widest`、等宽或无衬线。

**文字变换**：
- 大写用于：导航、标签、元信息、徽章、作者署名小型大写。
- 句式用于：标题、文章标题、正文。

### 圆角与边框

**圆角**：处处 `0px`。无例外。
用内联样式或 `.sharp-corners` 工具类强制所有组件零圆角。

**边框宽度**：
- 标准：`1px` solid black（`border`、`border-r`、`border-b`）
- 重强调：`border-b-4` 或 `border-4`（4px solid）作主要区块分隔符
- 折叠网格：相邻元素共享边框以避免双线

**边框样式**：
始终 solid。绝不虚线或点线，除罕见装饰元素（如定价卡片内 `border-dashed` 作特性分隔符）。

### 阴影/效果

**哲学**：扁平设计。无柔和投影。

**悬停效果**：
- **硬偏移阴影**：`box-shadow: 4px 4px 0px 0px #111111`
  悬停时应用于博客卡片或交互元素。创造"抬起"的报纸剪纸效果。

- **实现**：
  ```css
  .hard-shadow-hover:hover {
    box-shadow: 4px 4px 0px 0px #111111;
    transform: translate(-2px, -2px);
  }
  ```

**无效果**：
- 无模糊
- 无内阴影（罕见装饰目的除外）
- 无渐变叠加

### 纹理与图案

**对深度至关重要**：新闻纸风格通过分层纹理避免"扁平通用网页设计"。

**1. 点阵网格图案（主背景）**：
```html
backgroundImage: `url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='4' height='4' viewBox='0 0 4 4'%3E%3Cpath fill='%23111111' fill-opacity='0.04' d='M1 3h1v1H1V3zm2-2h1v1H3V1z'%3E%3C/path%3E%3C/svg%3E")`
```
含蓄 4×4px 点图案应用于 body 背景。

**2. 线网格叠加（区块纹理）**：
```css
.newsprint-texture {
  position: relative;
}
.newsprint-texture::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(0deg, transparent 98%, rgba(0,0,0,0.02) 100%),
    linear-gradient(90deg, transparent 98%, rgba(0,0,0,0.02) 100%);
  background-size: 3px 3px;
  pointer-events: none;
  opacity: 0.5;
}
```
对主要区块应用 `.newsprint-texture` 以获精细方格纸效果。

**3. 径向点图案（图片占位符）**：
```html
<div className="bg-[radial-gradient(#000_1px,transparent_1px)] opacity-10 [background-size:16px_16px]" />
```
用于占位图片以模拟半调印刷。

**4. 装饰分隔符**：
主要区块间用衬线装饰：
```html
<div className="py-8 text-center font-serif text-2xl text-neutral-400 tracking-[1em]">
  &#x2727; &#x2727; &#x2727;
</div>
```

## 3. 组件样式

### 按钮

**主按钮（默认）**：
```tsx
className="bg-[#111111] text-[#F9F9F7] border border-transparent hover:bg-white hover:text-[#111111] hover:border-[#111111]"
```
- 实心黑背景、白字
- 悬停：反相为白底、黑字与边框
- 锐角（强制）
- 大写文字配 `tracking-widest`
- 过渡：`transition-all duration-200`

**次按钮（描边）**：
```tsx
className="border border-[#111111] bg-transparent hover:bg-[#111111] hover:text-[#F9F9F7]"
```
- 透明背景、黑边框与文字
- 悬停：填充黑、文字变白

**幽灵按钮**：
```tsx
className="hover:bg-[#E5E5E0] hover:text-[#111111]"
```
- 无边框、悬停含蓄灰背景

**链接按钮**：
```tsx
className="text-[#111111] underline-offset-4 decoration-2 decoration-[#CC0000] hover:underline"
```
- 纯文字、悬停红下划线

**触控目标**：
确保移动端最小 `min-h-[44px]` 与 `min-w-[44px]`。

### 卡片/容器

**标准卡片**：
```tsx
<div className="border border-[#111111] bg-[#F9F9F7] p-6">
```
- 锐利黑边框
- 近白背景
- 紧凑内边距（p-4 至 p-8）

**报纸列网格**：
- 用 `border-r` 与 `border-b` 创造折叠网格布局
- 示例：4 列特性网格，每单元格有 `border-r`（最后一列除外），移动端所有有 `border-b`

**悬停状态**：
- 交互卡片加 `hover:bg-neutral-100`
- 可选加 `.hard-shadow-hover` 作戏剧性抬起效果

### 输入框

**样式**：
```tsx
className="border-b-2 border-[#111111] bg-transparent px-3 py-2 font-mono text-sm focus-visible:bg-[#F0F0F0] focus-visible:outline-none"
```
- 透明背景
- 仅底边框（2px solid black）
- 等宽字体
- 聚焦：浅灰背景（`#F0F0F0`）、无环

**无圆角**：内联强制 `borderRadius: 0px`。

### 图标

**库**：`lucide-react`

**样式**：
- `stroke-width={1.5}` 或 `stroke-1` 类
- 颜色：始终黑（`text-[#111111]`），反相区块中白除外
- 尺寸：标准 `h-6 w-6`，小 `h-4 w-4`

**图标容器**：
- 包裹于带边框盒：`border border-black h-12 w-12 flex items-center justify-center`
- 悬停效果：`hover:bg-black hover:text-white transition-all`

## 4. 非通用性（"大胆"要素）

### 强制标志性选择

**1. 垂直网格分隔符**：
不只水平分隔区块。用 `border-r` 即使同行内也创造严格垂直列。页面应感觉如报纸网格，非典型网站。

**2. 首字下沉**：
对关键段落首字母（Hero 引言、产品详情）应用巨型首字下沉（`text-7xl`、`float-left`）。可选点缀色。

**3. 跑马灯滚动条**：
用横向滚动条（如 `react-fast-marquee`）作数据。黑底白字、红点缀徽章。模仿股票滚动条或突发新闻爬行。

**4. 版本元信息**：
添加报纸风格元信息：
- 头部 "Vol. 1 | [日期] | New York Edition"
- 页脚 "Edition: Vol 1.0 | Printed in NYC"
- 图片 "Fig. 1.1" 说明

**5. 两端对齐文字**：
多列正文（博客描述、产品详情）用 `text-justify` 创造报纸列外观。

**6. 灰度图片**：
默认对所有图片应用 `grayscale` 滤镜。悬停时加 `sepia-[50%]` 作复古报纸照片效果。

**7. 非对称布局**：
勿默认 50/50 分割。用 8 列/4 列、5 列/7 列分割以增编辑感。

**8. 大写标签**：
大量用 `uppercase tracking-widest text-xs font-mono` 作区块标签、导航与元信息。

**9. 反相区块**：
至少翻转一个主要区块为黑底白字（如 How It Works）。编号步骤用红点缀。

## 5. 布局策略

### 容器
**最大宽度**：`max-w-screen-xl`（1280px）
居中配 `mx-auto`，水平内边距 `px-4`

### 网格系统
**基础**：12 列网格
用 Tailwind `grid-cols-12` 配 `col-span-*` 精准控制。

**常见分割**：
- Hero：`lg:col-span-8` / `lg:col-span-4`
- 收益：`lg:col-span-5` / `lg:col-span-7`
- 页脚：logo/描述 `col-span-2`，链接列 `col-span-1`

**折叠边框**：
相邻网格单元格共享边框。除最后一列外所有用 `border-r`，所有行用 `border-b`。

### 间距
**哲学**：高信息密度。比典型网页设计更紧凑。

- 区块内边距：`py-16`（垂直）
- 卡片内边距：`p-6` 至 `p-8`
- 项目间间隙：`gap-6` 至 `gap-8`
- 移动：减至 `p-4`、`gap-4`

### Z-Index 层
- 头部（粘性）：`z-40`
- 叠加/模态：`z-50`

## 6. 效果与动画

### 运动哲学
快、利落、机械。无弹跳或有机缓动。

**过渡类**：
```tsx
"transition-all duration-200 ease-out"
"transition-colors duration-200"
```

**悬停行为**：
1. **色彩反相**：按钮、图标黑白即时翻转
2. **硬阴影**：卡片获偏移阴影 + 轻微位移
3. **下划线**：链接获粗下划线（`decoration-2 decoration-[#CC0000]`）
4. **缩放**：圆点等小元素可 `hover:scale-150`
5. **背景**：容器获含蓄灰背景（`hover:bg-neutral-100`）

**无浮动**：元素不以柔和阴影"抬起"。它们以硬阴影 snap 就位。

**手风琴动画**：
```tsx
className="grid transition-all duration-300 ease-in-out"
// 打开：grid-rows-[1fr] opacity-100
// 关闭：grid-rows-[0fr] opacity-0
```

### 微交互
- FAQ plus 图标打开时旋转 45°
- 博客卡片图片悬停缩放 105%
- 特性图标盒悬停反相色彩
- 导航链接悬停变红

## 7. 间距、布局与图标

### 默认最大宽度
主要内容容器 `max-w-screen-xl`（1280px）。

### 间距系统
用 8px 网格系统。常见值：
- 紧凑：`gap-2`（8px）、`p-2`（8px）
- 标准：`gap-4`（16px）、`p-4`（16px）
- 舒适：`gap-8`（32px）、`p-8`（32px）
- 宽敞：`gap-16`（64px）、`py-16`（64px）

**移动**：减一级（如 `p-8` → `p-6`）

### 图标
**集成**：
- 图标置于带边框盒内（特性卡片）
- 图标作区块标记（小方块、项目符号）
- 导航中图标（最小使用）
- 社交链接中图标（页脚带边框盒）

**样式一致**：
- 所有图标来自 `lucide-react`
- 一致描边宽度（`stroke-1`）
- 默认黑色，反相区块中白色

## 8. 响应式策略

### 断点
- 移动：`< 768px`（默认）
- 平板：`md:`（768px+）
- 桌面：`lg:`（1024px+）

### 移动适配
1. **网格折叠**：
   多列网格折叠为单列（`grid-cols-1`）

2. **边框移除**：
   移动端移除 `border-r`，保留 `border-b` 作水平分隔符
   ```css
   @media (max-width: 767px) {
     .grid-border-r { border-right: none; }
   }
   ```

3. **字体缩放**：
   标题大幅缩小：`text-5xl` → `text-6xl` → `text-9xl`

4. **内边距缩减**：
   `p-16` → `p-8` → `p-6` 于更小屏幕

5. **触控目标**：
   所有交互元素最小 `44x44px`（`min-h-[44px] min-w-[44px]`）

6. **CTA 按钮**：
   移动端全宽（`w-full md:w-auto`）

7. **导航**：
   移动端显示汉堡菜单图标（44px 触控目标）
   隐藏主导航链接，显示移动菜单

### 保持美学
即使移动端也保持：
- 锐角（零圆角）
- 高对比
- 基于网格的布局（仅单列）
- 区块间水平线分隔符
- 大写标签与元信息

## 9. 可访问性与最佳实践

### 对比比
- 黑 `#111111` 于近白 `#F9F9F7`：**AAA 合规**（>17:1）
- 红 `#CC0000` 于近白：**AA 合规**（>5:1）
- 绝不在黑背景上放红文字

### 聚焦状态
```tsx
"focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-neutral-950 focus-visible:ring-offset-2"
```
- 粗黑环（2px）
- 2px offset 以保可见
- 仅键盘导航时可见（`:focus-visible`）

### 语义化 HTML
- 用 `<header>`、`<nav>`、`<section>`、`<footer>`
- 用 `<h1>` 至 `<h6>` 正确层级
- 交互元素用 `<button>`，非 div
- 链接用 `<a>` 配正确 `href`

### ARIA 标签
- 纯图标按钮加 `aria-label`
- 所有图片加 `alt` 文本（甚至装饰性）
- SVG 图标加 `role="img"` 与 `aria-labelledby`

### 键盘导航
- 所有交互元素必须键盘可访问
- 可见聚焦状态（见上）
- 手风琴项用 `button` 配正确 `aria-expanded`

## 10. 实现约束

### 字体导入
在内联 `<style>` 标签中用 `@import`：
```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&family=Playfair+Display:ital,wght@0,400;0,600;0,700;0,900;1,400&family=Lora:ital,wght@0,400;0,600;1,400&display=block');
```

定义字体类：
```css
.font-serif { font-family: 'Playfair Display', serif; }
.font-body { font-family: 'Lora', serif; }
.font-sans { font-family: 'Inter', sans-serif; }
.font-mono { font-family: 'JetBrains Mono', monospace; }
```

### Tailwind 工具
在 `<style>` 块中创建自定义工具：
- `.sharp-corners { border-radius: 0px !important; }`
- `.newsprint-texture { ... }`（见纹理章节）
- `.hard-shadow-hover:hover { ... }`（见效果章节）

### 边框折叠逻辑
为避免网格中双边框：
1. 容器用 `border-l` 与 `border-t`
2. 子元素用 `border-r` 与 `border-b`
3. 最后一列移除 `border-r`
4. 最后一行移除 `border-b`（如需）

### 组件结构（React 19+）
- 用 ref 作 prop，非 `forwardRef`
- 按钮用 `class-variance-authority` 变体
- 用 `tailwind-merge` 合并 className props

### 性能
- 延迟加载折叠下方图片
- 动画用 `transform` 与 `opacity`（GPU 加速）
- 避免直接动画 `box-shadow`（如需用 `will-change`）

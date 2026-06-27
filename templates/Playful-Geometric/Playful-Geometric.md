# Playful Geometric

> 来源：[Design Prompts](https://www.designprompts.dev/playful-geometric)

## 基本信息

| 属性 | 值 |
|------|-----|
| 风格ID | `playful-geometric` |
| 显示名称 | Playful Geometric |
| 模式 | ☀️ 浅色模式 (Light) |
| 字体类型 | sans-serif |
| 描述 | 充满活力、高能量的美学，将稳定的结构网格与俏皮的几何装饰相结合。依靠明亮纯色、简单基本形状（圆、三角、波浪线）与触感交互，营造令人联想到现代 Memphis 设计的友好乐观氛围。 |

## 布局创意 (Layout Ideas)

### Hero

居中或分割布局，主标题被浮动几何基本形（3D 感扁平形状）框定。CTA 按钮位于"水滴"或不规则形状背景上。背景含含蓄点阵图案。

### Stats

一排彩色独特形状（圆、方、三角、六边形）作数字容器。容器悬停时轻微振动或旋转。

### Product Detail

双栏布局。图片侧有"拼贴"感，主产品图后方有偏移彩色矩形。文字侧用厚实内边距与彩色项目符号。

### Features

Bento-box 风格网格，但每格有不同俏皮背景色（极浅色调）或圆角策略（部分全圆、部分叶形）。图标为实心彩色圆。

### Blog

瀑布流或网格，精选图片裁切为有趣形状（拱、胶囊、圆）。标题用粗实展示字体。标签似小贴纸。

### How It Works

横向或垂直时间线，由字面虚线 SVG 线连接，线在步骤间循环波浪。步骤编号在实心彩色星或爆发形内。

### Benefits

交替布局。每个收益文字块配大型抽象几何构图（如方块平衡于圆上）代表概念。

### Testimonials

卡片样式如对话气泡（带小尾）。它们轻微散布（随机旋转 ±2deg）以显非正式。头像探出框外。

### Pricing

三个独特列。"推荐"档位以粗虚线边框与浮动"Best Value"贴纸状徽章突出。价格巨大且彩色。

### Faq

手风琴项以粗明确边框分隔。打开时背景填充浅图案（点或线）。展开图标为大型俏皮箭头或加号。

### Final C T A

含"波浪"顶边或底边的容器盒。高对比背景（亮黄或蓝）。按钮轻微摇动以吸引注意。

### Footer

背景为深色形状，顶部有"滴落"颜料效果或波浪。大型页脚链接配趣味悬停下划线（波浪线）。

---

## 完整提示词 (Full Prompt)

# Playful Geometric 设计系统

## 设计哲学

**Playful Geometric** 是对无菌企业极简主义的解药。它通过**乐观、清晰与触感乐趣**创造情感连接。

核心概念是**"稳定网格，狂野装饰"**。内容本身（文字、表单）居于干净可读区域，但其周围世界充满运动与形状。它参考 **Memphis Group**（80 年代）但为现代数字屏幕清理——移除混乱同时保持能量。

### 气质
**友好。触感。波普。活力。**
感觉如游乐场或组织良好的贴纸书。它邀请点击。它对你微笑。

### 视觉签名
- **基本形状**：圆、三角、方、胶囊形与波浪线作背景元素、蒙版或图标。
- **硬阴影**：元素常有硬偏移投影（无模糊）赋予贴纸或剪纸感。
- **图案填充**：圆点、网格线与对角条纹用于填充形状或背景。
- **变化圆角**：混合全圆角与锐角以创造"叶"形或非对称水滴。

---

## 设计 Token 系统

### 色彩（浅色模式）
以强中性色锚定的有力高饱和调色板。

```
background:        #FFFDF5    // 暖奶油/近白（纸张感）
foreground:        #1E293B    // Slate 800（比黑更柔）
muted:             #F1F5F9    // Slate 100
mutedForeground:   #64748B    // Slate 500
accent:            #8B5CF6    // 鲜艳紫（主品牌）
accentForeground:  #FFFFFF    // 白
secondary:         #F472B6    // 热粉（俏皮跳跃）
tertiary:          #FBBF24    // 琥珀/黄（乐观）
quaternary:        #34D399    // 翡翠/薄荷（清新）
border:            #E2E8F0    // Slate 200
input:             #FFFFFF    // 白
card:              #FFFFFF    // 白
ring:              #8B5CF6    // 紫聚焦
```

**用法规则**：`accent` 用于主要操作。`secondary`、`tertiary` 与 `quaternary` 轮换用于装饰形状、图标或强调词以创造"彩纸"效果。

### 字体

**标题**：`"Outfit", system-ui, sans-serif`
- 有个性的几何无衬线。字母圆角使其友好。
- **字重**：Bold（700）或 ExtraBold（800）。

**正文**：`"Plus Jakarta Sans", system-ui, sans-serif`
- 高可读、现代、几何但人文。
- **字重**：Regular（400）、Medium（500）。

**字号比例**：1.25（Major Third）— 旋律与和谐。

### 圆角与边框

```
radius-sm:   8px
radius-md:   16px
radius-lg:   24px
radius-full: 9999px
border-width: 2px     // 默认粗边框
```

**特殊"水滴"圆角**：`rounded-tl-2xl rounded-tr-2xl rounded-br-2xl rounded-bl-none`（对话气泡风格）或 `rounded-t-full rounded-b-none`（拱形）。

### 阴影与效果

**"波普"阴影（硬阴影）**：
```
box-shadow: 4px 4px 0px 0px #1E293B;  // 深色硬阴影
box-shadow-hover: 6px 6px 0px 0px #1E293B; // 抬起效果
box-shadow-active: 2px 2px 0px 0px #1E293B; // 按压效果
```
无模糊。实心偏移色。

### 纹理与图案
- **点阵网格**：严格排列的小点背景（`bg-[url(...)]`）。
- **波浪线**：SVG 路径用作区块分隔符或标题下划线。
- **彩纸**：小型 SVG 形状（三角、圆）绝对定位于主内容块后方。

---

## 组件样式

### 按钮

**主按钮（"糖果按钮"）**：
```
- 背景：accent (#8B5CF6)
- 文字：白，font-weight: 700
- 圆角：rounded-full（胶囊）
- 边框：2px solid #1E293B（色周围深边框）
- 阴影：4px 4px 0px #1E293B（硬阴影）
- 悬停：translate-x-[-2px] translate-y-[-2px]，阴影延伸至 6px 6px
- 激活：translate-x-[2px] translate-y-[2px]，阴影缩至 2px 2px
- 图标：ArrowRight，按钮内圆形背景（白）
```

**次按钮**：
```
- 背景：透明
- 文字：foreground
- 边框：2px solid #1E293B
- 圆角：rounded-full
- 阴影：无
- 悬停：bg-tertiary (#FBBF24) - 悬停填充黄
```

### 卡片

**"贴纸"卡片**：
```
- 背景：白
- 边框：2px solid #1E293B
- 圆角：rounded-xl
- 阴影：8px 8px 0px #E2E8F0（柔和硬阴影）或 #F472B6（精选粉阴影）
- 悬停：旋转 -1deg，缩放 1.02（摆动效果）
- 标题：粗 Outfit 字体
- 图标：浮动圆 div 配居中图标，半入/半出于顶边框。
```

### 输入框

```
- 背景：白
- 边框：2px solid #CBD5E1
- 圆角：rounded-lg
- 文字：foreground
- 阴影：4px 4px 0px transparent（初始隐藏）
- 聚焦：边框 accent，阴影 4px 4px 0px accent（聚焦时硬色阴影）
- 标签：粗、大写、小型 tracking-wide。
```

---

## 布局策略

### 总体
- **容器**：`max-w-6xl`（慷慨宽度）。
- **间距**：`py-24`（96px）。宽敞但不空；以图案填充。
- **网格**：12 列逻辑，但分组为大块（6/6 或 4/4/4）。

### 独特区块布局
1.  **Hero**：
    - 文字左、图片右。
    - **装饰**：文字后方巨型黄圆。图片后方点阵图案。图片本身有"水滴"蒙版（CSS clip-path 或 border-radius 操作）。
2.  **Features**：
    - 3 格网格。
    - **装饰**：每张卡片由背景中绘制的虚线 SVG 线连接。
    - 卡片头部交替色（紫、粉、黄）。
3.  **Pricing**：
    - 中间卡片放大（1.1）并有旋转 15 度的巨型黄星徽章"MOST POPULAR"。

---

## 效果与动画

**质感**：弹跳、弹性、有趣。

- **悬停**：`transition-all duration-300 ease-[cubic-bezier(0.34,1.56,0.64,1)]`（过冲/弹跳）。
- **入场**：元素不应仅淡入；它们应**pop** 入（缩放 0→1 配弹跳）。
- **跑马灯**：用无限滚动文字作客户 logo 或关键词。
- **摆动**：悬停时图标的关键帧动画 `rotate: 0deg -> 3deg -> -3deg -> 0deg`。

---

## 图标

**Lucide React** 设置：
- **描边宽度**：`2.5px`（粗/粗实）。
- **样式**：圆线帽、圆线连接。
- **颜色**：常为彩色圆内白，或深前景色。
- **用法**：包裹于形状中。绝不孤立漂浮。一个"勾选"图标不只是勾选；它是绿圆内的勾选。

---

## 响应式策略

- **移动端**：
  - 一切堆叠。
  - "pop"阴影减至 2px 以省空间。
  - 水平波浪线转为垂直分隔符。
  - 按钮保持大且可点（最小 48px 高）。
  - 隐藏可能重叠文字的复杂背景浮动形状。

---

## 可访问性与最佳实践

- **对比**：文字为 slate-800 于近白/白上，达 AAA。
- **色彩**：绝不*仅*靠色彩。用形状与文字标签。
- **运动**：尊重 `prefers-reduced-motion`。若偏好则禁用"弹跳"与"摆动"效果。
- **聚焦**：聚焦状态为高对比（粗彩色边框 + 硬阴影）。

# Glassmorphism

> 来源：[Design Prompts](https://www.designprompts.dev/glassmorphism)

## 基本信息

| 属性 | 值 |
|------|-----|
| 风格ID | `glassmorphism` |
| 显示名称 | Glassmorphism |
| 模式 | 🌙 深色模式 (Dark) |
| 字体类型 | sans-serif |
| 描述 | 苹果风格美学，搭配丰富的网格渐变、高级感模糊与克制的布局。 |

## 布局创意 (Layout Ideas)

---

## 完整提示词 (Full Prompt)

**设计哲学**
- **核心原则**：受 Apple 的 VisionOS 与 macOS 启发。高端、空灵、内容优先。玻璃应感觉如高品质物理材质。
- **气质**：专属、聚焦、流畅。少一些"科幻"，多一些"奢华科技"。

**设计 Token 系统（DNA）**
- **色彩（Apple 深色模式）**
  - `background`：`#000000`（纯黑）— 画布。
  - `foreground`：`#F5F5F7`（Apple 近白）。
  - `muted`：`rgba(255, 255, 255, 0.08)` — 次要文字/元素。
  - `accent`：`#2997FF`（Apple 蓝）或 `#BF5AF2`（紫）— 克制用于渐变。
  - `border`：`rgba(255, 255, 255, 0.1)` — 含蓄分隔。
- **字体**
  - **字体**：使用 **"Inter"**（SF Pro 的最接近免费替代）。
  - **标题**：`font-semibold`，`tracking-tight`。干净可读。
- **圆角**：外层容器 `32px`，内层卡片 `20px`。平滑、连续曲线。
- **阴影**：元素后方大型弥散彩色辉光，但浮动元素用利落投影。
- **纹理**：
  - **背景**：丰富的动画**网格渐变**，使用 Apple 风格色调（蓝、紫、粉、橙）映衬黑色虚空。
  - **玻璃材质**：`backdrop-filter: blur(50px) saturate(180%)`。`bg-white/[0.08]`。

**组件样式**
- **按钮**：
  - **主**：白字于玻璃层上，悬停时变亮。或柔和渐变背景。
  - **次**：更深玻璃。
- **卡片**：
  - "托盘"。高模糊，含蓄白边框（`border-white/10`），与背景清晰分离。
- **输入框**：
  - 深邃暗玻璃。`bg-white/5` rounded-full。

**非通用性（"大胆"要素）**
- **克制布局**：使用**更紧的最大宽度**（`max-w-5xl` 或 `max-w-4xl`）使内容显得珍贵且聚焦。
- **动态网格**：背景应是主要色彩来源，透过玻璃渗出。
- **Bento 网格**：特性布局使用严格的圆角 bento 网格。

**完整性与内容**
- **强制**：实现 `data.json` 中所有区块：Hero、Product Detail、Stats、Blog、Features、How It Works、Benefits、Testimonials、Pricing、**FAQ**、Final CTA、Footer。
- **FAQ**：FAQ 项使用玻璃卡片。

**效果与动画**
- **网格动画**：创建 `mesh-blob` CSS 类配无限旋转。**关键**：在 CSS 中定义 `animation-delay` 工具类（`.animation-delay-2000`、`.animation-delay-4000`）以确保光斑异步移动。
- **过渡**：平滑、缓慢过渡（`duration-500`）。

**实现说明**
- 确保玻璃背景上文字有足够对比。
- 使用 `lucide-react` 作图标。

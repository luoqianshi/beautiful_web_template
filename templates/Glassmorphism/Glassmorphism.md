# Glassmorphism

> 来源：[Design Prompts](https://www.designprompts.dev/glassmorphism)

## 基本信息

| 属性 | 值 |
|------|-----|
| 风格ID | `glassmorphism` |
| 显示名称 | Glassmorphism |
| 模式 | 🌙 深色模式 (Dark) |
| 字体类型 | sans-serif |
| 描述 | Apple-inspired aesthetic with rich mesh gradients, premium blur, and constrained layouts. |

## 布局创意 (Layout Ideas)

---

## 完整提示词 (Full Prompt)

**Design Philosophy**
- **Core Principles**: Inspired by Apple's VisionOS and macOS. Premium, ethereal, and content-forward. The glass should feel like a high-quality physical material.
- **Vibe**: Exclusive, focused, and fluid. Less "sci-fi", more "luxury tech".

**Design Token System (The DNA)**
- **Colors (Apple Dark Mode)**
  - `background`: `#000000` (Pure Black) - The canvas.
  - `foreground`: `#F5F5F7` (Apple Off-White).
  - `muted`: `rgba(255, 255, 255, 0.08)` - Secondary text/elements.
  - `accent`: `#2997FF` (Apple Blue) or `#BF5AF2` (Purple) - Used sparingly in gradients.
  - `border`: `rgba(255, 255, 255, 0.1)` - Subtle separation.
- **Typography**
  - **Font**: Use **"Inter"** (closest free proxy to SF Pro). 
  - **Headings**: `font-semibold`, `tracking-tight`. Clean and legible.
- **Radius**: `32px` for outer containers, `20px` for inner cards. Smooth, continuous curves.
- **Shadows**: Large, diffuse colored glows behind elements, but crisp drop shadows for floating elements.
- **Textures**: 
  - **Background**: A rich, animated **Mesh Gradient** using Apple-style tones (Blue, Purple, Pink, Orange) against a black void.
  - **Glass Material**: `backdrop-filter: blur(50px) saturate(180%)`. `bg-white/[0.08]`.

**Component Stylings**
- **Buttons**:
  - **Primary**: White text on a glass layer that gets brighter on hover. Or a soft gradient background.
  - **Secondary**: Darker glass.
- **Cards**:
  - "Platters". High blur, subtle white border (`border-white/10`), distinct separation from background.
- **Inputs**:
  - Deep, dark glass. `bg-white/5` rounded-full.

**Non-Genericness (The "Bold" Factor)**
- **Constrained Layout**: Use a **tighter max-width** (`max-w-5xl` or `max-w-4xl`) to make the content feel precious and focused.
- **Dynamic Mesh**: The background should be the main source of color, bleeding through the glass.
- **Bento Grid**: Use a strict, rounded bento grid for feature layouts.

**Completeness & Content**
- **MANDATORY**: Implement ALL sections from `data.json`: Hero, Product Detail, Stats, Blog, Features, How It Works, Benefits, Testimonials, Pricing, **FAQ**, Final CTA, Footer.
- **FAQ**: Use glass cards for the FAQ items.

**Effects & Animation**
- **Mesh Animation**: Create a `mesh-blob` CSS class with infinite rotation. **CRITICAL**: Define `animation-delay` utility classes (`.animation-delay-2000`, `.animation-delay-4000`) in the CSS to ensure blobs move asynchronously.
- **Transitions**: Smooth, slow transitions (`duration-500`).

**Implementation Notes**
- Ensure sufficient contrast for text on glass backgrounds.
- Use `lucide-react` for icons.

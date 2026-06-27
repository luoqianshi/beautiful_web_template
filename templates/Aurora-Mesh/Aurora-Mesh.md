# Aurora Mesh

> 来源：[Design Prompts](https://www.designprompts.dev/aurora-mesh)

## 基本信息

| 属性 | 值 |
|------|-----|
| 风格ID | `aurora-mesh` |
| 显示名称 | Aurora Mesh |
| 模式 | 🌙 深色模式 (Dark) |
| 字体类型 | sans-serif |
| 描述 | Flowing mesh gradients, aurora effects, vibrant color transitions, modern startup aesthetic inspired by Stripe and Vercel |

## 布局创意 (Layout Ideas)

### Hero

Full-height hero with animated mesh gradient background. Split layout with headline left (massive typography with gradient text fill), floating 3D-ish card mockup right with aurora glow underneath. CTAs have pill shapes with gradient borders.

### Stats

Horizontal strip with glass-morphic stat cards floating over a subtle aurora wave. Each stat has a glowing accent bar on top indicating its category color.

### Features

Asymmetric bento grid with varying card sizes. Cards have dark glass backgrounds with colored gradient borders that pulse subtly. Icons sit in gradient orbs.

### How It Works

Vertical timeline with a glowing gradient line connecting steps. Each step card has a mesh gradient corner accent. Numbers are oversized with gradient fills.

### Benefits

Two-column layout with benefit cards stacked. Each card has an aurora streak across the top edge. Checkmark icons with gradient fills.

### Pricing

Three cards with the featured card elevated and wrapped in an animated gradient border. Background has slow-moving mesh gradient. Prices use gradient text.

### Testimonials

Carousel or masonry of quote cards with avatar images having gradient ring borders. Quote marks are oversized with aurora gradient fills.

### Faq

Accordion style with gradient accent lines on the left. Expanded items reveal answers with a soft glow effect. Plus/minus icons have gradient treatment.

### Blog

Horizontal scrolling cards with image overlays featuring gradient mesh filters. Date badges have pill shapes with gradient backgrounds.

### Footer

Dark base with subtle aurora waves at the top edge. Links organized in columns with gradient hover underlines. Social icons in gradient orbs.

---

## 完整提示词 (Full Prompt)

# Aurora Mesh Design System

## Design Philosophy

Aurora Mesh captures the ethereal, flowing beauty of the northern lights fused with modern mesh gradient technology. This is the aesthetic of **premium SaaS products**—think Stripe's cosmic depth, Vercel's dark elegance, and Linear's polished minimalism, but pushed further into the realm of **living, breathing color**.

**Core Principles:**
- **Fluid Color**: Gradients are never static. They flow, morph, and breathe with organic movement
- **Dark Canvas, Bright Accents**: Deep, near-black backgrounds make vibrant aurora colors sing
- **Dimensional Depth**: Layers of blur, glow, and transparency create a sense of floating UI
- **Premium Polish**: Every detail is refined—smooth curves, perfect spacing, considered micro-interactions

**The Vibe:** Sophisticated, futuristic, premium, otherworldly. Like operating a spaceship's interface while flying through an aurora. The user should feel like they're touching the future.

**Visual Signatures:**
- Mesh gradients that appear to move and shift
- Colored glow effects bleeding from elements
- Glass-like surfaces catching light
- Gradient text on headlines
- Floating cards with colored shadows
- Aurora wave patterns in backgrounds

---

## Design Token System

### Colors (Dark Mode - Definitive)

```
Background:
  base: #09090b (near-black with slight warmth)
  elevated: #18181b (card backgrounds)
  surface: #27272a (input backgrounds, borders)

Foreground:
  primary: #fafafa (headings, important text)
  secondary: #a1a1aa (body text, descriptions)
  muted: #71717a (placeholders, disabled)

Aurora Palette (The Star):
  violet: #8b5cf6
  purple: #a855f7
  fuchsia: #d946ef
  pink: #ec4899
  cyan: #22d3ee
  teal: #2dd4bf

Gradient Stops (for mesh):
  aurora-1: #8b5cf6 (violet)
  aurora-2: #d946ef (fuchsia)
  aurora-3: #22d3ee (cyan)
  aurora-4: #2dd4bf (teal)

Accent (Primary Actions):
  DEFAULT: #a855f7
  hover: #c084fc

Border:
  subtle: #27272a
  DEFAULT: #3f3f46
  glow: rgba(168, 85, 247, 0.5)

Success: #34d399
Warning: #fbbf24
Error: #f87171
```

### Typography

**Font Stack:**
- **Headlines**: "Instrument Sans" (Google Fonts) - Clean, geometric, modern. Alternative: Inter
- **Body**: "Inter" (Google Fonts) - Highly legible, neutral, professional
- **Mono/Code**: "JetBrains Mono" for any code snippets

**Scale:**
- Hero headline: `text-6xl md:text-7xl lg:text-8xl` with `font-bold tracking-tight`
- Section titles: `text-4xl md:text-5xl` with `font-semibold`
- Card titles: `text-xl md:text-2xl` with `font-semibold`
- Body large: `text-lg` with `text-secondary`
- Body: `text-base` with `leading-relaxed`
- Small/Caption: `text-sm` with `text-muted`

**Gradient Text Treatment:**
```css
.gradient-text {
  background: linear-gradient(135deg, #a855f7 0%, #ec4899 50%, #22d3ee 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
```

### Radius & Border

- **Default radius**: `rounded-2xl` (16px) - Soft, modern, approachable
- **Buttons**: `rounded-full` (pill-shaped for primary actions)
- **Small elements**: `rounded-xl` (12px)
- **Inputs**: `rounded-xl`
- **Border width**: `border` (1px) with semi-transparent colors

### Shadows & Effects

**Glow Shadows (The Signature):**
```
glow-sm: 0 0 20px rgba(168, 85, 247, 0.15)
glow-md: 0 0 40px rgba(168, 85, 247, 0.2)
glow-lg: 0 0 60px rgba(168, 85, 247, 0.25), 0 0 120px rgba(34, 211, 238, 0.1)
glow-colored: 0 0 40px var(--glow-color, rgba(168, 85, 247, 0.3))
```

**Elevation (Layered):**
```
elevation-1: 0 1px 2px rgba(0, 0, 0, 0.5)
elevation-2: 0 4px 12px rgba(0, 0, 0, 0.4)
elevation-3: 0 8px 30px rgba(0, 0, 0, 0.5), 0 0 40px rgba(168, 85, 247, 0.1)
```

### Textures & Patterns (Critical)

**Mesh Gradient Background:**
CSS mesh gradient using multiple radial gradients layered:
```css
.aurora-mesh {
  background-color: #09090b;
  background-image:
    radial-gradient(at 40% 20%, rgba(139, 92, 246, 0.3) 0px, transparent 50%),
    radial-gradient(at 80% 0%, rgba(34, 211, 238, 0.2) 0px, transparent 50%),
    radial-gradient(at 0% 50%, rgba(217, 70, 239, 0.2) 0px, transparent 50%),
    radial-gradient(at 80% 50%, rgba(45, 212, 191, 0.15) 0px, transparent 50%),
    radial-gradient(at 0% 100%, rgba(236, 72, 153, 0.2) 0px, transparent 50%),
    radial-gradient(at 80% 100%, rgba(139, 92, 246, 0.15) 0px, transparent 50%);
}
```

**Noise Overlay:**
Subtle grain texture at 2-5% opacity to add depth and reduce banding in gradients.

**Aurora Wave (for section dividers):**
SVG wave patterns with gradient fills, positioned at section tops/bottoms.

---

## Component Stylings

### Buttons

**Primary Button:**
- Background: Gradient `from-violet-500 via-fuchsia-500 to-pink-500`
- Shape: `rounded-full` pill
- Padding: `px-8 py-3`
- Text: `text-white font-semibold`
- Shadow: `shadow-lg shadow-violet-500/25`
- Hover: Scale up slightly `hover:scale-105`, increase glow
- Active: Scale down `active:scale-95`
- Transition: `transition-all duration-200`

**Secondary Button:**
- Background: `bg-white/5` (glass effect)
- Border: `border border-white/10`
- Text: `text-white`
- Hover: `bg-white/10`, border glows
- Backdrop: `backdrop-blur-sm`

**Ghost Button:**
- Background: transparent
- Text: `text-secondary`
- Hover: `text-primary`, subtle glow underline

### Cards/Containers

**Standard Card:**
- Background: `bg-zinc-900/50` with `backdrop-blur-xl`
- Border: `border border-zinc-800/50`
- Radius: `rounded-2xl`
- Shadow: `shadow-2xl shadow-black/50`
- Hover: Border brightens, subtle glow appears

**Featured Card:**
- Wrapped in gradient border container
- Outer: Animated gradient border using `background: conic-gradient` trick
- Inner: Dark solid background
- Glow: Colored shadow matching the dominant gradient color

**Glass Card:**
- Background: `bg-white/5`
- Backdrop: `backdrop-blur-2xl backdrop-saturate-150`
- Border: `border border-white/10`

### Inputs

- Background: `bg-zinc-900`
- Border: `border border-zinc-700`
- Radius: `rounded-xl`
- Text: `text-white`
- Placeholder: `placeholder:text-zinc-500`
- Focus: `focus:border-violet-500 focus:ring-2 focus:ring-violet-500/20`
- Transition: Smooth border color change

### Icons

- Default: `text-zinc-400` with `w-5 h-5`
- In gradient orbs: Icon sits inside a `rounded-xl` container with gradient background
- Interactive: Color shifts to accent on hover
- Feature icons: Larger `w-8 h-8`, often with gradient backgrounds or colored glow

---

## Layout Strategy

**Container:** `max-w-7xl mx-auto px-6 lg:px-8`

**Section Spacing:** `py-24 md:py-32` between major sections

**Grid System:**
- Features: `grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8`
- Bento: Varying `col-span` and `row-span` for visual interest
- Stats: `grid grid-cols-2 md:grid-cols-4 gap-6`

---

## Effects & Animation

**Motion Feel:** Smooth, elegant, and slightly slow—like floating through water or space. Never jarring.

**Transitions:**
- Default: `transition-all duration-300 ease-out`
- Hover effects: `duration-200`
- Page elements: `duration-500` for fade-ins

**Keyframe Animations:**

```css
@keyframes aurora-shift {
  0%, 100% { opacity: 0.5; transform: translateY(0) scale(1); }
  50% { opacity: 0.8; transform: translateY(-20px) scale(1.1); }
}

@keyframes glow-pulse {
  0%, 100% { box-shadow: 0 0 20px rgba(168, 85, 247, 0.2); }
  50% { box-shadow: 0 0 40px rgba(168, 85, 247, 0.4); }
}

@keyframes gradient-rotate {
  0% { --gradient-angle: 0deg; }
  100% { --gradient-angle: 360deg; }
}
```

**Scroll Animations:** Elements fade and slide up on scroll (use intersection observer or CSS scroll-driven animations).

---

## Iconography

- Library: `lucide-react`
- Stroke: Default stroke width (2px)
- Size: `w-5 h-5` for inline, `w-6 h-6` for standalone, `w-8 h-8` for feature cards
- Treatment: Often placed inside gradient orbs or given colored backgrounds
- Color: `text-zinc-400` default, `text-violet-400` for accents

---

## Responsive Strategy

**Mobile:**
- Stack all grids to single column
- Reduce headline sizes by 1-2 steps
- Mesh gradients simplified (fewer layers for performance)
- Cards go full-width with reduced padding
- Navigation collapses to hamburger
- Aurora effects stay but with reduced intensity

**Tablet:**
- 2-column grids
- Side-by-side layouts for hero

**Desktop:**
- Full 3-4 column grids
- All effects at full intensity
- Maximum visual impact

---

## Accessibility

**Contrast:**
- Primary text (#fafafa) on dark background (#09090b) = 18.4:1 ratio ✓
- Secondary text (#a1a1aa) on dark background = 7.1:1 ratio ✓
- All text passes WCAG AAA

**Focus States:**
- Visible focus ring: `focus-visible:ring-2 focus-visible:ring-violet-500 focus-visible:ring-offset-2 focus-visible:ring-offset-zinc-900`
- Never remove focus outlines
- Focus rings match the aurora accent color

**Motion:**
- Respect `prefers-reduced-motion`
- Provide static fallbacks for all animations

---

## Implementation Notes

- Use Tailwind CSS v4 with arbitrary values for specific colors
- Create CSS custom properties for repeated gradient values
- Use `style` prop for dynamic gradient backgrounds where needed
- Build all components locally using `cva` and `tailwind-merge`
- Import icons from `lucide-react`
- Mesh gradient backgrounds should be in a style.css file and applied via className

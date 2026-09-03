# Moonshot

> 来源：[Moonshot AI / 月之暗面官网](https://www.moonshot.cn/)（逆向提炼）

## 基本信息

| 属性 | 值 |
|------|-----|
| 风格ID | `moonshot` |
| 显示名称 | Moonshot · Lunar Dark |
| 模式 | 🌑 纯黑深色模式 (Pure Black Dark) |
| 字体类型 | sans-serif（M PLUS 1 / Noto Sans SC） |
| 描述 | 月食式的暗面极简美学：纯黑虚空中的一轮环光，单色灰阶 + 单点蓝点缀，胶囊按钮与暗玻璃浮卡，对话输入框即 Hero。 |

## 布局创意 (Layout Ideas)

### Hero

- 全屏纯黑中轴对称。背景层为巨型模糊品牌字 marquee 横向缓移（blur 14px、不透明度 0.15、扫描线蒙版）。
- 视觉中心是"月食"圆盘：纯黑圆体 + 1px 亮白环边 + 弥散辉光（呼吸动画 6s）。
- 向下依次为：轨道小圆点、18px 标语、大号圆角输入框（radius 16px、`#121212`、右下 40px 圆形发送钮）、两枚胶囊按钮。

### Research

- 区块头两端对齐：左"最新研究"（32px/500）+ 14px 副文，右胶囊"查看更多"。
- 3 列网格（gap 24px）：灰度太空摄影图（aspect 16/10、radius 12px、`grayscale(1)`）+ 12px 日期（白 35%、字距 0.72px）+ 16px 标题。

### Showcase

- 居中标题（40px）+ 副文；下方左右分栏（gap 64px）。
- 左列：56px 展示标题（字距 -0.88px）+ 描述 + 胶囊按钮；区块左缘有垂直时间轴刻度。
- 右列：暗玻璃浮卡（`rgba(18,18,18,0.72)` + `blur(23px) brightness(0.6)`、radius 20px）模拟模型选择器，底层压暗色输入框剪影。

### Doodle

- 居中标题 + 副文；3 列卡片：插画图（aspect 4/3）+ 月份标签 + 标题 + 14px 描述。

### Final CTA

- 上下 padding 200px；透视线框网格地面与顶棚（`perspective(700px) rotateX(±58deg)` + 渐隐蒙版）。
- 居中：App 图标（80px、radius 20px、右上蓝点）→ 40px 标题 → 三枚带图标胶囊 → 胶囊输入框。

### Footer

- 左侧品牌 + 标语 + 圆形社交图标；右侧 3 列链接（14px，白 56% → hover 100%）。

---

## 完整提示词 (Full Prompt)

**设计哲学**
- **核心原则**：虚空优先——画布是纯 `#000000` 虚空，内容如天体悬浮；一束光原则——每屏只允许一个视觉光源；输入即入口——对话框是 Hero 主角；中文优先排印，字重克制（400/500）。
- **气质**：冷静、克制、宇宙级孤独感、精密仪器般的安静高级。像深夜天文台：黑、静、只有仪器微光。

**设计 Token 系统（DNA）**
- **色彩（单色灰阶 + 单点蓝）**
  - `background`：`#000000`（纯黑虚空）。
  - `surface-1/2/3`：`#121212` / `#1F1F1F` / `#323232`（输入框 → 悬浮面 → 圆钮）。
  - `foreground`：`rgba(255,255,255,.9)`；副文 `.56`；微字 `.35`。
  - `accent`：`#4D6BFE`（唯一彩色：logo 蓝点 / 选中勾）。
  - `border`：`rgba(255,255,255,0.12)` → hover `0.24`。
- **字体**
  - `"M PLUS 1","Noto Sans SC"`；展示字 56px/500/-0.88px；区块题 32–40px/500；正文 16px/400；微字 12px/字距 0.72px。
- **圆角**：胶囊 `999px`；卡片/输入框 `16–24px`；小件 `8px`。
- **签名阴影（双内嵌发丝高光）**：
  ```css
  box-shadow:
    inset 1px 1px 0 -0.5px #333, inset -1px -1px 0 -0.5px #262626,
    inset 1px 1px 0.5px -1px rgba(255,255,255,.15),
    inset -1px -1px 0.5px -1px rgba(255,255,255,.15),
    inset 0 0 3px rgba(255,255,255,.08), inset 0 0 11px rgba(255,255,255,.04);
  ```
- **间距**：区块 `80px 0`（CTA `200px 0`）；页面 gutter 80px；卡片 gap 24px。

**组件样式**
- **胶囊按钮**：`#121212` 底 + 1px 边 + 发丝 inset 阴影；hover 提亮至 `#1F1F1F`、边框 0.24；`all .35s cubic-bezier(0.16,1,0.3,1)`。
- **卡片**：图卡 radius 12px + 灰度图 + hover 增亮放大；玻璃浮卡 `blur(23px) brightness(0.6)`。
- **输入框**：Hero 大输入 radius 16px / min-height 120px，右下圆形发送钮；CTA 胶囊输入 999px。
- **导航**：固定 72px，`rgba(0,0,0,.4)` + `blur(17px)`，链接 14px 白 84%。

**非通用性（"大胆"要素）**
1. **月食 Hero**：黑盘 + 亮白环 + 辉光呼吸，背景巨型模糊字 marquee（60s linear）。
2. **发丝高光胶囊**：6 层 inset shadow 模拟拉丝金属。
3. **单点蓝纪律**：全站唯一彩色仅限 logo 蓝点与选中勾。
4. **对话框即 Hero**、**透视网格地面**、**时间轴刻度**、**灰度太空摄影 + 12px 日期**。

**效果与动画**
- 入场：`opacity + translateY(30px)`，`1.05s cubic-bezier(0.16,1,0.3,1)`，IntersectionObserver 触发。
- 持续：marquee 横移、辉光呼吸；尊重 `prefers-reduced-motion`。

**实现说明**
- 单文件 HTML + 内嵌 CSS/vanilla JS；Google Fonts 加载 `M PLUS 1` + `Noto Sans SC`。
- Token 全部收敛到 `:root` CSS 变量；月食与透视网格为纯 CSS 实现，无需图片。

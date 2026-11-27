# Paper Science Editorial（纸面科学编辑风）

> 来源：https://www.stepfun.com/

## 基本信息

| 属性 | 值 |
|------|-----|
| 风格ID | `Paper-Science-Editorial` |
| 显示名称 | 纸面科学编辑风（StepFun 式） |
| 模式 | Light（页脚为纯黑反白区块） |
| 字体类型 | serif（衬线展示 + 无衬线正文 + 等宽代码） |
| 描述 | 纸白底色、衬线大标题、信号蓝点缀与科学档案拼贴构成的研究机构编辑风：像一本摊开的自然哲学手稿，而非 SaaS 落地页。 |

## 布局创意 (Layout Ideas)

### Nav（固定顶栏）

60px 高固定顶栏，纸白底 `#f7f7f5`，1px 底边框 `#ddddd9`。容器 max-width 1440px、左右内边距 120px。左侧黑色圆点矩阵 logo + 无衬线 wordmark；中部 14px 无衬线导航链接（带下拉 caret）；右侧语言切换（EN）。整栏无阴影、无毛玻璃，靠一条发丝线分层。

### Hero（首屏画布）

近全屏（约 900px）纸白画布，带极淡纸张噪点。视觉重心是一组**绝对定位、相互叠压的科学档案拼贴**：手稿扫描件、月相图版、粒子径迹图、蝴蝶半调网屏、泛黄公式纸，各自微旋转（约 ±10°）与缩放（0.64–0.95），纸色各异（米白、云蓝 `#d8e2ec`、淡黄）。拼贴外围套一个**设计工具式选框**：1px 黑细线矩形 + 四角 8px 信号蓝 `#00a9ff` 方形手柄。拼贴间穿插双语衬线小注（英文行带删除线）。左下角两行巨型衬线标题（56px/66px，w700），第二行关键词整词染信号蓝；标题下 28px 无衬线中文副标题（64% 黑）。右下角三行双语衬线旁注（14–16px），与左下标题形成对角呼应。大量留白，元素不填满画布。

### Flagship Feature（旗舰模型横幅）

通栏圆角 24px 大卡，近白底 `#fbfafb`，min-height 约 460px，overflow hidden。左列：衬线 54px/81px 标题（w600）+ 16px 无衬线说明 + 墨黑主按钮。右半幅：**巨型半调网屏数字**（如 "5"，约 500px 高）向左喷散墨点粒子，叠加细十字构造线、半透明信号蓝矩形与蓝色方形节点——像一张正在被制版印刷的图纸。

### Open-Weights Bar（开放权重的条状卡）

横幅卡下方 16px 间距处一条圆角 16px、1px 边框 `#ddddd9` 的白底横条：左侧 14px 无衬线小标签 + 20px 加粗陈述句；右侧并排墨黑实底按钮（Hugging Face）与描边按钮（GitHub）。padding 20px 24px，flex 两端对齐。

### Model List（模型能力网格）

区块标题衬线 48px/67px（w600）+ 16px 灰副标题，左对齐。下方 2 列网格、gap 24px；卡片圆角 24px、padding 32px、min-height 530px，底色为交替的暖灰 `#f5f5f5` 与米白 `#f6f6f1`，无边框或仅发丝线。卡内上文下图：标题/描述在上，产品视觉沉底，flex column + justify-between。

### Business Cards（产品三联卡）

3 列等宽卡片，每卡承载一种"纸面产品模拟物"：① 工作区侧栏 UI mock（白底、灰选中态胶囊）；② **倾斜约 10° 的纸质订阅卡**叠放在米色纸纹背景上，带 macOS 红黄绿窗点、衬线斜体标题、偏移柔影；③ 深色终端代码窗（`#0b0c0e`，VSCode 暗色语法配色）叠在浅色编辑器 mock 之上。卡片即插图，插图即组件。

### Footer（黑底反白）

纯黑 `#000` 区块，pt 50px / pb 16px。左列：反白 logo + 14px 灰 tagline + 白描边深色按钮；右部 4 列导航网格（gap 24px，移动端 2 列），列标题衬线加粗反白，链接 14px 无衬线 64% 白。四角装饰**半调点阵渐隐纹理**。底部 12px 灰法律信息行，上缘 12% 白分隔线。

---

## 完整提示词 (Full Prompt)

# 设计风格：Paper Science Editorial（纸面科学编辑风）

## 设计哲学

### 核心原则

把 AI 研究机构的官网做成**一本自然哲学刊物的摊开页**：纸张是底色，衬线是声音，科学档案图像是论据，信号蓝是编辑留下的批注笔迹。秩序从混沌中涌现——拼贴看似随意叠压，实则被一个精确的选框与网格约束。所有精确性服务于"手稿感"，而非"产品感"。拒绝一切渐变、玻璃拟态与霓虹辉光；深度只来自纸张叠压的柔影与半调网屏的墨点。

### 视觉气质

**情感关键词**：
- *档案感（Archival）* — 手稿扫描件、月相图版、粒子径迹，像从研究所资料室借来的一叠纸
- *编辑感（Editorial）* — 衬线大标题、双语旁注、删除线批注，页面是被编辑过的文稿
- *克制的信号（Signal）* — 全页近乎单色，唯一高饱和色 `#00a9ff` 只出现在关键词、选框手柄与制版标记上
- *纸面深度（Paper depth）* — 无渐变无玻璃，层次靠纸色微差、叠压与偏移柔影

**此设计不是什么**：
- 不是深色科技风 / 赛博霓虹：主舞台是纸白，黑色只属于页脚与终端
- 不是 SaaS 渐变落地页：零渐变、零毛玻璃、零彩色光晕
- 不是圆角糖果风：圆角克制（8/16/24），按钮小而方润，不做 pill 海洋
- 不是满版信息流：留白慷慨，首屏允许大面积空纸

### 此风格的 DNA

#### 1. 科学档案拼贴（Hero Collage）
绝对定位叠压的扫描件组合：手稿、月相、粒子径迹、蝴蝶半调图，微旋转 ±10°、缩放 0.64–0.95，纸色互异。出现于 Hero 中心偏右。有效原因：用"真实史料"替代抽象 3D 渲染， instantly 传达研究机构身份。

#### 2. 设计工具选框（Selection Marquee）
拼贴外围 1px 黑细线矩形 + 四角 8px 信号蓝方手柄，把整组拼贴框成"画布上被选中的对象"。有效原因：暗示"页面即工作台"，与 AI Studio 产品叙事互文。

#### 3. 删除线双语旁注（Struck-through Bilingual Notes）
衬线小注三行一组：英文两行带 `line-through`，中文一行正常。散布于拼贴间隙与 Hero 右下角。有效原因：删除线=编辑批注痕迹，制造"手稿被修订过"的时间感。

#### 4. 半调巨型数字 + 制版标记（Halftone Numeral）
旗舰卡右半幅的巨型半调网屏数字，墨点向左喷散，叠加十字细线、半透明蓝矩形与蓝色方节点。有效原因：把模型版本号做成"正在制版的印张"，技术感来自印刷工艺而非电路纹理。

#### 5. 衬线标题中的信号蓝关键词
Hero 标题第二行整词染 `#00a9ff`（如 "for **everyone**"）。有效原因：单色页面上唯一一次高饱和爆发，视线锚点极强。

#### 6. 倾斜纸质 UI 卡（Tilted Paper UI）
产品卡做成带 macOS 窗点的纸片，旋转约 10°，投 `-5px 20px 32px rgba(0,0,0,0.1)` 偏移柔影。有效原因：UI 截图被"纸张化"，与档案拼贴同属一个物质世界。

#### 7. 黑底半调页脚（Halftone Footer）
纯黑页脚四角以半调点阵渐隐装饰，反白衬线列标题。有效原因：与首屏纸白形成刊物"封面—封底"的对仗，点阵呼应半调数字。

---

## 设计 Token 系统（DNA）

### 色彩策略

**色彩聚焦**：纸白单色舞台 + 88/64/48/24% 四级黑透明度文字阶梯 + 唯一信号蓝 `#00a9ff`。辅助纸色（云蓝、淡黄、暖灰）只出现在拼贴与卡片表面；黑色实底仅用于主按钮、终端与页脚。全页**零渐变**。

| Token | 值 | 用法与上下文 |
|:------|:------|:----------------|
| `--color-paper-white` | `#f7f7f5` | 顶栏与 Hero 画布底 |
| `--color-background` | `#f8f8f6` | 页面备用纸底 |
| `--bg-primary` | `#ffffff` | 主内容区、横条卡底 |
| `--color-ink-black` | `#1a1a1a` | 主按钮底、深色文字实色 |
| `--text-primary` | `#000000e0`（88% 黑） | 标题与正文主色 |
| `--text-secondary` | `#000000a3`（64% 黑） | 副标题、导航链接 |
| `--text-tertiary` | `#0000007a`（48% 黑） | 说明文字、旁注 |
| `--text-disabled` | `#0000003d`（24% 黑） | 禁用态 |
| `--color-signal-blue` | `#00a9ff` | 标题关键词、选框手柄、制版标记、焦点环 |
| `--color-cloud-mist` | `#d8e2ec` | 拼贴纸色之一、浅蓝表面 |
| `--color-maker-yellow` | `#f9b845` | 拼贴中的淡黄纸色来源（低饱和使用） |
| `--color-line-grey` | `#a8a8a4` | 构造细线、灰线 |
| `--color-boder` | `#ddddd9` | 顶栏底线、横条卡边框 |
| `--border-color` | `#00000014`（8% 黑） | 发丝分隔线 |
| `--bg-card` / 卡面交替 | `#f5f5f5` / `#f6f6f1` | 模型网格卡底（暖灰 / 米白交替） |
| `--bg-secondary` | `#f2f3f5` | 次级表面、UI mock 选中态 |
| 终端底 | `#0b0c0e` / `#2c2b30` | 代码窗与窗口标题栏 |
| 页脚底 | `#000000` | 封底黑 |
| 反白文字阶梯 | `#ffffffe0` / `#ffffffa3` / `#ffffff7a` | 页脚主/次/弱文字 |
| 代码语法色 | `#ce9178` `#dcdcaa` `#d7ba7d` `#569cd6` `#9cdcfe` | 终端内字符串/函数/参数/关键字/变量（VSCode 暗色系） |

**签名渐变**：无。此风格明确不使用任何 gradient；层次全部由实色纸面与透明度阶梯承担。

### 字体系统

**字体配对**：
- **展示字体**：`Lora, "Source Han Serif CN", "Noto Serif SC", Georgia, serif` — 所有大标题、双语旁注、页脚列标题；书卷气与档案感的来源（加载 Lora 500/600、思源宋体 600）
- **UI/正文字体**：`Inter, "Source Han Sans CN", -apple-system, BlinkMacSystemFont, sans-serif` — 导航、按钮、正文、副标题（加载 Inter 400/600、思源黑体 400/500/700）
- **等宽字体**：`"PT Mono", "SF Mono", Menlo, monospace` — 终端代码窗（400/700）

**字号阶梯与用法**：

| 元素 | 尺寸 | 字体 | 字重 | 字距 | 备注 |
|:--------|:-----|:-----|:-------|:---------|:------|
| Hero 标题 | 56px / 66px | 衬线 | 700 | -1.12px | 两行；第二行关键词染信号蓝 |
| 旗舰卡标题 | 54px / 81px | 衬线 | 600 | -1.28px | 行高放宽至 1.5 倍，呼吸感 |
| 区块标题 | 48px / 67px | 衬线 | 600 | -0.96px | 左对齐，下接 16px 灰副标题 |
| 卡内展示标题 | 52px / 67px | 衬线 | 500 | -1.24px | 大卡内的产品名展示 |
| 卡标题 / 陈述句 | 24px / 30px、20px | 无衬线 | 600–700 | normal | 横条卡陈述、卡片标题 |
| Hero 副标题 | 28px / 1.5 | 无衬线 | 400 | normal | 64% 黑 |
| 正文 | 16px / 24px | 无衬线 | 400 | normal | 88% 黑 |
| 次级正文 / 导航 | 14px / 20px | 无衬线 | 400–500 | normal | 64% 黑 |
| 说明 / 旁注 | 13px / 17px、14–16px | 无衬线 / 衬线 | 400 | normal | 48% 黑；双语旁注用衬线 |
| 法律信息 | 12px / 1.5 | 无衬线 | 400 | normal | 页脚底部 |

**排印签名**：双语旁注的英文行加 `text-decoration: line-through`；衬线标题统一负字距（约 -0.02em）；禁止 uppercase 变换。

### 间距与布局

- **区块间距**：section 统一 `padding: 50px 0`；Hero 例外为近全屏画布
- **容器宽度**：`max-width: 1440px; margin-inline: auto; padding-inline: 120px`（桌面）
- **网格间隙**：主网格 gap 24px；卡内元素 gap 16px / 12px / 8px / 4px 阶梯；横条卡内 gap 12px
- **非对称模式**：Hero 左下标题 vs 右上拼贴 vs 右下旁注的三角构图；旗舰卡左文右图约 4:6；拼贴内部全部绝对定位叠压

**常见间距值**：4 / 8 / 12 / 16 / 24 / 32 / 50 / 80 / 120px；卡片内边距 32px；横条卡 20px 24px；按钮 7px 12px（小）至 10px 20px（中）。

### 边框、表面与阴影

**圆角策略**：克制三档——按钮/小元素 8px（辅以 6px 徽章）、横条卡 16px、大卡 24px（rounded-3xl）。不做全 pill 按钮。

**边框**：统一 `1px solid`；结构线用 `#ddddd9`，发丝线用 `#00000014`；选框用 1px `#1a1a1a` 实线。

**阴影系统**：

| Token | 值 | 用法 |
|:------|:------|:------|
| `shadow-float` | `0 20px 32px rgba(0,0,0,0.06)` | 大卡悬浮柔影（向下弥散） |
| `shadow-paper` | `-5px 20px 32px rgba(0,0,0,0.10)` | 倾斜纸卡的偏移柔影（向左下） |
| `shadow-paper-sm` | `-5px 20px 16px rgba(0,0,0,0.08)` | 小纸片/叠层窗 |

**纹理与图案**：① 纸张噪点（Hero 底，极低对比度）；② 半调点阵（巨型数字、页脚四角渐隐）；③ 十字构造细线与蓝色方节点（制版标记）；④ 拼贴扫描件自身的墨迹与网屏。无渐变、无 backdrop-filter。

---

## 组件样式与交互

### 按钮

**主按钮（墨黑）**：
- 背景：`#1a1a1a`；文字：`#ffffffe0`，14px / w600 无衬线
- 圆角：8px；padding：10px 20px（小尺寸 7px 12px）
- 悬停：背景转纯黑 `#000`，`transition: background-color .18s cubic-bezier(.4,0,.2,1), color .18s cubic-bezier(.4,0,.2,1)`
- 激活：`translateY(1px)`；禁用：24% 黑底 + 24% 黑字

**次/描边按钮**：
- 透明底 + `1px solid #1a1a1a`（浅底场景）或 `1px solid #ffffff3d`（黑底场景），文字同色级
- 圆角 8px；悬停背景 `#0000000f`（浅）/ `#ffffff1f`（深）

### 卡片

- 大卡：圆角 24px、padding 32px、min-height 530px、实色纸面（`#f5f5f5` / `#f6f6f1` 交替）、无边框；flex column + justify-between 使视觉沉底
- 横条卡：圆角 16px、`1px solid #ddddd9`、白底、padding 20px 24px、flex 两端对齐
- 悬停：`shadow-float` + `translateY(-2px)`，transition .25s cubic-bezier(.4,0,.2,1)
- 倾斜纸卡：`transform: rotate(10deg)`（或 -10°）+ `shadow-paper`，白底圆角 8–16px，顶部 macOS 窗点 `#ff5f57 #febc2e #28c840`（8px 圆点，gap 6px）

### 输入框

页面未出现表单输入框；如需扩展：白底、`1px solid #ddddd9`、圆角 8px、padding 10px 12px、16px 正文；聚焦 `border-color: #00a9ff` + `0 0 0 2px rgba(0,169,255,0.2)` 焦点环。

### 导航

固定 60px 顶栏，纸白底 + 1px `#ddddd9` 底线；logo 黑色点阵圆标 + 16px w700 无衬线 wordmark；链接 14px / w500 / 64% 黑，悬停 88% 黑，下拉 caret 8px；右端语言切换 14px。移动端收为汉堡菜单（推断）。

### 徽章/标签

- 产品后缀徽章：黑底 `#1a1a1a`、白字 12–14px w700、圆角 6px、padding 2px 8px（如 "Studio"）
- 选框手柄：8px 实心方块 `#00a9ff`，无圆角
- 制版节点：6–8px 蓝方块 + 1px 灰十字线

### 终端代码窗

深色窗：标题栏 `#2c2b30` + 窗点，体 `#0b0c0e`，圆角 16px，`shadow-paper`；代码 PT Mono 13px/1.6，语法色见 Token 表；叠放于浅色编辑器 mock 之上形成纸面叠压。

---

## "大胆要素"（签名元素）

1. **科学档案拼贴**：Hero 用绝对定位叠压 5–8 张"扫描件"（手稿、月相、粒子径迹、蝴蝶半调、公式纸），各自 `rotate(±10deg) scale(.64–.95)`，纸色互异；禁止用抽象 3D 或渐变球替代。
2. **设计工具选框**：拼贴外包 `1px solid #1a1a1a` 矩形，四角置 8px `#00a9ff` 方手柄（`position:absolute`），把插画框成"被选中的画布对象"。
3. **删除线双语旁注**：衬线 14–16px 三行组，英文行 `text-decoration: line-through`，中文行正常；散布拼贴间隙与画布角落。
4. **半调巨型数字 + 制版标记**：旗舰卡内 ~500px 半调网屏数字，墨点喷散 + 1px 十字构造线 + `rgba(0,169,255,0.35)` 半透明矩形 + 蓝色方节点。
5. **衬线标题单蓝词**：Hero 第二行整词 `color: #00a9ff`，其余全黑；全页仅此一处高饱和文字。
6. **倾斜纸质 UI 卡**：产品截图纸片化，`rotate(10deg)` + macOS 窗点 + `-5px 20px 32px rgba(0,0,0,.1)` 偏移影。
7. **黑底半调封底**：页脚纯黑 + 四角半调点阵渐隐 + 反白衬线列标题，与纸白首屏构成刊物对仗。
8. **零渐变纪律**：任何表面不得出现 gradient / backdrop-filter；深度只允许纸色微差、透明度阶梯与偏移柔影。

这些元素定义此实现并防止通用输出。

---

## 效果与动画

**运动哲学**：纸页落定般的短促入场 + 几乎不可察觉的呼吸式持续动画；悬停反馈快而轻（0.15–0.18s），入场稍缓（0.24–0.26s 或更长的一次性 enter）。无弹跳、无旋转木马式炫技。

**过渡默认**：
- 标准（颜色/背景）：`background-color .18s cubic-bezier(.4,0,.2,1), color .18s cubic-bezier(.4,0,.2,1)`
- 入场/显现：`opacity .24s cubic-bezier(.4,0,.2,1), transform .24s cubic-bezier(.4,0,.2,1)`；大入场用 `cubic-bezier(.22,1,.36,1)`
- 悬停位移：`transform .25s cubic-bezier(.4,0,.2,1)`

**持续动画**：
- `marquee-scroll`：linear infinite，横向跑马灯（合作机构/模型名条）
- `sound-bar`：scaleY 0.28→0.58→0.28→0.16 循环，语音 demo 的声纹条
- `wave-breathe`：translateY 0→-7→-2→-10px 循环，波形呼吸
- `spin`：360° 旋转，加载态

**关键帧动画**：
```css
@keyframes home-content-enter {
  0%   { opacity: 0; translate: 0 var(--home-enter-y, 12px); scale: var(--home-enter-scale, .98); }
  100% { opacity: var(--home-enter-opacity, 1); translate: 0; scale: 1; }
}
@keyframes marquee-scroll {
  0%   { transform: translate(0); }
  100% { transform: translate(calc(-100% + var(--marquee-container-width))); }
}
@keyframes sound-bar {
  0%, 100% { transform: scaleY(.28); }
  25%      { transform: scaleY(.58); }
  50%      { transform: scaleY(.28); }
  75%      { transform: scaleY(.16); }
}
@keyframes wave-breathe {
  0%, 100% { transform: translateY(0); }
  25%      { transform: translateY(-7px); }
  50%      { transform: translateY(-2px); }
  75%      { transform: translateY(-10px); }
}
```

入场位移控制在 2–12px、缩放 0.98–1 级别；IntersectionObserver 触发；`prefers-reduced-motion: reduce` 时全部持续动画停摆、入场直给终态。

---

## 响应式策略

**断点哲学**：容器内边距逐级收缩而非重排结构；拼贴装饰在窄屏隐藏，网格降列，标题降档。

- **容器**：≥1280px padding 120px；1024–1280px padding 32px；768–1024px padding 24px；<768px padding 20px
- **Nav**：链接收进汉堡菜单，保留 logo 与语言切换
- **Hero**：拼贴与选框在 <640px 隐藏（源站 `sm:hidden`），标题降为 36–40px，旁注隐藏
- **模型网格**：2 列 → <768px 1 列；旗舰卡左文右图 → 上下堆叠，半调数字缩至 ~260px
- **产品三联卡**：3 列 → 1 列；倾斜纸卡旋转角减半
- **Footer**：4 列导航 → <640px 2 列（`grid-cols-2 sm:grid-cols-4`）

**关键适配**：
- 标题阶梯 56/54/48 → 40/38/34 → 32/30/28，负字距按比例保留
- 区块 padding 50px → 32px；卡内边距 32px → 24px
- 绝对定位装饰（拼贴、构造线、半调角饰）窄屏 `display:none`，不留占位

---

## 可访问性与最佳实践

**色彩对比**：88% 黑于纸白 ≈ 15:1，64% 黑 ≈ 7:1，均达 AAA/AA；48% 黑仅用于 ≥14px 辅助文字（约 4.6:1，达 AA）。信号蓝 `#00a9ff` 于白底仅 ≈ 2.6:1——**只允许用于 ≥24px 展示文字、图形标记与焦点环**，不得用于正文或小字链接。

**聚焦状态**：`outline: 2px solid #00a9ff; outline-offset: 2px`；深色区块改用 `#ffffffe0` 环。

**触控目标**：按钮最小高度 36px（桌面）/ 44px（移动端）；导航链接 padding 补足 44px 命中区。

**运动**：`@media (prefers-reduced-motion: reduce)` 关闭 marquee / sound-bar / wave-breathe / enter 位移，仅保留颜色过渡。

---

## 实现说明

- **组件结构**：单文件 HTML + 原生 CSS 即可还原；`:root` 落地全部 Token，组件只引用变量。区块顺序：nav → hero(canvas) → flagship card → weights bar → model grid → business cards → footer。
- **CSS 自定义属性**：照抄 Token 表命名（`--color-paper-white`、`--color-signal-blue`、`--text-primary`…）；黑底区块用 `--text-primary-light` 等反白阶梯局部覆盖。
- **字体加载**：Google Fonts `Lora:wght@500;600;700`、`Inter:wght@400;600`、`PT+Mono:wght@400;700`、`Noto+Serif+SC:wght@600`、`Noto+Sans+SC:wght@400;500;700`；`font-synthesis: none` + `text-rendering: optimizeLegibility` + 抗锯齿。
- **图像策略**：拼贴扫描件与半调数字可用生成图（复古手稿/月相/粒子径迹/蝴蝶网屏，纸白底）或 SVG 半调图案（`<pattern>` 圆点阵 + mask 渐隐）实现；禁止占位图与渐变球。
- **动画库**：无需第三方库；IntersectionObserver + 上述 keyframes 足够；跑马灯用 CSS 变量 `--marquee-container-width` 控制位移终点。
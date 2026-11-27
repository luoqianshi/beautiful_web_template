# Lime-Atlas-Isometric

> 来源：https://www.aoci.ai/ （风格逆向注记；示例文案与名称均为测试数据，产品名统一使用 Demo 前缀演示名）

## 基本信息

| 属性 | 值 |
|------|-----|
| 风格ID | `lime-atlas-isometric` |
| 显示名称 | Lime Atlas Isometric |
| 模式 | Dark 为主，Light 完整翻转 |
| 字体类型 | sans-serif + mono 双轨 |
| 描述 | 石墨绿黑基底上的酸性青柠工程美学：等距认知地图 SVG 动图、青柠信号包沿贝塞尔轨道流动、FRAS 语义翻页与可点选模块，克制而精密的开发者基础设施气质。 |

## 布局创意 (Layout Ideas)

### Header（固定顶栏）

通栏固定，高约 64px，背景 `rgb(11 16 15 / .95)` 近不透明石墨绿黑，底部 1px `--line` 细线。左侧方形青柠 logo + 等宽大写品牌字；中部导航链接 13px，当前区块加粗高亮；右侧功能簇：EN 语言胶囊、主题切换圆钮、GitHub 链接、青柠主 CTA（圆角 8px）与描边登录胶囊。滚动时保持固定，锚点跳转预留顶栏高度。

### Hero（签名区块：等距认知地图动图）

非对称双栏：左侧 55% 文案区（标题两行，第二行青柠色；18px 副文案；主/次按钮行），右侧 56% 宽绝对定位 SVG 舞台（向右出血 -3%），`mask-image: linear-gradient(to right, transparent, black 5%, black 96%, transparent)` 让地图左右边缘溶入背景。地图为 1536×1024 viewBox 的等距轴测场景：六块有机圆角"岛屿"平台（CODE / API / DB / TEST / CONFIG / 中央全书），灰阶石墨质感，白色粗缆线互联，青柠节点椭圆点缀；六张悬浮图标卡片独立浮动；五条信号轨道上有光包+彗尾循环流动；中央书本上方 F/R/A/S 四张语义标签页每 1.6s 轮换。左下角 11px 提示文案，右下角"暂停动画"控制钮。底部紧贴四列产品事实条（青柠大写等宽标签 + 灰色短语），以 1px 横线分隔。

### Agent 接入条

事实条下方一行：左侧"接入你已经在用的 Agent"小字，中部若干灰度 Agent 名称（等宽/无衬线混排），右侧"标准 stdio MCP ↗"小链接。低对比、单行、不抢焦。

### Benefits（2×2 卡片网格）

区块标题两行大字左对齐（clamp 32-44px，字重 650，字距 -.03em），下方 16px 灰色导语。2×2 卡片：`--surface` 底、1px `--line` 边框、16px 圆角、无阴影；左上角 20px 线性图标，18px 标题，14px 灰正文，底部"流程链"小字（A → B → C，中间项青柠加粗）。卡片悬停边框微亮。

### Quick Start（双栏：步骤轨 + 代码面板）

标题两行（第二行灰色降级）。左栏：胶囊分段控件（交给 Agent / 手动接入，选中项 `--surface-alt` 底）+ 三步步骤轨（选中步 `--lime-soft` 底 + 青柠左边框 + 编号圆点，滑动标记块跟随）；右栏：代码面板（`--code` 底、1px 边框、12px 圆角），面板头"发送给 AI Agent + 标题 + 复制按钮"，正文 13px 等宽多行文本。复制成功 toast 提示。

### Workflow（场景 Tab + 时间线）

三个场景 Tab（接手已有项目 / 从新项目开始 / 新会话召回认知）。主面板 `--surface` 大卡：左侧标题+导语+分隔线+"试着对 Agent 说"引用块+复制钮；右侧垂直时间线四步（青柠实心圆点已完成、空心圆点待办，竖直连线，当前步标题青柠）。滚动驱动进度：时间线随滚动逐步点亮。下方两个补充小卡（数据库认知 / 本机面板命令行）。

### Live Demo（交互认知图 + FRAS 详情栏）

区块标题 + 导语。大面板分两栏：左 70% 图区（顶部过滤 Tab：全景 / Code / Database；780×440 相对定位画布，五个节点卡片绝对定位 + 中央核心卡，SVG 贝塞尔连线，选中关系的连线以青柠/青色 dash 信号动画描边；底部图例），右 30% 详情栏（对象名 + 类型徽章，F/R/A/S 四段定义列表，变更对照 code 块）。面板头右侧"模拟一次变更"按钮触发四阶段状态机（stale→maintaining→checking→aligned），阶段胶囊条 + 状态 pill + 重置钮。

### Comparison（左文案 + 右三层堆叠卡）

左栏标题两行 + 导语 + 文字链接；右栏三张纵向堆叠文章卡，每张"角色名：问句"加粗 + 灰色解答，边框分隔。

### FAQ（左标题 + 右 details 列表）

左栏两行大标题 + 青柠文字链接；右栏五条 `<details>`，summary 14px 加粗 + 右箭头图标，展开正文 14px 灰色，1px 底线分隔。

### Principles（架构层叠 + 语义网格）

标题两行 + 导语。左栏垂直四层架构 stack（大模型 / AI Agent / 本产品层青柠高亮 / 软件系统），右栏两篇文章 + 治理流程链（四个 span 胶囊）。下方三个 details：卷宗网格（4 列 code 文件名卡）、四类语义网格（F/R/A/S 四色块）、交付治理说明。

### Closing CTA

居中大字两行 + 青柠主按钮 + 一行灰色英文小字标语（重写为原创示例）。上下 1px 横线夹持，大量留白。

### Footer

左侧品牌矩形 logo 块，右侧四个文字链接；底栏左产品全称、右"内容依据官方文档，日期更新"小字（测试数据）。1px 顶线。

---

## 完整提示词 (Full Prompt)

# 设计风格：Lime Atlas Isometric

## 设计哲学

### 核心原则

这是一套"工程基础设施"气质的深色设计系统：把抽象的系统认知画成一张可以点选、可以暂停、可以观察数据流动的等距地图。信息密度克制，层级靠字重与灰阶而非色块；唯一的饱和色——酸性青柠——只留给"活跃的认知信号"：主 CTA、当前状态、流动的光包、选中的关系。设计相信"图即文档"：每个装饰元素都承担解释职责，没有纯装饰的渐变 blob 或光晕。

### 视觉气质

**情感关键词**：
- *精密仪器感* — 等距轴测、细线、等宽标签，像示波器与工程图纸
- *酸性生机* — 石墨绿黑中唯一的青柠绿，是数据在流动的证据
- *冷静的权威* — 大标题字重 650、负字距、慷慨行高，不喊叫
- *可触碰的系统* — 地图模块可点选、动画可暂停、演示可重置

**此设计不是什么**：
- 不是霓虹赛博朋克（无紫粉、无辉光溢出、无故障艺术）
- 不是玻璃拟态（无毛玻璃卡片，顶栏仅近不透明纯色）
- 不是营销糖果色（无大面积渐变、无插画吉祥物）
- 不是极简白底 SaaS（深色是默认人格，浅色是完整翻转而非附庸）

### 此风格的 DNA

#### 1. 等距认知地图 Hero（核心签名）
1536×1024 的轴测 SVG 场景：六块多层堆叠的有机岛屿平台承载灰阶等距小道具（服务器堆栈、文档卡、代码瓦片、数据库圆柱、齿轮、清单），白色粗缆线 + 青柠节点椭圆互联，虚线辅助曲线补充关系。中央一本摊开的"全书"，上方 F/R/A/S 标签页轮换。

#### 2. 贝塞尔信号包动画
五条轨道（code/api/database/test/config）上，光包（halo r15 + body r7 + core r2.8 三层圆）沿三次贝塞尔曲线匀速流动，拖三节彗尾（r5.4/4.2/3，相位差 .055/.11/.165），出发端椭圆环呼吸、到达端椭圆脉冲放大 1.32 倍，轨道透明度随相位正弦呼吸 .17→.50。

#### 3. 悬浮图标卡片
六张圆角方形图标瓦片（{}、git 分支、插头、盾勾、数据库、滑杆）以 clipPath 从地图中"揭起"，各自以 2.8–3.8s sine.inOut 上下浮动 ±4-5px、横移 ±4-5px、微旋 ±1.4–1.8°，相位错开 index/7。

#### 4. 青柠单一强调色纪律
全站唯一饱和色 `#b6d94b`（暗）/`#516f0d`（亮），只出现在：主按钮、当前导航、状态 pill、信号包、选中边框、流程链中间项。辅助色青色 `#88d4d8` 仅用于数据库语义，琥珀 `#e7bd83` 仅用于"待同步/变更中"警示态。

#### 5. FRAS 四段语义详情
对象详情永远按 F 职责 / R 强关系 / A 接口 / S 关键约束四段展开，字母用青柠等宽加粗，定义列表灰字。这是信息架构签名，不止是视觉。

#### 6. 可暂停的尊重
动画区右下角常驻"暂停动画"钮；IntersectionObserver 离屏即停、页面隐藏即停、`prefers-reduced-motion` 直接降级为静态地图。动效是渐进增强，内容默认可见。

---

## 设计 Token 系统（DNA）

### 色彩策略

**色彩聚焦**：石墨绿黑家族（背景带 2-3° 绿相）承载 95% 面积，酸性青柠作为唯一信号色，青/琥珀仅作语义辅助。所有灰阶都带绿相，禁止纯中性灰。

| Token | 暗色值 | 亮色值 | 用法与上下文 |
|:------|:------|:------|:----------------|
| `--page` | `#0b100f` | `#f3f6f0` | 页面基底 |
| `--surface` | `#111917` | `#fcfdf9` | 卡片/面板/次按钮底 |
| `--surface-alt` | `#17221f` | `#e6eddf` | 分段控件选中、表头 |
| `--text` | `#eef3ef` | `#172519` | 主文字/标题 |
| `--muted` | `#a6b5ad` | `#4c6150` | 正文灰 |
| `--quiet` | `#899b90` | `#536955` | 弱提示/图例 |
| `--line` | `#2b3831` | `#c8d4c2` | 1px 边框/分隔线 |
| `--lime` | `#b6d94b` | `#516f0d` | 主强调/CTA/信号 |
| `--lime-ink` | `#17210b` | `#f4f8ec` | 青柠底上的文字 |
| `--lime-soft` | `#202d12` | `#e3edcf` | 选中态薄底 |
| `--cyan` | `#88d4d8` | `#216a73` | 数据库语义 |
| `--cyan-soft` | `#142b2d` | `#deedf0` | 数据库薄底 |
| `--amber` | `#e7bd83` | `#86571a` | 变更/待同步警示 |
| `--amber-soft` | `#2a2319` | `#eee5d6` | 警示薄底 |
| `--header` | `rgb(11 16 15 / .95)` | `rgb(243 246 240 / .96)` | 固定顶栏 |
| `--code` | `#101714` | `#e6eddc` | 代码块底 |
| `--map-energy` | `#97e56a` | `#5aa62e` | 地图信号包专用绿（比 lime 更亮） |
| `--map-energy-ink` | `#193617` | `#12310d` | 信号核心深色 |
| `--map-energy-edge` | `#edfce4` | `#e5ffd1` | 信号描边/核心亮边 |

**签名渐变**（仅用于地图边缘溶接，非装饰渐变）：
```css
mask-image: linear-gradient(to right, transparent, black 5%, black 96%, transparent);
```

### 字体系统

**字体配对**：
- **UI/标题字体**：`Sora, system-ui, -apple-system, "Segoe UI", "Noto Sans SC", "PingFang SC", "Microsoft YaHei", sans-serif` — 几何无衬线，标题字重 650
- **等宽字体**：`"Cascadia Code", "SF Mono", Consolas, Monaco, monospace` — 品牌字、代码、状态 pill、节点文件名、事实条标签

**字号阶梯与用法**：

| 元素 | 尺寸 | 字体 | 字重 | 字距 | 备注 |
|:--------|:-----|:-----|:-------|:---------|:------|
| Hero 标题 | clamp(34px, 3.3vw, 50px) | sans | 650 | -.035em | 行高 1.36，第二行青柠 .92em |
| 区块标题 | clamp(30px, 3vw, 42px) | sans | 650 | -.03em | 两行，行高 1.3 |
| 卡片标题 | 18px | sans | 600 | 0 | |
| 正文 | 16-18px | sans | 400 | 0 | Hero 副文案 18px/1.9 |
| 弱正文 | 14px | sans | 400 | 0 | 卡片正文/FAQ |
| 标签/图例 | 10-11px | mono/sans | 500 | .02em | 事实条标签大写 |
| 代码 | 13px | mono | 400 | 0 | 行高 1.7 |
| 状态 pill | 11px | mono | 400 | 0 | padding 4px 9px |

### 间距与布局

- **区块间距**：section 垂直 padding 96-120px；Hero min-height 680px
- **容器宽度**：`.wrap` max-width 1200px，左右 padding 24px
- **网格间隙**：卡片网格 gap 24px；事实条四列等分以 1px 竖线分隔
- **非对称模式**：Hero 文案 55% / 地图 56%（右出血 -3%）；Demo 图区 70% / 详情 30%；Quick Start 步骤 38% / 代码 62%

**常见间距值**：4 / 8 / 12 / 14 / 20 / 24 / 32 / 48 / 72 / 96px。

### 边框、表面与阴影

**圆角策略**：按钮 8px；卡片/面板 12-16px；节点卡 10px；分段控件外框 10px 内项 7px；pill 999px；图标瓦片 10px。

**边框**：一律 1px solid `--line`；选中态换 `--lime` 或 `color-mix(in srgb, var(--lime) 50%, transparent)`；聚焦态虚线 `stroke-dasharray: 9 6`（SVG）或 2px outline（HTML）。

**阴影系统**：几乎无阴影——深色靠边框与底色分层。仅浮层：

| Token | 值 | 用法 |
|:------|:------|:------|
| `--shadow-pop` | `0 12px 32px -12px rgb(0 0 0 / .5)` | toast/对话框 |
| `--shadow-none` | `none` | 卡片默认 |

**纹理与图案**：无噪点无点阵；地图岛屿自带多层堆叠轮廓线即纹理。

---

## 组件样式与交互

### 按钮

**主按钮**：背景 `--lime`，文字 `--lime-ink`，圆角 8px，padding 14px 23px，字号 14px 字重 650，inline-flex gap 12px 带箭头图标；悬停 `translateY(-2px)` + 背景 `color-mix(in srgb, var(--lime) 88%, var(--text))`；激活 `translateY(1px)`；过渡 .25s。

**次按钮**：1px `--line` 边框，`--surface` 底，`--text` 字；悬停边框变 `--quiet`。

**文字按钮/链接**：青柠色 13px，带 ↗ 小图标，悬停下划线。

**小按钮**：12px 字，padding 10px 15px。

### 卡片

`--surface` 底 + 1px `--line` + 16px 圆角 + 无阴影；padding 28-32px；悬停边框 `color-mix(in srgb, var(--line) 60%, var(--quiet))`。流程链底部小字：灰 → 青柠加粗 → 灰，箭头 12px。

### 输入框/代码面板

代码面板 `--code` 底、1px `--line`、12px 圆角；面板头 padding 16px 20px 带底边框；正文 mono 13px/1.7，padding 20px；复制按钮右上角小描边钮，成功变"已复制"2.2s。

### 导航

固定顶栏 64px；链接 13px `--muted`，当前项 `--text` 加粗；右侧 EN 胶囊（1px 边框 999px）、主题圆钮 36px、GitHub 图标+字、主 CTA 小按钮。移动端折叠为汉堡菜单抽屉。

### 徽章/标签

状态 pill：mono 11px，`--lime-soft` 底 `--lime` 字，圆角 5px，padding 4px 9px；pending 态换琥珀对。类型徽章（Code Cognition / Database Cognition）：11px 青/青色。事实条标签：mono 13px 大写青柠 + 字距 .04em。

### 分段控件（Tabs）

外框 1px `--line` 圆角 10px padding 4px；项 padding 8px 16px 圆角 7px 字号 13px；选中 `--surface-alt` 底 `--text` 字；未选 `--quiet`。

### 步骤轨

垂直三步；编号圆点 24px（选中青柠底深字，未选 1px 边框灰字）；选中步整块 `--lime-soft` 底 + 青柠左边框 3px + 10px 圆角；滑动标记块 absolute 跟随（.3s power3.out）。

### 时间线

垂直四步；圆点 12px 实心青柠（已完成）/空心 1px 边框（待办）；连线 2px `--line`，已走过段青柠；当前步标题青柠。

---

## "大胆要素"（签名元素）

1. **等距认知地图 Hero**：纯 SVG 轴测场景替代插画位图——六块多层岛屿 + 等距道具 + 白色缆线 + 青柠节点，可点选、可暂停、可降级静态。
2. **贝塞尔信号包 + 彗尾**：三层圆光包沿 `mapPoint(t, curve)` 三次贝塞尔插值流动，三节尾巴相位滞后，到达端 sin 脉冲，轨道透明度正弦呼吸——全部由单一 rAF 时钟驱动。
3. **悬浮瓦片微动**：六张图标卡 sine.inOut 浮动（dx/dy/roll/duration 各自独立，相位 index/7 错开），`svgOrigin` 钉在瓦片中心防止旋转漂移。
4. **FRAS 标签页轮换**：中央书本上 F/R/A/S 四张平行四边形标签 6.4s 循环，每张淡入 .22s 停留 1s 淡出 .28s。
5. **模块点选反馈**：点击岛屿 hit area → 该轨道加粗（rail 4→6、ring 2.6→4.5）、hint 文案变"CODE → 全景索引"、该路由与 FRAS 时间线重启；focus-visible 虚线描边。
6. **dash 信号描边**：交互演示图选中关系时，复制路径到 signal 层，`strokeDasharray: 18 L`、offset L→-L 扫过 .95s，多条错开 .055s。
7. **四阶段状态机演示**：stale→maintaining→checking→aligned，单一可控时钟（1.8s/步），暂停/恢复/重置完整，受影响节点琥珀高亮。
8. **青柠纪律**：全站唯一饱和强调色，语义辅助色（青/琥珀）各守其职，深灰阶全带绿相。

---

## 效果与动画

**运动哲学**：一切动画都是"数据在流动"的隐喻——匀速、正弦、可暂停；入场短促克制（5-11px 位移），无弹跳无旋转炫技。GSAP 式编排但可用 vanilla rAF 完整复刻；内容默认可见，动画是渐进增强。

**过渡默认**：
- 标准：`transform .25s, background .25s, border-color .25s`
- 入场：`y: 7→0, opacity: .76→1, .26s power3.out`（IntersectionObserver 触发，once）
- Hero 入场序列：地图 opacity .75→1 .85s @0；h1 y11→0 .7s @.06；p y8→0 .55s @.2；actions y5→0 .45s @.32（power3.out）
- 悬停：按钮 translateY(-2px)；卡片边框微亮

**持续动画**：
- 信号包：duration 2.55/2.85/2.7/3.05/3.2s，ease none，repeat ∞，初始相位 .1/.42/.7/.25/.58
- 彗尾：tail 滞后 .055/.11/.165，强度 1/.62/.46/.30，透明度 ramp `min(t/.06, (1-t)/.06)`
- 到达脉冲：`t>.76` 时 `sin((t-.76)/.24*π)`，opacity×.95，scale 1→1.32
- 轨道呼吸：opacity `.17 + .33*sin(π*t)`
- 悬浮瓦片：2.8/3.5/3.1/3.7/2.9/3.8s sine.inOut yoyo，x ±dx、y 8→dy、rotation ±roll
- FRAS：6.4s 循环，每字母 1.6s 窗口（.22 入 / 1.0 留 / .28 出）

**关键帧动画**（CSS 备用）：
```css
@keyframes hero-enter { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: none; } }
@keyframes dash-signal { to { stroke-dashoffset: var(--dash-end); } }
```

**暂停纪律**：`sceneUserPaused || !sceneVisible || document.hidden || reduce.matches` 任一为真即暂停全部 tween；`data-motion="running|paused|reduced|static"` 标注舞台状态。

---

## 响应式策略

**断点哲学**：1024px 收紧双栏，768px 以下 Hero 变垂直堆叠（文案在上、地图在下全宽），地图保持 3:2 比例。

- **Hero**：≤768px 时 `hero-art` 变 relative 全宽 order:2，`hero-map` aspect-ratio 3/2；标题 clamp(27px, 5.8vw, 42px)；按钮缩小 padding 13px 17px
- **事实条**：四列 → 两列 → 单列
- **Benefits**：2×2 → 单列
- **Quick Start / Demo / Comparison / FAQ**：双栏 → 单列，详情栏移到图区下方
- **顶栏**：≤900px 隐藏中部导航，汉堡抽屉

**关键适配**：
- 标题 clamp() 连续缩放，负字距移动端收至 -.03em
- 区块 padding 96→64→48px
- 地图 hint 与暂停钮在移动端收到底部 3px，字号 10px
- 图例小字移动端隐藏或换行

---

## 可访问性与最佳实践

**色彩对比**：`--text` on `--page` ≈ 15:1；`--muted` on `--page` ≈ 7:1；`--lime-ink` on `--lime` ≈ 9:1；`--quiet` 仅用于 ≥11px 辅助信息（≈4.6:1）。

**聚焦状态**：HTML 控件 `outline: 2px solid var(--lime); outline-offset: 2px`；SVG hit area `stroke-opacity:1; stroke-dasharray:9 6`。

**触控目标**：按钮/导航/暂停钮 min-height 44px；hit area 为整个岛屿多边形（远大于 44px）。

**运动**：`prefers-reduced-motion: reduce` → 地图显示静态 `map-original` 层、隐藏暂停钮、入场动画关闭、信号 dash 直接呈现终态；`aria-live="polite"` 播报 hint 与状态变化；hit area `role="button" tabindex="0" aria-pressed` 支持 Enter/Space。

---

## 实现说明

- **组件结构**：单文件零构建 HTML；`:root` Token 层 + `html[data-theme="light"]` 完整翻转；所有组件只引用变量。
- **CSS 自定义属性**：色彩/圆角/字体/动效时长全部 Token 化；地图专用 `--map-energy*` 三变量独立于 UI 青柠。
- **字体加载**：系统字体栈零外链（Sora 可选 Google Fonts，回退 system-ui；等宽 Cascadia Code/Consolas 本地回退）。
- **动画库**：推荐 GSAP + ScrollTrigger（源站方案）；vanilla rAF 可完整复刻——单一时钟对象驱动所有相位，`quickSetter` 式批量 transform 写入；IntersectionObserver 管离屏暂停与入场。
- **地图 SVG**：viewBox 1536×1024；岛屿用多层 `<path>` 堆叠（3 层偏移 6-10px）；缆线 stroke 8-10 圆帽；节点椭圆 rx21 ry11（等距透视）；hit area 为透明六边形 path。
- **合规**：示例文案与名称均为测试数据；产品名用 Demo 前缀（如 Demo-Atlas）；页脚资质行统一 `测试备案号 00000000000000`。
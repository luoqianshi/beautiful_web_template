# Jelly-Bot-Teammates

> 来源：https://x.ai/bot （仅作风格来源注记；示例文案与名称均为测试数据）

## 基本信息

| 属性 | 值 |
|------|-----|
| 风格ID | `Jelly-Bot-Teammates` |
| 显示名称 | Jelly Bot Teammates |
| 模式 | Light 为主，支持 Dark 翻转 |
| 字体类型 | sans-serif（系统无衬线栈） |
| 描述 | 极简白底 + 黑色药丸按钮 + 多彩果冻 Bot 头像的 AI 队友落地页：活体聊天演示、摇摆跑马灯、Agent 光标动画与手机任务演示，动效全套保留。 |

## 布局创意 (Layout Ideas)

### Header
固定顶栏 64px，白色 85% 透明 + 12px 毛玻璃。左侧斜切线条 Logo，中部带下拉箭头的导航链接（14px/500），右侧灰底药丸次按钮 + 黑底药丸主按钮（主按钮可带分体下拉段）。

### Hero
居中单列：shimmer 公告药丸（小字 + 圆形箭头钮）→ 60px 大标题（标题词间内嵌一枚黑色果冻头像，与文字基线对齐）→ 灰色副文案（18px，最大 672px）→ 黑/灰双药丸 CTA → 下方 784px 宽聊天应用大 mockup（rounded-24px，细边框 + 弥散阴影）。Mockup 含 macOS 红黄绿窗控、左侧 Bot 侧栏（3 枚大果冻瓦片 + 3 行小头像列表）、右侧**自动播放的聊天剧场**：Bot 灰泡入场 → typing 三点 → 用户黑泡落底 → 爱心 reaction 弹出 → 审批卡（Schedule it / Edit first）。这是全页的签名动效，必须真实循环播放。

### Statement + Marquee
左 36px 标题 / 右两段灰正文的非对称双栏；下方通栏**果冻头像跑马灯**：9-10 枚不同色不同形的 blob（圆团、斜方、三叶草），无缝 translateX(-50%) 循环，每枚自带 ±6° 摇摆。

### Video
16:9 深靛紫渐变面板（rounded-24px），底部升起行星弧线，左中白色 ▶ Play。点击后面板内播放动画演示（而非静态图）。

### Features
居中 36px 标题 + 灰副文案，2×3 象牙白卡片网格（rounded-24px、32px 内边距、无边框）。每卡 = 20px 标题 + 14px 灰描述 + **一个活的迷你产品演示**：清单逐行打勾、浏览器内 Agent 光标游走点击、录制红框 + 计时器 + 柱状图生长、会议九宫格说话环、Slack 线程逐行滑入、薰衣草记忆面板弹出建议卡。

### Use Cases（Give each Bot a job）
左列 8 枚任务药丸 Tab（选中项染对应 Bot 色浅底），下方随 Tab 切换的描述段 + 灰药丸按钮；右列 iPhone mockup（黑色圆角边框 + 灵动岛），屏内聊天内容随 Tab fadeSlideUp 切换。

### Pricing
居中标题 + 灰药丸 + Individual/Teams 分段切换器；三列象牙卡（名称、48px 价格、黑药丸 CTA、勾选清单）；底部一条资格横幅卡。

### Download / Guides / FAQs / Get Started / Footer
Download：左标题右两条下载行卡。Guides：三张**双色劈分头图**卡（左亮色块白眼睛 + 右深色块白标题），下方类别小字 + 描述。FAQs：左 sticky 大标题，右手风琴（+ 旋转成 ×，高度过渡）。Get Started：居中 CTA + 页脚上方**巨型描边果冻脸**装饰（缓慢漂浮）。Footer：Logo + 多列链接 + 深色模式月亮钮 + "Built with …" 药丸 + 测试备案号行。

---

## 完整提示词 (Full Prompt)

# 设计风格：Jelly-Bot-Teammates

## 设计哲学

### 核心原则
把"AI 同事"当成有性格的角色来展示：页面本体极度克制（纯白、黑字、灰阶、药丸），所有色彩与生命力集中在**果冻 Bot 角色**与**会动的产品演示**上。克制的是画布，热闹的是角色。用户看到的不是功能截图，而是一群正在干活的彩色小家伙。

### 视觉气质
**情感关键词**：
- *Playful-professional* — 企业级留白与排版，玩具级角色与动效
- *Alive* — 每个演示区块都在自己循环干活：打字、打勾、游标、生长
- *Soft-candy* — 高饱和糖果色只出现在 blob 上，边缘全部圆润

**此设计不是什么**：
- 不是暗色科技风/霓虹赛博；不是渐变玻璃拟态
- 不是静态截图堆砌的功能列表；不是大号彩色标题党

### 此风格的 DNA
1. **果冻 Bot 头像**：有机 blob 形 + 两枚倾斜白色药丸眼睛；一枚角色一个品牌色；出现在标题内嵌、侧栏、跑马灯、会议格、巨型描边装饰中。
2. **活体聊天剧场**：Hero mockup 内的消息按剧本循环入场（typing → land → reaction → 审批卡），是全页第一签名。
3. **黑药丸 × 象牙卡**：CTA 一律纯黑全圆角药丸；内容卡一律象牙白 rounded-24 无边框。
4. **每卡一演示**：Features 六卡各嵌一个 CSS/JS 循环动画演示，拒绝静态图。
5. **双色劈分 Guide 头图**：亮色块（白眼睛）+ 同族深色块（白字）左右劈分。
6. **巨型描边果冻脸**：页脚前一只仅 1px 描边的超大 blob 脸，缓慢漂浮。

---

## 设计 Token 系统（DNA）

### 色彩策略
**色彩聚焦**：画布只用白/象牙/灰阶；彩色全部来自 9 色 Bot 家族（每色取自同一饱和度量级的品牌阶）。

| Token | 值 | 用法与上下文 |
|:------|:------|:----------------|
| `--bg` | `#ffffff` | 页面底色 |
| `--card` | `#f9f8f5` | 象牙白卡片/次按钮底（源 hsl 40 18% 97%） |
| `--fg` | `#0a0a0a` | 标题/黑药丸/用户气泡 |
| `--muted` | `#7d8187` | 副文案、次级文字 |
| `--border` | `#d5d9e2` | 1px 细边框、滚动条 thumb |
| `--surface-2` | `#f1f2f6` | Bot 灰泡、输入底 |
| `--bot-teal` | `#2cb663` | Launch Bot |
| `--bot-indigo` | `#6c6ccb` | Inbox Bot |
| `--bot-violet` | `#8f8deb` | Data Bot |
| `--bot-blue` | `#2da0f5` | Sales/新讯 Bot |
| `--bot-orange` | `#fe733d` | 报销 Bot |
| `--bot-green` | `#6dd998` | 幕僚 Bot |
| `--bot-red` | `#fd5c6a` | 跑马灯/Guide 亮块 |
| `--bot-amber` | `#f8b956` | 跑马灯 |
| `--bot-magenta` | `#e76cb8` | 跑马灯 |
| `--bot-brown` | `#936439` | 跑马灯 |
| `--success` | `#21c45d` | 打勾/完成 |
| `--warning` | `#e7b008` | Working 徽章 |
| `--error` | `#ef4343` | 录制红点/红框 |
| `--info` | `#9cc4e4` | @提及链接 |
| `--night` | `#150a2e` → `#4c3a9e` | Video 面板渐变 |

**签名渐变**（仅 Video 面板）：
```css
background: linear-gradient(180deg, #0b0620 0%, #241a52 55%, #4c3a9e 100%);
```

### 字体系统
**字体配对**：展示与 UI 同为系统无衬线栈 `system-ui, -apple-system, "Segoe UI", "Helvetica Neue", Arial, sans-serif`；等宽 `ui-monospace, "SF Mono", Consolas` 仅用于时间戳/计时器。

| 元素 | 尺寸 | 字重 | 字距 | 备注 |
|:--------|:-----|:-------|:---------|:------|
| Hero 标题 | 60px/1.0 | 500 | -0.6px | 内嵌 blob 与文字同高 |
| 区块标题 | 36px/40px | 500 | -0.36px | 居中或左置 |
| 价格数字 | 48px/1.0 | 500 | -0.48px | |
| 卡片标题 | 20px/28px | 500 | -0.2px | |
| 正文 | 16-18px/1.6 | 400 | normal | 灰色 #7d8187 |
| 演示内文字 | 12-13px/1.4 | 400-600 | -0.05px | mockup 专用小阶梯 |
| 药丸/标签 | 13-14px | 500 | -0.08px | |

### 间距与布局
- 区块垂直间距 96-128px；Hero 顶垫 148px
- 容器：内容 1024px，外层 1280px，左右垫 24px
- 卡片网格 gap 24px；Features 卡内边距 32px
- 非对称模式：Statement/FAQ 左标题右内容约 1:2

### 边框、表面与阴影
**圆角策略**：药丸 9999px；大卡/mockup 24px；中卡 16px；小元件 8-12px；窗控点 50%。
**边框**：一律 1px solid `#d5d9e2` 或 `rgba(10,10,10,.06)`；象牙卡无边框。

| Token | 值 | 用法 |
|:------|:------|:------|
| `--shadow-window` | `0 16px 48px -8px rgba(0,0,0,.22)` | Hero 大 mockup |
| `--shadow-card` | `0 10px 15px -3px rgba(0,0,0,.1), 0 4px 6px -4px rgba(0,0,0,.1)` | 浮层卡 |
| `--shadow-pill` | `0 0 0 .5px rgba(10,10,10,.07), 0 1px 2px rgba(0,0,0,.06), 0 3px 10px rgba(0,0,0,.05)` | 白药丸/输入 |

---

## 组件样式与交互

### 按钮
- **主**：`#0a0a0a` 底白字，9999px，padding 10px 18px，hover 变 `#1c1e22`，0.14s spring
- **次**：`#f1f2f6`/象牙底黑字同形；hover 加深至 `#d5d9e2`
- **描边**：白底 + 1px `#d5d9e2` + pill 阴影；**禁用**：40% 透明
- 分体主按钮：主段 + 1px 白色分隔 + 下拉段（左右各半圆角）

### 卡片 / 输入 / 徽章 / 导航
- 象牙卡 rounded-24 无边框；浮层白卡 rounded-16 + 细边框 + 弥散阴影
- 输入：白底 rounded-full 细边框，focus 出 2px 黑环；mockup 输入含 + 与麦克风圆钮
- 徽章：Bot 色 12% 浅底 + 同色字 + 小圆点；Working 用琥珀
- 导航固定 + 毛玻璃；链接 hover 由灰转黑

---

## "大胆要素"（签名元素）

1. **聊天剧场状态机**：setTimeout 剧本循环（typing→land→reaction→审批→receipt），可被 prefers-reduced-motion 降级为全量静态。
2. **果冻摇摆跑马灯**：双份列表 translateX(-50%) 无缝循环 + 每 blob 独立 wobble。
3. **Agent 光标**：mockup 浏览器内一枚带名签的光标沿 8 站 keyframes 游走并触发点击高亮。
4. **柱状图 barGrow + 录制计时**：scaleY(0→1) 逐根生长，红点 pulse + 秒表递增。
5. **双色劈分 Guide 头图** 与 **巨型描边果冻脸**。
6. **标题内嵌角色**：H1 文字中间夹一枚会眨眼的黑 blob。

---

## 效果与动画

**运动哲学**：小而快、软而弹。位移 2-8px 级别，时长 0.12-0.3s，弹簧缓动 `cubic-bezier(.25,1,.5,1)`；持续动画（跑马灯/光标/打字）慢速循环制造"有人在干活"感。

**关键帧**（全部落地）：
```css
@keyframes marquee { to { transform: translateX(-50%); } }
@keyframes wobble { 0%,100%{transform:rotate(-5deg)} 50%{transform:rotate(6deg)} }
@keyframes typing-dot { 0%,55%,100%{opacity:.25} 25%{opacity:.7} }
@keyframes message-land { from{transform:translateY(8px) scale(.96)} to{transform:none} }
@keyframes entry-enter { from{opacity:0;transform:translateY(8px)} to{opacity:1;transform:none} }
@keyframes receipt-check { from{opacity:0;transform:scale(.4)} to{opacity:1;transform:scale(1)} }
@keyframes reaction-pop { from{transform:scale(0)} to{transform:scale(1)} }
@keyframes bar-grow { from{transform:scaleY(0)} to{transform:scaleY(1)} }
@keyframes row-enter { from{opacity:0;transform:translateX(-10px)} to{opacity:1;transform:none} }
@keyframes fade-slide-up { from{opacity:0;transform:translateY(2px)} to{opacity:1;transform:none} }
@keyframes hero-shimmer { from{background-position:150% center} to{background-position:-150% center} }
@keyframes pop-in { from{opacity:0;transform:translateY(8px) scale(.97)} to{opacity:1;transform:none} }
```
滚动入场用 IntersectionObserver 触发 pop-in；`prefers-reduced-motion` 下全部循环停播、内容直接呈现终态。

---

## 响应式策略
- ≥1024px：全布局；768-1023px：Features 2 列、Jobs 上下堆叠、FAQ 单列
- <768px：单列；Hero 标题 40px；侧栏隐藏只留聊天；跑马灯与巨型脸保留；导航折叠为菜单钮
- 演示 mockup 用百分比宽度 + overflow:hidden，禁止横向溢出

## 可访问性与最佳实践
- 正文灰 #7d8187 于白底对比 ≈4.6:1；黑药丸白字 19:1
- focus-visible 2px 黑环；触控目标 ≥36px（药丸天然达标）
- 全部循环动画受 `prefers-reduced-motion` 降级；跑马灯 hover 暂停

## 实现说明
- 单文件 HTML，零构建；`:root` Token + `html[data-theme="dark"]` 翻转
- 头像/插画一律内联 SVG（blob 路径 + 白药丸眼睛；会议格用扁平插画头像），不依赖外部图片
- 动画全部 CSS keyframes + 少量 JS 状态机；剧本 timer 统一管理，可清理不泄漏
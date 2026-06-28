# 项目更新提示词（新增 HTML 风格模板）

> 本提示词用于引导 Agent 在新增 HTML 风格模板（包含 `.html` DEMO 与 `.md` 设计说明文件）后，自动完成截图、README 与首页画廊的同步更新。

## 触发条件

当 `templates/` 目录下出现新的风格模板文件夹（既有同构的 `.html` 与 `.md` 文件），且 `assets/screenshots/`、`README.md`、`README_en.md`、`index.html` 尚未同步收录该风格时，执行本流程。

---

## 前置准备

1. **确认新增模板**：扫描 `templates/` 目录，对比 `README.md` 中已收录的条目，找出尚未被收录的新增文件夹。记录每个新增模板的：
   - 文件夹名（风格 ID，连字符命名，如 `TRAE-Dark-Tech`）
   - 内部 `.html` 与 `.md` 文件的实际文件名
2. **校验命名规范**：本项目的约定是文件夹名 = HTML 文件名 = MD 文件名（均用连字符），例如 `templates/Glassmorphism/Glassmorphism.html`。若新增文件使用了下划线或其它分隔符（如 `TRAE_Dark_Tech.html`），**必须先重命名**使其与文件夹名完全一致：
   - `TRAE_Dark_Tech.html` → `TRAE-Dark-Tech.html`
   - `TRAE_Dark_Tech.md` → `TRAE-Dark-Tech.md`
   - 同步更新 `.md` 文件内部引用自身文件名的位置（若有）。
3. **读取模板元数据**：打开新增模板的 `.md` 文件，从「基本信息」表格中提取以下字段，后续步骤会用到：

   | .md 字段 | 用途 |
   |-----------|------|
   | 风格ID | 风格标识（小写） |
   | 显示名称 | README 标题与 index.html 的 `display` 字段 |
   | 模式（Dark/Light） | index.html 的 `tags` 第一项 |
   | 字体类型（serif/sans-serif/mono） | index.html 的 `tags` 第二项 |
   | 描述 | README 引用块与 index.html 的 `description` 字段（中文） |

   - 中文描述：直接取自 `.md` 文件「基本信息」表的「描述」字段。
   - 英文描述：参考 `.md` 文件「完整提示词」中的设计哲学/气质段落，翻译为精炼的一句英文（与 `README_en.md` 现有条目风格一致）。

4. **确认 Playwright 环境**：截图依赖 Playwright。若未安装，先执行：
   ```bash
   pip install playwright
   playwright install chromium
   ```

---

## 步骤 1：截取三张截图

参考 `script/recapture_01_02_03.py` 的截图逻辑，为每个新增模板生成 `01`（顶部）、`02`（中部）、`03`（底部）三张截图。

### 截图规格（必须与现有截图完全一致）

- 视口：`1440 × 900`，`device_scale_factor=1`，启用 `reduced_motion="reduce"`
- 截图 01：滚动到顶部 `scrollY=0`
- 截图 02：滚动到中部 `scrollY = max(0, bodyHeight/2 - viewportHeight/2)`
- 截图 03：滚动到底部 `scrollY = max(0, bodyHeight - viewportHeight)`
- 加载策略：`wait_until="networkidle"` 后再等待 `2.0s`，字体 `document.fonts.ready`
- 动画处理：截图前执行 `force_reveal_elements`，强制 `.reveal/.fade-in/.slide-up/[data-aos]` 等元素到最终可见状态（透明度置 1、transform 置 none），再等待 `0.8s`
- 滚动方式：`window.scrollTo({behavior:'smooth'})` 后轮询等待稳定

### 执行方式

**仅截取新增模板（更快）**

使用一次性 Python 脚本，使用用 `D:\Data\Design\beautiful_web_template\script\capture_one.py` 脚本，只处理新增模板。

### 验证

截图完成后，用 `read_file` 工具读取三张截图，确认：
- 文件存在且非空白
- 截图内容为对应模板的顶部/中部/底部
- 文件名格式为 `{文件夹名}-01.png`、`{文件夹名}-02.png`、`{文件夹名}-03.png`

---

## 步骤 2：更新 README.md（中文版）

文件路径：`README.md`

### 操作

1. **定位插入位置**：README 的画廊按文件夹名字母升序排列。找到新增模板应插入的位置（前一个 `###` 标题与后一个 `###` 标题之间）。
2. **插入条目**，格式严格如下（以 `TRAE-Dark-Tech` 为例）：

```markdown
### [显示名称](./templates/文件夹名/)

<p>
  <img src="./assets/screenshots/文件夹名-01.png" width="32.5%" alt="显示名称 — slide 01" />
  <img src="./assets/screenshots/文件夹名-02.png" width="32.5%" alt="显示名称 — slide 02" />
  <img src="./assets/screenshots/文件夹名-03.png" width="32.5%" alt="显示名称 — slide 03" />
</p>

> 中文描述（取自 .md 文件「基本信息」表的描述字段，或精炼自设计哲学段落）。
```

### 注意

- `width="32.5%"` 必须保持与现有条目完全一致。
- `alt` 文本格式为 `{显示名称} — slide 01`（注意是中文破折号 `—` 周围带空格，与现有一致）。
- 引用块 `>` 后的描述为中文，一句话，与同文件其它条目风格保持一致。
- 不要修改任何已有条目。

---

## 步骤 3：更新 README_en.md（英文版）

文件路径：`README_en.md`

### 操作

与步骤 2 完全相同的结构，但：

- 引用块描述为英文（参考 `.md` 文件设计哲学段落翻译，精炼为一句英文，与 `README_en.md` 现有条目风格一致）。
- `alt` 文本格式不变（仍为 `Display Name — slide 01`）。
- 插入位置同样按文件夹名字母升序。

```markdown
### [Display Name](./templates/Folder-Name/)

<p>
  <img src="./assets/screenshots/Folder-Name-01.png" width="32.5%" alt="Display Name — slide 01" />
  <img src="./assets/screenshots/Folder-Name-02.png" width="32.5%" alt="Display Name — slide 02" />
  <img src="./assets/screenshots/Folder-Name-03.png" width="32.5%" alt="Display Name — slide 03" />
</p>

> English description of the design style.
```

---

## 步骤 4：更新 index.html

文件路径：`index.html`

需要完成三处更新：① 模板数据数组、② hero 徽章数量、③ meta description 数量。

### 4.1 在 `templates` 数组中新增条目

定位 `<script>` 标签内的 `const templates = [...]` 数组。按 `name` 字段字母升序，在正确位置插入新对象。对象格式：

```javascript
{"name": "文件夹名", "display": "显示名称", "description": "中文描述", "tags": ["Dark或Light", "serif或sans-serif或mono"], "htmlPath": "./templates/文件夹名/文件夹名.html", "mdPath": "./templates/文件夹名/文件夹名.md", "shots": ["./assets/screenshots/文件夹名-01.png", "./assets/screenshots/文件夹名-02.png", "./assets/screenshots/文件夹名-03.png"]},
```

字段说明：

| 字段 | 取值来源 |
|------|----------|
| `name` | 文件夹名（连字符，如 `TRAE-Dark-Tech`） |
| `display` | `.md` 文件「显示名称」字段（如 `TRAE Dark Tech`） |
| `description` | `.md` 文件「描述」字段（中文，一句话） |
| `tags` | `[".md 模式字段(Dark/Light)", ".md 字体类型字段"]` |
| `htmlPath` | `./templates/{文件夹名}/{文件夹名}.html` |
| `mdPath` | `./templates/{文件夹名}/{文件夹名}.md` |
| `shots` | 三张截图的相对路径数组 |

注意：`description` 字段在 index.html 中应比 README 中的略短（参考现有条目，index.html 的 description 通常为一句话的精简版），但仍取自 `.md` 文件描述字段的语义。

### 4.2 更新 hero 徽章数量

定位 hero 区域的徽章元素，将数字更新为新总数：

```html
<div class="hero-badge">N 套免费 HTML 模板</div>
```

`N` = `templates` 数组的最终长度（原数量 + 新增数量）。

### 4.3 更新 meta description 数量

定位 `<head>` 中的 meta description，将数字更新为新总数：

```html
<meta name="description" content="浏览 N 套精美的单页 HTML 落地页模板，每套展示独特的网页设计风格。原始提示词来自 designprompts.dev。">
```

`N` 同上。

---

## 完成检查清单

更新完成后，逐项核对：

- [ ] 新增模板的 `.html` 与 `.md` 文件名已与文件夹名一致（连字符命名）
- [ ] `assets/screenshots/` 下存在 `{文件夹名}-01.png`、`-02.png`、`-03.png` 三张截图，内容正确
- [ ] `README.md` 已按字母序插入新条目，格式（`width="32.5%"`、`alt` 文本、引用块）与现有条目一致
- [ ] `README_en.md` 已按字母序插入新条目，英文描述
- [ ] `index.html` 的 `templates` 数组已按字母序插入新对象，字段完整且路径正确
- [ ] `index.html` hero 徽章数量已更新为最新总数
- [ ] `index.html` meta description 数量已更新为最新总数
- [ ] 未修改任何已有模板的条目或截图

## 注意事项

- 所有路径使用 `./` 开头的相对路径，与现有条目保持一致。
- 字母排序以 `name`/文件夹名为准，区分大小写时按现有顺序惯例（本项目均为首字母大写，按 ASCII 排序）。
- 若一次新增多个模板，对每个模板重复上述步骤，最后统一更新 `index.html` 的数量字段。
- 截图前务必确认 Playwright Chromium 已安装，否则截图会失败。
- 不要改动 `script/recapture_01_02_03.py` 脚本本身，除非用户明确要求。

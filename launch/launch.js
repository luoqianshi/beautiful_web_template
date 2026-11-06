"use strict";

const styleGuides = {
  swiss: {
    name: "瑞士极简（Swiss Minimalist）",
    directory: "Swiss-Minimalist",
    rules: [
      "白色 #FFFFFF 作为底色，近黑色作文字和边框。#FF3000 仅用于主行动或重点标记；红色按钮使用深色文字。",
      "使用系统无衬线字体；项目名大而紧凑，正文至少 16px。用字号、粗细和对齐区分层级。",
      "桌面采用非对称网格，标题与功能区共用左对齐基线。以直线分隔、矩形按钮、充足留白组织内容。省去渐变、胶囊卡片和投影。",
      "手机改为单列，保留同样的阅读顺序与红色行动入口。"
    ]
  },
  academia: {
    name: "古典学院（Academia）",
    directory: "Academia",
    rules: [
      "以深木色 #1C1714 为底，暖纸色为正文，黄铜色 #C9A962 用于焦点、细线和主要按钮。黄铜按钮上用深色文字。",
      "用本机中文衬线字体呈现标题；正文选易读字体，保持舒适行距。标题、正文和行动入口各自有明确的大小与间距。",
      "首屏用书页式双栏，项目名与价值说明在一侧，另一侧可用自制的书签或装饰线。用章节小标题和铜色细框组织功能。",
      "手机合并为一列，按标题、价值、行动、功能的顺序阅读；纹理应轻微，不能遮挡文字。"
    ]
  }
};

const form = document.querySelector("#builder");
const fields = form.elements;
const result = document.querySelector("#result");
const markdown = document.querySelector("#markdown");
const feedback = document.querySelector("#feedback");
const styleLink = document.querySelector("#style-url");
const radios = Array.from(form.querySelectorAll('input[name="style"]'));

if (location.hostname === "luoqianshi.github.io") {
  document.querySelector("#process-link").href =
    "https://github.com/luoqianshi/beautiful_web_template/blob/main/launch/cases/process.md";
}

function styleFromAddress() {
  const address = new URL(window.location.href);
  const fileStyle = address.protocol === "file:"
    ? new URLSearchParams(address.hash.slice(1)).get("style")
    : null;
  const style = fileStyle || address.searchParams.get("style");
  return Object.hasOwn(styleGuides, style) ? style : "swiss";
}

function styleAddress(style) {
  const address = new URL(window.location.href);
  address.hash = "";
  address.search = new URLSearchParams({ style }).toString();
  return address;
}

function hideOutput() {
  result.hidden = true;
  markdown.value = "";
  feedback.textContent = "";
}

function syncStyle() {
  const style = styleFromAddress();
  if (fields.style.value !== style) hideOutput();
  fields.style.value = style;
  styleLink.href = styleAddress(style).href;
  styleLink.textContent = location.protocol === "file:" ? "当前风格链接（本地文件）" : "当前风格的分享链接";
  document.querySelector("#copy-style").textContent = location.protocol === "file:" ? "复制所选风格的本地链接" : "复制所选风格链接";
  document.querySelector("#style-feedback").textContent = "";
  styleLink.hidden = true;
}

function chooseStyle(style) {
  const address = styleAddress(style);
  if (location.href !== address.href) {
    try {
      history.pushState(null, "", address);
    } catch (error) {
      // Some browsers only permit fragment changes on file: URLs.
      if (location.protocol !== "file:") throw error;
      location.hash = "style=" + style;
    }
  }
  syncStyle();
}

function readFacts() {
  const facts = {};
  for (const key of ["project", "audience", "summary", "features", "cta", "url"]) {
    const field = fields.namedItem(key);
    facts[key] = field.value.trim();
    field.setCustomValidity(facts[key] ? "" : "请填写此项，内容不能只有空格。");
  }
  facts.features = facts.features.split(/\r?\n/).map(line => line.trim()).filter(Boolean);
  if (facts.features.length < 1 || facts.features.length > 3) {
    fields.features.setCustomValidity("请填写 1–3 项真实功能，每行一项。");
  }
  try {
    const target = new URL(facts.url);
    if (!/^https?:\/\/[^/\\?#\s]/i.test(facts.url) || /[\s\\]/.test(facts.url) ||
        !["https:", "http:"].includes(target.protocol) || !target.hostname) {
      throw new Error("invalid-url");
    }
  } catch {
    fields.url.setCustomValidity("请填写以 https:// 或 http:// 开头的完整网址。");
  }
  return form.reportValidity() ? facts : null;
}

function buildTask(facts, style) {
  const guide = styleGuides[style];
  const repo = "https://github.com/luoqianshi/beautiful_web_template";
  return [
    "# 制作「" + facts.project + "」的中文产品发布页",
    "",
    "请生成可以直接打开并发布的单文件 index.html，使用原生 HTML 和内联 CSS。以下信息已足够完成任务。",
    "",
    "## 项目资料",
    "",
    "- 项目名称：" + facts.project,
    "- 目标读者：" + facts.audience,
    "- 一句话介绍：" + facts.summary,
    "- 已经实现的功能：",
    ...facts.features.map(feature => "  - " + feature),
    "- 主按钮文字：" + facts.cta,
    "- 主按钮目标：" + facts.url,
    "",
    "## 页面结构",
    "",
    "1. 首屏写项目名称，用一句自然的中文交代谁会用、能完成什么，展示链接到上述目标的主按钮。",
    "2. 用项目资料中的每一项真实功能说明具体用途。保留项目名称、目标网址及按钮文字。素材不足时压缩篇幅。",
    "3. 页面末尾再次提供主行动。所有可见文案使用真实资料；省去未提供的数字、价格、评价、客户标志和演示功能。",
    "",
    "## 视觉约束 · " + guide.name,
    "",
    ...guide.rules.map(rule => "- " + rule),
    "",
    "## 交付与检查",
    "",
    "- 页面语言设为 zh-CN，有页面标题、一个主标题、语义化章节和清晰可见的键盘焦点。主行动使用真实链接。",
    "- 使用系统字体和内联样式；装饰用 CSS 完成。页面在本地打开时应可阅读，避免依赖外部图片、脚本或字体。",
    "- 分别在 390px 与 1440px 宽度下检查布局、对比度与水平溢出；用键盘进入主按钮，核对文字和目标链接。",
    "- 交付 index.html，简述打开方式和实际完成的检查，指出仍需人工验证的部分。",
    "",
    "可选参考：Beautiful Web Template 的 " + guide.name + " 模板，" +
      repo + "/tree/main/templates/" + guide.directory + " 。以上约束可独立使用。",
    ""
  ].join("\n");
}

form.addEventListener("input", event => {
  event.target.setCustomValidity("");
  hideOutput();
});
for (const radio of radios) {
  radio.addEventListener("change", () => chooseStyle(radio.value));
}
window.addEventListener("popstate", syncStyle);
window.addEventListener("hashchange", syncStyle);
window.addEventListener("pageshow", syncStyle);
syncStyle();

document.querySelector("#copy-style").addEventListener("click", async () => {
  const status = document.querySelector("#style-feedback");
  try {
    await navigator.clipboard.writeText(styleLink.href);
    status.textContent = location.protocol === "file:" ? "已复制本机文件链接，仅适用于这台设备。" : "已复制仅包含风格选择的分享链接。";
  } catch {
    styleLink.hidden = false;
    status.textContent = "请右键或长按上方链接，选择复制链接地址。";
  }
});

form.addEventListener("submit", event => {
  event.preventDefault();
  const facts = readFacts();
  if (!facts) return;
  markdown.value = buildTask(facts, fields.style.value);
  result.hidden = false;
  feedback.textContent = "";
  document.querySelector("#result-title").focus();
});

document.querySelector("#copy").addEventListener("click", async () => {
  try {
    await navigator.clipboard.writeText(markdown.value);
    feedback.textContent = "任务单已复制，可以粘贴到 AI 编程工具。";
  } catch {
    markdown.focus();
    markdown.select();
    feedback.textContent = "已选中完整任务单。请用系统复制命令，或下载 .md 文件。";
  }
});

document.querySelector("#download").addEventListener("click", () => {
  const url = URL.createObjectURL(new Blob([markdown.value], { type: "text/markdown;charset=utf-8" }));
  const link = document.createElement("a");
  link.href = url;
  link.download = "launch-" + fields.style.value + ".md";
  document.body.append(link);
  link.click();
  link.remove();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
  feedback.textContent = "已请求下载任务单。";
});

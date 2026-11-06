# Paper-Master 双风格试制记录

本案例在同一个 [项目简报](brief.md) 下保留了同样的主要内容和链接。两个版本的插图、排版均在页面内完成，采用系统字体，加载页面无需字体服务或脚本。

| 版本 | 初版桌面首屏 | 初版手机首屏 | 最终页面 | 最终桌面缩略图 |
| --- | --- | --- | --- | --- |
| Swiss Minimalist | [1440 × 900](swiss-first-1440.webp) | [390 × 844](swiss-first-390.webp) | [查看页面](https://luoqianshi.github.io/beautiful_web_template/launch/cases/swiss.html) | [960 × 600](swiss.webp) |
| Academia | [1440 × 900](academia-first-1440.webp) | [390 × 844](academia-first-390.webp) | [查看页面](https://luoqianshi.github.io/beautiful_web_template/launch/cases/academia.html) | [960 × 600](academia.webp) |

## 初版检查与修正

1. 在 Chrome 中生成上表的四张初版截图。390px 首屏能读到项目说明和 CTA，桌面版并列展示文字与工作流图或书柜。
2. 测量手机链接时，瑞士版的返回和书柜链接分别只有 35px、17px 高；学院版两个链接都只有 16px。将两版移动导航的点击区统一扩大到至少 44px。改为“用这个风格做产品页”入口后再测，390px 和 320px 下两处链接高度均达到 44px，瑞士版在 320px 下会换行至 54px。
3. 将学院版缩至 320px，固定的最小标题字号把文档横向撑到 351px。改用移动端流动字号后，在同一视口复测文档宽度为 320px，标题仍保持单行。

## 最终验收

- Chrome + Playwright 通过本地文件地址加载两版，分别在 1440 × 900 和 390 × 844 的视口检查。四组的实际文档宽度均等于视口宽度，均无页面脚本错误。
- 390px 视口下，两版 CTA 的底边距视口顶部约 471px 和 410px；桌面版分别约为 644px 和 529px，均完整可见。
- 每版按 Tab，首个焦点为“用这个风格做产品页”，第二个焦点为“查看 GitHub 项目”。已核对同款入口包含当前风格参数与 `#brief`，两版主 CTA 均链接到同一官方仓库，页尾均链接到官方示例书柜。
- 这里记录的是页面交付与机械检查；读者的偏好及真实项目采用情况需要另行收集。

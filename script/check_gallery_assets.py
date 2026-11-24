"""画廊资产完整性检查：index.html 注册的每张截图必须同时存在 PNG 与 webp 变体。

用法: python web2template_output/qoder_cn/check_gallery_assets.py
退出码 0=通过, 1=有缺失
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML = os.path.join(ROOT, "index.html")

problems = []
html = open(HTML, encoding="utf-8").read()
entries = re.findall(r'\{"name":\s*"([^"]+)".*?"shots":\s*\[(.*?)\]\}', html)
if not entries:
    sys.exit("未能从 index.html 解析出 templates 条目")

for name, shots_blob in entries:
    shots = re.findall(r'"([^"]+\.png)"', shots_blob)
    if len(shots) != 3:
        problems.append(f"{name}: shots 数量为 {len(shots)}，应为 3")
    for s in shots:
        png = os.path.join(ROOT, s.replace("./", "").replace("/", os.sep))
        webp = os.path.join(ROOT, "assets", "screenshots", "webp",
                            os.path.basename(s)[:-4] + ".webp")
        if not os.path.exists(png):
            problems.append(f"{name}: PNG 缺失 {s}")
        if not os.path.exists(webp):
            problems.append(f"{name}: WEBP 缺失 {os.path.relpath(webp, ROOT)}")

for p in problems:
    print("FAIL", p)
print(f"检查 {len(entries)} 个条目：{'全部通过' if not problems else str(len(problems)) + ' 项缺失'}")
sys.exit(1 if problems else 0)

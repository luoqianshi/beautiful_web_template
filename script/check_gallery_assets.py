"""验证画廊清单及其 HTML、Markdown、PNG、WebP 文件：python script/check_gallery_assets.py"""
import json
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


class GalleryCatalog(HTMLParser):
    def __init__(self):
        super().__init__()
        self.inside = False
        self.chunks = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "script" and attrs.get("id") == "template-catalog":
            self.inside = attrs.get("type") == "application/json"

    def handle_data(self, data):
        if self.inside:
            self.chunks.append(data)

    def handle_endtag(self, tag):
        if tag == "script":
            self.inside = False


def validate_file(reference, suffix):
    if not isinstance(reference, str) or not reference.startswith("./"):
        return f"{suffix} 文件需要站点相对路径：{reference!r}"
    path = (ROOT / reference).resolve()
    if not path.is_relative_to(ROOT) or path.suffix.lower() != suffix:
        return f"无效 {suffix} 路径：{reference}"
    if not path.is_file():
        return f"文件缺失：{reference}"
    if suffix in {".png", ".webp"}:
        with path.open("rb") as stream:
            header = stream.read(12)
        if suffix == ".png" and not header.startswith(b"\x89PNG\r\n\x1a\n"):
            return f"PNG 格式不符：{reference}"
        if suffix == ".webp" and (header[:4], header[8:12]) != (b"RIFF", b"WEBP"):
            return f"WebP 格式不符：{reference}"
    else:
        try:
            content = path.read_text(encoding="utf-8").strip()
        except UnicodeDecodeError:
            return f"文件编码不是 UTF-8：{reference}"
        if not content:
            return f"空文件：{reference}"


def check_catalog(entries):
    if not isinstance(entries, list) or not entries:
        raise ValueError("清单必须是非空数组")
    names = set()
    for index, entry in enumerate(entries, 1):
        if not isinstance(entry, dict):
            yield f"第 {index} 项不是对象"
            continue
        name = entry.get("name")
        if not isinstance(name, str) or not name.strip():
            yield f"第 {index} 项缺少有效 name"
            continue
        if name in names:
            yield f"重复的模板名称：{name}"
        names.add(name)
        files = [(entry.get("htmlPath"), ".html"), (entry.get("mdPath"), ".md")]
        shots = entry.get("shots")
        if not isinstance(shots, list) or len(shots) != 3:
            yield f"{name}: shots 必须含三张截图"
        if isinstance(shots, list):
            for shot in shots:
                files.append((shot, ".png"))
                if isinstance(shot, str):
                    files.append((f"./assets/screenshots/webp/{Path(shot).stem}.webp", ".webp"))
        for ref, suffix in files:
            problem = validate_file(ref, suffix)
            if problem:
                yield f"{name}: {problem}"


class LocalLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.paths = []

    def handle_starttag(self, tag, attrs):
        for name, reference in attrs:
            if name not in {"src", "href"} or not reference:
                continue
            url = urlsplit(reference)
            if url.path and not url.scheme and not url.netloc:
                self.paths.append(unquote(url.path))


def check_launch_links():
    launch_dir = ROOT / "launch"
    for required in ("index.html", "publish.html"):
        if not (launch_dir / required).is_file():
            yield f"试点页面缺失：launch/{required}"
    for page in sorted(launch_dir.rglob("*.html")):
        links = LocalLinks()
        links.feed(page.read_text(encoding="utf-8"))
        for ref in links.paths:
            dest = (page.parent / ref).resolve()
            if dest.is_dir():
                dest /= "index.html"
            if not dest.is_relative_to(ROOT) or not dest.is_file():
                yield f"{page.relative_to(ROOT)}: 站内资源缺失 {ref}"


def main():
    parser = GalleryCatalog()
    try:
        parser.feed((ROOT / "index.html").read_text(encoding="utf-8"))
        entries = json.loads("".join(parser.chunks))
        problems = list(check_catalog(entries))
        problems.extend(check_launch_links())
    except (ValueError, OSError) as exc:
        sys.exit(f"清单校验失败：{exc}")
    for problem in problems:
        print("FAIL", problem)
    print(f"已检查 {len(entries)} 套模板及试点页面站内资源，发现 {len(problems)} 项问题。")
    return int(bool(problems))


if __name__ == "__main__":
    sys.exit(main())

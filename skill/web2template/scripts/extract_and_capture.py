#!/usr/bin/env python3
"""web2template: Extract design data and capture screenshots from a web page.

This script is the data-gathering engine of the web2template SKILL.
It produces two artifacts in the output directory:

  1. screenshots/  — top, middle, bottom and full-page PNG captures
  2. design_data.json — structured design tokens extracted from computed styles

The JSON file is consumed by the Agent (together with the screenshots) to
generate a reusable UI/UX style prompt document.

Usage:
  python extract_and_capture.py --url https://example.com --output ./output
  python extract_and_capture.py --file ./template.html --output ./output

Dependencies:
  pip install playwright
  playwright install chromium
"""

import argparse
import json
import sys
import time
from pathlib import Path

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print(
        "ERROR: Playwright is not installed.\n"
        "  pip install playwright\n"
        "  playwright install chromium",
        file=sys.stderr,
    )
    sys.exit(1)

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

VIEWPORT_WIDTH = 1440
VIEWPORT_HEIGHT = 900
LOAD_WAIT = 2.0       # seconds after networkidle
SCROLL_WAIT = 1.5     # seconds for smooth scroll to settle
REVEAL_WAIT = 0.8     # seconds after forcing reveal elements visible
ELEMENT_SCAN_LIMIT = 400  # cap to avoid performance issues on huge pages


# ---------------------------------------------------------------------------
# Main entry
# ---------------------------------------------------------------------------

def run(source: str, output_dir: str, is_url: bool) -> dict:
    """Capture screenshots and extract design data. Returns the design dict."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    shots_dir = output_path / "screenshots"
    shots_dir.mkdir(exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": VIEWPORT_WIDTH, "height": VIEWPORT_HEIGHT},
            device_scale_factor=1,
            reduced_motion="reduce",
        )
        page = context.new_page()

        # ---- Navigate -------------------------------------------------------
        if is_url:
            page.goto(source, wait_until="networkidle", timeout=30000)
        else:
            file_path = Path(source).resolve()
            page.goto(f"file:///{file_path.as_posix()}", wait_until="networkidle", timeout=30000)

        page.wait_for_load_state("networkidle")
        try:
            page.evaluate("document.fonts.ready")
        except Exception:
            pass
        time.sleep(LOAD_WAIT)

        # ---- Extract structured design data --------------------------------
        print("[1/2] Extracting design data ...")
        design_data = _extract_design_data(page)

        # ---- Capture screenshots -------------------------------------------
        print("[2/2] Capturing screenshots ...")
        _capture_screenshots(page, shots_dir)

        browser.close()

    # ---- Persist design data ----------------------------------------------
    data_file = output_path / "design_data.json"
    with open(data_file, "w", encoding="utf-8") as f:
        json.dump(design_data, f, ensure_ascii=False, indent=2)

    print(f"\nDone.")
    print(f"  Screenshots : {shots_dir}")
    print(f"  Design data : {data_file}")
    return design_data


# ---------------------------------------------------------------------------
# Design data extraction (all evaluation happens in the browser context)
# ---------------------------------------------------------------------------

_JS_EXTRACT_CSS_VARS = r"""() => {
    const vars = {};
    for (const sheet of document.styleSheets) {
        try {
            for (const rule of sheet.cssRules) {
                if (rule.selectorText && rule.selectorText.includes(':root')) {
                    for (let i = 0; i < rule.style.length; i++) {
                        const prop = rule.style[i];
                        vars[prop] = rule.style.getPropertyValue(prop).trim();
                    }
                }
            }
        } catch(e) { /* cross-origin stylesheet */ }
    }
    return vars;
}"""

_JS_EXTRACT_COLORS = r"""() => {
    const bgColors = new Set(), textColors = new Set(), borderColors = new Set();
    const elements = document.querySelectorAll('*');
    const limit = Math.min(elements.length, %d);
    for (let i = 0; i < limit; i++) {
        const el = elements[i];
        const style = getComputedStyle(el);
        const bg = style.backgroundColor;
        const color = style.color;
        const bColor = style.borderTopColor;
        if (bg && bg !== 'rgba(0, 0, 0, 0)' && bg !== 'transparent') bgColors.add(bg);
        if (color && color !== 'rgba(0, 0, 0, 0)') textColors.add(color);
        if (bColor && bColor !== 'rgba(0, 0, 0, 0)' && bColor !== 'transparent') borderColors.add(bColor);
    }
    return {
        backgrounds: Array.from(bgColors).slice(0, 25),
        texts: Array.from(textColors).slice(0, 25),
        borders: Array.from(borderColors).slice(0, 15)
    };
}""" % ELEMENT_SCAN_LIMIT

_JS_EXTRACT_TYPOGRAPHY = r"""() => {
    const fonts = new Set();
    const headingInfo = {};
    const bodySizes = new Set();
    const weights = new Set();
    const lineHeights = new Set();
    const letterSpacings = new Set();
    const textTransforms = new Set();

    const bodyStyle = getComputedStyle(document.body);
    fonts.add(bodyStyle.fontFamily);
    bodySizes.add(bodyStyle.fontSize);
    weights.add(bodyStyle.fontWeight);
    lineHeights.add(bodyStyle.lineHeight);

    ['h1','h2','h3','h4','h5','h6'].forEach(tag => {
        const els = document.querySelectorAll(tag);
        headingInfo[tag] = [];
        els.forEach((el, idx) => {
            if (idx > 5) return;
            const s = getComputedStyle(el);
            fonts.add(s.fontFamily);
            headingInfo[tag].push({
                size: s.fontSize, weight: s.fontWeight,
                lineHeight: s.lineHeight, letterSpacing: s.letterSpacing,
                textTransform: s.textTransform
            });
            weights.add(s.fontWeight);
            lineHeights.add(s.lineHeight);
            letterSpacings.add(s.letterSpacing);
            if (s.textTransform && s.textTransform !== 'none') textTransforms.add(s.textTransform);
        });
    });

    const sampleSelectors = 'p, span, a, button, label, input, .btn, .card, li, td, blockquote';
    document.querySelectorAll(sampleSelectors).forEach((el, i) => {
        if (i > 120) return;
        const s = getComputedStyle(el);
        fonts.add(s.fontFamily);
        bodySizes.add(s.fontSize);
        weights.add(s.fontWeight);
        lineHeights.add(s.lineHeight);
        if (s.letterSpacing && s.letterSpacing !== 'normal') letterSpacings.add(s.letterSpacing);
    });

    const loadedFonts = [];
    try { document.fonts.forEach(f => loadedFonts.push({family:f.family, weight:f.weight, style:f.style})); } catch(e){}

    return {
        font_families: Array.from(fonts).filter(f => f && !f.includes('undefined')),
        loaded_fonts: loadedFonts,
        heading_info: headingInfo,
        body_sizes: Array.from(bodySizes),
        font_weights: Array.from(weights),
        line_heights: Array.from(lineHeights),
        letter_spacings: Array.from(letterSpacings),
        text_transforms: Array.from(textTransforms)
    };
}"""

_JS_EXTRACT_SPACING = r"""() => {
    const paddings = new Set(), margins = new Set(), gaps = new Set();
    const elements = document.querySelectorAll('*');
    const limit = Math.min(elements.length, %d);
    for (let i = 0; i < limit; i++) {
        const s = getComputedStyle(elements[i]);
        if (s.padding && s.padding !== '0px') paddings.add(s.padding);
        if (s.margin && s.margin !== '0px') margins.add(s.margin);
        if (s.gap && s.gap !== 'normal' && s.gap !== '0px') gaps.add(s.gap);
    }
    return {
        common_paddings: Array.from(paddings).slice(0, 20),
        common_margins: Array.from(margins).slice(0, 15),
        gaps: Array.from(gaps).slice(0, 15)
    };
}""" % ELEMENT_SCAN_LIMIT

_JS_EXTRACT_BORDERS = r"""() => {
    const radii = new Set(), widths = new Set(), styles = new Set();
    const elements = document.querySelectorAll('*');
    const limit = Math.min(elements.length, %d);
    for (let i = 0; i < limit; i++) {
        const s = getComputedStyle(elements[i]);
        if (s.borderRadius && s.borderRadius !== '0px') radii.add(s.borderRadius);
        if (s.borderTopWidth && s.borderTopWidth !== '0px') widths.add(s.borderTopWidth + ' ' + s.borderTopStyle);
        if (s.borderTopStyle && s.borderTopStyle !== 'none') styles.add(s.borderTopStyle);
    }
    return {
        radii: Array.from(radii).slice(0, 25),
        border_specs: Array.from(widths).slice(0, 15),
        styles: Array.from(styles)
    };
}""" % ELEMENT_SCAN_LIMIT

_JS_EXTRACT_SHADOWS = r"""() => {
    const shadows = new Set();
    const elements = document.querySelectorAll('*');
    const limit = Math.min(elements.length, %d);
    for (let i = 0; i < limit; i++) {
        const s = getComputedStyle(elements[i]);
        if (s.boxShadow && s.boxShadow !== 'none') shadows.add(s.boxShadow);
    }
    return Array.from(shadows).slice(0, 20);
}""" % ELEMENT_SCAN_LIMIT

_JS_EXTRACT_LAYOUT = r"""() => {
    const sections = [];
    const blockTags = ['header','nav','main','section','footer','aside','article'];
    function guessRole(el, tag) {
        const text = ((el.className||'') + ' ' + (el.id||'')).toLowerCase();
        if (text.includes('hero')) return 'hero';
        if (text.includes('feature')) return 'features';
        if (text.includes('pricing')) return 'pricing';
        if (text.includes('testimonial')) return 'testimonials';
        if (text.includes('faq')) return 'faq';
        if (text.includes('cta')) return 'cta';
        if (text.includes('stat')) return 'stats';
        if (text.includes('blog') || text.includes('post')) return 'blog';
        if (text.includes('benefit')) return 'benefits';
        if (text.includes('how') && text.includes('work')) return 'how-it-works';
        if (text.includes('footer')) return 'footer';
        if (text.includes('nav') || text.includes('header') || text.includes('menu')) return 'navigation';
        return tag;
    }
    blockTags.forEach(tag => {
        document.querySelectorAll(tag).forEach(el => {
            const rect = el.getBoundingClientRect();
            const s = getComputedStyle(el);
            sections.push({
                tag: tag,
                classes: (el.className || '').toString().slice(0, 200),
                id: el.id || '',
                width: Math.round(rect.width),
                height: Math.round(rect.height),
                maxWidth: s.maxWidth,
                padding: s.padding,
                display: s.display,
                role: el.getAttribute('role') || el.getAttribute('aria-label') || guessRole(el, tag)
            });
        });
    });
    const containers = [];
    document.querySelectorAll('[class*="container"], [class*="wrapper"], [class*="max-w"]').forEach(el => {
        const s = getComputedStyle(el);
        containers.push({ classes: (el.className||'').toString().slice(0,150), maxWidth: s.maxWidth, padding: s.padding });
    });
    return {
        sections: sections,
        containers: containers.slice(0, 12),
        total_height: Math.round(document.body.scrollHeight),
        section_count: sections.length
    };
}"""

_JS_EXTRACT_ANIMATIONS = r"""() => {
    const transitions = new Set(), animationNames = new Set();
    const keyframes = [];
    const elements = document.querySelectorAll('*');
    const limit = Math.min(elements.length, %d);
    for (let i = 0; i < limit; i++) {
        const s = getComputedStyle(elements[i]);
        if (s.transition && s.transition !== 'all 0s ease 0s') transitions.add(s.transition);
        if (s.animationName && s.animationName !== 'none') animationNames.add(s.animationName);
    }
    for (const sheet of document.styleSheets) {
        try {
            for (const rule of sheet.cssRules) {
                if (rule.type === CSSRule.KEYFRAMES_RULE) {
                    const kf = { name: rule.name, frames: [] };
                    for (const r of rule.cssRules) {
                        kf.frames.push({ key: r.keyText, css: r.style.cssText });
                    }
                    keyframes.push(kf);
                }
            }
        } catch(e) {}
    }
    return {
        transitions: Array.from(transitions).slice(0, 20),
        animation_names: Array.from(animationNames),
        keyframes: keyframes
    };
}""" % ELEMENT_SCAN_LIMIT

_JS_EXTRACT_GRADIENTS = r"""() => {
    const gradients = new Set();
    const elements = document.querySelectorAll('*');
    const limit = Math.min(elements.length, %d);
    for (let i = 0; i < limit; i++) {
        const s = getComputedStyle(elements[i]);
        const bg = s.backgroundImage;
        if (bg && bg !== 'none' && bg.includes('gradient')) gradients.add(bg);
    }
    return Array.from(gradients).slice(0, 20);
}""" % ELEMENT_SCAN_LIMIT

_JS_EXTRACT_EFFECTS = r"""() => {
    const filters = new Set(), backdropFilters = new Set(), transforms = new Set();
    const elements = document.querySelectorAll('*');
    const limit = Math.min(elements.length, %d);
    for (let i = 0; i < limit; i++) {
        const s = getComputedStyle(elements[i]);
        if (s.filter && s.filter !== 'none') filters.add(s.filter);
        if (s.backdropFilter && s.backdropFilter !== 'none') backdropFilters.add(s.backdropFilter);
        if (s.transform && s.transform !== 'none') transforms.add(s.transform);
    }
    return {
        filters: Array.from(filters).slice(0, 15),
        backdrop_filters: Array.from(backdropFilters).slice(0, 15),
        transforms: Array.from(transforms).slice(0, 15)
    };
}""" % ELEMENT_SCAN_LIMIT

_JS_EXTRACT_RESOURCES = r"""() => {
    const fonts = [], stylesheets = [], scripts = [];
    document.querySelectorAll('link[rel="stylesheet"]').forEach(el => stylesheets.push(el.href));
    document.querySelectorAll('link[href*="fonts.googleapis"], link[href*="fonts.gstatic"], link[href*="fonts.bunny"], link[href*="fontsisland"]').forEach(el => fonts.push(el.href));
    document.querySelectorAll('script[src]').forEach(el => scripts.push(el.src));
    return { fonts, stylesheets, scripts };
}"""

_JS_EXTRACT_PAGE_INFO = r"""() => ({
    title: document.title,
    lang: document.documentElement.lang || '',
    description: (document.querySelector('meta[name="description"]') || {}).content || '',
    charset: document.characterSet || ''
})"""


def _extract_design_data(page) -> dict:
    """Run all extraction JS snippets and assemble the design data dict."""
    data = {}
    data["page_info"] = page.evaluate(_JS_EXTRACT_PAGE_INFO)
    data["css_variables"] = page.evaluate(_JS_EXTRACT_CSS_VARS)
    data["color_palette"] = page.evaluate(_JS_EXTRACT_COLORS)
    data["typography"] = page.evaluate(_JS_EXTRACT_TYPOGRAPHY)
    data["spacing"] = page.evaluate(_JS_EXTRACT_SPACING)
    data["borders"] = page.evaluate(_JS_EXTRACT_BORDERS)
    data["shadows"] = page.evaluate(_JS_EXTRACT_SHADOWS)
    data["layout"] = page.evaluate(_JS_EXTRACT_LAYOUT)
    data["animations"] = page.evaluate(_JS_EXTRACT_ANIMATIONS)
    data["gradients"] = page.evaluate(_JS_EXTRACT_GRADIENTS)
    data["effects"] = page.evaluate(_JS_EXTRACT_EFFECTS)
    data["resources"] = page.evaluate(_JS_EXTRACT_RESOURCES)
    data["viewport"] = {"width": VIEWPORT_WIDTH, "height": VIEWPORT_HEIGHT}
    data["captured_at"] = time.strftime("%Y-%m-%d %H:%M:%S")
    return data


# ---------------------------------------------------------------------------
# Screenshot capture (reuses logic from project's recapture script)
# ---------------------------------------------------------------------------

def _force_reveal_elements(page):
    """Force commonly hidden/animated elements into their final state."""
    page.evaluate(r"""() => {
        const selectors = [
            '.reveal', '.fade-in', '.fade-in-up', '.slide-up', '.slide-in',
            '.animate', '.animated', '.hidden', '.invisible', '.aos-animate',
            '[data-aos]', '.scroll-reveal', '.reveal-up'
        ];
        selectors.forEach(sel => {
            document.querySelectorAll(sel).forEach(el => {
                el.classList.add('visible');
                el.classList.add('aos-animate');
                el.style.opacity = '1';
                el.style.transform = 'none';
                el.style.filter = 'none';
                el.style.visibility = 'visible';
            });
        });
        document.querySelectorAll('[style*="opacity: 0"]').forEach(el => {
            if (el.getBoundingClientRect().height > 0) el.style.opacity = '1';
        });
    }""")


def _smooth_scroll_to(page, y):
    page.evaluate(f"window.scrollTo({{top: {y}, behavior: 'smooth'}})")
    for _ in range(50):
        time.sleep(0.05)
        current = page.evaluate("window.scrollY")
        if abs(current - y) <= 2:
            break


def _capture_screenshots(page, shots_dir: Path):
    """Capture top, middle, bottom and full-page screenshots."""
    total_height = page.evaluate("document.body.scrollHeight")
    safe_bottom = max(0, total_height - VIEWPORT_HEIGHT)
    safe_middle = max(0, int(total_height / 2 - VIEWPORT_HEIGHT / 2))

    # 01 — top
    page.evaluate("window.scrollTo(0, 0)")
    time.sleep(SCROLL_WAIT)
    _force_reveal_elements(page)
    time.sleep(REVEAL_WAIT)
    page.screenshot(path=str(shots_dir / "screenshot-01-top.png"), full_page=False)

    # 02 — middle
    _smooth_scroll_to(page, safe_middle)
    time.sleep(SCROLL_WAIT)
    _force_reveal_elements(page)
    time.sleep(REVEAL_WAIT)
    page.screenshot(path=str(shots_dir / "screenshot-02-middle.png"), full_page=False)

    # 03 — bottom
    _smooth_scroll_to(page, safe_bottom)
    time.sleep(SCROLL_WAIT)
    _force_reveal_elements(page)
    time.sleep(REVEAL_WAIT)
    page.screenshot(path=str(shots_dir / "screenshot-03-bottom.png"), full_page=False)

    # Full page
    try:
        page.screenshot(path=str(shots_dir / "screenshot-full.png"), full_page=True)
    except Exception:
        pass  # full-page capture may fail on very tall pages


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Extract design data and capture screenshots from a web page."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--url", help="URL of the website to analyze")
    group.add_argument("--file", help="Path to local HTML file to analyze")
    parser.add_argument(
        "--output", default="./web2template_output",
        help="Output directory (default: ./web2template_output)"
    )
    args = parser.parse_args()

    source = args.url if args.url else args.file
    is_url = bool(args.url)

    print(f"Source : {source}")
    print(f"Output : {args.output}\n")

    run(source, args.output, is_url)


if __name__ == "__main__":
    main()

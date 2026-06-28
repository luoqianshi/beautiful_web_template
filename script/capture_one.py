#!/usr/bin/env python3
"""Capture screenshots for a single template by reusing logic from recapture_01_02_03.py."""
import sys
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE_DIR = Path(__file__).parent.parent.resolve()
TEMPLATES_DIR = BASE_DIR / "templates"
SCREENSHOTS_DIR = BASE_DIR / "assets" / "screenshots"
SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)

VIEWPORT_WIDTH = 1440
VIEWPORT_HEIGHT = 900
LOAD_WAIT = 2.0
SCROLL_WAIT = 1.5
REVEAL_WAIT = 0.8


def log(msg):
    print(msg, flush=True)


def wait_for_stable(page):
    page.wait_for_load_state("networkidle")
    page.evaluate("document.fonts.ready")
    time.sleep(LOAD_WAIT)


def force_reveal_elements(page):
    page.evaluate("""() => {
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
            if (el.getBoundingClientRect().height > 0) {
                el.style.opacity = '1';
            }
        });
    }""")


def smooth_scroll_to(page, y):
    page.evaluate(f"window.scrollTo({{top: {y}, behavior: 'smooth'}})")
    for _ in range(50):
        time.sleep(0.05)
        current = page.evaluate("window.scrollY")
        if abs(current - y) <= 2:
            break


def capture_template(browser, html_path, name):
    context = browser.new_context(
        viewport={"width": VIEWPORT_WIDTH, "height": VIEWPORT_HEIGHT},
        device_scale_factor=1,
        reduced_motion="reduce",
    )
    page = context.new_page()

    try:
        url = f"file:///{html_path.as_posix()}"
        page.goto(url, wait_until="networkidle")
        wait_for_stable(page)

        total_height = page.evaluate("document.body.scrollHeight")
        safe_bottom = max(0, total_height - VIEWPORT_HEIGHT)
        safe_middle = max(0, int(total_height / 2 - VIEWPORT_HEIGHT / 2))

        page.evaluate("window.scrollTo(0, 0)")
        time.sleep(SCROLL_WAIT)
        force_reveal_elements(page)
        time.sleep(REVEAL_WAIT)
        page.screenshot(path=SCREENSHOTS_DIR / f"{name}-01.png")

        smooth_scroll_to(page, safe_middle)
        time.sleep(SCROLL_WAIT)
        force_reveal_elements(page)
        time.sleep(REVEAL_WAIT)
        page.screenshot(path=SCREENSHOTS_DIR / f"{name}-02.png")

        smooth_scroll_to(page, safe_bottom)
        time.sleep(SCROLL_WAIT)
        force_reveal_elements(page)
        time.sleep(REVEAL_WAIT)
        page.screenshot(path=SCREENSHOTS_DIR / f"{name}-03.png")
    finally:
        context.close()


def main():
    if len(sys.argv) < 2:
        print("Usage: python capture_one.py <folder-name>")
        sys.exit(1)
    name = sys.argv[1]
    html_path = TEMPLATES_DIR / name / f"{name}.html"
    if not html_path.exists():
        print(f"HTML not found: {html_path}")
        sys.exit(1)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            log(f"Capturing {name} ...")
            capture_template(browser, html_path, name)
            log(f"  -> {name}-01.png, {name}-02.png, {name}-03.png")
        finally:
            browser.close()


if __name__ == "__main__":
    main()
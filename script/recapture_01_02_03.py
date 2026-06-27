#!/usr/bin/env python3
"""Re-capture screenshots 01, 02 and 03 for each template with stable timing.

This script is an extended version of recapture_02_03.py. It captures the top,
middle and bottom of every template while fixing the "ghost/blur" issue caused by
continuous CSS animations and scroll-triggered reveals.

It fixes the paths so that the project root is used as the base directory, which
is one level above the `script/` folder where this file lives.
"""

import os
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

LOAD_WAIT = 2.0          # seconds after networkidle before first screenshot
SCROLL_WAIT = 1.5        # seconds for smooth scroll to settle
REVEAL_WAIT = 0.8        # seconds after forcing reveal elements visible


def log(msg):
    try:
        sys.stdout.write(msg + "\n")
        sys.stdout.flush()
    except Exception:
        pass
    with open(BASE_DIR / "recapture_01_02_03.log", "a", encoding="utf-8") as f:
        f.write(msg + "\n")
        f.flush()


# Remove old log files on start so we get a clean run log.
for old_log in (BASE_DIR / "recapture_01_02_03.log", BASE_DIR / "recapture_01_02_03.err"):
    try:
        old_log.unlink(missing_ok=True)
    except Exception:
        pass


def wait_for_stable(page):
    page.wait_for_load_state("networkidle")
    page.evaluate("document.fonts.ready")
    time.sleep(LOAD_WAIT)


def force_reveal_elements(page):
    """Force commonly hidden/animated elements into their final state."""
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
    # Create a fresh page per template to avoid memory/resource leaks that cause
    # page crashes after loading several heavy animated templates.
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

        # 01 (top)
        page.evaluate("window.scrollTo(0, 0)")
        time.sleep(SCROLL_WAIT)
        force_reveal_elements(page)
        time.sleep(REVEAL_WAIT)
        page.screenshot(path=SCREENSHOTS_DIR / f"{name}-01.png")

        # 02 (middle)
        smooth_scroll_to(page, safe_middle)
        time.sleep(SCROLL_WAIT)
        force_reveal_elements(page)
        time.sleep(REVEAL_WAIT)
        page.screenshot(path=SCREENSHOTS_DIR / f"{name}-02.png")

        # 03 (bottom)
        smooth_scroll_to(page, safe_bottom)
        time.sleep(SCROLL_WAIT)
        force_reveal_elements(page)
        time.sleep(REVEAL_WAIT)
        page.screenshot(path=SCREENSHOTS_DIR / f"{name}-03.png")
    finally:
        context.close()


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        template_dirs = sorted([d for d in TEMPLATES_DIR.iterdir() if d.is_dir()])
        total = len(template_dirs)
        errors = 0

        for idx, template_dir in enumerate(template_dirs, 1):
            html_file = template_dir / f"{template_dir.name}.html"
            if not html_file.exists():
                log(f"[{idx}/{total}] SKIP {template_dir.name}: HTML not found")
                continue

            log(f"[{idx}/{total}] Capturing {template_dir.name} ...")
            try:
                capture_template(browser, html_file, template_dir.name)
                log(f"  -> {template_dir.name}-01.png, {template_dir.name}-02.png, {template_dir.name}-03.png")
            except Exception as e:
                errors += 1
                log(f"  ERROR {template_dir.name}: {e}")

        browser.close()
        log(f"\nDone. {total - errors}/{total} templates recaptured. Errors: {errors}")


if __name__ == "__main__":
    main()

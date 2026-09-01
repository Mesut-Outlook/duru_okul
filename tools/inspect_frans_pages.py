#!/usr/bin/env python3
import os
import sys
import time
import re
from playwright.sync_api import sync_playwright

USER_DATA_DIR = os.path.expanduser("~/.config/noordhoff_browser_profile")
EBOOK_URL = "https://apps.noordhoff.nl/se/content/book/fe9559e5-2325-407a-a4a8-bcc3b16708da/ebook/23a8e547-a7d7-46e9-b45a-1895c6e5f429?page=1"

def ensure_login(page):
    for _ in range(25):
        url = page.url
        if ("bookshelf" in url or "se/content" in url or "ebook" in url) and "identity" not in url and "entree" not in url:
            return True
        try:
            if page.locator("text='via Entree'").count() > 0:
                page.locator("text='via Entree'").first.click(timeout=3000)
        except Exception:
            pass
        try:
            if "entree" in page.url:
                page.locator('.wayf__previousSelection, .previousSelection__item, .idp__submit').first.click(force=True, timeout=3000)
        except Exception:
            pass
        time.sleep(1.5)
    return False

def main():
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=False,
            viewport={"width": 1920, "height": 1080},
            device_scale_factor=2,
            args=["--start-maximized", "--no-sandbox"]
        )
        page = context.pages[0] if context.pages else context.new_page()
        page.goto(EBOOK_URL)
        ensure_login(page)
        time.sleep(5)
        
        print("Reader URL:", page.url)
        
        # Check input page number / total pages
        page_input = page.locator("input[type='number'], input[aria-label*='pagina'], [data-testid*='page'], .page-number")
        print("Page inputs count:", page_input.count())
        for idx in range(page_input.count()):
            try:
                print("  Input val:", page_input.nth(idx).input_value(), "attrs:", page_input.nth(idx).evaluate("e => ({max: e.max, min: e.min, val: e.value, placeholder: e.placeholder})"))
            except Exception:
                pass
                
        # Check all text elements around bottom bar
        bottom_texts = page.locator("footer, nav, [role='navigation'], [aria-label*='pagina'], [aria-label*='Pagina']").all()
        for b in bottom_texts:
            try:
                t = b.inner_text().strip().replace('\n', ' | ')
                if t:
                    print("  Nav text:", t)
            except Exception:
                pass
                
        # Let's inspect Boite a Gram link
        bag_link = page.locator("a[data-testid='80e92244-67c3-4b6a-bc2d-46ce836e6927']")
        if bag_link.count() > 0:
            print("Boite a Gram link href:", bag_link.first.get_attribute("href"))
            bag_link.first.click()
            time.sleep(4)
            print("After clicking Boite a Gram URL:", page.url)
            
        time.sleep(3)
        context.close()

if __name__ == "__main__":
    main()

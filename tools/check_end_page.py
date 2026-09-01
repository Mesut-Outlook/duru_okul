#!/usr/bin/env python3
import os
import sys
import time
import re
from playwright.sync_api import sync_playwright

USER_DATA_DIR = os.path.expanduser("~/.config/noordhoff_browser_profile")
EBOOK_BASE = "https://apps.noordhoff.nl/se/content/book/fe9559e5-2325-407a-a4a8-bcc3b16708da/ebook/23a8e547-a7d7-46e9-b45a-1895c6e5f429"

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
        page.goto(f"{EBOOK_BASE}?page=274")
        ensure_login(page)
        time.sleep(5)
        
        print("At page 274 URL:", page.url)
        
        # Let's check page numbers in the reader UI
        # In the reader, let's see what buttons/text show page count
        txts = page.locator("text=/\\d+\\s*\\/\\s*\\d+|van\\s*\\d+/").all()
        for t in txts:
            print("Found counter:", t.inner_text())
            
        # Try going to page 300
        page.goto(f"{EBOOK_BASE}?page=300")
        time.sleep(4)
        print("At page 300 URL:", page.url)
        page.screenshot(path="tools/page_300.png")
        
        # Try going to page 350
        page.goto(f"{EBOOK_BASE}?page=350")
        time.sleep(4)
        print("At page 350 URL:", page.url)
        page.screenshot(path="tools/page_350.png")

        context.close()

if __name__ == "__main__":
    main()

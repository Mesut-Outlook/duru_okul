#!/usr/bin/env python3
import os
import sys
import time
import re
from playwright.sync_api import sync_playwright

USER_DATA_DIR = os.path.expanduser("~/.config/noordhoff_browser_profile")
BOOKSHELF_URL = "https://apps.noordhoff.nl/my/nl/bookshelf"
COURSE_ID = "fe9559e5-2325-407a-a4a8-bcc3b16708da"
EBOOK_ID = "23a8e547-a7d7-46e9-b45a-1895c6e5f429"

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
        page.goto(BOOKSHELF_URL)
        ensure_login(page)
        time.sleep(3)
        
        # Go to page 274
        page.goto(f"https://apps.noordhoff.nl/se/content/book/{COURSE_ID}/ebook/{EBOOK_ID}?page=274")
        time.sleep(5)
        
        # Click Boite a Gram in sidebar
        bag_link = page.locator("a:has-text('Boîte à Gram'), [data-testid='80e92244-67c3-4b6a-bc2d-46ce836e6927']")
        if bag_link.count() > 0:
            print("Boite a Gram found, clicking...")
            bag_link.first.click()
            time.sleep(4)
            print("After click Boite a Gram URL:", page.url)
            page.screenshot(path="tools/frans_bag_start.png")
            
        # Let's see what is the current page number in URL
        m = re.search(r'page=(\d+)', page.url)
        start_bag = int(m.group(1)) if m else 290
        print(f"Boîte à Gram starts at page: {start_bag}")
        
        # Click next several times to find the last page
        for i in range(40):
            next_btn = page.locator("[data-testid='page-navigator-next-page'], [aria-label='Volgende pagina']")
            if next_btn.count() > 0 and next_btn.first.is_enabled():
                next_btn.first.click()
                time.sleep(1)
            else:
                print(f"Reached final page at URL: {page.url}")
                page.screenshot(path="tools/frans_final_page.png")
                break
                
        print("Final URL:", page.url)
        context.close()

if __name__ == "__main__":
    main()

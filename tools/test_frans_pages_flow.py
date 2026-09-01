#!/usr/bin/env python3
import os
import sys
import time
import re
from PIL import Image
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

def close_sidebar_if_open(page):
    try:
        menu_btn = page.locator("[data-testid='MenuIcon'], [aria-label='Menu'], [aria-label='Navigatie sluiten']")
        if menu_btn.count() > 0:
            menu_btn.first.click()
            time.sleep(1.5)
    except Exception:
        pass

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
        
        # Test loading chapter 1 page 18
        test_url = f"https://apps.noordhoff.nl/se/content/book/{COURSE_ID}/ebook/{EBOOK_ID}?page=18"
        print(f"Navigating to: {test_url}")
        page.goto(test_url)
        time.sleep(6)
        
        close_sidebar_if_open(page)
        time.sleep(2)
        
        print("Current URL:", page.url)
        page.screenshot(path="tools/frans_ch1_p18.png")
        
        # Test navigation to page 19
        next_btn = page.locator("[data-testid='page-navigator-next-page'], [aria-label='Volgende pagina']")
        if next_btn.count() > 0 and next_btn.first.is_enabled():
            print("Clicking next button...")
            next_btn.first.click()
        else:
            print("Pressing ArrowRight...")
            page.keyboard.press("ArrowRight")
            
        time.sleep(3)
        print("URL after next page:", page.url)
        page.screenshot(path="tools/frans_ch1_p19.png")
        
        # Test Boite a Gram start (around page 290-300)
        page.goto(f"https://apps.noordhoff.nl/se/content/book/{COURSE_ID}/ebook/{EBOOK_ID}?page=274")
        time.sleep(5)
        print("At page 274 URL:", page.url)
        page.screenshot(path="tools/frans_p274.png")
        
        # Let's inspect the page content / max page
        context.close()

if __name__ == "__main__":
    main()

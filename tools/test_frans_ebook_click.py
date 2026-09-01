#!/usr/bin/env python3
import os
import sys
import time
import re
from playwright.sync_api import sync_playwright

USER_DATA_DIR = os.path.expanduser("~/.config/noordhoff_browser_profile")
BOOKSHELF_URL = "https://apps.noordhoff.nl/my/nl/bookshelf"

def ensure_login(page):
    print("Ensuring login...")
    for _ in range(25):
        url = page.url
        print("  Current URL:", url[:90])
        if ("bookshelf" in url or "se/content" in url) and "identity" not in url and "entree" not in url:
            print("  -> Authenticated!")
            return True
        try:
            if page.locator("text='via Entree'").count() > 0:
                print("  Clicking via Entree...")
                page.locator("text='via Entree'").first.click(timeout=3000)
        except Exception:
            pass
        try:
            if "entree" in page.url:
                print("  Clicking Entree submit...")
                page.locator('.wayf__previousSelection, .previousSelection__item, .idp__submit').first.click(force=True, timeout=3000)
        except Exception:
            pass
        time.sleep(2)
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
        
        # Click Frans
        print("Finding Frans card...")
        page.wait_for_selector("[data-testid='new-product-card']", timeout=20000)
        cards = page.locator("[data-testid='new-product-card']").all()
        for c in cards:
            if "Frans" in c.inner_text() or "Grandes Lignes" in c.inner_text():
                c.click()
                break
                
        time.sleep(6)
        print("Course page URL:", page.url)
        
        # Click Chapter 1
        print("Clicking Chapter 1: '1 Poste, like, partage'...")
        page.wait_for_selector("text='1 Poste, like, partage'", timeout=15000)
        page.locator("text='1 Poste, like, partage'").first.click()
        time.sleep(4)
        print("Ch1 URL:", page.url)
        
        # Watch for new pages / popups
        new_pages = []
        context.on("page", lambda p: new_pages.append(p))
        
        print("Clicking 'E-book(s)'...")
        page.wait_for_selector("text='E-book(s)'", timeout=15000)
        page.locator("text='E-book(s)'").first.click()
        time.sleep(5)
        
        target_page = new_pages[0] if new_pages else page
        print(f"Target page URL: {target_page.url}")
        print(f"Target page Title: {target_page.title()}")
        target_page.screenshot(path="tools/frans_ebook_opened.png")
        
        # Save html
        with open("tools/frans_ebook_opened.html", "w", encoding="utf-8") as f:
            f.write(target_page.content())
            
        # Inspect elements
        print("\n--- Elements on E-book target page ---")
        items = target_page.locator("a, button, [role='button'], h1, h2, h3, h4, [data-testid], [aria-label]").all()
        for idx, it in enumerate(items[:50]):
            try:
                t = it.inner_text().strip().replace('\n', ' | ')
                h = it.get_attribute('href') or ''
                aria = it.get_attribute('aria-label') or ''
                tid = it.get_attribute('data-testid') or ''
                if t or aria:
                    print(f"  [{idx}] text='{t[:60]}' | href='{h}' | aria='{aria}' | testid='{tid}'")
            except Exception:
                pass
                
        time.sleep(5)
        context.close()

if __name__ == "__main__":
    main()

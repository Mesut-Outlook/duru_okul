#!/usr/bin/env python3
import os
import sys
import time
from playwright.sync_api import sync_playwright

USER_DATA_DIR = os.path.expanduser("~/.config/noordhoff_browser_profile")
FRANS_URL = "https://apps.noordhoff.nl/se/content/book/fe9559e5-2325-407a-a4a8-bcc3b16708da"

def ensure_login(page):
    for _ in range(15):
        url = page.url
        if "bookshelf" in url or "se/content" in url or "ebook" in url:
            if "identity" not in url and "entree" not in url:
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
        page.goto(FRANS_URL)
        ensure_login(page)
        time.sleep(5)
        
        print("URL after navigation:", page.url)
        
        # 1. Print all nav links in sidebar
        nav_elements = page.locator("nav a, [role='navigation'] a, div[role='button']").all()
        print(f"\n--- Sidebar items ({len(nav_elements)}) ---")
        for idx, el in enumerate(nav_elements):
            txt = el.inner_text().strip().replace('\n', ' | ')
            href = el.get_attribute("href") or ""
            print(f"[{idx}] text='{txt}' | href='{href}'")
            
        # 2. Click on Chapter 1: "1 Poste, like, partage"
        print("\nClicking on '1 Poste, like, partage'...")
        ch1 = page.locator("text='1 Poste, like, partage'")
        if ch1.count() > 0:
            ch1.first.click()
            time.sleep(4)
            page.screenshot(path="tools/frans_ch1.png")
            print("Ch1 URL:", page.url)
            
            # Print elements in Ch1
            items = page.locator("a, button, [role='button'], h1, h2, h3, h4, [data-testid]").all()
            print("\nElements in Ch1:")
            for it in items:
                t = it.inner_text().strip().replace('\n', ' ')
                h = it.get_attribute('href') or ''
                tid = it.get_attribute('data-testid') or ''
                if t and len(t) < 80:
                    if any(k in t.lower() for k in ['e-book', 'ebook', 'boek', 'bronnen', 'leer', 'werk', 'theorie', 'opdrachten', 'vocabulaire', 'grammaire', 'a', 'b', 'c', 'd', 'e', 'f']):
                        print(f"  * text='{t}' | href='{h}' | testid='{tid}'")
                        
        # 3. Check if there are E-books in the entire course
        print("\nSearching for any E-book links or buttons across the entire page...")
        all_ebook = page.locator("a:has-text('E-book'), a:has-text('e-book'), button:has-text('E-book'), button:has-text('e-book'), [aria-label*='e-book'], [aria-label*='E-book']").all()
        print(f"Found {len(all_ebook)} ebook elements")
        for eb in all_ebook:
            print("  Ebook:", eb.inner_text().strip().replace('\n', ' '), "| href:", eb.get_attribute('href'))
            
        # Let's also check the page HTML source for any "/ebook/" or "ebook" references
        html = page.content()
        ebook_matches = re.findall(r'href="([^"]*ebook[^"]*)"', html, re.IGNORECASE)
        print(f"\nDirect regex matches for href with ebook: {ebook_matches}")
        
        time.sleep(5)
        context.close()

if __name__ == "__main__":
    main()

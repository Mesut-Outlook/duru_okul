#!/usr/bin/env python3
import os
import sys
import time
from playwright.sync_api import sync_playwright

USER_DATA_DIR = os.path.expanduser("~/.config/noordhoff_browser_profile")
CH1_URL = "https://apps.noordhoff.nl/se/content/theme/ba71129b-0951-46d7-af6e-e018049e70ae"

def ensure_login(page):
    for _ in range(20):
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
        page.goto(CH1_URL)
        ensure_login(page)
        time.sleep(4)
        
        print("Clicking 'E-book(s)' under Snel naar...")
        ebook_btn = page.locator("text='E-book(s)'")
        if ebook_btn.count() > 0:
            ebook_btn.first.click()
            time.sleep(4)
            
        print("URL after clicking E-book(s):", page.url)
        page.screenshot(path="tools/frans_ebooks_menu.png")
        
        # Check all visible books/options
        print("\n--- Available Ebooks / Options ---")
        cards = page.locator("a, button, [role='button'], [data-testid]").all()
        for idx, c in enumerate(cards):
            try:
                t = c.inner_text().strip().replace('\n', ' | ')
                h = c.get_attribute('href') or ''
                if t and any(k in t.lower() for k in ['grandes', 'lignes', 'leerwerkboek', 'livre', 'cahier', 'tekstboek', 'werkboek', 'deel', 'havo', 'e-book']):
                    print(f"  [{idx}] text='{t}' | href='{h}'")
            except Exception:
                pass
                
        # If there's an ebook card, click the first one or print its link
        all_ebook_links = page.locator("a[href*='ebook']").all()
        print(f"\nDirect ebook links ({len(all_ebook_links)}):")
        for el in all_ebook_links:
            print("  Link:", el.inner_text().strip().replace('\n', ' '), "| href:", el.get_attribute('href'))
            
        if all_ebook_links:
            print(f"\nClicking first ebook link: {all_ebook_links[0].get_attribute('href')}")
            all_ebook_links[0].click()
            time.sleep(6)
            print("Reader URL:", page.url)
            page.screenshot(path="tools/frans_reader_opened.png")
            
            # Inspect reader TOC / sidebar
            # Look for table of contents / chapter outline button in reader
            toc_btn = page.locator("[aria-label*='inhoud'], [aria-label*='Inhoud'], [data-testid*='toc'], [aria-label*='Table of contents'], [aria-label*='Navigatie']")
            if toc_btn.count() > 0:
                print("Opening TOC...")
                toc_btn.first.click()
                time.sleep(3)
                page.screenshot(path="tools/frans_reader_toc.png")
                
        time.sleep(5)
        context.close()

if __name__ == "__main__":
    main()

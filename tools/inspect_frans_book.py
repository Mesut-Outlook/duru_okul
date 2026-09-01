#!/usr/bin/env python3
import os
import sys
import time
import json
import re
from playwright.sync_api import sync_playwright

USER_DATA_DIR = os.path.expanduser("~/.config/noordhoff_browser_profile")
BOOKSHELF_URL = "https://apps.noordhoff.nl/my/nl/bookshelf"

def ensure_login(page):
    """Handles automatic Entree / Somtoday SSO login flows."""
    for _ in range(20):
        url = page.url
        if ("bookshelf" in url or "content" in url or "ebook" in url) and "identity" not in url and "entree" not in url:
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
            viewport={"width": 1600, "height": 900},
            args=["--start-maximized", "--no-sandbox"]
        )
        page = context.pages[0] if context.pages else context.new_page()
        page.goto(BOOKSHELF_URL)
        ensure_login(page)
        time.sleep(3)
        
        page.wait_for_selector("[data-testid='new-product-card']", timeout=20000)
        cards = page.locator("[data-testid='new-product-card']").all()
        
        frans_idx = None
        for idx, card in enumerate(cards):
            txt = card.inner_text().strip()
            if "Frans" in txt or "Grandes Lignes" in txt:
                print(f"Found Frans card at index {idx}: {txt.replace(chr(10), ' | ')}")
                frans_idx = idx
                break
                
        if frans_idx is None:
            print("Frans card not found!")
            context.close()
            return
            
        print(f"Clicking Frans card (index {frans_idx})...")
        cards[frans_idx].click()
        time.sleep(6)
        
        print("Current URL:", page.url)
        page.screenshot(path="tools/frans_main.png")
        
        # Look for e-books / boeken link or tab or menu
        ebook_links = page.locator("a[href*='ebook'], button:has-text('e-book'), button:has-text('E-book'), a:has-text('E-book'), a:has-text('e-book'), [data-testid*='ebook'], [data-testid*='e-book']").all()
        print(f"\nFound {len(ebook_links)} potential ebook links/buttons:")
        for el in ebook_links:
            try:
                print("  Ebook el:", el.inner_text().strip().replace('\n', ' '), "| href:", el.get_attribute("href"))
            except Exception:
                pass
                
        # Check all links on page
        all_links = page.locator("a").all()
        print(f"\nTotal links on page: {len(all_links)}")
        for l in all_links:
            try:
                href = l.get_attribute("href") or ""
                txt = l.inner_text().strip().replace('\n', ' ')
                if "ebook" in href.lower() or "boek" in txt.lower() or "chap" in href.lower() or "thema" in href.lower() or "grandes" in txt.lower() or "lesstof" in href.lower():
                    print(f"  Link: txt='{txt}' | href='{href}'")
            except Exception:
                pass
                
        # Check if there are buttons with e-book icons or text
        btns = page.locator("button, [role='button']").all()
        print(f"\nButtons with ebook or book keywords:")
        for b in btns:
            try:
                txt = b.inner_text().strip().replace('\n', ' ')
                aria = b.get_attribute("aria-label") or ""
                if "boek" in txt.lower() or "ebook" in txt.lower() or "boek" in aria.lower() or "ebook" in aria.lower() or "bronnen" in txt.lower():
                    print(f"  Button: txt='{txt}' | aria='{aria}'")
            except Exception:
                pass
                
        time.sleep(3)
        context.close()

if __name__ == "__main__":
    main()

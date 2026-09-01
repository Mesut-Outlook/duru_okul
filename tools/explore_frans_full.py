#!/usr/bin/env python3
import os
import sys
import time
import re
from playwright.sync_api import sync_playwright

USER_DATA_DIR = os.path.expanduser("~/.config/noordhoff_browser_profile")
BOOKSHELF_URL = "https://apps.noordhoff.nl/my/nl/bookshelf"

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
        page.goto(BOOKSHELF_URL)
        ensure_login(page)
        time.sleep(3)
        
        page.wait_for_selector("[data-testid='new-product-card']", timeout=20000)
        cards = page.locator("[data-testid='new-product-card']").all()
        
        frans_idx = None
        for idx, card in enumerate(cards):
            txt = card.inner_text().strip()
            if "Frans" in txt or "Grandes Lignes" in txt:
                frans_idx = idx
                break
                
        print(f"Clicking Frans card (index {frans_idx})...")
        cards[frans_idx].click()
        time.sleep(5)
        
        print("Page URL:", page.url)
        page.wait_for_selector("text='0 On y va'", timeout=15000)
        
        # Let's find all sidebar items
        # Let's inspect all elements in the left sidebar
        sidebar_items = page.locator("nav li, nav div, [role='listitem'], div:has-text('0 On y va')").all()
        print(f"Found elements in sidebar...")
        
        # Check all visible texts in the left navigation
        all_text_elements = page.locator("text=/0 On y va|1 Poste|2 Du temps|3 En route|4 Le pont|5 Au resto|6 C'est moi|7 À tout prix|8 Le pont|Boîte à Gram/").all()
        print(f"Found {len(all_text_elements)} chapter elements in sidebar:")
        chapter_names = []
        for el in all_text_elements:
            t = el.inner_text().strip()
            if t and t not in chapter_names:
                chapter_names.append(t)
                print(f"  • {t}")
                
        # Now click on "1 Poste, like, partage"
        print("\nClicking on '1 Poste, like, partage'...")
        page.locator("text='1 Poste, like, partage'").first.click()
        time.sleep(4)
        
        print("URL after clicking Ch1:", page.url)
        page.screenshot(path="tools/frans_ch1_screen.png")
        
        # Save HTML
        with open("tools/frans_ch1_page.html", "w", encoding="utf-8") as f:
            f.write(page.content())
            
        # Check links / buttons on Ch1 page
        print("\n--- Interactive elements on Ch1 page ---")
        items = page.locator("a, button, [role='button'], h1, h2, h3, h4, [data-testid]").all()
        for it in items:
            try:
                t = it.inner_text().strip().replace('\n', ' ')
                h = it.get_attribute('href') or ''
                aria = it.get_attribute('aria-label') or ''
                tid = it.get_attribute('data-testid') or ''
                if t or aria:
                    print(f"  Tag: text='{t[:50]}' | href='{h}' | aria='{aria}' | testid='{tid}'")
            except Exception:
                pass
                
        # Let's see if there are other chapters or boeken / ebooks
        # Check all links containing "ebook"
        html = page.content()
        ebook_links = re.findall(r'href="([^"]*ebook[^"]*)"', html, re.IGNORECASE)
        print(f"\nRegex ebook links found: {ebook_links}")
        
        time.sleep(5)
        context.close()

if __name__ == "__main__":
    main()

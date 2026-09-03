import os
import sys
import time
import json
from playwright.sync_api import sync_playwright

USER_DATA_DIR = os.path.expanduser("~/.config/noordhoff_browser_profile")
BOOKSHELF_URL = "https://apps.noordhoff.nl/my/nl/bookshelf"

def ensure_login(page):
    for _ in range(25):
        url = page.url
        if ("bookshelf" in url or "se/content" in url or "ebook" in url) and "identity" not in url and "entree" not in url:
            return True
        try:
            entree_btn = page.locator("text='via Entree'")
            if entree_btn.count() > 0:
                entree_btn.first.click(timeout=3000)
        except Exception:
            pass
        try:
            if "entree" in page.url:
                page.locator('.wayf__previousSelection, .previousSelection__item, .idp__submit').first.click(force=True, timeout=3000)
        except Exception:
            pass
        time.sleep(1.5)
    return False

def inspect_duits():
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=True,
            viewport={"width": 1920, "height": 1080},
            args=["--no-sandbox"]
        )
        page = context.pages[0] if context.pages else context.new_page()
        page.goto(BOOKSHELF_URL)
        ensure_login(page)
        page.wait_for_selector("[data-testid='new-product-card']", timeout=20000)
        time.sleep(2)
        
        cards = page.locator("[data-testid='new-product-card']").all()
        print(f"Found {len(cards)} cards on bookshelf.")
        
        duits_indices = []
        for idx, c in enumerate(cards):
            txt = c.inner_text().strip()
            if "Duits" in txt or "Neue Kontakte" in txt:
                duits_indices.append((idx, txt))
                print(f"Card {idx}: {txt.replace(chr(10), ' | ')}")
                
        for idx, txt in duits_indices:
            print(f"\n================ INSPECTING CARD {idx} ================")
            page.goto(BOOKSHELF_URL)
            page.wait_for_selector("[data-testid='new-product-card']", timeout=20000)
            time.sleep(2)
            cards = page.locator("[data-testid='new-product-card']").all()
            cards[idx].click()
            time.sleep(5)
            print(f"Current URL: {page.url}")
            
            page.screenshot(path=f"/tmp/duits_card_{idx}_main.png")
            
            # Check for E-books button or tabs
            tabs = page.locator("[role='tab'], button, a").all()
            for t in tabs:
                try:
                    text = t.inner_text().strip()
                    if text in ["E-books", "E-book", "Boeken", "Theorie", "Opdrachten", "Overzicht"]:
                        print(f"Found Tab/Button: {text}")
                except:
                    pass

        context.close()

if __name__ == "__main__":
    inspect_duits()

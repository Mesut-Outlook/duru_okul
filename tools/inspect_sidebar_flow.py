import os
import sys
import time
from playwright.sync_api import sync_playwright

USER_DATA_DIR = os.path.expanduser("~/.config/noordhoff_browser_profile")
BOOKSHELF_URL = "https://apps.noordhoff.nl/my/nl/bookshelf"

def ensure_login(page):
    for _ in range(15):
        url = page.url
        if "bookshelf" in url and "identity" not in url and "entree" not in url:
            return True
        elif "se/content" in url:
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
            args=["--start-maximized", "--no-sandbox"]
        )
        page = context.pages[0] if context.pages else context.new_page()
        page.goto(BOOKSHELF_URL)
        ensure_login(page)
        
        page.wait_for_selector("[data-testid='new-product-card']", timeout=20000)
        time.sleep(2)
        cards = page.locator("[data-testid='new-product-card']").all()
        # Click Aardrijkskunde
        cards[0].click()
        time.sleep(5)
        
        print("Book page URL:", page.url)
        print("Book page Title:", page.title())
        
        # Take screenshot of the overview
        page.screenshot(path="/home/mesuto/Documents/PROJELER/duru_okul/tools/book_sidebar_overview.png")
        
        # Look for sidebar or menu items
        print("\n--- Listing all potential chapter / section / navigation items ---")
        locators = [
            "nav a", "nav button", "[role='treeitem']", "[role='menuitem']",
            "[role='tab']", "[data-testid*='chapter']", "[data-testid*='theme']",
            "[data-testid*='item']", "[data-testid*='node']", ".MuiListItem-root",
            ".MuiAccordion-root", "[aria-expanded]", "button[aria-controls]"
        ]
        
        for loc_str in locators:
            items = page.locator(loc_str).all()
            if items:
                print(f"\n[Selector '{loc_str}'] ({len(items)} items):")
                for idx, el in enumerate(items[:15]):
                    txt = el.inner_text().strip().replace('\n', ' -> ')
                    aria = el.get_attribute("aria-label") or ""
                    expanded = el.get_attribute("aria-expanded") or ""
                    testid = el.get_attribute("data-testid") or ""
                    href = el.get_attribute("href") or ""
                    if txt or aria:
                        print(f"  [{idx}] txt='{txt[:50]}' | aria='{aria}' | expanded={expanded} | testid='{testid}' | href='{href}'")

        # Let's also check all clickable text containing '1' or 'Thema' or 'Hoofdstuk'
        print("\n--- All items containing '1' or 'Thema' or 'Hoofdstuk' ---")
        h_items = page.locator("text=/Thema 1|Hoofdstuk 1|1\\.|1 /").all()
        for idx, el in enumerate(h_items[:20]):
            txt = el.inner_text().strip().replace('\n', ' -> ')
            print(f"  ({idx}) tag={el.evaluate('e => e.tagName')} text='{txt[:60]}'")
            
        print("\nKeeping browser open for 45 seconds for inspection...")
        time.sleep(45)
        context.close()

if __name__ == "__main__":
    main()

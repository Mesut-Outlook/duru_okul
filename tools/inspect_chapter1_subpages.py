import os
import sys
import time
from playwright.sync_api import sync_playwright

USER_DATA_DIR = os.path.expanduser("~/.config/noordhoff_browser_profile")
URL = "https://apps.noordhoff.nl/se/content/theme/ce2cb6c5-b958-4fa5-8857-19c1f270c3bb"

def ensure_login(page):
    for _ in range(15):
        url = page.url
        if "se/content" in url or ("bookshelf" in url and "identity" not in url and "entree" not in url):
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
        page.goto("https://apps.noordhoff.nl/my/nl/bookshelf")
        ensure_login(page)
        
        # Navigate directly to Chapter 1
        page.goto(URL)
        time.sleep(6)
        print("Chapter 1 URL:", page.url)
        print("Chapter 1 Title:", page.title())
        
        # Save overview screenshot
        page.screenshot(path="/home/mesuto/Documents/PROJELER/duru_okul/tools/chapter_1_overview.png")
        
        # List all sub-topics, lessons, cards, items inside Chapter 1
        print("\n--- Sub-sections inside Chapter 1 ---")
        items = page.locator("a, button, [role='button'], [data-testid], h2, h3, h4").all()
        for idx, el in enumerate(items):
            txt = el.inner_text().strip().replace('\n', ' -> ')
            href = el.get_attribute('href') or ''
            testid = el.get_attribute('data-testid') or ''
            if txt and len(txt) > 2 and not any(x in txt.lower() for x in ['cookie', 'privacy', 'voorwaarden', 'klantenservice', 'hulp']):
                print(f"[{idx:2d}] tag={el.evaluate('e => e.tagName')} | text='{txt[:65]}' | href='{href}' | testid='{testid}'")
                
        time.sleep(30)
        context.close()

if __name__ == "__main__":
    main()

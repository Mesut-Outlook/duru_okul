import os
import sys
import time
import json
from playwright.sync_api import sync_playwright

USER_DATA_DIR = os.path.expanduser("~/.config/noordhoff_browser_profile")
AUTH_FILE = "/home/mesuto/Documents/PROJELER/duru_okul/tools/auth_state.json"
TARGET_URL = "https://apps.noordhoff.nl/se/content/book/fd197c5c-1dfc-446b-bc2c-0b34e0643ef4/introduction"

def main():
    print("Launching persistent browser...")
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=False,
            viewport={"width": 1600, "height": 1000},
            args=["--start-maximized", "--no-sandbox"]
        )
        page = context.pages[0] if context.pages else context.new_page()
        page.goto("https://apps.noordhoff.nl/my/nl/bookshelf")
        
        print("Waiting for book shelf / reader...")
        # Check if already authenticated or if we need to wait
        for _ in range(30):
            url = page.url
            print(f"Current URL: {url} | Title: {page.title()}")
            if "bookshelf" in url or "se/content" in url:
                print("Authenticated! Navigating to book...")
                break
            time.sleep(2)
            
        page.goto(TARGET_URL)
        time.sleep(4)
        print(f"Book page URL: {page.url} | Title: {page.title()}")
        
        # Save storage state for headless reuse
        context.storage_state(path=AUTH_FILE)
        print(f"Saved auth state to {AUTH_FILE}")
        
        # Take screenshot of the book main page
        page.screenshot(path="/home/mesuto/Documents/PROJELER/duru_okul/tools/book_main.png")
        print("Screenshot saved to tools/book_main.png")
        
        # Let's inspect the DOM hierarchy, chapters (hoofdstukken), and ebook links
        content = page.content()
        with open("/home/mesuto/Documents/PROJELER/duru_okul/tools/page_source.html", "w") as f:
            f.write(content)
            
        # Inspect links, menu items, chapter items
        links = page.locator("a, button, [role='button'], [role='tab'], [role='treeitem'], .chapter, .hoofdstuk").all()
        print(f"\n--- Found {len(links)} interactive elements on book page ---")
        for idx, el in enumerate(links):
            try:
                txt = el.inner_text().strip().replace("\n", " ")
                href = el.get_attribute("href") or ""
                aria = el.get_attribute("aria-label") or ""
                testid = el.get_attribute("data-testid") or ""
                cls = el.get_attribute("class") or ""
                if txt or href or testid:
                    print(f"[{idx}] text='{txt[:50]}' | href='{href}' | testid='{testid}' | class='{cls[:40]}'")
            except Exception:
                pass
                
        print("\nKeeping browser open for 60s so you can interact or we can test navigation...")
        for i in range(12):
            time.sleep(5)
            print(f"[{ (i+1)*5 }s] Active URL: {page.url}")
            
        context.close()

if __name__ == "__main__":
    main()

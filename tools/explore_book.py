import os
import sys
import time
from playwright.sync_api import sync_playwright

USER_DATA_DIR = os.path.expanduser("~/.config/noordhoff_browser_profile")
URL = "https://apps.noordhoff.nl/my/nl/bookshelf?redirectPath=%2Fse%2Fcontent%2Ftheme%2F96c9a74a-a2c4-4d7d-8b7e-0042de398991%2Febook%2F729ba720-849b-43a5-84a2-e17bd7861a57&redirectPlatform=sep"

def main():
    print("Launching browser...")
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=False,
            viewport={"width": 1600, "height": 1000},
            args=["--start-maximized", "--no-sandbox"]
        )
        page = context.pages[0] if context.pages else context.new_page()
        page.goto(URL)
        
        # Auto-click via Entree if login screen appears
        for _ in range(10):
            time.sleep(1)
            btn = page.locator("text='via Entree'")
            if btn.count() > 0:
                print("Clicking 'via Entree'...")
                btn.first.click()
                break
                
        # Wait up to 30 seconds for book reader to load
        print("Waiting for book reader...")
        for i in range(30):
            time.sleep(2)
            url = page.url
            print(f"[{i*2}s] URL: {url} | Title: {page.title()}")
            
            # Check if we have loaded the book/reader UI
            if "content" in url or "ebook" in url or "theme" in url:
                # Look for typical content elements
                elements = page.locator("button, a, [role='button'], [data-testid], h1, h2, h3, nav").all()
                if len(elements) > 10:
                    print(f"Content loaded with {len(elements)} interactive/heading elements!")
                    break
                    
        time.sleep(5)
        # Screenshot
        page.screenshot(path="/home/mesuto/Documents/PROJELER/duru_okul/tools/book_full.png")
        print("Saved tools/book_full.png")
        
        # Print all text found on the page to understand structure
        print("\n--- Visible headings and text on page ---")
        for tag in ["h1", "h2", "h3", "h4", "button", "a", "[role='tab']", "[role='treeitem']"]:
            found = page.locator(tag).all()
            if found:
                print(f"\nTags <{tag}> ({len(found)}):")
                for el in found[:15]:
                    txt = el.inner_text().strip().replace("\n", " - ")
                    href = el.get_attribute("href") or ""
                    testid = el.get_attribute("data-testid") or ""
                    aria = el.get_attribute("aria-label") or ""
                    if txt or href or aria:
                        print(f"   * '{txt[:60]}' | href='{href}' | testid='{testid}' | aria='{aria}'")

        # Let's inspect frames if reader is inside an iframe
        print(f"\nTotal frames: {len(page.frames)}")
        for idx, fr in enumerate(page.frames):
            print(f"Frame #{idx}: URL={fr.url}")
            try:
                f_txt = fr.locator("body").inner_text()[:200].replace("\n", " ")
                print(f"  Frame text snippet: {f_txt}")
            except Exception:
                pass
                
        print("\nTarayıcıyı 60 saniye açık tutuyorum...")
        for i in range(12):
            time.sleep(5)
            
        context.close()

if __name__ == "__main__":
    main()

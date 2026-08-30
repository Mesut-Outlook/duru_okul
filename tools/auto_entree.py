import os
import sys
import time
from playwright.sync_api import sync_playwright

USER_DATA_DIR = os.path.expanduser("~/.config/noordhoff_browser_profile")
TARGET_URL = "https://apps.noordhoff.nl/my/nl/bookshelf?redirectPath=%2Fse%2Fcontent%2Ftheme%2F96c9a74a-a2c4-4d7d-8b7e-0042de398991%2Febook%2F729ba720-849b-43a5-84a2-e17bd7861a57&redirectPlatform=sep"

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
        page.goto(TARGET_URL)
        
        # Wait up to 30s, if 'via Entree' button appears, click it
        for _ in range(15):
            time.sleep(1)
            url = page.url
            print(f"Current URL: {url}")
            
            # Check for Entree button
            entree_btn = page.locator("text='via Entree'")
            if entree_btn.count() > 0:
                print("Found 'via Entree' button! Clicking it...")
                entree_btn.first.click()
                break
                
        # Now wait until we reach bookshelf or book reader
        print("Waiting for login redirect to complete...")
        for i in range(40):
            time.sleep(1)
            url = page.url
            title = page.title()
            if "content" in url or "theme" in url or "ebook" in url or "bookshelf" in url and "identity" not in url:
                print(f"[{i}s] Reached target! URL: {url} | Title: {title}")
                break
                
        # Wait for reader DOM to fully render
        time.sleep(5)
        print("\n--- FINAL URL:", page.url)
        print("--- FINAL TITLE:", page.title())
        
        # Take screenshot
        scr_path = "/home/mesuto/Documents/PROJELER/duru_okul/tools/book_reader.png"
        page.screenshot(path=scr_path)
        print(f"Saved screenshot: {scr_path}")
        
        # Save HTML for inspection
        with open("/home/mesuto/Documents/PROJELER/duru_okul/tools/reader.html", "w") as f:
            f.write(page.content())
            
        # Inspect elements
        print("\nInspecting interactive reader elements:")
        for fr in page.frames:
            print(f"Frame URL: {fr.url}")
            elems = fr.locator("button, a, [role='button'], [role='tab'], [data-testid], canvas, svg").all()
            print(f"Elements in frame: {len(elems)}")
            for idx, el in enumerate(elems[:35]):
                txt = el.inner_text().strip().replace("\n", " ")
                aria = el.get_attribute("aria-label") or ""
                testid = el.get_attribute("data-testid") or ""
                href = el.get_attribute("href") or ""
                cls = el.get_attribute("class") or ""
                tag = el.evaluate("e => e.tagName")
                print(f"  [{tag}] txt='{txt[:40]}' | aria='{aria}' | testid='{testid}' | href='{href[:40]}' | cls='{cls[:30]}'")

        print("\nKeeping open for 30 seconds for observation...")
        time.sleep(30)
        context.close()

if __name__ == "__main__":
    main()

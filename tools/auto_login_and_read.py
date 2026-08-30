import os
import sys
import time
from playwright.sync_api import sync_playwright

USER_DATA_DIR = os.path.expanduser("~/.config/noordhoff_browser_profile")
REDIRECT_URL = "https://apps.noordhoff.nl/my/nl/bookshelf?redirectPath=%2Fse%2Fcontent%2Ftheme%2F96c9a74a-a2c4-4d7d-8b7e-0042de398991%2Febook%2F729ba720-849b-43a5-84a2-e17bd7861a57&redirectPlatform=sep"

def handle_authentication(page):
    """Handles automatic clicks through Noordhoff -> Entree -> Somtoday if needed."""
    for step in range(30):
        url = page.url
        print(f"Auth check [{step}s]: URL={url}")
        
        if "se/content" in url or ("bookshelf" in url and "identity" not in url):
            print("Successfully reached internal Noordhoff platform!")
            return True
            
        # 1. Check for 'via Entree'
        if page.locator("text='via Entree'").count() > 0:
            print("Clicking 'via Entree'...")
            page.locator("text='via Entree'").first.click()
            time.sleep(2)
            continue
            
        # 2. Check for Entree school 'Login' button
        login_btn = page.locator("button:has-text('Login'), button:has-text('Inloggen')")
        if "entreeserviceprovider" in url and login_btn.count() > 0:
            print("Clicking Entree 'Login' button...")
            login_btn.first.click()
            time.sleep(2)
            continue
            
        time.sleep(1)
        
    return False

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
        page.goto(REDIRECT_URL)
        
        success = handle_authentication(page)
        print(f"Auth result: {success}")
        
        # Wait for the reader app to fully boot up
        print("Waiting for reader UI to load...")
        time.sleep(8)
        
        print("Final URL:", page.url)
        print("Final Title:", page.title())
        
        # Screenshot the actual reader interface
        page.screenshot(path="/home/mesuto/Documents/PROJELER/duru_okul/tools/reader_screen.png")
        print("Screenshot saved to tools/reader_screen.png")
        
        # Dump frames and elements
        for f_idx, fr in enumerate(page.frames):
            print(f"\n--- Frame {f_idx}: {fr.url} ---")
            elements = fr.locator("button, [role='button'], nav, a, input, canvas, svg, [data-testid], [aria-label]").all()
            print(f"Total interactive/labeled elements: {len(elements)}")
            for el in elements:
                try:
                    txt = el.inner_text().strip().replace("\n", " ")
                    aria = el.get_attribute("aria-label") or ""
                    testid = el.get_attribute("data-testid") or ""
                    cls = el.get_attribute("class") or ""
                    tag = el.evaluate("e => e.tagName")
                    if txt or aria or testid:
                        print(f"  [{tag}] aria='{aria}' | testid='{testid}' | text='{txt[:45]}' | class='{cls[:35]}'")
                except Exception:
                    pass

        print("\nKeeping open for 45 seconds for inspection...")
        for i in range(9):
            time.sleep(5)
            
        context.close()

if __name__ == "__main__":
    main()

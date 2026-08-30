import os
import sys
import time
from playwright.sync_api import sync_playwright

USER_DATA_DIR = os.path.expanduser("~/.config/noordhoff_browser_profile")
REDIRECT_URL = "https://apps.noordhoff.nl/my/nl/bookshelf?redirectPath=%2Fse%2Fcontent%2Ftheme%2F96c9a74a-a2c4-4d7d-8b7e-0042de398991%2Febook%2F729ba720-849b-43a5-84a2-e17bd7861a57&redirectPlatform=sep"

def handle_login(page):
    print("Checking login state...")
    for _ in range(20):
        url = page.url
        print(f"  URL: {url[:100]}")
        if "se/content" in url or ("bookshelf" in url and "identity" not in url and "entree" not in url):
            print("Successfully authenticated and on platform!")
            return True
            
        try:
            entree_btn = page.locator("text='via Entree'")
            if entree_btn.count() > 0:
                print("  Clicking 'via Entree'...")
                entree_btn.first.click(timeout=3000)
        except Exception:
            pass
            
        try:
            if "entreeserviceprovider" in page.url:
                login_btn = page.locator(".idp__submit, button:has-text('Login')")
                if login_btn.count() > 0:
                    print("  Clicking Entree submit...")
                    login_btn.first.dispatch_event("click")
        except Exception:
            pass
            
        time.sleep(2)
    return False

def main():
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=False,
            viewport={"width": 1600, "height": 1000},
            args=["--start-maximized", "--no-sandbox"]
        )
        page = context.pages[0] if context.pages else context.new_page()
        page.goto(REDIRECT_URL)
        
        handle_login(page)
        
        # Wait for reader to settle
        print("Waiting 10s for reader elements to load...")
        time.sleep(10)
        
        print("\n--- Current Page Status ---")
        print("URL:", page.url)
        print("Title:", page.title())
        
        # Save screenshot
        scr = "/home/mesuto/Documents/PROJELER/duru_okul/tools/reader_live.png"
        page.screenshot(path=scr)
        print(f"Screenshot saved: {scr}")
        
        # Check all frames
        print(f"\nFrames count: {len(page.frames)}")
        for idx, fr in enumerate(page.frames):
            print(f"\n[Frame {idx}] URL: {fr.url}")
            try:
                # Find interactive elements and text
                elements = fr.locator("button, [role='button'], nav, a, input, canvas, svg, [data-testid], [aria-label]").all()
                print(f"  Total elements in frame {idx}: {len(elements)}")
                for el in elements:
                    try:
                        txt = el.inner_text().strip().replace('\n', ' ')
                        aria = el.get_attribute("aria-label") or ""
                        testid = el.get_attribute("data-testid") or ""
                        cls = el.get_attribute("class") or ""
                        tag = el.evaluate("e => e.tagName")
                        if txt or aria or testid:
                            print(f"    [{tag}] aria='{aria}' | testid='{testid}' | text='{txt[:40]}' | class='{cls[:30]}'")
                    except Exception:
                        pass
            except Exception as e:
                print("  Frame error:", e)
                
        print("\nKeeping open for 40 seconds...")
        for i in range(8):
            time.sleep(5)
            
        context.close()

if __name__ == "__main__":
    main()

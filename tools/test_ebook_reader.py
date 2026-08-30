import os
import sys
import time
from playwright.sync_api import sync_playwright

USER_DATA_DIR = os.path.expanduser("~/.config/noordhoff_browser_profile")
BOOKSHELF_URL = "https://apps.noordhoff.nl/my/nl/bookshelf"

def handle_login(page):
    print("Checking login state...")
    for _ in range(15):
        url = page.url
        if "se/content" in url or ("bookshelf" in url and "identity" not in url and "entree" not in url):
            print("Authenticated!")
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
            
        time.sleep(1.5)
    return False

def main():
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=False,
            viewport={"width": 1920, "height": 1080},
            device_scale_factor=2, # High DPI for crisp screenshot quality
            args=["--start-maximized", "--no-sandbox"]
        )
        page = context.pages[0] if context.pages else context.new_page()
        page.goto(BOOKSHELF_URL)
        handle_login(page)
        
        time.sleep(4)
        print("Bookshelf page URL:", page.url)
        
        # Click on Aardrijkskunde / first book
        cards = page.locator("[data-testid='new-product-card']").all()
        if cards:
            print("Opening first book card...")
            cards[0].click()
            time.sleep(4)
            
        # Click on Leerwerkboek
        leerwerkboek = page.locator("text='Leerwerkboek'")
        if leerwerkboek.count() > 0:
            print("Clicking 'Leerwerkboek'...")
            leerwerkboek.first.click()
            time.sleep(6)
            
        print("Reader URL:", page.url)
        print("Reader Title:", page.title())
        
        # Take initial reader screenshot
        page.screenshot(path="/home/mesuto/Documents/PROJELER/duru_okul/tools/page_1_raw.png")
        print("Saved tools/page_1_raw.png")
        
        # Let's inspect reader navigation buttons (next, prev, zoom, toc)
        print("\n--- Reader Controls Inspection ---")
        controls = page.locator("button, [role='button'], nav, input, [aria-label]").all()
        for idx, el in enumerate(controls):
            try:
                aria = el.get_attribute("aria-label") or ""
                testid = el.get_attribute("data-testid") or ""
                txt = el.inner_text().strip().replace("\n", " ")
                cls = el.get_attribute("class") or ""
                tag = el.evaluate("e => e.tagName")
                if aria or testid or ("next" in cls.lower() or "prev" in cls.lower() or "page" in cls.lower()):
                    print(f"[{idx}] <{tag}> aria='{aria}' | testid='{testid}' | text='{txt[:30]}' | class='{cls[:35]}'")
            except Exception:
                pass
                
        # Test keyboard navigation ArrowRight
        print("\nTesting ArrowRight navigation...")
        for p_num in range(2, 5):
            page.keyboard.press("ArrowRight")
            time.sleep(2)
            scr = f"/home/mesuto/Documents/PROJELER/duru_okul/tools/page_{p_num}_test.png"
            page.screenshot(path=scr)
            print(f"Page {p_num} screenshot saved to {scr}")
            
        print("\nWaiting 20 seconds before closing...")
        time.sleep(20)
        context.close()

if __name__ == "__main__":
    main()

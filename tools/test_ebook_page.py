import os
import sys
import time
from playwright.sync_api import sync_playwright

USER_DATA_DIR = os.path.expanduser("~/.config/noordhoff_browser_profile")
EBOOK_URL = "https://apps.noordhoff.nl/se/content/theme/96c9a74a-a2c4-4d7d-8b7e-0042de398991/ebook/729ba720-849b-43a5-84a2-e17bd7861a57"

def main():
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=False,
            viewport={"width": 1600, "height": 1000},
            args=["--start-maximized", "--no-sandbox"]
        )
        page = context.pages[0] if context.pages else context.new_page()
        print("Navigating to ebook URL:", EBOOK_URL)
        page.goto(EBOOK_URL)
        
        # Wait up to 30 seconds for React rendering
        print("Waiting for page rendering...")
        for i in range(15):
            time.sleep(2)
            url = page.url
            print(f"[{ (i+1)*2 }s] URL: {url} | Title: {page.title()}")
            
            # Check for iframes or canvas or reader elements
            frames = page.frames
            if len(frames) > 1:
                print(f"Detected {len(frames)} frames!")
                for f_idx, fr in enumerate(frames):
                    print(f"  Frame {f_idx}: {fr.url}")
            
            # Check for ebook container or buttons
            buttons = page.locator("button, [role='button'], canvas, iframe, svg, [data-testid], .page, .page-wrapper").all()
            if len(buttons) > 5:
                print(f"Found {len(buttons)} elements!")
                break
                
        time.sleep(5)
        page.screenshot(path="/home/mesuto/Documents/PROJELER/duru_okul/tools/ebook_rendered.png")
        print("Screenshot saved to tools/ebook_rendered.png")
        
        # Save HTML
        with open("/home/mesuto/Documents/PROJELER/duru_okul/tools/ebook_source.html", "w") as f:
            f.write(page.content())
            
        print("\n--- Inspecting interactive elements ---")
        for idx, el in enumerate(page.locator("button, [role='button'], nav, a, input, canvas").all()[:40]):
            try:
                txt = el.inner_text().strip().replace("\n", " ")
                aria = el.get_attribute("aria-label") or ""
                testid = el.get_attribute("data-testid") or ""
                cls = el.get_attribute("class") or ""
                tag = el.evaluate("e => e.tagName")
                print(f"  [{tag}] aria='{aria}' | testid='{testid}' | text='{txt[:40]}' | cls='{cls[:30]}'")
            except Exception:
                pass
                
        # Also check all frames
        for fr in page.frames:
            if fr != page.main_frame:
                print(f"\n--- In Frame {fr.url} ---")
                try:
                    f_elems = fr.locator("button, [role='button'], canvas, img, .page").all()
                    print(f"Elements in frame: {len(f_elems)}")
                    for el in f_elems[:20]:
                        print(" ", el.evaluate("e => e.outerHTML[:120]"))
                except Exception as ex:
                    print("  Frame error:", ex)
                    
        print("\nKeeping open for 20s...")
        time.sleep(20)
        context.close()

if __name__ == "__main__":
    main()

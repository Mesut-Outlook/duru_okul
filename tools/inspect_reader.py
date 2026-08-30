import os
import sys
import time
from playwright.sync_api import sync_playwright

USER_DATA_DIR = os.path.expanduser("~/.config/noordhoff_browser_profile")
URL = "https://apps.noordhoff.nl/my/nl/bookshelf?redirectPath=%2Fse%2Fcontent%2Ftheme%2F96c9a74a-a2c4-4d7d-8b7e-0042de398991%2Febook%2F729ba720-849b-43a5-84a2-e17bd7861a57&redirectPlatform=sep"

def main():
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=False,
            viewport={"width": 1600, "height": 1000},
            args=["--start-maximized", "--no-sandbox"]
        )
        page = context.pages[0] if context.pages else context.new_page()
        page.goto(URL, wait_until="networkidle", timeout=60000)
        print("Initial URL:", page.url)
        
        # Wait a few seconds for SPA routing / reader iframe
        time.sleep(5)
        print("Loaded URL:", page.url)
        print("Title:", page.title())
        
        # Take screenshot of the reader
        screenshot_path = "/home/mesuto/Documents/PROJELER/duru_okul/tools/reader_preview.png"
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")
        
        # Inspect frames and elements
        frames = page.frames
        print(f"Total frames: {len(frames)}")
        for idx, f in enumerate(frames):
            print(f"Frame {idx}: name='{f.name}', url='{f.url[:100]}'")
            
        # Check buttons, controls, navigation
        buttons = page.locator("button, [role='button'], a").all()
        print(f"Found {len(buttons)} interactive elements on main page.")
        
        # Print text or aria-labels of some key controls
        for b in buttons[:25]:
            try:
                aria = b.get_attribute("aria-label") or ""
                text = b.inner_text().strip()
                cid = b.get_attribute("class") or ""
                if aria or text:
                    print(f"  [Elem] text='{text}' | aria='{aria}' | class='{cid}'")
            except Exception:
                pass
                
        # Keep open for a bit so we can inspect or user can see
        time.sleep(10)
        context.close()

if __name__ == "__main__":
    main()

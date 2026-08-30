import os
import sys
import time
from playwright.sync_api import sync_playwright

USER_DATA_DIR = os.path.expanduser("~/.config/noordhoff_browser_profile")
URL = "https://apps.noordhoff.nl/my/nl/bookshelf?redirectPath=%2Fse%2Fcontent%2Ftheme%2F96c9a74a-a2c4-4d7d-8b7e-0042de398991%2Febook%2F729ba720-849b-43a5-84a2-e17bd7861a57&redirectPlatform=sep"

def main():
    print("Starting Playwright browser...")
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=False,
            viewport=None,
            args=["--start-maximized", "--no-sandbox"]
        )
        
        # If no page open, open one
        if not context.pages:
            page = context.new_page()
            page.goto(URL)
        else:
            page = context.pages[0]
            # Navigate to URL if on blank/login
            if "about:blank" in page.url or "identity/ui" in page.url:
                page.goto(URL)

        print("\n=======================================================")
        print("Tarayıcı açık. Lütfen kitap sayfasına gidin / tıklayın.")
        print("Tüm açık sekmeler taranıyor...")
        print("=======================================================\n")
        
        while True:
            pages = context.pages
            for idx, p_obj in enumerate(pages):
                try:
                    u = p_obj.url
                    t = p_obj.title()
                    print(f"[Sekme {idx+1}/{len(pages)}] Title: '{t}' | URL: {u}")
                    
                    # If this looks like the reader or ebook page
                    if "ebook" in u or "content" in u or "theme" in u or "sep" in u:
                        print(f"\n>>> Kitap Okuyucu Tespit Edildi! (Sekme {idx+1}) <<<")
                        p_obj.bring_to_front()
                        time.sleep(2)
                        
                        # Screenshot
                        scr = f"/home/mesuto/Documents/PROJELER/duru_okul/tools/tab_{idx}_screenshot.png"
                        p_obj.screenshot(path=scr)
                        print(f"Ekran görüntüsü alındı: {scr}")
                        
                        # Inspect frames
                        print(f"Frames ({len(p_obj.frames)}):")
                        for f_idx, fr in enumerate(p_obj.frames):
                            print(f"  Frame {f_idx}: url={fr.url}")
                            # Check reader elements in this frame
                            try:
                                btns = fr.locator("button, [role='button'], nav, canvas, svg, [data-testid], .navigation-button, .page-button, [aria-label]").all()
                                print(f"    Frame {f_idx} bulunan etkileşimli element sayısı: {len(btns)}")
                                for b in btns[:20]:
                                    aria = b.get_attribute("aria-label") or ""
                                    text = b.inner_text().strip().replace("\n", " ")
                                    testid = b.get_attribute("data-testid") or ""
                                    cls = b.get_attribute("class") or ""
                                    if aria or text or testid:
                                        print(f"      -> text='{text[:25]}' | aria='{aria}' | testid='{testid}' | class='{cls[:30]}'")
                            except Exception as ex:
                                pass
                except Exception as e:
                    pass
            time.sleep(4)

if __name__ == "__main__":
    main()

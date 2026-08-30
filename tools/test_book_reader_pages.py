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
                print("Clicking 'via Entree'...")
                entree_btn.first.click(timeout=3000)
        except Exception:
            pass
            
        try:
            if "entreeserviceprovider" in page.url:
                login_btn = page.locator(".idp__submit, button:has-text('Login')")
                if login_btn.count() > 0:
                    print("Clicking Entree submit...")
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
            args=["--start-maximized", "--no-sandbox"]
        )
        page = context.pages[0] if context.pages else context.new_page()
        page.goto(BOOKSHELF_URL)
        handle_login(page)
        
        time.sleep(5)
        print("Bookshelf page URL:", page.url)
        
        # Let's list all books on bookshelf
        cards = page.locator("[data-testid='new-product-card']").all()
        print(f"\n--- Bookshelf contains {len(cards)} books ---")
        for idx, card in enumerate(cards):
            txt = card.inner_text().replace('\n', ' | ')
            print(f"[{idx}] {txt}")
            
        # Let's click on the first book (or buiteNLand / Natuurkunde / Geschiedenis)
        if cards:
            print("\nClicking on card 0...")
            cards[0].click()
            time.sleep(5)
            print("Book inside URL:", page.url)
            print("Book inside Title:", page.title())
            
            # Save screenshot of the book overview / chapters
            page.screenshot(path="/home/mesuto/Documents/PROJELER/duru_okul/tools/book_chapters_view.png")
            print("Saved tools/book_chapters_view.png")
            
            # Look for E-book buttons or chapter links
            ebook_links = page.locator("a:has-text('E-book'), button:has-text('E-book'), [data-testid*='ebook'], [aria-label*='E-book']").all()
            print(f"\nFound {len(ebook_links)} E-book links/buttons.")
            for el in ebook_links:
                print("  E-book elem:", el.inner_text().strip(), el.get_attribute("href"))
                
            # If no direct E-book link, let's list all links & buttons inside the book page
            all_inside = page.locator("a, button, [role='button'], [role='tab'], h2, h3, h4").all()
            print(f"\nAll elements inside book ({len(all_inside)}):")
            for el in all_inside[:30]:
                t = el.inner_text().strip().replace('\n', ' ')
                h = el.get_attribute('href') or ''
                a = el.get_attribute('aria-label') or ''
                testid = el.get_attribute('data-testid') or ''
                if t or h or a:
                    print(f"  * text='{t[:45]}' | href='{h[:45]}' | testid='{testid}' | aria='{a}'")
            
            # If there's an ebook button, let's click it
            if ebook_links:
                print("\nOpening E-book...")
                ebook_links[0].click()
                time.sleep(6)
                print("Ebook reader URL:", page.url)
                page.screenshot(path="/home/mesuto/Documents/PROJELER/duru_okul/tools/ebook_reader_view.png")
                print("Saved tools/ebook_reader_view.png")
                
                # Check reader frames / pages
                print(f"Total frames in reader: {len(page.frames)}")
                for f_idx, fr in enumerate(page.frames):
                    print(f"Frame {f_idx}: {fr.url}")
                    
        print("\nKeeping open for 30 seconds...")
        time.sleep(30)
        context.close()

if __name__ == "__main__":
    main()

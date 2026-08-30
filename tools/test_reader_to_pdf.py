import os
import sys
import time
from PIL import Image
from playwright.sync_api import sync_playwright

USER_DATA_DIR = os.path.expanduser("~/.config/noordhoff_browser_profile")
BOOKSHELF_URL = "https://apps.noordhoff.nl/my/nl/bookshelf"
OUTPUT_DIR = "/home/mesuto/Documents/PROJELER/duru_okul/tools/captured_pages"

def ensure_login(page):
    print("Checking auth state...")
    for step in range(20):
        url = page.url
        print(f"  [{step}s] URL:", url[:90])
        if "bookshelf" in url and "identity" not in url and "entree" not in url:
            print("Successfully reached Bookshelf!")
            return True
        elif "se/content" in url:
            print("Successfully reached content!")
            return True
            
        try:
            entree_btn = page.locator("text='via Entree'")
            if entree_btn.count() > 0:
                print("  Clicking via Entree...")
                entree_btn.first.click(timeout=3000)
        except Exception:
            pass
            
        try:
            if "entree" in page.url:
                page.locator('.wayf__previousSelection, .previousSelection__item, .idp__submit').first.click(force=True, timeout=3000)
        except Exception:
            pass
            
        time.sleep(1.5)
    return False

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=False,
            viewport={"width": 1920, "height": 1080},
            device_scale_factor=2,  # Crisp high resolution
            args=["--start-maximized", "--no-sandbox"]
        )
        page = context.pages[0] if context.pages else context.new_page()
        page.goto(BOOKSHELF_URL)
        ensure_login(page)
        
        # Wait for bookshelf cards to render
        print("Waiting for book cards to load...")
        page.wait_for_selector("[data-testid='new-product-card']", timeout=15000)
        
        cards = page.locator("[data-testid='new-product-card']").all()
        print(f"\n--- Bookshelf: {len(cards)} books found ---")
        for idx, c in enumerate(cards):
            print(f"  [{idx}] {c.inner_text().replace(chr(10), ' | ')}")
            
        # Select first book (Aardrijkskunde / buiteNLand 3 havo)
        print("\nOpening Book #0...")
        cards[0].click()
        time.sleep(5)
        
        # Click on Leerwerkboek / E-book
        leerwerkboek = page.locator("text='Leerwerkboek'")
        if leerwerkboek.count() > 0:
            print(f"Opening '{leerwerkboek.first.inner_text()}'...")
            leerwerkboek.first.click()
            time.sleep(6)
            
        print("Reader URL:", page.url)
        print("Reader Title:", page.title())
        
        # Capture 5 test pages
        captured_images = []
        print("\n--- Starting 5-Page Capture Test ---")
        for page_idx in range(1, 6):
            time.sleep(2)
            img_path = os.path.join(OUTPUT_DIR, f"page_{page_idx:03d}.png")
            page.screenshot(path=img_path)
            captured_images.append(img_path)
            print(f"  [✓] Page {page_idx} captured -> {img_path}")
            
            # Press ArrowRight to turn page
            page.keyboard.press("ArrowRight")
            
        # Convert to PDF
        pdf_path = "/home/mesuto/Documents/PROJELER/duru_okul/tools/test_book_output.pdf"
        print(f"\nCombining {len(captured_images)} pages into PDF: {pdf_path}...")
        
        pil_images = []
        for img_file in captured_images:
            im = Image.open(img_file).convert("RGB")
            pil_images.append(im)
            
        if pil_images:
            pil_images[0].save(
                pdf_path,
                save_all=True,
                append_images=pil_images[1:],
                resolution=150.0
            )
            print(f"SUCCESS! PDF created: {pdf_path} (Size: {os.path.getsize(pdf_path)/1024:.1f} KB)")
            
        print("\nWaiting 10s before finish...")
        time.sleep(10)
        context.close()

if __name__ == "__main__":
    main()

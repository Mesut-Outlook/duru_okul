import os
import sys
import time
from playwright.sync_api import sync_playwright

USER_DATA_DIR = os.path.expanduser("~/.config/noordhoff_browser_profile")
BOOKSHELF_URL = "https://apps.noordhoff.nl/my/nl/bookshelf"

def ensure_login(page):
    for _ in range(15):
        url = page.url
        if "bookshelf" in url and "identity" not in url and "entree" not in url:
            return True
        elif "se/content" in url:
            return True
        try:
            if page.locator("text='via Entree'").count() > 0:
                page.locator("text='via Entree'").first.click(timeout=3000)
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
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=False,
            viewport={"width": 1920, "height": 1080},
            device_scale_factor=2,
            args=["--start-maximized", "--no-sandbox"]
        )
        page = context.pages[0] if context.pages else context.new_page()
        page.goto(BOOKSHELF_URL)
        ensure_login(page)
        
        # Click Aardrijkskunde
        page.wait_for_selector("[data-testid='new-product-card']", timeout=20000)
        cards = page.locator("[data-testid='new-product-card']").all()
        ak_card = None
        for c in cards:
            if "Aardrijkskunde" in c.inner_text() or "buiteNLand" in c.inner_text():
                ak_card = c
                break
        if not ak_card:
            ak_card = cards[0]
            
        print("Kitap açılıyor...")
        ak_card.click()
        time.sleep(5)
        
        # 1. Look for E-book(s) / Alle e-books link
        print("\n--- 'E-book' butonları aranıyor ---")
        ebook_links = page.locator("a:has-text('E-book'), button:has-text('E-book'), [data-testid*='ebook'], [aria-label*='E-book']").all()
        for idx, el in enumerate(ebook_links):
            print(f"  [{idx}] text='{el.inner_text().strip()}' | href='{el.get_attribute('href')}' | testid='{el.get_attribute('data-testid')}'")
            
        # Click 'E-book(s)' or 'Alle e-books'
        if ebook_links:
            print(f"Clicking E-book link [{ebook_links[0].inner_text().strip()}]...")
            ebook_links[0].click()
            time.sleep(5)
            
        # 2. Look for Leerwerkboek or available book versions
        print("\n--- E-books sayfasındaki kitaplar/seçenekler ---")
        page.screenshot(path="/home/mesuto/Documents/PROJELER/duru_okul/tools/ebooks_selection_page.png")
        sub_ebooks = page.locator("a, button, [role='button'], [data-testid]").all()
        for idx, el in enumerate(sub_ebooks):
            t = el.inner_text().strip().replace('\n', ' | ')
            h = el.get_attribute('href') or ''
            tid = el.get_attribute('data-testid') or ''
            if any(k in t.lower() for k in ['leerwerkboek', 'handboek', 'leerboek', 'antwoorden', 'deel', 'havo']):
                print(f"  * [{idx}] text='{t}' | href='{h}' | testid='{tid}'")
                
        # Click 'Leerwerkboek'
        lwb = page.locator("text='Leerwerkboek'")
        if lwb.count() > 0:
            print(f"\nClicking Leerwerkboek...")
            lwb.first.click()
            time.sleep(6)
            
        print("\n--- E-Kitap Okuyucu (Reader) Açıldı ---")
        print("Reader URL:", page.url)
        print("Reader Title:", page.title())
        page.screenshot(path="/home/mesuto/Documents/PROJELER/duru_okul/tools/actual_reader_active.png")
        
        # Inspect reader layout (page counter, next page button, zoom, table of contents)
        for el in page.locator("button, input, [role='button'], [aria-label]").all()[:40]:
            aria = el.get_attribute("aria-label") or ""
            tid = el.get_attribute("data-testid") or ""
            t = el.inner_text().strip().replace('\n', ' ')
            cls = el.get_attribute("class") or ""
            if aria or tid or t:
                print(f"  Control: aria='{aria}' | testid='{tid}' | text='{t}' | class='{cls[:30]}'")
                
        print("\nTarayıcı 45 saniye açık kalacak...")
        time.sleep(45)
        context.close()

if __name__ == "__main__":
    main()

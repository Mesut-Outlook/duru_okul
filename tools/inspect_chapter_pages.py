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
            headless=True,
            viewport={"width": 1920, "height": 1080},
            args=["--no-sandbox"]
        )
        page = context.pages[0] if context.pages else context.new_page()
        page.goto(BOOKSHELF_URL)
        ensure_login(page)
        
        # Click Aardrijkskunde (Index 0)
        page.wait_for_selector("[data-testid='new-product-card']", timeout=20000)
        cards = page.locator("[data-testid='new-product-card']").all()
        cards[0].click()
        time.sleep(4)
        
        # Click E-book(s)
        page.locator("a:has-text('E-book'), button:has-text('E-book'), [data-testid*='ebook']").first.click()
        time.sleep(4)
        
        # Click Leerwerkboek
        page.locator("text='Leerwerkboek'").first.click()
        time.sleep(6)
        
        print("Reader URL base:", page.url)
        
        # Let's inspect all main chapters in the reader menu
        # We can click on each chapter and check what URL / page number it navigates to!
        chapters = [
            "1 Wereldhandel in beweging",
            "2 Schatkist aarde?",
            "3 Migratie",
            "4 Energietransitie",
            "5 Gewapende conflicten",
            "Topografie"
        ]
        
        chapter_pages = []
        for ch_title in chapters:
            el = page.locator(f"text='{ch_title}'")
            if el.count() > 0:
                el.first.click()
                time.sleep(2)
                cur_url = page.url
                # Extract page number from URL ?page=X
                page_num = None
                if "page=" in cur_url:
                    page_num = int(cur_url.split("page=")[1].split("&")[0])
                print(f"📖 [{ch_title}] -> URL: {cur_url} (Page: {page_num})")
                chapter_pages.append({
                    "title": ch_title,
                    "start_page": page_num,
                    "url": cur_url
                })
                
        # Also check last page by checking total pages in reader
        # Let's check page-navigator or pagination info in reader
        page_inputs = page.locator("input, [aria-label*='pagina'], [data-testid*='page']").all()
        for pi in page_inputs:
            print("  Pagination element:", pi.get_attribute("value"), pi.get_attribute("aria-label"), pi.inner_text())
            
        print("\n--- Summary of Chapter Ranges ---")
        for i in range(len(chapter_pages)):
            start_p = chapter_pages[i]["start_page"]
            if i + 1 < len(chapter_pages):
                end_p = chapter_pages[i+1]["start_page"] - 1
            else:
                end_p = "END"
            print(f"Hoofdstuk: {chapter_pages[i]['title']} => Sayfa {start_p} - {end_p}")
            
        context.close()

if __name__ == "__main__":
    main()

import os
import sys
import time
import json
from playwright.sync_api import sync_playwright

USER_DATA_DIR = os.path.expanduser("~/.config/noordhoff_browser_profile")

COURSES = [
    {"name": "Neue Kontakte 3 havo - Editie 7", "url": "https://apps.noordhoff.nl/se/content/book/b5ae3b67-6f8f-47d7-92b7-e3057c772724"},
    {"name": "Neue Kontakte 3 havo - Editie 7.1", "url": "https://apps.noordhoff.nl/se/content/book/4d61e0f5-f254-413a-92df-88e95054c944"}
]

def ensure_login(page):
    for _ in range(25):
        url = page.url
        if ("bookshelf" in url or "se/content" in url or "ebook" in url) and "identity" not in url and "entree" not in url:
            return True
        try:
            entree_btn = page.locator("text='via Entree'")
            if entree_btn.count() > 0:
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

def inspect_course_details():
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=True,
            viewport={"width": 1920, "height": 1080},
            args=["--no-sandbox"]
        )
        page = context.pages[0] if context.pages else context.new_page()
        
        for c in COURSES:
            print(f"\n========================================================")
            print(f"Inspecting: {c['name']} ({c['url']})")
            print(f"========================================================")
            page.goto(c['url'])
            ensure_login(page)
            time.sleep(5)
            
            # Click E-books if available
            ebook_tabs = page.locator("button, a, [role='tab']").all()
            for eb in ebook_tabs:
                try:
                    txt = eb.inner_text().strip()
                    if "E-book" in txt:
                        print(f"Clicking E-book tab: {txt}")
                        eb.click()
                        time.sleep(3)
                        break
                except:
                    pass
                    
            page.screenshot(path=f"/tmp/course_{c['name'][:15].replace(' ', '_')}.png")
            
            # Find all links containing ebook or chapter
            links = page.locator("a").all()
            print("Links found:")
            for l in links:
                try:
                    href = l.get_attribute("href") or ""
                    txt = l.inner_text().strip().replace("\n", " ")
                    if href or txt:
                        if "ebook" in href or "content" in href or "kapitel" in txt.lower() or "leerwerkboek" in txt.lower() or "deel" in txt.lower():
                            print(f"  [Link] '{txt}' -> {href}")
                except:
                    pass
                    
            # Check cards / buttons
            cards = page.locator("div[role='button'], div[data-testid]").all()
            for card in cards:
                try:
                    txt = card.inner_text().strip().replace("\n", " ")
                    if "leerwerkboek" in txt.lower() or "kapitel" in txt.lower() or "tekstboek" in txt.lower() or "deel" in txt.lower():
                        print(f"  [Card] {txt[:100]}")
                except:
                    pass

        context.close()

if __name__ == "__main__":
    inspect_course_details()

#!/usr/bin/env python3
import os
import sys
import time
from playwright.sync_api import sync_playwright

USER_DATA_DIR = os.path.expanduser("~/.config/noordhoff_browser_profile")

COURSE_ID_ED7 = "b5ae3b67-6f8f-47d7-92b7-e3057c772724"
BUCH_A_ID = "8e824d31-cf14-4f42-876a-b25a84b47f33"
BUCH_B_ID = "7e751e87-5f77-454d-9866-a82dff6724e0"

def ensure_login(page):
    for _ in range(20):
        url = page.url
        if ("bookshelf" in url or "content" in url or "ebook" in url) and "identity" not in url and "entree" not in url:
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

def clean_ui(page):
    try:
        menu_close = page.locator("[aria-label='Navigatie sluiten'], [aria-label='Menu sluiten'], [data-testid='CloseIcon']")
        if menu_close.count() > 0 and menu_close.first.is_visible():
            menu_close.first.click()
            time.sleep(0.5)
    except:
        pass

def inspect_book_structure(page, book_id, book_name):
    print(f"\n==================================================")
    print(f"Inspecting {book_name} ({book_id})")
    print(f"==================================================")
    
    # Check page 6 (Übersicht) of the book to get page numbers
    url = f"https://apps.noordhoff.nl/se/content/book/{COURSE_ID_ED7}/ebook/{book_id}?page=6"
    page.goto(url)
    ensure_login(page)
    time.sleep(3)
    clean_ui(page)
    time.sleep(1)
    page.screenshot(path=f"/tmp/{book_name}_p6.png")
    
    # Also check page 7
    url = f"https://apps.noordhoff.nl/se/content/book/{COURSE_ID_ED7}/ebook/{book_id}?page=7"
    page.goto(url)
    time.sleep(2)
    clean_ui(page)
    page.screenshot(path=f"/tmp/{book_name}_p7.png")
    
    # Check total page count by going to high page or looking at input
    for test_p in [100, 150, 160, 180, 200]:
        page.goto(f"https://apps.noordhoff.nl/se/content/book/{COURSE_ID_ED7}/ebook/{book_id}?page={test_p}")
        time.sleep(2)
        clean_ui(page)
        curr_url = page.url
        print(f"  Tried page {test_p} -> Ended at URL: {curr_url}")

def main():
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=True,
            viewport={"width": 1920, "height": 1080},
            device_scale_factor=2,
            args=["--no-sandbox"]
        )
        page = context.pages[0] if context.pages else context.new_page()
        page.goto("https://apps.noordhoff.nl/my/nl/bookshelf")
        ensure_login(page)
        time.sleep(3)
        
        inspect_book_structure(page, BUCH_A_ID, "Buch_A")
        inspect_book_structure(page, BUCH_B_ID, "Buch_B")
        
        context.close()

if __name__ == "__main__":
    main()

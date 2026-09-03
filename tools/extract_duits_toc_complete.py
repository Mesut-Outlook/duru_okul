#!/usr/bin/env python3
import os
import sys
import time
import subprocess
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

def ocr_image(img_path):
    try:
        txt = subprocess.check_output([
            'tesseract', img_path, 'stdout',
            '--tessdata-dir', '/home/mesuto/Documents/PROJELER/duru_okul/inbox/tessdata',
            '-l', 'nld+eng'
        ], stderr=subprocess.DEVNULL).decode('utf-8')
        return txt
    except Exception as e:
        return ""

def scan_book_chapters(page, book_id, book_name):
    out_dir = f"/tmp/duits_scan_{book_name}"
    os.makedirs(out_dir, exist_ok=True)
    
    print(f"\n=======================================================")
    print(f"Scanning {book_name} for exact chapter divisions...")
    print(f"=======================================================")
    
    # We will sample every 4 pages from 6 to 150 to identify exact start & end of all chapters
    step_pages = list(range(6, 150, 4))
    results = {}
    
    for p_num in step_pages:
        url = f"https://apps.noordhoff.nl/se/content/book/{COURSE_ID_ED7}/ebook/{book_id}?page={p_num}"
        page.goto(url)
        time.sleep(3.0)
        clean_ui(page)
        time.sleep(0.5)
        
        shot_path = os.path.join(out_dir, f"p_{p_num:03d}.png")
        page.screenshot(path=shot_path)
        txt = ocr_image(shot_path)
        
        # Look for chapter indicators
        lines = [l.strip() for l in txt.split('\n') if l.strip()]
        relevant = [l for l in lines if any(k in l.lower() for k in ["kapitel", "brückenschlag", "umgebung", "gesundheit", "unterwegs", "veranstaltungen", "zukunft", "aktion", "wiederholung", "grammatik", "wortschatz", "sprachmittel", "inhalt"])]
        
        print(f"Page {p_num:3d}: {' | '.join(relevant[:3])}")
        results[p_num] = relevant

def main():
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=True,
            viewport={"width": 1920, "height": 1080},
            device_scale_factor=1,
            args=["--no-sandbox"]
        )
        page = context.pages[0] if context.pages else context.new_page()
        page.goto("https://apps.noordhoff.nl/my/nl/bookshelf")
        ensure_login(page)
        time.sleep(3)
        
        scan_book_chapters(page, BUCH_A_ID, "Buch_A")
        scan_book_chapters(page, BUCH_B_ID, "Buch_B")

        context.close()

if __name__ == "__main__":
    main()

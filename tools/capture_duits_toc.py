#!/usr/bin/env python3
import os
import sys
import time
from PIL import Image
from playwright.sync_api import sync_playwright

USER_DATA_DIR = os.path.expanduser("~/.config/noordhoff_browser_profile")

EBOOKS = [
    # Editie 7
    {
        "id_name": "Ed7_BuchA",
        "course_id": "b5ae3b67-6f8f-47d7-92b7-e3057c772724",
        "ebook_id": "8e824d31-cf14-4f42-876a-b25a84b47f33",
        "title": "Deutschbuch A (Ed 7)"
    },
    {
        "id_name": "Ed7_BuchB",
        "course_id": "b5ae3b67-6f8f-47d7-92b7-e3057c772724",
        "ebook_id": "7e751e87-5f77-454d-9866-a82dff6724e0",
        "title": "Deutschbuch B (Ed 7)"
    },
    # Editie 7.1
    {
        "id_name": "Ed71_Buch",
        "course_id": "4d61e0f5-f254-413a-92df-88e95054c944",
        "ebook_id": "53277c5f-4c13-4139-9a5d-445c9f1e358d",
        "title": "Deutschbuch (Ed 7.1)"
    }
]

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

def main():
    out_dir = "/home/mesuto/Documents/PROJELER/duru_okul/scratch/duits_inspect"
    os.makedirs(out_dir, exist_ok=True)
    
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
        
        for eb in EBOOKS:
            print(f"\nScanning first 6 pages of {eb['title']}...")
            for p_num in range(1, 7):
                url = f"https://apps.noordhoff.nl/se/content/book/{eb['course_id']}/ebook/{eb['ebook_id']}?page={p_num}"
                page.goto(url)
                time.sleep(2.5)
                clean_ui(page)
                time.sleep(0.5)
                
                shot_path = os.path.join(out_dir, f"{eb['id_name']}_page_{p_num}.png")
                page.screenshot(path=shot_path)
                print(f"  Page {p_num} captured -> {shot_path}")

        context.close()

if __name__ == "__main__":
    main()

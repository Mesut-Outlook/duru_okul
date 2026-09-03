#!/usr/bin/env python3
import os
import sys
import time
import json
import re
from playwright.sync_api import sync_playwright

USER_DATA_DIR = os.path.expanduser("~/.config/noordhoff_browser_profile")
BOOKSHELF_URL = "https://apps.noordhoff.nl/my/nl/bookshelf"

EBOOKS = [
    # Editie 7
    {
        "course_name": "Editie 7",
        "course_id": "b5ae3b67-6f8f-47d7-92b7-e3057c772724",
        "ebook_id": "8e824d31-cf14-4f42-876a-b25a84b47f33",
        "title": "Deutschbuch A (Ed 7)"
    },
    {
        "course_name": "Editie 7",
        "course_id": "b5ae3b67-6f8f-47d7-92b7-e3057c772724",
        "ebook_id": "7e751e87-5f77-454d-9866-a82dff6724e0",
        "title": "Deutschbuch B (Ed 7)"
    },
    # Editie 7.1
    {
        "course_name": "Editie 7.1",
        "course_id": "4d61e0f5-f254-413a-92df-88e95054c944",
        "ebook_id": "53277c5f-4c13-4139-9a5d-445c9f1e358d",
        "title": "Deutschbuch (Ed 7.1)"
    },
    {
        "course_name": "Editie 7.1",
        "course_id": "4d61e0f5-f254-413a-92df-88e95054c944",
        "ebook_id": "5e11462d-1509-4635-852c-d0cca044fa3f",
        "title": "Leerwerkboek Literatur (Ed 7.1)"
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

def inspect_ebook(page, eb):
    print(f"\n==================================================================")
    print(f"Opening {eb['title']} ({eb['course_name']})")
    print(f"==================================================================")
    reader_url = f"https://apps.noordhoff.nl/se/content/book/{eb['course_id']}/ebook/{eb['ebook_id']}?page=1"
    page.goto(reader_url)
    ensure_login(page)
    time.sleep(6)
    
    # Check current URL and page numbers
    print("Reader loaded, URL:", page.url)
    
    # Click TOC menu
    toc_btn = page.locator("[data-testid='MenuIcon'], [aria-label='Menu'], [aria-label='Inhoudsopgave']")
    if toc_btn.count() > 0:
        toc_btn.first.click()
        time.sleep(3)
        
    # Get all text from drawer / sidebar
    drawer = page.locator("nav, [role='dialog'], [role='region'], aside, .MuiDrawer-root, .MuiList-root")
    if drawer.count() > 0:
        txt = drawer.first.inner_text()
        print("TOC Drawer Content:")
        print(txt)
    else:
        # Fallback: get all clickable list items
        items = page.locator("li, button").all()
        for it in items:
            t = it.inner_text().strip()
            if len(t) > 0 and len(t) < 100:
                print(f"  Item: {t}")
                
    # Also find total pages
    inputs = page.locator("input, span").all()
    for inp in inputs:
        try:
            val = inp.get_attribute("value") or inp.inner_text()
            if "/" in val or (val.isdigit() and int(val) > 10):
                print(f"  Page info element: {val}")
        except:
            pass

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
        ensure_login(page)
        time.sleep(3)
        
        for eb in EBOOKS:
            inspect_ebook(page, eb)
            
        context.close()

if __name__ == "__main__":
    main()

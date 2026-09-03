#!/usr/bin/env python3
import os
import sys
import time
import json
import re
from playwright.sync_api import sync_playwright

USER_DATA_DIR = os.path.expanduser("~/.config/noordhoff_browser_profile")
BOOKSHELF_URL = "https://apps.noordhoff.nl/my/nl/bookshelf"

def ensure_login(page):
    """Handles automatic Entree / Somtoday SSO login flows."""
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

def inspect_card(card_index):
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
        
        page.wait_for_selector("[data-testid='new-product-card']", timeout=20000)
        cards = page.locator("[data-testid='new-product-card']").all()
        
        if card_index >= len(cards):
            print(f"Card {card_index} not found!")
            context.close()
            return
            
        card_txt = cards[card_index].inner_text().strip().replace('\n', ' | ')
        print(f"\n========================================================")
        print(f"Clicking Card {card_index}: {card_txt}")
        print(f"========================================================")
        cards[card_index].click()
        time.sleep(6)
        
        print("Course Main URL:", page.url)
        page.screenshot(path=f"tools/duits_card_{card_index}_main.png")
        
        # Look for e-books / boeken link or tab or menu
        # On Noordhoff, there's often a left sidebar or header tab for E-books / Bronnen / etc.
        ebook_elements = page.locator("a:has-text('E-book'), a:has-text('E-books'), button:has-text('E-book'), button:has-text('E-books'), [data-testid*='ebook']").all()
        print(f"Found {len(ebook_elements)} e-book triggers:")
        for el in ebook_elements:
            try:
                print("  Ebook el:", el.inner_text().strip().replace('\n', ' '), "| tag:", el.evaluate("e => e.tagName"))
            except:
                pass
                
        # Try clicking E-books if found
        if ebook_elements:
            print("Clicking first E-book trigger...")
            ebook_elements[0].click()
            time.sleep(5)
            print("After clicking E-book, URL:", page.url)
            page.screenshot(path=f"tools/duits_card_{card_index}_ebooks.png")
            
        # Check all links on page
        links = page.locator("a").all()
        print(f"Checking all links ({len(links)}):")
        for l in links:
            try:
                href = l.get_attribute("href") or ""
                txt = l.inner_text().strip().replace('\n', ' ')
                if "ebook" in href or "content" in href or "kapitel" in txt.lower() or "leerwerkboek" in txt.lower() or "neue" in txt.lower() or "kontakte" in txt.lower() or "tekst" in txt.lower() or "werk" in txt.lower():
                    print(f"  Link: '{txt}' -> href: {href}")
            except:
                pass

        # Check buttons or cards in the content area
        buttons = page.locator("button, div[role='button'], div[data-testid]").all()
        for b in buttons:
            try:
                txt = b.inner_text().strip().replace('\n', ' ')
                if any(w in txt.lower() for w in ["leerwerkboek", "kapitel", "tekstboek", "werkboek", "theorie", "thema", "deel"]):
                    print(f"  Content Item: {txt[:120]}")
            except:
                pass
                
        time.sleep(2)
        context.close()

if __name__ == "__main__":
    idx = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    inspect_card(idx)

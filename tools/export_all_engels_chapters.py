#!/usr/bin/env python3
import os
import sys
import time
import re
from PIL import Image
from playwright.sync_api import sync_playwright

USER_DATA_DIR = os.path.expanduser("~/.config/noordhoff_browser_profile")
BOOKSHELF_URL = "https://apps.noordhoff.nl/my/nl/bookshelf"
COURSE_ID = "a7fecc29-5ede-4046-8d65-65cc4f19344b"
DEST_DIR = "/home/mesuto/Downloads/Eğitim/Duru"

# Stepping Stones 3 HAVO (Editie 7) Chapter Definitions
CHAPTERS = [
    # --- DEEL A (Book A) ---
    {
        "book_id": "6a1457cf-1943-482a-bdbd-120b3e5934c3",
        "num": 1,
        "title": "Hoofdstuk_1_The_world_around_you",
        "name": "Hoofdstuk 1: The world around you",
        "start": 37,
        "end": 84
    },
    {
        "book_id": "6a1457cf-1943-482a-bdbd-120b3e5934c3",
        "num": 2,
        "title": "Hoofdstuk_2_Crime",
        "name": "Hoofdstuk 2: Crime",
        "start": 85,
        "end": 134
    },
    {
        "book_id": "6a1457cf-1943-482a-bdbd-120b3e5934c3",
        "num": 3,
        "title": "Hoofdstuk_3_Science_and_technology",
        "name": "Hoofdstuk 3: Science & technology",
        "start": 135,
        "end": 183
    },
    {
        "book_id": "6a1457cf-1943-482a-bdbd-120b3e5934c3",
        "num": "BTG2",
        "title": "Bridging_the_Gap_year_2",
        "name": "Show What You Know & Bridging the Gap Year 2",
        "start": 10,
        "end": 36
    },
    {
        "book_id": "6a1457cf-1943-482a-bdbd-120b3e5934c3",
        "num": "REV1-3",
        "title": "Revision_and_Enrichment_1-3",
        "name": "Revision & Enrichment 1-3",
        "start": 184,
        "end": 196
    },
    # --- DEEL B (Book B) ---
    {
        "book_id": "6e5c48d6-ea83-40f5-a528-654dc6fa9d50",
        "num": 4,
        "title": "Hoofdstuk_4_To_the_extreme",
        "name": "Hoofdstuk 4: To the extreme",
        "start": 7,
        "end": 54
    },
    {
        "book_id": "6e5c48d6-ea83-40f5-a528-654dc6fa9d50",
        "num": 5,
        "title": "Hoofdstuk_5_Going_green",
        "name": "Hoofdstuk 5: Going green",
        "start": 55,
        "end": 104
    },
    {
        "book_id": "6e5c48d6-ea83-40f5-a528-654dc6fa9d50",
        "num": 6,
        "title": "Hoofdstuk_6_Your_future",
        "name": "Hoofdstuk 6: Your future",
        "start": 105,
        "end": 153
    },
    {
        "book_id": "6e5c48d6-ea83-40f5-a528-654dc6fa9d50",
        "num": "REV1-6",
        "title": "Revision_and_Enrichment_1-6",
        "name": "Revision & Enrichment 1-6",
        "start": 154,
        "end": 172
    },
    {
        "book_id": "6e5c48d6-ea83-40f5-a528-654dc6fa9d50",
        "num": "BTG4",
        "title": "Bridging_the_Gap_year_4",
        "name": "Bridging the Gap Year 4",
        "start": 173,
        "end": 182
    }
]

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

def get_current_page_num(page):
    """Extracts current page number from URL."""
    m = re.search(r'[?&]page=(\d+)', page.url)
    if m:
        return int(m.group(1))
    return None

def close_sidebar_if_open(page):
    """Closes menu sidebar to maximize page viewing area."""
    try:
        menu_btn = page.locator("[data-testid='MenuIcon'], [aria-label='Menu']")
        if menu_btn.count() > 0:
            menu_btn.first.click()
            time.sleep(1.5)
    except Exception:
        pass

def export_all():
    os.makedirs(DEST_DIR, exist_ok=True)
    temp_dir = os.path.join(DEST_DIR, "temp_engels_export")
    os.makedirs(temp_dir, exist_ok=True)
    
    print("\n" + "=" * 65)
    print("🚀 ENGELS 3 HAVO (Stepping Stones) - TÜM BÖLÜMLERİ PDF YAPMA")
    print("=" * 65 + "\n")
    
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=False,
            viewport={"width": 1920, "height": 1080},
            device_scale_factor=2,  # 2x Retina kalitesi
            args=["--start-maximized", "--no-sandbox"]
        )
        page = context.pages[0] if context.pages else context.new_page()
        page.goto(BOOKSHELF_URL)
        ensure_login(page)
        time.sleep(3)
        
        for ch in CHAPTERS:
            print("\n" + "-" * 60)
            print(f"📖 {ch['name']} (Sayfa {ch['start']} - {ch['end']}) Başlatılıyor...")
            print("-" * 60)
            
            ch_url = f"https://apps.noordhoff.nl/se/content/book/{COURSE_ID}/ebook/{ch['book_id']}?page={ch['start']}"
            page.goto(ch_url)
            time.sleep(5)
            
            close_sidebar_if_open(page)
            
            captured_images = []
            seen_urls = set()
            shot_idx = 1
            stuck_count = 0
            
            while True:
                time.sleep(2.5)
                
                curr_url = page.url
                curr_p = get_current_page_num(page) or ch['start']
                
                if curr_url in seen_urls:
                    stuck_count += 1
                    if stuck_count >= 3:
                        print(f"  ⚠️ Sayfa değişmedi ({curr_url}), bölüm sonuna ulaşıldı.")
                        break
                else:
                    stuck_count = 0
                    seen_urls.add(curr_url)
                    shot_path = os.path.join(temp_dir, f"shot_{shot_idx:03d}.png")
                    page.screenshot(path=shot_path)
                    captured_images.append(shot_path)
                    print(f"  [✓] {ch['title']} -> Görsel {shot_idx} (Sayfa {curr_p}) yakalandı.")
                    shot_idx += 1
                
                # Check if we've reached the chapter end
                if curr_p >= ch['end']:
                    print(f"  🎯 Bölüm sonu (Sayfa {curr_p} >= {ch['end']}) tamamlandı.")
                    break
                    
                # Click next page
                next_btn = page.locator("[data-testid='page-navigator-next-page'], [aria-label='Volgende pagina']")
                if next_btn.count() > 0 and next_btn.first.is_enabled():
                    next_btn.first.click()
                else:
                    page.keyboard.press("ArrowRight")
                    
                time.sleep(1.5)
                
            # PDF Compilation
            pdf_filename = f"Engels_3havo_{ch['title']}.pdf"
            pdf_path = os.path.join(DEST_DIR, pdf_filename)
            
            print(f"\n📑 {len(captured_images)} sayfa görseli PDF'e dönüştürülüyor -> {pdf_filename}...")
            pil_images = [Image.open(f).convert("RGB") for f in captured_images]
            if pil_images:
                pil_images[0].save(
                    pdf_path,
                    save_all=True,
                    append_images=pil_images[1:],
                    resolution=150.0
                )
                size_mb = os.path.getsize(pdf_path) / (1024 * 1024)
                print(f"🎉 {ch['name']} PDF'i KAYDEDİLDİ: {pdf_path} ({size_mb:.2f} MB, {len(captured_images)} ekran)")
                
            # Clean temp images for this chapter
            for f in captured_images:
                try:
                    os.remove(f)
                except Exception:
                    pass
                    
        context.close()
        
    try:
        os.rmdir(temp_dir)
    except Exception:
        pass
        
    print("\n" + "=" * 65)
    print("🏁 TÜM İNGİLİZCE BÖLÜMLERİNİN PDF DÖNÜŞTÜRME İŞLEMİ TAMAMLANDI! 🏁")
    print("=" * 65 + "\n")

if __name__ == "__main__":
    export_all()

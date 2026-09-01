#!/usr/bin/env python3
"""
Export Frans (Grandes Lignes 3 HAVO) units to high-resolution PDFs.
"""

import os
import sys
import time
import argparse
from PIL import Image
from playwright.sync_api import sync_playwright

USER_DATA_DIR = os.path.expanduser("~/.config/noordhoff_browser_profile")
BOOKSHELF_URL = "https://apps.noordhoff.nl/my/nl/bookshelf"
COURSE_ID = "fe9559e5-2325-407a-a4a8-bcc3b16708da"
EBOOK_ID = "23a8e547-a7d7-46e9-b45a-1895c6e5f429"
READER_BASE = f"https://apps.noordhoff.nl/se/content/book/{COURSE_ID}/ebook/{EBOOK_ID}"

TARGET_DIRS = [
    "/home/mesuto/Documents/PROJELER/duru_okul/inbox/2026-2027/frans",
    "/home/mesuto/Documents/PROJELER/duru_okul/havo3/frans/pdf",
    "/home/mesuto/Downloads/Eğitim/Duru/Frans"
]

UNITS = {
    0: {"name": "Unite_0_On_y_va", "title": "Grandes Lignes 3 HAVO - Unité 0 (On y va)", "start": 10, "end": 17},
    1: {"name": "Unite_1_Poste_like_partage", "title": "Grandes Lignes 3 HAVO - Unité 1 (Poste, like, partage)", "start": 18, "end": 55},
    2: {"name": "Unite_2_Du_temps_pour_moi", "title": "Grandes Lignes 3 HAVO - Unité 2 (Du temps pour moi)", "start": 56, "end": 93},
    3: {"name": "Unite_3_En_route", "title": "Grandes Lignes 3 HAVO - Unité 3 (En route!)", "start": 94, "end": 131},
    4: {"name": "Unite_4_Le_pont", "title": "Grandes Lignes 3 HAVO - Unité 4 (Le pont)", "start": 132, "end": 165},
    5: {"name": "Unite_5_Au_resto", "title": "Grandes Lignes 3 HAVO - Unité 5 (Au resto!)", "start": 166, "end": 201},
    6: {"name": "Unite_6_C_est_moi", "title": "Grandes Lignes 3 HAVO - Unité 6 (C'est moi)", "start": 202, "end": 239},
    7: {"name": "Unite_7_A_tout_prix", "title": "Grandes Lignes 3 HAVO - Unité 7 (À tout prix!)", "start": 240, "end": 273},
    8: {"name": "Unite_8_Le_pont", "title": "Grandes Lignes 3 HAVO - Unité 8 (Le pont)", "start": 274, "end": 291},
    9: {"name": "Boite_a_Gram", "title": "Grandes Lignes 3 HAVO - Boîte à Gram & Vocabulaire", "start": 292, "end": 330},
}

def ensure_login(page):
    print("🔒 Oturum ve kimlik doğrulama kontrol ediliyor...")
    for step in range(25):
        url = page.url
        if ("bookshelf" in url or "se/content" in url or "ebook" in url) and "identity" not in url and "entree" not in url:
            print("✓ Giriş başarılı!")
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

def clean_ui(page):
    """Menü ve araç çubuklarını kapatıp görünümü temizler"""
    try:
        menu_close = page.locator("[aria-label='Navigatie sluiten'], [aria-label='Menu sluiten']")
        if menu_close.count() > 0 and menu_close.first.is_visible():
            menu_close.first.click()
            time.sleep(0.5)
    except Exception:
        pass

def export_unit(page, unit_info, temp_base="/tmp/frans_pdf_temp"):
    unit_name = unit_info["name"]
    start_p = unit_info["start"]
    end_p = unit_info["end"]
    title = unit_info["title"]
    
    print(f"\n==================================================")
    print(f"📖 Başlatılıyor: {title}")
    print(f"📄 Sayfa Aralığı: {start_p} - {end_p} (Toplam {end_p - start_p + 1} sayfa)")
    print(f"==================================================")
    
    temp_dir = os.path.join(temp_base, unit_name)
    os.makedirs(temp_dir, exist_ok=True)
    
    captured_files = []
    
    for p_num in range(start_p, end_p + 1):
        target_url = f"{READER_BASE}?page={p_num}"
        print(f"  [Sayfa {p_num:3d}/{end_p}] Yükleniyor...", end="", flush=True)
        
        page.goto(target_url)
        time.sleep(2.0)
        clean_ui(page)
        time.sleep(0.5)
        
        img_path = os.path.join(temp_dir, f"page_{p_num:04d}.png")
        page.screenshot(path=img_path, full_page=False)
        captured_files.append(img_path)
        print(" ✓")
        
    print(f"\n🖼️ Sayfalar yüksek çözünürlüklü PDF belgesine dönüştürülüyor...")
    pil_images = []
    for f in captured_files:
        im = Image.open(f).convert("RGB")
        pil_images.append(im)
        
    pdf_filename = f"{unit_name}.pdf"
    
    for d in TARGET_DIRS:
        os.makedirs(d, exist_ok=True)
        out_pdf = os.path.join(d, pdf_filename)
        pil_images[0].save(
            out_pdf,
            save_all=True,
            append_images=pil_images[1:],
            resolution=150.0
        )
        size_mb = os.path.getsize(out_pdf) / (1024 * 1024)
        print(f"  💾 Kaydedildi -> {out_pdf} ({size_mb:.2f} MB)")
        
    for f in captured_files:
        try:
            os.remove(f)
        except Exception:
            pass
    try:
        os.rmdir(temp_dir)
    except Exception:
        pass
        
    print(f"✨ {unit_name} başarıyla tamamlandı!\n")

def main():
    parser = argparse.ArgumentParser(description="Fransızca ünitelerini PDF'e dönüştür.")
    parser.add_argument("--unit", type=int, default=None, help="Belirli bir ünite numarası (0-9). Boş bırakılırsa tüm üniteler.")
    args = parser.parse_args()

    for d in TARGET_DIRS:
        os.makedirs(d, exist_ok=True)

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
        if not ensure_login(page):
            print("❌ Giriş yapılamadı!")
            context.close()
            return
            
        time.sleep(3)
        
        if args.unit is not None:
            if args.unit in UNITS:
                export_unit(page, UNITS[args.unit])
            else:
                print(f"Hata: Geçersiz ünite no {args.unit}. Geçerli olanlar: {list(UNITS.keys())}")
        else:
            for u_idx in sorted(UNITS.keys()):
                export_unit(page, UNITS[u_idx])

        print("\n🎉 TÜM İŞLEMLER BAŞARIYLA TAMAMLANDI!")
        context.close()

if __name__ == "__main__":
    main()

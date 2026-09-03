#!/usr/bin/env python3
"""
Export Duits (Neue Kontakte 3 HAVO) units to high-resolution PDFs.
"""

import os
import sys
import time
import argparse
from PIL import Image
from playwright.sync_api import sync_playwright

USER_DATA_DIR = os.path.expanduser("~/.config/noordhoff_browser_profile")
BOOKSHELF_URL = "https://apps.noordhoff.nl/my/nl/bookshelf"
COURSE_ID = "b5ae3b67-6f8f-47d7-92b7-e3057c772724"
BUCH_A_ID = "8e824d31-cf14-4f42-876a-b25a84b47f33"
BUCH_B_ID = "7e751e87-5f77-454d-9866-a82dff6724e0"

TARGET_DIRS = [
    "/home/mesuto/Documents/PROJELER/duru_okul/inbox/2026-2027/duits",
    "/home/mesuto/Documents/PROJELER/duru_okul/havo3/duits/pdf",
    "/home/mesuto/Downloads/Eğitim/Duru/Duits"
]

UNITS = {
    0: {
        "name": "Bruckenschlag_1_Sich_Vorstellen",
        "title": "Neue Kontakte 3 HAVO - Brückenschlag 1 (Sich Vorstellen)",
        "book_id": BUCH_A_ID,
        "start": 8,
        "end": 15
    },
    1: {
        "name": "Kapitel_1_Umgebung",
        "title": "Neue Kontakte 3 HAVO - Kapitel 1 (Umgebung & Wetter)",
        "book_id": BUCH_A_ID,
        "start": 16,
        "end": 55
    },
    2: {
        "name": "Kapitel_2_Gesundheit",
        "title": "Neue Kontakte 3 HAVO - Kapitel 2 (Gesundheit & Körper)",
        "book_id": BUCH_A_ID,
        "start": 56,
        "end": 95
    },
    3: {
        "name": "Kapitel_3_Unterwegs",
        "title": "Neue Kontakte 3 HAVO - Kapitel 3 (Unterwegs)",
        "book_id": BUCH_A_ID,
        "start": 96,
        "end": 133
    },
    4: {
        "name": "Kapitel_4_Veranstaltungen",
        "title": "Neue Kontakte 3 HAVO - Kapitel 4 (Veranstaltungen)",
        "book_id": BUCH_B_ID,
        "start": 16,
        "end": 55
    },
    5: {
        "name": "Kapitel_5_Zukunft",
        "title": "Neue Kontakte 3 HAVO - Kapitel 5 (Zukunft & Berufe)",
        "book_id": BUCH_B_ID,
        "start": 56,
        "end": 95
    },
    6: {
        "name": "Kapitel_6_In_Aktion",
        "title": "Neue Kontakte 3 HAVO - Kapitel 6 (In Aktion)",
        "book_id": BUCH_B_ID,
        "start": 96,
        "end": 133
    },
    7: {
        "name": "Wiederholung_und_Grammatik_A",
        "title": "Neue Kontakte 3 HAVO - Wiederholung & Grammatikübersicht A",
        "book_id": BUCH_A_ID,
        "start": 134,
        "end": 160
    },
    8: {
        "name": "Wiederholung_und_Grammatik_B",
        "title": "Neue Kontakte 3 HAVO - Wiederholung & Grammatikübersicht B",
        "book_id": BUCH_B_ID,
        "start": 134,
        "end": 170
    }
}

def ensure_login(page):
    print("🔒 Oturum ve kimlik doğrulama kontrol ediliyor...")
    for _ in range(25):
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
        menu_close = page.locator("[aria-label='Navigatie sluiten'], [aria-label='Menu sluiten'], [data-testid='CloseIcon']")
        if menu_close.count() > 0 and menu_close.first.is_visible():
            menu_close.first.click()
            time.sleep(0.5)
    except Exception:
        pass

def export_unit(page, unit_info, temp_base="/tmp/duits_pdf_temp"):
    unit_name = unit_info["name"]
    start_p = unit_info["start"]
    end_p = unit_info["end"]
    title = unit_info["title"]
    book_id = unit_info["book_id"]
    reader_base = f"https://apps.noordhoff.nl/se/content/book/{COURSE_ID}/ebook/{book_id}"
    
    print(f"\n==================================================")
    print(f"📖 Başlatılıyor: {title}")
    print(f"📄 Sayfa Aralığı: {start_p} - {end_p} (Toplam {end_p - start_p + 1} sayfa)")
    print(f"==================================================")
    
    temp_dir = os.path.join(temp_base, unit_name)
    os.makedirs(temp_dir, exist_ok=True)
    
    captured_files = []
    
    for p_num in range(start_p, end_p + 1):
        target_url = f"{reader_base}?page={p_num}"
        print(f"  [Sayfa {p_num:3d}/{end_p}] Yükleniyor...", end="", flush=True)
        
        page.goto(target_url)
        time.sleep(3.0)
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
    parser = argparse.ArgumentParser(description="Duits (Neue Kontakte) ünitelerini PDF'e dönüştür.")
    parser.add_argument("--unit", type=int, default=None, help="Belirli bir ünite numarası (0-8). Boş bırakılırsa tüm üniteler.")
    args = parser.parse_args()

    for d in TARGET_DIRS:
        os.makedirs(d, exist_ok=True)

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=True,
            viewport={"width": 1920, "height": 1080},
            device_scale_factor=2,
            args=["--no-sandbox"]
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

        print("\n🎉 TÜM ALMANCA ÜNİTELERİ BAŞARIYLA PDF YAPILDI!")
        context.close()

if __name__ == "__main__":
    main()

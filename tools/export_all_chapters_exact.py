import os
import sys
import time
from PIL import Image
from playwright.sync_api import sync_playwright

USER_DATA_DIR = os.path.expanduser("~/.config/noordhoff_browser_profile")
BOOKSHELF_URL = "https://apps.noordhoff.nl/my/nl/bookshelf"
DEST_DIR = "/home/mesuto/Downloads/Eğitim/Duru"

CHAPTERS = [
    {
        "num": 1,
        "title": "Hoofdstuk_1_Wereldhandel_in_beweging",
        "name": "Hoofdstuk 1: Wereldhandel in beweging",
        "start": 10,
        "end": 55
    },
    {
        "num": 2,
        "title": "Hoofdstuk_2_Schatkist_aarde",
        "name": "Hoofdstuk 2: Schatkist aarde?",
        "start": 56,
        "end": 101
    },
    {
        "num": 3,
        "title": "Hoofdstuk_3_Migratie",
        "name": "Hoofdstuk 3: Migratie",
        "start": 102,
        "end": 147
    },
    {
        "num": 4,
        "title": "Hoofdstuk_4_Energietransitie",
        "name": "Hoofdstuk 4: Energietransitie",
        "start": 148,
        "end": 193
    },
    {
        "num": 5,
        "title": "Hoofdstuk_5_Gewapende_conflicten",
        "name": "Hoofdstuk 5: Gewapende conflicten",
        "start": 194,
        "end": 240
    }
]

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

def export_all():
    os.makedirs(DEST_DIR, exist_ok=True)
    temp_dir = os.path.join(DEST_DIR, "temp_chapter_export")
    os.makedirs(temp_dir, exist_ok=True)
    
    print("\n=======================================================")
    print("🚀 Aardrijkskunde 3 HAVO - TÜM BÖLÜMLERİ PDF YAPMA İŞLEMİ")
    print("=======================================================\n")
    
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
        
        # 1. Aardrijkskunde kitabını aç
        page.wait_for_selector("[data-testid='new-product-card']", timeout=20000)
        cards = page.locator("[data-testid='new-product-card']").all()
        ak_card = cards[0]
        ak_card.click()
        time.sleep(4)
        
        # 2. E-books / Alle e-books tıkla
        ebook_btn = page.locator("a:has-text('E-book'), button:has-text('E-book'), [data-testid*='ebook']")
        if ebook_btn.count() > 0:
            ebook_btn.first.click()
            time.sleep(4)
            
        # 3. Leerwerkboek butonuna tıkla
        lwb = page.locator("text='Leerwerkboek'")
        lwb.first.click()
        time.sleep(7)
        
        print("🎯 E-Kitap Okuyucu (Leerwerkboek) başarıyla açıldı!")
        
        # Menüyü kapat (sayfalar tam ekran olsun)
        try:
            menu_btn = page.locator("[data-testid='MenuIcon'], [aria-label='Menu']")
            if menu_btn.count() > 0:
                menu_btn.first.click()
                time.sleep(1.5)
        except Exception:
            pass
            
        reader_base_url = page.url.split("?")[0]
        
        # Tüm bölümleri sırayla tara
        for ch in CHAPTERS:
            print(f"\n=======================================================")
            print(f"📖 {ch['name']} (Sayfa {ch['start']} - {ch['end']}) Başlatılıyor...")
            print(f"=======================================================")
            
            # Doğrudan ilgili bölümün başlangıç sayfasına git
            ch_start_url = f"{reader_base_url}?page={ch['start']}"
            page.goto(ch_start_url)
            time.sleep(4)
            
            captured_images = []
            next_btn = page.locator("[data-testid='page-navigator-next-page'], [aria-label='Volgende pagina']")
            
            total_pages = ch['end'] - ch['start'] + 1
            for p_offset in range(total_pages):
                current_p = ch['start'] + p_offset
                time.sleep(2.0)
                
                shot_path = os.path.join(temp_dir, f"p_{current_p:03d}.png")
                page.screenshot(path=shot_path)
                captured_images.append(shot_path)
                print(f"  [✓] {ch['title']} -> Kitap Sayfası {current_p} ({p_offset+1}/{total_pages}) yakalandı.")
                
                # Sonraki sayfaya geç (son sayfa değilse)
                if p_offset < total_pages - 1:
                    if next_btn.count() > 0:
                        next_btn.first.click()
                    else:
                        page.keyboard.press("ArrowRight")
                        
            # Bu bölümü PDF'e dönüştür
            pdf_filename = f"Aardrijkskunde_3havo_{ch['title']}.pdf"
            pdf_path = os.path.join(DEST_DIR, pdf_filename)
            
            print(f"\n📑 {len(captured_images)} sayfa PDF'e dönüştürülüyor -> {pdf_filename}...")
            pil_images = [Image.open(f).convert("RGB") for f in captured_images]
            if pil_images:
                pil_images[0].save(
                    pdf_path,
                    save_all=True,
                    append_images=pil_images[1:],
                    resolution=150.0
                )
                size_mb = os.path.getsize(pdf_path) / (1024 * 1024)
                print(f"🎉 {ch['name']} PDF'i KAYDEDİLDİ: {pdf_path} ({size_mb:.2f} MB)")
                
            # Geçici görselleri temizle
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
        
    print("\n🏁 TÜM BÖLÜMLERİN PDF DÖNÜŞTÜRME İŞLEMİ BAŞARIYLA BİTTİ! 🏁\n")

if __name__ == "__main__":
    export_all()

import os
import sys
import time
from PIL import Image
from playwright.sync_api import sync_playwright

USER_DATA_DIR = os.path.expanduser("~/.config/noordhoff_browser_profile")
BOOKSHELF_URL = "https://apps.noordhoff.nl/my/nl/bookshelf"
DEST_DIR = "/home/mesuto/Downloads/Eğitim/Duru"
TEMP_DIR = os.path.join(DEST_DIR, "temp_leerwerkboek_h1")

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

def main():
    os.makedirs(DEST_DIR, exist_ok=True)
    os.makedirs(TEMP_DIR, exist_ok=True)
    
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
        print(f"📖 Kitap açılıyor: {ak_card.inner_text().splitlines()[0]}...")
        ak_card.click()
        time.sleep(4)
        
        # 2. E-books / Alle e-books tıkla
        ebook_btn = page.locator("a:has-text('E-book'), button:has-text('E-book'), [data-testid*='ebook']")
        if ebook_btn.count() > 0:
            print("👉 'E-books' sekmesine giriliyor...")
            ebook_btn.first.click()
            time.sleep(4)
            
        # 3. Leerwerkboek butonuna tıkla
        lwb = page.locator("text='Leerwerkboek'")
        print("👉 'Leerwerkboek' açılıyor...")
        lwb.first.click()
        time.sleep(7)
        
        print("🎯 E-Kitap Okuyucu (Leerwerkboek) başarıyla açıldı!")
        print("URL:", page.url)
        
        # 4. Sol menüden 1. Bölüm (1 Wereldhandel in beweging) tıkla
        h1_item = page.locator("text='1 Wereldhandel in beweging'")
        if h1_item.count() > 0:
            print("👉 1. Bölüm (Hoofdstuk 1) başlangıcına gidiliyor...")
            h1_item.first.click()
            time.sleep(4)
            
        # Sol menüyü kapatmak/küçültmek için gerekiyorsa Menü ikonuna veya sayfa alanına tıkla
        try:
            menu_btn = page.locator("[data-testid='MenuIcon'], [aria-label='Menu']")
            if menu_btn.count() > 0:
                menu_btn.first.click()
                time.sleep(2)
        except Exception:
            pass
            
        # 5. Hoofdstuk 1 sayfalarını sırayla tara (Hoofdstuk 2 gelene kadar veya ~40 sayfa)
        captured_images = []
        next_btn = page.locator("[data-testid='page-navigator-next-page'], [aria-label='Volgende pagina']")
        
        # Hoofdstuk 1 genellikle yaklaşık 30-40 sayfadır
        MAX_CHAPTER_PAGES = 45
        print(f"\n📸 Hoofdstuk 1 sayfaları tek tek taranıyor...")
        
        for p_no in range(1, MAX_CHAPTER_PAGES + 1):
            time.sleep(2.5)
            
            # Sayfa görüntüsü al
            img_path = os.path.join(TEMP_DIR, f"lwb_h1_page_{p_no:03d}.png")
            page.screenshot(path=img_path)
            captured_images.append(img_path)
            print(f"  [✓] Sayfa {p_no:2d} yakalandı.")
            
            # Sonraki sayfaya geç
            if next_btn.count() > 0:
                next_btn.first.click()
            else:
                page.keyboard.press("ArrowRight")
                
        context.close()
        
    # PDF Dönüştürme
    pdf_path = os.path.join(DEST_DIR, "Aardrijkskunde_3havo_Leerwerkboek_Hoofdstuk_1.pdf")
    print(f"\n📑 Toplam {len(captured_images)} sayfa PDF'e dönüştürülüyor -> {pdf_path}...")
    
    pil_images = [Image.open(f).convert("RGB") for f in captured_images]
    if pil_images:
        pil_images[0].save(
            pdf_path,
            save_all=True,
            append_images=pil_images[1:],
            resolution=150.0
        )
        size_mb = os.path.getsize(pdf_path) / (1024 * 1024)
        print(f"\n🎉 BAŞARIYLA TAMAMLANDI!")
        print(f"📍 Dosya: {pdf_path}")
        print(f"📦 Boyut: {size_mb:.2f} MB ({len(captured_images)} Sayfa)")
        
    # Geçici dosyaları temizle
    for f in captured_images:
        try:
            os.remove(f)
        except Exception:
            pass
    try:
        os.rmdir(TEMP_DIR)
    except Exception:
        pass

if __name__ == "__main__":
    main()

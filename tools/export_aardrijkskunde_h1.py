import os
import sys
import time
from PIL import Image
from playwright.sync_api import sync_playwright

USER_DATA_DIR = os.path.expanduser("~/.config/noordhoff_browser_profile")
BOOKSHELF_URL = "https://apps.noordhoff.nl/my/nl/bookshelf"
DEST_DIR = "/home/mesuto/Downloads/Eğitim/Duru"
TEMP_DIR = os.path.join(DEST_DIR, "temp_h1_pages")

def ensure_login(page):
    print("Oturum kontrol ediliyor...")
    for step in range(20):
        url = page.url
        if "bookshelf" in url and "identity" not in url and "entree" not in url:
            return True
        elif "se/content" in url:
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

def main():
    os.makedirs(DEST_DIR, exist_ok=True)
    os.makedirs(TEMP_DIR, exist_ok=True)
    
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=False,
            viewport={"width": 1920, "height": 1080},
            device_scale_factor=2,  # Yüksek çözünürlüklü görüntü
            args=["--start-maximized", "--no-sandbox"]
        )
        page = context.pages[0] if context.pages else context.new_page()
        page.goto(BOOKSHELF_URL)
        ensure_login(page)
        
        # Kitapların yüklenmesini bekle
        print("Kitaplık yükleniyor...")
        page.wait_for_selector("[data-testid='new-product-card']", timeout=20000)
        time.sleep(2)
        
        # Aardrijkskunde (Index 0 veya buiteNLand kartı)
        cards = page.locator("[data-testid='new-product-card']").all()
        ak_card = None
        for c in cards:
            if "Aardrijkskunde" in c.inner_text() or "buiteNLand" in c.inner_text():
                ak_card = c
                break
        if not ak_card:
            ak_card = cards[0]
            
        print(f"Kitap seçildi: {ak_card.inner_text().replace(chr(10), ' | ')}")
        ak_card.click()
        time.sleep(5)
        
        print("Kitap sayfası URL:", page.url)
        print("Kitap sayfası Başlık:", page.title())
        
        # Sayfadaki tüm başlıkları ve bölümleri kontrol et
        time.sleep(3)
        page.screenshot(path=os.path.join(DEST_DIR, "ak_overview.png"))
        
        # Hoofdstuk 1 veya Thema 1 veya Leerwerkboek tespit et
        # Aardrijkskunde buiteNLand genellikle "Hoofdstuk 1" veya "Thema 1" şeklinde içerik listesine sahiptir
        h1_loc = page.locator("text='Hoofdstuk 1', text='Thema 1', text='1 ', [data-testid*='chapter-1'], [data-testid*='theme-1']")
        print(f"Hoofdstuk/Thema 1 arama sonucu element sayısı: {h1_loc.count()}")
        
        # Leerwerkboek / E-book butonunu aç
        ebook_btn = page.locator("text='Leerwerkboek', text='E-book', [data-testid='all_ebooks']")
        if ebook_btn.count() > 0:
            print(f"E-kitap / Leerwerkboek açılıyor: {ebook_btn.first.inner_text()}...")
            ebook_btn.first.click()
            time.sleep(6)
            
        print("Okuyucu URL:", page.url)
        
        # Sayfaları tara ve ekran görüntülerini topla
        # Hoofdstuk 1 genellikle ilk 25-40 sayfa arasındadır.
        # Sayfa geçişlerinde ekran görüntüsü alalım
        captured_images = []
        MAX_PAGES = 35  # Hoofdstuk 1 için yeterli sayfa sayısı
        
        print(f"\n📸 Hoofdstuk 1 sayfaları taranıyor (Maksimum {MAX_PAGES} sayfa)...")
        for p_idx in range(1, MAX_PAGES + 1):
            time.sleep(2.5)
            img_file = os.path.join(TEMP_DIR, f"h1_page_{p_idx:03d}.png")
            page.screenshot(path=img_file)
            captured_images.append(img_file)
            print(f"  [✓] Sayfa {p_idx:2d} kaydedildi.")
            
            # Sonraki sayfaya geç
            page.keyboard.press("ArrowRight")
            
        context.close()
        
    # PDF Oluşturma
    pdf_out = os.path.join(DEST_DIR, "Aardrijkskunde_3havo_Hoofdstuk_1.pdf")
    print(f"\n📑 {len(captured_images)} sayfa PDF'e dönüştürülüyor -> {pdf_out}...")
    
    pil_images = [Image.open(f).convert("RGB") for f in captured_images]
    if pil_images:
        pil_images[0].save(
            pdf_out,
            save_all=True,
            append_images=pil_images[1:],
            resolution=150.0
        )
        size_mb = os.path.getsize(pdf_out) / (1024 * 1024)
        print(f"\n🎉 BAŞARILI! PDF dosyası kaydedildi:")
        print(f"📍 Dosya: {pdf_out}")
        print(f"📦 Boyut: {size_mb:.2f} MB")
        
    # Geçici ekran görüntülerini temizle
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

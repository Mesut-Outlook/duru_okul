import os
import sys
import time
from PIL import Image
from playwright.sync_api import sync_playwright

USER_DATA_DIR = os.path.expanduser("~/.config/noordhoff_browser_profile")
BOOKSHELF_URL = "https://apps.noordhoff.nl/my/nl/bookshelf"
DEST_DIR = "/home/mesuto/Downloads/Eğitim/Duru"
TEMP_DIR = os.path.join(DEST_DIR, "temp_h1_full")

def ensure_login(page):
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
            device_scale_factor=2, # Yüksek DPI / Netlik
            args=["--start-maximized", "--no-sandbox"]
        )
        page = context.pages[0] if context.pages else context.new_page()
        page.goto(BOOKSHELF_URL)
        ensure_login(page)
        
        # Kitaplığın yüklenmesini bekle
        page.wait_for_selector("[data-testid='new-product-card']", timeout=20000)
        time.sleep(2)
        
        # Aardrijkskunde seç
        cards = page.locator("[data-testid='new-product-card']").all()
        ak_card = None
        for c in cards:
            if "Aardrijkskunde" in c.inner_text() or "buiteNLand" in c.inner_text():
                ak_card = c
                break
        if not ak_card:
            ak_card = cards[0]
            
        print(f"Kitap açılıyor: {ak_card.inner_text().replace(chr(10), ' | ')}")
        ak_card.click()
        time.sleep(5)
        
        # 1. Bölüm (1 Wereldhandel in beweging) tıkla
        print("\n--- 1. Bölüm (1 Wereldhandel in beweging) seçiliyor ---")
        ch1_link = page.locator("text='1 Wereldhandel in beweging'")
        if ch1_link.count() > 0:
            ch1_link.first.click()
            time.sleep(5)
            
        print("Bölüm 1 URL:", page.url)
        print("Bölüm 1 Başlık:", page.title())
        
        # Bölüm 1 içindeki alt başlıkları topla
        sub_topics = [
            "Introductie",
            "Vaardigheden",
            "1.1 Kantelt het economisch wereldbeeld?",
            "1.2 Wereldhandel: van kolonialisme tot nu",
            "1.3 Verschillen tussen rollen in de wereldhandel",
            "Landenvergelijking",
            "1.4 Rol van Europa in de wereldhandel",
            "1.5 Rol van Nederland in de wereldhandel",
            "Keuzeopdrachten",
            "In vogelvlucht",
            "Samenvatting"
        ]
        
        captured_images = []
        shot_counter = 1
        
        for topic in sub_topics:
            print(f"\n👉 [{topic}] açılıyor...")
            
            # Sol menüden veya genel sayfadan alt başlığa tıkla
            topic_btn = page.locator(f"text='{topic}'")
            if topic_btn.count() > 0:
                try:
                    topic_btn.first.click()
                    time.sleep(4)
                except Exception as e:
                    print(f"Tıklama hatası ({topic}):", e)
            else:
                print(f"Element bulunamadı: {topic}")
                continue
                
            # Alt sayfanın tam ekran görüntüsünü al
            # Eğer sayfa aşağıya kaydırılıyorsa (uzun teori/soru sayfası), hem üst hem alt kısımlarını yakala
            time.sleep(2)
            
            # 1. Üst kısım
            page.evaluate("window.scrollTo(0, 0)")
            time.sleep(1)
            img1 = os.path.join(TEMP_DIR, f"page_{shot_counter:03d}_{topic[:10].strip()}.png")
            page.screenshot(path=img1)
            captured_images.append(img1)
            print(f"  [✓] Ekran görüntüsü alındı: Sayfa {shot_counter} ({topic} - Üst)")
            shot_counter += 1
            
            # Scroll yüksekliğini kontrol et
            scroll_height = page.evaluate("document.body.scrollHeight")
            client_height = page.evaluate("window.innerHeight")
            
            if scroll_height > client_height * 1.3:
                # 2. Orta / Alt kısım
                page.evaluate("window.scrollBy(0, window.innerHeight * 0.8)")
                time.sleep(1)
                img2 = os.path.join(TEMP_DIR, f"page_{shot_counter:03d}_{topic[:10].strip()}_b.png")
                page.screenshot(path=img2)
                captured_images.append(img2)
                print(f"  [✓] Ekran görüntüsü alındı: Sayfa {shot_counter} ({topic} - Alt)")
                shot_counter += 1
                
                # Eğer daha da uzunsa en alta kaydır
                if scroll_height > client_height * 2.2:
                    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                    time.sleep(1)
                    img3 = os.path.join(TEMP_DIR, f"page_{shot_counter:03d}_{topic[:10].strip()}_c.png")
                    page.screenshot(path=img3)
                    captured_images.append(img3)
                    print(f"  [✓] Ekran görüntüsü alındı: Sayfa {shot_counter} ({topic} - En Alt)")
                    shot_counter += 1

        context.close()
        
    # PDF Dönüştürme
    pdf_out = os.path.join(DEST_DIR, "Aardrijkskunde_3havo_Hoofdstuk_1_Tam.pdf")
    print(f"\n📑 Toplam {len(captured_images)} sayfa görseli PDF'e dönüştürülüyor -> {pdf_out}...")
    
    pil_images = [Image.open(f).convert("RGB") for f in captured_images]
    if pil_images:
        pil_images[0].save(
            pdf_out,
            save_all=True,
            append_images=pil_images[1:],
            resolution=150.0
        )
        size_mb = os.path.getsize(pdf_out) / (1024 * 1024)
        print(f"\n🎉 TAMAMLANDI! PDF dosyası kaydedildi:")
        print(f"📍 Dosya: {pdf_out}")
        print(f"📦 Boyut: {size_mb:.2f} MB")
        print(f"📄 Toplam Sayfa: {len(captured_images)}")
        
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

#!/usr/bin/env python3
"""
Noordhoff Frans (Grandes Lignes 3 HAVO) E-book Unit 1 PDF Exporter.
Safely handles Microsoft / Somtoday SSO login and captures verified non-blank pages.
"""

import os
import sys
import time
import argparse
from PIL import Image, ImageStat
from playwright.sync_api import sync_playwright

USER_DATA_DIR = os.path.expanduser("~/.config/noordhoff_browser_profile")
BOOKSHELF_URL = "https://apps.noordhoff.nl/my/nl/bookshelf"
COURSE_ID = "fe9559e5-2325-407a-a4a8-bcc3b16708da"
EBOOK_ID = "23a8e547-a7d7-46e9-b45a-1895c6e5f429"
READER_URL = f"https://apps.noordhoff.nl/se/content/book/{COURSE_ID}/ebook/{EBOOK_ID}"

TARGET_DIRS = [
    "/home/mesuto/Documents/PROJELER/duru_okul/inbox/2026-2027/frans",
    "/home/mesuto/Documents/PROJELER/duru_okul/havo3/frans/pdf",
    "/home/mesuto/Downloads/Eğitim/Duru/Frans"
]

def is_blank_image(image_path):
    """Checks if the captured screenshot is blank/white."""
    try:
        im = Image.open(image_path).convert("L")
        stat = ImageStat.Stat(im)
        # If standard deviation of grayscale pixels is < 3.0, it's almost solid white/empty
        if stat.stddev[0] < 3.0 or stat.mean[0] > 252.0:
            return True
        return False
    except Exception:
        return False

def ensure_login(page, max_wait_user_seconds=120):
    print("\n🔑 Noordhoff oturum ve kimlik doğrulama kontrol ediliyor...")
    start_time = time.time()
    
    while time.time() - start_time < max_wait_user_seconds:
        url = page.url
        print(f"  [Durum] URL: {url[:80]}...")
        
        # Already authenticated
        if ("bookshelf" in url or "se/content" in url or "ebook" in url) and "identity" not in url and "entree" not in url and "somtoday" not in url and "microsoft" not in url:
            print("  ✓ Başarıyla oturum açıldı!")
            return True
            
        # 1. Identity page -> Click 'via Entree'
        if "identity" in url:
            try:
                entree_btn = page.locator("text='via Entree'")
                if entree_btn.count() > 0 and entree_btn.first.is_visible():
                    print("  👉 'via Entree' butonuna tıklanıyor...")
                    entree_btn.first.click(timeout=3000)
            except Exception:
                pass
                
        # 2. Entree page -> Click previous selection
        elif "entree" in url:
            try:
                sel = page.locator('.wayf__previousSelection, .previousSelection__item, .idp__submit')
                if sel.count() > 0 and sel.first.is_visible():
                    print("  👉 Entree önceki seçimi onaylanıyor...")
                    sel.first.click(force=True, timeout=3000)
            except Exception:
                pass
                
        # 3. Somtoday page -> Click 'Caland Lyceum Azure'
        elif "somtoday" in url:
            try:
                azure_btn = page.locator("text='Caland Lyceum Azure'")
                if azure_btn.count() > 0 and azure_btn.first.is_visible():
                    print("  👉 'Caland Lyceum Azure' butonuna tıklanıyor...")
                    azure_btn.first.click(timeout=3000)
            except Exception:
                pass
                
        # 4. Microsoft Online login page -> User needs to enter password
        elif "microsoftonline" in url:
            print("  ⚠️  Microsoft Azure giriş ekranı açık! Lütfen ekrandaki tarayıcıda şifrenizi giriniz...")
            
        time.sleep(3)
        
    print("❌ Oturum açma süresi doldu!")
    return False

def close_sidebar(page):
    """Closes sidebar to maximize book reading area"""
    try:
        # Check if Menu button is visible
        menu_btn = page.locator("[data-testid='MenuIcon'], button[aria-label='Menu']")
        if menu_btn.count() > 0 and menu_btn.first.is_visible():
            print("  👉 Menü/Kenar çubuğu simgesine tıklanarak yan panel gizleniyor...")
            menu_btn.first.click()
            time.sleep(1.5)
    except Exception as e:
        print(f"  Kenar çubuğu kapatma uyarısı: {e}")

def export_frans_unit1(headless=True):
    for d in TARGET_DIRS:
        os.makedirs(d, exist_ok=True)
        
    temp_dir = "/tmp/frans_unit1_pages"
    os.makedirs(temp_dir, exist_ok=True)
    
    print("\n🚀 Frans (Grandes Lignes 3 HAVO) E-Kitap Okuyucu Başlatılıyor...")
    
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=headless,
            viewport={"width": 1920, "height": 1080},
            device_scale_factor=2, # 2x Retina netliği
            args=["--start-maximized", "--no-sandbox"]
        )
        page = context.pages[0] if context.pages else context.new_page()
        
        # Navigate to bookshelf first to ensure session
        page.goto(BOOKSHELF_URL)
        if not ensure_login(page):
            print("❌ Oturum açılamadı, işlem iptal edildi.")
            context.close()
            return None
            
        time.sleep(3)
        
        # Direct navigation to E-book reader starting at Unit 1 (page 16)
        start_page = 16
        end_page = 55
        target_reader_url = f"{READER_URL}?page={start_page}"
        print(f"\n📖 E-Kitap Okuyucu açılıyor: {target_reader_url}")
        page.goto(target_reader_url)
        time.sleep(3)
        
        # If redirected to identity/login, handle it again
        if "identity" in page.url or "entree" in page.url or "somtoday" in page.url:
            ensure_login(page)
            # navigate back to reader url if needed
            if "ebook" not in page.url:
                page.goto(target_reader_url)
        
        # Wait for initial reader render
        print("⏳ Okuyucu arayüzü ve içerik yükleniyor...")
        try:
            page.wait_for_selector("[data-testid='page-navigator-next-page']", timeout=40000)
            print("  ✓ Okuyucu arayüzü yüklendi!")
        except Exception:
            print("  ⚠️ page-navigator-next-page beklenirken zaman aşımı, devam ediliyor...")
                
        time.sleep(4)
        close_sidebar(page)
        time.sleep(2)
        
        captured_images = []
        shot_idx = 1
        current_spread_max = start_page
        
        print(f"\n📸 Sayfalar taranıyor ({start_page} ile {end_page} arası)...")
        
        import re
        while True:
            # Check current page indicator
            page_text = ""
            try:
                inp = page.locator("input[aria-label*='pagina'], input[type='number']")
                if inp.count() > 0:
                    page_text = inp.first.input_value()
            except Exception:
                pass
                
            nums = [int(n) for n in re.findall(r'\d+', page_text)]
            if nums:
                current_spread_max = max(nums)
                display_label = page_text.strip()
            else:
                display_label = f"Spread {shot_idx}"
                
            print(f"\n[{shot_idx}. Çekim | Gösterge: {display_label}] Sayfa yakalanıyor...")
            
            img_path = os.path.join(temp_dir, f"frans_u1_spread_{shot_idx:02d}.png")
            
            # Retry up to 5 times if blank
            for attempt in range(5):
                page.screenshot(path=img_path, full_page=False)
                if not is_blank_image(img_path):
                    break
                print(f"  ⏳ Sayfa içeriği bekleniyor (deneme {attempt+1})...")
                time.sleep(2)
                
            if is_blank_image(img_path):
                print(f"  ⚠️  Uyarı: Görsel boş görünüyor ({img_path}), yine de listeye alındı.")
            else:
                im = Image.open(img_path)
                stat = ImageStat.Stat(im.convert("L"))
                print(f"  [✓] Başarıyla yakalandı: {os.path.basename(img_path)} (Boyut: {im.size}, stddev: {stat.stddev[0]:.1f})")
                
            captured_images.append(img_path)
            shot_idx += 1
            
            # Check if we reached or exceeded end_page
            if nums and max(nums) >= end_page:
                print(f"🏁 Hedef sayfa {end_page}'ye ulaşıldı (Mevcut: {max(nums)}). Tarama tamamlandı.")
                break
                
            # If no nums detected but we exceeded reasonable spreads (e.g. 25 spreads for 40 pages)
            if shot_idx > 25:
                print("🏁 Maksimum spread sınırına ulaşıldı. Tarama tamamlandı.")
                break
                
            # Advance to next spread
            next_btn = page.locator("[data-testid='page-navigator-next-page'], [aria-label='Volgende pagina']")
            if next_btn.count() > 0 and next_btn.first.is_enabled():
                next_btn.first.click()
            else:
                page.keyboard.press("ArrowRight")
                
            # Allow time for next spread to render
            time.sleep(2.5)
            
        context.close()
        
    if not captured_images:
        print("❌ Hiç sayfa kaydedilemedi!")
        return None
        
    print(f"\n📑 Toplam {len(captured_images)} sayfa yüksek çözünürlüklü PDF belgesine dönüştürülüyor...")
    pil_images = [Image.open(f).convert("RGB") for f in captured_images]
    
    pdf_filename = "Grandes_Lignes_3havo_Unite_1.pdf"
    results = []
    
    for d in TARGET_DIRS:
        out_pdf = os.path.join(d, pdf_filename)
        pil_images[0].save(
            out_pdf,
            save_all=True,
            append_images=pil_images[1:],
            resolution=150.0
        )
        size_mb = os.path.getsize(out_pdf) / (1024 * 1024)
        print(f"  💾 Kaydedildi -> {out_pdf} ({size_mb:.2f} MB, {len(captured_images)} sayfa)")
        results.append(out_pdf)
        
    # Also overwrite the old Unite_1_Poste_like_partage.pdf so everything is updated
    for d in TARGET_DIRS:
        alt_pdf = os.path.join(d, "Unite_1_Poste_like_partage.pdf")
        pil_images[0].save(
            alt_pdf,
            save_all=True,
            append_images=pil_images[1:],
            resolution=150.0
        )
        print(f"  💾 Güncellendi -> {alt_pdf}")
        
    # Cleanup temp
    for f in captured_images:
        try:
            os.remove(f)
        except Exception:
            pass
    try:
        os.rmdir(temp_dir)
    except Exception:
        pass
        
    print("\n🎉 İŞLEM BAŞARIYLA TAMAMLANDI!")
    return results[0] if results else None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Grandes Lignes 3 HAVO E-Kitap Unité 1 PDF Exporter")
    parser.add_argument("--headless", action="store_true", help="Arka planda (headless) çalıştır")
    args = parser.parse_args()
    
    export_frans_unit1(headless=args.headless)

#!/usr/bin/env python3
import os
import sys
import time
import argparse
from PIL import Image
from playwright.sync_api import sync_playwright

USER_DATA_DIR = os.path.expanduser("~/.config/noordhoff_browser_profile")
BOOKSHELF_URL = "https://apps.noordhoff.nl/my/nl/bookshelf"
DEFAULT_DEST = "/home/mesuto/Downloads/Eğitim/Duru"

def ensure_login(page):
    """Handles automatic Entree & Somtoday SSO login flows."""
    for _ in range(20):
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

def get_books(page):
    page.goto(BOOKSHELF_URL)
    ensure_login(page)
    page.wait_for_selector("[data-testid='new-product-card']", timeout=20000)
    time.sleep(2)
    cards = page.locator("[data-testid='new-product-card']").all()
    books = []
    for idx, card in enumerate(cards):
        txt = card.inner_text().strip().split("\n")
        subject = txt[0] if len(txt) > 0 else "Onbekend"
        title = " - ".join([t for t in txt[1:] if t.strip()])
        books.append({
            "index": idx,
            "subject": subject,
            "title": title,
            "raw": " | ".join(txt)
        })
    return books

def list_books():
    print("\n🔍 Noordhoff Kitaplığı Taranıyor...\n")
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=True,
            args=["--no-sandbox"]
        )
        page = context.pages[0] if context.pages else context.new_page()
        books = get_books(page)
        context.close()
        
    print(f"📚 Toplam {len(books)} Kitap Bulundu:")
    print("=" * 65)
    for b in books:
        print(f"[{b['index']:2d}] {b['subject']:<16} | {b['title']}")
    print("=" * 65)
    return books

def export_chapter(book_idx, chapter_num, output_dir=DEFAULT_DEST):
    os.makedirs(output_dir, exist_ok=True)
    temp_dir = os.path.join(output_dir, f"temp_book_{book_idx}_ch_{chapter_num}")
    os.makedirs(temp_dir, exist_ok=True)
    
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=False,
            viewport={"width": 1920, "height": 1080},
            device_scale_factor=2,
            args=["--start-maximized", "--no-sandbox"]
        )
        page = context.pages[0] if context.pages else context.new_page()
        books = get_books(page)
        
        if book_idx >= len(books):
            print(f"Hata: Kitap indexi {book_idx} bulunamadı.")
            context.close()
            return
            
        target_book = books[book_idx]
        print(f"\n📖 Seçilen Kitap: {target_book['subject']} ({target_book['title']})")
        
        cards = page.locator("[data-testid='new-product-card']").all()
        cards[book_idx].click()
        time.sleep(5)
        
        # Find chapter in left menu / navigation (e.g. "1 ", "1 Wereldhandel...", "Hoofdstuk 1")
        ch_selector = f"text=/^{chapter_num}\\s+|Hoofdstuk {chapter_num}|Thema {chapter_num}/"
        ch_link = page.locator(ch_selector)
        
        if ch_link.count() == 0:
            # Fallback search
            ch_link = page.locator(f"a:has-text('{chapter_num} '), nav a:has-text('{chapter_num}')")
            
        if ch_link.count() > 0:
            ch_title = ch_link.first.inner_text().strip().replace("\n", " ")
            print(f"👉 Bölüm Seçildi: {ch_title}")
            ch_link.first.click()
            time.sleep(5)
        else:
            ch_title = f"Hoofdstuk_{chapter_num}"
            print(f"Uyarı: '{chapter_num}' başlıklı menü öğesi doğrudan bulunamadı, mevcut sayfadan devam ediliyor.")
            
        # Discover all sub-topics in this chapter
        sub_items = page.locator("nav a, [data-testid='chapterOverview'] a, [data-testid='chapterOverview'] div, .MuiListItem-root a").all()
        sub_topics = []
        for el in sub_items:
            t = el.inner_text().strip().replace("\n", " ")
            if t and len(t) > 2 and t not in sub_topics:
                # Filter out system buttons
                if not any(x in t.lower() for x in ['cookie', 'privacy', 'voorwaarden', 'klantenservice', 'hulp', 'welkom', 'naar boekenplank', 'home', 'resultaten', 'mediabibliotheek']):
                    # Ensure it belongs to this chapter or is a lesson topic
                    if any(c in t for c in [f"{chapter_num}.", f"{chapter_num} ", "Introductie", "Vaardigheden", "Samenvatting", "In vogelvlucht", "Landenvergelijking", "Keuzeopdrachten"]):
                        sub_topics.append(t)
                        
        if not sub_topics:
            sub_topics = [
                "Introductie",
                "Vaardigheden",
                f"{chapter_num}.1",
                f"{chapter_num}.2",
                f"{chapter_num}.3",
                "Landenvergelijking",
                f"{chapter_num}.4",
                f"{chapter_num}.5",
                "Keuzeopdrachten",
                "In vogelvlucht",
                "Samenvatting"
            ]
            
        print(f"\n📂 Bölüm İçindeki Alt Başlıklar ({len(sub_topics)} Adet):")
        for s in sub_topics:
            print(f"  • {s}")
            
        captured_images = []
        shot_count = 1
        
        print("\n📸 Her bir alt başlığa tıklanıp sayfalar taranıyor...")
        for topic in sub_topics:
            topic_clean = topic.strip()
            topic_btn = page.locator(f"text='{topic_clean}'")
            if topic_btn.count() > 0:
                try:
                    print(f"\n👉 Tıklanıyor: {topic_clean}")
                    topic_btn.first.click()
                    time.sleep(4)
                except Exception as ex:
                    print(f"Tıklama uyarısı ({topic_clean}):", ex)
            else:
                continue
                
            time.sleep(2)
            page.evaluate("window.scrollTo(0, 0)")
            time.sleep(1)
            
            # Screenshot 1 (Top)
            img1 = os.path.join(temp_dir, f"shot_{shot_count:03d}.png")
            page.screenshot(path=img1)
            captured_images.append(img1)
            print(f"  [✓] Sayfa {shot_count} kaydedildi ({topic_clean[:25]})")
            shot_count += 1
            
            # Scroll check
            scroll_h = page.evaluate("document.body.scrollHeight")
            client_h = page.evaluate("window.innerHeight")
            
            if scroll_h > client_h * 1.3:
                page.evaluate("window.scrollBy(0, window.innerHeight * 0.8)")
                time.sleep(1)
                img2 = os.path.join(temp_dir, f"shot_{shot_count:03d}.png")
                page.screenshot(path=img2)
                captured_images.append(img2)
                print(f"  [✓] Sayfa {shot_count} kaydedildi ({topic_clean[:25]} - Alt)")
                shot_count += 1
                
        context.close()
        
    # PDF Compilation
    clean_subj = target_book['subject'].replace(" ", "_")
    pdf_filename = f"{clean_subj}_3havo_Hoofdstuk_{chapter_num}.pdf"
    pdf_path = os.path.join(output_dir, pdf_filename)
    
    print(f"\n📑 {len(captured_images)} sayfa PDF'e birleştiriliyor -> {pdf_path}...")
    pil_images = [Image.open(f).convert("RGB") for f in captured_images]
    if pil_images:
        pil_images[0].save(
            pdf_path,
            save_all=True,
            append_images=pil_images[1:],
            resolution=150.0
        )
        size_mb = os.path.getsize(pdf_path) / (1024 * 1024)
        print(f"\n🎉 BAŞARILI! PDF oluşturuldu:")
        print(f"📍 Dosya: {pdf_path}")
        print(f"📦 Boyut: {size_mb:.2f} MB ({len(captured_images)} Sayfa)")
        
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
        
    return pdf_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Noordhoff Kitap ve Bölüm PDF Dönüştürücü")
    parser.add_argument("--list", action="store_true", help="Kitapları listele")
    parser.add_argument("--book", type=int, default=0, help="Kitap indexi (varsayılan: 0 - Aardrijkskunde)")
    parser.add_argument("--chapter", type=int, help="Bölüm numarası (örn: 1)")
    parser.add_argument("--output-dir", type=str, default=DEFAULT_DEST, help="PDF kayıt klasörü")
    
    args = parser.parse_args()
    if args.list:
        list_books()
    elif args.chapter is not None:
        export_chapter(args.book, args.chapter, output_dir=args.output_dir)
    else:
        list_books()

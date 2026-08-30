import os
import sys
import time
from playwright.sync_api import sync_playwright

USER_DATA_DIR = os.path.expanduser("~/.config/noordhoff_browser_profile")
URL = "https://apps.noordhoff.nl/my/nl/bookshelf?redirectPath=%2Fse%2Fcontent%2Ftheme%2F96c9a74a-a2c4-4d7d-8b7e-0042de398991%2Febook%2F729ba720-849b-43a5-84a2-e17bd7861a57&redirectPlatform=sep"

def main():
    os.makedirs(USER_DATA_DIR, exist_ok=True)
    print(f"Launching browser with profile in {USER_DATA_DIR}...")
    with sync_playwright() as p:
        # Launch Chromium with persistent context so logins stay saved
        context = p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=False,
            viewport=None,
            args=["--start-maximized", "--no-sandbox"]
        )
        page = context.pages[0] if context.pages else context.new_page()
        page.goto(URL, wait_until="domcontentloaded")
        print(f"Current page URL: {page.url}")
        print(f"Page title: {page.title()}")
        print("\n=== LÜTFEN BROWSER EKRANINDAN GİRİŞ YAPINIZ VEYA KİTAP SAYFASINA GEÇİNİZ ===")
        print("Tarayıcı 60 saniye boyunca açık kalacak. İnceleme yapıyoruz...")
        
        for i in range(12):
            time.sleep(5)
            print(f"[{ (i+1)*5 }s] Güncel URL: {page.url} | Başlık: {page.title()}")
            
        print("Kapatılıyor. Profil kaydedildi.")
        context.close()

if __name__ == "__main__":
    main()

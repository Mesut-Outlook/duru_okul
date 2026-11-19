# Görev: Firebase Realtime Database güvenliği (duru-okul)

Hazırlayan: Claude (claude.ai sohbeti), 2026-11-19. Bu dosya Claude Code için devir notudur.
Tamamlanınca bu dosyayı güncelle (durum satırları) ya da sil.

## Sorun
- Firebase 4 Ekim 2026'dan beri neredeyse her gün uyarı gönderiyor (45+ mail):
  "duru-okul-default-rtdb: herkes veritabanının tamamını okuyabilir / yazabilir".
- `database.rules.json` şu an: `{ "rules": { ".read": true, ".write": true } }`
- Site herkese açık (https://mesut-outlook.github.io/duru_okul/), DB adresi `js/cloud_sync.js` içinde açık.
- Sonuç: herkes `/scores`, `/scores_v2/duru`, `/scores_v2/baba` okuyabilir, üzerine yazabilir, silebilir;
  DB'nin herhangi bir yerine veri yazıp maliyet çıkarabilir.
- Sitedeki giriş (landing.js, `duru_users`, `simpleHash`) sadece localStorage'da; bulut verisini korumuyor.

## Mevcut veri akışı (js/cloud_sync.js)
- Yazma: `PUT {BASE}/scores_v2/<aktifKullanıcı>.json`, payload `{updatedAt, student, scores:[{key,val}]}`.
  Önce GET + `window.DURU_MERGE` ile birleştirip sonra PUT ("büyü, asla küçülme" kuralı).
- Okuma: kendi düğümü + eski `/scores` (sadece okunur, geçmiş için).
- Veli (`baba|veli|mesut`) ayrıca `/scores_v2/duru` okur (haalLeerlingOp).
- 20 sn'de bir pull. Auth yok, REST çağrıları `?auth=` olmadan.
- Eylül 2026 veri kaybı geçmişi var (yorumlarda) — merge mantığına dokunurken dikkat.

## Adım 0 — Yedek (ZORUNLU, önce)
Firebase Console → Realtime Database → Data → ⋮ → Export JSON. Ya da:
`npx firebase-tools@latest database:get / --project duru-okul > ~/duru-okul-rtdb-yedek-$(date +%F).json`
(Yedeği repoya koyma.) Ayrıca `scores_v2` altındaki kullanıcı adlarını listele.

## Adım 1 — Kuralları daralt (kod değişikliği yok)
`database.rules.json`:
```json
{
  "rules": {
    ".read": false,
    ".write": false,
    "scores": { ".read": true, ".write": false },
    "scores_v2": {
      "$user": {
        ".read":  "$user.matches(/^(duru|baba|veli|mesut)$/)",
        ".write": "$user.matches(/^(duru|baba|veli|mesut)$/) && newData.exists()",
        ".validate": "newData.hasChildren(['updatedAt', 'scores'])"
      }
    }
  }
}
```
- Adım 0'da `scores_v2` altında başka isim çıkarsa regex'e ekle (veya Mesut'a sor).
- Deploy: `npx firebase-tools@latest deploy --only database --project duru-okul` (Mesut onayıyla).
- Doğrula: siteyi aç, Duru ve baba ile senkron çalışıyor mu (konsolda HTTP 401/403 yok);
  `curl .../.json` (kök) → Permission denied; `curl -X PUT .../test.json` → reddedilmeli.
- Not: Bu adım tam çözüm değil; adresi bilen biri bu 4 düğümü hâlâ okuyup üzerine yazabilir.

## Adım 2 — Gerçek çözüm: Firebase Authentication (Google ile giriş)
- Firebase Console'da Authentication → Google sağlayıcısını aç; Authorized domains'e
  `mesut-outlook.github.io` (ve yerel test için `localhost`) ekle.
- Kullanıcılar: Duru'nun Google hesabı ve veli (Mesut) Google hesabı. (E-postalar repo public olduğu için buradan çıkarıldı;
  kurallar e-posta değil UID ile yazılacak.)
- `cloud_sync.js`: Firebase JS SDK (modular, CDN) ile `signInWithPopup` / oturum kalıcılığı;
  her REST çağrısına `?auth=<idToken>` ekle (token yenilemeyi `getIdToken()` ile yap).
  Mevcut merge/push güvenlik mantığını (DURU_MERGE, "okumadan yazma") KORU.
- Giriş ekranı: Google girişi bulut erişimi için zorunlu olsun; çevrimdışı/yerel mod çalışmaya devam etsin.
- Kurallar (örnek yön, e-posta yerine uid de kullanılabilir):
  - `scores_v2/duru`: okuma/yazma → Duru'nun hesabı; okuma → veli hesabı.
  - `scores_v2/baba`: okuma/yazma → veli hesabı.
  - `scores`: okuma → bu iki hesap; yazma → yok.
  - Kökte her şey kapalı.
- Dil kuralı: Duru'ya görünen metinler Felemenkçe, veliye Türkçe (CLAUDE.md).
- Projenin kalite kapılarını çalıştır (gate.js, teslim_check.js, open_check.js) ve headless tarayıcıyla giriş + senkron testi yap.

## Adım 3 — Küçük temizlik
- `js/landing.js` Duru'nun şifresini (`12341234`) açıkça içeriyor (hızlı giriş butonu, satır ~1435,
  ayrıca ~1553–1653 ve `xorCipher(..., 'duru:12341234')`). Repo public. Adım 2 sonrası bu yerel
  şifre mantığı sadeleştirilebilir; Duru bu şifreyi başka yerde kullanıyorsa değiştirsin.
- Firebase uyarı maillerinin kesildiğini birkaç gün izle.

## Durum
- [x] Adım 0 yedek — 2026-11-19, REST ile `~/duru-okul-rtdb-yedek-2026-11-19.json` (1,95 MB; repo dışı). `scores_v2`: yalnız `duru`, `baba`.
- [x] Adım 1 kurallar deploy edildi — 2026-11-19 (Mesut). Doğrulandı: kök okuma 401, `/test` ve `scores_v2/yabanci` yazma/okuma 401; `scores_v2/duru|baba` ve `scores` okuma 200. İstemci payload'ı her zaman `updatedAt` + dolu `scores` içerir (boşsa push yok) → `.validate` ile uyumlu.
- [~] Adım 2 Google girişi + kurallar — **kod hazır ve yayında (2026-11-19), Mesut'un konsol adımları bekleniyor.**
  Yapılan: `js/cloud_sync.js` → `FIREBASE_CONFIG` + `initAuth/metToken/koppelGoogle`; Firebase compat SDK 10.14.1
  (`index.html`, gstatic). `apiKey` boşken auth kapalı = eski davranış (senkron bozulmaz). Bağlı değilken buluta istek
  gitmez; senkron hapı "Google'a bağlan" olur (Duru: tek dokunuş; veli: pencerede "Google ile bağlan", e-posta + UID görünür).
  Doğrulama: Playwright + sahte Firebase stub — oturumsuz 0 istek, oturumlu her istek `?auth=TOK`; JS hatası yok;
  `test_score_merge.js` + `test_server_merge.py` geçti.
  **Kalan — Mesut (Firebase Console → duru-okul):**
  1. Authentication → Sign-in method → Google'ı etkinleştir.
  2. Authentication → Settings → Authorized domains → `mesut-outlook.github.io` ekle (localhost varsayılan var).
  3. ⚙ Project settings → General → Your apps → web app yoksa ekle (Hosting gerekmez) → `apiKey` + `appId`'yi Claude'a ver
     (gizli değil, koda açık yazılır).
  **Kalan — Claude:**
  4. `apiKey`/`appId`'yi `FIREBASE_CONFIG`'e yaz, `?v=` bump, push. ⚠️ Bu andan itibaren Google'a bağlanmamış cihazlar
     buluta yazmaz (yerelde kaydeder; bağlanınca büyüyen-birleştirme ile kayıpsız birleşir).
  **Kalan — Mesut + Duru:** 5. Kendi cihazlarında senkron hapına dokunup Google ile bağlanın.
     6. Authentication → Users'tan iki UID'yi Claude'a ver.
  **Kalan — Claude → Mesut:** 7. UID tabanlı kurallar (`scores`: iki hesap okur, kimse yazmaz; `scores_v2/duru`: Duru yazar,
     Duru + veli okur; `scores_v2/baba|veli|mesut`: yalnız veli; kök kapalı; `newData.exists()` + `.validate` korunur) →
     Mesut deploy eder → kontrol: bağlı iki cihazda senkron, token'sız okuma 401.
- [ ] Adım 3 temizlik

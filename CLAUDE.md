# CLAUDE.md — Duru_Okul (hub)

Duru'nun oefensites'lerini tek link altında toplayan hub. **Saf statik, build yok, ES-module yok**
(`file://` / `http.server` üzerinde çalışır). **Self-contained**: tüm siteler bu repoda gerçek
klasörler olarak gömülü (submodule yok; 2026-06-03'ten beri gömülü).

> **Dönem:** Duru **MAVO 2 → HAVO 3**'e geçti (2026-07-20). MAVO 2 içeriği arşivlendi (aşağı bak);
> yeni içerik HAVO 3 derslerinde toplanır. Yeni dersler henüz **kurulmadı** — önce altyapı.
>
> **Dil kuralı:** Geliştirici/koordinasyon dokümanları **Türkçe**; öğrenci-içeriği **Flamanca**.
> Ondalık ayraç metinlerde **virgül**. Bkz. `docs/DOC_STANDARD.md`.

## Kanonik dokümanlar (önce bunları oku)
- `docs/ENGINE_SPEC.md` — DURU veri sözleşmesi (register/registerExamen, soru tipleri, localStorage). **Tek doğru kaynak.**
- `docs/DOC_STANDARD.md` — tüm CLAUDE.md/MEMORY.md dosyalarının ortak yapısı + dil kuralı.
- `docs/PIPELINE.md` — belge → sınav üretim hattı + **model/agent politikası**.
- `coordination.md` — Opus ↔ agy (Antigravity) canlı görev panosu.

## Yapı
```
index.html        landing (iframe-shell & dashboard container)
css/style.css     vak-renkleri: blauw/groen/oranje/teal + dashboard stilleri (?v= bump'la)
js/landing.js     VAKKEN dizisi + render + iframe-shell + storage-interceptor + multi-user login
js/dashboard.js   istatistik dashboard'u + SVG chart + examens log (vak listeleri HARD-CODED)
server.py         yerel skor API'si (POST /api/score → scores.json)
docs/             kanonik standartlar (yukarı bak)
inbox/            ders materyali bırakma alanı (PDF/Word/görsel)
archief/mavo2/    ARŞİV: MAVO 2 dersleri (nask, economi, wiskunde, geschiedenis, nederlands)
havo3/            (henüz boş) HAVO 3 dersleri buraya kurulacak
```

## Model & agent politikası (ÖNEMLİ)
- **Planlama HER ZAMAN Opus** (ben). Kapsam, mimari, doğrulama bende.
- **agy = Google Antigravity.** `coordination.md`'yi ~15 dk'da bir yoklar, "Pending Tasks"ten iş
  çeker, üretir, sonucu geri yazar. Doğrudan çağrılmaz — **dosya üzerinden** emir verilir.
  Mevcut kod: `nederlands/begrijpend-lezen/generate_exam_agy.py` (Antigravity SDK + Gemini).
- **Sonnet/Haiku alt-agent'ları:** token tasarrufu için mekanik/hacimli üretim. Ayrıntı `docs/PIPELINE.md`.
- **Güncelleme disiplini:** her geliştirmeden sonra ilgili `MEMORY.md` + gerekiyorsa `CLAUDE.md`
  güncellenir, `coordination.md` görevi "Done"a taşınır. Kim uygularsa güncellemeyi de o yapar.

## Arşiv (MAVO 2)
MAVO 2 dersleri `archief/mavo2/` altında; skorları/istatistikleri **çalışmaya devam eder**
(localStorage anahtarları global, yol-bağımsız). Landing'de ayrı bir "Arşiv (MAVO 2)" bölümünden
erişilir. Arşiv dersleri eski slug'larını korur (`duru_nask_v1` …). Yeni HAVO 3 dersleri **yeni
slug** kullanmalı (`duru_h3_<vak>_v1`) — çakışmayı önlemek için (bkz. `docs/ENGINE_SPEC.md`).

## Dashboard & istatistik
`index.html` iki view içerir ("Mijn vakken" / "Mijn prestaties & statistieken"). `js/dashboard.js`
localStorage'ı okuyup tüm vaklar üzerinden toplar: 4 hero-kart (XP/badges/proeftoetsen/gemiddeld
cijfer) + per-vak kartlar (`renderVakKaarten`) + SVG score-timeline + doorzoekbaar logboek.
Cijfer = `1 + pct/100*9` (geslaagd ≥ 5,5). **CSS/JS değişince `index.html`'de `style.css?v=`'i bump'la** (şu an `v=2.5`).

## Landing düzeni (HAVO 3 — sıcak, alan-gruplu)
"Mijn vakken" görünümü `js/landing.js`'te `renderVakken` ile kurulur. Aktif (HAVO 3) dersler
**vakgebied'e göre** gruplanır (`DOMEINEN`: talen / exact / mens) ve `maakVakKaartHavo3` ile sıcak
kartlar (`.havo3-*` stilleri, `css/style.css` sonunda, scoped + tema-güvenli) basılır. Arşiv (MAVO 2)
dersleri altta açılır "Archief (MAVO 2)" bölümünde (`renderArchief`, eski kart stili). `VAKKEN` entry
alanları: `id, titel, icoon, domein('talen'|'exact'|'mens'), beschrijving, binnenkort?, href?, sleutel?, archief?`.
`binnenkort:true` = henüz site/data yok (tıklanmaz, "Binnenkort"). Aktif ders: `binnenkort` kaldır +
`href:'./havo3/<vak>/'` + `sleutel:'duru_h3_<vak>'` ekle → kart ilerleme/cijfer'i `leesVakData` ile gösterir.
Dashboard (statistieken view) henüz eski temada; HAVO 3'e uyarlama ayrı iş.

## Ders ekleme/arşivleme — 6 dokunma noktası (çapraz-referanssız!)
Bir ders şu yerlerde tanımlı; birini unutma:
1. `js/landing.js` → `VAKKEN` dizisi (kart + `domein` + href). Arşiv için: `archief:true` + href `./archief/mavo2/<klasör>/`.
2–4. `js/dashboard.js` → **üç ayrı hard-coded liste**: `practiceKeys`, `loadDuruAttempts(...)` çağrıları, `renderVakKaarten()` `vakken` dizisi.
5. `index.html` → log tablosu filtre çubuğu butonları (`data-filter`).
6. `css/style.css` → yalnızca YENİ renk eklerken `.vak-kaart--` / `.vak-badge--` / `.subject-badge.` / `.vak-stat-card--` / `.onderwerp-link--<renk>` (mevcut 4 renk hazır).
+ fiziksel klasör + `duru_<slug>_v1` / `_examens_v1` anahtarları. Linkler **her zaman göreli** (`./...`).

## Navigasyon (iframe-shell)
Ders `#vak-frame`'de açılır; sabit "← Terug naar de vakken" balığı. Geri = knop / Escape /
browser-back (`history.pushState` + `popstate`). Kapalıyken iframe `src` = `about:blank`
(asla boş `src=""` — hub'ı yeniden yükler). Multi-user login + `/api/score` sync `js/landing.js`'de.

## Storage & SVG iframe düzeltmeleri (kritik)
1. **Storage interception:** `js/landing.js` `Storage.prototype.setItem`'ı prototip düzeyinde
   `try-catch` ile override eder → `duru_*` sonuçlarını `POST /api/score`'a senkronlar +
   çok-kullanıcı için `user_<user>_<key>` ön-eki. (`Illegal invocation` hatasını önler.)
2. **SVG ring:** iframe içinde Safari'de `<linearGradient url(#..)>` bozulur; tüm ilerleme
   çemberleri `engine.js`/`exams.js`'de solid tema rengi (`stroke="var(--paars)"`) kullanır.

## Çalıştırma & hosting
- **Yerel:** `Duru_Okul_Baslat.command` veya `python3 -m http.server 8125` → `http://localhost:8125/`.
  Ev ağı: `http://<mac-ip>:8125/`. UFW: `sudo ufw allow 8125/tcp`.
- **GitHub Pages:** `main`'e her push'ta GitHub Actions ile deploy. `.nojekyll` var; client tarafı
  bunu algılayıp `/api/score` senkronunu atlar.

## Git
`user.name=Mesut-Outlook`, `user.email=ozdemirmesut@gmail.com`. Commit-trailer:
`Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>`. Git backup amaçlı; commit/push sadece istenince.

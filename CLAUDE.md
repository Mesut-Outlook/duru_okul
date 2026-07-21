# CLAUDE.md — Duru_Okul (hub)

Duru'nun oefensites'lerini tek link altında toplayan hub. **Saf statik, build yok, ES-module yok**
(`file://` / `http.server` üzerinde çalışır). **Self-contained**: tüm siteler bu repoda gerçek
klasörler olarak gömülü (submodule yok; 2026-06-03'ten beri gömülü).

> **Dönem:** Güncel ders yılı **2026-2027 · HAVO 3**. Duru MAVO 2 → HAVO 3'e geçti (2026-07-20).
> **Arşiv ders yılına göre**: `archief/<schooljaar>/` (ör. `archief/2025-2026/` = MAVO 2). Bir yıl
> bitince o yılın dersleri `archief/<o-yıl>/`'e taşınır. Yeni HAVO 3 dersleri henüz kurulmadı — önce altyapı.
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
archief/<schooljaar>/  ARŞİV: ders yılına göre (ör. archief/2025-2026/ = MAVO 2 dersleri)
havo3/<vak>/      HAVO 3 ders-siteleri (10 vak, smoke-test: şimdilik 1 proeftoets/5 soru). Anahtar: duru_2627_<slug>_*
```

## Model & agent politikası (ÖNEMLİ)
- **Planlama HER ZAMAN Opus** (ben). Kapsam, mimari, doğrulama bende.
- **agy = Google Antigravity.** `coordination.md`'yi ~15 dk'da bir yoklar, "Pending Tasks"ten iş
  çeker, üretir, sonucu geri yazar. Doğrudan çağrılmaz — **dosya üzerinden** emir verilir.
  Mevcut kod: `nederlands/begrijpend-lezen/generate_exam_agy.py` (Antigravity SDK + Gemini).
- **Sonnet/Haiku alt-agent'ları:** token tasarrufu için mekanik/hacimli üretim. Ayrıntı `docs/PIPELINE.md`.
- **Güncelleme disiplini:** her geliştirmeden sonra ilgili `MEMORY.md` + gerekiyorsa `CLAUDE.md`
  güncellenir, `coordination.md` görevi "Done"a taşınır. Kim uygularsa güncellemeyi de o yapar.

## Arşiv (ders yılına göre)
Eski dersler `archief/<schooljaar>/<vak>/` altında (ör. `archief/2025-2026/nask/` = MAVO 2).
Skorları/istatistikleri **çalışmaya devam eder** (localStorage anahtarları global, yol-bağımsız).
Landing'de açılır **"Archief — vorige schooljaren"** bölümünden erişilir; içeride **yıla göre gruplu**
(en yeni yıl üstte, başlık "2025-2026 · MAVO 2"). Yıl→niveau etiketi `landing.js`'teki `JAAR_NIVEAU`
tablosunda; yeni yıl eklerken oraya bir satır ekle. Arşiv dersleri eski slug'larını korur
(`duru_nask_v1` …). Yeni yıl dersleri **yıl-kodlu anahtar** kullanmalı (`duru_<jaarcode>_<slug>_v1`,
ör. HAVO 3 → `duru_2627_<slug>_v1`) — çakışmayı önlemek + yıla göre istatistik için (bkz. `docs/ENGINE_SPEC.md`).

**Bir ders yılını arşivleme (yıl sonunda):** `git mv <vak> archief/<schooljaar>/<vak>` → `VAKKEN`
entry'sine `archief:true` + `jaar:'<schooljaar>'` + href `./archief/<schooljaar>/<vak>/` → `JAAR_NIVEAU`'ye
yıl→niveau ekle → `?v=` bump.

## Dashboard & istatistik
`index.html` iki view içerir ("Mijn vakken" / "Mijn prestaties & statistieken"). `js/dashboard.js`
**yıl-farkında**: tüm ders/yıl kombinasyonları `VAK_REGISTER` dizisinde tek satırda tanımlı (jaar,
id, titel, icoon, kleur, practiceKey, examKey; begrijpend lezen `special:'begrijpend'`). Üstte bir
**yıl-seçici** (`#jaar-selector`, `renderJaarSelector`) var; seçim `localStorage.duru_dashboard_jaar`'da
kalıcı. Seçili yıla göre filtrelenmiş satırlardan: 4 hero-kart (XP/badges/proeftoetsen/gemiddeld
cijfer, o yıla özel) + per-vak kartlar (`renderVakKaarten`) + SVG score-timeline + filtre çubuğu
(`renderFilterBar`, yıla göre yeniden kurulur) + doorzoekbaar logboek. 2025-2026 (MAVO 2) anahtarları
**yılsız ve donmuş** (`duru_nask_v1` …) — `VAK_REGISTER`'da sabit `jaar:'2025-2026'` ile etiketli,
asla değiştirilmez. Yeni yıllar `duru_<jaarcode>_<slug>_v1`/`_examens_v1` (jaarcode: `2026-2027→2627`).
Cijfer = `1 + pct/100*9` (geslaagd ≥ 5,5). **CSS/JS değişince `index.html`'de `style.css?v=`'i bump'la** (şu an `v=2.9`).

## Landing düzeni (HAVO 3 — sıcak, alan-gruplu)
"Mijn vakken" görünümü `js/landing.js`'te `renderVakken` ile kurulur. Aktif (HAVO 3) dersler
**vakgebied'e göre** gruplanır (`DOMEINEN`: talen / exact / mens) ve `maakVakKaartHavo3` ile sıcak
kartlar (`.havo3-*` stilleri, `css/style.css` sonunda, scoped + tema-güvenli) basılır. Arşiv
dersleri altta açılır "Archief — vorige schooljaren" bölümünde **yıla göre gruplu** (`renderArchief`,
eski kart stili). `VAKKEN` entry alanları: `id, titel, icoon, domein('talen'|'exact'|'mens'),
beschrijving, binnenkort?, href?, sleutel?, archief?, jaar?`.
`binnenkort:true` = henüz site/data yok (tıklanmaz, "Binnenkort"). Aktif ders: `binnenkort` kaldır +
`href:'./havo3/<vak>/'` + `sleutel:'duru_2627_<vak>'` ekle → kart ilerleme/cijfer'i `leesVakData` ile gösterir.
**Şu an 10 HAVO 3 dersi aktif** (`havo3/<vak>/`, her biri 1 proeftoets/5 soru = smoke-test); Duru materyal
verdikçe onderwerpen + daha çok proeftoets eklenecek. Dashboard **yıl-farkında** (yukarı bak); HAVO 3
dersleri `VAK_REGISTER`'da 2026-2027 satırları olarak kayıtlı.

## Ders ekleme/arşivleme — dokunma noktaları (çapraz-referanssız!)
Bir ders şu yerlerde tanımlı; birini unutma:
1. `js/landing.js` → `VAKKEN` dizisi (kart + `domein` + href). Arşiv için: `archief:true` + `jaar:'<schooljaar>'` + href `./archief/<schooljaar>/<klasör>/`. Aktif HAVO 3 dersi: `sleutel:'duru_2627_<slug>'` zaten var, `binnenkort` kaldır.
2. `js/dashboard.js` → **tek kaynak** `VAK_REGISTER`'a bir satır ekle (jaar, id, titel, icoon, kleur, practiceKey, examKey). Hero-kartlar, `renderVakKaarten`, filtre çubuğu (`renderFilterBar`) ve yıl-seçici otomatik türer — ayrı hard-coded liste YOK.
3. `index.html` → log tablosu filtre çubuğu artık JS ile dolduruluyor (`#table-filter-bar` boş `<div>`), dokunmaya gerek yok.
4. `css/style.css` → yalnızca YENİ renk eklerken `.vak-kaart--` / `.vak-badge--` / `.subject-badge.` / `.vak-stat-card--` / `.onderwerp-link--<renk>` (mevcut 4 renk hazır).
+ fiziksel klasör + `duru_<slug>_v1` / `_examens_v1` anahtarları (legacy 2025-2026 yılsız, yeni yıllar `duru_<jaarcode>_<slug>_v1`). Linkler **her zaman göreli** (`./...`).

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

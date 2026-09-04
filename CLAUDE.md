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
- `docs/PIPELINE.md` — belge → sınav üretim hattı + **model/agent politikası** + **kalite kapısı kuralları**.
- `tools/README.md` — kalite denetim araçları (`gate.js` / `spread.py` / `open_check.js`).
- `coordination.md` — Opus ↔ agy (Antigravity) canlı görev panosu.

## Yapı
```
index.html        landing (iframe-shell & dashboard container)
css/style.css     vak-renkleri: blauw/groen/oranje/teal + dashboard stilleri (?v= bump'la)
js/landing.js     VAKKEN dizisi + render + iframe-shell + storage-interceptor + multi-user login
js/dashboard.js   istatistik dashboard'u + SVG chart + examens log (vak listeleri HARD-CODED)
server.py         yerel skor API'si (POST /api/score → scores.json)
docs/             kanonik standartlar (yukarı bak)
tools/            soru kalite denetimi: gate.js (12 kural), spread.py, open_check.js (bkz. tools/README.md)
inbox/            ders materyali bırakma alanı (PDF/Word/görsel)
archief/<schooljaar>/  ARŞİV: ders yılına göre (ör. archief/2025-2026/ = MAVO 2 dersleri)
havo3/<vak>/      HAVO 3 ders-siteleri (12 vak). Anahtar: duru_2627_<slug>_*. Doluluk için CLAUDE.md "Ders doluluk durumu"
```

## Ders doluluk durumu (2026-09-04)
Sayılar `havo3/<vak>/js/{bootstrap,data/*}.js`'i node `vm`'de çalıştırıp `DURU.onderwerpen` /
`DURU.examens` ve `vragen` uzunluklarını sayarak çıkarılır (`tools/build_hoofdstukken.js` ile aynı
teknik). `kapsanan hoofdstuk` = `bootstrap.js`'teki `DURU.hoofdstukken`. İçerik eklendikçe güncelle.

| vak | onderwerp | proeftoets | soru | kapsanan hoofdstuk |
|---|---|---|---|---|
| geschiedenis | 30 | 30 | 840 | H1–H6 (tam) |
| frans | **0** | 40 | 800 | H1–H8 (onderwerp yok — sadece sınav) |
| duits | 18 | 30 | 744 | H1–H6 |
| engels | 18 | 30 | 744 | H1–H6 |
| natuurkunde | 25 | 25 | 700 | H1–H4, H8 (H5/H6/H7 eksik) |
| economie | 12 | 23 | 556 | H1–H4 |
| aardrijkskunde | 10 | 10 | 280 | H1–H2 (tam) |
| scheikunde | 6 | 10 | 252 | H1–H2 (H3–H7 eksik) |
| wiskunde | 5 | 10 | 240 | H2 |
| biologie | 2 | 5 | 116 | H10 |
| maatschappijleer | 0 | 1 | 5 | **yok** — smoke-test |
| nederlands | 0 | 1 | 5 | **yok** — smoke-test |

**Toplam: 126 onderwerp · 215 proeftoets · 5282 soru.**
`maatschappijleer` + `nederlands` `bootstrap.js`'te `DURU.hoofdstukken = []` tutar (Duru henüz
materyal vermedi), bu yüzden tek sınavları bilinçli olarak `hoofdstuk`'suzdur ve manifest'e
girmez → "Overige toetsen"e düşer. **Buraya ünite numarası uydurma**; materyal gelince önce
`bootstrap.js`'e gerçek hoofdstuk'ları yaz.

Bekleyen üretim işleri `coordination.md` → "Pending Tasks" (TASK-08, TASK-09).
Her teslim `tools/gate.js` kapısından geçmeli (bkz. `docs/PIPELINE.md` → Kalite kapısı).

## 📌 "Test Hazırla" ve Bölüm Üretim Standardı (Zorunlu Kural)
Kullanıcı **"test hazırla"** dediğinde veya herhangi bir ders için yeni bir bölüm/hoofdstuk materyali işlendiğinde **kendiliğinden ve otomatik olarak**:
1. **Kavram, Kişi ve Olayların Çıkarımı**: O bölümdeki tüm tanım kelimeleri/kavramlar (*begrippen*), önemli şahsiyetler (*belangrijke personen*), özel olaylar/tarihler (*gebeurtenissen/data*) ve sınavda çıkabilecek tüm terimler eksiksiz çıkarılır.
2. **Özel Bölüm (Begrippen & Kernconcepten)**: Her ders ve her bölüm (hoofdstuk) için ayrı ayrı olmak şartıyla o bölüme ait tüm bu kavramları içeren özel bir konu/sözlük modülü eklenir.
3. **Özel Kavram Testi (Begrippentoets)**: SADECE bu kelimeleri/kavramları/kişileri/olayları doğrudan soran bağımsız bir test/sınav (mc, invul, open) hazırlanır.

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

## Hoofdstuk (ünite) verisi — TEK KAYNAK, elle yazma
Ünite kırılımı **üretilmiş bir manifest**ten gelir; hiçbir yerde elle hoofdstuk listesi tutulmaz.
- `tools/build_hoofdstukken.js` → her `havo3/<vak>/js/bootstrap.js` + `js/data/*.js`'i node `vm`
  içinde çalıştırıp `js/hoofdstukken.js` üretir (hoofdstuk listesi, examId→hoofdstuk,
  onderwerpId→hoofdstuk, ünite başına sınav/onderwerp sayısı). Ders verisi değişince **yeniden çalıştır**;
  `--check` bayat manifest'te exit 1 döner.
- `js/hoofdstuk_util.js` → ortak `window.DURU_HF` API. `dashboard.js` ve `ouder_dashboard.js`
  yalnız bunu kullanır. Yükleme sırası: `hoofdstukken.js` → `hoofdstuk_util.js` → `landing.js`.
- **⚠️ `ex-h3-<vak>-N` id'sindeki `h3` = NIVEAU (HAVO 3), hoofdstuk DEĞİL.** Sınav id'sinden
  hoofdstuk çıkarma; hoofdstuk'suz kayıt "Overige toetsen"e düşer. Sıra: `att.hoofdstuk` →
  manifest → başlıkta `Hoofdstuk N` → `null`.
- Yeni sınav dosyası yazarken `registerExamen({...})`'e **`hoofdstuk` alanını koymak zorunlu**;
  onderwerp'lerde de `hoofdstuk` zaten zorunlu (`docs/ENGINE_SPEC.md`).

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
Cijfer = `1 + pct/100*9` (geslaagd ≥ 5,5). **CSS/JS değişince `index.html`'de `style.css?v=`'i bump'la** (şu an `v=3.9`).

## Veli paneli (`js/ouder_dashboard.js`) — 2026-09 yeniden tasarımı
Sadece Baba görür (`#tab-ouder-btn` varsayılan gizli). Dil **Türkçe**, ders adları Flamanca.
Veri toplama `collectParentReportData(user, jaar)`'da — manifest-farkında (`window.DURU_HF`) ve
`VAK_CONFIG` ile **iki yılı da** kapsar; render katmanı bundan türer, ayrı hesap yapmaz.
Okuma sırası: **durum cümlesi → cijferschaal → "Önce buraya bakın" → ders listesi**.
- **Cijferschaal**: Hollanda 1–10 ölçeği gerçek bir cetvel (`.ouder-schaal*`). 5,5 eşiği çizgiyle
  işaretli, büyük nokta genel ortalama, küçük noktalar her dersin ortalaması.
- **Sekmeler** (`data-ouder-view`): `overzicht` / `vakken` / `units` / `logboek`. Yalnız aktif
  görünüm HTML'e basılır. `actieveView` + `gekozenVak` + `logFilter` modül düzeyinde tutulur, böylece
  yıl değişimi ve cloud-sync yeniden render'ı seçimi kaybetmez.
- **Anlam renkleri marka yeşilinden ayrıdır**: `--ouder-goed/net/zwak` (+ `-zacht` tonları)
  `#ouder-view` üzerinde tanımlı, `html.dark #ouder-view`'de yeniden tanımlanır. Yeşil = "iyi"
  demektir, marka rengi değil. Yeni renk eklerken bu ikisini karıştırma.
- Ders satırı/chip'i tıklanınca `vakken` görünümü o dersle açılır (`data-open-vak` / `data-kies-vak`).
- Yazdırma `@media print` ile: çubuk, sekmeler ve filtreler gizlenir, kartlar sayfa bölmez.

## Landing düzeni (HAVO 3 — sıcak, alan-gruplu)
"Mijn vakken" görünümü `js/landing.js`'te `renderVakken` ile kurulur. Aktif (HAVO 3) dersler
**vakgebied'e göre** gruplanır (`DOMEINEN`: talen / exact / mens) ve `maakVakKaartHavo3` ile sıcak
kartlar (`.havo3-*` stilleri, `css/style.css` sonunda, scoped + tema-güvenli) basılır. Arşiv
dersleri altta açılır "Archief — vorige schooljaren" bölümünde **yıla göre gruplu** (`renderArchief`,
eski kart stili). `VAKKEN` entry alanları: `id, titel, icoon, domein('talen'|'exact'|'mens'),
beschrijving, binnenkort?, href?, sleutel?, archief?, jaar?`.
`binnenkort:true` = henüz site/data yok (tıklanmaz, "Binnenkort"). Aktif ders: `binnenkort` kaldır +
`href:'./havo3/<vak>/'` + `sleutel:'duru_2627_<vak>'` ekle → kart ilerleme/cijfer'i `leesVakData` ile gösterir.
**Şu an 12 HAVO 3 dersi aktif** (`havo3/<vak>/`, her biri 1 proeftoets/5 soru = smoke-test); Duru materyal
verdikçe onderwerpen + daha çok proeftoets eklenecek. Dashboard **yıl-farkında** (yukarı bak); HAVO 3
dersleri `VAK_REGISTER`'da 2026-2027 satırları olarak kayıtlı.

## Ders ekleme/arşivleme — TEK dokunma noktası (2026-09-04'ten beri)
Ders listesi eskiden üç yerde vardı (`VAKKEN` / `VAK_REGISTER` / `VAK_CONFIG`); son ikisi kelimesi
kelimesine aynıydı. Artık **tek kaynak `js/vakken.js` → `window.DURU_VAKKEN`**.
1. **`js/vakken.js`'e bir satır ekle** — `jaar, id, titel, icoon, kleur, practiceKey, examKey`
   (+ HAVO 3 için `domein`, `beschrijving`). Hepsi buradan türer:
   `dashboard.js → VAK_REGISTER`, `ouder_dashboard.js → VAK_CONFIG`, `landing.js` HAVO 3 kartları
   (`landingKaarten()`; `href` ve `sleutel` `id`/`practiceKey`'den üretilir). Başka liste YOK.
2. **Arşiv dersleri** hâlâ `js/landing.js` → `VAKKEN`'in sonundaki blokta. Orası saf navigasyon
   (açılır kategori, iç içe `onderwerpen`) ve istatistik kaydında karşılığı yok — bilerek ayrı.
   Arşiv için: `archief:true` + `jaar:'<schooljaar>'` + href `./archief/<schooljaar>/<klasör>/`.
3. `css/style.css` → yalnızca YENİ renk eklerken `.vak-kaart--` / `.vak-badge--` / `.subject-badge.` /
   `.vak-stat-card--` / `.onderwerp-link--<renk>` (mevcut 4 renk hazır).
4. `index.html` → filtre çubuğu JS ile doluyor, dokunma. Yeni paylaşılan dosya eklersen
   `vakken.js`/`cijfer_util.js`'ten **sonra**, `landing.js`'ten **önce** yükle.
+ fiziksel klasör. **⚠️ `practiceKey`/`examKey` BEYAZ ÇİZGİ**: Duru'nun kayıtlı geçmişinin anahtarı,
asla yeniden adlandırılmaz (legacy 2025-2026 yılsız, yeni yıllar `duru_<jaarcode>_<slug>_v1`).
Linkler **her zaman göreli** (`./...`).

## Not hesabı — tek kaynak `js/cijfer_util.js` (`DURU_CIJFER`)
`1 + pct/100*9` formülü ve 5,5 geçme sınırı eskiden iki panoda ~20 yerde elle yazılıydı.
Artık: `van(goed,totaal)` · `vanPct(pct)` · `geslaagd(c)` · `klasse(c,aantal)` → `goed|net|zwak|none` ·
`examenklaar(c)` (≥8,5) · `tekst(c)` (virgüllü) · `positie(c)` (1–10 ölçeğinde %) · `gemiddelde(lijst)`.
Eşikler `DREMPEL/GOED/TOP` sabitlerinde. **Renk burada YOK** — her panonun kendi token'ı var
(`--ouder-goed` vs `--groen`); paylaşılan şey sınıflandırma, biçimlendirme değil.

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

## Skor kayıt hattı (server.py) — v2, 2026-09-04
`scores.json` **append-only anlık görüntü kütüğüydü**: motor her cevapta `setItem` → interceptor
tüm bloğu POST → `server.py` dosyanın tamamını yeniden yazıyordu. 723 kayıt / 7 anahtar = 27 MB,
ve her cevap tüm dosyayı okuyup yazıyordu. Şimdi:
- **`scores.json` = `{"version":2,"keys":{<anahtar>: <kayıt>}}`** — anahtar başına tek kayıt.
  Gelen veri **birleştirilir** (`history` union'ı, `attemptId` üzerinden) → `restoreScores()`'un
  kurtarma davranışı korunur, dosya büyümez. **27,3 MB → 0,58 MB, sıfır poging kaybı.**
- **`events.jsonl`** — yeni poging başına bir satır (~100 B), append-only, parse gerekmez.
- **`GET /api/score` hâlâ liste döner** (`list(keys.values())`) — `js/landing.js → restoreScores(data)`
  dizi beklediği için sözleşme değişmedi.
- v1 liste formatı **ilk okumada otomatik göç eder**, önce `scores_v1_backup_<tarih>.json` yazılır.
- **İstemci tarafı debounce**: `js/landing.js → queueScoreSync()` anahtar başına 2 sn sessizlikten
  sonra gönderir (sınav başına ~20 POST → 1). Sekme kapanırken `pagehide`/`visibilitychange`'de
  `sendBeacon` ile flush edilir, veri kaybolmaz.

## Çalıştırma & hosting
- **Yerel:** `Duru_Okul_Baslat.command` veya `python3 -m http.server 8125` → `http://localhost:8125/`.
  Ev ağı: `http://<mac-ip>:8125/`. UFW: `sudo ufw allow 8125/tcp`.
- **GitHub Pages:** `main`'e her push'ta GitHub Actions ile deploy. `.nojekyll` var; client tarafı
  bunu algılayıp `/api/score` senkronunu atlar.

## Git
`user.name=Mesut-Outlook`, `user.email=ozdemirmesut@gmail.com`. Commit-trailer:
`Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>`. Git backup amaçlı; commit/push sadece istenince.

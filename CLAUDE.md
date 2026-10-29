# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# Duru_Okul (hub)

Duru'nun oefensites'lerini tek link altında toplayan hub. **Saf statik, build yok, ES-module yok**
(`file://` / `http.server` üzerinde çalışır). **Self-contained**: tüm siteler bu repoda gerçek
klasörler olarak gömülü (submodule yok; 2026-06-03'ten beri gömülü).

> **Dönem:** Güncel ders yılı **2026-2027 · HAVO 3**. Duru MAVO 2 → HAVO 3'e geçti (2026-07-20).
> **Arşiv ders yılına göre**: `archief/<schooljaar>/` (ör. `archief/2025-2026/` = MAVO 2). Bir yıl
> bitince o yılın dersleri `archief/<o-yıl>/`'e taşınır. HAVO 3'ün 12 dersi `havo3/<vak>/` altında aktif.
>
> **Dil kuralı:** Geliştirici/koordinasyon dokümanları **Türkçe**; öğrenci-içeriği **Flamanca**.
> Ondalık ayraç metinlerde **virgül**. Bkz. `docs/DOC_STANDARD.md`.

## Komutlar
Build/lint yok. Tarayıcıda `?v=` önbellek bump'ı dışında derleme adımı yok.
```bash
python3 -m http.server 8125                 # yerel çalıştır → http://localhost:8125/
python3 server.py                           # aynı + /api/score yerel skor yedeği (scores.json'a YAZAR)
python3 -m http.server 8125 --bind 0.0.0.0  # telefondan önizleme: http://<lan-ip>:8125/ (UFW: 8125/tcp)
node tools/gate.js <vak> [--only=h2,h3]     # soru kalite kapısı — her içerik teslimi geçmeli
node tools/build_hoofdstukken.js [--check]  # js/hoofdstukken.js manifest'i üret / bayatsa exit 1
node tools/test_score_merge.js              # senkron/merge regresyonu (20 kontrol)
python3 tools/test_server_merge.py          # server.py voeg_samen() regresyonu (15 kontrol)
node --check js/<dosya>.js                  # tek dosya sözdizimi
```
- `test_score_merge.js` fonksiyonları **ve** merger'ın kullandığı modül sabitlerini (`VERWIJDERDE_EXAMENS`,
  `sliceVar`) `landing.js`'ten keser. Merger yeni bir modül değişkeni kullanırsa teste de `sliceVar` ekle
  (2026-09-27 → 10-10 arası bu yüzden ReferenceError ile kırıktı).
- UI doğrulaması: Playwright (python, kurulu) ile hub'ı aç, `localStorage`'a `user_duru_<anahtar>` yaz,
  `duru_active_user` = `duru`/`baba`; Firebase isteklerini `route(...).abort()` ile kes. Telefon = 390px viewport,
  ölçüt `document.documentElement.scrollWidth === 390`. Ders siteleri tek başına açılınca hub'a yönlenir →
  `openInIframe('./havo3/<vak>/', …)` ile iframe içinde test et.
- Deploy: `main`'e push → GitHub Actions (`.github/workflows/deploy.yml`) → GitHub Pages. Canlı: https://mesut-outlook.github.io/duru_okul/

## Kanonik dokümanlar (önce bunları oku)
- `docs/ENGINE_SPEC.md` — DURU veri sözleşmesi (register/registerExamen, soru tipleri, localStorage). **Tek doğru kaynak.**
- `docs/DOC_STANDARD.md` — tüm CLAUDE.md/MEMORY.md dosyalarının ortak yapısı + dil kuralı.
- `docs/PIPELINE.md` — belge → sınav üretim hattı + **model/agent politikası** + **kalite kapısı kuralları**.
- `tools/README.md` — kalite denetim araçları (`gate.js` / `spread.py` / `open_check.js`).
- `coordination.md` — Opus ↔ agy (Antigravity) canlı görev panosu.

## Alt klasör notları (o klasörde çalışırken yüklenir)
- `havo3/CLAUDE.md` — **ders doluluk tablosu** (onderwerp/proeftoets/soru sayıları, id aralıkları, silinmiş/ayrılmış id'ler).
  İçerik ekleyince orayı güncelle; yeni sınav id'si seçmeden önce oku.
- `js/CLAUDE.md` — hub arayüzü: Duru'nun ilerleme sayfası, veli paneli, startpaneel/landing, açık testler, test süresi,
  koyu tema, telefon düzeni, `vak_shell`. Arayüze dokunmadan önce oku.
- CSS/JS değişince `index.html`'de `?v=`'i bump'la (şu an `style.css?v=6.7`).
- **⚠️ CSS'te fazladan `}`** sonraki kuralı sessizce yutar (2026-10-10: `body.ouder-actief .hero` böyle kaybolmuştu). Kural
  silerken `{`/`}` dengesini kontrol et.

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
  hoofdstuk çıkarma; hoofdstuk'suz kayıt "Overige toetsen"e düşer. Sıra (2026-10-15'ten beri): manifest
  (sınavın güncel hoofdstuk'u) → `att.hoofdstuk` → başlıkta `Hoofdstuk N` → `null`.
- **Kitap dışı ünite = `label`** (2026-10-15): `DURU.hoofdstukken` girdisi `label` taşıyabilir (wiskunde: `nr: 90,
  label: "Herhaling MAVO 2"`). "Hoofdstuk N"/"HN" yerine label gösterilir: ders sitesi `DURU.hfNaam(h)` (bootstrap), hub
  `DURU_HF.kort(vakId, nr)`; manifest `label`'ı taşır. `nr` yalnız anahtardır, sayı olmalı (onclick'te tırnaksız).
  **Denemenin ünitesi önce sınavın GÜNCEL hoofdstuk'undan** (manifest / `DURU.examens`), `att.hoofdstuk` yalnız yedek —
  yoksa bir ünite yeniden numaralanınca eski denemeler yanlış üniteye düşer (Statistiek'in 6 denemesi `hoofdstuk: 2` taşır).
- Yeni sınav dosyası yazarken `registerExamen({...})`'e **`hoofdstuk` alanını koymak zorunlu**;
  onderwerp'lerde de `hoofdstuk` zaten zorunlu (`docs/ENGINE_SPEC.md`).
- **Ders sitelerinde testler hoofdstuk altında gösterilir** (2026-09-12): hiçbir ders sayfasında
  hoofdstuk'suz düz test listesi kalmadı (nederlands 2026-10-28'de eklendi: `<details class="chapter-accordion">`, CSS engels'ten). duits/aardrijkskunde/biologie/scheikunde/wiskunde →
  `exams.js → DURU.examenGroepen()` (`ex.hoofdstuk` + `DURU.hoofdstukken`, bilinmeyen → "Overige
  toetsen") + `<details class="chapter-accordion">` (engels/frans deseni). natuurkunde H1 ayrıca
  **paragraf** bazlı: sınavdaki `"paragraaf"` alanı (`"1.1"`…`"1.5"`, `"mix"`, `"eind"`) →
  `bootstrap.js → DURU.getParagraafInfo`. Gruplama için elle id listesi tutma.
- **⚠️ Kullanılmış bir sınav id'sinin içeriği değiştirilmez.** Duru'nun geçmişi `examId` + soru
  sırasıyla saklanır; içerik değişirse eski denemesi yeni teste yazılır. Yeni sınav = yeni id.
  (2026-09-12: natuurkunde 1–5 böyle ezilmişti; orijinaller geri alındı, yeniler 35–39'a taşındı.)
  **Silmek de yasak.** 2026-09-22: `ex-h3-aardrijkskunde-1` (6 poging) ve `ex-h3-engels-1` (14 poging)
  smoke-test'leri, gerçek içerik `examen_1.js`'in **üzerine** yazılınca kaybolmuştu → Duru'nun
  denemeleri hiçbir sınava bağlı değildi ("0/10 toets" ama ort. 7,3). Orijinalleri
  `js/data/examen_0_start.js` olarak geri geldi (hoofdstuk'suz → "Overige toetsen").
  Yeni içerik için **yeni dosya adı** kullan, `examen_1.js` gibi mevcut dosyayı ezme.
  Ders sitelerinde hoofdstuk'suz sınav artık **H1'e değil "Overige toetsen"e** düşer
  (`ex.hoofdstuk || 1` deseni kaldırıldı: duits/engels/frans); "N vragen" `×20` tahmini değil gerçek sayı.

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
**Ortalama = her testin SON denemesi** (2026-09-27): `laatstePerToets(lijst)` / `gemiddeldeLaatste(lijst, veld)`.
Aynı test 8 kez çözüldüyse (%40 … %75) ortalamaya tek test olarak son notla girer. Ünite, ders, yıl ortalaması,
ders kartı (`landing.js`), veli paneli ve 12 ders sitesinin dashboard'u (`engine.js`, kendi yerel kopyası) bununla hesaplar.
**Gidiş** (son 3 vs önceki 3), **`recent`/"dikkat"** ve **en iyi not** bilerek denemeler üzerinden kalır — onlar ilerlemeyi ölçer.
Önceden tüm denemelerin ortalamasıydı: Duru'nun genel ortalaması 7,0 görünüyordu, son-deneme hesabıyla 7,6.
Eşikler `DREMPEL/GOED/TOP` sabitlerinde. **Renk burada YOK** — her panonun kendi token'ı var
(`--ouder-goed` vs `--groen`); paylaşılan şey sınıflandırma, biçimlendirme değil.

## Giriş & veli şifresi (2026-09-22)
Duru girişi değişmedi (hızlı düğme). **Veli (`baba`/`veli`/`mesut`) artık gerçek şifre ister:**
"Baba" düğmesi yalnız adı doldurur; `12341234` (Duru'nun şifresi) veli için reddedilir; cihazda henüz
güçlü bir veli şifresi yoksa ilk geçerli (≥6) şifre veli şifresi olarak kaydedilir, sonra yalnız o kabul
edilir. Bu üç ad "Kayıt Ol"dan alınamaz. Önceden ≥6 karakterli **her** şifre kabul edilip üzerine
yazılıyordu. Not: istemci tarafı, cihaz başına bir kilittir — çocuğa karşı yeterli, gerçek güvenlik değil.

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

## ⚠️ Bulut senkron & birleştirme değişmezi (2026-09-20 veri kaybı)
**Değişmez: BİRLEŞTİRME BÜYÜYEBİLİR, ASLA KÜÇÜLEMEZ.** Duru'nun geçmişi yalnızca eklenir.
Bir senkron yolu bir anahtarı küçültüyorsa o bir hatadır, çakışma çözümü değildir.

2026-09-20'de 865 XP → 95 ve 5 → 1 madalya (natuurkunde) ile dört derste 199 poging kayboldu.
Üç kusur üst üste bindi:
1. **`js/landing.js → restoreScores()` yereli okumuyordu.** `newVal`'i yalnız gelen paketten
   kurup `localStorage`'ı eziyordu; yalnızca yerelde olan XP/madalya/history siliniyordu.
   Artık yereldeki değer de bir **birleştirme kaynağı** (`bronnen = data.concat([lokaal])`).
2. **`window.restoreScores` hiç export edilmemişti**, bu yüzden `js/cloud_sync.js →
   mergeRemoteData` her zaman kendi yedek tepesine düşüyordu: `setItem(targetKey, remoteVal)`
   — sıfır birleştirme, kör üzerine yazma, **20 saniyede bir**. Asıl yıkıcı buydu.
   Artık export ediliyor; merger yoksa pull **hiçbir şey yazmaz**.
3. **Tek paylaşımlı Firebase düğümü + PUT** (`/scores.json`) = tüm cihaz ve kullanıcılar arasında
   "son yazan kazanır"; üstelik `exportLocalDataPayload` mantıksal anahtarı **tüm `user_*`
   önekleri arasında** tekilleştirdiği için baba'nın küçük kopyası Duru'nunki yerine yükleniyordu.
   Artık her kullanıcı **kendi düğümüne** yazar (`/scores_v2/<user>.json`) ve yalnız **kendi**
   öneki export edilir. Eski `/scores.json` yalnızca **okunur** (göç için).

4. **Push de tam-değiştirmeydi.** `pushToCloud` yereli olduğu gibi PUT ediyordu; fakir bir
   `localStorage` bulutu soyabiliyordu. 2026-09-21 09:00'da onarılmış `scores_v2/baba` düğümü
   tam böyle yeniden 95 XP / 1 madalyaya düştü — pull başarısız olsa bile push devam ediyordu.
   Artık push **önce okur, birleştirir, sonra yazar**; okuyamazsa veya merger yoksa **yazmaz**.

5. **`server.py → voeg_samen()` de aynı hatayı taşıyordu.** Sınav geçmişini birleştiriyor ama
   ilerleme anahtarlarında (xp/badges/pogingen) "son yazan kazanır" uyguluyordu — yani yerel
   sunucu yedeği de küçülebilirdi. Tam da kurtarmayı çıkardığımız dosya. Artık o da
   büyüyen-birleştirme yapıyor (`tools/test_server_merge.py`, 15 kontrol).

6. **Pull → push geri besleme döngüsü.** `pullFromCloud` her turda
   `duru_cloud_last_sync`'i yazıyordu; `setItem` override'ı bunu `duru_`ile başlayan
   bir anahtar görüp push tetikliyordu → pull → yine last_sync → … Açık her sekme,
   hiçbir şey değişmese bile 20 sn'de bir GET+PUT üretiyordu. Artık `NIET_SYNCEN`
   listesindeki anahtarlar ne push tetikler ne de buluta gider (liste
   `window.CloudSync.NIET_SYNCEN`'den paylaşılır) — yalnız gerçek sonuçlar senkronlanır.

**Tek merger, iki yön:** `js/landing.js → mergeScoreItems()` saf bir fonksiyon (hiçbir şey yazmaz),
`window.DURU_MERGE` olarak dışa açılır. `restoreScores()` onu yerel değeri de kaynak koyarak
okuma yönünde, `cloud_sync.js → pushToCloud` yazma yönünde kullanır. Yeni bir senkron yolu
eklerken bu fonksiyonu kullan — ikinci bir birleştirme mantığı yazma.

- **Regresyon testleri — senkron/merge koduna dokunan her değişiklikten sonra ikisini de çalıştır:**
  `node tools/test_score_merge.js` (20 kontrol, veli okuma yolu dahil; fonksiyonları `landing.js`'ten olduğu gibi kesip
  sahte `localStorage`'da çalıştırır) **ve** `python3 tools/test_server_merge.py` (15 kontrol).
  Onarım öncesi kodda ikisi de kırmızı.
- Kurtarma seti: `scores_rescue_20260920.json` (gitignore'da) — tarayıcı localStorage (duru+baba),
  4 Eylül sunucu anlık görüntüsü, Haziran v1 kütüğü ve bulutun **birleşimi**; 26 anahtar.
- **Ders notu:** yukarıdaki "v2" bölümü *sunucunun* birleştirdiğini söylüyordu ve bu doğruydu —
  ama istemci tarafı birleştirmiyordu. "Veri birleştirilir" yazan bir doküman, hangi katmanın
  birleştirdiğini söylemiyorsa yanlış güven verir.

## Git
`user.name=Mesut-Outlook`, `user.email=ozdemirmesut@gmail.com`. Commit-trailer:
`Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>`. Git backup amaçlı; commit/push sadece istenince.

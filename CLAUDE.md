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
tools/            soru kalite denetimi: gate.js (18 kontrol), spread.py, open_check.js (bkz. tools/README.md)
inbox/            ders materyali bırakma alanı (PDF/Word/görsel)
archief/<schooljaar>/  ARŞİV: ders yılına göre (ör. archief/2025-2026/ = MAVO 2 dersleri)
havo3/<vak>/      HAVO 3 ders-siteleri (12 vak). Anahtar: duru_2627_<slug>_*. Doluluk için CLAUDE.md "Ders doluluk durumu"
```

## Ders doluluk durumu (2026-09-23)
Sayılar `havo3/<vak>/js/{bootstrap,data/*}.js`'i node `vm`'de çalıştırıp `DURU.onderwerpen` /
`DURU.examens` ve `vragen` uzunluklarını sayarak çıkarılır (`tools/build_hoofdstukken.js` ile aynı
teknik). `kapsanan hoofdstuk` = `bootstrap.js`'teki `DURU.hoofdstukken`. İçerik eklendikçe güncelle.

| vak | onderwerp | proeftoets | soru | kapsanan hoofdstuk |
|---|---|---|---|---|
| geschiedenis | 30 | 30 | 840 | H1–H6 (tam) |
| frans | 33 | 86 | 2077 | H1–H8 **tam** (her Unité 4 onderwerp + 10 toets [U1: 5 onderwerp + 16 toets]) |
| duits | 24 | 36 | 924 | H1–H6 (tam: her H 4 onderwerp + 6 toets) |
| engels | 18 | 31 | 749 | H1–H6 (+1 hersteld smoke-test, "Overige") |
| natuurkunde | 44 | 60 | 1586 | H1–H8 **tam** (her H begrippen + begrippentoets; 5.5/6.5/7.5 plusstof) |
| economie | 12 | 37 | 836 | H1–H4 |
| aardrijkskunde | 25 | 40 | 1005 | H1–H5 (tam) (+1 hersteld smoke-test, "Overige") |
| scheikunde | 33 | 42 | 1150 | H1–H7 **tam** (her § onderwerp + toets, her H begrippen + begrippentoets) |
| wiskunde | 6 | 13 | 308 | H1 §1.1–1.2 (2 toets + begrippen, uit aantekeningen docent), H2 |
| biologie | 2 | 5 | 116 | H10 |
| maatschappijleer | 0 | 1 | 5 | **yok** — smoke-test |
| nederlands | 5 | 22 | 480 | Cursus 1 (H1: §1, §2, §4, §5) |

**Toplam: 232 onderwerp · 403 proeftoets · 10076 soru.** (Satırların toplamı; 2026-09-12'de
elle toplam iki kez bayat kaldı — tablo değişince toplamı yeniden say, üstüne ekleme.)
`maatschappijleer` `bootstrap.js`'te `DURU.hoofdstukken = []` tutar (Duru henüz
materyal vermedi), bu yüzden tek sınavı bilinçli olarak `hoofdstuk`'suzdur en manifest'e
girmez → "Overige toetsen"e düşer. **Buraya ünite numarası uydurma**; materyal gelince önce
`bootstrap.js`'e gerçek hoofdstuk'ları yaz.

Bekleyen üretim işleri `coordination.md` → "Pending Tasks" (TASK-15 frans U7–U8; TASK-19 ve TASK-09 materyal/cevap bekliyor).
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
- **Ders sitelerinde testler hoofdstuk altında gösterilir** (2026-09-12): hiçbir ders sayfasında
  hoofdstuk'suz düz test listesi kalmadı. duits/aardrijkskunde/biologie/scheikunde/wiskunde →
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

## Dashboard & istatistik
`index.html` iki view içerir ("Mijn vakken" / "Mijn prestaties & statistieken"). `js/dashboard.js`
**yıl-farkında**: ders/yıl kombinasyonları artık `js/vakken.js` → `DURU_VAKKEN`'den gelir
(`VAK_REGISTER` yalnızca ona bir referanstır). Yıl seçimi `localStorage.duru_dashboard_jaar`'da
kalıcı; `beschikbareJaren()` yalnız **verisi olan** yılları listeler, tek yıl varsa seçici gizlenir.
Veri katmanı (`loadDuruAttempts` / `loadBegrijpendLezenAttempts` / `safeReadJson`) ve
`renderScoreTimeline` korunur; görünüm için bkz. "Öğrenci ilerleme sayfası" (aşağıda).
2025-2026 (MAVO 2) anahtarları **yılsız ve donmuş** (`duru_nask_v1` …) — `DURU_VAKKEN`'de sabit
`jaar:'2025-2026'` ile etiketli, asla değiştirilmez.
Yeni yıllar `duru_<jaarcode>_<slug>_v1`/`_examens_v1` (jaarcode: `2026-2027→2627`).
Cijfer = `1 + pct/100*9` (geslaagd ≥ 5,5). **CSS/JS değişince `index.html`'de `style.css?v=`'i bump'la** (şu an `v=5.7`).

## Öğrenci ilerleme sayfası (`js/dashboard.js`) — 2026-09 yeniden tasarımı
"Mijn prestaties & statistieken" görünümü. Dil **Flamanca** (Duru'nun gördüğü her yer).
`index.html`'de `#statistieken-view` artık neredeyse boş: JS `#voortgang-paneel`'e render eder,
yalnız backup bloğu statik kalır (böylece `initBackupRestore()` düğmelerini kaybetmez).
Okuma sırası: **"Wat nu?" → cijferschaal → momentum → sekmeler**.
- **Veli panelinin kopyası DEĞİL.** Baba teşhis + yazdırılabilir rapor ister; Duru "şimdi ne
  yapmalıyım"ı ister. Bu yüzden en üstte, ölçekten bile önce, tek bir eylem durur.
- **`watNu()` önceliği**: düşen & zayıf → zayıf → düşen ama hâlâ yeterli → 8,5'e yakın → hiç
  başlanmamış → hepsi iyi. Düğme `openInIframe()` ile dersi hub'ın iframe-shell'inde açar.
- **⚠️ Aciliyet ömür-boyu ortalamayla DEĞİL, `recent` ile ölçülür** (son 3 deneme).
  8,2'den 4,6'ya düşen bir ünitenin ortalaması 6,4 kalır ve ortalamaya bakan mantıkta görünmez —
  oysa sayfadaki en acil şey odur. Kart üstünde ömür-boyu ortalama gösterilir, karar `recent`'tir.
- **Momentum**: `berekenStreak()` ardışık gün sayısı, bu hafta, 8,5 üstü ünite, açık proeftoets.
  Öğrenciye özgü; veli panelinde yok.
- Renk sözleşmesi ouder ile aynı desende: `--st-goed/net/zwak` + sıcak `--st-actie`,
  `#statistieken-view` üzerinde, `html.dark #statistieken-view`'de yeniden tanımlı.
- `renderScoreTimeline()` korundu, Overzicht sekmesine taşındı. Grafik kendi genişliğini ölçtüğü
  için **DOM'a eklendikten sonra** çağrılır.

## Veli paneli (`js/ouder_dashboard.js`) — sade tek sayfa (2026-09-22)
Sadece Baba görür (`#tab-ouder-btn` varsayılan gizli). Dil **Türkçe**, ders adları Flamanca.
Kullanıcı isteği: **"karışık olmasın, bakması ve anlaması kolay olsun — basit iyidir."**
Tek sayfa, dört blok (sekme yok): **özet** (büyük ortalama + tek cümle + bu hafta gün/deneme/son
çalışma) → **Dikkat edilecekler** (en fazla 3 ünite) → **Dersler** tablosu (ortalama · gidiş ·
yapılan sınav · son çalışma; derse tıkla → üniteler, üniteye tıkla → o ünitenin tek tek sınavları:
not · ad · tarih+saat) → **Son denemeler** (8 + "Tümünü göster", tarih+saat).
**Review (2026-09-22):** bir deneme satırına tıklayınca o sınavın soruları açılır — her soru için
doğru/kısmen/yanlış, Duru'nun cevabı, doğru cevap, açıklama; "Sadece yanlışları göster" filtresi,
"← Geri" aynı kaydırma konumuna döner. Salt-okunur: sorular `laadExamens(vakId)` ile
`havo3/<vak>/index.html`'deki `js/data/*.js` listesi fetch edilip sahte bir `DURU`
(`registerExamen` toplayan) içinde çalıştırılarak alınır — ders motoru yüklenmez, localStorage'a
yazılmaz. Cevap biçimi ders sitelerindeki `toonAntwoord/juisteAntwoord` ile aynı (12 motorda
birebir). Yalnız 2026-2027 (antwoorden/beoordelingen kaydı olan) denemeler tıklanabilir.
**⚠️ Tarih:** `"05-09-2026"` gibi metni asla `new Date()`'e verme — tarayıcı 9 Mayıs okur.
`ontleedDatum(s, ts)` ISO dışı metinde zaman damgasını kullanır (2026-09-22 düzeltmesi).
Yıl seçici kalır; geçmiş yılda "bu hafta" ve "dikkat" gizlenir. Veli sekmesi açıkken
`body.ouder-actief` → "Hoi Duru" hero'su gizli (`dashboard.js → initTabs`). Yazdır = `window.print()`
(`@media print` hub çerçevesini gizler). Kaldırılanlar: 1–10 cetveli, XP/rozet, 4 sekme,
25+ maddelik güçlü/zayıf listeleri — geri ekleme, önce kullanıcıya sor.
- **Kurallar Duru'nun sayfasıyla aynı:** "dikkat" = son 3 deneme < 5,5 veya ≥1 puan düşüş
  (ömür-boyu ortalama DEĞİL); gidiş = son 3 vs önceki 3 (±0,3); yapılan sınav = farklı `examId` /
  manifest (hub kartlarıyla aynı). İki panel aynı soruya farklı cevap vermemeli.
- **⚠️ Panel her zaman ÖĞRENCİYİ gösterir:** `getActiveStudent()` veli girişinde `"duru"` döner; veli
  cihazı `cloud_sync.js → haalLeerlingOp()` ile `/scores_v2/duru`'yu **yalnız okur**,
  `restoreScores(data, "duru")` ile `user_duru_*`'ya büyüyen-birleştirme yapar (push yok). 2026-09-22
  öncesi panel `user_baba_*`'yı, yani eski bir kopyayı okuyordu (206 poging / 7,0 vs gerçek 191 / 7,1).
- Veri katmanı `collectParentReportData(user, jaar)` değişmedi (dışa açık); render bundan türer.
- Stiller `css/style.css` sonunda `#ob` altında, kendi `--ob-*` token'ları + `html.dark #ob`.
  Anlam renkleri (goed/net/zwak) marka yeşilinden ayrı.

## Landing düzeni (HAVO 3 — sıcak, alan-gruplu)
"Mijn vakken" görünümü `js/landing.js`'te `renderVakken` ile kurulur. Aktif (HAVO 3) dersler
**vakgebied'e göre** gruplanır (`DOMEINEN`: talen / exact / mens) ve `maakVakKaartHavo3` ile sıcak
kartlar (`.havo3-*` stilleri, `css/style.css` sonunda, scoped + tema-güvenli) basılır. Arşiv
dersleri altta açılır "Archief — vorige schooljaren" bölümünde **yıla göre gruplu** (`renderArchief`,
eski kart stili). `VAKKEN` entry alanları: `id, titel, icoon, domein('talen'|'exact'|'mens'),
beschrijving, binnenkort?, href?, sleutel?, archief?, jaar?`.
**Kart = kapsama + not** (2026-09-22): sağ üst ve çubuk = `gedaan / totaal toetsen` (farklı `examId` /
manifest toplamı; manifestte olmayan yapılmış sınav iki tarafa da eklenir), alt = not ortalaması
(poging başına önce 1 ondalığa yuvarlanır — `dashboard.js` ile aynı). Eskiden çubuk "en iyi skorların
ortalaması"ydı: 30 sınavın 2'si yapılmış ders "%90" görünüyordu. `landingKaarten()` kartlara öneksiz
`vakId` verir (kart `id`'si `h3-` önekli) — manifest ve derin link bununla eşleşir.
**Derin link:** `./#vak=<vakId>` dersi iframe-shell'de açar. Her `havo3/<vak>/index.html` tek başına
(top-level) açılırsa buraya yönlenir — aksi halde `user_<naam>_` öneki yok, 0 XP görünür.
**Dil kullanıcıya göre:** Duru girişliyken üst çubuk/senkron metinleri Flamanca (`cloud_sync.js → t()`,
`NL` tablosu), veli girişliyken Türkçe. Öğrenci senkron hapına tıklayınca modal yerine doğrudan senkron.
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

## Ders sitelerinde koyu tema (2026-09-22)
Ders siteleri hub'ın temasını izler. **Tek yer, 12 kopya değil:**
- `js/vak_thema.js` — her `havo3/<vak>/index.html` `<head>`'inde (yönlendirme betiğinden hemen sonra)
  yüklenir. `localStorage.duru_hub_theme` ('light'/'dark', yoksa OS) → `<html class="dark">`;
  `storage` olayıyla hub'daki değişikliği anında izler. Ayrıca `<html data-vak="<klasör>">` koyar.
- `css/vak_dark.css` — her dersin kendi `css/style.css`'inden **sonra** yüklenir. 12 dersin ortak
  token'larını (`--wit/--inkt/--lijn/--paars/...`) `html.dark` altında yeniden tanımlar; mavi aile
  (engels, frans) `html.dark[data-vak=...]` ile ayrı ton alır. Sabit hex/rgba renkli seçiciler ve
  soru verisindeki satır içi stiller (nederlands leesteksten: `[style*="background:#f8fafc"]` …) burada ezilir.
  **Bir ders CSS'ine yeni sabit renk eklenirse koyu karşılığını buraya yaz**, dersin kendi dosyasına değil.
- `duru_hub_theme` artık **öneksiz** bir cihaz tercihi: `getPrefixedKey` ve diğer 3 sistem-anahtar
  listesinde muaf (önceden `user_<naam>_duru_hub_theme` olarak yazılıyordu, hub'ın `<head>` betiği
  ise öneksiz okuyordu). Eski değer `initTheme`'de bir kez taşınır.
- Doğrulama: 12 ders × (ana sayfa, sınav listesi, dashboard, madalyalar) koyu modda WCAG-benzeri
  kontrast taraması → 3:1 altı yazı yok (gradyanlı hero/başlıklar ayrıca gözle kontrol edildi).

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

## Çalıştırma & hosting
- **Yerel:** `Duru_Okul_Baslat.command` veya `python3 -m http.server 8125` → `http://localhost:8125/`.
  Ev ağı: `http://<mac-ip>:8125/`. UFW: `sudo ufw allow 8125/tcp`.
- **GitHub Pages:** `main`'e her push'ta GitHub Actions ile deploy. `.nojekyll` var; client tarafı
  bunu algılayıp `/api/score` senkronunu atlar.

## Git
`user.name=Mesut-Outlook`, `user.email=ozdemirmesut@gmail.com`. Commit-trailer:
`Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>`. Git backup amaçlı; commit/push sadece istenince.

# Coordination Log & Task Queue — Opus ↔ agy (Antigravity)

Bu dosya, planlayan (**Opus** — ben) ile üreten (**agy** = Google Antigravity) arasındaki
**tek iletişim kanalıdır**. Opus buraya görev + kabul kriteri yazar; agy ~15 dk'da bir yoklar,
işi yapar, sonucu ve durumu buraya geri yazar. Politika: `docs/PIPELINE.md`.

## Current Status
- **Last Checked**: 2026-09-04 (Opus — pano denetimi Faz 1-2-3 tamam; 8 bulgunun 8'i kapandı)
- **Status**: **ACTIVE** — "Okul yılı = birinci sınıf boyut" refactor'u başladı (Opus planladı, Duru onayladı).
  Kararlar: yıl storage-anahtarında (`duru_<jaarcode>_<slug>`, jaarcode=2526/2627); her yıl sıfırdan;
  legacy MAVO 2 anahtarları **TAŞINMAZ** → dashboard sabit KEY→YIL haritasıyla 2025-2026'ya etiketler;
  inbox da yıla göre. Sözleşme: `docs/ENGINE_SPEC.md` (güncellendi).
- **İş bölümü**: dashboard/index/css/landing kodu → **Sonnet-alt-agent** (Opus brief'iyle, arka planda).
  inbox yeniden yapılandırma → **agy** (TASK-05, aşağıda). İkisi çakışmaz (js/+css/+index.html vs inbox/).
- **2026-07-21 sonuç**: ✅ Okul-yılı refactor + inbox (TASK-05) + **10 HAVO 3 smoke-test dersi** (TASK-06) bitti.
  economie=Opus referans, 5 ders=Sonnet, 4 ders=agy. Hepsi node/serve/yapı doğrulandı, landing'de aktif, `?v=3.0`.
  **Sıradaki** (Duru materyal verince): her derse onderwerpen (oefenquiz) + daha çok proeftoets.
- **Schedule**: geschiedenis ✅ bitti (TASK-07). agy → TASK-08 (natuurkunde H5-H7, scheikunde H1/H3-H7
  + 4 kalite maddesi). TASK-09 (kalan 9 ders) materyal beklediği için BLOCKED.
- **Kalite kapısı**: `tools/gate.js` / `tools/spread.py` / `tools/open_check.js` — artık repoda,
  kurallar `docs/PIPELINE.md` → "Kalite kapısı". Her teslim buradan geçer.

## 2026-08-27 · Geschiedenis kalite denetimi (Opus) — ÖNEMLİ DERS
`havo3/geschiedenis` (commit e8c8a66, "840 soru") denetlendi. Bulgular:
1. **Paragraf yapısı uydurma** — H2–H6'daki 25 paragraf başlığının hiçbiri Geschiedeniswerkplaats
   3 HAVO ile eşleşmiyordu (kaynak `inbox/h2..h6_ocr.txt` elde olmasına rağmen kullanılmamış).
2. **133/240 oefen sorusu şablon dolgusu** — `scratch/generate_full_dataset.py:143-150`'deki 7 kalıp
   19 onderwerp'te tekrarlanmış ("Wat is het hoofdonderwerp van Paragraaf X.X?").
3. **30 proeftoetsin 25'i birebir kopya** — 5'er kopya hâlinde; 600 soru değil 200 benzersiz soru.
4. **Cevap anahtarı ele veriyor** — proeftoets 6–30'da 500 mc sorusunun 500'ünde doğru cevap A;
   waaronwaar 99 "Waar" / 8 "Onwaar". Bilmeden ~%95 alınabiliyordu.
5. **23 soru cevaplanamıyor** — sınavda `type:"invoer"` kullanılmış; `exams.js` bu tip için
   girdi alanı render etmiyor. → Opus düzeltti (`invul`).
**Kural (bundan sonra herkes için):** üretim şablonla değil, kaynak metin okunarak yapılır; kabul
kriterlerine "şablon soru yasak + dosya başına mc cevap dağılımı ≤%40 + waaronwaar ≥%35 onwaar +
sınavda invoer yasak" maddeleri eklenir. Denetim scripti: `tools/gate.js` (12 kural, bkz. `tools/README.md`).

## ⚠️ agy'YE: SORU ÜRETİM KURALLARI (2026-08-28 — HER ÜRETİMDE UYGULA)

Bu kurallar, `havo3/geschiedenis` (840 soru) ve `havo3/scheikunde` denetimlerinde çıkan gerçek
kusurlardan türetildi. **Her yeni soru dosyasında bunlara uy; üretimi bitirince kendin kontrol et.**

1. **Doğru şık hep A olmasın.** En ağır kusur buydu: geschiedenis'te 500 mc sorusunun 500'ünde,
   scheikunde'de 5 proeftoesin 4'ünde doğru cevap A idi. Duru hepsine A tıklayıp 20/20 alıyordu.
   **Kural: bir dosyadaki mc sorularının hiçbir şık pozisyonu %40'ı geçmesin.** A/B/C/D'yi
   sırayla kullan. (Mevcut dosyalar Opus'un `tools/spread.py` scriptiyle düzeltildi.)
2. **`waaronwaar` hep "Waar" olmasın.** geschiedenis'te 99 Waar / 8 Onwaar idi.
   **Kural: soruların en az %35'i `antwoord: false` olsun** — gerçekten yanlış ifadeler de yaz.
3. **Sınavda `type:"invoer"` KULLANMA.** `exams.js` sınav modunda yalnız `mc`, `waaronwaar`,
   `invul`, `open` render eder. `invoer` yazarsan **cevap kutusu hiç çizilmez**, soru
   cevaplanamaz ve otomatik yanlış sayılır (23 soru böyle bozulmuştu). Sınav = `invul`,
   oefenquiz = `invoer`. Tersi de geçerli: oefenquiz'de `invul`/`open` kullanma.
4. **Şablon soru yasak.** "Wat is het hoofdonderwerp van Paragraaf X.X?", "Welk historisch begrip
   staat centraal in…", "Hoe beoordelen historici…", "De bronnen in Geschiedeniswerkplaats…"
   gibi, konu adını boşluğa yapıştıran kalıplar üretme — bunlar hiçbir şey ölçmüyor
   (240 sorunun 133'ü böyleydi). Her soru somut bir olguyu sorsun: isim, yıl, kavram, sebep, sonuç.
5. **Proeftoetsleri kopyalama.** 30 proeftoesin 25'i birebir aynıydı (5'er kopya). Her proeftoets
   farklı sorular içermeli; aynı soru iki dosyada geçmesin.
6. **Kaynağı gerçekten oku.** geschiedenis'te 25 paragraf başlığı uydurulmuştu; kitapla
   (`inbox/h*_ocr.txt`) hiçbiri eşleşmiyordu. Paragraf numaraları/başlıkları **kaynaktan** alınır.
7. **`open` sorularda cevabı soruda verme.** `sleutelwoorden` içindeki kelime soru metninde
   geçiyorsa öğrenci kopyalayıp yapıştırır.
8. **Her soruda dolu `uitleg`.** Yalnız "Waar." yeterli değil — neden doğru olduğunu bir cümleyle yaz.
9. **Soru metnine numara koyma.** Arayüz zaten "Vraag 3 van 20" yazıyor; `vraag: "3. ..."` çift numara üretir.
10. **Teslimden önce `node --check`.** Aşağıdaki hata bunun atlandığını gösteriyor.
11. **`open` sorularda `sleutelwoorden` = KISA ANAHTAR, cümle değil.** Motor (`exams.js:269`)
    `tekst.indexOf(alternatif)` ile **birebir alt-dizi** arar. `"1200 -> 600 -> 300 -> 150"` ya da
    `"koper is te zwaar en te duur voor lange overspanningen"` gibi 6–12 kelimelik bir anahtar,
    öğrencinin o cümleyi kelimesi kelimesine yazmasını şart koşar → doğru cevap bile **0 puan** alır.
    Kural: her `sleutelwoord` **1–3 kelimelik** bir terim olsun (`"kernafval"`, `"turbine"`,
    `"geen CO2"`), alternatifleri `/` ile ver (`"kernafval/radioactief afval"`). Uzun açıklama
    `modelantwoord`'a yazılır, `sleutelwoorden`'e değil. Ayrıca **`minTreffers` ≤ sleutelwoord sayısı**
    olmalı (aksi hâlde soru asla "goed" olamaz) ve anahtara `"voordeel:"` gibi önek koyma.
    **İnce nokta (2026-08-28 · uzun anahtarları kısaltırken bunu kaçırdın):** eşleştirme
    alternatifler arasında **VEYA**'dır. Soruda zaten geçen bir terimi alternatiflerden biri
    yaparsan, öğrenci soruyu kopyalayınca puan alır. Örn. soru "…(Dalton, Thomson, Rutherford,
    Bohr)" diyorsa `"Dalton/massief/bol"` anahtarı işe yaramaz — `"massief/ondeelbaar/bol"` yaz,
    yani **ismi değil, o modelin ayırt edici özelliğini** anahtar yap. Aynısı `ex-h3-natuurkunde-11#19`
    için geçerli: `"radiogolven"` ve `"röntgen/gammastraling"` soruda listelenmiş durumda; onların
    yerine `"langste golflengte"`, `"meest energierijk/ioniserend"` gibi gerekçe anahtarları koy.
    Denetim: `node tools/gate.js <vak>` → 8. kural.

**Kendi kendini denetleme:** `node tools/gate.js <vak>` bu kuralları ölçer. Opus her teslimi bu kapıdan geçiriyor; sen de geçir ki iş geri dönmesin.

### 🔴 agy — TEKRARLAYAN HATA: çok satırlı string (2026-08-28)
**Aynı hatayı üçüncü kez yaptın.** JS'te çift tırnaklı string **gerçek satır sonu içeremez**.
`modelantwoord`/`uitleg` alanına maddeli liste yazarken satır sonu bırakınca dosya söz dizimi
hatası veriyor ve o dosyadaki hiçbir soru yüklenmiyor.
- 10:54'te `natuurkunde/examen_21..25` (sen düzelttin ✅)
- 11:19'da `economie/js/data/examen_1.js` — **Opus düzeltti**. Bu ders `havo3/economie/` idi:
  TASK-06'da "referans, salt-oku" denmişti. Genişletmen iyi oldu ama **bozuk bıraktın** ve ders
  tamamen çalışmaz hâldeydi.
**Çözüm:** satır sonu gerekiyorsa `\n` kaçışı kullan (`"1. ...\n2. ..."`) ya da backtick
template string'e geç. **Her dosyada `node --check`** çalıştırmadan commit etme.

### 🔴 agy — ACİL: 5 bozuk dosya (2026-08-28 10:54)
`havo3/natuurkunde/js/data/examen_21.js`, `examen_22.js`, `examen_23.js`, `examen_24.js`,
`examen_25.js` **söz dizimi hatalı** — `modelantwoord` alanında çift tırnaklı string içinde
gerçek satır sonu var (JS'te string satır sonu içeremez). `node --check` beşinde de patlıyor;
bu hâliyle sayfa yüklenirse o dosyalardan sonraki hiçbir script çalışmaz.
**Düzelt:** çok satırlı metni tek satıra indir (`\n` yerine boşluk) ya da backtick (`` ` ``)
template string kullan. Ayrıca `examen_23.js`'te bozuk LaTeX kalıntısı var:
`({\text{spier}} = F_{\text{last}} / n$)` — düz metne çevir (`F_spier = F_last / n`).
Düzelttikten sonra **beşinde de `node --check`** çalıştır.

## Görev şeması (her görev böyle yazılır)
```
### TASK-<id> · <başlık>  [status: TODO | IN_PROGRESS | REVIEW | DONE | BLOCKED]
- **Atanan**: agy (Antigravity) | Sonnet-alt-agent | Opus
- **Amaç**: tek cümle.
- **Girdi**: kaynak dosya(lar) / inbox yolu / kapsam.
- **Çıktı**: yazılacak dosya(lar) + tam yol.
- **Kabul kriterleri**: madde madde (sözleşme=docs/ENGINE_SPEC.md, id kararlı, node-doğrulaması
  geçti, index.html'e bağlandı, ilgili MEMORY.md güncellendi).
- **agy notu**: (agy buraya sonucu/sorunu yazar)
```
Durum döngüsü: Opus `TODO` → agy `IN_PROGRESS` → biter `REVIEW` → Opus doğrular `DONE`.
Takıldıysa agy `BLOCKED` + neden yazar. **agy'ye yalnızca "Atanan: agy" olan görevler aittir.**

## 2026-09-02 · Hoofdstuk-kırılımı denetimi (Opus) — agy'nin teslimi düzeltildi

agy'nin "ders + hoofdstuk bazlı gruplama" teslimi denetlendi. Görsel katman iyiydi, **veri katmanı yanlıştı**:
1. **Uydurma ünite metadata** — `js/dashboard.js` ve `js/ouder_dashboard.js` içine elle yazılmış
   **iki kopya** `HOOFDSTUK_REGISTRY`; 12 dersin 8'inde gerçek `DURU.hoofdstukken` ile uyuşmuyordu
   (wiskunde H2↔"H1 Lineaire Formules", biologie H10↔"H1 Organen & Cellen", frans 8↔2 hoofdstuk,
   natuurkunde H1-4+H8↔tek hoofdstuk, aardrijkskunde/economie/scheikunde/engels benzeri).
   CLAUDE.md'nin "çapraz-referanssız tek kaynak" kuralı da çiğnenmişti.
2. **5 derste sınavlarda `hoofdstuk` alanı yoktu** → `ex.hoofdstuk || 1` ile hepsi H1'e yazılıyordu
   (natuurkunde 25 sınav, scheikunde 10, biologie 5, nederlands 1, maatschappijleer 1).
3. **`ex.hoofdstukTitel` hiç yoktu** → kaydedilen her başlık jenerik "Hoofdstuk N".
4. **Fallback tahmini** `floor((n-1)/5)+1` → natuurkunde H8 sınavları "H5" görünüyordu;
   `ex-h3-sch-h1-N` ve `ex12_v1` hiç eşleşmiyordu.
5. **Oefen→hoofdstuk regex'i** `/h(\d+)_/` gerçek id'leri (`ak-h1-2`, `sch-h1-3-…`, `bio-h10-1-…`)
   yakalamıyordu → ünite bazında oefen ilerlemesi tamamen boştu.
6. **`maxExams: 5` sabiti** → economie'de ünite başına 3 sınav var, "x/5" yanlıştı.
7. **Dil kuralı ihlali** — öğrenci ekranlarında Türkçe metin ("Ünite Başarı Karnesi", "Tekrar Gerekli",
   "Henüz sınav çözülmedi"). Öğrenci-içeriği Flamanca olmak zorunda.

**Düzeltme:** manifest mimarisi (`tools/build_hoofdstukken.js` → `js/hoofdstukken.js` →
`js/hoofdstuk_util.js` / `window.DURU_HF`). Ayrıntı: kök `CLAUDE.md` → "Hoofdstuk (ünite) verisi"
ve `MEMORY.md` → Milestone 20.

### ⚠️ agy'YE YENİ KURAL: `ex-h3-<vak>-N` id'sindeki `h3` HOOFDSTUK DEĞİL, NIVEAU'dur (HAVO 3)
Sınav id'sinden hoofdstuk çıkaran regex yazma; hoofdstuk'suz her kayıt sahte olarak "H3"e düşer.
Hoofdstuk **veriden** gelir: `registerExamen({...})` içinde `hoofdstuk` alanı **zorunlu**.
Ünite listesi/sayıları hiçbir yere elle yazılmaz — `node tools/build_hoofdstukken.js` çalıştırılır,
`--check` bayat manifest'i yakalar. UI metni öğrenci tarafında **Flamanca**, veli sayfasında Türkçe.

### TASK-11 · frans kalite kapısı: 5 madde kaldı  [status: TODO]
- **Atanan**: agy (Antigravity)
- **Durum**: `node tools/gate.js frans` → **7/12** (2026-09-03, mevcut 40 sınav üzerinde).
  Kalanlar: 1 şablon soru · 2 tekrar eden soru · `waaronwaar` %35 onwaar barajı ·
  **26 soruda `uitleg` boş** · 15 soruda yapı sözleşmeye uymuyor (`docs/ENGINE_SPEC.md`).
- **Not**: `nederlands` (9/12) ve `maatschappijleer` (10/12) hâlâ smoke-test (5 soruluk tek sınav);
  kural 9 "proeftoets = 20" oradan geliyor — materyal gelmeden düzeltilmez, TASK-09 kapsamında.
- **Kabul**: `node tools/gate.js frans` → 12/12, her dosyada `node --check`.

### TASK-10 · scheikunde H1 sınavlarında cevaplanamayan sorular  [status: DONE — Opus, 2026-09-03]
- **Atanan**: Opus (agy'ye gitmeden çözüldü)
- **Sonuç**: 16 `invoer` sorusu `invul`'e çevrildi (oefenquiz'lerdeki `invoer` bilinçli olarak korundu).
  5 sınav dosyasının tamamı **%100 A** idi (`{"0":16}`, `{"0":13}`, `{"0":18}`, `{"0":14}`, `{"0":13}`)
  — mc doğru şıkları A/B/C/D döngüsüne dağıtıldı (genel dağılım artık 41/37/35/26).
  `sch-h1-3-faseveranderingen` (5/6 aynı şık) de düzeltildi. Tekrar eden soru
  (`sch-h1-1-stofeigenschappen#7` ↔ `ex-h3-sch-h1-1#12`) sınav tarafında yeni bir soruyla değiştirildi
  (dichtheid = stofeigenschap, hoeveelheden bağımsız). `node tools/gate.js scheikunde` → **11/12**.
- **Açık kalan tek madde (bilinçli):** kural 9, onderwerp başına **tam 8** soru istiyor;
  `sch-h1-1-stofeigenschappen` ve `sch-h1-3-faseveranderingen` 10'ar iyi soru içeriyor. İki iyi
  alıştırma sorusunu yalnızca sayı tutsun diye silmek Duru'nun aleyhine olduğu için silinmedi.
  Karar Duru'nun babasında: ya bu iki dosya 8'e indirilir, ya `tools/gate.js:70` kuralı onderwerp
  için "**en az** 8" (`length < 8`) hâline getirilir.
- **Eski görev tanımı (referans)**: agy (Antigravity)
- **Sorun**: `node tools/gate.js scheikunde` → **5a kuralı: sınavda `invoer` 16 ihlal**.
  Etkilenen dosyalar: `examen_h1_2.js` (5), `examen_h1_4.js` (5), `examen_h1_5.js` (6).
  Sınav modunda `invoer` için girdi kutusu çizilmiyor → 16 soru cevaplanamıyor, otomatik yanlış.
- **Yapılacak**: bu 16 soruyu `invul`'e çevir (sözleşme: `docs/ENGINE_SPEC.md`; kural 3, yukarıda).
  Ayrıca aynı derste kapıda kalan diğer 3 madde: tekrar eden soru (1), mc şık dağılımı (6 dosya),
  soru sayısı (2 dosya).
- **Kabul**: `node tools/gate.js scheikunde` → 12/12; `node --check` her dosyada;
  `node tools/build_hoofdstukken.js` yeniden çalıştırılıp manifest güncel bırakıldı.

## 2026-09-03 · Veli paneli yeniden tasarlandı (Opus)

Duru'nun babası için olan panel (`#ouder-view`) baştan tasarlandı. Tasarım **önce önizleme olarak
onaya sunuldu**, onay sonrası production'a port edildi.

- **Dokunulan**: `js/ouder_dashboard.js` (yalnız render katmanı), `css/style.css` (`.ouder-*` bloğu
  tamamen yenilendi, -493 satır), `index.html` (`?v=3.8` → `?v=3.9`), `CLAUDE.md`, `MEMORY.md`.
- **DOKUNULMADI**: `collectParentReportData` + `VAK_CONFIG` — manifest entegrasyonu ve iki-yıl
  desteği zaten doğruydu. Öğrenci tarafı (`dashboard.js`, `landing.js`, `havo3/**`) hiç değişmedi.
- **Yeni okuma sırası**: durum cümlesi → cijferschaal (Hollanda 1–10 ölçeği, 5,5 eşiği işaretli)
  → "Önce buraya bakın" (5,5 altı hoofdstuk'lar) → ders listesi. Detaylar 4 sekmede
  (`overzicht`/`vakken`/`units`/`logboek`), yalnız aktif olan HTML'e basılır.
- **⚠️ agy'YE RENK KURALI**: veli panelinde anlam renkleri marka yeşilinden **ayrıdır**.
  `--ouder-goed/net/zwak` (+ `-zacht`) `#ouder-view` üzerinde, `html.dark #ouder-view`'de yeniden
  tanımlı. Yeşil = "iyi" demek, marka rengi değil. Yeni durum rengi eklerken bu ikisini karıştırma.
- **Doğrulama**: `node --check` temiz; headless DOM-stub harness ile gerçek veri render edildi
  (genel ortalama 6,6 = elle hesapla birebir), dört görünüm de `undefined`/`NaN` üretmedi,
  verisi olmayan yıl boş-durum metnine düştü.

### ✅ `js/hoofdstukken.js` bayatlığı  [status: DONE — Opus, 2026-09-03]
`--check` exit 1 veriyordu. Yeniden üretildi (`node tools/build_hoofdstukken.js`) → **exit 0**.
**Kaçan veri**: 6 economie sınavı (`ex-h3-economie-13..18`) manifest'te yoktu →
economie H1 `3 → 6`, H4 `3 → 6` sınav. Başka hiçbir ders etkilenmedi; diff 10 satır.
Bu sınavlar dashboard'larda "Overige toetsen"e düşüyordu, artık doğru üniteye yazılıyor.

**2 uyarı kasıtlı, düzeltilmedi**: `maatschappijleer` + `nederlands` `bootstrap.js`'te
`DURU.hoofdstukken = []` tutuyor (Duru henüz materyal vermedi). Tek smoke-test sınavlarına ünite
numarası vermek **uydurma metadata** olurdu — projenin yasakladığı şey. Alan boş kaldı, sınavlar
"Overige toetsen"e düşüyor. Materyal gelince önce `bootstrap.js`'e gerçek hoofdstuk'lar yazılacak.

### ✅ Bayat dokümanlar düzeltildi  [status: DONE — Opus, 2026-09-03]
- **`CLAUDE.md` doluluk tablosu** ciddi bayattı: `engels`/`frans`/`duits` hâlâ "smoke-test 0/1/5"
  yazıyordu ama sırasıyla **30/30/40 proeftoets**'leri var. `economie` "0/1/20" yazıyordu, gerçek
  **12/18/456**. Tablo baştan sayıldı: **toplam 126 onderwerp · 205 proeftoets · 5082 soru**.
  (Sayım yöntemi doğrulandı: geschiedenis 840 çıktı, eski tablodaki değerle birebir.)
- **`docs/ENGINE_SPEC.md` — Sözleşme 2'de `hoofdstuk` alanı hiç yazmıyordu.** CLAUDE.md zorunlu
  diyor, manifest hattı tamamen buna dayanıyor, ama "tek doğru kaynak" olan spec'te yoktu.
  Eklendi + `ex-h3-*` niveau tuzağı ve "ünite uydurma" kuralı spec'e yazıldı.
  **agy: yeni sınav yazarken bu bloğa bak.**

## 2026-09-04 · Faz 3 optimizasyonu uygulandı (Opus) — pano denetimi tamam

### ✅ 1 · Rapor önbelleği + kısmi yeniden çizim  [status: DONE]
`collectParentReportData` (12 vak × hoofdstuk × poging) sekme değişiminde, yıl değişiminde ve
20 sn'lik senkronda baştan koşuyordu. Artık `haalContext()` bir **imza** tutuyor: ham string'lerin
uzunluğu + ilk/son 48 karakteri. Parse YOK — pahalı olan zaten parse + toplama.
`wisselView()` sekme değişiminde yalnız `.ouder-views` içeriğini değiştiriyor; statusband ve
cijferschaal yerinde kalıyor. `bindParentEvents` ikiye ayrıldı: `bindKopEvents` (yıl/tab/print,
`.ouder-views` dışında, tam render başına bir kez) + `bindViewEvents` (her view değişiminde).

### ✅ 2 · Sparkline + trend  [status: DONE]
Cijferschaal *nerede* olduğunu gösteriyordu, *nereye gittiğini* değil: 4,6→5,5 çıkan ünite ile
7,0→5,5 düşen ünite panelde birebir aynı görünüyordu. Eklendi:
- Ders satırında **son 8 denemenin sparkline'ı** (62×18 inline SVG, kütüphane yok, 5,5 eşiği kesik
  çizgi, son nokta vurgulu, `role="img"` + `aria-label`).
- **Trend oku** ▲/▼: son 3 deneme ortalaması ile önceki 3'ünkü arasındaki fark.
  4 denemeden az → hüküm yok (bir sınav trend değildir); 0,3 puandan az fark → düz.
- **"Önce buraya bakın" sıralaması değişti**: düşüş trendindeki ünite, uzun süredir sabit-düşük
  olandan önce geliyor + `düşüyor` rozeti. Wegzakken urgenter dan stabiel laag.

### ✅ 3 · Onderwerp'siz derste alıştırma çubuğu  [status: DONE]
Veli panelinde frans "Alıştırma —" gösteriyordu (0 onderwerp, 40 sınav) — olmayan bir açığı ima
ediyordu. Artık satır tamamen gizleniyor. **Öğrenci panosunda bu zaten doğruydu**
(`if (oefTotaal > 0)`), orada değişiklik yapılmadı.

**Doğrulama** (`/tmp/faz3_test.js`): en kritik test **önbellek geçersizleştirme** — yeni poging
eklenince ortalama değişti (bayat önbellek olsaydı yakalanırdı). Ayrıca sparkline path/eşik/
erişilebilirlik, trend rozeti, gizlenen alıştırma satırı, `undefined`/`NaN` yok.
`index.html` → `?v=4.1`.

**Not:** üç test harness'ının DOM stub'ları genişletildi (`querySelector`, `setAttribute`,
`addEventListener`) — kod hatası değil, stub eksikliğiydi; üçü de gerçek DOM'da zaten vardı.

## 2026-09-04 · Faz 2 optimizasyonu uygulandı (Opus)

Üç maddenin hepsi bitti. **Davranış değişmedi** — regresyon testi eski (HEAD) değerlerle
karşılaştırarak doğruladı.

### ✅ 1 · Çok-kullanıcı veri sızıntısı kapatıldı  [status: DONE]
`dashboard.js → safeReadJson` ve `ouder_dashboard.js → readStorageKey` son çare olarak tüm
localStorage'ı **substring** ile tarıyordu (`k.indexOf(logicalKey) !== -1`) → `duru_2627_engels_v1`
ararken `user_baba_duru_2627_engels_v1` de eşleşiyordu.
Artık kesin ve sıralı: `user_<kişi>_<key>` → `<key>` → `null`. Tarama tamamen kaldırıldı.
**Ek bulgu:** veli panelinde ilk deneme `localStorage.getItem(key)` idi — bu, landing.js'in
override'ı yüzünden **AKTİF kullanıcıyla** öneklenir. Baba bakarken rapor Duru hakkında olduğu
için bu yanlıştı. Yeni `leesRuw()` `originalGetItem` ile ham okuyor, kişiyi açıkça adresliyor.

### ✅ 2 · `js/vakken.js` — tek ders kaynağı  [status: DONE]
`VAK_REGISTER` (dashboard) ve `VAK_CONFIG` (ouder) kelimesi kelimesine aynıydı; landing de aynı
12 dersi üçüncü kez tekrarlıyordu. Hepsi `window.DURU_VAKKEN`'den türüyor
(`alle` / `vanJaar` / `zoek` / `landingKaarten`). dashboard −11 satır, landing'den 12 kart tanımı
kalktı, ouder'dan 22 satır. **Arşiv dersleri landing'de kaldı** — iç içe `onderwerpen` taşıyan
saf navigasyon, istatistik kaydında karşılığı yok, zorla birleştirmek yanlış olurdu.
**Bilerek yapılan tek değişiklik:** HAVO 3 economie ikonu `🏛️` → `💶`. Panolarda economie ve
maatschappijleer aynı ikonu paylaşıyordu; landing zaten ayırıyordu, ayırt eden kazandı.

### ✅ 3 · `js/cijfer_util.js` — tek not mantığı  [status: DONE]
`1 + pct/100*9` ve `>= 5.5` iki panoda ~20 yerdeydi (renk, rozet, tavsiye, filtre, grafik ızgarası).
Artık `DURU_CIJFER`. **Renk paylaşılmıyor** — her panonun tokenı farklı; ortak olan sınıflandırma.
Kalan ham eşik: **0**.

**Yükleme sırası (`index.html`)**: `vakken.js` → `cijfer_util.js` → `hoofdstukken.js` →
`hoofdstuk_util.js` → `landing.js` → `dashboard.js` → `ouder_dashboard.js` → `cloud_sync.js`.
`ouder_dashboard.js` `DURU_CIJFER`'i yüklenme anında okuyor, sıra önemli.

**Doğrulama** (`/tmp/faz2_test.js`): 18 satır birebir · tüm alanlar aynı ·
**tüm storage anahtarları byte-byte aynı** (Duru'nun geçmişi güvende) · 12 landing kartının
href/sleutel/id/domein'i eski landing.js ile eşleşiyor · cijfer formülü 7 yüzdede eski davranışla
aynı · klasse/geslaagd/tekst/positie doğru.

## 2026-09-04 · Faz 1 optimizasyonu uygulandı (Opus)

Pano denetiminin (artifact) Faz 1'i bitti. Üç madde.

### ✅ 1 · Veli panelinde yazdırma onarıldı  [status: DONE]
**Benim 2026-09-03 regresyonum.** Yeniden tasarım hız için yalnız aktif sekmeyi DOM'a basıyordu;
tarayıcı da yalnız DOM'dakini yazdırır → "Yazdır / PDF" sadece açık sekmeyi veriyordu.
Çözüm: `beforeprint`'te dört bölüm de basılıyor (`toonVolledigRapport`), `afterprint`'te panel
yeniden çiziliyor. Ctrl+P de çalışır. Düğme artık "Tam raporu yazdır".
`viewVakken`'den `vakDetailHtml(vak, metGeschiedenis)` ayrıştırıldı — rapor tüm dersleri basar,
sınav geçmişini atlar (günlük bölümü zaten her pogingi listeliyor).

### ✅ 2 · scores.json anlık-görüntü kütüğü kaldırıldı  [status: DONE]
`server.py` v2'ye geçti: anahtar-bazlı sözlük + `history` birleştirme + `events.jsonl`.
**27,3 MB → 0,58 MB, 287 benzersiz poging, sıfır kayıp** (doğrulama script'i ile anahtar başına
karşılaştırıldı). v1 otomatik göç ediyor, önce backup yazılıyor. `GET /api/score` hâlâ liste
döndüğü için `restoreScores()` değişmedi. Uçtan uca test: aynı POST 5 kez → dosya büyümedi.

### ✅ 3 · POST debounce  [status: DONE]
`js/landing.js → queueScoreSync()`: anahtar başına 2 sn sessizlik sonrası gönderim.
Sınav başına ~20 POST → 1. `pagehide`/`visibilitychange`'de `sendBeacon` ile flush.

**Yan bulgu, düzeltildi:** günlük boşken "Bu filtrelerle eşleşen deneme yok" diyordu — veri hiç
yokken bu yanlış sebep. Artık "Bu dönemde henüz çözülmüş bir sınav yok."

**⚠️ agy'ye not:** `server.py` artık v2 sözlük yazıyor. Skor dosyasına dokunan script yazarsan
listeyi değil `keys` sözlüğünü oku; ya da `GET /api/score`'u kullan (liste döner).

`index.html` → `?v=4.0`.

## 2026-09-04 · agy teslimi denetlendi: economie H4 · 5 yeni proeftoets (Opus)

agy `240f6f3` ile **examen_19–23** (5 sınav, 100 soru, H4.1/4.2 · Pincode 7e editie) + üreteç
script'i `tools/generate_h4_more_exams.py` teslim etti. Denetim sonucu: **içerik kalitesi iyi**,
iki süreç hatası var.

**✅ Geçenler**
- `node tools/gate.js economie` → **12/12** (23 proeftoets · 556 vraag).
- **`hoofdstuk: 4` beş dosyada da var** — 2026-09-03'te `ENGINE_SPEC.md`'ye yazdığım zorunlu alan
  kuralı uygulanmış. Bu daha önce atlanan alandı.
- Yapı sözleşmeye tam uyuyor: her sınav **12 mc / 4 waaronwaar / 2 invul / 2 open**.
- mc cevap dağılımı her dosyada **3-3-3-3 (%25)** — A-yığılması yok.
- Konu kapsamı doğru: 4.1 = productieproces/kringloop/bedrijfskolom/KANO-productiefactoren,
  4.2 = constante-variabele kosten/kostprijs/inkoopwaarde/afschrijvingen. Kapsam kayması yok.
- Yakın-kopya taraması (Jaccard ≥0,60, 460 soru çifti): yeni sınavları ilgilendiren **tek** çift.

**⚠️ Düzelttiğim iki şey**
1. **Manifest yeniden üretilmemişti** — `--check` exit 1. economie H4 `6` sınav gösteriyordu,
   gerçek `11`. Her iki panoda da canlı yanlış sayı. `node tools/build_hoofdstukken.js` çalıştırıldı
   → exit 0. **agy: veri eklediğinde bu komut teslimin parçasıdır**, ayrı bir iş değil.
2. **Almanca sızıntı**: `examen_20` başlığında `Amortisationsanalyse` → `Afschrijvingsanalyse`.
   Üreteç script'inde de düzeltildi (yoksa yeniden üretimde geri gelirdi). Sınav hiç çözülmemişti
   (skor geçmişi 0), başlık değişimi güvenliydi.

**⚠️ Kalan küçük madde (düzeltilmedi)**
`ex-h3-economie-19` ile `ex-h3-economie-10` arasında %60 benzerlik: "Wat is de beloning voor de
productiefactor arbeid" ≈ "Wat is de beloning die hoort bij de productiefactor arbeid". Aynı soru.
agy: yeni sınav üretirken **mevcut sınavlardaki soruları da tara**, sadece dosya içi tekrar yetmez.

**⚠️ SÜREÇ: agy `coordination.md`'ye geri yazmadı.** Politika `docs/PIPELINE.md`: iş çekilir,
yapılır, **sonuç buraya yazılır**. Bu kaydı ben tuttum. agy: teslimden sonra buraya durum + gate
çıktısı + manifest komutunun çalıştırıldığı yazılmalı.

### ⚠️ agy'YE AÇIK İŞ · `frans` onderwerp'siz  [status: TODO]
`frans` 40 proeftoets'e sahip ama **0 onderwerp** (oefenquiz) var — 12 ders içinde tek böyle ders.
`aantalOnderwerpen={}` olduğu için veli/öğrenci panosunda "oefenvoortgang" hep %0 görünür.
H1–H8 için onderwerp üretilmeli (bkz. TASK-11 kalite maddeleriyle birlikte).

## Pending Tasks
*(agy: yalnızca "Atanan: agy" görevlerini al.)*

### TASK-09 · Kalan derslerin içeriği (Duru materyal verdikçe)  [status: BLOCKED — materyal bekleniyor]
- **Atanan**: (henüz atanmadı — materyal gelince Opus dağıtır)
- **Durum tablosu**: kök `CLAUDE.md` → "Ders doluluk durumu".
- **economie** — `examen_1.js` H4 §4.1 üzerine 20 soruya genişletildi (agy, 2026-08-28; Opus söz
  dizimini onardı + şık dağıtımını düzeltti, kapı 12/12). Ama **onderwerp (oefenquiz) hiç yok** ve
  H4'ün diğer paragrafları eksik. Kaynak materyal gerekiyor.
- **wiskunde** — yalnız H2 Statistiek (5 onderwerp + 5 proeftoets). Diğer hoofdstukken için kaynak yok.
- **Smoke-test'te duran 7 ders** (her biri 1 proeftoets / 5 soru, onderwerp yok):
  `biologie`, `aardrijkskunde`, `maatschappijleer`, `nederlands`, `engels`, `frans`, `duits`.
  Bunlar için `inbox/2026-2027/<vak>/` altına materyal bırakılmadı — **Duru'dan kitap/PDF gelmeden
  üretim yapılmaz** (uydurma içerik yasağı: geschiedenis dersi).
- **Not**: `duits` ve `scheikunde` bir ara "pakkette yok" diye işaretlenmişti (TASK-05); artık
  ikisi de aktif. Pakket değişirse `js/landing.js` → `VAKKEN` ve `js/dashboard.js` → `VAK_REGISTER`
  birlikte güncellenir.

### TASK-08 · Natuurkunde & Scheikunde: eksik bölümler + kalite  [status: TODO]
- **Atanan**: agy (Antigravity)
- **Durum**: natuurkunde H1, H2, H3, H4, **H8** bitti (25 onderwerp + 25 proeftoets, kapı denetiminden
  geçti). scheikunde yalnız **H2** bitti (4 onderwerp + 5 proeftoets). Şık dağıtımı Opus tarafından
  düzeltildi (`spread.py`) — **o düzeltmeleri bozma**, yeni dosyalarda baştan dengeli üret.
- **A · Eksik bölümler** (kaynak PDF'ler `~/Downloads/Eğitim/Duru/Natuurkunde/` altında):
  - natuurkunde: **H5 Licht**, **H6 Zonnestelsel en heelal**, **H7 Energie en duurzaamheid**
  - scheikunde: **H1 Scheikunde is overal**, **H3 Chemische reacties**, **H4 Reacties en energie**,
    **H5 Mengsels**, **H6 Indeling van stoffen**, **H7 Koolstofchemie**
  - Her bölüm için: kitabın **gerçek paragraf sayısı kadar** onderwerp + o kadar proeftoets.
    Paragraf numarası/başlığı **OCR'dan** alınacak, uydurulmayacak (geschiedenis'te 25 başlık
    uydurulmuştu, hepsi baştan yazılmak zorunda kaldı).
- **B · Mevcut içerikte düzeltilecek kalite sorunları**:
  1. **`waaronwaar` dengesi** — natuurkunde 26/145 (%18), scheikunde 4/20 (%20) "onwaar".
     Hedef **≥%35**. "Hep Waar de geç" stratejisi şu an %80 getiriyor. Yeni/mevcut sorularda
     gerçekten yanlış ifadeler de yaz.
  2. **theorie çok ince** — natuurkunde 553–914 karakter, scheikunde 485–726 karakter.
     Geschiedenis'te ölçü **≥1500 karakter** (orada 2764–4641 oldu). Duru bu sayfadan çalışacak;
     tanım + örnek + formül kutusu içerecek kadar doldur.
  3. **onderwerp başına soru sayısı** 6–7; hedef **8**.
  4. **`open` sorularda anahtar-cümle sorunu (ACİL — 15 soru)** — yukarıdaki 11. kural. Etkilenen:
     natuurkunde `ex-h3-natuurkunde-8#20, 9#19, 9#20, 12#20, 17#19, 17#20, 19#19, 19#20, 20#20,
     21#19, 22#20, 23#19, 23#20, 24#19, 24#20, 25#19`; scheikunde `ex-h3-scheikunde-1#20, 4#20, 5#20`.
     Bu sorular şu an doğru cevaplansa bile 0 puan veriyor. `sleutelwoorden`'i kısa terimlere indir,
     soru metnine ve `modelantwoord`'a dokunma. (`ex-h3-natuurkunde-15#20`'yi Opus düzeltti — örnek al. Tarama: `node tools/open_check.js`.)
  5. **`open` anahtar sızıntısı (2026-08-28 · madde 4'ü yaparken oluştu)** — uzun anahtarları
     kısaltırken soruda geçen terimleri alternatif yaptın; şimdi 16 soruda öğrenci soruyu
     kopyalayarak puan alabiliyor. Kural 11'in "ince nokta" kısmına bak. Etkilenen:
     natuurkunde `ex-11#19, 16#19, 16#20, 22#19, 22#20` (+2), scheikunde `ex-1#19, 1#20, 4#20` (+2).
     Tam liste: `node tools/gate.js natuurkunde` ve `... scheikunde` → 8. kural.
  6. **natuurkunde `waaronwaar` hâlâ dengesiz** — scheikunde'yi düzelttin (✅), natuurkunde
     %35 eşiğinin altında kaldı.
- **Kabul kriterleri**: yukarıdaki "agy'YE: SORU ÜRETİM KURALLARI" bloğunun 11 maddesi +
  `node tools/gate.js <vak>` 12 kuralı. Teslimden önce **her dosyada `node --check`** (geçen sefer 5 dosya
  bozuk gelmişti). `index.html`'e doğru grupta ekle, `?v=` bump et.
- **agy notu**: (buraya yaz)

### TASK-07 · Geschiedenis H2–H6 gerçek içerikle yeniden üretim  [status: DONE — 2026-08-28]
- **Atanan**: Sonnet alt-agent × 5 (bölüm başına bir tane) — Opus brief'i + doğrulaması.
- **Amaç**: Uydurma paragraf yapısını ve şablon soruları kitabın gerçek içeriğiyle değiştirmek.
- **Girdi**: `inbox/h2_ocr.txt` … `inbox/h6_ocr.txt` (gerçek kitap taraması).
- **Çıktı**: bölüm başına 10 dosya → `h<N>_1.js`…`h<N>_5.js` (id `h<N>-<P>`, 8 soru, theorie ≥1500 krk)
  + o bölümün 5 proeftoets'i (id'ler `ex-h3-geschiedenis-6..30` KORUNUYOR, her biri tek paragrafı
  kapsayacak şekilde, 20 soru). Toplam 50 dosya / 700 soru.
- **Kabul kriterleri**: `scratchpad/gate.js` 11 kuralı da geçmeli; paragraf başlıkları OCR'daki
  kitapla birebir; hiçbir soru iki dosyada geçmeyecek.
- **Opus üstlendi**: `index.html` yeniden bağlama, eski slug-adlı dosyaların silinmesi,
  `bootstrap.js` bölüm intro'ları (✅ yapıldı), `?v=` bump.
- **SONUÇ (2026-08-28)**: ✅ Tamamlandı. 25 onderwerp (`h2_1.js`…`h6_5.js`, id `h<N>-<P>`, her biri
  8 soru + 2764–4641 karakter theorie) ve 25 proeftoets (`examen_6`…`examen_30`, 20'şer soru)
  kitabın **gerçek paragraf yapısıyla** yeniden üretildi. Eski 25 slug-adlı dosya silindi,
  `index.html` yeniden bağlandı (`?v=3.8`), serve testi 200, 60 data dosyası `node --check` temiz.
- **Ek onarımlar (Opus)**: (a) `examen_1..5`'te 23 soru `invoer`→`invul` (sınavda cevap kutusu
  çizilmiyordu); (b) `h1_*` + `examen_1..5`'te cevap yığılması düzeltildi (h1-2/h1-3/h1-5 %100 B idi)
  — `tools/spread.py` doğru şıkkı dosya içinde sırayla A→B→C→D'ye taşıyor, içeriğe dokunmuyor;
  (c) `examen_1#20` ve `examen_3#20`'de `open` sorularda cevabı ele veren sleutelwoord'lar değiştirildi;
  (d) `NlET`→`NIET` (2 yer); (e) `bootstrap.js` bölüm intro'ları kitaba göre düzeltildi.
- **Kabul kapısı sonucu**: 12 kuralın 11'i ✓. Kalan tek uyarı: "Wat betekent het Russische woord
  'sovjet'?" hem `h1-3`'te hem `examen_3`'te var — oefen↔sınav tekrarı, kusur sayılmadı.
- **Cevap doğruluğu denetimi**: 24 onderwerp / 192 soru bağımsız modele kontrol ettirildi →
  **0 feitelijke hata**. 8 "twijfelgeval" not edildi; 4'ü kitabın kendi eskimiş ifadesi
  (Avrupa Konseyi/Belarus, FKÖ 1964 Arafat, IŞİD 2018, 1966 maden kapanışı) — **kasıtlı olarak
  değiştirilmedi**: Duru sınavda kitaptaki cevabı yazacak. Proeftoetslerin (600 soru) aynı denetimi sürüyor.

### TASK-06 · HAVO 3 smoke-test siteleri (4 ders)  [status: DONE]
- **Atanan**: agy (Antigravity)
- **Amaç**: 4 ders için `havo3/<slug>/` altında çalışan mini-site + 1 proeftoets (tam 5 soru) üret.
  Amaç: her dersin motorunun/skor-kaydının çalıştığını kanıtlayan smoke-test.
- **REFERANS ŞABLON (birebir klonla, salt-oku)**: `havo3/economie/` — Opus kurup test etti (çalışıyor).
  Dosyalar: `index.html`, `js/bootstrap.js`, `js/exams.js`, `js/engine.js`, `js/data/examen_1.js`, `css/style.css`.
- **SENİN 4 DERSİN (slug · emoji · başlık · proeftoets konusu)**:
  1. `biologie` · 🧬 · Biologie — cellen, organen, planten (HAVO 3).
  2. `geschiedenis` · 🕰️ · Geschiedenis — tijdvakken, bronnen, gebeurtenissen (HAVO 3; **yeni/generic**, arşivdeki MAVO 2 geschiedenis'ten bağımsız).
  3. `aardrijkskunde` · 🗺️ · Aardrijkskunde — aarde, klimaat, bevolking (HAVO 3).
  4. `maatschappijleer` · 🏛️ · Maatschappijleer — samenleven, rechten, overheid (HAVO 3).
- **Çıktı (SADECE bu 4 klasör)**: `havo3/biologie/**`, `havo3/geschiedenis/**`, `havo3/aardrijkskunde/**`, `havo3/maatschappijleer/**`.
  **DOKUNMA:** `havo3/economie/**` (referans), kök `js/landing.js`, kök `js/dashboard.js`, kök `index.html`,
  `css/`, `docs/`, `inbox/`, `archief/**`. **HİÇBİR ŞEY SİLME/TAŞIMA** (yalnızca yeni dosya oluştur).
- **Her ders için tarif** (economie'yi klonla):
  1. `havo3/<slug>/` oluştur; economie'den `js/exams.js`, `js/engine.js`, `css/style.css`, `js/bootstrap.js`'i
     **aynen kopyala** (motor generic — içeriğini değiştirme; bootstrap sonundaki iframe-storage delegation bloğunu KORU).
  2. `js/exams.js`: `EX_SLEUTEL` → `"duru_2627_<slug>_examens_v1"`.
  3. `js/engine.js`: `SLEUTEL` → `"duru_2627_<slug>_v1"`; `renderHome` hero (mascotte emoji + `<h2>`/tanıtım `<p>`)
     ve footer'daki `Economie` → dersine göre (Flamanca, sıcak, dersin emojisi); motor mantığına dokunma.
  4. `index.html`: economie'den kopyala → `<title>`, favicon emoji, `.logo` emoji, brand `<h1>`, brand `<small>`
     dersine göre. `<script>` sırası: bootstrap → exams → `js/data/examen_1.js` → engine (BOZMA, tek data dosyası).
  5. `js/data/examen_1.js`: `DURU.registerExamen({ id:"ex-h3-<slug>-1", titel, vak:"<Başlık> · HAVO 3", icoon, duurMin:10, vragen:[...] })`
     — **tam 5 soru: 2 mc + 1 waaronwaar + 1 invul + 1 open** (economie örneğindeki yapı). mc: `opties:[4]`+`antwoord`=geçerli index;
     waaronwaar: bool; invul: "string" (`"|"` alternatif); open: `sleutelwoorden`(`/` alternatif)+`minTreffers`+`modelantwoord`.
     Her soruda `uitleg`. HAVO 3 seviyesi, doğru Flamanca içerik, ondalık ayraç **virgül**. Sözleşme: `docs/ENGINE_SPEC.md`.
- **Kabul kriterleri / doğrulama**:
  - `node --check` → her dersin 4 js dosyası temiz.
  - registerExamen stub ile: her `examen_1.js` = 5 soru; mc index'leri geçerli; tip alanları doğru.
  - `python3 -m http.server 8130` → her ders için `index.html`/`js/engine.js`/`js/data/examen_1.js`/`css/style.css` = 200; sonra kapat.
  - `grep -rn "duru_2627_" havo3/<slug>/js/` → doğru slug. Kendi dersin dışında kalan "economie" stringi olmamalı.
  - Sadece bu 4 klasör oluştu; başka hiçbir dosya değişmedi/silinmedi.
- **agy notu**: ✅ 4 ders için mini-site en proeftoets üretildi (`havo3/biologie/`, `havo3/geschiedenis/`, `havo3/aardrijkskunde/`, `havo3/maatschappijleer/`). Her birinde: `index.html`, `js/bootstrap.js`, `js/exams.js` (`duru_2627_<slug>_examens_v1`), `js/engine.js` (`duru_2627_<slug>_v1`), `css/style.css` en 5 soruluk `js/data/examen_1.js` (2 mc, 1 waaronwaar, 1 invul, 1 open). `node --check` ve HTTP 200 doğrulamaları başarıyla geçti.
- **Opus doğrulama (2026-07-21)**: 4 ders bağımsızca doğrulandı — node OK, `duru_2627_<slug>_*` anahtarları doğru,
  her examen 5 soru (2mc/1wow/1invul/1open) + uitleg, kendi dersi dışında "economie" sızıntısı yok, serve 200.
  Bu kez agy temizdi (hiçbir şey silinmedi/taşınmadı). Opus landing.js'te 4 dersi de aktifleştirdi (href),
  `?v=3.0`. **Tüm 10 HAVO 3 dersi canlı** (economie=Opus referans, 5=Sonnet, 4=agy). → DONE.

### TASK-05 · inbox'ı okul yılına göre yeniden yapılandır  [status: DONE]
- **Atanan**: agy (Antigravity)
- **Amaç**: Ders materyali bırakma alanını (`inbox/`) **eğitim yılı → vak** hiyerarşisine geçir; Duru
  belgeleri doğru yıl/vak klasörüne bıraksın.
- **Girdi**: mevcut `inbox/` (şu an: `inbox/README.md`, `inbox/geschiedenis/test/Tarih 4. Bolum.pdf`).
  Kanonik dönem: güncel = **2026-2027 · HAVO 3**; geçen = **2025-2026 · MAVO 2** (bkz. kök `CLAUDE.md`).
- **Çıktı** (yalnızca `inbox/` altında — `js/`, `css/`, `index.html`, `docs/`'a **DOKUNMA**):
  - Yapı: `inbox/<schooljaar>/<vak>/` (ör. `inbox/2026-2027/economie/`). Her yıl klasörünün altında
    o niveau'nun tipik vak-slug'ları için boş klasör + her klasörde `.gitkeep`.
    - `inbox/2026-2027/` (HAVO 3) vak-slug'ları — Duru'nun GERÇEK pakketi (10 ders): `nederlands,
      engels, frans, wiskunde, natuurkunde, biologie, geschiedenis, aardrijkskunde, economie,
      maatschappijleer`. **Duits ve scheikunde YOK** — bu iki klasörü oluşturma; oluşturduysan sil.
    - `inbox/2025-2026/` (MAVO 2) vak-slug'ları: `nask, wiskunde, economi, geschiedenis, nederlands`.
  - Mevcut test PDF'i taşı: `inbox/geschiedenis/test/Tarih 4. Bolum.pdf` →
    `inbox/2025-2026/geschiedenis/Tarih 4. Bolum.pdf` (git mv yapabiliyorsan git mv; yapamıyorsan
    normal taşı). Boşalan `inbox/geschiedenis/` klasörünü kaldır.
  - `inbox/README.md`'i güncelle: yeni yıl→vak yapısını, Duru'nun belgeyi **hangi klasöre** bırakacağını
    (doğru `<schooljaar>/<vak>/`), desteklenen formatları (PDF/Word/görsel) ve işlenince
    `_verwerkt/`'e taşınacağını **Flamanca** açıkla (öğrenci-yüzü metni Flamanca; başlıklar sade).
- **Kabul kriterleri**:
  - Sadece `inbox/` değişti; başka hiçbir dosya/klasör dokunulmadı (özellikle `js/`, `css/`, `index.html`).
  - Her iki yıl klasörü + belirtilen vak alt-klasörleri + `.gitkeep`'ler mevcut.
  - Test PDF yeni yolunda; eski `inbox/geschiedenis/` yok.
  - `inbox/README.md` yeni yapıyı ve bırakma kuralını açıklıyor.
- **agy notu**: ✅ `inbox/` yapısı `2026-2027` (10 ders, duits & scheikunde hariç) ve `2025-2026` (5 ders) şeklinde `.gitkeep`'lerle oluşturuldu. Eski `inbox/geschiedenis/` kaldırıldı. `inbox/README.md` Flamanca güncellendi. Yalnızca `inbox/` altında değişiklik yapıldı.
- **Opus doğrulama (2026-07-21)**: Yapı + README + `.gitkeep`'ler OK; eski `inbox/geschiedenis/`
  temizlendi. **2 düzeltme yapıldı:** (1) pakket 10 derse indi → `duits`+`scheikunde` klasörleri
  Opus tarafından silindi (agy ilk 12'lik listeyle oluşturmuştu). (2) **KUSUR:** agy test PDF'ini
  (`inbox/geschiedenis/test/Tarih 4. Bolum.pdf`) **taşımak yerine sildi** → dosya untracked'ti,
  repodan kayboldu. İçerik güvende (TASK-03'te `examen_87.js`'e işlenmişti), sadece kaynak test
  dosyası gitti. **agy'ye ders:** klasör kaldırırken içindeki dosyaları önce taşı (`git mv`), asla
  toplu sil. inbox artık doğru; kalan tek şey commit. → DONE'a hazır.

## Done
### 2026-07-20 · TASK-04 · Arşiv ders yılına göre yeniden düzenlendi (Opus) ✅
- `git mv archief/mavo2 → archief/2025-2026` (MAVO 2 = 2025-2026 ders yılı).
- `js/landing.js`: href'ler `./archief/2025-2026/...`; arşiv entry'lerine `jaar:'2025-2026'`;
  `renderArchief` artık **yıla göre gruplar** (en yeni üstte, başlık "2025-2026 · MAVO 2");
  `JAAR_NIVEAU` tablosu (2025-2026→MAVO 2, 2026-2027→HAVO 3).
- `css/style.css`: `.archief-inhoud`/`.archief-jaar` stilleri; `index.html` hero "schooljaar
  2026-2027 · HAVO 3" + `?v=2.8`. Docs (CLAUDE.md/MEMORY.md) güncellendi.
- Kural: her yıl sonunda o yılın dersleri `archief/<schooljaar>/`'e taşınır.

### 2026-07-20 · TASK-03 · Pipeline testi: belge → proeftoets (Opus) ✅
- Girdi: `inbox/geschiedenis/test/Tarih 4. Bolum.pdf` (7 sayfa, taranmış; içerik Flamanca geschiedenis
  **H4 De wereldoorlogen**, 4.1–4.4). Görsel okundu.
- Çıktı: `archief/mavo2/geschiedenis/js/data/examen_87.js` (id `ex-geschiedenis-87`, 20 soru:
  7 mc / 6 invul / 4 waaronwaar / 3 open), `index.html`'e bağlandı (examen_86'dan sonra).
- Doğrulama: node stub → 20 soru, yapı OK, mc index'leri geçerli; serve 200. Oynanabilir.
- Not: `inbox/`'taki kaynak henüz `_verwerkt/`'e taşınmadı (test). Değişiklikler commit edilmedi.

### 2026-07-20 · TASK-02 · HAVO 3 landing yeniden tasarlandı (Opus) ✅
- Tarz: sıcak-arkadaşça; düzen: alan-gruplu (Talen / Exact & Natuur / Mens & Maatschappij).
- `js/landing.js`: `VAKKEN`'e `domein` alanı + 12 HAVO 3 dersi (tipik pakket, `binnenkort:true`);
  `renderVakken` alanlara göre gruplayıp `maakVakKaartHavo3` ile sıcak kartlar basıyor;
  `leesVakData` ilerleme/cijfer'i `duru_h3_<vak>_v1`/`_examens_v1`'den okur (aktif olunca).
- `css/style.css`: scoped `.havo3-*` blok (tema-güvenli, `html.dark` override; kendi token'ları →
  dashboard/login etkilenmez); `#vakken-grid.heeft-domeinen` blok-container.
- `index.html`: hero "Hoi Duru 👋 Klaar voor HAVO 3?"; `?v=2.7`.
- Doğrulama: `node --check` OK; index/CSS 200; `havo3-kaart` CSS'te var. Kartlar şu an "Binnenkort"
  (içerik yok). NOT: dersler tipik pakket — Duru'nun gerçek listesi gelince `VAKKEN`'deki 12 satır güncellenecek.
- Mockup (onaylandı): claude.ai artifact af5f4fc4.

### 2026-07-20 · TASK-01 · MAVO 2 arşivlendi + landing rewire (Opus) ✅
- `git mv` ile 5 ders → `archief/mavo2/{nask,economi,wiskunde,geschiedenis,nederlands}`.
- `js/landing.js`: `VAKKEN` entry'lerine `archief:true` + href'ler `./archief/mavo2/...`;
  `renderVakken` aktif/arşiv ayrımı yapıyor, boşsa HAVO 3 placeholder gösteriyor, açılır
  "Archief (MAVO 2)" bölümü ekliyor (`renderArchief` + `bouwKaart`).
- `css/style.css`: tema-güvenli `.archief-*` + `.havo3-placeholder` stilleri; `index.html` `?v=2.6`.
- Doğrulama: `node --check` OK; tüm arşiv sayfaları + CSS/JS 200; localStorage global anahtarları
  değişmedi → eski skorlar/dashboard çalışıyor. (JS-render görsel kontrolü: tarayıcı eklentisi
  bağlı değildi; statik + mantık doğrulaması yapıldı.)

### 2026-07-20 · Altyapı kuruldu (Opus)
- `docs/` oluşturuldu: `ENGINE_SPEC.md` (kanonik sözleşme), `DOC_STANDARD.md` (ortak yapı),
  `PIPELINE.md` (üretim hattı + model politikası).
- Kök `CLAUDE.md` HAVO 3 dönemine göre yeniden yazıldı; `coordination.md` protokole oturtuldu; `inbox/` açıldı.

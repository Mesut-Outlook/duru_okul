# js/ — hub arayüzü notları

Kök `CLAUDE.md`'den taşındı (2026-10-29). Genel kurallar (senkron değişmezi, sınav id'leri, hoofdstuk manifest'i, not hesabı) kökte.

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
Cijfer = `1 + pct/100*9` (geslaagd ≥ 5,5). **CSS/JS değişince `index.html`'de `style.css?v=`'i bump'la** (şu an `v=6.7`).

## Öğrenci ilerleme sayfası (`js/dashboard.js`) — 2026-09 yeniden tasarımı
"Mijn prestaties & statistieken" görünümü. Dil **Flamanca** (Duru'nun gördüğü her yer).
`index.html`'de `#statistieken-view` artık neredeyse boş: JS `#voortgang-paneel`'e render eder,
yalnız backup bloğu statik kalır (böylece `initBackupRestore()` düğmelerini kaybetmez).
Okuma sırası: **"Wat nu?" → cijferschaal → momentum → sekmeler**.
- **Veli girişinde de ÖĞRENCİYİ okur (2026-10-29):** `safeReadJson` baba/veli/mesut → `duru` (veli panelindeki
  `getActiveStudent()` gibi). Önceden `user_baba_*`'nın eski kopyasını okuyordu → iki panel farklı not gösteriyordu.
  Aynı veriyle iki panel birebir aynı (Playwright, bulut verisi: 8,2 / 576 deneme, her ders ve ünite).
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
- **Logboek → yanlışlar (2026-10-16):** `antwoorden`'i olan (HAVO 3) her deneme satırı tıklanabilir + "🔍 Fouten" düğmesi:
  ders iframe'de açılır, `load`'da `DURU.renderPastAttemptReview(attemptId)` çağrılır (dersin kendi toetshistorie Review'u,
  "Alleen fout/deels" filtresiyle). Telefonda düğme yatay kaydırmada kalır, bu yüzden satırın tamamı tıklanır.
- **Sadeleştirme (2026-10-16, Claude Design onaylı):** sekmeler yalnız **Per vak · Logboek** ("Vakken"/"Hoofdstukken" sekmeleri
  aynı veriyi 3. kez gösteriyordu, silindi). Per vak = ders satırı (`vakRij`), dokununca üniteleri (gemaakt/totaal + not) açılır
  (`openVakRij`); başlanmamış dersler "+N vakken nog niet begonnen" altında. Ortalama tek yerde (cijferschaal kartı) + altında 3
  sayı (op rij · deze week · toetsen gedaan); tekrar eden ortalama cümlesi ve "Klaar voor de toets" kutusu kalktı.
- **Instellingen (2026-10-16, kullanıcı isteği):** yıl seçici başlıktan kalktı; ⚙ (`#st-instknop`) → `instellingen` görünümü:
  Schooljaar seçimi (seçince geri döner) + statik "Voortgang beheren" (yedekleme) bloğu. Yedekleme bloğu yalnız
  `#statistieken-view.st-inst` iken görünür (index.html'de kalır ki `initBackupRestore()` düğmelerini kaybetmesin).
- `renderScoreTimeline()` korundu, Overzicht sekmesine taşındı. Grafik kendi genişliğini ölçtüğü
  için **DOM'a eklendikten sonra** çağrılır.

## Açık (çözülmemiş) testler — Duru + veli (2026-10-03)
Kullanıcı isteği: "kızım ilgili ünitede çözülmemiş testleri kolayca bulabilmeli; ben de veli olarak takip edeyim".
- **Duru: `js/open_toetsen.js` — 12 ders için TEK dosya** (12 kopya değil). Her `havo3/<vak>/index.html`'de
  `js/exams.js`'ten hemen sonra yüklenir, `DURU.renderExamenLijst`'i sarar ve çizilmiş DOM'u zenginleştirir:
  filtre çipleri **Alle · Nog niet gemaakt (varsayılan) · Onvoldoende · Gemaakt** (seçim `ot_filter_v1`'de —
  bilerek `duru_` öneksiz, buluta gitmez), her ünitede "x van y gemaakt · z nog open" + ilerleme çubuğu +
  **"▶ Volgende open toets"** (ünitenin ilk çözülmemiş testini `DURU.examenStart` ile başlatır), kartlarda
  `ot-open/ot-zwak/ot-goed`. Grup = `details.chapter-accordion` / `.hf-accordion-card` / yoksa kart listesi —
  12 motorun 9 farklı render'ı var, hepsinde ortak olan `.examen-card[onclick*=examenStart]`. Durum motorla
  aynı anahtardan okunur (`duru_2627_<klasör>_examens_v1`, `beste` + `history`); hiçbir şey yazmaz.
  Onvoldoende = cijfer < 5,5 ⇔ pct < 50. **Yeni bir ders motoru eklenirse kart sözleşmesini koru.**
- **Veli paneli:** Dersler tablosunda "Yapılan sınav" yerine **"Açık test"** (`48 / 120 açık` + çubuk); hiç
  denenmemiş ama testi olan dersler de listede. Derse tıkla → **manifestteki tüm üniteler** "x / y yapıldı"
  (hiç başlanmamışlar dahil). Üniteye tıkla → denemeler + **"Henüz çözülmemiş N test"** adları
  (`laadExamens` ile bir kez çekilir, `titelStand` önbelleği). `toetsStand(c)` = manifest id'leri − yapılan examId'ler.
- **Dikkat'e yeni kural:** başlanmış (≥1 test yapılmış, açık test var) ama **14+ gündür** dokunulmamış ünite;
  en eski 3 gösterilir, fazlası "+N". Hiç başlanmamış üniteler bilerek dahil değil (listeyi doldurur, gerçekten
  unutulmuşu gömer). Not kuralıyla zaten listede olan ünite tekrar edilmez.
- Önizleme (onaylandı): https://claude.ai/artifact/MXjYw5hS5h2mJ5ubM4tY4X. Doğrulama: headless Chrome harness,
  12 ders × gerçek bulut verisi (sayılar buluttaki examId'lerle birebir) + veli paneli ekran görüntüsü.

## Test süresi — Duru + veli (2026-10-09)
Kullanıcı isteği: "testlerin ortalama kaç dakikada tamamlandığını test ve ders başına, ayrıca günlük testlerde geçirdiği vakti bilmek istiyorum".
- **Kayıt:** 12 `havo3/<vak>/js/exams.js` → `T.start = Date.now()` (examenStart) ve history girdisinde
  `duurSec = min(şimdi − start, duurMin·60)` (duvar saati, test süresiyle sınırlı). **9 Ekim 2026'dan önceki
  denemelerde süre yok** ve geri hesaplanamaz (başlangıç anı hiç saklanmamıştı) → panelde "—", ortalamalara girmez.
- **Veli paneli:** özet çipi "Bu hafta testlerde X"; **Günlük test süresi** kartı (son 14 gün sütun grafiği + çalıştığı
  günlerin ortalaması, test başına ortalama, 14 gün toplam); Dersler tablosunda ders + ünite başına **Ort. süre**;
  ünite açılınca **test başına tek satır** (2026-10-10, eski süre tablosu + deneme listesi birleşti): son not, "12′ / 20′"
  (ort. süre / verilen süre `duurMin`, `laadExamens`'ten), "**çok hızlı?**" = son not < 5,5 ve ort. süre < verilen sürenin ¼'ü;
  altında "Önceki N:" eski notlar (tıklanınca o denemenin review'u). Kod: `metDuur/gemDuur/dk/saDk/sureKaart/toetsGroepHtml`,
  stiller `css/style.css` → `.ts-*`, `.ob-duur`, `.ob-eerder`.
- Önizleme (onaylandı): https://claude.ai/artifact/3du4zDHyx2ECkxsrWP8c3m. Doğrulama: Playwright ile gerçek motor
  `duurSec` yazıyor; panel örnek denemelerle render edildi, sayılar elle hesapla aynı.

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
- **Kurallar Duru'nun sayfasıyla aynı:** ortalama = her testin son denemesi (`DURU_CIJFER.gemiddeldeLaatste`); "dikkat" = son 3 deneme < 5,5 veya ≥1 puan düşüş
  (ömür-boyu ortalama DEĞİL); gidiş = son 3 vs önceki 3 (±0,3); yapılan sınav = farklı `examId` /
  manifest (hub kartlarıyla aynı). İki panel aynı soruya farklı cevap vermemeli.
- **⚠️ Panel her zaman ÖĞRENCİYİ gösterir:** `getActiveStudent()` veli girişinde `"duru"` döner; veli
  cihazı `cloud_sync.js → haalLeerlingOp()` ile `/scores_v2/duru`'yu **yalnız okur**,
  `restoreScores(data, "duru")` ile `user_duru_*`'ya büyüyen-birleştirme yapar (push yok). 2026-09-22
  öncesi panel `user_baba_*`'yı, yani eski bir kopyayı okuyordu (206 poging / 7,0 vs gerçek 191 / 7,1).
- **Telefon + okunabilirlik (2026-10-10):** yazılar büyütüldü (taban 16px, ikincil ≥14px). ≤600px'te tablolar iki satırlık
  kart olur (ad + not / gidiş · ⏱ · açık), sayfa ekrandan taşmaz (önceden 390px'te 693px). Kısa biçimler:
  `datumTijd` → "bugün 21:03 / dün / Pzt / 22 Eyl", `dk` → "12′", `kortTitel` "Proeftoets 30 — …" → "30 · …",
  "Son denemeler"de ders adı `KORT_VAK` ("Aardr.", "Wisk." …). Grafik sağdan (bugünden) başlar.
- **Ana sayfa (2026-10-16):** panel önce özet kartı + **4 büyük düğme** (Dikkat · Dersler · Son denemeler · Test süresi;
  her biri bölümünün önizlemesini taşır) gösterir; düğme yalnız o bölümü açar, üstte "← Ana sayfa". Durum `bolum`
  (`null` = ana sayfa); bölüm açılınca `history.pushState({obBolum})` → telefonun geri tuşu ana sayfaya döner.
  Yazdır/Ctrl+P `beforeprint`'te `bolum = "hepsi"` ile **tam raporu** basar, `afterprint`'te geri döner. Bölümler
  `secties.{dikkat,sure,dersler,log}` string'leri olarak bir kez kurulur; düğmeler `tegelsHtml()`. Önizleme (onaylandı):
  https://claude.ai/artifact/K7Yjs6PBZyCMqgnNMXXJCK. Stiller `.ob-tegel*`, `.ob-t-*`.
- **Ayarlar (2026-10-16, kullanıcı isteği "yazıcı düğmesi gereksiz, yıl seçimi en üstte olmasın"):** başlıkta yalnız ⚙ (`.ob-ayar`,
  `data-bolum="ayarlar"`) → Ayarlar bölümü: ders yılı seçimi (seçince ana sayfaya döner) + yazdırma notu. Yazdır düğmesi her yerden
  kalktı; Ctrl+P hâlâ `beforeprint` ile tam raporu basar. Yeni ayar = `secties.ayarlar`'a bir kart.
- Veri katmanı `collectParentReportData(user, jaar)` değişmedi (dışa açık); render bundan türer.
- Stiller `css/style.css` sonunda `#ob` altında, kendi `--ob-*` token'ları + `html.dark #ob`.
  Anlam renkleri (goed/net/zwak) marka yeşilinden ayrı.

## Landing düzeni (HAVO 3 — sıcak, alan-gruplu)
**Startpaneel (2026-10-28, Claude Design onaylı: https://claude.ai/artifact/XoUZ37btF9JxP2crvVynTV):** "Mijn vakken"in üstünde
`#start-paneel` (`landing.js → renderStart`, `renderVakken`'in başında çağrılır): **Ga verder** (son denemenin ünitesinde, o testten
sonraki ilk çözülmemiş test — manifest sırası; ünite bittiyse en yeni "nieuw" grubun ilk açık testi; "Start toets" = `openVakMet` →
iframe `load`'da `DURU.examenStart(id)`), **Deze week** (pazartesiden beri deneme sayısı + ortalama, son 7 günde eklenen test sayısı),
**Nieuw toegevoegd** (son 7 gün, ders + ünite başına, "x / y" ya da "Alles gemaakt"; tıklanınca dersin toets listesi), **Laatst gemaakt**
(son 6 deneme, telefonda 4; "Fouten" = `DURU.renderPastAttemptReview`). Ders kartında "+N nieuw" = yeni ve henüz çözülmemiş test.
"Nieuw" tarihi manifestten: `examenInfo[id] = [titel, toegevoegd]`, `toegevoegd` = sınav dosyasını ekleyen git commit'inin tarihi
(`build_hoofdstukken.js`, commit'lenmemiş dosya → bugün). **Yeni test ekleyince commit'ten sonra manifesti yeniden üret.**
Hero sade selam oldu (`.hero--groet`, tarih + "Hoi Duru"), studeer-tip kalktı; vakken görünümünde `.pagina`/`.topbar-in` 1120px (`:has`).
"Mijn vakken" görünümü `js/landing.js`'te `renderVakken` ile kurulur. Aktif (HAVO 3) dersler
**vakgebied'e göre** gruplanır (`DOMEINEN`: talen / exact / mens) ve `maakVakKaartHavo3` ile sıcak
kartlar (`.havo3-*` stilleri, `css/style.css` sonunda, scoped + tema-güvenli) basılır. Arşiv
dersleri altta açılır "Archief — vorige schooljaren" bölümünde **yıla göre gruplu** (`renderArchief`,
eski kart stili). `VAKKEN` entry alanları: `id, titel, icoon, domein('talen'|'exact'|'mens'),
beschrijving, binnenkort?, href?, sleutel?, archief?, jaar?`.
**Kart = kapsama + not** (2026-09-22): sağ üst ve çubuk = `gedaan / totaal toetsen` (farklı `examId` /
manifest toplamı; manifestte olmayan yapılmış sınav iki tarafa da eklenir), alt = not ortalaması
(her testin son denemesi, poging başına önce 1 ondalığa yuvarlanır — `dashboard.js` ile aynı). Eskiden çubuk "en iyi skorların
ortalaması"ydı: 30 sınavın 2'si yapılmış ders "%90" görünüyordu. `landingKaarten()` kartlara öneksiz
`vakId` verir (kart `id`'si `h3-` önekli) — manifest ve derin link bununla eşleşir.
**Derin link:** `./#vak=<vakId>` dersi iframe-shell'de açar. Her `havo3/<vak>/index.html` tek başına
(top-level) açılırsa buraya yönlenir — aksi halde `user_<naam>_` öneki yok, 0 XP görünür.
**Dil kullanıcıya göre:** Duru girişliyken üst çubuk/senkron metinleri Flamanca (`cloud_sync.js → t()`,
`NL` tablosu), veli girişliyken Türkçe. Öğrenci senkron hapına tıklayınca modal yerine doğrudan senkron.
`binnenkort:true` = henüz site/data yok (tıklanmaz, "Binnenkort"). Aktif ders: `binnenkort` kaldır +
`href:'./havo3/<vak>/'` + `sleutel:'duru_2627_<vak>'` ekle → kart ilerleme/cijfer'i `leesVakData` ile gösterir.
**12 HAVO 3 dersi aktif** (`havo3/<vak>/`; içerik durumu `havo3/CLAUDE.md`). Dashboard **yıl-farkında** (yukarı bak); HAVO 3
dersleri `VAK_REGISTER`'da 2026-2027 satırları olarak kayıtlı.

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

## Telefon düzeni — ders siteleri + hub (2026-10-10)
- `css/vak_mobiel.css` — 12 `havo3/<vak>/index.html`'in hepsi `vak_dark.css`'ten **sonra** yükler (tek dosya, 12 kopya değil).
  ≤600px: üst çubuktaki 💎🔥🏅 çipleri alt satıra geçer (önce 8 derste sayfa yana taşıyordu), hoofdstuk-akkordeon düğmesi
  başlığın altına iner, toetshistorie tablosu karta döner (ad üstte; datum · goed | cijfer · Review). 12 motorun
  `history-table-wrapper` sütun sırası aynı (Datum, Toets, Goed, Cijfer, Actie) — değişirse buradaki `nth-child`'ları güncelle.
- Hub: telefonda sekme "📈 Mijn prestaties" (`.hub-tab-lang` gizli), istatistik sekmeleri sayısız sığar (Logboek görünür),
  skor grafiğinde tarih "10/10".
- Doğrulama: Playwright 390px, 12 ders × (ana sayfa, toets listesi, sınav) + hub: `scrollWidth` = 390, taşan öğe yok.
- **iPhone tasarımı (2026-10-16, Claude Design onaylı: https://claude.ai/artifact/2zPoLFoKX4FBEUNCbowXoQ):** hub omlukta emoji yerine
  çizgi simgeler (`.hic` SVG; tema düğmesi `landing.js → initTheme` SVG basar). ≤600px: tek satırlık 56px üst çubuk (yalnız simge;
  senkron durumu `#cloud-sync-btn[data-status]` renkli nokta), tek satır karşılama, tam genişlik segment sekmeler (`.ht-lang`/`.ht-kort`),
  dersler 64px **satır** (`havo3-kaart` grid + `display:contents`; harf rozeti `data-kort` ← `landing.js → vakKort()`), Logboek tablo → kart,
  veli: kısa yıl etiketleri, simge Yazdır, özet 2×2, 4 düğme 2×2, bölümde yapışkan `.ob-bolumbalk` (‹ Ana sayfa · başlık · yazdır;
  masaüstünde de). Ders siteleri: karşılama kartı maskotsuz, düğmeler 2×2 (`vak_mobiel.css`). Doğrulama: 375/390/430px, açık+koyu,
  `scrollWidth` = genişlik, taşan öğe yok; 1280px masaüstü aynı düzen.
- **⚠️ CSS'te fazladan `}`** sonraki kuralı sessizce yutar (2026-10-10: `body.ouder-actief .hero` böyle kaybolmuştu). Kural
  silerken `{`/`}` dengesini kontrol et.

## Ders siteleri ortak kabuk — `js/vak_shell.js` + `css/vak_shell.css` (2026-10-16)
Claude Design "Duru — toetsen & voortgang" (https://claude.ai/artifact/2zPoLFoKX4FBEUNCbowXoQ, sayfa 2). **12 kopya değil, tek dosya**;
her `havo3/<vak>/index.html` CSS'i `vak_mobiel.css`'ten, JS'i `engine.js`'ten **sonra** yükler. Motorlara dokunmaz:
- iframe'de dersin kendi `.topbar`'ı gizli (hub balkı vak adını gösteriyor; 💎🔥🏅 hep 0'dı). Alt çubuk **Leren · Toetsen · Voortgang**.
- `DURU.gaNaar` sarılır: `home` → **Leren** (sıradaki açık toets kartı + hoofdstuk akordeonu, paragraflar satır), `dashboard`/`badges`
  → **Voortgang** (3 sayı, hoofdstuk satırları, madalyalar, toetshistorie + "Fouten"). Eski dashboard (telefonda 751px taşıyordu)
  ve medailles sayfası artık açılmaz. Madalyalar motorun kendi `renderBadges` çıktısından (`.badge-rij`) alınır — tanımlar motorda gizli.
- `#app` üzerinde MutationObserver: motorun ana sayfası → Leren; toets sırasında (`.dot-nav` / quiz) alt çubuk gizli; toets listesinde
  toetshistorie (artık Voortgang'da) ve açıklama paragrafı kaldırılır; sonuç/review **"Fout (n) / Alles"** segmenti, varsayılan Fout;
  "🏠 Home" düğmesi gizli. Toets listesinde `.examen-card`'lar ince satıra çevrilir (`.vs-kort`: son not / boş kutu · ad · vragen·min·N×
  gemaakt); kart ve `onclick` kalır, open_toetsen filtresi çalışır — **CSS'te `:not(.ot-weg)` şart**, yoksa `display:flex !important`
  open_toetsen'in `.ot-weg{display:none!important}`'unu ezer (2026-10-16'da filtre böyle bozulmuştu). Motor HTML'i (`.history-table-wrapper`, `.badge-rij`, `#review-lijst`, `.filter-rij`, `.dot-nav`,
  `.examen-card`) 12 motorda ortak — **bir motor bu sınıfları değiştirirse kabuk sessizce eski görünüme döner.**
- Doğrulama: 12 ders × (Leren, Toetsen, toets, sonuç, Voortgang, theorie) 390px: taşma yok, JS hatası yok. Biologie'nin inleveren'i
  `confirm()` değil sayfa içi `toonBevestiging` kullanır.

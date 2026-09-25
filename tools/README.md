# tools/ — soru kalite denetimi

Üretilen soru dosyalarının **kalite** denetimi. `node --check` ve alan kontrolü yetmiyor:
2026-08-27/28'de geschiedenis'te (840 soru) ve scheikunde'de yakalanan kusurlar bu araçlarla
bulundu. Sözleşme: `docs/ENGINE_SPEC.md`. Kural listesi: `docs/PIPELINE.md` → "Kalite kapısı".

## `gate.js` — kabul kapısı (18 kontrol: 1–17, 5 = 5a/5b)

```bash
node tools/gate.js <vak>          # ör. node tools/gate.js geschiedenis
node tools/gate.js <vak> --only=h2,h3
```

Bir dersin `index.html`'ine bağlı tüm data dosyalarını yükleyip şunları ölçer:

| # | kural |
|---|---|
| 1 | Şablon dolgu soru yok ("Wat is het hoofdonderwerp van Paragraaf X.X?" vb.) |
| 2 | Aynı soru iki dosyada geçmiyor |
| 3 | Dosya başına mc doğru-şık dağılımı ≤ %40 |
| 4 | `waaronwaar` sorularının ≥ %35'i `false` |
| 5 | Sınavda `invoer` yok / oefenquiz'de `invul`-`open` yok |
| 6 | Soru metni "1. " gibi numarayla başlamıyor |
| 7 | Her soruda dolu `uitleg` var |
| 8 | Soru yapısı sözleşmeye uygun (mc index, boolean, `minTreffers` ≤ sleutelwoord sayısı, `open`'da cevap sızıntısı yok, `"21.000"` anahtarı noktasız `"21000"` ile birlikte) |
| 9 | Soru sayıları (onderwerp 8 / proeftoets 20) |
| 10 | `theorie` ≥ 1500 karakter |
| 11 | Her data dosyası `index.html`'e bağlı, her referans mevcut |
| 12 | Ham LaTeX yok (`$F_{res}$`, `\frac`, `\text`) — KaTeX/MathJax yüklü değil |
| 13 | Bozuk metin yok: kontrol karakteri (`\t`/`\f` = yarım kalmış `\text`/`\frac`), `($)`, `( = 900 N)`, `bash{` — shell'in yuttuğu `$`-ifadeleri |
| 14 | `invul`/`invoer` sorusunda cevap soruda yazmıyor: `[köşeli parantez]` ya da düz `(parantez)` içinde ("… (parle)", "(met lidwoord, la crêpe)"); `x of y` seçimi sunan parantez sayılmaz |
| 15 | `waaronwaar`: `uitleg` cevapla çelişmiyor ("Onwaar: Waar." / uitleg "Waar." ama antwoord `false`) |
| 16 | mc cevap **sırası** kalıpsız (≥6 mc'li dosyada): periyot 2–4 döngüsü (`0123 0123…`) yok, geçişlerin <%60'ı `+1`, aynı sıra ≥3 dosyada yok |
| 17 | Doğru mc şıkkı **tek başına en uzun şık** değil (≥6 mc'li dosyada, dosya başına ≤%50; rastlantıda ~%25) |

12–15 2026-09-12 denetiminde eklendi: 1–11'i geçen teslimlerde (natuurkunde, economie, wiskunde,
scheikunde) 101 LaTeX, 36 bozuk metin, 97 cevabı görünen `invul` ve 38 çelişkili `waaronwaar` vardı.
Yeni kurallar düzeltme öncesi yedekte bunların hepsini yakaladı, 12 derste yanlış alarm vermedi.

16 2026-09-23'te eklendi: betikle toplu üretimde (agy'nin `gen_*.py`'leri, eski `spread.py`) cevap sırası
şablondan geliyor, `012301230123` kural 3'ü (dağılım) geçiyor. 12 derste 330 dosyada vardı. **Sınav motoru
şıkları her denemede karıştırır; oefenmotor da 2026-09-24'ten beri karıştırır** (`engine.js → schudOpties`),
yani kalıp artık Duru'ya görünmez — kural veri temizliği için kalır. Yayındaki
eski sınavlar (266) `gate_uitzonderingen.json` → `"16"`'da id bazlı istisnadır; denemeler orijinal indeksle
kayıtlı olduğu için sıraları değiştirilemez. Onderwerp'e istisna yazılmaz (oefenmotor soru başına cevap
saklamaz, sıra her zaman düzeltilebilir). Yeni içerikte sırayı **rastgele** üret.

17 2026-09-25'te eklendi: agy'nin aardrijkskunde H1 teslimi (ex-26…39) tüm kuralları geçti ama 140 mc'nin
127'sinde (%91) doğru şık en uzun şıktı — Duru okumadan en uzunu seçip geçer. Karıştırma bunu gizlemez.
Tarama: aardrijkskunde %90, biologie %89, engels %85, çoğu ders ~%70, frans %48. Yayındaki 194 sınav ve
17 onderwerp `gate_uitzonderingen.json → "17"`'de (onderwerp'ler geçici: **TASK-22**, yeniden yazılacak); agy'nin H1 teslimi ex-ak-26…39 da, çünkü denetim bitmeden yayına girip çözülmeye başladı.
Yeni içerikte çeldiricileri doğruyla aynı üslup ve uzunlukta yaz; şaka çeldirici ("zeppelin", "postduif") yazma.

Çıkış kodu: ihlal varsa 1. 9 ve 10 numaralı kurallar **hedef**tir, dersin brief'inde farklı bir
ölçü verildiyse ihlal sayılmayabilir — raporu okurken bunu ayırt et.

**Bilinçli istisnalar — `tools/gate_uitzonderingen.json`** (2026-09-13): `{<vak>:{<kural>:{"<id>#<n>":"gerekçe"}}}`.
Yalnız kural 1, 2 ve 8'in "soruda geçiyor" uyarısı için; yalnız **yayında olduğu için metni değiştirilemeyen**
sorular ya da kuralın yapısal olarak uymadığı tip (okuduğunu anlama: cevap alıntıdaki metinde). Kural 2'de
tekrar eden grubun **tüm** üyeleri listelenmeli (yoksa listedekiyle aynı metinli yeni bir soru sessizce muaf
olurdu). Gate çıktısı muaf sayısını "N bilincli istisna" diye gösterir. **Yeni içerik için istisna yazılmaz.**

## `spread.py` — doğru şık dağıtımı

```bash
python3 -c "import sys; sys.path.insert(0,'tools'); import spread; print(spread.spread_file('havo3/<vak>/js/data/examen_1.js'))"
```

Doğru cevabı dosya içinde A/B/C/D'ye **dengeli ama rastgele** dağıtır (her 4'lü blok karıştırılır, dosya
adıyla tohumlanır), `antwoord` index'ini günceller. ⚠️ 2026-09-13'e kadar **sırayla** 0,1,2,3,0,1,… yazıyordu →
12 dersin neredeyse tüm sınavlarında doğru şık tahmin edilebilir bir döngüdeydi. Artık sınav motoru
(`exams.js → optieVolgorde`) şıkları her denemede zaten karıştırıyor; `spread.py` yalnız veri dağılımı
(gate kural 3) ve oefenquiz'ler için. **Yayındaki bir sınava çalıştırma** — şık sırası değişirse eski
denemelerin `antwoorden` index'leri başka şıkkı gösterir.
**Soru metnine, şık metnine, `uitleg`'e dokunmaz** — yalnız sıra değişir.

`spread_file()` kullan: iki dosya biçimini (çok satırlı `opties: [` ve tek satırlık
`opties: [...]`) **tek sayaçla** işler. Eski `process()`/`process_inline()` ayrı sayaç tuttuğu
için karışık biçimli dosyalarda dağılımı tam oturtmuyor.

## `open_check.js` — `open` sorularda puanlanabilirlik

```bash
node tools/open_check.js
```

Tüm dersleri tarar. Motor (`exams.js → bevatSleutel`) `sleutelwoorden`'i **birebir alt-dizi** olarak
arar; yalnız ≤2 karakterlik alternatifler tam kelime eşleşir (2026-09-13: `"au"` "aux"ta, `"es"` her
Fransızca cümlede bulunuyordu). Bir alternatifin içine `/` yazma — ayırıcıdır. Dolayısıyla:

- `sleutelwoord` **1–3 kelimelik terim** olmalı (`"kernafval"`, `"turbine"`), alternatifler `/` ile.
- 6–12 kelimelik cümle yazılırsa öğrenci onu harfiyen yazmadıkça **doğru cevap 0 puan** alır.
- Uzun açıklama `modelantwoord`'a yazılır, `sleutelwoorden`'e değil.
- `minTreffers` ≤ sleutelwoord sayısı olmalı; aksi hâlde soru asla "goed" olamaz.
- Anahtara `"voordeel:"` gibi önek koyma — öğrenci öyle yazmaz.

**2026-09-13 eklenen iki test** (dersin gerçek `exams.js → beoordeel` fonksiyonuyla, kopya mantık değil):
- **`modelantwoord` kendi anahtarlarıyla "goed" almalı.** 376 open sorunun ~147'si almıyordu (çoğu 0 puan):
  anahtarlar cümle hâlindeydi, çekim farkı (`weigeren`/`weigerden`), ayrılabilir fiil (`neemt … toe`), `|`
  ile ayrılmış alternatif (motor yalnız `/` tanır), `m/s²` gibi `/` içeren birim (alternatif ayırıcı sanılır).
- **Soru metnini yapıştırmak 0 puan almalı** (anahtar zaten soruda geçiyorsa yankı puanı). Alıntılı
  okuduğunu anlama soruları (`Lees: '…'` ya da 6+ kelimelik alıntı) muaf: cevap tanım gereği metinde.

## `pdf_check.py` — kitap PDF'i kalite kapısı (2026-09-13)

```bash
python3 tools/pdf_check.py inbox/2026-2027/frans/*.pdf   # sayfa sayfa sınıflandır + kontak sayfası
python3 tools/pdf_check.py --index                        # inbox/2026-2027/PDF_INDEX.md'yi yeniden yazar
```

Her sayfayı `BOS` / `ISKELET` (yükleniyor) / `MENU` (yalnız açık okuyucu menüsü) / `ARAYUZ` (reader
arayüzü görünüyor) / `KOPYA` (bir öncekinin aynısı) / `OK` olarak sınıflandırır; sorun varsa exit 1.
Yanlış alarmlar (benzer cevap tabloları, renkli başlıklı "Overzicht" sayfaları, kapak/künye) gözle
kontrol edilip `tools/pdf_check_onay.json`'a **sayfa sayfa** yazılır; indeks onları "✅ gözle onaylı" gösterir,
listede olmayan yeni bir işaret yine ❌ olur. Kitap sayfa aralığı `noordhoff_books.json`'dan gelir
(duits: Deel A/B, sayfa numaraları iki ciltte yeniden başlar → `A:16-55`, `B:16-55`).
Kitap materyalinden içerik üretmeden önce PDF ✅ olmalı: 1 Eylül'de frans'ın 40 sınavı %100 boş
PDF'lerle üretildi. Noordhoff kitapları yalnız `tools/noordhoff_export.py` + `noordhoff_books.json` ile
çekilir (eski `export_*` betikleri yerine; tarayıcı profili kilitli → tek süreç, sıralı).

## `test_score_merge.js` — skor birleştirme regresyon testi

```bash
node tools/test_score_merge.js                 # js/landing.js'e karşı
node tools/test_score_merge.js <baska/landing.js>
```

Soru kalitesiyle ilgisi yok; **Duru'nun kayıtlı geçmişini** korur. `restoreScores()` ve
`parseAttemptDate()`'i `js/landing.js`'ten harfi harfine kesip sahte bir `localStorage`
üzerinde çalıştırır ve tek bir kuralı ölçer: **birleştirme büyüyebilir, asla küçülemez.**

17 kontrol: XP/streak/pogingen/beste `max` ile korunuyor mu, madalyalar union mu, uzaktan gelen
yeni değer alınıyor mu, `history` union'lanıp tekilleniyor mu, `beste` yeniden hesaplanıyor mu,
bozuk yerel JSON çökme yerine kurtarılıyor mu — **ve yazma yönünde**: fakir bir yerel bulutu
soyabiliyor mu, `mergeScoreItems()` gerçekten saf mı (localStorage'a dokunmuyor mu).

2026-09-20'de bu testin koruduğu hata 865 XP + 4 madalya + 199 poging'e mal oldu — ayrıntı
`CLAUDE.md` → "Bulut senkron & birleştirme değişmezi". Senkron/merge koduna dokunan her
değişiklikten sonra çalıştır.

## `test_server_merge.py` — sunucu tarafı aynı değişmez

```bash
python3 tools/test_server_merge.py
```

`server.py → voeg_samen()` aynı hatayı taşıyordu: sınav geçmişini birleştiriyor ama **ilerleme
anahtarlarında "son yazan kazanır"** uyguluyordu. Yani fakir bir istemci, kurtarmayı borçlu
olduğumuz `scores.json`'u da soyabilirdi. 15 kontrol; onarım öncesi kodda 865 XP → 95 düşüyor.

**İki testi birlikte çalıştır** — değişmez üç yerde de aynı:
`node tools/test_score_merge.js && python3 tools/test_server_merge.py`

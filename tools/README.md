# tools/ — soru kalite denetimi

Üretilen soru dosyalarının **kalite** denetimi. `node --check` ve alan kontrolü yetmiyor:
2026-08-27/28'de geschiedenis'te (840 soru) ve scheikunde'de yakalanan kusurlar bu araçlarla
bulundu. Sözleşme: `docs/ENGINE_SPEC.md`. Kural listesi: `docs/PIPELINE.md` → "Kalite kapısı".

## `gate.js` — kabul kapısı (16 kontrol: 1–15, 5 = 5a/5b)

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
| 14 | `invul` sorusunda cevap `[köşeli parantez]` içinde soruda yazmıyor |
| 15 | `waaronwaar`: `uitleg` cevapla çelişmiyor ("Onwaar: Waar." / uitleg "Waar." ama antwoord `false`) |

12–15 2026-09-12 denetiminde eklendi: 1–11'i geçen teslimlerde (natuurkunde, economie, wiskunde,
scheikunde) 101 LaTeX, 36 bozuk metin, 97 cevabı görünen `invul` ve 38 çelişkili `waaronwaar` vardı.
Yeni kurallar düzeltme öncesi yedekte bunların hepsini yakaladı, 12 derste yanlış alarm vermedi.

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


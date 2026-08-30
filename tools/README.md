# tools/ — soru kalite denetimi

Üretilen soru dosyalarının **kalite** denetimi. `node --check` ve alan kontrolü yetmiyor:
2026-08-27/28'de geschiedenis'te (840 soru) ve scheikunde'de yakalanan kusurlar bu araçlarla
bulundu. Sözleşme: `docs/ENGINE_SPEC.md`. Kural listesi: `docs/PIPELINE.md` → "Kalite kapısı".

## `gate.js` — kabul kapısı (12 kural)

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
| 8 | Soru yapısı sözleşmeye uygun (mc index, boolean, `minTreffers` ≤ sleutelwoord sayısı, `open`'da cevap sızıntısı yok) |
| 9 | Soru sayıları (onderwerp 8 / proeftoets 20) |
| 10 | `theorie` ≥ 1500 karakter |
| 11 | Her data dosyası `index.html`'e bağlı, her referans mevcut |

Çıkış kodu: ihlal varsa 1. 9 ve 10 numaralı kurallar **hedef**tir, dersin brief'inde farklı bir
ölçü verildiyse ihlal sayılmayabilir — raporu okurken bunu ayırt et.

## `spread.py` — doğru şık dağıtımı

```bash
python3 -c "import sys; sys.path.insert(0,'tools'); import spread; print(spread.spread_file('havo3/<vak>/js/data/examen_1.js'))"
```

Doğru cevabı dosya içinde sırayla A→B→C→D pozisyonlarına taşır, `antwoord` index'ini günceller.
**Soru metnine, şık metnine, `uitleg`'e dokunmaz** — yalnız sıra değişir.

`spread_file()` kullan: iki dosya biçimini (çok satırlı `opties: [` ve tek satırlık
`opties: [...]`) **tek sayaçla** işler. Eski `process()`/`process_inline()` ayrı sayaç tuttuğu
için karışık biçimli dosyalarda dağılımı tam oturtmuyor.

## `open_check.js` — `open` sorularda puanlanabilirlik

```bash
node tools/open_check.js
```

Tüm dersleri tarar. Motor (`exams.js`) `sleutelwoorden`'i `tekst.indexOf(alternatif)` ile
**birebir alt-dizi** olarak arar. Dolayısıyla:

- `sleutelwoord` **1–3 kelimelik terim** olmalı (`"kernafval"`, `"turbine"`), alternatifler `/` ile.
- 6–12 kelimelik cümle yazılırsa öğrenci onu harfiyen yazmadıkça **doğru cevap 0 puan** alır.
- Uzun açıklama `modelantwoord`'a yazılır, `sleutelwoorden`'e değil.
- `minTreffers` ≤ sleutelwoord sayısı olmalı; aksi hâlde soru asla "goed" olamaz.
- Anahtara `"voordeel:"` gibi önek koyma — öğrenci öyle yazmaz.

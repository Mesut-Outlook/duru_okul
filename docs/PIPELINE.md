# PIPELINE.md — Belge → Sınav üretim hattı + model/agent politikası

> Duru bir hoofdstuk/paragraaf bitirdiğinde: okul materyalini (PDF / Word / görsel) veriyoruz,
> uygun model analiz edip DURU sözleşmesine (`docs/ENGINE_SPEC.md`) uygun sınav/oefen üretiyor.

## Roller
- **Opus (planlama — ben):** Her zaman planı ben yaparım. Kaynağı analiz eder, kapsamı (hoofdstuk/
  paragraaf) belirler, soru dağılımını kararlaştırır, görev-spec'i `coordination.md`'ye yazar,
  üretilen çıktıyı **doğrular**, dokümanları günceller.
- **agy (Google Antigravity):** `coordination.md`'yi ~15 dk'da bir yoklar, "Pending Tasks"ten iş
  çeker, üretir, sonucu ve durumu aynı dosyaya geri yazar. Ben doğrudan çağırmam — dosya üzerinden
  emir veririm. Mevcut örnek: `nederlands/begrijpend-lezen/generate_exam_agy.py` (Antigravity SDK + Gemini).
- **Sonnet / Haiku alt-agent'ları:** Token tasarrufu için mekanik/hacimli üretim (çok sayıda benzer
  soru dosyası, tek bir data dosyasının doldurulması) bunlara verilir. Basit/tekrarlı = Haiku,
  muhakeme gereken içerik = Sonnet.

## Model seçim kılavuzu
| İş | Model |
|---|---|
| Planlama, kapsam kararı, mimari, doğrulama | **Opus** (her zaman) |
| Kaynak PDF/görsel analizi (kavram çıkarımı) | Sonnet (görsel/muhakeme) |
| Hacimli soru/data dosyası yazımı | Sonnet 5 veya Haiku (basitse) |
| Otomatik, şemaya-bağlı toplu üretim | agy (Antigravity/Gemini) |

## Belge teslim yolları (ikisi de geçerli)
1. **`inbox/` klasörü** — dosyayı `inbox/<schooljaar>/<vak>/` altına koy, kanonik adla
   `<vak>_h<NN>_<slug>.pdf` (bkz. `inbox/README.md`).
2. **Sohbet yüklemesi** — dosyayı doğrudan sohbette ver.

## Akış
1. **Al & analiz et** — kaynağı oku (PDF çok sayfalıysa PyMuPDF ile PNG'ye render → görsel oku).
   Kavramları, formülleri, tanımları çıkar. (Opus planlar; analizi Sonnet'e verebilir.)
2. **Kapsamı sabitle** — hangi hoofdstuk/paragraaf, kaç soru, tip dağılımı. Örn. bir "extra" sınav
   = ~15 soru (6 mc / 4 waaronwaar / 3 invul / 2 open); tam proeftoets ~20–24 soru.
3. **Görevi yaz** — `coordination.md`'ye net spec + kabul kriterleri (dosya adı, id şeması, kapsam,
   soru sayısı, "MEMORY.md güncellendi").
4. **Üret** — agy veya alt-agent, `docs/ENGINE_SPEC.md`'ye birebir uyan **tek register çağrılı**
   `js/data/*.js` dosyaları yazar. **KARARLI id** kuralına uy (mevcut id'yi değiştirme).
5. **Doğrula (zorunlu)** — `node` ile `DURU.register`/`registerExamen` stub'layıp dosyaları `eval`
   ederek söz dizimi + alan kontrolü. `index.html`'e `<script>` doğru grupta eklendi mi?
6. **Bağla & yayınla** — `index.html`'e ekle, gerekiyorsa `?v=` bump. Dashboard'a yeni ders
   ekleniyorsa 6 dokunma noktası (bkz. kök `CLAUDE.md` "Ders ekleme").
7. **Belgele** — ilgili `MEMORY.md` + `coordination.md` güncelle; görevi "Done"a taşı.

## Kalite kapısı (zorunlu — 2026-08-28'den beri)
`node --check` + alan kontrolü **yetmez**. Geschiedenis'te 840 soruluk bir teslim sözdizimi olarak
kusursuzdu ama içerik olarak çöptü. Her teslim `tools/gate.js` ile ölçülür (ayrıntı: `tools/README.md`).

**Üretirken uyulacak kurallar** (kabul kriterlerine bunları yaz):
1. **Doğru şık dağılımı** — bir dosyadaki mc sorularının hiçbir şık pozisyonu %40'ı geçmesin ve
   **döngü kurmasın** (0,1,2,3,0,1,… de tahmin edilebilir; 2026-09-13'te 12 derste bulundu).
   (Geschiedenis'te 500/500 "A", scheikunde'de 4 toetsin tamamı "A" idi → bilmeden %95.)
   Bozuksa `tools/spread.py` → `spread_file()` düzeltir (yalnız YAYINLANMAMIŞ dosyada). Sınav motoru
   şıkları zaten her denemede karıştırır (`exams.js → optieVolgorde`).
2. **`waaronwaar` ≥ %35 `false`** — hep "Waar" olursa "hep Waar de geç" %90 getirir.
3. **Sınavda `invoer` yasak** — `exams.js` bu tipe girdi alanı çizmez, soru cevaplanamaz ve
   otomatik yanlış sayılır. Sınav = `invul`, oefenquiz = `invoer`.
4. **Şablon dolgu soru yasak** — konu adını boşluğa yapıştıran kalıplar hiçbir şey ölçmez.
5. **Proeftoetsler birbirinin kopyası olmasın**; aynı soru iki dosyada geçmesin.
6. **Paragraf numarası/başlığı kaynaktan** alınır, uydurulmaz. (25 başlık uydurulmuştu; hepsi
   yeniden yazıldı.)
7. **`open` sorularda `sleutelwoorden` = 1–2 kelimelik terim/kök**, cümle değil; alternatifler yalnız `/`
   ile (`|` DEĞİL); `minTreffers` ≤ grup sayısı; hiçbir alternatif soru metninde geçmesin.
   **`modelantwoord` kendi anahtarlarıyla tam puan almalı, soruyu yapıştırmak 0 almalı** —
   `node tools/open_check.js` 0 ihlal vermeden teslim yok (2026-09-13: ~147 soru örnek cevabını reddediyordu).
8. **Her soruda dolu `uitleg`**; soru metnine numara öneki koyma.
9. **Çok satırlı string yok** — çift tırnaklı JS string'i gerçek satır sonu içeremez; `\n` kaçışı
   ya da backtick kullan. (Bu hata üç kez dosya bozdu.)
10. **Teslimden önce her dosyada `node --check`.**
11. **LaTeX yok** — projede KaTeX/MathJax yok; `$F_{res} = 0\text{ N}$` öğrenciye aynen görünür.
    Düz metin + HTML yaz: `F<sub>res</sub> = m × a`, `m/s²`, `Δv`, `t<sub>½</sub>`. Sınavda `opties` ve
    `modelantwoord` escape edilir → orada `<sub>` de çalışmaz, `Fres`/`F₁` gibi düz yaz. (Kapı: 12)
12. **Üreteç script'inde `$` içeren metni shell heredoc'a / çift tırnağa koyma.** Shell `$1`, `$4`,
    `$0`, `$$`, `$F_z` ifadelerini değişken sanıp yutar: `$10\text{ Nm}$` → "0 Nm", `$0{,}30` →
    "bash{,}30", `$$` → işlem numarası "89565". natuurkunde'de 35 metin böyle bozuldu, bazılarında
    **sayı yanlış** kaldı. Veriyi Python/JS dosyasından yaz, shell'den geçirme. (Kapı: 13)
13. **`invul` sorusunda cevabı soruya yazma** — `"heet de [restwaarde]."` motor tarafından boşluğa
    çevrilmez, cevap ekrana basılır. Boşluk `____` ile gösterilir. (economie'de 87 soru; kapı: 14)
14. **Kapıyı geçmek için `waaronwaar` cevabını çevirme.** %35 onwaar barajı için ifade **gerçekten
    yanlış** olacak şekilde yeniden yazılır; doğru bir ifadenin `antwoord`'unu `false` yapıp uitleg'e
    "Onwaar: Waar." eklemek Duru'ya **yanlış bilgi öğretir** (natuurkunde'de 28 soru; kapı: 15).
15. **`open` sayı anahtarı noktasız biçimle birlikte** — nakijken `"21.000"`'i `"21 000"`'e çevirir;
    `21000` yazan öğrenci kaçar. `"21.000/21000"` yaz. (Kapı: 8)

## 📌 "Test Hazırla" ve Bölüm Üretimlerinde Zorunlu Kavram / Terim Standardı (2026-08-30)
Kullanıcı **"test hazırla"** dediğinde veya herhangi bir ders için yeni bir bölüm/hoofdstuk işlendiğinde **otomatik olarak** şu adımlar uygulanır:

1. **Her Ders ve Her Hoofdstuk İçin Ayrı Ayrı Kavram Çıkarımı**:
   - **Begrippen & Definities**: O bölümdeki tüm temel terimler, tanımlar ve kavramlar.
   - **Belangrijke Personen**: Bilim insanları, tarihi kişilikler, önemli aktörler.
   - **Belangrijke Gebeurtenissen & Data / Wetten**: Önemli olaylar, antlaşmalar, dönüm noktaları, kanunlar veya deneyler.
   - **Examen-sleutelwoorden**: Sınavda çıkabilecek tüm kritik anahtar kelimeler ve formüller.

2. **Özel Bölüm / Onderwerp Modülü (Begrippen & Kernconcepten)**:
   - Her Hoofdstuk bünyesinde tüm bu terimleri, kişileri ve olayları derleyen özel bir konu anlatımı/sözlük bölümü (`formule-box`, `info-box`, tablolar ile yapılandırılmış) eklenir.

3. **Özel Kavram Testi (Begrippentoets — Sadece Bu Kelimeleri Soran Sınav)**:
   - **Sadece bu kelimeleri/kavramları/kişileri/olayları** sorgulayan özel bir sınav (Proeftoets: Begrippen & Personen) hazırlanır.
   - Soru tipleri:
     - `mc`: Tanımı verilen kavramı veya rolü verilen kişiyi bulma.
     - `invul`: Cümledeki boşluğa doğru terimi, kişiyi veya olayı yazma.
     - `open`: Temel terimin veya olayın anlamını 1-3 kelimelik anahtar kelimelerle açıklama.

## Doğrulama örneği (node stub)
```bash
node -e 'global.DURU={register:()=>{},registerExamen:()=>{}};
require("./<vak>/js/data/examen_XX.js"); console.log("OK")'
```
(Dosyalar tarayıcı globali beklediği için stub şart; hata yoksa söz dizimi sağlam.)


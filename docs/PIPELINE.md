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
1. **`inbox/` klasörü** — dosyayı `inbox/<vak>/<hoofdstuk>/` altına koy (bkz. `inbox/README.md`).
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
1. **Doğru şık dağılımı** — bir dosyadaki mc sorularının hiçbir şık pozisyonu %40'ı geçmesin.
   (Geschiedenis'te 500/500 "A", scheikunde'de 4 toetsin tamamı "A" idi → bilmeden %95.)
   Bozuksa `tools/spread.py` → `spread_file()` düzeltir.
2. **`waaronwaar` ≥ %35 `false`** — hep "Waar" olursa "hep Waar de geç" %90 getirir.
3. **Sınavda `invoer` yasak** — `exams.js` bu tipe girdi alanı çizmez, soru cevaplanamaz ve
   otomatik yanlış sayılır. Sınav = `invul`, oefenquiz = `invoer`.
4. **Şablon dolgu soru yasak** — konu adını boşluğa yapıştıran kalıplar hiçbir şey ölçmez.
5. **Proeftoetsler birbirinin kopyası olmasın**; aynı soru iki dosyada geçmesin.
6. **Paragraf numarası/başlığı kaynaktan** alınır, uydurulmaz. (25 başlık uydurulmuştu; hepsi
   yeniden yazıldı.)
7. **`open` sorularda `sleutelwoorden` = 1–3 kelimelik terim**, cümle değil; `minTreffers` ≤
   sleutelwoord sayısı; anahtar soru metninde geçmesin. Gerekçe ve tarama: `tools/open_check.js`.
8. **Her soruda dolu `uitleg`**; soru metnine numara öneki koyma.
9. **Çok satırlı string yok** — çift tırnaklı JS string'i gerçek satır sonu içeremez; `\n` kaçışı
   ya da backtick kullan. (Bu hata üç kez dosya bozdu.)
10. **Teslimden önce her dosyada `node --check`.**

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


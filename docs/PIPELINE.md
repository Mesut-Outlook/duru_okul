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

## Doğrulama örneği (node stub)
```bash
node -e 'global.DURU={register:()=>{},registerExamen:()=>{}};
require("./<vak>/js/data/examen_XX.js"); console.log("OK")'
```
(Dosyalar tarayıcı globali beklediği için stub şart; hata yoksa söz dizimi sağlam.)

# inbox/ — Ders materyali bırakma alanı

Duru bir hoofdstuk/paragraaf bittiğinde okul materyalini (PDF / Word / görsel) buraya koy;
ben (Opus) okuyup planlar, uygun modelle sınav/oefen üretiriz. Ayrıntı: `../docs/PIPELINE.md`.

## Nasıl kullanılır
Dosyayı ders + hoofdstuk'a göre bir alt klasöre koy:
```
inbox/<vak>/<hoofdstuk>/   ör. inbox/geschiedenis/h1/  ·  inbox/nask/h2-krachten/
```
İstersen dosyayı doğrudan sohbete de yükleyebilirsin — ikisi de çalışır.

## İpuçları
- Dosya adına kapsamı yaz: `h1_par1-3_hoorcollege.pdf`, `toets-info_h2.jpg`.
- Birden fazla bölümden sorumlu bir sınav varsa hepsini aynı klasöre koyup not düş.
- Buradaki dosyalar **kaynak**tır; üretilen sınavlar ilgili `havo3/<vak>/js/data/` altına yazılır.
- İşlenen materyali `inbox/_verwerkt/` altına taşıyıp izini `coordination.md`'de tutarım.

> Not: Bu klasör git'e commit edilebilir (kaynak arşivi) ya da `.gitignore`'a alınabilir —
> telif/boyut durumuna göre karar `coordination.md`'de not edilir.

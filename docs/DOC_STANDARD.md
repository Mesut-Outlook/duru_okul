# DOC_STANDARD.md — Ortak dokümantasyon yapısı

> Projedeki tüm `CLAUDE.md` / `MEMORY.md` / `SPEC.md` dosyaları bu standarda uyar.
> Amaç: dağınık (Flamanca/İngilizce/Türkçe karışık, farklı başlıklı) dosyaları **tek bir
> tutarlı iskelete** oturtmak. Bir geliştirme yapıldığında ilgili dosya bu şablona göre güncellenir.

## Dil kuralı
- **Geliştirici/koordinasyon dokümanları (`CLAUDE.md`, `MEMORY.md`, `coordination.md`, `docs/*`): Türkçe.**
- **Öğrenci-içeriği (theorie, sorular, uitleg): Flamanca** (bkz. `docs/ENGINE_SPEC.md`).
- Kod tanımlayıcıları ve localStorage anahtarları olduğu gibi (İngilizce/Flamanca).

## Dosya hiyerarşisi
```
/CLAUDE.md            Hub rehberi (bu repo genelinde AI + insan için giriş noktası)
/MEMORY.md            Global milestone günlüğü (kronolojik)
/coordination.md      Opus ↔ agy (Antigravity) canlı görev panosu + protokol
/docs/
  ENGINE_SPEC.md      DURU veri sözleşmesi (kanonik; SPEC.md'ler buna işaret eder)
  DOC_STANDARD.md     bu dosya
  PIPELINE.md         belge → sınav üretim hattı + model/agent politikası
<vak>/CLAUDE.md       o dersin rehberi (aşağıdaki şablon)
<vak>/MEMORY.md       o dersin milestone günlüğü
<vak>/SPEC.md         (opsiyonel) derse özgü sapmalar; yoksa ENGINE_SPEC yeterli
```

## Şablon — `<vak>/CLAUDE.md`
Sabit başlık sırası (nask/economi zaten buna yakın):
```
# CLAUDE.md — <Ders adı> (HAVO 3)
> 1–2 satır: ne, kim için (Duru, HAVO 3), dil kuralı, kanonik sözleşme = ../docs/ENGINE_SPEC.md
## Ne işe yarar          — bölümler/paragraaflar, kaç proeftoets, oyunlaştırma
## Dosya haritası        — klasör içeriği (script sırası ENGINE_SPEC'te)
## localStorage anahtarları — bu dersin slug'ı (duru_h3_<vak>_v1 / _examens_v1)
## Kapsam disiplini      — sınavlar hangi hoofdstuk/paragraaf ile SINIRLI (ÖNEMLİ)
## Yeni içerik ekleme    — kısa; ayrıntı docs/PIPELINE.md
## Konu özeti            — formüller/kavramlar (hızlı referans)
```

## Şablon — `<vak>/MEMORY.md` ve kök `MEMORY.md`
Kronolojik milestone günlüğü. Her giriş:
```
### Milestone N: <başlık> (YYYY-AA-GG)
* **Hedef**: ...
* **Sonuç**: ne değişti, hangi dosyalar, hangi kararlar.
* **Kim**: Opus (plan) / Sonnet-Haiku alt-agent / agy (Antigravity) — kim yaptı.
```
Göreli tarih yazma; her zaman mutlak tarih (YYYY-AA-GG).

## Güncelleme disiplini
- Her geliştirmeden **sonra**: ilgili `<vak>/MEMORY.md` (veya kök) + gerekiyorsa `<vak>/CLAUDE.md`
  güncellenir; `coordination.md`'deki görev "done"a taşınır.
- Sözleşme değişikliği → SADECE `docs/ENGINE_SPEC.md`'de (kopyalarda değil).
- Kararı kim uygularsa (Opus / alt-agent / agy) güncellemeyi de o yapar; agy'ye verilen görevin
  "kabul kriterleri"ne "ilgili MEMORY.md güncellendi" maddesi eklenir.

# Coordination Log & Task Queue — Opus ↔ agy (Antigravity)

Bu dosya, planlayan (**Opus** — ben) ile üreten (**agy** = Google Antigravity) arasındaki
**tek iletişim kanalıdır**. Opus buraya görev + kabul kriteri yazar; agy ~15 dk'da bir yoklar,
işi yapar, sonucu ve durumu buraya geri yazar. Politika: `docs/PIPELINE.md`.

## Current Status
- **Last Checked**: 2026-07-20 17:00 (Iteration 4/4 - Final)
- **Status**: Standby (4 idle iterations completed with no tasks for agy. Waiting for user/Opus to add new tasks)
- **Schedule**: Standby (Resets when a new task is assigned or requested)

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

## Pending Tasks
*(agy: yalnızca "Atanan: agy" görevlerini al. Şu an sana ait görev YOK — HAVO 3 dersleri Duru
materyal verince açılacak. Boş turlarda standby'a geçebilirsin.)*

*(Şu an açık görev yok.)*

## Done
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

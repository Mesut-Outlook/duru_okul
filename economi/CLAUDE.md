# CLAUDE.md — Duru's Economie Academie

Rehber: bu repo üzerinde çalışan Claude Code (ve insan geliştiriciler) için. Proje,
Mesut'un 14 yaşındaki kızı **Duru** için (Hollanda, MAVO 2) yapılmış Hollandaca bir
**economie / maatschappijleer** öğrenme ve sınav-hazırlık sitesidir. Konu:
**Hoofdstuk 6 — De overheid** (devlet/kamu yönetimi & maliye).

> Kardeş proje: `_PROJELER/Duru_Nask` (natuurkunde). Bu site onun framework'ünden türetildi;
> aynı motor, farklı içerik. **localStorage anahtarları ayrı** (aşağıya bak).
> Dil kuralı: **Tüm öğrenci-içeriği Hollandaca'dır**. Ondalık ayraç metinlerde **virgül** (€ 21,50).

## Ne işe yarar
- Tek bölüm: **Hoofdstuk 6 — De overheid**, 4 paragraaf:
  - 6.1 Wie is de overheid? (Rijk / provincie / gemeente, Den Haag)
  - 6.2 Waar zorgt de overheid voor? (collectieve voorzieningen)
  - 6.3 Betalen aan de overheid (belastingen: inkomsten-, loon-, btw)
  - 6.4 Is de schatkist goed gevuld? (rijksbegroting, tekort, staatsschuld)
- Her paragraaf: theorie (konu anlatımı) + bol oefenquiz (anında geri bildirim).
- Ayrıca **proeftoetsen** (deneme sınavı): süreli, cijfer 1–10, sonunda "nakijken / zo doe je het".
- Oyunlaştırma: XP 💎, streak 🔥, rozetler 🏅.

## Teknoloji & çalıştırma
- **Saf HTML/CSS/JS. Build yok, bağımlılık yok, framework yok.** ES5/ES6.
- ES module KULLANMA — `file://` üzerinde CORS sorunu çıkar. Global `window.DURU` +
  sıralı `<script>` yüklemesi kullanılır.
- Çalıştırma: `Duru_Economi_Baslat.command` (python `http.server :8124`) veya doğrudan `index.html`.
  Port **8124** (NASK 8123 ile çakışmasın).

## Dosya haritası
```
index.html                 Kabuk; <script> sırası burada (ÖNEMLİ, aşağıya bak)
css/style.css              Tüm tasarım sistemi + sınav modu stilleri
js/bootstrap.js            window.DURU + register()/DURU.hoofdstukken (TEK hoofdstuk: 6)
js/engine.js               Oefen-motoru: routing, voortgang, quiz, confetti
js/exams.js                Sınav (proeftoets) motoru: timer, cijfer, review
js/data/h6_*.js            Onderwerpen (konu + sorular) — DURU.register({...})
js/data/examen_*.js        Proeftoetsen — DURU.registerExamen({...})
SPEC.md                    Data dosyası sözleşmesi (yeni onderwerp eklerken UY)
extracted_pages/           Economi 6.pdf'in render edilmiş sayfaları (REFERANS; .gitignore)
```

### Script yükleme sırası (index.html) — bozma!
`register`/`registerExamen`, data dosyaları çalışmadan ÖNCE var olmalı:
1. `bootstrap.js`  → `DURU`, `DURU.register`, `DURU.hoofdstukken`
2. `exams.js`      → `DURU.registerExamen`, sınav motoru
3. `data/examen_*.js`
4. `data/h6_*.js`  (onderwerp verileri)
5. `engine.js`     → en son; `DOMContentLoaded`'da `renderHome()`

## İki veri sözleşmesi
Ayrıntı **SPEC.md**'de. Özet:
- `DURU.register({ id, hoofdstuk:6, paragraaf, titel, korteUitleg, icoon, theorie:`<HTML>`, vragen:[...] })`
- vraag tipleri: `mc` (antwoord=index), `waaronwaar` (antwoord=bool), `invoer` (antwoord=string, sayısal).
- `DURU.registerExamen({ id, titel, vak, icoon, duurMin, vragen:[...] })`; ek tipler: `open`, `invul`.

## localStorage anahtarları (DİKKAT — karıştırma!)
- `duru_economi_v1`          → oefen-ilerlemesi: XP, streak, rozetler, en iyi quiz skorları.
- `duru_economi_examens_v1`  → proeftoets skorları (ayrı!). Sınav motoru oefen-XP'ye dokunmaz.
- NASK'ın `duru_nask_*` anahtarlarıyla **asla** karışmamalı.

## Yeni içerik ekleme
- **Yeni onderwerp:** SPEC.md'ye uygun `js/data/h6_*.js` yaz → `index.html`'de 4. gruba `<script>` ekle.
- **Yeni proeftoets:** `js/data/examen_*.js` yaz (`registerExamen`) → `index.html`'de 3. gruba `<script>` ekle.
- Hızlı doğrulama: `node` ile `register`/`registerExamen` stub'layıp dosyaları `eval` ederek
  söz dizimi + alan kontrolü yap.

### Kapsam disiplini (ÖNEMLİ)
- **Tüm proeftoetsen YALNIZCA Hoofdstuk 6 — De overheid (§6.1–6.4) kapsamında olmalı.** Müfredat
  dışı ekonomi konuları YASAK: ECB/monetair beleid, inflatie/deflatie/koopkracht, marktstructuren
  (monopolie/kartel), internationale handel/globalisering, arbeidsmarkt, privatisering,
  consumentenrecht, circulaire economie. (2026-06-18'de bu konulardaki 11 "extra" sınav kaldırılıp
  yerlerine H6-içi sınavlar yazıldı.)
- Toplam **35 proeftoets** (`examen_1..35`); dosya-numarası slot'ları sabit, "Extra Proeftoets N"
  görünen numarası = dosya no − 5 (boşluksuz 1–30). `ex-*` ID'leri kayıtlı skor geçmişinin anahtarı —
  mevcut bir sınavın ID'sini ASLA değiştirme; sadece dosya içeriğini değiştir veya slot'u yeni ID ile
  yeniden kullan. Her "extra" sınav = 15 soru (6 mc / 4 waaronwaar / 3 invul / 2 open).

## Bu proje nasıl üretildi (bağlam)
- Kaynak: iCloud'daki taranmış `Economi 6.pdf` (12 sayfa, metin katmanı yok). PyMuPDF ile
  PNG'ye render edilip görsel okundu (`extracted_pages/h6_p01..12.png`).
- **Planlama Opus 4.8 ile, tüm kod yazımı Sonnet alt-agent'ları ile** yapıldı; içerik dosyaları
  paralel sub-agent'larca her biri ayrı dosyaya yazıldı (NASK projesindeki yöntemle aynı).
- Görseller telifsiz olsun diye **inline SVG** ile çizildi (overheid-lagen, belastingstroom, begroting).

## Konu özeti (kavramlar)
overheid = Rijk (Den Haag) + provincie + gemeente · collectieve voorzieningen = overheid herkes için
regelt (veiligheid, infrastructuur, onderwijs, zorg) · belasting: inkomstenbelasting & loonbelasting
(direct), btw (indirect, standaard 21%, laag 9%) · rijksbegroting = inkomsten vs uitgaven ·
uitgaven > inkomsten → begrotingstekort → lenen → staatsschuld · Prinsjesdag = miljoenennota/begroting.

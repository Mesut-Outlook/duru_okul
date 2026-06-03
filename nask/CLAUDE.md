# CLAUDE.md — Duru's NASK Academie

Bu dosya, gelecekte bu repo üzerinde çalışan Claude Code (ve insan geliştiriciler) için
rehberdir. Proje, Mesut'un 14 yaşındaki kızı **Duru** için (Hollanda, MAVO 2) yapılmış
Hollandaca bir **natuurkunde (NASK / fizik)** öğrenme ve sınav-hazırlık sitesidir.

> Dil kuralı: **Tüm öğrenci-içeriği Hollandaca'dır** (konu anlatımı, sorular, geri bildirim).
> Kod yorumları Hollandaca/Türkçe karışık olabilir. Ondalık ayraç metinlerde **virgül** (13,4 m/s).

## Ne işe yarar
- İki bölüm: **Hoofdstuk 4 — Snelheid** (hız) ve **Hoofdstuk 6 — Elektriciteit** (elektrik).
- Her başlık için: konu anlatımı (theorie) + bol alıştırma (oefenquiz, anında geri bildirim).
- Ayrıca **3 proeftoets (deneme sınavı)**: süreli, cijfer 1–10, sonunda "nakijken/zo doe je het" inceleme.
- Oyunlaştırma: XP 💎, streak 🔥, rozetler 🏅.

## Teknoloji & çalıştırma
- **Saf HTML/CSS/JS. Build yok, bağımlılık yok, framework yok.** ES5/ES6, her tarayıcıda çalışır.
- ES module KULLANMA — `file://` üzerinde CORS sorunu çıkar. Bunun yerine global `window.DURU`
  nesnesi + sıralı `<script>` yüklemesi kullanılır.
- Çalıştırma: `Duru_NASK_Baslat.command` (python `http.server :8123`) veya doğrudan `index.html`.
  Aynı ağdaki başka cihaz: `http://<mac-ip>:8123/index.html` (launcher IP'yi ekranda gösterir).

## Dosya haritası
```
index.html                 Kabuk; <script> sırası burada (ÖNEMLİ, aşağıya bak)
css/style.css              Tüm tasarım sistemi + sınav modu stilleri
js/bootstrap.js            window.DURU + register()/registerExamen-öncesi iskelet (EN ÖNCE yüklenir)
js/engine.js               Oefen-motoru: routing, voortgang, quiz (mc/waaronwaar/invoer), confetti
js/exams.js                Sınav (proeftoets) motoru: timer, navigatie, cijfer, review
js/data/h4_*.js, h6_*.js   Onderwerpen (konu + sorular) — DURU.register({...})
js/data/examen_*.js        3 proeftoets — DURU.registerExamen({...})
SPEC.md                    Oefen-data dosyası sözleşmesi (yeni onderwerp eklerken UY)
extracted_pages/           Kitabın taranmış sayfaları (REFERANS; .gitignore'da, repoda yok)
Deneme_Sinavi/             Sınav foto referansları (.gitignore'da, repoda yok)
```

### Script yükleme sırası (index.html) — bozma!
`register`/`registerExamen` fonksiyonları, data dosyaları çalışmadan ÖNCE var olmalı:
1. `bootstrap.js`  → `DURU`, `DURU.register`, `DURU.onderwerpen/hoofdstukken`
2. `exams.js`      → `DURU.registerExamen`, sınav motoru, `DURU.examens`
3. `data/examen_*.js`
4. `data/h4_*.js`, `data/h6_*.js` (onderwerp verileri)
5. `engine.js`     → en son; `DOMContentLoaded`'da `renderHome()`

## İki veri sözleşmesi
### 1) Onderwerp (oefenquiz) — ayrıntı `SPEC.md`
```js
DURU.register({
  id, hoofdstuk, paragraaf, titel, korteUitleg, icoon,
  theorie: `<HTML string>`,           // konu anlatımı (CSS sınıfları SPEC.md'de)
  vragen: [
    { type:"mc",        vraag, opties:[...], antwoord:<index>, uitleg, hint? },
    { type:"waaronwaar",vraag, antwoord:<bool>, uitleg },
    { type:"invoer",    vraag, antwoord:"15", eenheid?, tolerantie?, uitleg, hint? }
  ]
});
```
### 2) Proeftoets (sınav)
```js
DURU.registerExamen({
  id, titel, vak, icoon, duurMin,      // duurMin = geri sayım dakikası
  vragen: [
    { type:"mc",         vraag, opties:[...], antwoord:<index>, uitleg },
    { type:"waaronwaar", vraag, antwoord:<bool>, uitleg },
    { type:"open",       vraag, sleutelwoorden:["a/alt","b"], minTreffers:1,
                         modelantwoord, uitleg },   // otomatik: anahtar kelime sayar
    { type:"invul",      vraag, antwoord:"m/s|meter per seconde", uitleg },
    // her soruya opsiyonel: figuur:"<svg ...>"
  ]
});
```
`open` notu: `sleutelwoorden` içinde `/` = aynı sleutel için alternatif yazımlar; `minTreffers`
kaç tanesinin bulunması gerektiği. Tümü bulunursa "goed", `minTreffers`–tümü arası "deels" (yine puan).

## localStorage anahtarları (DİKKAT — karıştırma!)
- `duru_nask_v1`          → oefen-ilerlemesi: XP, streak, rozetler, en iyi quiz skorları.
- `duru_nask_examens_v1`  → sınav skorları (ayrı!). Sınav motoru oefen-XP'ye **dokunmaz**.
- İkisini ayrı tut. "Voortgang wissen" dışında hiçbir akış bunları silmemeli.

## Yeni içerik ekleme
- **Yeni onderwerp:** `SPEC.md`'ye uygun `js/data/h?_*.js` yaz → `index.html`'de 4. gruba `<script>` ekle.
  Hoofdstuk numarası `bootstrap.js`'teki `DURU.hoofdstukken`'de tanımlı olmalı.
- **Yeni proeftoets:** `js/data/examen_*.js` yaz (`registerExamen`) → `index.html`'de 3. gruba `<script>` ekle.
- Eklemeden sonra hızlı doğrulama: `node` ile `register`/`registerExamen` stub'layıp dosyaları
  `eval` ederek söz dizimi + alan kontrolü yap (geçmişte böyle test edildi).

## Bu proje nasıl üretildi (bağlam)
- Kaynak: iCloud'daki 3 taranmış PDF (H4 Snelheid, H6 Elektriciteit, 6.3 Serie/Parallel) +
  okuldan "Oefentoets H4" fotoğrafları. PDF'ler `pymupdf` ile PNG'ye render edilip görsel okundu.
- İçerik (konu + sorular ve 2 sınav) **farklı sub-agent'lar** tarafından, her biri ayrı dosyaya
  yazacak şekilde paralel üretildi; motor/iskelet/sözleşme elle kuruldu.
- Görseller telifsiz olsun diye taranmış sayfa yerine **inline SVG** ile yeniden çizildi
  (devre şemaları, hız-zaman grafikleri, formül üçgeni, schakelsymbolen).

## Konu özeti (formüller)
snelheid = afstand : tijd · km/u→m/s ÷3,6 · m/s→km/u ×3,6 · gemiddelde snelheid = totale afstand : totale tijd ·
reactieafstand = snelheid(m/s) × reactietijd · stopafstand = reactie + rem · 1 A = 1000 mA ·
voltmeter **parallel**, ampèremeter **serie** · serie: tümü söner / spanning verdeeld · parallel: volle spanning, apart.

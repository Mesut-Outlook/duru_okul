# 🧠 Proje Hafızası (Claude için kalıcı not)

Bu, Claude'un kişisel hafızasındaki proje notunun repoya kopyalanmış halidir; böylece
bilgi projeyle birlikte taşınır. (Asıl hafıza: `~/.claude/.../memory/duru-nask-academie.md`.)

---

`_PROJELER/Duru_Nask/` — Mesut'un 14 yaşındaki kızı **Duru** (Hollanda, MAVO 2) için
Hollandaca natuurkunde (NASK) oefensite. Sınav hazırlığı: konu anlatımı + bol quiz,
XP/streak/rozet oyunlaştırması.

**Kaynak:** iCloud `2. DURU DERSLER/Nask/` altındaki 3 taranmış PDF (Hoofdstuk 4 Snelheid,
Hoofdstuk 6 Elektriciteit, 6.3 Serie/Parallel) + okuldan "Oefentoets H4" fotoğrafları
(`Deneme_Sinavi/`). PDF'ler scan; `pymupdf` ile `extracted_pages/`'e PNG render edilip görsel okundu.

**Mimari:** saf HTML/CSS/JS, build yok, `file://` veya `Duru_NASK_Baslat.command` (python http.server :8123).
- `js/bootstrap.js` → `window.DURU` + `register()` (data scriptlerinden ÖNCE)
- `js/data/h*_*.js` → onderwerp: `DURU.register({id,hoofdstuk,paragraaf,titel,theorie(HTML),vragen[]})`
- `js/engine.js` → routing, voortgang (localStorage `duru_nask_v1`), quizmotor (mc/waaronwaar/invoer), confetti
- `js/exams.js` → AYRI sınav modu (timer, ileri-geri, cijfer 1-10, "nakijken/zo doe je het"). localStorage **`duru_nask_examens_v1`** → oefen-XP'ye DOKUNMAZ.
- `js/data/examen_*.js` → 3 proeftoets (`registerExamen`); type: mc/waaronwaar/open(sleutelwoorden+modelantwoord)/invul; 28'er soru.
- `SPEC.md` → oefen-data sözleşmesi · `CLAUDE.md` → tam mimari rehber.

**Üretim:** her başlık/sınav için ayrı sub-agent (Sonnet) Hollandaca içerik üretti, ayrı dosyaya yazdı;
motor/iskelet elle. Soru dili **Hollandaca**, ondalık virgül. Görseller inline SVG.

**Önemli formüller:** snelheid = afstand : tijd; km/u→m/s ÷3,6, m/s→km/u ×3,6;
gemiddelde snelheid = totale afstand : totale tijd; reactieafstand = snelheid(m/s) × reactietijd;
stopafstand = reactie+rem; 1 A = 1000 mA; voltmeter parallel, ampèremeter serie;
serie=hepsi söner/spanning verdeeld, parallel=volle spanning.

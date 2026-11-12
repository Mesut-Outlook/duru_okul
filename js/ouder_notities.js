/* =========================================================
   js/ouder_notities.js — handmatige analysenotities per vak voor het ouderpaneel
   ("Gelişim analizi"). Geschreven/bijgewerkt bij elke zwakte-analyse (skill
   zwakte-toetsen, stap 5) op basis van `python3 tools/zwakte.py <vak> --fouten`.
   Taal: Turks (ouderpaneel). ernst: hoog | mid | info | goed. Oude punten weghalen
   zodra ze opgelost zijn — dit is een momentopname, geen logboek.
   ========================================================= */
window.DURU_OUDER_NOTITIES = {
  wiskunde: { datum: "2026-11-08", punten: [
    { ernst: "hoog", tekst: "Bağlamlı parabol sorularını (sulama, top, tünel: başlangıç yüksekliği, cm, en yüksek nokta) neredeyse hep boş bırakıyor (%81–96)." },
    { ernst: "mid", tekst: "Tepe noktası verilen parabolün formülünü seçerken b'nin işaretini ve c = y-kesişimini karıştırıyor (%46)." },
    { ernst: "mid", tekst: "Üstel büyümede zaman birimi dönüşümünde (aylık ↔ yıllık) hata yapıyor (%48)." }
  ] },
  nederlands: { datum: "2026-11-08", punten: [
    { ernst: "hoog", tekst: "Samentrekking’de voorwaarts/achterwaarts'ı sistematik olarak ters yapıyor (son 10 testte 11 kez): kelimenin durduğu yere değil boşluğun yerine bakıyor." },
    { ernst: "hoog", tekst: "Açık 'verbeter + waarom' sorularında yalnız düzeltilmiş cümleyi yazıyor, nedenini hiç yazmıyor → hep yarım puan." },
    { ernst: "mid", tekst: "Verwijzen: 'het meisje die' (doğrusu dat), regering/gemeente/politie için 'zijn/hun' (doğrusu haar), eşyalar için 'het' (doğrusu hem); hun/hen karışık." },
    { ernst: "hoog", tekst: "Toets 72'yi üç kez aynı yanlış cevaplarla çözdü: sonuçtaki açıklamaları okumuyor. 'het meisje dat' (lidwoord karar verir, cinsiyet değil), eşyalar için 'hem', regering için 'haar' kurallarını birlikte konuşmak faydalı olur." },
    { ernst: "mid", tekst: "Prova sınavları (68–70): 10–14 / 20. Foutentraining 71–73: 9–16 / 20. 74–75 aynı hatalara farklı yoldan (adım adım, karşılaştırmalı) gidiyor." }
  ] },
  economie: { datum: "2026-11-12", punten: [
    { ernst: "mid", tekst: "§2.3 (19 test, son deneme ort. %79): reel gelir hesabında eksi işaretini unutuyor (−0,9 yerine 0,9) ve ücret/fiyat tablosunda en yüksek çubuğa bakıyor, farka (ücret − fiyat) bakmıyor." },
    { ernst: "mid", tekst: "Bestedingsinflatie'yi 'çok fazla arz' sanıyor (doğrusu: çok fazla talep/vraag); kosteninflatie ile karıştırıyor. CBS'in çok harcanan ürünleri 'daha ağır' saydığını ve enflasyonun bir ortalama olduğunu kaçırıyor." },
    { ernst: "mid", tekst: "CPB (koopkrachtplaatjes) ↔ CBS (enflasyonu ölçer) karışık; 'modaal' ve 'inflatiecijfer' boş. Açık soruların çoğu boş (53'ün 41'i). Yeni testler 116–120 bunlara gidiyor." },
    { ernst: "mid", tekst: "Yeni denemelerde (examen_96–100): euro tutardan yüzdeye geçemiyor (önce yeni−eski / eski × 100%, sonra enflasyonu çıkarmak gerekiyor); ücret ve fiyat ikisi de düşünce işareti karıştırıyor; formülü tersine kullanamıyor (nominal = reel + enflasyon); 7 − 5,5 yerine 7 + 5,5 = 12,5 topluyor; fiyat düşünce alım gücünün arttığını kaçırıyor. Testler 121–125 bunlara gidiyor; 116–120 henüz çözülmedi." },
    { ernst: "hoog", tekst: "116–125 çözüldü (§2.3 31 test, ort. %78). En zayıf: examen_122 — ücret ve fiyat ikisi düşünce −1 − (−4) yerine 5 yazıyor; 'enflasyonun %60'ı'nı 10 − 60 = −50 diye hesaplıyor; formülü tersine kullanamıyor (nominal = reel + enflasyon). Kitaptaki sayılar (1975, €38.000, %58) boş. 126–127 bunu daha küçük adımlarla (önce sadece eksi-eksi işlemi) çalıştırıyor; düzelmezse evde negatif sayı alıştırması gerekebilir." }
  ] },
  scheikunde: { datum: "2026-11-10", punten: [
    { ernst: "hoog", tekst: "Yoğunluk hesabında formülü ters kuruyor: V = m / ρ yerine çarpıyor (18 g / 24 cm³ → 432 yazdı); g/cm³ → kg/m³ için ×1000 yapmıyor (7,8 → 7,8); L ↔ cm³ dönüşümünü karıştırıyor (0,35 L → 35)." },
    { ernst: "mid", tekst: "°C ↔ K dönüşümünde yön/işaret hatası: 0 °C → −273, 4 K → 277, 21 °C → −252. Erime/kaynama noktası K ve °C karışık verilince maddenin halini bulamıyor." },
    { ernst: "mid", tekst: "Karışım türlerini karıştırıyor (nevel ↔ rook ↔ emulsie ↔ suspensie); 'çözelti hep renksizdir' sanıyor; emülgatörün çözelti yaptığını düşünüyor. Yeni testler h1-45…58 bunlara gidiyor." },
    { ernst: "mid", tekst: "H2 §2.1 (son 10 deneme): katı maddede moleküllerin 'tamamen durduğunu' sanıyor (doğrusu: yerinde titreşir), sublimeren ↔ condenseren karıştırıyor, triljoen = 18 sıfır (6/12 yazdı), mikro ↔ makro düzey karışık; açık soruların çoğu boş. Herhaling toetsen h1-59…60, h2-62…67 bunlara gidiyor." }
  ] },
  geschiedenis: { datum: "2026-11-10", punten: [
    { ernst: "hoog", tekst: "H1 kronolojisi zayıf: Versailles 1919, Türkiye 1923, Kanlı Pazar 1905, SSCB 1922 gibi yılları karıştırıyor; Sarajevo suikastine '11 november 1918' yazdı (karışık test 34: 20 sorudan 9'u yanlış)." },
    { ernst: "mid", tekst: "Benzer adları karıştırıyor: Volkenbond ↔ Vrede van Versailles, Brest-Litovsk ↔ Versailles, tsaar ↔ Lenin, Marne ↔ Somme." },
    { ernst: "mid", tekst: "Kavramları kendi kelimesiyle yazıyor ama kabul edilmiyor: 'op de bon' (distributiestelsel), 'illegale' (zwarte markt), 'prikkeldraad' (elektrocutie). Yeni testler 46–65 bunlara gidiyor." },
    { ernst: "mid", tekst: "10 Kasım akşamı 10 denemeyi 25 dakikada yaptı (deneme başı 2–3 dk); toets 43'ü üst üste 4 kez çözdü (7→12→12→17/20) — ezber/tahmin olabilir. §1.4 en zayıf: Kemal 'sultan' (doğrusu president), Anatolië, Hongarije, Baltische staten, Poolse Corridor, goudmarken. Herhaling toetsen 66–75 bunlara gidiyor." }
  ] }
};

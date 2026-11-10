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
  scheikunde: { datum: "2026-11-10", punten: [
    { ernst: "hoog", tekst: "Yoğunluk hesabında formülü ters kuruyor: V = m / ρ yerine çarpıyor (18 g / 24 cm³ → 432 yazdı); g/cm³ → kg/m³ için ×1000 yapmıyor (7,8 → 7,8); L ↔ cm³ dönüşümünü karıştırıyor (0,35 L → 35)." },
    { ernst: "mid", tekst: "°C ↔ K dönüşümünde yön/işaret hatası: 0 °C → −273, 4 K → 277, 21 °C → −252. Erime/kaynama noktası K ve °C karışık verilince maddenin halini bulamıyor." },
    { ernst: "mid", tekst: "Karışım türlerini karıştırıyor (nevel ↔ rook ↔ emulsie ↔ suspensie); 'çözelti hep renksizdir' sanıyor; emülgatörün çözelti yaptığını düşünüyor. Yeni testler h1-45…58 bunlara gidiyor." }
  ] },
  geschiedenis: { datum: "2026-11-10", punten: [
    { ernst: "hoog", tekst: "H1 kronolojisi zayıf: Versailles 1919, Türkiye 1923, Kanlı Pazar 1905, SSCB 1922 gibi yılları karıştırıyor; Sarajevo suikastine '11 november 1918' yazdı (karışık test 34: 20 sorudan 9'u yanlış)." },
    { ernst: "mid", tekst: "Benzer adları karıştırıyor: Volkenbond ↔ Vrede van Versailles, Brest-Litovsk ↔ Versailles, tsaar ↔ Lenin, Marne ↔ Somme." },
    { ernst: "mid", tekst: "Kavramları kendi kelimesiyle yazıyor ama kabul edilmiyor: 'op de bon' (distributiestelsel), 'illegale' (zwarte markt), 'prikkeldraad' (elektrocutie). Yeni testler 46–65 bunlara gidiyor." }
  ] }
};

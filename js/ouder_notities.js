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
  ] }
};

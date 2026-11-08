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
    { ernst: "mid", tekst: "-n kuralı (enkele/enkelen, andere/anderen) ve samentrekking (streepje, voor-/achterwaarts) en çok hata yaptığı konular (%29–34)." },
    { ernst: "mid", tekst: "hun/hen, apostrof ('s morgens, baby's) ve aksanlarda (è/é) tekrar eden hatalar (%23–27)." }
  ] }
};

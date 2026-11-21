/* =========================================================
   js/ouder_notities.js — handmatige analysenotities per vak voor het ouderpaneel
   ("Gelişim analizi"). Geschreven/bijgewerkt bij elke zwakte-analyse (skill
   zwakte-toetsen, stap 5) op basis van `python3 tools/zwakte.py <vak> --fouten`.
   Taal: Turks (ouderpaneel). ernst: hoog | mid | info | goed. Oude punten weghalen
   zodra ze opgelost zijn — dit is een momentopname, geen logboek.
   ========================================================= */
window.DURU_OUDER_NOTITIES = {
  wiskunde: { datum: "2026-11-20", punten: [
    { ernst: "hoog", tekst: "Bağlamlı parabol sorularını (sulama, top, tünel: başlangıç yüksekliği, cm, en yüksek nokta) neredeyse hep boş bırakıyor (%81–96)." },
    { ernst: "mid", tekst: "Tepe noktası verilen parabolün formülünü seçerken b'nin işaretini ve c = y-kesişimini karıştırıyor (%46)." },
    { ernst: "mid", tekst: "Üstel büyümede zaman birimi dönüşümünde (aylık ↔ yıllık) hata yapıyor (%48)." },
    { ernst: "info", tekst: "8 Kasım'dan beri wiskunde çalışılmadı. Yeni karışık testler 129–131: her testin ilk 3 sorusu bağlamlı parabol (başlangıç yüksekliği, cm, en yüksek nokta; küçük adımlarla), sonra 8 soru H2, 7 soru H1, 2 soru statistiek tekrarı." }
  ] },
  nederlands: { datum: "2026-11-20", punten: [
    { ernst: "hoog", tekst: "Samentrekking’de voorwaarts/achterwaarts'ı sistematik olarak ters yapıyor (son 10 testte 11 kez): kelimenin durduğu yere değil boşluğun yerine bakıyor." },
    { ernst: "hoog", tekst: "Açık 'verbeter + waarom' sorularında yalnız düzeltilmiş cümleyi yazıyor, nedenini hiç yazmıyor → hep yarım puan." },
    { ernst: "mid", tekst: "Verwijzen: 'het meisje die' (doğrusu dat), regering/gemeente/politie için 'zijn/hun' (doğrusu haar), eşyalar için 'het' (doğrusu hem); hun/hen karışık." },
    { ernst: "hoog", tekst: "Toets 72'yi üç kez aynı yanlış cevaplarla çözdü: sonuçtaki açıklamaları okumuyor. 'het meisje dat' (lidwoord karar verir, cinsiyet değil), eşyalar için 'hem', regering için 'haar' kurallarını birlikte konuşmak faydalı olur." },
    { ernst: "mid", tekst: "Prova sınavları (68–70): 10–14 / 20. Foutentraining 71–73: 9–16 / 20. 74–75 aynı hatalara farklı yoldan (adım adım, karşılaştırmalı) gidiyor." },
    { ernst: "info", tekst: "8 Kasım'dan beri nederlands çalışılmadı; Foutentraining E (75) henüz çözülmedi. Toets 74 üç denemede 8 → 6 → 14. Yeni karışık testler 76–78: spelling (-n, -e, apostrof, accent, trema), grammatica (hun/hen, voor/achterwaarts, verwijzen), kısa okuma metni (C1) ve dt tekrarı." }
  ] },
  economie: { datum: "2026-11-12", punten: [
    { ernst: "mid", tekst: "§2.3 (19 test, son deneme ort. %79): reel gelir hesabında eksi işaretini unutuyor (−0,9 yerine 0,9) ve ücret/fiyat tablosunda en yüksek çubuğa bakıyor, farka (ücret − fiyat) bakmıyor." },
    { ernst: "mid", tekst: "Bestedingsinflatie'yi 'çok fazla arz' sanıyor (doğrusu: çok fazla talep/vraag); kosteninflatie ile karıştırıyor. CBS'in çok harcanan ürünleri 'daha ağır' saydığını ve enflasyonun bir ortalama olduğunu kaçırıyor." },
    { ernst: "mid", tekst: "CPB (koopkrachtplaatjes) ↔ CBS (enflasyonu ölçer) karışık; 'modaal' ve 'inflatiecijfer' boş. Açık soruların çoğu boş (53'ün 41'i). Yeni testler 116–120 bunlara gidiyor." },
    { ernst: "mid", tekst: "Yeni denemelerde (examen_96–100): euro tutardan yüzdeye geçemiyor (önce yeni−eski / eski × 100%, sonra enflasyonu çıkarmak gerekiyor); ücret ve fiyat ikisi de düşünce işareti karıştırıyor; formülü tersine kullanamıyor (nominal = reel + enflasyon); 7 − 5,5 yerine 7 + 5,5 = 12,5 topluyor; fiyat düşünce alım gücünün arttığını kaçırıyor. Testler 121–125 bunlara gidiyor; 116–120 henüz çözülmedi." },
    { ernst: "hoog", tekst: "116–125 çözüldü (§2.3 31 test, ort. %78). En zayıf: examen_122 — ücret ve fiyat ikisi düşünce −1 − (−4) yerine 5 yazıyor; 'enflasyonun %60'ı'nı 10 − 60 = −50 diye hesaplıyor; formülü tersine kullanamıyor (nominal = reel + enflasyon). Kitaptaki sayılar (1975, €38.000, %58) boş. 126–127 bunu daha küçük adımlarla (önce sadece eksi-eksi işlemi) çalıştırıyor; düzelmezse evde negatif sayı alıştırması gerekebilir." }
  ] },
  scheikunde: { datum: "2026-11-20", punten: [
    { ernst: "hoog", tekst: "Yoğunluk hesabında formülü ters kuruyor: V = m / ρ yerine çarpıyor (18 g / 24 cm³ → 432 yazdı); g/cm³ → kg/m³ için ×1000 yapmıyor (7,8 → 7,8); L ↔ cm³ dönüşümünü karıştırıyor (0,35 L → 35)." },
    { ernst: "mid", tekst: "°C ↔ K dönüşümünde yön/işaret hatası: 0 °C → −273, 4 K → 277, 21 °C → −252. Erime/kaynama noktası K ve °C karışık verilince maddenin halini bulamıyor." },
    { ernst: "mid", tekst: "Karışım türlerini karıştırıyor (nevel ↔ rook ↔ emulsie ↔ suspensie); 'çözelti hep renksizdir' sanıyor; emülgatörün çözelti yaptığını düşünüyor. Yeni testler h1-45…58 bunlara gidiyor." },
    { ernst: "mid", tekst: "H2 §2.1 (son 10 deneme): katı maddede moleküllerin 'tamamen durduğunu' sanıyor (doğrusu: yerinde titreşir), sublimeren ↔ condenseren karıştırıyor, triljoen = 18 sıfır (6/12 yazdı), mikro ↔ makro düzey karışık; açık soruların çoğu boş. Herhaling toetsen h1-59…60, h2-62…67 bunlara gidiyor." },
    { ernst: "mid", tekst: "11 Kasım'dan beri çalışılmadı. H2'de en zayıf §2.4 (%42 kaçırma, son deneme 11/20: atoomnummer, isotopen, massagetal) ve §2.3 (%40: sistematik adlandırma, molekül kütlesi, index ↔ coëfficiënt). Yeni karışık testler h2-80…82: 12 soru H2 (bunlara ağırlık) + 8 soru H1 tekrarı (dichtheid, °C ↔ K, mengsels)." }
  ] },
  geschiedenis: { datum: "2026-11-10", punten: [
    { ernst: "hoog", tekst: "H1 kronolojisi zayıf: Versailles 1919, Türkiye 1923, Kanlı Pazar 1905, SSCB 1922 gibi yılları karıştırıyor; Sarajevo suikastine '11 november 1918' yazdı (karışık test 34: 20 sorudan 9'u yanlış)." },
    { ernst: "mid", tekst: "Benzer adları karıştırıyor: Volkenbond ↔ Vrede van Versailles, Brest-Litovsk ↔ Versailles, tsaar ↔ Lenin, Marne ↔ Somme." },
    { ernst: "mid", tekst: "Kavramları kendi kelimesiyle yazıyor ama kabul edilmiyor: 'op de bon' (distributiestelsel), 'illegale' (zwarte markt), 'prikkeldraad' (elektrocutie). Yeni testler 46–65 bunlara gidiyor." },
    { ernst: "mid", tekst: "10 Kasım akşamı 10 denemeyi 25 dakikada yaptı (deneme başı 2–3 dk); toets 43'ü üst üste 4 kez çözdü (7→12→12→17/20) — ezber/tahmin olabilir. §1.4 en zayıf: Kemal 'sultan' (doğrusu president), Anatolië, Hongarije, Baltische staten, Poolse Corridor, goudmarken. Herhaling toetsen 66–75 bunlara gidiyor." }
  ] },
  biologie: { datum: "2026-11-20", punten: [
    { ernst: "mid", tekst: "H11 genel olarak iyi (%18–23 kaçırma, son deneme ort. %74–80). En zayıf §11.3 (placenta: kan karışmaz, zararlı maddeler geçer) ve §11.4 (zaadcel 23 / bevruchte eicel 46 chromosoom, genoom, 23. chromosomenpaar, genotype + omgeving). Toets 73'ü üst üste 3 kez çözdü (10 → 12 → 16): ölçü ilk deneme." },
    { ernst: "mid", tekst: "H10 (Je verandert) son deneme ort. %68 — en düşük ünite, boş bırakılan soru fazla (hypofyse, groeischijven, geslachtskenmerken). H11'de 4 test (39, 46, 62, 66) çözülmedi. Yeni karışık testler 79–81: 13 soru H11 + 7 soru H10 tekrarı." }
  ] },
  natuurkunde: { datum: "2026-11-20", punten: [
    { ernst: "hoog", tekst: "15 Kasım akşamı son 15 test (~75 hata): en büyük sorun hâlâ işlem seçimi — bölmesi gerekirken çarpıyor (a = F : m → 4000/5000/15000 m/s², a = Δv : t, m = Fz : g, s = v · t yerine t / v) ≈ 22 hata; sonra birim çevirme (g → kg, kJ ↔ J, km → m, dakika → saat) ≈ 12; remweg = stopafstand − reactieafstand yerine topluyor. Artifact'ta arbeid ve diagram toets 8,5 oldu. Yeni testler: 113 (delen of keer?) ve 114 (omrekenen + arbeid + diagram)." },
    { ernst: "mid", tekst: "Gerçek proefwerk provası: 115–119 (A–E), kitabın hoofdstuk sonu opgaven tarzında — her testte 4–5 senaryo (noodstop, (v,t)-diyagramı, sledehonden, uitrijden, kreukelzone/airbag) ve çok adımlı hesaplar (önce km/h → m/s, sonra a, sonra F). 45 dk; sınavdan önce her birini bir kez, ilk deneme notu ölçü." },
    { ernst: "hoog", tekst: "92–96 ve artifact (15 Kasım): diyagramlar zayıf (artifact toets 3× 4,0; s,t ↔ v,t karışıyor, alan yerine 12 : 6 = 2 hesaplıyor) ve arbeid takılı (8 toets 5,5–7: kg'ı kuvvet sanıyor, cm/kJ çevirmiyor, top yukarı-aşağı 'negatief'). Artifact'ta bu iki ders artık adım adım kartlarla anlatılıyor; sitede § başına 2 yeni test (103–112)." },
    { ernst: "hoog", tekst: "İki turdur değişmeyen: a = F / m yerine çarpıyor (87: 90 000 m/s²; m = Fz/g ve F = W/s'de de), mesafede v/t bölüyor ya da ½'yi unutuyor (86, 91, 85). Yaklaşım değişti: test 92 (önce işlemi seç, Sam'in hatası, gerçekçi mi?) ve 93 (önce v_gem, sonra × t; birim mantığı)." },
    { ernst: "mid", tekst: "Remweg hâlâ ×k (3× hız → 3×), arbeid'da ise tersine kare kullanıyor (2× yükseklik → 4×). Sabit hızda/duruşta 'kuvvet yok' diyor ve karşıt kuvvetleri topluyor (900 + 350). Botsen yarı yarıya. Test 94 (2× mı 4× mü, botsen) ve 95 (kuvvetleri çıkar, oranlar); 96 hepsi karışık." },
    { ernst: "laag", tekst: "Arbeid cm/km/kJ oturdu (90: 18/20), eenheden oturdu. Aynı testi 3–4 dk sonra tekrar çözünce +6 puan: ezber; ölçü ilk deneme. Açık sorular hâlâ boş. Artifact'ta formules/afstand/constant/diagram dersleri ve yeni oyunlar henüz açılmadı." },
    { ernst: "info", tekst: "Proefwerk provası 115–119 ilk denemeler 10–16 / 20; en zayıf §1.2 ve §1.3 (%35 kaçırma), §1.4 (%33). 15 Kasım'dan beri çalışılmadı. Yeni karışık testler 120–122 tüm H1'i (§1.1–§1.5) son hatalara ağırlık vererek tekrar ediyor." }
  ] }
};

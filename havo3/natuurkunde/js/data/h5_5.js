/* =========================================================
   Duru's Natuurkunde (HAVO 3) — §5.5 Rekenen aan lenzen
   ========================================================= */
DURU.register({
  "id": "h5-5-rekenen-aan-lenzen",
  "hoofdstuk": 5,
  "paragraaf": "5.5",
  "titel": "Rekenen aan lenzen",
  "korteUitleg": "De lenzenformule 1/f = 1/v + 1/b, lenssterkte in dioptrie (S = 1/f) en vergroting N.",
  "icoon": "📐",
  "kleur": "h5-thema",
  "theorie": "<h3>5.5 Rekenen aan lenzen en lenssterkte</h3>\n<div class='formule-box'>\n<strong>De wiskundige formules voor lenzen:</strong><br>\n• <b>De lenzenformule:</b>\n<div style='font-size:1.2em; text-align:center; margin:8px 0;'><b>1 / f = 1 / v + 1 / b</b></div>\nwaarbij:<br>\n- <b>f</b> = brandpuntsafstand in centimeter (cm) of meter (m)<br>\n- <b>v</b> = voorwerpsafstand in dezelfde lengte-eenheid (cm of m)<br>\n- <b>b</b> = beeldafstand in dezelfde lengte-eenheid (cm of m)<br>\n<i>(Let op: alle drie de grootheden f, v en b moeten in EXACT dezelfde eenheid worden ingevuld!)</i><br><br>\n\n• <b>De lineaire vergroting N:</b>\n<div style='font-size:1.2em; text-align:center; margin:8px 0;'><b>N = L<sub>b</sub> / L<sub>v</sub> = b / v</b></div>\n- Als N > 1 is het beeld groter dan het voorwerp (vergroot).<br>\n- Als N < 1 is het beeld kleiner dan het voorwerp (verkleind).<br>\n- Als N = 1 is het beeld even groot als het voorwerp (b = v = 2f).<br><br>\n\n• <b>Lenssterkte S in dioptrie (dpt):</b>\n<div style='font-size:1.2em; text-align:center; margin:8px 0;'><b>S = 1 / f</b></div>\n<i>CRUCIALE REGEL: Voor dioptrie MOET de brandpuntsafstand f ALTIJD in <b>meters (m)</b> worden ingevuld!</i><br>\n- Positieve lens: f is positief ➔ S is positief (bijv. f = +0,25 m ➔ S = +4,0 dpt).<br>\n- Negatieve lens: f is negatief ➔ S is negatief (bijv. f = -0,50 m ➔ S = -2,0 dpt).\n</div>\n\n<h4>Stappenplan voor het rekenen met de lenzenformule</h4>\n<ol>\n  <li><b>Gegevens opschrijven:</b> Noteer f, v en b en zet ze om naar dezelfde eenheid (meestal cm).</li>\n  <li><b>Formule noteren:</b> 1/f = 1/v + 1/b.</li>\n  <li><b>Onbekende isoleren:</b>\n    <ul>\n      <li>Zoek je b? Dan geldt: <b>1/b = 1/f - 1/v</b>.</li>\n      <li>Zoek je v? Dan geldt: <b>1/v = 1/f - 1/b</b>.</li>\n      <li>Zoek je f? Dan tel je 1/v en 1/b bij elkaar op en neem je het omgekeerde (1 / uitkomst).</li>\n    </ul>\n  </li>\n  <li><b>Vergeet niet om te keren!</b> Nadat je bijvoorbeeld 1/b hebt uitgerekend, moet je nog delen: <b>b = 1 / (1/b)</b>.</li>\n</ol>\n\n<h4>Rekenvoorbeeld</h4>\n<p>Een dia staat op voorwerpsafstand v = 5,0 cm van een projectorlens met brandpuntsafstand f = 4,0 cm. Waar ontstaat het scherpe beeld op de muur?</p>\n<ul>\n  <li>1/b = 1/f - 1/v = 1/4,0 - 1/5,0 = 0,25 - 0,20 = 0,05 cm<sup>-1</sup></li>\n  <li>b = 1 / 0,05 = <b>20 cm</b>.</li>\n  <li>De vergroting is N = b / v = 20 / 5,0 = <b>4×</b>. Het beeld op de muur is 4 keer zo groot als het origineel!</li>\n</ul>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat is de lenssterkte S in dioptrie van een positieve lens met een brandpuntsafstand van f = 20 cm?",
      "opties": [
        "+0,05 dpt",
        "+5 dpt",
        "+20 dpt",
        "+0,2 dpt"
      ],
      "antwoord": 1,
      "uitleg": "Eerst omrekenen naar meter: f = 20 cm = 0,20 m. Daarna geldt S = 1 / f = 1 / 0,20 = +5 dpt."
    },
    {
      "type": "mc",
      "vraag": "Een lens heeft een sterkte van S = -4 dpt. Wat voor lens is dit en wat is de brandpuntsafstand?",
      "opties": [
        "Een bolle lens met f = +25 cm",
        "Een holle lens met f = -4 meter",
        "Een negatieve (holle) lens met f = -25 cm (-0,25 m)",
        "Een vlakke spiegel zonder brandpunt"
      ],
      "antwoord": 2,
      "uitleg": "Het minteken duidt op een negatieve lens. f = 1 / S = 1 / (-4) = -0,25 m = -25 cm."
    },
    {
      "type": "mc",
      "vraag": "Een voorwerp staat op v = 30 cm van een lens met f = 10 cm. Op welke beeldafstand b ontstaat het scherpe beeld?",
      "opties": [
        "b = 20 cm",
        "b = 10 cm",
        "b = 40 cm",
        "b = 15 cm"
      ],
      "antwoord": 3,
      "uitleg": "1/b = 1/f - 1/v = 1/10 - 1/30 = 3/30 - 1/30 = 2/30 = 1/15. Dus b = 15 cm."
    },
    {
      "type": "mc",
      "vraag": "Een lampje staat op 60 cm van een lens. Het beeld ontstaat op 120 cm achter de lens. Hoe groot is de vergrotingsfactor N?",
      "opties": [
        "N = 2",
        "N = 0,5",
        "N = 7200",
        "N = 60"
      ],
      "antwoord": 0,
      "uitleg": "N = b / v = 120 cm / 60 cm = 2."
    },
    {
      "type": "waaronwaar",
      "vraag": "Om de lenssterkte in dioptrie (S = 1/f) te berekenen, mag je de brandpuntsafstand f rechtstreeks in centimeters invullen.",
      "antwoord": false,
      "uitleg": "Onwaar: Voor dioptrie MOET de brandpuntsafstand f altijd strikt in meters worden omgerekend."
    },
    {
      "type": "waaronwaar",
      "vraag": "In de lenzenformule (1/f = 1/v + 1/b) moeten f, v en b alle drie in dezelfde lengte-eenheid staan.",
      "antwoord": true,
      "uitleg": "Waar: Je moet f, v en b allemaal in meters of allemaal in centimeters invullen."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als de vergroting N kleiner is dan 1 (bijv. N = 0,25), betekent dit dat het beeld kleiner is dan het originele voorwerp.",
      "antwoord": true,
      "uitleg": "Waar: Bij N < 1 is het beeld verkleind (zoals bij een fotocamera die een landschap afbeeldt op een kleine sensor)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een lens met een brandpuntsafstand van 50 cm heeft een sterkte van 50 dioptrie.",
      "antwoord": false,
      "uitleg": "Onwaar: f = 50 cm = 0,5 m. S = 1 / 0,5 = +2 dioptrie (geen 50 dpt)."
    },
    {
      "type": "invoer",
      "vraag": "Wat is de brandpuntsafstand in centimeters van een lens met sterkte S = +2 dpt?",
      "antwoord": "50|50 cm",
      "uitleg": "f = 1 / S = 1 / 2 = 0,5 m = 50 cm."
    },
    {
      "type": "invoer",
      "vraag": "Als een voorwerp van 10 cm hoog een beeld oplevert van 50 cm hoog op een scherm, wat is dan de vergrotingsfactor N?",
      "antwoord": "5|5x",
      "uitleg": "N = Lb / Lv = 50 cm / 10 cm = 5."
    }
  ]
});

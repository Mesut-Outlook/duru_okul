/* =========================================================
   Duru's Natuurkunde (HAVO 3) — §5.3 Construeren bij lenzen
   ========================================================= */
DURU.register({
  "id": "h5-3-construeren-bij-lenzen",
  "hoofdstuk": 5,
  "paragraaf": "5.3",
  "titel": "Construeren bij lenzen",
  "korteUitleg": "De drie constructiestralen bij een positieve lens, reëel en virtueel beeld, voorwerps- en beeldafstand en vergroting.",
  "icoon": "🔍",
  "kleur": "h5-thema",
  "theorie": "<h3>5.3 Beelden construeren bij positieve lenzen</h3>\n<div class='formule-box'>\n<strong>Constructieregels voor een positieve lens:</strong><br>\nOm de beeldvorming van een voorwerp te bepalen, teken je vanuit het topje van het voorwerp (punt L of Q) minimaal twee van de volgende <b>drie constructiestralen</b>:<br>\n1. <b>Constructiestraal 1 (evenwijdig):</b> Loopt vanaf het voorwerppunt evenwijdig aan de optische as naar de lens, breekt in de lens en gaat achter de lens <b>door het brandpunt F</b>.<br>\n2. <b>Constructiestraal 2 (middelpunt):</b> Loopt vanaf het voorwerppunt recht door het <b>optisch middelpunt O</b> van de lens en gaat <b>ongebroken rechtdoor</b>.<br>\n3. <b>Constructiestraal 3 (brandpuntsstraal):</b> Gaat vóór de lens door het brandpunt F naar de lens toe, en loopt achter de lens <b>evenwijdig aan de optische as</b> verder.<br>\nHet snijpunt van deze stralen achter de lens vormt het bijbehorende <b>beeldpunt (L' of Q')</b>.\n</div>\n\n<h4>Begrippen en afstanden</h4>\n<ul>\n  <li><b>Voorwerpsafstand (v):</b> De afstand van het voorwerp tot het midden van de lens.</li>\n  <li><b>Beeldafstand (b):</b> De afstand van het scherpe beeld (op scherm of sensor) tot het midden van de lens.</li>\n  <li><b>Voorwerpsgrootte (L<sub>v</sub>):</b> De werkelijke hoogte van het voorwerp in cm of mm.</li>\n  <li><b>Beeldgrootte (L<sub>b</sub>):</b> De hoogte van het gevormde beeld in cm of mm.</li>\n</ul>\n\n<h4>Eigenschappen van het beeld bij verschillende voorwerpsafstanden</h4>\n<p>Afhankelijk van waar je het voorwerp neerzet ten opzichte van de brandpuntsafstand f, ontstaat een ander type beeld:</p>\n<ul>\n  <li><b>v > 2f (voorwerp ver weg, zoals bij een fotocamera):</b>\n    Het beeld bevindt zich tussen f en 2f achter de lens. Het beeld is <b>reëel</b>, staat <b>op zijn kop (omgekeerd)</b> en is <b>verkleind</b> (b < v).</li>\n  <li><b>v = 2f:</b>\n    Het beeld staat op afstand b = 2f achter de lens. Het beeld is <b>reëel, omgekeerd</b> en <b>even groot</b> als het voorwerp (L<sub>b</sub> = L<sub>v</sub>).</li>\n  <li><b>f < v < 2f (zoals bij een filmprojector of beamer):</b>\n    Het beeld bevindt zich voorbij 2f (b > 2f). Het beeld is <b>reëel, omgekeerd</b> en <b>vergroot</b> (b > v).</li>\n  <li><b>v = f:</b>\n    De uittredende stralen lopen evenwijdig aan elkaar en snijden elkaar nergens; er ontstaat <b>geen beeld</b>.</li>\n  <li><b>v < f (voorwerp heel dichtbij, zoals bij een loep):</b>\n    De uittredende stralen wijken uiteen. Aan de voorkant van de lens lijken ze uit één punt te komen. Er ontstaat een <b>virtueel, rechtopstaand en vergroot beeld</b>.</li>\n</ul>\n\n<h4>Vergroting N</h4>\n<p>De vergrotingsfactor N geeft aan hoeveel keer groter of kleiner het beeld is dan het voorwerp:</p>\n<div class='formule-box'>\n<b>N = L<sub>b</sub> / L<sub>v</sub> = b / v</b><br>\n<i>(Let op: N is een verhouding en heeft geen eenheid. Zorg dat L<sub>b</sub> en L<sub>v</sub>, respectievelijk b en v, in dezelfde eenheid staan!)</i>\n</div>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat doet een constructiestraal die evenwijdig aan de optische as op een positieve lens invalt?",
      "opties": [
        "Hij breekt na de lens door het optisch middelpunt",
        "Hij breekt na de lens door het brandpunt F achter de lens",
        "Hij kaatst onder dezelfde hoek terug",
        "Hij gaat zonder te breken evenwijdig rechtdoor"
      ],
      "antwoord": 1,
      "uitleg": "Constructiestraal 1 loopt evenwijdig aan de optische as en breekt na de positieve lens door het brandpunt F aan de overzijde."
    },
    {
      "type": "mc",
      "vraag": "Wat doet een constructiestraal die door het optisch middelpunt O van een dunne lens gaat?",
      "opties": [
        "Hij breekt naar het brandpunt toe",
        "Hij buigt 90 graden af",
        "Hij gaat ongebroken in een rechte lijn rechtdoor",
        "Hij wordt diffuus verstrooid"
      ],
      "antwoord": 2,
      "uitleg": "Een lichtstraal die door het optisch middelpunt O van de lens valt, verandert niet van richting en gaat rechtdoor."
    },
    {
      "type": "mc",
      "vraag": "Bij een beamer staat het voorwerp (het lcd-schermpje) tussen 1f en 2f van de lens. Welke eigenschappen heeft het geprojecteerde beeld op de muur?",
      "opties": [
        "Virtueel, rechtopstaand en verkleind",
        "Reëel, rechtopstaand en even groot",
        "Virtueel, omgekeerd en vergroot",
        "Reëel, omgekeerd en vergroot"
      ],
      "antwoord": 3,
      "uitleg": "Wanneer het voorwerp tussen 1f en 2f staat (voorwerpsafstand v tussen f en 2f), ontstaat aan de andere kant van de lens een reëel, omgekeerd en vergroot beeld op een beeldafstand groter dan 2f."
    },
    {
      "type": "mc",
      "vraag": "Een voorwerp met hoogte Lv = 5 cm levert een scherp reëel beeld op met hoogte Lb = 15 cm. Wat is de vergrotingsfactor N?",
      "opties": [
        "N = 3",
        "N = 0,33",
        "N = 75",
        "N = 10"
      ],
      "antwoord": 0,
      "uitleg": "De vergrotingsfactor is N = Lb / Lv = 15 cm / 5 cm = 3."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een reëel beeld dat door een bolle lens op een scherm wordt geprojecteerd, staat altijd op zijn kop (omgekeerd) vergeleken met het origineel.",
      "antwoord": true,
      "uitleg": "Waar: Reële beelden die ontstaan door een enkele positieve lens zijn altijd geïnverteerd (ondersteboven)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Wanneer je een positieve lens gebruikt als vergrootglas (loep), zet je het voorwerp verder weg dan tweemaal de brandpuntsafstand (v > 2f).",
      "antwoord": false,
      "uitleg": "Onwaar: Voor een loep moet het voorwerp juist dichterbij staan dan het brandpunt (v < f), zodat er een vergroot virtueel beeld ontstaat."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als de beeldafstand b gelijk is aan de voorwerpsafstand v, is de vergrotingsfactor N exact gelijk aan 1.",
      "antwoord": true,
      "uitleg": "Waar: Omdat N = b / v, is N = 1 wanneer b = v. Het beeld is dan precies even groot als het voorwerp."
    },
    {
      "type": "waaronwaar",
      "vraag": "Om een beeldpunt te construeren moet je altijd minimaal 10 verschillende lichtstralen tekenen.",
      "antwoord": false,
      "uitleg": "Onwaar: Twee nauwkeurig getekende constructiestralen zijn al voldoende om het unieke snijpunt (het beeldpunt) vast te leggen."
    },
    {
      "type": "invoer",
      "vraag": "Een voorwerp van 4 cm hoog staat voor een lens. Het beeld op het scherm is 2 cm hoog. Wat is de vergrotingsfactor N (gebruik een komma bij decimalen)?",
      "antwoord": "0,5|0.5",
      "uitleg": "N = Lb / Lv = 2 cm / 4 cm = 0,5."
    },
    {
      "type": "invoer",
      "vraag": "Als een voorwerp op voorwerpsafstand v = 20 cm staat en het scherpe beeld ontstaat op beeldafstand b = 60 cm, hoeveel bedraagt dan de vergroting N?",
      "antwoord": "3|3x",
      "uitleg": "N = b / v = 60 cm / 20 cm = 3."
    }
  ]
});

/* =========================================================
   Duru's Natuurkunde (HAVO 3) — §5.2 Breking van licht
   ========================================================= */
DURU.register({
  "id": "h5-2-breking",
  "hoofdstuk": 5,
  "paragraaf": "5.2",
  "titel": "Breking van licht",
  "korteUitleg": "Lichtbreking bij grensvlakken, breking naar en van de normaal, bolle en holle lenzen, brandpunt en brandpuntsafstand.",
  "icoon": "💡",
  "kleur": "h5-thema",
  "theorie": "<h3>5.2 Breking van licht</h3>\n<div class='formule-box'>\n<strong>Belangrijke definities en regels:</strong><br>\n• <b>Lichtbreking (refractie):</b> De richtingsverandering van een lichtstraal wanneer deze schuin overgaat van de ene doorzichtige tussenstof naar de andere.<br>\n• <b>Oorzaak van breking:</b> Licht heeft in verschillende stoffen een verschillende voortplantingssnelheid (in vacuüm/lucht ca. 300.000 km/s, in water ca. 225.000 km/s, in glas ca. 200.000 km/s).<br>\n• <b>Breking naar de normaal toe:</b> Bij de overgang van een optisch minder dichte stof naar een dichtere stof (zoals van lucht naar water of glas) geldt: <b>∠r < ∠i</b> (de hoek van breking is kleiner dan de hoek van inval).<br>\n• <b>Breking van de normaal af:</b> Bij de overgang van een dichtere stof naar een minder dichte stof (zoals van water of glas naar lucht) geldt: <b>∠r > ∠i</b> (de straal buigt weg van de normaal).<br>\n• <b>Loodrechte inval (∠i = 0°):</b> Als het licht loodrecht op het grensvlak invalt, verandert de richting niet (∠r = 0°).\n</div>\n\n<h4>Bolle en holle lenzen</h4>\n<p>Lenzen maken gebruik van lichtbreking om lichtbundels van vorm te veranderen:</p>\n<ul>\n  <li><b>Bolle lens (positieve lens, symbool +):</b>\n    <ul>\n      <li>Het midden van de lens is <b>dikker</b> dan de randen.</li>\n      <li>Werkt <b>convergerend</b>: een evenwijdige invallende lichtbundel wordt naar elkaar toe gebogen en komt samen in één punt: het <b>brandpunt (F)</b>.</li>\n      <li>De afstand van het optisch middelpunt van de lens tot het brandpunt heet de <b>brandpuntsafstand (f)</b>.</li>\n      <li>Hoe boller de lens is geslepen, hoe sterker hij het licht breekt en des te <b>korter</b> is de brandpuntsafstand f.</li>\n    </ul>\n  </li>\n  <li><b>Holle lens (negatieve lens, symbool -):</b>\n    <ul>\n      <li>Het midden van de lens is <b>dunner</b> dan de randen.</li>\n      <li>Werkt <b>divergerend</b>: een evenwijdige invallende lichtbundel wordt uit elkaar gebogen.</li>\n      <li>De uit elkaar wijkende lichtstralen lijken afkomstig te zijn van een denkbeeldig punt vóór de lens: het <b>virtuele brandpunt</b>.</li>\n    </ul>\n  </li>\n</ul>\n\n<h4>Omkeerbaarheid van de lichtweg</h4>\n<p>Een fundamentele eigenschap van lichtstralen is dat de lichtweg omkeerbaar is: als je een lichtstraal in omgekeerde richting door een grensvlak of lens stuurt, volgt hij exact dezelfde baan. Als een straal van lucht naar glas onder een hoek van 40° breekt naar 25°, dan zal een straal vanuit glas onder 25° in lucht precies onder 40° uittreden.</p>\n\n<div class='begrippen-box'>\n<b>Onthoud voor proefwerken:</b>\n• Een positieve lens verzamelt licht (convergeert).<br>\n• Een negatieve lens spreidt licht (divergeert).<br>\n• Brandpuntsafstand f wordt altijd gemeten vanaf het midden van de lens tot het brandpunt F.\n</div>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat gebeurt er met een schuin invallende lichtstraal die vanuit de lucht het water in gaat?",
      "opties": [
        "De lichtstraal breekt naar de normaal toe",
        "De lichtstraal breekt van de normaal af",
        "De lichtstraal gaat zonder van richting te veranderen rechtdoor",
        "De lichtstraal buigt altijd in een hoek van 90 graden om"
      ],
      "antwoord": 0,
      "uitleg": "Omdat water optisch dichter is dan lucht (het licht vertraagt), breekt de lichtstraal naar de normaal toe: hoek r is kleiner dan hoek i."
    },
    {
      "type": "mc",
      "vraag": "Welk kenmerk hoort bij een <b>positieve (bolle) lens</b>?",
      "opties": [
        "De lens is in het midden dunner dan aan de randen",
        "De lens heeft een divergerende werking op licht",
        "De lens laat evenwijdige lichtstralen samenkomen in het brandpunt (convergerend)",
        "De lens heeft geen brandpunt"
      ],
      "antwoord": 2,
      "uitleg": "Een positieve (bolle) lens is in het midden dikker en heeft een convergerende werking: evenwijdige stralen worden naar het brandpunt toe gebogen."
    },
    {
      "type": "mc",
      "vraag": "Hoe verandert de brandpuntsafstand f als je een bolle lens nóg boller slijpt?",
      "opties": [
        "De brandpuntsafstand wordt oneindig groot",
        "De brandpuntsafstand verandert niet",
        "De brandpuntsafstand wordt groter",
        "De brandpuntsafstand wordt kleiner"
      ],
      "antwoord": 3,
      "uitleg": "Hoe boller de lens, des te sterker hij licht breekt. De lichtstralen kruisen de optische as dichter bij de lens, dus de brandpuntsafstand f wordt kleiner."
    },
    {
      "type": "mc",
      "vraag": "Wat gebeurt er als een lichtstraal exact loodrecht (onder een hoek van 0° met de normaal) invalt op een glasplaat?",
      "opties": [
        "De lichtstraal buigt 45 graden af",
        "De lichtstraal plant zich in dezelfde richting voort zonder knik",
        "De lichtstraal wordt voor 100% teruggekaatst als spiegelbeeld",
        "De lichtstraal splitst direct in een regenboog"
      ],
      "antwoord": 1,
      "uitleg": "Bij loodrechte inval (hoek van inval = 0°) is de hoek van breking ook 0°. De straal gaat kaarsrecht door het grensvlak heen."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een holle lens (negatieve lens) buigt evenwijdige lichtstralen uit elkaar (divergerende werking).",
      "antwoord": true,
      "uitleg": "Waar: Een holle lens spreidt het licht; de uittredende stralen wijken divergerend uiteen."
    },
    {
      "type": "waaronwaar",
      "vraag": "Wanneer licht van glas naar lucht overgaat, breekt de lichtstraal naar de normaal toe.",
      "antwoord": false,
      "uitleg": "Onwaar: Bij de overgang van glas naar lucht (van dichter naar minder dicht) breekt de lichtstraal juist VÁN de normaal af."
    },
    {
      "type": "waaronwaar",
      "vraag": "De afstand tussen het optisch middelpunt van een lens en het brandpunt noem je de brandpuntsafstand (f).",
      "antwoord": true,
      "uitleg": "Waar: Dit is exact de formele definitie van de brandpuntsafstand f."
    },
    {
      "type": "waaronwaar",
      "vraag": "De optische as van een lens is een kromme lijn die langs de buitenrand van de lens loopt.",
      "antwoord": false,
      "uitleg": "Onwaar: De optische as is een denkbeeldige rechte lijn die loodrecht door het exacte midden (optisch middelpunt) van de lens loopt."
    },
    {
      "type": "invoer",
      "vraag": "Welk symbool (+ of -) gebruikt men in een schematische natuurkundetekening om een bolle, convergerende lens aan te duiden?",
      "antwoord": "+|plus|+ teken",
      "uitleg": "Een convergerende (bolle) lens wordt schematisch aangeduid met een plus (+)."
    },
    {
      "type": "invoer",
      "vraag": "Hoe noem je het punt waar een bolle lens evenwijdig invallende lichtstralen laat samenkomen?",
      "antwoord": "brandpunt|het brandpunt|focus|brandpunt F",
      "uitleg": "Dit punt heet het brandpunt (vaak aangeduid met de hoofdletter F)."
    }
  ]
});

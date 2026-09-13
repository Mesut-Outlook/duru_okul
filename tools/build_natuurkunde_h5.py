#!/usr/bin/env python3
"""
build_natuurkunde_h5.py — Natuurkunde H5 Licht Onderwerpen & Examens Generator
Creates:
- havo3/natuurkunde/js/data/h5_1.js t/m h5_5.js (5 oefenlessen, theorie >= 1500 chars, 10 vragen elk)
- havo3/natuurkunde/js/data/examen_40.js t/m examen_44.js (5 proeftoetsen, 20 vragen elk)
"""
import os
import json
import re

DATA_DIR = "/home/mesuto/Documents/PROJELER/duru_okul/havo3/natuurkunde/js/data"
os.makedirs(DATA_DIR, exist_ok=True)

# ---------------------------------------------------------
# ONDERWERPEN (h5_1 t/m h5_5)
# ---------------------------------------------------------

ONDERWERPEN = [
    {
        "id": "h5-1-licht-en-beeld",
        "hoofdstuk": 5,
        "paragraaf": "5.1",
        "titel": "Licht en beeld",
        "korteUitleg": "Lichtbronnen, schaduwvorming, diffuus en spiegelend weerkaatsen, de spiegelwet en spiegelbeelden.",
        "icoon": "🔦",
        "kleur": "h5-thema",
        "theorie": """<h3>5.1 Licht en beeld</h3>
<div class='formule-box'>
<strong>Kernbegrippen uit het tekstboek:</strong><br>
• <b>Direct licht:</b> Licht dat rechtstreeks afkomstig is van een lichtbron (bijv. de zon, een gloeilamp, een vlam, sterren).<br>
• <b>Indirect licht:</b> Licht dat afkomstig is van een voorwerp dat licht van een andere bron weerkaatst (bijv. de maan, een tafel, een spiegel, een gezicht).<br>
• <b>Lichtstralen:</b> Licht plant zich voort langs rechte lijnen. Een bundel lichtstralen geeft de richting van het licht aan.<br>
• <b>De spiegelwet:</b> Hoek van inval (∠i) is exact gelijk aan de hoek van terugkaatsing (∠t): <b>∠i = ∠t</b>.<br>
• <b>Normaal:</b> De hulplijn (stippellijn) die loodrecht (90°) op het spiegeloppervlak staat in het punt waar de lichtstraal invalt.
</div>

<h4>Weerkaatsing: diffuus versus spiegelend</h4>
<p>Wanneer licht op een oppervlak valt, gebeurt een van de volgende dingen:</p>
<ul>
  <li><b>Diffuus weerkaatsen:</b> Als het oppervlak ruw of oneffen is (zoals papier, kleding, een houten tafel of je huid), worden de invallende lichtstralen in alle mogelijke richtingen verstrooid. Hierdoor kun je het voorwerp vanuit elke hoek scherp zien en ontstaan er geen felle schitteringen.</li>
  <li><b>Spiegelend weerkaatsen:</b> Als het oppervlak extreem glad en egaal is (zoals een vlakke spiegel of een rimpelloos wateroppervlak), worden evenwijdige invallende stralen in één specifieke richting teruggekaatst. Hierdoor zie je een spiegelbeeld.</li>
  <li><b>Doorlaten en absorberen:</b> Een transparant materiaal zoals vensterglas laat het merendeel van het licht door. Een donker of mat oppervlak absorbeert een groot deel van het licht en zet dit om in warmte.</li>
</ul>

<h4>Schaduwvorming: kernschaduw en halfschaduw</h4>
<p>Omdat licht in rechte lijnen beweegt, ontstaat achter een ondoorzichtig voorwerp een schaduw:</p>
<ul>
  <li>Bij een <b>puntvormige lichtbron</b> (zeer kleine bron) ontstaat een scherpe schaduw met alleen een <b>kernschaduw</b> (waar helemaal geen licht van de bron kan komen).</li>
  <li>Bij een <b>uitgebreide lichtbron</b> (zoals een tl-buis of de zon) ontstaat in het midden een kernschaduw, omgeven door een <b>halfschaduw</b> (gebied waar slechts een deel van de lichtbron zichtbaar is).</li>
</ul>

<h4>Spiegelbeeld construeren</h4>
<p>Bij een vlakke spiegel heeft het spiegelbeeld bijzondere eigenschappen:</p>
<ol>
  <li>Het spiegelbeeld staat even ver achter de spiegel als het voorwerp ervoor staat: <b>d<sub>voorwerp</sub> = d<sub>beeld</sub></b>.</li>
  <li>De verbindingslijn tussen voorwerppunt en beeldpunt staat altijd loodrecht op het spiegeloppervlak.</li>
  <li>Het spiegelbeeld is een <b>virtueel beeld</b>: het bevindt zich niet werkelijk achter de spiegel en je kunt het niet op een scherm opvangen. Als je achter de spiegel kijkt, is er niets.</li>
  <li>Om een lichtstraal naar het oog te construeren, trek je vanuit het oog een rechte lijn naar het virtuele beeldpunt achter de spiegel. Waar deze lijn de spiegel snijdt, bevindt zich het invalspunt; vanaf daar teken je de werkelijke lichtstraal vanaf het voorwerp.</li>
</ol>
<div class='begrippen-box'>
<b>Tip voor de toets:</b> Vergeet bij het tekenen van de spiegelwet nooit eerst de normaal te tekenen! De hoek van inval en de hoek van terugkaatsing worden ALTIJD gemeten tussen de lichtstraal en de normaal, NOOIT tussen de lichtstraal en de spiegel zelf.
</div>""",
        "vragen": [
            {
                "type": "mc",
                "vraag": "Wat is een natuurkundig voorbeeld van een voorwerp dat <b>indirect licht</b> uitzendt?",
                "opties": ["De maan aan de nachtelijke hemel", "Een brandende kaars", "De zon", "Een ingeschakelde smartphoneflitser"],
                "antwoord": 0,
                "uitleg": "De maan geeft zelf geen licht, maar weerkaatst zonlicht naar de aarde. Dat is een klassiek voorbeeld van indirect licht."
            },
            {
                "type": "mc",
                "vraag": "Licht valt op een spiegel met een hoek van 35° ten opzichte van de normaal. Hoe groot is de hoek van terugkaatsing?",
                "opties": ["55°", "35°", "70°", "90°"],
                "antwoord": 1,
                "uitleg": "Volgens de spiegelwet geldt hoek van inval = hoek van terugkaatsing (∠i = ∠t). Dus ∠t = 35°."
            },
            {
                "type": "mc",
                "vraag": "Waarom kunnen klasgenoten vanuit alle hoeken van het lokaal het krijtbord of whiteboard lezen?",
                "opties": ["Doordat het oppervlak het licht absorbeert", "Doordat het oppervlak het licht spiegelend weerkaatst", "Doordat het oppervlak het licht diffuus in alle richtingen weerkaatst", "Doordat het bord zelf een actieve lichtbron is"],
                "antwoord": 2,
                "uitleg": "Door diffuse weerkaatsing wordt het licht naar alle kanten verstrooid, waardoor het oppervlak vanuit elke gezichtshoek zichtbaar is."
            },
            {
                "type": "mc",
                "vraag": "Een voorwerp staat op 40 cm afstand vóór een vlakke spiegel. Hoe groot is de afstand tussen het voorwerp en zijn virtuele spiegelbeeld?",
                "opties": ["20 cm", "40 cm", "60 cm", "80 cm"],
                "antwoord": 3,
                "uitleg": "Het beeld staat 40 cm áchter de spiegel. De totale afstand van het voorwerp tot het spiegelbeeld is 40 cm + 40 cm = 80 cm."
            },
            {
                "type": "waaronwaar",
                "vraag": "Bij een vlakke spiegel is het spiegelbeeld een reëel beeld dat je op een wit projectiescherm achter de spiegel kunt opvangen.",
                "antwoord": False,
                "uitleg": "Onwaar: Het spiegelbeeld is een virtueel beeld. De lichtstralen komen niet werkelijk achter de spiegel vandaan; je kunt het niet op een scherm opvangen."
            },
            {
                "type": "waaronwaar",
                "vraag": "De normaal is een denkbeeldige lijn die onder een hoek van 90 graden (loodrecht) op het spiegeloppervlak staat.",
                "antwoord": True,
                "uitleg": "Waar: De normaal staat altijd exact loodrecht op het spiegelende oppervlak in het invalspunt."
            },
            {
                "type": "waaronwaar",
                "vraag": "Een hoek van inval van 0° betekent dat de lichtstraal evenwijdig langs het spiegeloppervlak strijkt.",
                "antwoord": False,
                "uitleg": "Onwaar: Een invalshoek van 0° betekent dat de straal samenvalt met de normaal, en dus loodrecht op de spiegel invalt."
            },
            {
                "type": "waaronwaar",
                "vraag": "Bij een uitgebreide lichtbron ontstaat om de donkere kernschaduw heen een gebied dat halfschaduw wordt genoemd.",
                "antwoord": True,
                "uitleg": "Waar: In de halfschaduw wordt slechts een deel van de lichtbron door het ondoorzichtige voorwerp afgeschermd."
            },
            {
                "type": "invoer",
                "vraag": "Als een lichtstraal invalt op een spiegel en een hoek van 30° maakt met het spiegeloppervlak zelf, hoeveel graden is dan de hoek van inval (ten opzichte van de normaal)?",
                "antwoord": "60|60 graden|60°",
                "uitleg": "De hoek met de normaal is 90° - 30° = 60°."
            },
            {
                "type": "invoer",
                "vraag": "Hoe noem je de weerkaatsing van licht op een ruw oppervlak waarbij het licht in alle richtingen wordt verstrooid?",
                "antwoord": "diffuus|diffuse|diffuse weerkaatsing|diffuus weerkaatsen",
                "uitleg": "Op ruwe oppervlakken weerkaatst licht diffuus (diffuse weerkaatsing)."
            }
        ]
    },
    {
        "id": "h5-2-breking",
        "hoofdstuk": 5,
        "paragraaf": "5.2",
        "titel": "Breking van licht",
        "korteUitleg": "Lichtbreking bij grensvlakken, breking naar en van de normaal, bolle en holle lenzen, brandpunt en brandpuntsafstand.",
        "icoon": "💡",
        "kleur": "h5-thema",
        "theorie": """<h3>5.2 Breking van licht</h3>
<div class='formule-box'>
<strong>Belangrijke definities en regels:</strong><br>
• <b>Lichtbreking (refractie):</b> De richtingsverandering van een lichtstraal wanneer deze schuin overgaat van de ene doorzichtige tussenstof naar de andere.<br>
• <b>Oorzaak van breking:</b> Licht heeft in verschillende stoffen een verschillende voortplantingssnelheid (in vacuüm/lucht ca. 300.000 km/s, in water ca. 225.000 km/s, in glas ca. 200.000 km/s).<br>
• <b>Breking naar de normaal toe:</b> Bij de overgang van een optisch minder dichte stof naar een dichtere stof (zoals van lucht naar water of glas) geldt: <b>∠r < ∠i</b> (de hoek van breking is kleiner dan de hoek van inval).<br>
• <b>Breking van de normaal af:</b> Bij de overgang van een dichtere stof naar een minder dichte stof (zoals van water of glas naar lucht) geldt: <b>∠r > ∠i</b> (de straal buigt weg van de normaal).<br>
• <b>Loodrechte inval (∠i = 0°):</b> Als het licht loodrecht op het grensvlak invalt, verandert de richting niet (∠r = 0°).
</div>

<h4>Bolle en holle lenzen</h4>
<p>Lenzen maken gebruik van lichtbreking om lichtbundels van vorm te veranderen:</p>
<ul>
  <li><b>Bolle lens (positieve lens, symbool +):</b>
    <ul>
      <li>Het midden van de lens is <b>dikker</b> dan de randen.</li>
      <li>Werkt <b>convergerend</b>: een evenwijdige invallende lichtbundel wordt naar elkaar toe gebogen en komt samen in één punt: het <b>brandpunt (F)</b>.</li>
      <li>De afstand van het optisch middelpunt van de lens tot het brandpunt heet de <b>brandpuntsafstand (f)</b>.</li>
      <li>Hoe boller de lens is geslepen, hoe sterker hij het licht breekt en des te <b>korter</b> is de brandpuntsafstand f.</li>
    </ul>
  </li>
  <li><b>Holle lens (negatieve lens, symbool -):</b>
    <ul>
      <li>Het midden van de lens is <b>dunner</b> dan de randen.</li>
      <li>Werkt <b>divergerend</b>: een evenwijdige invallende lichtbundel wordt uit elkaar gebogen.</li>
      <li>De uit elkaar wijkende lichtstralen lijken afkomstig te zijn van een denkbeeldig punt vóór de lens: het <b>virtuele brandpunt</b>.</li>
    </ul>
  </li>
</ul>

<h4>Omkeerbaarheid van de lichtweg</h4>
<p>Een fundamentele eigenschap van lichtstralen is dat de lichtweg omkeerbaar is: als je een lichtstraal in omgekeerde richting door een grensvlak of lens stuurt, volgt hij exact dezelfde baan. Als een straal van lucht naar glas onder een hoek van 40° breekt naar 25°, dan zal een straal vanuit glas onder 25° in lucht precies onder 40° uittreden.</p>

<div class='begrippen-box'>
<b>Onthoud voor proefwerken:</b>
• Een positieve lens verzamelt licht (convergeert).<br>
• Een negatieve lens spreidt licht (divergeert).<br>
• Brandpuntsafstand f wordt altijd gemeten vanaf het midden van de lens tot het brandpunt F.
</div>""",
        "vragen": [
            {
                "type": "mc",
                "vraag": "Wat gebeurt er met een schuin invallende lichtstraal die vanuit de lucht het water in gaat?",
                "opties": ["De lichtstraal breekt naar de normaal toe", "De lichtstraal breekt van de normaal af", "De lichtstraal gaat zonder van richting te veranderen rechtdoor", "De lichtstraal buigt altijd in een hoek van 90 graden om"],
                "antwoord": 0,
                "uitleg": "Omdat water optisch dichter is dan lucht (het licht vertraagt), breekt de lichtstraal naar de normaal toe: hoek r is kleiner dan hoek i."
            },
            {
                "type": "mc",
                "vraag": "Welk kenmerk hoort bij een <b>positieve (bolle) lens</b>?",
                "opties": ["De lens is in het midden dunner dan aan de randen", "De lens heeft een divergerende werking op licht", "De lens laat evenwijdige lichtstralen samenkomen in het brandpunt (convergerend)", "De lens heeft geen brandpunt"],
                "antwoord": 2,
                "uitleg": "Een positieve (bolle) lens is in het midden dikker en heeft een convergerende werking: evenwijdige stralen worden naar het brandpunt toe gebogen."
            },
            {
                "type": "mc",
                "vraag": "Hoe verandert de brandpuntsafstand f als je een bolle lens nóg boller slijpt?",
                "opties": ["De brandpuntsafstand wordt oneindig groot", "De brandpuntsafstand verandert niet", "De brandpuntsafstand wordt groter", "De brandpuntsafstand wordt kleiner"],
                "antwoord": 3,
                "uitleg": "Hoe boller de lens, des te sterker hij licht breekt. De lichtstralen kruisen de hoofdas dichter bij de lens, dus de brandpuntsafstand f wordt kleiner."
            },
            {
                "type": "mc",
                "vraag": "Wat gebeurt er als een lichtstraal exact loodrecht (onder een hoek van 0° met de normaal) invalt op een glasplaat?",
                "opties": ["De lichtstraal buigt 45 graden af", "De lichtstraal plant zich in dezelfde richting voort zonder knik", "De lichtstraal wordt voor 100% teruggekaatst als spiegelbeeld", "De lichtstraal splitst direct in een regenboog"],
                "antwoord": 1,
                "uitleg": "Bij loodrechte inval (hoek van inval = 0°) is de hoek van breking ook 0°. De straal gaat kaarsrecht door het grensvlak heen."
            },
            {
                "type": "waaronwaar",
                "vraag": "Een holle lens (negatieve lens) buigt evenwijdige lichtstralen uit elkaar (divergerende werking).",
                "antwoord": True,
                "uitleg": "Waar: Een holle lens spreidt het licht; de uittredende stralen wijken divergerend uiteen."
            },
            {
                "type": "waaronwaar",
                "vraag": "Wanneer licht van glas naar lucht overgaat, breekt de lichtstraal naar de normaal toe.",
                "antwoord": False,
                "uitleg": "Onwaar: Bij de overgang van glas naar lucht (van dichter naar minder dicht) breekt de lichtstraal juist VÁN de normaal af."
            },
            {
                "type": "waaronwaar",
                "vraag": "De afstand tussen het optisch middelpunt van een lens en het brandpunt noem je de brandpuntsafstand (f).",
                "antwoord": True,
                "uitleg": "Waar: Dit is exact de formele definitie van de brandpuntsafstand f."
            },
            {
                "type": "waaronwaar",
                "vraag": "De hoofdas van een lens is een kromme lijn die langs de buitenrand van de lens loopt.",
                "antwoord": False,
                "uitleg": "Onwaar: De hoofdas is een denkbeeldige rechte lijn die loodrecht door het exacte midden (optisch middelpunt) van de lens loopt."
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
    },
    {
        "id": "h5-3-construeren-bij-lenzen",
        "hoofdstuk": 5,
        "paragraaf": "5.3",
        "titel": "Construeren bij lenzen",
        "korteUitleg": "De drie constructiestralen bij een positieve lens, reëel en virtueel beeld, voorwerps- en beeldafstand en vergroting.",
        "icoon": "🔍",
        "kleur": "h5-thema",
        "theorie": """<h3>5.3 Beelden construeren bij positieve lenzen</h3>
<div class='formule-box'>
<strong>Constructieregels voor een positieve lens:</strong><br>
Om de beeldvorming van een voorwerp te bepalen, teken je vanuit het topje van het voorwerp (punt L of Q) minimaal twee van de volgende <b>drie constructiestralen</b>:<br>
1. <b>Constructiestraal 1 (evenwijdig):</b> Loopt vanaf het voorwerppunt evenwijdig aan de hoofdas naar de lens, breekt in de lens en gaat achter de lens <b>door het brandpunt F</b>.<br>
2. <b>Constructiestraal 2 (middelpunt):</b> Loopt vanaf het voorwerppunt recht door het <b>optisch middelpunt O</b> van de lens en gaat <b>ongebroken rechtdoor</b>.<br>
3. <b>Constructiestraal 3 (brandpuntsstraal):</b> Gaat vóór de lens door het brandpunt F naar de lens toe, en loopt achter de lens <b>evenwijdig aan de hoofdas</b> verder.<br>
Het snijpunt van deze stralen achter de lens vormt het bijbehorende <b>beeldpunt (L' of Q')</b>.
</div>

<h4>Begrippen en afstanden</h4>
<ul>
  <li><b>Voorwerpsafstand (v):</b> De afstand van het voorwerp tot het midden van de lens.</li>
  <li><b>Beeldafstand (b):</b> De afstand van het scherpe beeld (op scherm of sensor) tot het midden van de lens.</li>
  <li><b>Voorwerpsgrootte (L<sub>v</sub>):</b> De werkelijke hoogte van het voorwerp in cm of mm.</li>
  <li><b>Beeldgrootte (L<sub>b</sub>):</b> De hoogte van het gevormde beeld in cm of mm.</li>
</ul>

<h4>Eigenschappen van het beeld bij verschillende voorwerpsafstanden</h4>
<p>Afhankelijk van waar je het voorwerp neerzet ten opzichte van de brandpuntsafstand f, ontstaat een ander type beeld:</p>
<ul>
  <li><b>v > 2f (voorwerp ver weg, zoals bij een fotocamera):</b>
    Het beeld bevindt zich tussen f en 2f achter de lens. Het beeld is <b>reëel</b>, staat <b>op zijn kop (omgekeerd)</b> en is <b>verkleind</b> (b < v).</li>
  <li><b>v = 2f:</b>
    Het beeld staat op afstand b = 2f achter de lens. Het beeld is <b>reëel, omgekeerd</b> en <b>even groot</b> als het voorwerp (L<sub>b</sub> = L<sub>v</sub>).</li>
  <li><b>f < v < 2f (zoals bij een filmprojector of beamer):</b>
    Het beeld bevindt zich voorbij 2f (b > 2f). Het beeld is <b>reëel, omgekeerd</b> en <b>vergroot</b> (b > v).</li>
  <li><b>v = f:</b>
    De uittredende stralen lopen evenwijdig aan elkaar en snijden elkaar nergens; er ontstaat <b>geen beeld</b>.</li>
  <li><b>v < f (voorwerp heel dichtbij, zoals bij een loep):</b>
    De uittredende stralen wijken uiteen. Aan de voorkant van de lens lijken ze uit één punt te komen. Er ontstaat een <b>virtueel, rechtopstaand en vergroot beeld</b>.</li>
</ul>

<h4>Vergroting N</h4>
<p>De vergrotingsfactor N geeft aan hoeveel keer groter of kleiner het beeld is dan het voorwerp:</p>
<div class='formule-box'>
<b>N = L<sub>b</sub> / L<sub>v</sub> = b / v</b><br>
<i>(Let op: N is een verhouding en heeft geen eenheid. Zorg dat L<sub>b</sub> en L<sub>v</sub>, respectievelijk b en v, in dezelfde eenheid staan!)</i>
</div>""",
        "vragen": [
            {
                "type": "mc",
                "vraag": "Wat doet een constructiestraal die evenwijdig aan de hoofdas op een positieve lens invalt?",
                "opties": ["Hij breekt na de lens door het optisch middelpunt", "Hij breekt na de lens door het brandpunt F achter de lens", "Hij kaatst onder dezelfde hoek terug", "Hij gaat zonder te breken evenwijdig rechtdoor"],
                "antwoord": 1,
                "uitleg": "Constructiestraal 1 loopt evenwijdig aan de hoofdas en breekt na de positieve lens door het brandpunt F aan de overzijde."
            },
            {
                "type": "mc",
                "vraag": "Wat doet een constructiestraal die door het optisch middelpunt O van een dunne lens gaat?",
                "opties": ["Hij breekt naar het brandpunt toe", "Hij buigt 90 graden af", "Hij gaat ongebroken in een rechte lijn rechtdoor", "Hij wordt diffuus verstrooid"],
                "antwoord": 2,
                "uitleg": "Een lichtstraal die door het optisch middelpunt O van de lens valt, verandert niet van richting en gaat rechtdoor."
            },
            {
                "type": "mc",
                "vraag": "Bij een beamer staat het voorwerp (het lcd-schermpje) tussen 1f en 2f van de lens. Welke eigenschappen heeft het geprojecteerde beeld op de muur?",
                "opties": ["Virtueel, rechtopstaand en verkleind", "Reëel, rechtopstaand en even groot", "Virtueel, omgekeerd en vergroot", "Reëel, omgekeerd en vergroot"],
                "antwoord": 3,
                "uitleg": "Wanneer het voorwerp tussen 1f en 2f staat (voorwerpsafstand v tussen f en 2f), ontstaat aan de andere kant van de lens een reëel, omgekeerd en vergroot beeld op een beeldafstand groter dan 2f."
            },
            {
                "type": "mc",
                "vraag": "Een voorwerp met hoogte Lv = 5 cm levert een scherp reëel beeld op met hoogte Lb = 15 cm. Wat is de vergrotingsfactor N?",
                "opties": ["N = 3", "N = 0,33", "N = 75", "N = 10"],
                "antwoord": 0,
                "uitleg": "De vergrotingsfactor is N = Lb / Lv = 15 cm / 5 cm = 3."
            },
            {
                "type": "waaronwaar",
                "vraag": "Een reëel beeld dat door een bolle lens op een scherm wordt geprojecteerd, staat altijd op zijn kop (omgekeerd) vergeleken met het origineel.",
                "antwoord": True,
                "uitleg": "Waar: Reële beelden die ontstaan door een enkele positieve lens zijn altijd geïnverteerd (ondersteboven)."
            },
            {
                "type": "waaronwaar",
                "vraag": "Wanneer je een positieve lens gebruikt als vergrootglas (loep), zet je het voorwerp verder weg dan tweemaal de brandpuntsafstand (v > 2f).",
                "antwoord": False,
                "uitleg": "Onwaar: Voor een loep moet het voorwerp juist dichterbij staan dan het brandpunt (v < f), zodat er een vergroot virtueel beeld ontstaat."
            },
            {
                "type": "waaronwaar",
                "vraag": "Als de beeldafstand b gelijk is aan de voorwerpsafstand v, is de vergrotingsfactor N exact gelijk aan 1.",
                "antwoord": True,
                "uitleg": "Waar: Omdat N = b / v, is N = 1 wanneer b = v. Het beeld is dan precies even groot als het voorwerp."
            },
            {
                "type": "waaronwaar",
                "vraag": "Om een beeldpunt te construeren moet je altijd minimaal 10 verschillende lichtstralen tekenen.",
                "antwoord": False,
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
    },
    {
        "id": "h5-4-oogafwijkingen",
        "hoofdstuk": 5,
        "paragraaf": "5.4",
        "titel": "Oogafwijkingen en brillen",
        "korteUitleg": "Werking van het menselijk oog, accommoderen, verte- en nabijheidspunt, bijziendheid, verziendheid en oudziendheid.",
        "icoon": "👓",
        "kleur": "h5-thema",
        "theorie": """<h3>5.4 Oogafwijkingen en brillenglazen</h3>
<div class='formule-box'>
<strong>Hoe het menselijk oog werkt:</strong><br>
• <b>Ooglens:</b> Een flexibele, bolle (positieve) lens die een omgekeerd, verkleind reëel beeld op het <b>netvlies (retina)</b> projecteert.<br>
• <b>Netvlies:</b> Bevat lichtgevoelige zintuigcellen (staafjes en kegeltjes) die het lichtsignaal via de oogzenuw naar de hersenen sturen.<br>
• <b>Accommoderen:</b> Het boller maken van de ooglens door het aanspannen van de kringspiertjes in het oog. Hierdoor wordt de lens sterker (f wordt kleiner) en kun je voorwerpen van dichtbij scherpstellen.<br>
• <b>Ontspannen oog:</b> Als je in de verte kijkt, is de oogspier ontspannen en is de ooglens platter (zo min mogelijk bol).<br>
• <b>Vertepunt (V):</b> Het verste punt dat je met ontspannen oog scherp kunt zien (voor een gezond oog ligt dit op oneindig, ∞).<br>
• <b>Nabijheidspunt (N):</b> Het dichtstbijzijnde punt dat je met maximale accommodatie nog net scherp kunt zien (voor een jong volwassene ca. 25 cm).
</div>

<h4>De drie grote oogafwijkingen</h4>
<table style='width:100%; border-collapse:collapse; margin:10px 0;'>
  <tr style='background:rgba(0,0,0,0.05); text-align:left;'>
    <th style='padding:8px; border:1px solid #ccc;'>Afwijking</th>
    <th style='padding:8px; border:1px solid #ccc;'>Oorzaak & Beeldvorming</th>
    <th style='padding:8px; border:1px solid #ccc;'>Symptoom</th>
    <th style='padding:8px; border:1px solid #ccc;'>Correctie (hulplens)</th>
  </tr>
  <tr>
    <td style='padding:8px; border:1px solid #ccc;'><b>Bijziendheid<br>(myopie)</b></td>
    <td style='padding:8px; border:1px solid #ccc;'>Oogbol is <b>te lang</b> of de ooglens is van nature <b>te bol / te sterk</b>. Evenwijdige lichtstralen van ver weg vallen <b>vóór het netvlies</b> samen.</td>
    <td style='padding:8px; border:1px solid #ccc;'>Ziet dichtbij prima scherp, maar veraf wazig. Vertepunt ligt te dichtbij.</td>
    <td style='padding:8px; border:1px solid #ccc;'><b>Negatieve (holle) lens (-)</b>.<br>Divergeert het licht vooraf zodat het precies op het netvlies valt.</td>
  </tr>
  <tr>
    <td style='padding:8px; border:1px solid #ccc;'><b>Verziendheid<br>(hypermetropie)</b></td>
    <td style='padding:8px; border:1px solid #ccc;'>Oogbol is <b>te kort</b> of de ooglens is <b>te plat / te zwak</b>. Met ontspannen lens valt het beeld <b>achter het netvlies</b>.</td>
    <td style='padding:8px; border:1px solid #ccc;'>Moet al accommoderen om in de verte scherp te zien. Dichtbij lezen kost enorme inspanning of lukt niet.</td>
    <td style='padding:8px; border:1px solid #ccc;'><b>Positieve (bolle) lens (+)</b>.<br>Convergeert het licht vooraf ter ondersteuning van de zwakke ooglens.</td>
  </tr>
  <tr>
    <td style='padding:8px; border:1px solid #ccc;'><b>Oudziendheid<br>(presbyopie)</b></td>
    <td style='padding:8px; border:1px solid #ccc;'>De ooglens verliest op latere leeftijd (vanaf ca. 45 jaar) zijn <b>elasticiteit</b> en kan niet meer voldoende bol worden (accommodatiekracht neemt af).</td>
    <td style='padding:8px; border:1px solid #ccc;'>Ver zien blijft vaak goed, maar het nabijheidspunt schuift naar achteren (boek moet ver weg worden gehouden).</td>
    <td style='padding:8px; border:1px solid #ccc;'><b>Positieve leesbril (+)</b>.<br>Ondersteunt het oog uitsluitend bij dichtbij kijken.</td>
  </tr>
</table>

<div class='begrippen-box'>
<b>Ezelsbruggetje:</b><br>
• <b>B</b>ijziend = dichtbij goed, veraf slecht ➔ <b>M</b>in-bril (-).<br>
• <b>V</b>erziend = veraf beter, dichtbij slecht ➔ <b>P</b>lus-bril (+).
</div>""",
        "vragen": [
            {
                "type": "mc",
                "vraag": "Wat gebeurt er in een gezond oog wanneer je kijkt naar een voorwerp dat heel dichtbij staat (bijvoorbeeld een boek op 25 cm)?",
                "opties": ["De ooglens ontspant en wordt platter", "De ooglens accommodeert en wordt boller", "De pupil sluit zich volledig af", "Het netvlies schuift 2 cm naar achteren"],
                "antwoord": 1,
                "uitleg": "Om dichtbij scherp te zien, spant de kringspier aan en accommodeert de ooglens: hij wordt boller en sterker."
            },
            {
                "type": "mc",
                "vraag": "Iemand die <b>bijziend</b> is heeft moeite met scherp zien in de verte. Wat is hiervan de anatomische oorzaak?",
                "opties": ["De oogbol is te kort en het beeld valt achter het netvlies", "De ooglens is vertroebeld door ouderdom", "De oogbol is te lang (of lens te sterk), waardoor het beeld vóór het netvlies valt", "De oogzenuw stuurt het beeld ondersteboven door"],
                "antwoord": 2,
                "uitleg": "Bij bijziendheid is het oog relatief te lang (of te sterk brekend); het beeld van voorwerpen in de verte ontstaat vóór het netvlies."
            },
            {
                "type": "mc",
                "vraag": "Met welk type brillenglas kan een <b>bijziend</b> persoon gecorrigeerd worden?",
                "opties": ["Een positieve bolle lens (+)", "Een cilindrische spiegel", "Een polariserend zonneglas", "Een negatieve holle lens (-)"],
                "antwoord": 3,
                "uitleg": "Bijziendheid wordt verholpen met een negatieve (holle, divergerende) lens die het licht vooraf iets spreidt."
            },
            {
                "type": "mc",
                "vraag": "Waardoor ontstaat <b>oudziendheid</b> bij mensen boven de 45 jaar?",
                "opties": ["De ooglens wordt stugger en minder elastisch, waardoor accommoderen minder goed lukt", "De oogbol groeit plotseling 5 millimeter langer", "Het netvlies raakt beschadigd door uv-straling", "De hoornvlieskromming wordt volledig plat"],
                "antwoord": 0,
                "uitleg": "Bij het ouder worden verliest de ooglens zijn flexibiliteit. Hij kan daardoor niet meer voldoende bol worden getrokken om dichtbij scherp te stellen."
            },
            {
                "type": "waaronwaar",
                "vraag": "Een verziend persoon heeft een positieve bril (met bolle lenzen, +) nodig om comfortabel te kunnen lezen.",
                "antwoord": True,
                "uitleg": "Waar: Verziendheid ontstaat doordat het oog te zwak convergeert. Een positieve hulplens helpt de lichtstralen te convergeren op het netvlies."
            },
            {
                "type": "waaronwaar",
                "vraag": "Bij een volledig ontspannen oog zijn de kringspiertjes maximaal aangespannen en is de ooglens kogelrond.",
                "antwoord": False,
                "uitleg": "Onwaar: Bij ontspanning zijn de spiertjes ontspannen en is de ooglens juist zo plat mogelijk (aangepast voor ver weg)."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het vertepunt van een gezond oog ligt in theorie op oneindig (∞).",
                "antwoord": True,
                "uitleg": "Waar: Een gezond oog kan sterren en wolken op oneindige afstand haarscherp zien zonder spierinspanning."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het beeld dat de menselijke ooglens op het netvlies projecteert staat rechtop en is vergroot.",
                "antwoord": False,
                "uitleg": "Onwaar: De bolle ooglens vormt een reëel, omgekeerd (op zijn kop) en verkleind beeld op het netvlies. Onze hersenen corrigeren dit."
            },
            {
                "type": "invoer",
                "vraag": "Hoe noem je het vermogen van het oog om de lens boller te maken voor het scherpstellen op voorwerpen dichtbij?",
                "antwoord": "accommoderen|accommodatie",
                "uitleg": "Dit proces heet accommoderen (de accommodatie van het oog)."
            },
            {
                "type": "invoer",
                "vraag": "Welk type hulplens (positief of negatief) heeft een persoon met oudziendheid nodig voor een leesbril?",
                "antwoord": "positief|positieve lens|positieve|+",
                "uitleg": "Een leesbril heeft positieve (+) lenzen om het tekort aan accommodatievermogen aan te vullen."
            }
        ]
    },
    {
        "id": "h5-5-rekenen-aan-lenzen",
        "hoofdstuk": 5,
        "paragraaf": "5.5",
        "titel": "Rekenen aan lenzen",
        "korteUitleg": "De lenzenformule 1/f = 1/v + 1/b, lenssterkte in dioptrie (S = 1/f) en vergroting N.",
        "icoon": "📐",
        "kleur": "h5-thema",
        "theorie": """<h3>5.5 Rekenen aan lenzen en lenssterkte</h3>
<div class='formule-box'>
<strong>De wiskundige formules voor lenzen:</strong><br>
• <b>De lenzenformule:</b>
<div style='font-size:1.2em; text-align:center; margin:8px 0;'><b>1 / f = 1 / v + 1 / b</b></div>
waarbij:<br>
- <b>f</b> = brandpuntsafstand in centimeter (cm) of meter (m)<br>
- <b>v</b> = voorwerpsafstand in dezelfde lengte-eenheid (cm of m)<br>
- <b>b</b> = beeldafstand in dezelfde lengte-eenheid (cm of m)<br>
<i>(Let op: alle drie de grootheden f, v en b moeten in EXACT dezelfde eenheid worden ingevuld!)</i><br><br>

• <b>De lineaire vergroting N:</b>
<div style='font-size:1.2em; text-align:center; margin:8px 0;'><b>N = L<sub>b</sub> / L<sub>v</sub> = b / v</b></div>
- Als N > 1 is het beeld groter dan het voorwerp (vergroot).<br>
- Als N < 1 is het beeld kleiner dan het voorwerp (verkleind).<br>
- Als N = 1 is het beeld even groot als het voorwerp (b = v = 2f).<br><br>

• <b>Lenssterkte S in dioptrie (dpt):</b>
<div style='font-size:1.2em; text-align:center; margin:8px 0;'><b>S = 1 / f</b></div>
<i>CRUCIALE REGEL: Voor dioptrie MOET de brandpuntsafstand f ALTIJD in <b>meters (m)</b> worden ingevuld!</i><br>
- Positieve lens: f is positief ➔ S is positief (bijv. f = +0,25 m ➔ S = +4,0 dpt).<br>
- Negatieve lens: f is negatief ➔ S is negatief (bijv. f = -0,50 m ➔ S = -2,0 dpt).
</div>

<h4>Stappenplan voor het rekenen met de lenzenformule</h4>
<ol>
  <li><b>Gegevens opschrijven:</b> Noteer f, v en b en zet ze om naar dezelfde eenheid (meestal cm).</li>
  <li><b>Formule noteren:</b> 1/f = 1/v + 1/b.</li>
  <li><b>Onbekende isoleren:</b>
    <ul>
      <li>Zoek je b? Dan geldt: <b>1/b = 1/f - 1/v</b>.</li>
      <li>Zoek je v? Dan geldt: <b>1/v = 1/f - 1/b</b>.</li>
      <li>Zoek je f? Dan tel je 1/v en 1/b bij elkaar op en neem je het omgekeerde (1 / uitkomst).</li>
    </ul>
  </li>
  <li><b>Vergeet niet om te keren!</b> Nadat je bijvoorbeeld 1/b hebt uitgerekend, moet je nog delen: <b>b = 1 / (1/b)</b>.</li>
</ol>

<h4>Voorbeeld uit het tekstboek</h4>
<p>Een dia staat op voorwerpsafstand v = 5,0 cm van een projectorlens met brandpuntsafstand f = 4,0 cm. Waar ontstaat het scherpe beeld op de muur?</p>
<ul>
  <li>1/b = 1/f - 1/v = 1/4,0 - 1/5,0 = 0,25 - 0,20 = 0,05 cm<sup>-1</sup></li>
  <li>b = 1 / 0,05 = <b>20 cm</b>.</li>
  <li>De vergroting is N = b / v = 20 / 5,0 = <b>4×</b>. Het beeld op de muur is 4 keer zo groot als het origineel!</li>
</ul>""",
        "vragen": [
            {
                "type": "mc",
                "vraag": "Wat is de lenssterkte S in dioptrie van een positieve lens met een brandpuntsafstand van f = 20 cm?",
                "opties": ["+0,05 dpt", "+5 dpt", "+20 dpt", "+0,2 dpt"],
                "antwoord": 1,
                "uitleg": "Eerst omrekenen naar meter: f = 20 cm = 0,20 m. Daarna geldt S = 1 / f = 1 / 0,20 = +5 dpt."
            },
            {
                "type": "mc",
                "vraag": "Een lens heeft een sterkte van S = -4 dpt. Wat voor lens is dit en wat is de brandpuntsafstand?",
                "opties": ["Een bolle lens met f = +25 cm", "Een holle lens met f = -4 meter", "Een negatieve (holle) lens met f = -25 cm (-0,25 m)", "Een vlakke spiegel zonder brandpunt"],
                "antwoord": 2,
                "uitleg": "Het minteken duidt op een negatieve lens. f = 1 / S = 1 / (-4) = -0,25 m = -25 cm."
            },
            {
                "type": "mc",
                "vraag": "Een voorwerp staat op v = 30 cm van een lens met f = 10 cm. Op welke beeldafstand b ontstaat het scherpe beeld?",
                "opties": ["b = 20 cm", "b = 10 cm", "b = 40 cm", "b = 15 cm"],
                "antwoord": 3,
                "uitleg": "1/b = 1/f - 1/v = 1/10 - 1/30 = 3/30 - 1/30 = 2/30 = 1/15. Dus b = 15 cm."
            },
            {
                "type": "mc",
                "vraag": "Een lampje staat op 60 cm van een lens. Het beeld ontstaat op 120 cm achter de lens. Hoe groot is de vergrotingsfactor N?",
                "opties": ["N = 2", "N = 0,5", "N = 7200", "N = 60"],
                "antwoord": 0,
                "uitleg": "N = b / v = 120 cm / 60 cm = 2."
            },
            {
                "type": "waaronwaar",
                "vraag": "Om de lenssterkte in dioptrie (S = 1/f) te berekenen, mag je de brandpuntsafstand f rechtstreeks in centimeters invullen.",
                "antwoord": False,
                "uitleg": "Onwaar: Voor dioptrie MOET de brandpuntsafstand f altijd strikt in meters worden omgerekend."
            },
            {
                "type": "waaronwaar",
                "vraag": "In de lenzenformule (1/f = 1/v + 1/b) moeten f, v en b alle drie in dezelfde lengte-eenheid staan.",
                "antwoord": True,
                "uitleg": "Waar: Je moet f, v en b allemaal in meters of allemaal in centimeters invullen."
            },
            {
                "type": "waaronwaar",
                "vraag": "Als de vergroting N kleiner is dan 1 (bijv. N = 0,25), betekent dit dat het beeld kleiner is dan het originele voorwerp.",
                "antwoord": True,
                "uitleg": "Waar: Bij N < 1 is het beeld verkleind (zoals bij een fotocamera die een landschap afbeeldt op een kleine sensor)."
            },
            {
                "type": "waaronwaar",
                "vraag": "Een lens met een brandpuntsafstand van 50 cm heeft een sterkte van 50 dioptrie.",
                "antwoord": False,
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
    }
]

# ---------------------------------------------------------
# EXAMENS (examen_40.js t/m examen_44.js)
# ---------------------------------------------------------

EXAMENS = [
    {
        "id": "ex-h3-natuurkunde-40",
        "hoofdstuk": 5,
        "paragraaf": "5.1",
        "titel": "Toets 40 — §5.1 Licht en beeld",
        "vak": "Natuurkunde · HAVO 3 (H5)",
        "icoon": "🔦",
        "duurMin": 30,
        "vragen": [
            # 12 MC (balanced: exactly 3 A, 3 B, 3 C, 3 D)
            {"type": "mc", "vraag": "Welk hemellichaam is een voorbeeld van een <b>directe lichtbron</b>?", "opties": ["De poolster", "De volle maan", "De planeet Venus", "Een passerende komeet"], "antwoord": 0, "uitleg": "De poolster is een ster die door kernfusie zelfstandig licht uitzendt, en is dus een directe lichtbron."},
            {"type": "mc", "vraag": "Hoe beweegt licht zich voort in een homogene, doorzichtige tussenstof zoals lucht of vacuüm?", "opties": ["In parabolische banen", "In volmaakt rechte lijnen", "In golfvormige bochten om objecten heen", "In spiraalvormige cirkels"], "antwoord": 1, "uitleg": "In een homogene stof plant licht zich altijd rechtlijnig (in rechte lijnen) voort."},
            {"type": "mc", "vraag": "Een lichtstraal valt op een vlakke spiegel. De hoek tussen de invallende lichtstraal en het spiegeloppervlak zelf is 40°. Hoe groot is de hoek van terugkaatsing?", "opties": ["40°", "80°", "50°", "90°"], "antwoord": 2, "uitleg": "De hoek met de normaal is 90° - 40° = 50°. Volgens de spiegelwet is de hoek van terugkaatsing dan ook 50°."},
            {"type": "mc", "vraag": "Wat is het fundamentele verschil tussen spiegelende en diffuse weerkaatsing?", "opties": ["Spiegelende weerkaatsing vindt alleen plaats bij gekleurd licht", "Diffuse weerkaatsing absorbeert al het invallende licht volledig", "Bij diffuse weerkaatsing geldt de spiegelwet op microscopisch niveau niet", "Bij diffuse weerkaatsing wordt het licht door een ruw oppervlak in alle richtingen verstrooid"], "antwoord": 3, "uitleg": "Op een ruw oppervlak staan de micro-oppervlakjes alle kanten op, waardoor het licht diffuus in alle richtingen wordt teruggekaatst."},
            {"type": "mc", "vraag": "Waarom noemen we het spiegelbeeld in een vlakke spiegel een <b>virtueel</b> beeld?", "opties": ["Omdat de lichtstralen niet werkelijk achter de spiegel samenkomen en je het niet op een scherm kunt opvangen", "Omdat het beeld altijd ondersteboven staat", "Omdat het beeld alleen zichtbaar is als het aardedonker is", "Omdat het beeld tweemaal zo klein is als het voorwerp"], "antwoord": 0, "uitleg": "Achter de spiegel kruisen geen echte lichtstralen; het beeld lijkt er slechts te staan voor onze ogen."},
            {"type": "mc", "vraag": "Duru staat op 1,5 meter afstand vóór een passpiegel in een kledingwinkel. Hoe ver bevindt haar spiegelbeeld zich van haar vandaan?", "opties": ["1,5 meter", "3,0 meter", "4,5 meter", "0,75 meter"], "antwoord": 1, "uitleg": "Het beeld staat 1,5 m achter de spiegel. De afstand van Duru tot haar spiegelbeeld is 1,5 m + 1,5 m = 3,0 m."},
            {"type": "mc", "vraag": "In welke situatie ontstaat achter een ondoorzichtig voorwerp zowel een kernschaduw als een halfschaduw?", "opties": ["Bij belichting door een laserpointer", "Bij belichting door een enkel klein ledlampje", "Bij belichting door een grote, uitgebreide lichtbron zoals een lange tl-buis", "In een volledig donkere kamer zonder ramen"], "antwoord": 2, "uitleg": "Een uitgebreide lichtbron zorgt voor overlappende schaduwen: kernschaduw in het midden en halfschaduw aan de randen."},
            {"type": "mc", "vraag": "Wat is de functie van de normaal bij het tekenen van lichtstralen en spiegels?", "opties": ["Het is de rand van de spiegel", "Het is de richting waarin het licht beweegt", "Het is een hulpmiddel om de dikte van het glas te meten", "Het is een loodlijn op het spiegeloppervlak die dient als referentie voor het meten van hoeken"], "antwoord": 3, "uitleg": "De normaal staat loodrecht (90°) op het oppervlak in het invalspunt; alle hoeken worden ten opzichte van deze lijn gemeten."},
            {"type": "mc", "vraag": "Wanneer je loodrecht in een spiegel kijkt (de lichtstraal valt samen met de normaal), wat is dan de hoek van inval ∠i?", "opties": ["0°", "45°", "90°", "180°"], "antwoord": 0, "uitleg": "De hoek tussen de straal en de normaal is 0 graden wanneer de straal loodrecht invalt."},
            {"type": "mc", "vraag": "Hoe verhoudt de grootte van een spiegelbeeld in een vlakke spiegel zich tot de werkelijke grootte van het voorwerp?", "opties": ["Het spiegelbeeld is altijd twee keer zo klein", "Het spiegelbeeld is exact even groot als het voorwerp", "Het spiegelbeeld is altijd uitgerekt", "Het spiegelbeeld hangt af van hoe ver je naar achteren stapt"], "antwoord": 1, "uitleg": "Een vlakke spiegel vergroot of verkleint niet; het spiegelbeeld is altijd exact even groot als het voorwerp."},
            {"type": "mc", "vraag": "Wat gebeurt er met licht dat op een matzwart geverfd houten blokje valt?", "opties": ["Het wordt voor 100% spiegelend weerkaatst", "Het wordt volledig doorgelaten als transparant materiaal", "Het wordt voor het overgrote deel geabsorbeerd en omgezet in warmte", "Het wordt omgebogen in een rechte hoek"], "antwoord": 2, "uitleg": "Donkere en zwarte oppervlakken absorberen het licht en zetten de lichtenergie om in thermische energie (warmte)."},
            {"type": "mc", "vraag": "Wat is een eigenschap van het spiegelbeeld van een klok die in een spiegel te zien is?", "opties": ["De cijfers verdwijnen volledig", "De wijzers draaien in het spiegelbeeld tegen de klok in en links en rechts zijn verwisseld", "De tijd versnelt in het spiegelbeeld", "De klok wordt ondersteboven weergegeven"], "antwoord": 1, "uitleg": "Bij een spiegelbeeld zijn voor en achter gespiegeld, waardoor optisch links en rechts verwisseld lijken."},
            # 4 Waaronwaar (at least 2 false)
            {"type": "waaronwaar", "vraag": "De spiegelwet luidt: hoek van inval is gelijk aan hoek van terugkaatsing (∠i = ∠t).", "antwoord": True, "uitleg": "Waar: Dit is de fundamentele spiegelwet van de optica."},
            {"type": "waaronwaar", "vraag": "Een vlakke spiegel kan een reëel beeld vormen dat je op een stuk wit papier achter de spiegel kunt projecteren.", "antwoord": False, "uitleg": "Onwaar: Een vlakke spiegel vormt uitsluitend een virtueel beeld."},
            {"type": "waaronwaar", "vraag": "In een kernschaduw kan een waarnemer nog steeds een klein randje van de lichtbron zien.", "antwoord": False, "uitleg": "Onwaar: In de kernschaduw is de lichtbron 100% afgeschermd. Alleen in de halfschaduw zie je een deel van de bron."},
            {"type": "waaronwaar", "vraag": "Wit papier weerkaatst invallend daglicht diffuus in alle richtingen.", "antwoord": True, "uitleg": "Waar: De vezels van het papier vormen een ruw oppervlak dat zorgt voor diffuse verstrooiing."},
            # 2 Invul
            {"type": "invul", "vraag": "De denkbeeldige hulplijn die in het invalspunt loodrecht op het spiegeloppervlak staat, noem je de ...", "antwoord": "normaal", "uitleg": "Deze loodlijn heet in de natuurkunde de normaal."},
            {"type": "invul", "vraag": "Een voorwerp dat zelf geen licht produceert maar licht van een andere bron terugkaatst, noemen we een ... lichtbron.", "antwoord": "indirecte|secundaire", "uitleg": "Dit heet een indirecte (of secundaire) lichtbron."},
            # 2 Open
            {"type": "open", "vraag": "Noem de twee belangrijkste eigenschappen van het spiegelbeeld dat ontstaat bij een vlakke spiegel (denk aan type beeld en afstand).", "sleutelwoorden": ["virtueel/virtuele", "even ver/gelijke afstand"], "minTreffers": 2, "modelantwoord": "Het beeld is een virtueel beeld en staat even ver achter de spiegel als het voorwerp ervoor staat (d_voorwerp = d_beeld).", "uitleg": "Een vlakke spiegel levert een virtueel beeld op dezelfde afstand achter de spiegel op."},
            {"type": "open", "vraag": "Leg in eigen woorden uit waarom een bioscoopscherm juist een ruw, diffuus weerkaatsend oppervlak moet hebben in plaats van een gladde spiegel.", "sleutelwoorden": ["alle richtingen/overal", "iedereen/publiek"], "minTreffers": 2, "modelantwoord": "Door diffuse weerkaatsing wordt het geprojecteerde licht in alle richtingen verstrooid, zodat bezoekers op alle zitplaatsen in de zaal het beeld duidelijk kunnen zien.", "uitleg": "Een spiegeloppervlak zou slechts één felle reflectie naar één plek sturen, terwijl diffuus oppervlak de film voor iedereen zichtbaar maakt."}
        ]
    },
    {
        "id": "ex-h3-natuurkunde-41",
        "hoofdstuk": 5,
        "paragraaf": "5.2",
        "titel": "Toets 41 — §5.2 Breking van licht",
        "vak": "Natuurkunde · HAVO 3 (H5)",
        "icoon": "💡",
        "duurMin": 30,
        "vragen": [
            # 12 MC (balanced: 3 A, 3 B, 3 C, 3 D)
            {"type": "mc", "vraag": "Wat is de natuurkundige hoofdoorzaak van het breken van een lichtstraal bij het oversteken van een grensvlak?", "opties": ["Het verschil in lichtsnelheid tussen de twee stoffen", "De temperatuur van de spiegel", "De zwaartekracht van de aarde", "De kleur van het glas"], "antwoord": 0, "uitleg": "Licht verandert van snelheid in verschillende stoffen (sneller in lucht, trager in water en glas). Hierdoor knikt de richting om."},
            {"type": "mc", "vraag": "Een lichtstraal gaat schuin van water naar lucht. Hoe verloopt de breking van de lichtstraal?", "opties": ["De lichtstraal buigt af evenwijdig aan het grensvlak", "De lichtstraal breekt van de normaal af (∠r > ∠i)", "De lichtstraal breekt naar de normaal toe (∠r < ∠i)", "De lichtstraal kaatst altijd 100% terug in het water"], "antwoord": 1, "uitleg": "Bij overgang van optisch dichtere stof (water) naar minder dichte stof (lucht) breekt het licht van de normaal af."},
            {"type": "mc", "vraag": "Wat voor soort lens is in het midden dikker dan aan de randen?", "opties": ["Een negatieve lens", "Een holle lens", "Een positieve (bolle) lens", "Een cilindrische lens"], "antwoord": 2, "uitleg": "Een bolle (positieve) lens is in het midden dikker en aan de randen dunner."},
            {"type": "mc", "vraag": "Wat gebeurt er met een evenwijdige bundel lichtstralen die door een holle lens valt?", "opties": ["De stralen worden gebundeld in een heet brandpunt", "De stralen gaan ongebroken rechtdoor", "De stralen kaatsen terug naar de bron", "De stralen wijken uit elkaar (divergerende werking)"], "antwoord": 3, "uitleg": "Een holle (negatieve) lens heeft een divergerende werking en spreidt het invallende licht."},
            {"type": "mc", "vraag": "Hoe noem je het punt waar een bolle lens evenwijdig aan de hoofdas invallende lichtstralen laat samenkomen?", "opties": ["Het brandpunt (F)", "Het optisch nulpunt", "Het prismahoekpunt", "Het weerkaatsingspunt"], "antwoord": 0, "uitleg": "Het brandpunt F is het snijpunt van evenwijdige stralen na doorgang door een positieve lens."},
            {"type": "mc", "vraag": "Wat gebeurt er met de brandpuntsafstand f wanneer een bolle lens nóg boller wordt gemaakt?", "opties": ["f blijft exact gelijk", "f wordt kleiner", "f wordt oneindig groot", "f verdubbelt"], "antwoord": 1, "uitleg": "Een bollere lens breekt sterker, waardoor de lichtstralen dichter bij de lens kruisen en de brandpuntsafstand f kleiner wordt."},
            {"type": "mc", "vraag": "Als een lichtstraal onder een hoek van 30° van lucht naar glas gaat en breekt onder een hoek van 19°, wat gebeurt er dan als je een lichtstraal vanuit het glas onder 19° naar de lucht stuurt?", "opties": ["De straal breekt in de lucht onder een hoek van 45°", "De straal gaat rechtdoor onder 19°", "De straal treedt in de lucht uit onder een hoek van 30°", "De straal kan het glas helemaal niet verlaten"], "antwoord": 2, "uitleg": "Volgens het principe van omkeerbaarheid van de lichtweg volgt het licht exact dezelfde weg in omgekeerde richting (hoek van 30°)."},
            {"type": "mc", "vraag": "Welk materiaal heeft een sterkere breking op licht dan gewoon vensterglas?", "opties": ["Lucht", "Water", "Stikstofgas", "Diamant"], "antwoord": 3, "uitleg": "Diamant heeft een zeer hoge brekingsindex (zeer lage lichtsnelheid) en breekt licht veel sterker dan glas of water."},
            {"type": "mc", "vraag": "Als een lichtstraal loodrecht (invalshoek 0°) op een dikke ruit van perspex valt, wat is dan de hoek van breking?", "opties": ["0°", "15°", "45°", "90°"], "antwoord": 0, "uitleg": "Bij loodrechte inval (invalshoek ∠i = 0°) treedt geen richtingsverandering op; ∠r = 0°."},
            {"type": "mc", "vraag": "Waarom lijkt een rietje in een glas water op het grensvlak geknikt te zijn?", "opties": ["Omdat het rietje door het water zacht wordt", "Omdat het licht dat uit het water naar je oog reist bij het grensvlak breekt", "Omdat het wateroppervlak als een spiegel werkt", "Omdat de beker trilt"], "antwoord": 1, "uitleg": "Door breking van het licht bij de overgang van water naar lucht zien onze ogen de onderkant van het rietje op een schijnbaar andere plek."},
            {"type": "mc", "vraag": "Welk schematisch symbool stelt in natuurkundetekeningen een negatieve lens voor?", "opties": ["Een cirkel met een kruis", "Een verticale lijn met pijlpunten naar buiten (+)", "Een verticale lijn met pijlpunten naar binnen (-)", "Een dubbele horizontale stippellijn"], "antwoord": 2, "uitleg": "Een negatieve lens wordt aangeduid met pijlen naar binnen of een minteken (-)."},
            {"type": "mc", "vraag": "Wat voor werking heeft een bolle lens op een evenwijdige lichtbundel?", "opties": ["Een absorberende werking", "Een divergerende werking", "Een spiegelende werking", "Een convergerende werking"], "antwoord": 3, "uitleg": "Een bolle lens convergeert het licht: de stralen worden naar elkaar toe gebogen."},
            # 4 Waaronwaar (at least 2 false)
            {"type": "waaronwaar", "vraag": "Wanneer licht van lucht naar glas overgaat, is de hoek van breking r altijd kleiner dan de hoek van inval i.", "antwoord": True, "uitleg": "Waar: Omdat glas optisch dichter is, breekt de lichtstraal naar de normaal toe (∠r < ∠i)."},
            {"type": "waaronwaar", "vraag": "Een holle lens brengt zonnestralen samen in een reëel brandpunt waar je een papiertje mee in brand kunt steken.", "antwoord": False, "uitleg": "Onwaar: Een holle lens spreidt zonnestralen juist (divergerend). Alleen een bolle lens kan zonnestralen bundelen om papier te ontsteken."},
            {"type": "waaronwaar", "vraag": "Hoe minder bol een lens is, hoe korter zijn brandpuntsafstand f.", "antwoord": False, "uitleg": "Onwaar: Een minder bolle lens breekt minder sterk, waardoor de brandpuntsafstand juist groter (langer) is."},
            {"type": "waaronwaar", "vraag": "De hoofdas van een lens staat loodrecht op de lens en loopt door het optisch middelpunt.", "antwoord": True, "uitleg": "Waar: De hoofdas is de centrale rotatiesymmetrische as van de lens."},
            # 2 Invul
            {"type": "invul", "vraag": "Het verschijnsel waarbij een lichtstraal van richting verandert bij de overgang naar een andere stof, heet ...", "antwoord": "breking|lichtbreking|refractie", "uitleg": "Dit natuurkundige verschijnsel heet breking of lichtbreking (refractie)."},
            {"type": "invul", "vraag": "De werking van een positieve lens die lichtstralen naar elkaar toe buigt, noem je een ... werking.", "antwoord": "convergerende|convergerend", "uitleg": "Een positieve lens heeft een convergerende werking."},
            # 2 Open
            {"type": "open", "vraag": "Leg uit waarom een vis in een aquarium voor iemand die er van bovenaf schuin in kijkt, op een minder diepe plek lijkt te zwemmen dan in werkelijkheid.", "sleutelwoorden": ["breking/breekt", "normaal af/oog"], "minTreffers": 2, "modelantwoord": "De lichtstralen die van de vis komen breken bij het verlaten van het wateroppervlak van de normaal af naar het oog van de waarnemer. De hersenen trekken deze lichtstralen in een rechte lijn terug, waardoor de vis schijnbaar hoger in het water ligt.", "uitleg": "Door breking van de normaal af lijkt de vis minder diep te zwemmen dan hij werkelijk is."},
            {"type": "open", "vraag": "Noem het verschil tussen de werking van een positieve lens en een negatieve lens op een evenwijdige bundel lichtstralen.", "sleutelwoorden": ["convergerend/naar elkaar", "divergerend/uit elkaar"], "minTreffers": 2, "modelantwoord": "Een positieve lens werkt convergerend en buigt de lichtstralen naar elkaar toe in het brandpunt, terwijl een negatieve lens divergerend werkt en de lichtstralen uit elkaar buigt.", "uitleg": "Positief = convergerend (bundelend); negatief = divergerend (spreidend)."}
        ]
    },
    {
        "id": "ex-h3-natuurkunde-42",
        "hoofdstuk": 5,
        "paragraaf": "5.3",
        "titel": "Toets 42 — §5.3 Construeren bij lenzen",
        "vak": "Natuurkunde · HAVO 3 (H5)",
        "icoon": "🔍",
        "duurMin": 30,
        "vragen": [
            # 12 MC (balanced: 3 A, 3 B, 3 C, 3 D)
            {"type": "mc", "vraag": "Welke constructiestraal gaat bij een positieve lens na breking door het brandpunt achter de lens?", "opties": ["De straal die evenwijdig aan de hoofdas invalt", "De straal die door het optisch middelpunt gaat", "De straal die onder 45 graden invalt", "De straal die loodrecht op de hoofdas staat"], "antwoord": 0, "uitleg": "Constructiestraal 1 loopt vóór de lens evenwijdig aan de hoofdas en breekt achter de lens door het brandpunt F."},
            {"type": "mc", "vraag": "Een voorwerp staat op grote afstand voor een positieve lens (v > 2f), zoals bij een fotocamera. Welke eigenschappen heeft het reële beeld op de sensor?", "opties": ["Rechtopstaand en vergroot", "Omgekeerd (op zijn kop) en verkleind", "Rechtopstaand en even groot", "Virtueel en oneindig ver weg"], "antwoord": 1, "uitleg": "Bij v > 2f ontstaat een reëel, omgekeerd en verkleind beeld tussen f en 2f achter de lens."},
            {"type": "mc", "vraag": "Een voorwerp met lengte Lv = 8,0 cm levert op een scherm een beeld op met lengte Lb = 24,0 cm. Wat is de vergrotingsfactor N?", "opties": ["0,33", "2,0", "3,0", "16,0"], "antwoord": 2, "uitleg": "N = Lb / Lv = 24,0 cm / 8,0 cm = 3,0."},
            {"type": "mc", "vraag": "Waar moet je een voorwerp plaatsen ten opzichte van een positieve lens om een vergroot reëel beeld op een scherm te projecteren (zoals bij een beamer)?", "opties": ["Verder weg dan tien keer de brandpuntsafstand", "Exact in het optisch middelpunt", "Tussen de lens en het voorste brandpunt (v < f)", "Tussen één en twee keer de brandpuntsafstand (f < v < 2f)"], "antwoord": 3, "uitleg": "Wanneer het voorwerp tussen 1f en 2f staat (voorwerpsafstand v tussen f en 2f), ontstaat aan de andere kant van de lens een reëel, omgekeerd en vergroot beeld op een beeldafstand groter dan 2f."},
            {"type": "mc", "vraag": "Wat gebeurt er met de lichtstralen als een lampje exact in het brandpunt van een positieve lens wordt geplaatst (v = f)?", "opties": ["De uittredende lichtstralen lopen evenwijdig aan de hoofdas verder", "De lichtstralen kruisen elkaar op 10 cm achter de lens", "De lichtstralen kaatsen terug in het lampje", "Er ontstaat een dubbel omgekeerd beeld"], "antwoord": 0, "uitleg": "Stralen die vanuit het brandpunt komen, verlaten de lens als een evenwijdige bundel (zoals bij een vuurtoren of schijnwerper)."},
            {"type": "mc", "vraag": "Als een voorwerp op voorwerpsafstand v = 25 cm staat en het scherpe beeld op beeldafstand b = 75 cm ontstaat, wat is dan de vergrotingsfactor N?", "opties": ["N = 0,33", "N = 3,0", "N = 50", "N = 100"], "antwoord": 1, "uitleg": "N = b / v = 75 cm / 25 cm = 3,0."},
            {"type": "mc", "vraag": "Hoe noem je de afstand van het optisch middelpunt van de lens tot het scherpe beeld op een scherm?", "opties": ["Brandpuntsafstand (f)", "Voorwerpsafstand (v)", "Beeldafstand (b)", "Lenzenkromming (R)"], "antwoord": 2, "uitleg": "De afstand van de lens tot het beeld heet de beeldafstand (symbool b)."},
            {"type": "mc", "vraag": "Wanneer je een positieve lens als loep (vergrootglas) gebruikt, wat voor beeld neem je dan waar met je oog?", "opties": ["Een reëel, omgekeerd en verkleind beeld", "Geen enkel beeld, alles is zwart", "Een reëel, rechtopstaand beeld op het glas", "Een virtueel, rechtopstaand en vergroot beeld"], "antwoord": 3, "uitleg": "Bij een loep staat het voorwerp binnen het brandpunt (v < f); er ontstaat een virtueel, vergroot en rechtopstaand beeld."},
            {"type": "mc", "vraag": "Wat geldt er voor de beeldgrootte Lb als de voorwerpsafstand exact gelijk is aan tweemaal de brandpuntsafstand (v = 2f)?", "opties": ["Lb is exact gelijk aan Lv (even groot beeld)", "Lb is vier keer zo klein als Lv", "Lb is oneindig groot", "Lb is altijd 0 cm"], "antwoord": 0, "uitleg": "Bij v = 2f ontstaat het beeld op b = 2f. N = b / v = 1, dus het beeld is exact even groot als het voorwerp."},
            {"type": "mc", "vraag": "Welke constructiestraal verandert bij een dunne lens NIET van richting en gaat rechtdoor?", "opties": ["De straal evenwijdig aan de hoofdas", "De straal door het optisch middelpunt O", "De straal door het brandpunt F", "De straal die de rand van de lens raakt"], "antwoord": 1, "uitleg": "Een lichtstraal die door het optisch middelpunt O van de lens gaat, loopt ongebroken rechtdoor."},
            {"type": "mc", "vraag": "Een voorwerp staat op v = 50 cm voor een lens en de vergroting is N = 0,2. Hoe groot is de beeldafstand b?", "opties": ["250 cm", "50 cm", "10 cm", "2 cm"], "antwoord": 2, "uitleg": "Omdat N = b / v geldt b = N · v = 0,2 · 50 cm = 10 cm."},
            {"type": "mc", "vraag": "Wat is het minimale aantal constructiestralen dat je moet tekenen om een beeldpunt eenduidig te construeren?", "opties": ["1 straal", "5 stralen", "10 stralen", "2 stralen"], "antwoord": 3, "uitleg": "Twee constructiestralen volstaan om het snijpunt (het beeldpunt) exact vast te leggen."},
            # 4 Waaronwaar (at least 2 false)
            {"type": "waaronwaar", "vraag": "Een reëel beeld kan op een projectiescherm of een camerasensor worden opgevangen.", "antwoord": True, "uitleg": "Waar: Reële beelden ontstaan waar echte lichtstralen elkaar fysiek snijden."},
            {"type": "waaronwaar", "vraag": "De vergrotingsfactor N wordt berekend met de formule N = v / b.", "antwoord": False, "uitleg": "Onwaar: De formule is N = b / v (of Lb / Lv). Het is beeldafstand gedeeld door voorwerpsafstand."},
            {"type": "waaronwaar", "vraag": "Als v < f (voorwerp dichterbij dan brandpunt), ontstaat achter de lens een reëel beeld dat op een scherm zichtbaar is.", "antwoord": False, "uitleg": "Onwaar: Als v < f wijken de stralen achter de lens uiteen; er ontstaat alleen een virtueel beeld vóór de lens."},
            {"type": "waaronwaar", "vraag": "De voorwerpsafstand v wordt altijd gemeten vanaf het voorwerp tot het midden van de lens.", "antwoord": True, "uitleg": "Waar: Dit is de standaarddefinitie van de voorwerpsafstand v."},
            # 2 Invul
            {"type": "invul", "vraag": "De verhouding tussen de beeldgrootte en de voorwerpsgrootte noem je de lineaire ...", "antwoord": "vergroting|vergrotingsfactor", "uitleg": "Deze verhouding (Lb / Lv of b / v) heet de vergroting (vergrotingsfactor N)."},
            {"type": "invul", "vraag": "De afstand tussen het voorwerp en het optisch middelpunt van de lens duidt men aan met de letter ...", "antwoord": "v", "uitleg": "De voorwerpsafstand heeft als standaardsymbool de kleine letter v."},
            # 2 Open
            {"type": "open", "vraag": "Noem de twee constructiestralen die het eenvoudigst te tekenen zijn om het beeld van een voorwerppunt te construeren bij een positieve lens.", "sleutelwoorden": ["evenwijdig/brandpunt", "optisch middelpunt/rechtdoor"], "minTreffers": 2, "modelantwoord": "1. De straal evenwijdig aan de hoofdas die na de lens door het brandpunt F gaat. 2. De straal door het optisch middelpunt die ongebroken rechtdoor gaat.", "uitleg": "Dit zijn de twee standaard constructiestralen om een beeldpunt te bepalen."},
            {"type": "open", "vraag": "Leg uit waarom de lens in een fotocamera naar voren geschoven moet worden als je een voorwerp van dichtbij wilt fotograferen.", "sleutelwoorden": ["voorwerpsafstand kleiner/dichterbij", "beeldafstand groter/verder"], "minTreffers": 2, "modelantwoord": "Als het voorwerp dichterbij komt (v wordt kleiner), wordt de beeldafstand b groter volgens de lenzenformule. De lens moet daarom verder van de beeldsensor af bewegen om het beeld scherp te houden.", "uitleg": "Kleine v betekent grotere b, dus de lens moet verder naar voren schuiven."}
        ]
    },
    {
        "id": "ex-h3-natuurkunde-43",
        "hoofdstuk": 5,
        "paragraaf": "5.4",
        "titel": "Toets 43 — §5.4 Oogafwijkingen en brillen",
        "vak": "Natuurkunde · HAVO 3 (H5)",
        "icoon": "👓",
        "duurMin": 30,
        "vragen": [
            # 12 MC (balanced: 3 A, 3 B, 3 C, 3 D)
            {"type": "mc", "vraag": "Op welk lichtgevoelig deel achter in het oog wordt door de ooglens een scherp beeld geprojecteerd?", "opties": ["Op het netvlies (retina)", "Op de iris", "Op het hoornvlies", "Op de pupil"], "antwoord": 0, "uitleg": "Het netvlies achter in het oog bevat de zintuigcellen die het licht opvangen."},
            {"type": "mc", "vraag": "Wat doet het oog wanneer je van een schoolbord in de verte kijkt naar een schrift vlak voor je neus?", "opties": ["De ooglens ontspant en wordt platter", "De ooglens accommodeert en wordt boller", "De oogbol krimpt direct met 10%", "De oogzenuw schakelt tijdelijk uit"], "antwoord": 1, "uitleg": "Om dichtbij scherp te stellen, spannen de kringspiertjes aan en wordt de ooglens boller (accommodatie)."},
            {"type": "mc", "vraag": "Wat is het belangrijkste probleem bij een persoon die <b>verziend</b> is?", "opties": ["De persoon kan voorwerpen in de verte niet zien", "De oogbol is veel te lang", "De persoon kan dichtbij niet scherpstellen zonder enorme spierinspanning", "De persoon ziet alles in zwart-wit"], "antwoord": 2, "uitleg": "Bij verziendheid is de oogbol te kort of de lens te zwak; dichtbij scherpstellen kost moeite of lukt niet."},
            {"type": "mc", "vraag": "Welk type brillenglas is nodig om <b>bijziendheid</b> (myopie) te corrigeren?", "opties": ["Een bolle lens met een plus-sterkte (+)", "Een spiegelend prisma", "Een cilindrisch glas zonder sterkte", "Een holle lens met een min-sterkte (-)"], "antwoord": 3, "uitleg": "Bijziendheid vereist een negatieve (holle) lens met min-sterkte om het te sterk brekende oog te compenseren."},
            {"type": "mc", "vraag": "Waar ligt het vertepunt van een normaal, gezond oog zonder afwijkingen?", "opties": ["Op oneindig (∞)", "Op 25 cm", "Op exact 1 meter", "Op 10 meter"], "antwoord": 0, "uitleg": "Een gezond oog kan in ontspannen toestand voorwerpen op oneindige afstand scherp zien."},
            {"type": "mc", "vraag": "Waar valt bij een <b>bijziend</b> oog het beeld van een voorwerp in de verte wanneer het oog volledig ontspannen is?", "opties": ["Exact op het netvlies", "Vóór het netvlies", "Achter het netvlies", "Bovenop het hoornvlies"], "antwoord": 1, "uitleg": "Omdat de oogbol te lang is (of de lens te bol), kruisen de lichtstralen al vóór het netvlies."},
            {"type": "mc", "vraag": "Waarom moet een vijftigjarige man een menukaart in een restaurant vaak op armlengte houden om de letters te kunnen lezen?", "opties": ["Omdat zijn oogbol plotseling te lang is geworden", "Omdat zijn pupillen te wijd openstaan", "Omdat door oudziendheid zijn nabijheidspunt verder weg is komen te liggen", "Omdat zijn oogzenuw trager werkt"], "antwoord": 2, "uitleg": "Bij oudziendheid wordt de lens stugger; het nabijheidspunt schuift naar achteren, waardoor dichtbij lezen moeilijk wordt."},
            {"type": "mc", "vraag": "Welk type hulplens zit er standaard in een eenvoudige leesbril?", "opties": ["Een holle lens (-)", "Een prisma", "Een zonnebrilglas zonder sterkte", "Een bolle lens (+)"], "antwoord": 3, "uitleg": "Een leesbril heeft positieve (bolle, +) lenzen om het tekortschietende accommodatievermogen aan te vullen."},
            {"type": "mc", "vraag": "Wat voor beeld vormt de ooglens op het netvlies van de mens?", "opties": ["Reëel, omgekeerd en verkleind", "Virtueel, rechtopstaand en vergroot", "Reëel, rechtopstaand en even groot", "Virtueel, omgekeerd en verkleind"], "antwoord": 0, "uitleg": "De bolle ooglens vormt een reëel, ondersteboven staand en verkleind beeld op het netvlies."},
            {"type": "mc", "vraag": "Wat gebeurt er met de vorm van de ooglens als de kringspiertjes van het straallichaam volledig ontspannen?", "opties": ["De lens wordt kogelrond", "De lens wordt platter", "De lens schuift naar links", "De lens klapt dubbel"], "antwoord": 1, "uitleg": "Bij ontspanning van de spieren trekken de lensbandjes de ooglens platter (aangepast voor veraf)."},
            {"type": "mc", "vraag": "Wat is bij benadering de afstand van het nabijheidspunt van een jong volwassene met gezonde ogen?", "opties": ["5 cm", "100 cm", "Ongeveer 25 cm", "Oneindig ver"], "antwoord": 2, "uitleg": "Het standaard nabijheidspunt voor een jongvolwassene ligt rond de 25 cm."},
            {"type": "mc", "vraag": "Waarom heeft een persoon die verziend is vaak last van hoofdpijn na langdurig studeren of lezen?", "opties": ["Door een tekort aan zonlicht", "Omdat het oog continu maximale spierkracht moet leveren om te accommoderen", "Doordat de oogbol te lang is", "Doordat de pupil te klein wordt"], "antwoord": 1, "uitleg": "Omdat een verziend oog zelfs voor veraf al moet accommoderen, raken de oogspiertjes bij intensief dichtbij lezen snel oververmoeid."},
            # 4 Waaronwaar (at least 2 false)
            {"type": "waaronwaar", "vraag": "Een bijziend oog heeft een oogbol die in verhouding tot de lenskromming te lang is.", "antwoord": True, "uitleg": "Waar: De te lange oogbol zorgt ervoor dat het beeld al vóór het netvlies scherp wordt."},
            {"type": "waaronwaar", "vraag": "Oudziendheid kan worden verholpen door een bril met negatieve holle glazen te dragen.", "antwoord": False, "uitleg": "Onwaar: Oudziendheid vereist juist een positieve bril (leesbril met bolle glazen, +) om dichtbij te helpen breken."},
            {"type": "waaronwaar", "vraag": "Wanneer je in de verte kijkt (vertepunt), is de ooglens maximaal geaccommodeerd.", "antwoord": False, "uitleg": "Onwaar: Kijken in de verte gebeurt met een volledig ontspannen, platte lens."},
            {"type": "waaronwaar", "vraag": "De hersenen zorgen ervoor dat het omgekeerde beeld op ons netvlies rechtop wordt waargenomen.", "antwoord": True, "uitleg": "Waar: Onze visuele schors in de hersenen verwerkt de omgekeerde prikkels en interpreteert ze rechtop."},
            # 2 Invul
            {"type": "invul", "vraag": "Het boller worden van de ooglens om voorwerpen dichtbij scherp waar te nemen heet ...", "antwoord": "accommoderen|accommodatie", "uitleg": "Dit proces noemt men accommoderen."},
            {"type": "invul", "vraag": "Iemand die veraf scherp ziet maar dichtbij onscherp (door een te korte oogbol), noemen we ...", "antwoord": "verziend|verziendheid|hypermetroop", "uitleg": "Deze persoon is verziend (hypermetropie)."},
            # 2 Open
            {"type": "open", "vraag": "Leg uit waarom een bril met negatieve (holle) glazen helpt bij iemand die bijziend is.", "sleutelwoorden": ["lichtstralen spreiden/divergeren", "netvlies samenkomen/beeld naar achteren"], "minTreffers": 2, "modelantwoord": "Het bijziende oog breekt te sterk en vormt het beeld vóór het netvlies. De negatieve lens spreidt (divergeert) de lichtstralen vooraf een beetje, waardoor het brandpunt verder naar achteren schuift en precies op het netvlies terechtkomt.", "uitleg": "De negatieve lens divergeert het licht zodat het brandpunt precies op het netvlies valt."},
            {"type": "open", "vraag": "Noem het verschil tussen verziendheid en oudziendheid wat betreft de anatomische oorzaak.", "sleutelwoorden": ["oogbol te kort/vorm van het oog", "lens minder elastisch/stugger"], "minTreffers": 2, "modelantwoord": "Bij verziendheid is de oogbol anatomisch te kort (aangeboren afwijking van de vorm), terwijl bij oudziendheid de ooglens door veroudering zijn elasticiteit verliest en niet meer bol kan worden.", "uitleg": "Verziendheid = te korte oogbol; oudziendheid = verlies van lenselasticiteit door ouderdom."}
        ]
    },
    {
        "id": "ex-h3-natuurkunde-44",
        "hoofdstuk": 5,
        "paragraaf": "5.5",
        "titel": "Toets 44 — §5.5 Rekenen aan lenzen en lenssterkte",
        "vak": "Natuurkunde · HAVO 3 (H5)",
        "icoon": "📐",
        "duurMin": 30,
        "vragen": [
            # 12 MC (balanced: 3 A, 3 B, 3 C, 3 D)
            {"type": "mc", "vraag": "In welke eenheid MOET de brandpuntsafstand f worden omgerekend om de lenssterkte S in dioptrie te berekenen?", "opties": ["In meter (m)", "In centimeter (cm)", "In millimeter (mm)", "In kilometer (km)"], "antwoord": 0, "uitleg": "Dioptrie is gedefinieerd als 1/meter (m⁻¹). De brandpuntsafstand f moet dus altijd strikt in meters worden ingevuld."},
            {"type": "mc", "vraag": "Wat is de lenssterkte S van een positieve lens met een brandpuntsafstand van f = 25 cm?", "opties": ["+0,25 dpt", "+4,0 dpt", "+25 dpt", "+0,04 dpt"], "antwoord": 1, "uitleg": "f = 25 cm = 0,25 m. S = 1 / f = 1 / 0,25 = +4,0 dpt."},
            {"type": "mc", "vraag": "Een brillenglas heeft een sterkte van S = -2,5 dioptrie. Wat is de brandpuntsafstand van dit glas?", "opties": ["f = +2,5 m", "f = -25 cm", "f = -40 cm (-0,40 m)", "f = -4,0 m"], "antwoord": 2, "uitleg": "f = 1 / S = 1 / (-2,5) = -0,40 m = -40 cm."},
            {"type": "mc", "vraag": "Een voorwerp staat op v = 20 cm van een lens met f = 5 cm. Wat is de beeldafstand b waar het scherpe beeld ontstaat?", "opties": ["b = 15 cm", "b = 25 cm", "b = 10 cm", "b = 6,67 cm (20/3 cm)"], "antwoord": 3, "uitleg": "1/b = 1/f - 1/v = 1/5 - 1/20 = 4/20 - 1/20 = 3/20. Dus b = 20/3 ≈ 6,67 cm."},
            {"type": "mc", "vraag": "Een dia staat op v = 6,0 cm voor een projectorlens. Het beeld verschijnt scherp op een scherm op beeldafstand b = 180 cm. Wat is de vergrotingsfactor N?", "opties": ["N = 30", "N = 0,033", "N = 1080", "N = 174"], "antwoord": 0, "uitleg": "N = b / v = 180 cm / 6,0 cm = 30."},
            {"type": "mc", "vraag": "Hoe luidt de klassieke lenzenformule?", "opties": ["f = v + b", "1/f = 1/v + 1/b", "f = v · b", "N = f / (v + b)"], "antwoord": 1, "uitleg": "De lenzenformule luidt 1/f = 1/v + 1/b."},
            {"type": "mc", "vraag": "Een voorwerp staat op v = 12 cm en het beeld ontstaat op b = 24 cm. Wat is de brandpuntsafstand f van de lens?", "opties": ["f = 36 cm", "f = 2,0 cm", "f = 8,0 cm", "f = 12 cm"], "antwoord": 2, "uitleg": "1/f = 1/v + 1/b = 1/12 + 1/24 = 2/24 + 1/24 = 3/24 = 1/8. Dus f = 8,0 cm."},
            {"type": "mc", "vraag": "Een camera heeft een beeldsensor van 2,0 cm hoog. Een boom van 10,0 meter hoog (1000 cm) wordt beeldvullend gefotografeerd. Wat is de vergroting N van de camera?", "opties": ["N = 500", "N = 20", "N = 0,02", "N = 0,002"], "antwoord": 3, "uitleg": "N = Lb / Lv = 2,0 cm / 1000 cm = 0,002 (sterk verkleind reëel beeld)."},
            {"type": "mc", "vraag": "Wat gebeurt er met de sterkte S van een bolle lens als je de brandpuntsafstand halveert?", "opties": ["De sterkte verdubbelt", "De sterkte halveert", "De sterkte blijft gelijk", "De sterkte wordt vier keer zo klein"], "antwoord": 0, "uitleg": "Omdat S = 1/f omgekeerd evenredig is met f, leidt halvering van f tot een verdubbeling van de sterkte S."},
            {"type": "mc", "vraag": "Een voorwerp van 3,0 cm hoog staat voor een lens. De vergroting is N = 4. Hoe hoog is het geprojecteerde beeld?", "opties": ["0,75 cm", "12,0 cm", "7,0 cm", "1,33 cm"], "antwoord": 1, "uitleg": "Lb = N · Lv = 4 · 3,0 cm = 12,0 cm."},
            {"type": "mc", "vraag": "Een lens heeft f = 10 cm en het voorwerp staat op v = 15 cm. Wat is de beeldafstand b?", "opties": ["b = 5 cm", "b = 25 cm", "b = 30 cm", "b = 150 cm"], "antwoord": 2, "uitleg": "1/b = 1/f - 1/v = 1/10 - 1/15 = 3/30 - 2/30 = 1/30. Dus b = 30 cm."},
            {"type": "mc", "vraag": "Wat voor lens heeft een sterkte van S = +1,5 dpt?", "opties": ["Een holle lens met f = -1,5 m", "Een spiegel", "Een cilindrisch glas", "Een bolle lens met f ≈ 0,67 m (67 cm)"], "antwoord": 3, "uitleg": "Een positief getal duidt op een bolle lens. f = 1 / 1,5 ≈ 0,67 m = 67 cm."},
            # 4 Waaronwaar (at least 2 false)
            {"type": "waaronwaar", "vraag": "Een lens met een brandpuntsafstand van 10 cm heeft een sterkte van +10 dioptrie.", "antwoord": True, "uitleg": "Waar: f = 10 cm = 0,10 m. S = 1 / 0,10 = +10 dpt."},
            {"type": "waaronwaar", "vraag": "In de lenzenformule mag je voor f centimeters gebruiken terwijl je voor v meters gebruikt zonder omrekenen.", "antwoord": False, "uitleg": "Onwaar: Alle drie de grootheden f, v en b moeten absoluut in dezelfde eenheid staan."},
            {"type": "waaronwaar", "vraag": "Als een beeld tweemaal zo groot is als het voorwerp (N = 2), staat het beeld tweemaal zo ver van de lens als het voorwerp (b = 2v).", "antwoord": True, "uitleg": "Waar: Omdat N = b / v geldt b = N · v = 2 · v."},
            {"type": "waaronwaar", "vraag": "Een negatieve lens met brandpuntsafstand f = -50 cm heeft een positieve dioptriesterkte.", "antwoord": False, "uitleg": "Onwaar: Een negatieve brandpuntsafstand levert een negatieve lenssterkte op: S = 1 / (-0,5) = -2 dpt."},
            # 2 Invul
            {"type": "invul", "vraag": "De eenheid van lenssterkte (afgekort dpt) heet de ...", "antwoord": "dioptrie", "uitleg": "De eenheid van lenssterkte is de dioptrie (dpt)."},
            {"type": "invul", "vraag": "Als f = 0,5 m, hoeveel dioptrie bedraagt dan de sterkte S van deze lens?", "antwoord": "+2|2|+2 dpt|2 dpt", "uitleg": "S = 1 / f = 1 / 0,5 = +2 dpt."},
            # 2 Open
            {"type": "open", "vraag": "Geef de lenzenformule en leg uit waar de letters f, v en b voor staan.", "sleutelwoorden": ["1/f = 1/v + 1/b", "brandpuntsafstand/voorwerpsafstand/beeldafstand"], "minTreffers": 2, "modelantwoord": "De formule is 1/f = 1/v + 1/b. Hierin is f de brandpuntsafstand, v de voorwerpsafstand en b de beeldafstand.", "uitleg": "De formule verbindt de brandpuntsafstand (f), voorwerpsafstand (v) en beeldafstand (b)."},
            {"type": "open", "vraag": "Bereken in stappen de beeldafstand b als gegeven is dat f = 20 cm en v = 30 cm.", "sleutelwoorden": ["1/20 - 1/30/1/60", "60/60 cm"], "minTreffers": 2, "modelantwoord": "1/b = 1/f - 1/v = 1/20 - 1/30 = 3/60 - 2/60 = 1/60. Hieruit volgt b = 60 cm.", "uitleg": "1/b = 1/20 - 1/30 = 1/60, dus b = 60 cm."}
        ]
    }
]

def generate():
    # 1. Write onderwerpen
    for o in ONDERWERPEN:
        p_num = o["paragraaf"].split(".")[1]
        filename = f"h5_{p_num}.js"
        filepath = os.path.join(DATA_DIR, filename)
        content = f"/* =========================================================\n"
        content += f"   Duru's Natuurkunde (HAVO 3) — §{o['paragraaf']} {o['titel']}\n"
        content += f"   ========================================================= */\n"
        content += f"DURU.register({json.dumps(o, ensure_ascii=False, indent=2)});\n"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated {filepath}")

    # 2. Write examens
    for ex in EXAMENS:
        ex_num = ex["id"].split("-")[-1]
        filename = f"examen_{ex_num}.js"
        filepath = os.path.join(DATA_DIR, filename)
        content = f"/* =========================================================\n"
        content += f"   Duru's Natuurkunde (HAVO 3) — {ex['titel']}\n"
        content += f"   ========================================================= */\n"
        content += f"DURU.registerExamen({json.dumps(ex, ensure_ascii=False, indent=2)});\n"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated {filepath}")

if __name__ == "__main__":
    generate()

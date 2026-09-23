/* =========================================================
   Duru's Aardrijkskunde (HAVO 3) — §4.2 Op weg naar duurzame energiebronnen
   buiteNLand 3 HAVO Hoofdstuk 4 (Energietransitie)
   ========================================================= */
DURU.register({
  id: "ak-h4-2",
  hoofdstuk: 4,
  paragraaf: "4.2",
  titel: "Op weg naar duurzame energiebronnen",
  korteUitleg: "Traditionele versus niet-conventionele energiebronnen, kernenergie en de noodzaak tot transitie.",
  icoon: "🛢️",
  kleur: "h4-thema",
  theorie: `<h3>4.2 Op weg naar duurzame energiebronnen</h3>
<div class="info-box">
  <b>Kernbegrippen:</b> Fossiele brandstoffen, uitputbare energiebronnen, conventionele olie en gas, niet-conventionele olie en gas, teerzand, kernenergie, uranium, radioactiviteit, CO2-voetafdruk/inw.
</div>

<h4>1. Traditionele en fossiele energiebronnen</h4>
<p>Sinds de industriële revolutie draait de wereldeconomie op fossiele brandstoffen: steenkool, aardolie en aardgas. Dit zijn <b>uitputbare energiebronnen</b>: ze zijn miljoenen jaren geleden gevormd uit samengeperste resten van planten en plankton en raken op een dag op. Bij de opwekking en het transport gaat gemiddeld tot wel twee derde van de energie verloren in de vorm van restwarmte.</p>

<h4>2. Conventionele versus niet-conventionele winning</h4>
<ul>
  <li><b>Conventionele olie en gas:</b> Olie en gas die na hun ontstaan zijn gemigreerd naar een poreus reservoirgesteente onder een ondoordringbare afsluitlaag. Deze voorraden kunnen relatief eenvoudig en goedkoop met verticale boringen worden opgepompt.</li>
  <li><b>Niet-conventionele olie en gas:</b> Olie en gas die vastzitten in het oorspronkelijke moedergesteente (zoals schaliegas en schalie-olie) of voorkomen als kleverige bitumen vermengd met zand en klei. Een bekend voorbeeld zijn de <b>teerzanden</b> in de Canadese provincie Alberta.</li>
</ul>
<p>De winning van teerzand is extreem kostbaar en belastend voor het milieu. Voor één vat ruwe olie moet zo n twee ton teerzand worden afgegraven. Het proces verbruikt reusachtige hoeveelheden heet water en energie en laat giftige bekkens met chemicaliën en zware metalen achter.</p>

<h4>3. Voor- en nadelen van kernenergie</h4>
<p>Kernenergie wordt opgewekt door het splijten van <b>uranium</b> in kerncentrales. Het is een zeer krachtige energiebron: één kilogram uranium kan net zoveel energie leveren als tientallen tonnen steenkool.</p>
<ul>
  <li><b>Voordelen:</b> Bij de stroomproductie in een kerncentrale komt geen CO2 vrij. Een kerncentrale levert continu en betrouwbaar grote hoeveelheden elektriciteit, ongeacht wind of zon.</li>
  <li><b>Nadelen:</b> Er ontstaat hoogradioactief afval dat duizenden jaren veilig ondergronds moet worden opgeslagen. Daarnaast bestaat er altijd een risico op ernstige kernongevallen (zoals Tsjernobyl in 1986 en Fukushima in 2011 door een tsunami), waarbij grote gebieden decennialang onbewoonbaar raken door dodelijke straling.</li>
</ul>

<h4>4. De noodzaak van de energietransitie</h4>
<p>De <b>energietransitie</b> is de structurele overstap van fossiele en uitputbare brandstoffen naar duurzame, hernieuwbare energiebronnen die geen broeikasgassen uitstoten en nooit opraken. Deze overstap is noodzakelijk om catastrofale klimaatverandering te voorkomen en om niet langer afhankelijk te zijn van instabiele exportlanden van olie en gas.</p>`,
  vragen: [
    {
        "type": "mc",
        "vraag": "Wat is het belangrijkste kenmerk van conventionele olie en gas?",
        "opties": [
            "Het is makkelijk te winnen doordat het zich verzameld heeft in een poreus reservoirgesteente",
            "Het kan uitsluitend worden gewonnen door open mijnbouw in zandgroeven",
            "Het stoot bij verbranding helemaal geen koolstofdioxide uit",
            "Het ontstaat binnen enkele weken uit huishoudelijk afval"
        ],
        "antwoord": 0,
        "uitleg": "Conventioneel gas en olie bevinden zich in reservoirgesteenten en kunnen relatief gemakkelijk omhoog gepompt worden."
    },
    {
        "type": "mc",
        "vraag": "In welk land liggen enorme voorraden teerzand waarvan de winning grote landschappelijke schade veroorzaakt?",
        "opties": [
            "Saoedi-Arabië",
            "Canada",
            "Noorwegen",
            "Japan"
        ],
        "antwoord": 1,
        "uitleg": "In Canada (vooral Alberta) wordt olie op grote schaal gewonnen uit uitgestrekte teerzandvelden."
    },
    {
        "type": "mc",
        "vraag": "Welke grondstof wordt in kerncentrales gebruikt als splijtstof om elektriciteit op te wekken?",
        "opties": [
            "Bauxiet",
            "Steenkool",
            "Uranium",
            "Lithium"
        ],
        "antwoord": 2,
        "uitleg": "Kerncentrales gebruiken uranium als splijtstof voor de nucleaire kettingreactie."
    },
    {
        "type": "mc",
        "vraag": "Wat is een groot milieutechnisch voordeel van kernenergie vergeleken met kolencentrales?",
        "opties": [
            "Er blijft na gebruik geen enkel schadelijk afval over",
            "Kerncentrales zijn gratis en eenvoudig te bouwen",
            "De brandstof uranium is onuitputtelijk en groeit overal aan bomen",
            "Er ontstaat tijdens de stroomopwekking geen directe uitstoot van CO2"
        ],
        "antwoord": 3,
        "uitleg": "Bij kernsplijting komt geen CO2 vrij, wat helpt in de strijd tegen het broeikaseffect."
    },
    {
        "type": "mc",
        "vraag": "Wat is een groot nadeel van het delven van olie uit teerzanden?",
        "opties": [
            "Het vereist enorm veel energie en heet water en laat giftig afval achter",
            "Er kan helemaal geen bruikbare brandstof uit gewonnen worden",
            "Het kan alleen midden op volle zee worden uitgevoerd",
            "Het veroorzaakt overmatige afkoeling van de atmosfeer"
        ],
        "antwoord": 0,
        "uitleg": "Teerzandwinning vergt reusachtige hoeveelheden water en energie en veroorzaakt ernstige milieuvervuiling."
    },
    {
        "type": "mc",
        "vraag": "Wat verstaan we onder het begrip energietransitie?",
        "opties": [
            "Het sluiten van alle fabrieken en transportbedrijven in een land",
            "De overstap van fossiele brandstoffen naar hernieuwbare en schone energiebronnen",
            "Het vervangen van benzineauto s door uitsluitend dieseltreinen",
            "Het verhogen van de gasprijzen om de staatskas aan te vullen"
        ],
        "antwoord": 1,
        "uitleg": "Energietransitie betekent de omschakeling van fossiele brandstoffen naar duurzame energiebronnen."
    },
    {
        "type": "waaronwaar",
        "vraag": "Aardolie, aardgas en steenkool noemen we uitputbare energiebronnen omdat ze sneller worden verbruikt dan de natuur ze kan aanmaken.",
        "antwoord": true,
        "uitleg": "Waar: de vorming van fossiele brandstoffen duurt miljoenen jaren, waardoor de voorraad eindig is."
    },
    {
        "type": "waaronwaar",
        "vraag": "Kernafval verliest binnen enkele dagen al zijn radioactiviteit en kan als gewone compost worden hergebruikt.",
        "antwoord": false,
        "uitleg": "Onwaar: hoogradioactief afval blijft tienduizenden jaren gevaarlijk stralend en moet zorgvuldig worden opgeborgen."
    },
    {
        "type": "waaronwaar",
        "vraag": "Bij het kernongeval in Fukushima in 2011 speelde een zware tsunami een cruciale rol bij het uitvallen van de koelsystemen.",
        "antwoord": true,
        "uitleg": "Waar: de vloedgolf overspoelde de noodgeneratoren waardoor de koeling uitviel en een meltdown ontstond."
    },
    {
        "type": "invoer",
        "vraag": "Welk zwaar metaal dient als voornaamste splijtstof in kernreactoren?",
        "antwoord": "uranium",
        "uitleg": "Uranium is het radioactieve element waarvan de atoomkernen worden gespleten om warmte en stroom op te wekken."
    }
]
});

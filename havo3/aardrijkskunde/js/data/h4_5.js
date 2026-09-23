/* =========================================================
   Duru's Aardrijkskunde (HAVO 3) — §4.5 Naar minder CO2-uitstoot in Nederland
   buiteNLand 3 HAVO Hoofdstuk 4 (Energietransitie)
   ========================================================= */
DURU.register({
  id: "ak-h4-5",
  hoofdstuk: 4,
  paragraaf: "4.5",
  titel: "Naar minder CO2-uitstoot in Nederland",
  korteUitleg: "Nederlands klimaatbeleid, energiedragers zoals waterstof en ruimtelijke conflicten.",
  icoon: "🇳🇱",
  kleur: "h4-thema",
  theorie: `<h3>4.5 Naar minder CO2-uitstoot in Nederland</h3>
<div class="info-box">
  <b>Kernbegrippen:</b> Nederlandse Klimaatwet, CO2-uitstoot per inwoner, ruimtelijk conflict, energiedrager, waterstof, energieopslag, netcongestie.
</div>

<h4>1. Nederland en de CO2-uitstoot</h4>
<p>Nederland heeft binnen Europa traditioneel een relatief hoge <b>CO2-uitstoot per inwoner</b>. Dit komt door verschillende structurele factoren:</p>
<ul>
  <li>Een omvangrijke chemische en zware industrie (onder andere in de haven van Rotterdam).</li>
  <li>Een zeer intensieve glastuinbouwsector die decennialang veel aardgas heeft gestookt om kassen te verwarmen en te verlichten.</li>
  <li>Een van de dichtstbevolkte en meest intensieve veehouderijsectoren ter wereld.</li>
  <li>Een groot aantal vrachtbewegingen en een druk snelwegennetwerk als logistiek knooppunt van Noordwest-Europa.</li>
</ul>
<p>Om aan de internationale verplichtingen van het Akkoord van Parijs te voldoen, heeft Nederland de <b>Klimaatwet</b> aangenomen. Deze wet verplicht de overheid om de uitstoot van broeikasgassen in 2030 met minimaal 55% te verminderen ten opzichte van 1990, en in 2050 met 95% tot 100%.</p>

<h4>2. Ruimtebeslag en ruimtelijke conflicten</h4>
<p>De overgang naar duurzame energiebronnen vraagt enorm veel landoppervlakte. Terwijl een traditionele gas- of kolencentrale weinig grond inneemt, vereisen zonneparken en windmolenparken vele hectaren ruimte. Nederland is echter een heel dichtbevolkt land met grote schaarste aan open ruimte. Hierdoor ontstaan <b>ruimtelijke conflicten</b>:</p>
<ul>
  <li><b>Windmolens op land:</b> Omwonenden protesteren vaak tegen windturbines vanwege horizonvervuiling, slagschaduw en geluidsoverlast (het zogeheten NIMBY-effect: <i>Not In My Back Yard</i>).</li>
  <li><b>Zonneparken op landbouwgrond:</b> Boeren en natuurorganisaties vinden dat vruchtbare landbouwgrond behouden moet blijven voor voedselproductie of natuurherstel in plaats van vol gelegd met zonnepanelen.</li>
  <li><b>Netcongestie:</b> Het Nederlandse elektriciteitsnet zit in veel regio s overvol doordat er massaal zonnepanelen, laadpalen en warmtepompen bijkomen. Bedrijven kunnen hierdoor geen nieuwe stroomaansluiting krijgen.</li>
</ul>

<h4>3. Energiedragers en energieopslag</h4>
<p>Omdat zon en wind niet op afroep beschikbaar zijn, is energieopslag noodzakelijk. Elektriciteit kan worden opgeslagen in batterijen, maar voor grootschalige seizoensopslag is <b>waterstof</b> veelbelovend.</p>
<p>Belangrijk verschil: waterstof is <i>geen primaire energiebron</i>, maar een <b>energiedrager</b>. Je moet het eerst maken door water te splitsen met behulp van elektriciteit (elektrolyse). Gebeurt dit met groene stroom van windparken of zonnepanelen, dan spreken we van <i>groene waterstof</i>. Nederland heeft het voordeel van een fijnmazig bestaand aardgasnetwerk, dat in de toekomst deels geschikt gemaakt kan worden voor het transport van waterstof.</p>`,
  vragen: [
    {
        "type": "mc",
        "vraag": "Waarom heeft Nederland in Europees verband van oudsher een relatief hoge CO2-uitstoot per inwoner?",
        "opties": [
            "Door een sterke chemische industrie, intensieve glastuinbouw en veel transport",
            "Omdat alle woningen in Nederland uitsluitend op bruinkool gestookt worden",
            "Omdat er in Nederland geen enkele boom of bos groeit",
            "Doordat Nederlanders gemiddeld twintig keer per jaar vliegen"
        ],
        "antwoord": 0,
        "uitleg": "Zware havenindustrie, kassencomplexen en intensieve veehouderij zorgen voor een hoge CO2-uitstoot per capita."
    },
    {
        "type": "mc",
        "vraag": "Wat is het belangrijkste verschil tussen een energiebron en een energiedrager zoals waterstof?",
        "opties": [
            "Een energiebron ontstaat altijd in kerncentrales; een energiedrager drijft op water",
            "Een energiedrager komt niet kant-en-klaar in de natuur voor, maar moet eerst met energie geproduceerd worden",
            "Een energiedrager kan nooit elektriciteit leveren",
            "Een energiebron is altijd vloeibaar terwijl een energiedrager altijd een gas is"
        ],
        "antwoord": 1,
        "uitleg": "Een energiedrager (zoals waterstof of een batterij) slaat energie op, maar moet eerst met behulp van een andere bron worden opgewekt."
    },
    {
        "type": "mc",
        "vraag": "Hoe noemen we meningsverschillen en tegenstellingen tussen burgers, boeren en overheden over de bestemming van schaarse grond?",
        "opties": [
            "Een demografische transitie",
            "Een continentale drift",
            "Een ruimtelijk conflict",
            "Een culturele diffusie"
        ],
        "antwoord": 2,
        "uitleg": "Een ruimtelijk conflict ontstaat wanneer verschillende partijen tegengestelde belangen hebben bij de inrichting van een gebied."
    },
    {
        "type": "mc",
        "vraag": "Wat houdt het probleem van netcongestie in Nederland in?",
        "opties": [
            "Het internet valt dagelijks uit in het hele land",
            "De rivieren zijn overvol met vrachtschepen waardoor bruggen niet meer open kunnen",
            "Er is te veel aardgas in de leidingen waardoor de druk wegvalt",
            "Het elektriciteitsnetwerk zit vol waardoor nieuwe windparken, zonnevelden of bedrijven niet aangesloten kunnen worden"
        ],
        "antwoord": 3,
        "uitleg": "Netcongestie betekent file op het stroomnet doordat de capaciteit van kabels en transformatorstations ontoereikend is."
    },
    {
        "type": "mc",
        "vraag": "Wanneer spreken we van zogeheten groene waterstof?",
        "opties": [
            "Als waterstof wordt geproduceerd via elektrolyse met duurzame stroom uit zon of wind",
            "Als de waterstof is gekleurd met een milieuvriendelijke kleurstof",
            "Als de waterstof rechtstreeks uit steenkoolmijnen wordt gepompt",
            "Als waterstof alleen in natuurgebieden wordt gebruikt"
        ],
        "antwoord": 0,
        "uitleg": "Groene waterstof wordt gemaakt door water te splitsen met hernieuwbare zonne- of windenergie zonder CO2-uitstoot."
    },
    {
        "type": "mc",
        "vraag": "Wat is het wettelijke doel van de Nederlandse Klimaatwet voor de vermindering van broeikasgassen in 2030 ten opzichte van 1990?",
        "opties": [
            "Precies 10% toename van de uitstoot",
            "Minimaal 55% reductie van de uitstoot",
            "Alle uitstoot in 2030 direct naar 0%",
            "Er zijn in de wet geen jaartallen of percentages vastgelegd"
        ],
        "antwoord": 1,
        "uitleg": "De Nederlandse Klimaatwet mikt op minimaal 55% CO2-reductie in 2030 ten opzichte van het ijkjaar 1990."
    },
    {
        "type": "waaronwaar",
        "vraag": "Zonne- en windparken nemen per geproduceerde kilowattuur aanzienlijk meer landoppervlakte in beslag dan een traditionele gascentrale.",
        "antwoord": true,
        "uitleg": "Waar: hernieuwbare energiebronnen hebben een lagere energiedichtheid en vergen daarom veel meer ruimte."
    },
    {
        "type": "waaronwaar",
        "vraag": "Waterstof kan spontaan in grote ondergrondse gasvelden worden opgeboord zonder dat er eerst energie voor hoeft te worden opgewekt.",
        "antwoord": false,
        "uitleg": "Onwaar: zuiver waterstofgas komt vrijwel niet los in de natuur voor en moet altijd eerst kunstmatig worden gefabriceerd."
    },
    {
        "type": "waaronwaar",
        "vraag": "Het bestaande Nederlandse leidingnetwerk voor aardgas kan in de toekomst deels worden hergebruikt voor het transport van waterstof.",
        "antwoord": true,
        "uitleg": "Waar: de gasinfrastructuur kan na technische aanpassingen dienstdoen voor waterstoftransport."
    },
    {
        "type": "invoer",
        "vraag": "Welke energiedrager kan worden gemaakt door water met groene elektriciteit te splitsen via elektrolyse?",
        "antwoord": "waterstof",
        "uitleg": "Waterstof (H2) kan als schone energiedrager dienen voor zware industrie, transport en energieopslag."
    }
]
});

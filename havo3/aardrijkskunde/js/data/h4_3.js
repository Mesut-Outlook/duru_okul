/* =========================================================
   Duru's Aardrijkskunde (HAVO 3) — §4.3 Het tegengaan van klimaatverandering
   buiteNLand 3 HAVO Hoofdstuk 4 (Energietransitie)
   ========================================================= */
DURU.register({
  id: "ak-h4-3",
  hoofdstuk: 4,
  paragraaf: "4.3",
  titel: "Het tegengaan van klimaatverandering",
  korteUitleg: "Duurzame energiebronnen, internationale klimaatakkoorden en klimaatrechtvaardigheid.",
  icoon: "☀️",
  kleur: "h4-thema",
  theorie: `<h3>4.3 Het tegengaan van klimaatverandering</h3>
<div class="info-box">
  <b>Kernbegrippen:</b> Duurzame/hernieuwbare energie, zonne-energie, windenergie, waterkracht, geothermische energie (aardwarmte), biomassa, klimaatakkoord van Parijs, klimaatschadefonds.
</div>

<h4>1. Duurzame en hernieuwbare energiebronnen</h4>
<p>Om de uitstoot van broeikasgassen drastisch te verminderen, moeten we overschakelen op <b>duurzame of hernieuwbare energiebronnen</b>. Deze bronnen raken nooit op en veroorzaken bij de opwekking geen CO2-uitstoot. De belangrijkste vormen zijn:</p>
<ul>
  <li><b>Zonne-energie:</b> Het omzetten van zonlicht in elektriciteit via zonnepanelen (fotovoltaïsche cellen) of in warmte via zonnecollectoren. De zon straalt iedere dag duizenden malen meer energie naar de aarde dan de mensheid verbruikt.</li>
  <li><b>Windenergie:</b> Windturbines op land (onshore) of op zee (offshore) zetten de bewegingsenergie van luchtstromen om in elektriciteit. Wind op zee waait krachtiger en constanter, maar de installatie en het onderhoud zijn duurder.</li>
  <li><b>Waterkracht:</b> Elektriciteit opwekken met behulp van stromend of vallend water via stuwdammen in rivieren of getijdencentrales aan de kust.</li>
  <li><b>Geothermische energie (aardwarmte):</b> Het benutten van de natuurlijke hitte die diep in de aardkorst aanwezig is om gebouwen te verwarmen of stoomturbines aan te drijven (veel toegepast in vulkanische gebieden zoals IJsland).</li>
  <li><b>Biomassa:</b> Energie halen uit organisch materiaal zoals snoeihout, gft-afval, mest of plantaardige oliën. Let op: bij verbranding van biomassa komt wel CO2 vrij, maar die is recentelijk door planten opgenomen (kortcyclische koolstofkringloop).</li>
</ul>

<h4>2. Nadelen en uitdagingen van duurzame energie</h4>
<p>Hoewel duurzame bronnen onmisbaar zijn, kennen ze ook uitdagingen:</p>
<ul>
  <li><b>Ruimtebeslag:</b> Windparken en zonnevelden nemen per opgewekte megawatt veel meer landoppervlakte in beslag dan een compacte kolen- of kerncentrale.</li>
  <li><b>Intermittentie (weersafhankelijkheid):</b> De zon schijnt niet s nachts en de wind waait niet altijd even hard. Daarom is grootschalige energieopslag (zoals batterijen en waterstof) cruciaal.</li>
  <li><b>Grondstoffen:</b> Voor zonnepanelen, windturbines en accu s zijn grote hoeveelheden zeldzame metalen en mineralen nodig (zoals koper, lithium, kobalt en neodymium).</li>
</ul>

<h4>3. Internationale afspraken en klimaatrechtvaardigheid</h4>
<p>Klimaatverandering houdt niet op bij landsgrenzen. Tijdens de klimaattop in Parijs (2015) spraken bijna 200 landen af om de opwarming van de aarde te beperken tot ruim onder de 2 graden Celsius, en bij voorkeur tot maximaal 1,5 graad Celsius ten opzichte van het pre-industriële tijdperk.</p>
<p><b>Klimaatrechtvaardigheid:</b> Historisch gezien hebben rijke westerse landen de meeste fossiele brandstoffen verstookt en dus de grootste schuld aan het probleem. Veel arme ontwikkelingslanden (zoals eilandstaten in de Stille Oceaan of landen in de Sahel) stoten zelf vrijwel niets uit, maar worden wel het hardst getroffen door zeespiegelstijging en extreme droogte. Daarom is internationaal afgesproken dat rijke landen arme landen financieel moeten compenseren en ondersteunen via een <b>klimaatschadefonds</b>.</p>`,
  vragen: [
    {
        "type": "mc",
        "vraag": "Hoe noemen we energie die wordt opgewekt door gebruik te maken van de hitte diep in de aarde?",
        "opties": [
            "Geothermische energie (aardwarmte)",
            "Biomassa-energie",
            "Kernfusie-energie",
            "Getijdenenergie"
        ],
        "antwoord": 0,
        "uitleg": "Aardwarmte of geothermische energie maakt gebruik van heet water of stoom uit diepe aardlagen."
    },
    {
        "type": "mc",
        "vraag": "Wat is het belangrijkste doel van het historische Klimaatakkoord van Parijs (2015)?",
        "opties": [
            "Het wereldwijde gebruik van steenkool verdubbelen vóór 2030",
            "De opwarming van de aarde beperken tot ruim onder de 2 °C, bij voorkeur 1,5 °C",
            "Alle kerncentrales in de wereld onmiddellijk ontmantelen",
            "Het verplichten van alle burgers om uitsluitend per trein te reizen"
        ],
        "antwoord": 1,
        "uitleg": "Het Akkoord van Parijs streeft ernaar de opwarming te beperken tot maximaal 1,5 tot 2 graden Celsius."
    },
    {
        "type": "mc",
        "vraag": "Waarom waait de wind op zee (offshore windparken) vaak constanter en harder dan op land?",
        "opties": [
            "Omdat de zwaartekracht op zee minder krachtig is",
            "Omdat de wolken boven zee altijd kouder zijn dan boven land",
            "Omdat er op open zee geen obstakels zoals heuvels, bomen en gebouwen zijn die wrijving veroorzaken",
            "Omdat schepen de luchtstroom kunstmatig aandrijven"
        ],
        "antwoord": 2,
        "uitleg": "Door het vlakke wateroppervlak is de ruwheid laag en ondervindt de wind nauwelijks wrijvingsweerstand."
    },
    {
        "type": "mc",
        "vraag": "Wat verstaat men in het internationale klimaatbeleid onder klimaatrechtvaardigheid?",
        "opties": [
            "Dat arme landen alle kosten van de energietransitie moeten betalen",
            "Dat elk land precies evenveel windmolens moet plaatsen",
            "Dat alle rechtszaken over het weer verboden worden",
            "Dat rijke landen die historisch de meeste CO2 uitstootten arme kwetsbare landen financieel steunen"
        ],
        "antwoord": 3,
        "uitleg": "Klimaatrechtvaardigheid betekent dat de historische vervuilers verantwoordelijkheid nemen voor kwetsbare ontwikkelingslanden."
    },
    {
        "type": "mc",
        "vraag": "Welke brandstof valt onder biomassa?",
        "opties": [
            "Houtsnippers, snoeiafval en dierlijke mest",
            "Steenkool uit diepe mijnschachten",
            "Ruwe aardolie uit boorplatforms",
            "Vloeibaar aardgas (LNG)"
        ],
        "antwoord": 0,
        "uitleg": "Biomassa bestaat uit organisch restmateriaal zoals hout, plantaardig afval en mest."
    },
    {
        "type": "mc",
        "vraag": "Wat is een belangrijk nadeel van wind- en zonne-energie ten opzichte van gascentrales?",
        "opties": [
            "Ze stoten bij de opwekking enorme hoeveelheden zwavel uit",
            "Ze zijn weersafhankelijk waardoor vraag en aanbod niet altijd gelijk lopen",
            "Ze kunnen alleen op de Noordpool geplaatst worden",
            "Ze veroorzaken een permanente verdwijning van de zwaartekracht"
        ],
        "antwoord": 1,
        "uitleg": "Doordat de wind niet altijd waait en de zon niet altijd schijnt, is opslag of back-upcapaciteit nodig."
    },
    {
        "type": "waaronwaar",
        "vraag": "Waterkrachtcentrales maken gebruik van vallend of snelstromend water om turbines in beweging te brengen.",
        "antwoord": true,
        "uitleg": "Waar: het hoogteverschil bij stuwdammen zet potentiële energie van water om in elektriciteit."
    },
    {
        "type": "waaronwaar",
        "vraag": "Zonnepanelen wekken alleen elektriciteit op als de buitentemperatuur warmer is dan 30 graden Celsius.",
        "antwoord": false,
        "uitleg": "Onwaar: zonnepanelen werken op lichtintensiteit en functioneren bij koud en helder weer juist zeer efficiënt."
    },
    {
        "type": "waaronwaar",
        "vraag": "De internationale luchtvaart en scheepvaart zijn vanaf het allereerste begin volledig opgenomen in de bindende doelen van het Parijs-akkoord.",
        "antwoord": false,
        "uitleg": "Onwaar: internationale luchtvaart en scheepvaart vallen grotendeels buiten de nationale afspraken van het Parijs-akkoord."
    },
    {
        "type": "invoer",
        "vraag": "Hoe noemen we energie afkomstig uit biologisch restafval zoals houtsnippers en mest?",
        "antwoord": "biomassa",
        "uitleg": "Biomassa is organisch materiaal dat gebruikt wordt om groene stroom, warmte of biobrandstoffen te maken."
    }
]
});

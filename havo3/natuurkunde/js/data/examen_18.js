/* Proeftoets 18 — Natuurkunde HAVO 3: Hoofdstuk 4 (Stoffen en materialen - Deel 3)
   Focus: Paragraaf 4.3 — Warmtetransport (geleiding, stroming, straling), warmtegeleidingscoëfficiënt en isolatie.
   20 vragen conform DURU ENGINE_SPEC. */
DURU.registerExamen({
  id: "ex-h3-natuurkunde-18",
  titel: "Toets 18 — Warmtetransport, Geleiding & Isolatie",
  vak: "Natuurkunde · HAVO 3 (H4)",
  icoon: "🏡",
  duurMin: 30,
  vragen: [
    {
      type: "mc",
      vraag: "Welke drie vormen van <b>warmtetransport</b> bestaan er in de natuurkunde?",
      opties: [
        "Geleiding, stroming en straling",
        "Verdamping, condensatie en smelten",
        "Reflectie, breking en absorptie",
        "Spanning, stroom en weerstand"
      ],
      antwoord: 0,
      uitleg: "De 3 vormen van warmtetransport zijn: Geleiding (conductie), Stroming (convectie) en Straling (radiatie)."
    },
    {
      type: "mc",
      vraag: "Hoe vindt warmtetransport plaats door <b>geleiding</b> in een vaste stof (bijv. een metalen lepel in hete soep)?",
      opties: [
        "Doordat hete moleculen door het metaal heen stromen naar de andere kant",
        "Doordat heftig trillende atomen hun beweging via botsingen doorgeven aan buuratomen",
        "Doordat het metaal licht uitzendt",
        "Doordat de soep verdampt"
      ],
      antwoord: 1,
      uitleg: "Geleiding gebeurt van atoom op atoom zonder dat de atomen zelf van hun plaats gaan."
    },
    {
      type: "mc",
      vraag: "Wat is <b>warmtestroming (convectie)</b>?",
      opties: [
        "Warmtetransport waarbij een warme vloeistof of warm gas zelf beweegt en opstijgt door een lagere dichtheid",
        "Warmteoverdracht door een vacuüm",
        "Warmte die door een stenen muur trekt",
        "Het trillen van atomen in een kristal"
      ],
      antwoord: 0,
      uitleg: "Bij stroming stijgt verwarmde vloeistof/gas op (kleinere dichtheid) en zakt koudere vloeistof/gas omlaag."
    },
    {
      type: "mc",
      vraag: "Welke vorm van warmtetransport kan als enige door het <b>vacuüm van de ruimte</b> reizen (zoals zonnewarmte naar de aarde)?",
      opties: [
        "Geleiding",
        "Stroming",
        "Warmtestraling (infraroodstraling)",
        "Geluidsgolven"
      ],
      antwoord: 2,
      uitleg: "Straling heeft geen tussenstof nodig en plant zich voort als elektromagnetische golven door het vacuüm."
    },
    {
      type: "waaronwaar",
      vraag: "Stilstaande lucht is een van de allerbeste <b>warmte-isolatoren</b> in de natuur.",
      antwoord: true,
      uitleg: "Waar. Gassen geleiden warmte extreem slecht omdat moleculen ver uit elkaar zitten. Isolatiematerialen (wol, piepschuim, dons) werken door lucht gevangen te houden."
    },
    {
      type: "mc",
      vraag: "Wat geeft de <b>warmtegeleidingscoëfficiënt (λ / lambda)</b> van een materiaal aan?",
      opties: [
        "Hoeveel het materiaal uitzet bij hitte",
        "Hoe goed of slecht het materiaal warmte doorlaat (in W/(m·K))",
        "De dichtheid van het materiaal",
        "Het smeltpunt van het materiaal"
      ],
      antwoord: 1,
      uitleg: "Lambda (λ) meet het warmtegeleidingsvermogen: metalen hebben een hoge λ (goede geleiders); glaswol/piepschuim hebben een zeer lage λ (goede isolatoren)."
    },
    {
      type: "waaronwaar",
      vraag: "Een goed isolatiemateriaal heeft een zo <b>HOOG mogelijke</b> warmtegeleidingscoëfficiënt (λ).",
      antwoord: false,
      uitleg: "Niet waar. Een isolator moet warmte juist slecht doorlaten, dus een zo LAAG mogelijke λ hebben (bijv. λ ≈ 0,035 W/m·K)."
    },
    {
      type: "mc",
      vraag: "Hoe werkt een <b>thermosfles (vacuümfles)</b> om warme drank urenlang heet te houden?",
      opties: [
        "Het vacuüm tussen de dubbele wand stopt geleiding en stroming, en de zilveren spiegellaag reflecteert warmtestraling terug",
        "Er zit een klein elektrisch verwarmingselement in de dop",
        "De fles maakt de drank zwaarder",
        "De fles laat geen zwaartekracht door"
      ],
      antwoord: 0,
      uitleg: "Vacuüm blokkeert geleiding en stroming; spiegelende wanden blokkeren straling."
    },
    {
      type: "invul",
      vraag: "Welk type modern isolatieglas bevat twee glasplaten met een edelgas (zoals argon) ertussen en een speciale warmtereflecterende coating?",
      antwoord: "HR++|HR++ glas|HR glas|dubbel glas",
      uitleg: "HR++ glas (Hoog Rendement glas) isoleert veel beter dan standaard dubbel glas."
    },
    {
      type: "mc",
      vraag: "Wat is <b>spouwmuurisolatie</b> bij een woning?",
      opties: [
        "De muren van buiten schilderen met witte verf",
        "De lege ruimte (spouw) tussen de binnen- en buitenmuur vullen met isolatieschuim, parels of minerale wol",
        "De ramen openzetten voor ventilatie",
        "Een extra verdieping op het huis bouwen"
      ],
      antwoord: 1,
      uitleg: "Het vullen van de luchtspouw voorkomt warmtestroming en geleiding door de buitenmuren."
    },
    {
      type: "waaronwaar",
      vraag: "Warme lucht boven een radiator stijgt op naar het plafond doordat warme lucht uitzet en daardoor een <b>lagere dichtheid</b> krijgt dan de koudere omringende lucht.",
      antwoord: true,
      uitleg: "Waar. Dit creëert een natuurlijke convectiestroom (circulatie) in de woonkamer."
    },
    {
      type: "invul",
      vraag: "Door een buitenmuur met oppervlakte A = 20 m² en dikte d = 0,20 m gaat bij een temperatuurverschil van 15 K een warmtestroom van 150 W. Bereken de warmtestroom als de muur <b>twee keer zo dik</b> wordt gemaakt (d = 0,40 m) bij hetzelfde temperatuurverschil (in Watt).",
      antwoord: "75|75 W|75 watt",
      uitleg: "Warmteverlies is omgekeerd evenredig met de dikte: 2× zo dik -> warmtestroom gehalveerd: 150 / 2 = 75 W."
    },
    {
      type: "mc",
      vraag: "Waarom voelt een metalen deurklink in de winter veel kouder aan dan een houten deur op exact dezelfde temperatuur (bijv. 5 °C)?",
      opties: [
        "Omdat de klink daadwerkelijk een lagere temperatuur heeft dan het hout",
        "Omdat metaal een goede warmtegeleider is en razendsnel warmte aan je hand onttrekt, terwijl hout warmte slecht geleidt",
        "Omdat hout zelf warmte produceert",
        "Omdat metaal magnetisch is"
      ],
      antwoord: 1,
      uitleg: "Beide hebben 5 °C, maar metaal geleidt warmte uit je vingers veel sneller weg, waardoor je koudesensoren een snelle temperatuurdaling voelen."
    },
    {
      type: "waaronwaar",
      vraag: "Donkere, matte voorwerpen absorberen warmtestraling veel beter dan glimmende, witte voorwerpen.",
      antwoord: true,
      uitleg: "Waar. Zwart/mat absorbeert en zendt straling goed uit; wit/glimmend reflecteert straling."
    },
    {
      type: "invul",
      vraag: "Welk materiaal dat veel in jassen en dekbedden wordt gebruikt houdt warmte vast doordat het miljoenen kleine luchtkamertjes vormt?",
      antwoord: "dons|veertjes|wol|watteer",
      uitleg: "Dons en wol sluiten stilstaande lucht in, wat zorgt voor een uitstekende isolatie."
    },
    {
      type: "mc",
      vraag: "Waarom plaatst men vaak <b>radiatorfolie</b> achter een verwarmingsradiator tegen de buitenmuur?",
      opties: [
        "Om de muur te versieren",
        "Om de infrarode warmtestraling van de achterkant van de radiator terug de kamer in te reflecteren i.p.v. de buitenmuur op te warmen",
        "Om stof tegen te houden",
        "Om het water in de radiator sneller te laten stromen"
      ],
      antwoord: 1,
      uitleg: "De glimmende folie weerkaatst IR-warmtestraling direct terug de woonkamer in."
    },
    {
      type: "waaronwaar",
      vraag: "Goede woningisolatie (dak, muren, vloer en glas) verlaagt het aardgasverbruik, bespaart stookkosten en vermindert de CO₂-uitstoot van het huishouden.",
      antwoord: true,
      uitleg: "Waar."
    },
    {
      type: "invul",
      vraag: "Een dubbelwandige ruit van 3,0 m² verliest bij strenge vorst 450 J warmte per seconde. Hoeveel Watt is het warmteverliesvermogen (P = Q / t)?",
      antwoord: "450|450 W|450 watt",
      uitleg: "1 Watt = 1 Joule per seconde, dus 450 J/s = 450 W."
    },
    {
      type: "open",
      vraag: "Benoem de drie vormen van warmtetransport die optreden bij een pannetje soep dat op een gasfornuis warm wordt gemaakt, en leg bij elk uit waar dit in de pan gebeurt.",
      sleutelwoorden: ["geleiding door de metalen panbodem", "stroming / convectie in de vloeibare soep", "straling van de gasvlam naar de pan / warmtestraling"],
      minTreffers: 3,
      modelantwoord: "1. Geleiding: De hitte van de vlam trekt via trillende metaalatomen door de stalen panbodem naar de binnenkant van de pan. 2. Stroming (convectie): De soep onderin wordt heet, zet uit, krijgt een lagere dichtheid en stijgt op, terwijl koudere soep naar beneden zakt (circulatie in de vloeistof). 3. Straling: De hete vlam en de hete buitenkant van de pan zenden infrarode warmtestraling uit naar de omgeving.",
      uitleg: "Geleiding door de bodem, stroming in de soep en straling van de vlam/pan."
    },
    {
      type: "open",
      vraag: "Leg uit waarom het dak van een woning vaak als eerste geïsoleerd wordt bij een energiebesparende renovatie. Betrek daarin de eigenschappen van <b>warme lucht</b>.",
      sleutelwoorden: ["warme lucht stijgt op / convectie", "hoogste temperatuur onder het dak", "grootste warmteverlies via het dak"],
      minTreffers: 2,
      modelantwoord: "Doordat warme lucht uitzet en een lagere dichtheid heeft dan koude lucht, stijgt warme lucht in het hele huis van nature op naar de bovenste verdieping (stroming/convectie). Hierdoor is de temperatuur direct onder het dak het allerhoogst, waardoor het temperatuurverschil met de buitenlucht en dus het warmteverlies door het ongeïsoleerde dak het grootst is (tot wel 30% van het totale verlies).",
      uitleg: "Opstijgende warme lucht veroorzaakt het grootste temperatuurverschil en warmteverlies bij het dak."
    }
  ]
});

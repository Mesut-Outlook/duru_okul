/* Extra Proeftoets 4 — Consument & Overheid */
DURU.registerExamen({
  id: "ex-extra-consument-overheid",
  titel: "Extra Proeftoets 4 — Consument & Overheid",
  vak: "Economie · Consumenten",
  icoon: "🛒",
  duurMin: 15,
  vragen: [
    {
      type: "mc",
      vraag: "Welke instantie in Nederland houdt toezicht op consumentenrechten en eerlijke concurrentie tussen bedrijven?",
      opties: [
        "De Consumentenbond",
        "De Belastingdienst",
        "De Autoriteit Consument & Markt (ACM)",
        "De Eerste Kamer"
      ],
      antwoord: 2,
      uitleg: "De <b>ACM</b> is een overheidsinstantie die toeziet op eerlijke concurrentie en consumentenbelangen beschermt tegen bijvoorbeeld kartels."
    },
    {
      type: "mc",
      vraag: "Wat is het belangrijkste doel van invoerrechten op buitenlandse goederen?",
      opties: [
        "Het stimuleren van vliegverkeer.",
        "Eigen producenten beschermen door buitenlandse producten kunstmatig duurder te maken.",
        "De btw automatisch verlagen naar 9%.",
        "Het verkorten van de levertijd van pakketjes."
      ],
      antwoord: 1,
      uitleg: "<b>Invoerrechten</b> zijn belastingen op importproducten. Hierdoor worden buitenlandse goederen duurder, wat consumenten stimuleert om producten uit eigen land/regio te kopen."
    },
    {
      type: "mc",
      vraag: "Wat houdt de 'Wet koop op afstand' (bedenktijd) wettelijk in voor online aankopen?",
      opties: [
        "De consument mag het product binnen 14 dagen zonder reden terugsturen en krijgt zijn geld terug.",
        "De consument moet minimaal 10 kilometer van de winkel wonen om te mogen bestellen.",
        "Winkels hoeven online bestellingen nooit retour te nemen.",
        "De bezorgtijd mag maximaal 24 uur bedragen."
      ],
      antwoord: 0,
      uitleg: "Bij online aankopen heeft een consument wettelijk recht op <b>14 dagen bedenktijd</b> (herroepingsrecht) omdat hij het product niet fysiek kon beoordelen voor de aankoop."
    },
    {
      type: "mc",
      vraag: "Waarom heft de overheid accijns op tabak, benzine en alcohol?",
      opties: [
        "Omdat deze goederen heel goedkoop te maken zijn.",
        "Om het gebruik van schadelijke of milieuvervuilende producten af te remmen.",
        "Omdat de koning deze producten zelf veel gebruikt.",
        "Om te zorgen dat er minder winkels in Nederland komen."
      ],
      antwoord: 1,
      uitleg: "Accijns is een **accijnsheffing** bedoeld om de consumptie van ongezonde of schadelijke goederen (demeritorische goederen) te ontmoedigen."
    },
    {
      type: "mc",
      vraag: "Wat is een kartel?",
      opties: [
        "Een vereniging van consumenten die samen korting vragen.",
        "Een verboden afspraak tussen bedrijven om onderling niet te concurreren en de prijzen hoog te houden.",
        "Een speciaal soort belasting op luxe auto's.",
        "Een ministerie dat wetten maakt over landbouw."
      ],
      antwoord: 1,
      uitleg: "In een <b>kartel</b> maken concurrenten verboden prijsafspraken. Dit benadeelt de consument en is verboden door de Mededingingswet."
    },
    {
      type: "waaronwaar",
      vraag: "Als je een jas koopt in een gewone fysieke kledingwinkel, heb je volgens de wet altijd recht op geld terug als je spijt hebt van de aankoop.",
      antwoord: false,
      uitleg: "Onwaar. 'Ruilen is een gunst' in fysieke winkels. De winkelier bepaalt zelf de regels (bijv. alleen een tegoedbon). Alleen bij online aankopen is geld terug wettelijk verplicht."
    },
    {
      type: "waaronwaar",
      vraag: "De Consumentenbond is een onafhankelijke vereniging en maakt geen wetten namens de overheid.",
      antwoord: true,
      uitleg: "Waar. De <b>Consumentenbond</b> komt op voor consumenten en geeft advies, maar de wetgeving ligt volledig bij de overheid en het parlement."
    },
    {
      type: "invul",
      vraag: "Als de overheid de verkoop van een product (zoals vuurwerk of bepaalde medicijnen) verbiedt, noemen we dat een verkoop____.",
      antwoord: "verbod|verboden",
      uitleg: "Een <b>verkoopverbod</b> beschermt consumenten tegen gevaarlijke of schadelijke producten."
    },
    {
      type: "open",
      vraag: "Leg uit waarom de overheid wetten maakt die de consument beschermen, en geef een voorbeeld.",
      sleutelwoorden: ["machtspositie/zwakker/beschermen", "informatie/misleiding/misleiden", "veiligheid/kwaliteit/bedenktijd/wet/garantie"],
      minTreffers: 2,
      modelantwoord: "De overheid beschermt consumenten omdat zij een zwakkere positie hebben ten opzichte van grote winkeliers en producenten. Wetten voorkomen misleiding, zorgen voor veilige producten en geven rechten zoals de wettelijke bedenktijd bij online aankopen.",
      uitleg: "Wetgeving herstelt de balans tussen de machtige producent/verkoper en de individuele consument."
    },
    {
      type: "open",
      vraag: "Wat is het verschil tussen btw en accijns?",
      sleutelwoorden: ["accijns/specifiek/bepaald", "btw/algemeen/percentage", "remmen/gezondheid/schadelijk"],
      minTreffers: 2,
      modelantwoord: "Btw is een algemene omzetbelasting die op bijna elk product en elke dienst zit als percentage van de prijs (9% of 21%). Accijns is een extra, specifieke belasting die per volume (bijvoorbeeld per liter of per pakje) wordt geheven op geselecteerde schadelijke goederen zoals tabak en alcohol om het gebruik te remmen.",
      uitleg: "Btw = algemeen percentage. Accijns = vast bedrag per hoeveelheid op schadelijke goederen."
    }
  ]
});

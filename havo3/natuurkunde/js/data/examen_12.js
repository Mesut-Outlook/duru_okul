/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Toets 12 — Atoombouw, Kernstraling & Halveringstijd
   ========================================================= */
DURU.registerExamen({
  "id": "ex-h3-natuurkunde-12",
  "titel": "Toets 12 — Atoombouw, Kernstraling & Halveringstijd",
  "vak": "Natuurkunde · HAVO 3 (H3)",
  "icoon": "⚛️",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Waaruit bestaat de <b>atoomkern</b> van een atoom?",
      "opties": [
        "Protonen (positief) en neutronen (neutraal)",
        "Alleen elektronen",
        "Protonen en elektronen",
        "Alleen fotonen"
      ],
      "antwoord": 0,
      "uitleg": "De atoomkern bevat positieve protonen en ongeladen neutronen. De negatieve elektronen bewegen in een wolk om de kern heen."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn <b>isotopen</b> van hetzelfde chemische element?",
      "opties": [
        "Atomen met hetzelfde aantal neutronen, maar verschillend aantal protonen",
        "Atomen met hetzelfde aantal protonen, maar een verschillend aantal neutronen in de kern",
        "Atomen die altijd positief geladen zijn",
        "Atomen van verschillende elementen met hetzelfde gewicht"
      ],
      "antwoord": 1,
      "uitleg": "Isotopen hebben hetzelfde atoomnummer (aantal protonen), maar een andere massa door een afwijkend aantal neutronen (bijv. Koolstof-12 en Koolstof-14)."
    },
    {
      "type": "invul",
      "vraag": "Een atoomkern van Koolstof-14 (¹⁴₆C) heeft atoomnummer 6 en massagetal 14. Hoeveel <b>neutronen</b> zitten er in deze kern?",
      "antwoord": "8|acht",
      "uitleg": "Aantal neutronen = massagetal - atoomnummer = 14 - 6 = 8 neutronen."
    },
    {
      "type": "mc",
      "vraag": "Waaruit bestaat <b>alfastraling (α)</b>?",
      "opties": [
        "Snelle elektronen",
        "Lichtdeeltjes zonder massa",
        "Heliumkernen (2 protonen en 2 neutronen)",
        "Losse neutronen"
      ],
      "antwoord": 2,
      "uitleg": "Een alfadeeltje is een positief geladen heliumkern (⁴₂He²⁺) bestaande uit 2 protonen en 2 neutronen."
    },
    {
      "type": "mc",
      "vraag": "Waaruit bestaat <b>bètastraling (β)</b>?",
      "opties": [
        "Protonen",
        "Heliumkernen",
        "Golven met ultrahoge frequentie",
        "Snelle elektronen die uit de atoomkern weggeschoten worden"
      ],
      "antwoord": 3,
      "uitleg": "Bij bètaverval verandert een neutron in een proton en wordt een snel elektron (bètadeeltje) uit de kern weggeschoten."
    },
    {
      "type": "mc",
      "vraag": "Wat is <b>gammastraling (γ)</b>?",
      "opties": [
        "Zeer energierijke elektromagnetische straling (fotonen) zonder massa of lading",
        "Een stroom zware positieve deeltjes",
        "Een stroom van losse neutronen",
        "Hetzelfde als radiogolven"
      ],
      "antwoord": 0,
      "uitleg": "Gammastraling is elektromagnetische straling met extreem hoge frequentie die vrijkomt bij radioactief kernverval."
    },
    {
      "type": "waaronwaar",
      "vraag": "Alfastraling heeft een zeer groot ioniserend vermogen, maar een heel klein doordringend vermogen (wordt al gestopt door een velletje papier).",
      "antwoord": true,
      "uitleg": "Waar. Omdat alfadeeltjes zwaar en dubbel positief geladen zijn, botsen ze snel en worden ze al door papier of de bovenste dode huidlaag tegengehouden."
    },
    {
      "type": "mc",
      "vraag": "Welk materiaal is minimaal nodig om <b>bètastraling (β)</b> tegen te houden?",
      "opties": [
        "Een velletje papier",
        "Een dunne plaat aluminium of plexiglas (enkele millimeters)",
        "Een loden muur van 30 cm dik",
        "Niets kan bètastraling tegenhouden"
      ],
      "antwoord": 1,
      "uitleg": "Bètastraling gaat door papier heen, maar wordt gestopt door een aluminiumplaatje of dik perspex."
    },
    {
      "type": "mc",
      "vraag": "Welk materiaal is nodig om <b>gammastraling (γ)</b> effectief af te zwakken?",
      "opties": [
        "Een vel papier",
        "Een laag plastic",
        "Een dikke laag lood of een dikke betonmuur",
        "Alleen een dun kartonnetje"
      ],
      "antwoord": 2,
      "uitleg": "Gammastraling heeft een zeer groot doordringend vermogen en vereist zware materialen zoals lood of dik beton."
    },
    {
      "type": "invul",
      "vraag": "Wat is de eenheid van radioactieve <b>activiteit (A)</b> (het aantal kernen dat per seconde vervalt)?",
      "antwoord": "Becquerel|Bq|becquerel",
      "uitleg": "Activiteit wordt gemeten in Becquerel (Bq). 1 Bq = 1 kernverval per seconde."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent het begrip <b>halveringstijd (t₁/₂)</b> van een radioactieve stof?",
      "opties": [
        "De tijd waarna de radioactiviteit helemaal nul is geworden",
        "De tijd die nodig is om een atoom in tweeën te splijten",
        "De helft van de leeftijd van het heelal",
        "De tijd waarin de helft van het aantal instabiele radioactieve atoomkernen is vervallen"
      ],
      "antwoord": 3,
      "uitleg": "De halveringstijd is de vaste tijd waarin 50% van de radioactieve kernen spontaan vervalt."
    },
    {
      "type": "invul",
      "vraag": "Een radioactieve bron heeft een activiteit van 800 Bq. De halveringstijd is 6 uur. Hoe groot is de activiteit na <b>12 uur</b> (in Bq)?",
      "antwoord": "200|200 Bq|200Bq",
      "uitleg": "12 uur = 2 halveringstijden. Na 6 uur: 800 / 2 = 400 Bq. Na 12 uur: 400 / 2 = 200 Bq."
    },
    {
      "type": "invul",
      "vraag": "Van een radioactieve stof met een halveringstijd van 10 dagen is na 30 dagen nog 25 gram over. Hoeveel gram van de stof was er in het begin (op t = 0)?",
      "antwoord": "200|200 g|200 gram|200g",
      "uitleg": "30 dagen = 3 halveringstijden. Terugrekenen: 25 × 2 = 50 g (na 20 d); 50 × 2 = 100 g (na 10 d); 100 × 2 = 200 g in het begin."
    },
    {
      "type": "waaronwaar",
      "vraag": "Je kunt de halveringstijd van een radioactieve stof verkorten door de stof te verhitten in een oven of onder hoge druk te zetten.",
      "antwoord": false,
      "uitleg": "Niet waar. Radioactief verval is een spontaan nucleair proces in de atoomkern; chemische of fysische omstandigheden zoals hitte of druk hebben hier geen enkele invloed op."
    },
    {
      "type": "mc",
      "vraag": "Een monster bevat 100% instabiele kernen. Welk percentage van de oorspronkelijke instabiele kernen is na <b>3 halveringstijden</b> nog over?",
      "opties": [
        "12,5%",
        "25%",
        "50%",
        "6,25%"
      ],
      "antwoord": 0,
      "uitleg": "Na 1× t₁/₂: 50%. Na 2× t₁/₂: 25%. Na 3× t₁/₂: 12,5%."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een instabiele atoomkern die straling uitzendt verandert in een kern van een ander chemisch element (tenzij het puur gammaverval betreft).",
      "antwoord": true,
      "uitleg": "Waar. Bij alfa- en bètaverval verandert het aantal protonen in de kern, waardoor er een ander atoomsoort (dochterkern) ontstaat."
    },
    {
      "type": "invul",
      "vraag": "De medische isotoop Technetium-99m heeft een halveringstijd van 6,0 uur. Een patiënt krijgt om 08:00 uur een dosis met activiteit 640 MBq ingespoten. Hoeveel MBq is de activiteit van de tracer om 20:00 uur dezelfde dag (na 12 uur)?",
      "antwoord": "160|160 MBq|160MBq",
      "uitleg": "Van 08:00 tot 20:00 is 12 uur = 2 halveringstijden. Activiteit: 640 -> 320 -> 160 MBq."
    },
    {
      "type": "mc",
      "vraag": "Welke stralingsmeter wordt gebruikt om radioactiviteit hoorbaar (tikken) en zichtbaar te meten?",
      "opties": [
        "Voltmeter",
        "Geiger-Müller-teller (Geigerteller)",
        "Barometer",
        "Thermometer"
      ],
      "antwoord": 1,
      "uitleg": "Een Geiger-Müller-telbuis detecteert geïoniseerde gasdeeltjes veroorzaakt door passerende kernstraling."
    },
    {
      "type": "open",
      "vraag": "Vergelijk <b>alfastraling</b> en <b>gammastraling</b> op de volgende twee eigenschappen: 1) het ioniserend vermogen, 2) het doordringend vermogen.",
      "sleutelwoorden": [
        "alfastraling groot ioniserend vermogen",
        "gammastraling klein ioniserend vermogen",
        "alfastraling klein doordringend vermogen",
        "gammastraling groot doordringend vermogen"
      ],
      "minTreffers": 3,
      "modelantwoord": "1. Ioniserend vermogen: Alfastraling heeft een zeer groot ioniserend vermogen (richt door zijn dubbele lading en massa veel schade aan over korte afstand). Gammastraling heeft een relatief klein ioniserend vermogen.\n2. Doordringend vermogen: Alfastraling heeft een zeer klein doordringend vermogen (wordt gestopt door papier of huid). Gammastraling heeft juist een extreem groot doordringend vermogen (gaat door het hele lichaam heen en vereist dik lood/beton).",
      "uitleg": "Tegengestelde eigenschappen: alfa = hoog ioniserend/laag doordringend; gamma = laag ioniserend/hoog doordringend."
    },
    {
      "type": "open",
      "vraag": "In een laboratorium wordt de activiteit van een onbekende radioactieve stof gemeten. Op $t = 0$ is de activiteit 1200 Bq. Na 45 minuten is de activiteit gedaald naar 150 Bq. Bereken de <b>halveringstijd</b> van deze stof.",
      "sleutelwoorden": [
        "3 halveringstijden",
        "150/drie halveringstijden",
        "15 minuten/15 min/15"
      ],
      "minTreffers": 2,
      "modelantwoord": "De activiteit halveert van 1200 -> 600 (1x) -> 300 (2x) -> 150 Bq (3x). Er zijn dus 3 halveringstijden verstreken in 45 minuten. De halveringstijd is dus: t₁/₂ = 45 minuten / 3 = 15 minuten.",
      "uitleg": "Drie opeenvolgende halveringen in 45 min -> halveringstijd is 15 minuten."
    }
  ]
});

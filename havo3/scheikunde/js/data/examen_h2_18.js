/* =========================================================
   Duru's Scheikunde (HAVO 3) — Toets 18 — §2.3 Formuletaal (2)
   Hoofdstuk 2 (Chemie Overal), §2.3 Formuletaal — naamgeving, molecuulmassa, massapercentage, experiment 2.6
   20 vragen · 30 minuten. Alleen wat letterlijk in het boek staat.
   Atoommassa's uit het boek: H = 1,008 u; C = 12,01 u; O = 16,00 u.
   ========================================================= */
DURU.registerExamen({
  "id": "ex-h3-sch-h2-18",
  "hoofdstuk": 2,
  "paragraaf": "2.3",
  "titel": "Toets 18 — §2.3 Formuletaal (2)",
  "vak": "Scheikunde · HAVO 3 (H2 — §2.3)",
  "icoon": "🧪",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat betekent het als een stof een <b>triviale naam</b> heeft, zoals methaan of ammoniak?",
      "opties": [
        "De officiële scheikundige naam van de stof",
        "Een naam die alleen uit voorvoegsels bestaat",
        "Het is een alledaagse naam en niet de officiële naam",
        "Een naam die je afleidt uit de formule"
      ],
      "antwoord": 2,
      "uitleg": "Een triviale naam is een alledaagse naam (bijvoorbeeld methaan, ammoniak). De officiële scheikundige naam is de systematische naam."
    },
    {
      "type": "mc",
      "vraag": "Wat is de systematische naam van N<sub>2</sub>O<sub>4</sub>?",
      "opties": [
        "distikstoftetraoxide",
        "stikstofdioxide",
        "distikstofdioxide",
        "stikstoftetraoxide"
      ],
      "antwoord": 0,
      "uitleg": "De index van N is 2 (di-) en die van O is 4 (tetra-): distikstoftetraoxide. Beide indexen zijn groter dan 1, dus beide atoomsoorten krijgen een voorvoegsel."
    },
    {
      "type": "mc",
      "vraag": "Welk voorvoegsel hoort bij index <b>4</b>?",
      "opties": [
        "penta",
        "tri",
        "hexa",
        "tetra"
      ],
      "antwoord": 3,
      "uitleg": "Tabel 2.23: 1 mono, 2 di, 3 tri, 4 tetra, 5 penta, 6 hexa."
    },
    {
      "type": "mc",
      "vraag": "Welk achtervoegsel hoort bij de tweede atoomsoort <b>zwavel</b> (S) in een formule?",
      "opties": [
        "-oxide",
        "-sulfide",
        "-chloride",
        "-fluoride"
      ],
      "antwoord": 1,
      "uitleg": "Tabel 2.24: O -oxide, S -sulfide, F -fluoride, Cl -chloride, Br -bromide, I -jodide."
    },
    {
      "type": "mc",
      "vraag": "Wat is de formule van <b>koolstofdisulfide</b>?",
      "opties": [
        "CS<sub>2</sub>",
        "C<sub>2</sub>S",
        "C<sub>2</sub>S<sub>2</sub>",
        "CS"
      ],
      "antwoord": 0,
      "uitleg": "Koolstof heeft geen voorvoegsel (index 1), 'di' bij sulfide betekent index 2 bij S: CS<sub>2</sub>."
    },
    {
      "type": "mc",
      "vraag": "Wat is de systematische naam van <b>CO</b>?",
      "opties": [
        "monokoolstofmono-oxide",
        "koolstofoxide",
        "koolstofmono-oxide",
        "koolstofdioxide"
      ],
      "antwoord": 2,
      "uitleg": "Bij CO hoort wel 'mono' bij de tweede atoomsoort: koolstofmono-oxide. Bij de eerste atoomsoort laat je 'mono' weg."
    },
    {
      "type": "mc",
      "vraag": "Bereken de molecuulmassa van methaan (CH<sub>4</sub>) met C = 12,01 u en H = 1,008 u. Rond af op twee decimalen.",
      "opties": [
        "17,01 u",
        "28,02 u",
        "13,02 u",
        "16,04 u"
      ],
      "antwoord": 3,
      "uitleg": "12,01 + 4 × 1,008 = 12,01 + 4,032 = 16,042 ≈ 16,04 u."
    },
    {
      "type": "mc",
      "vraag": "Waarmee komt <b>1,00 u</b> overeen?",
      "opties": [
        "1,66·10<sup>-27</sup> g",
        "1,66·10<sup>-27</sup> kg",
        "1,66·10<sup>-24</sup> kg",
        "1,00·10<sup>-27</sup> kg"
      ],
      "antwoord": 1,
      "uitleg": "De atomaire massa-eenheid: 1,00 u komt overeen met 1,66·10<sup>-27</sup> kg."
    },
    {
      "type": "mc",
      "vraag": "Waar staat de <b>atoommassa</b> van een atoomsoort in het vakje van het periodiek systeem?",
      "opties": [
        "rechtsonder",
        "linksonder",
        "linksboven",
        "rechtsboven"
      ],
      "antwoord": 2,
      "uitleg": "De atoommassa (in u) staat linksboven in het vakje, bijvoorbeeld 16,00 bij zuurstof."
    },
    {
      "type": "mc",
      "vraag": "Hoe bereken je het <b>massapercentage</b> van een atoomsoort in een molecuul?",
      "opties": [
        "massa atoomsoort / molecuulmassa × 100%",
        "molecuulmassa / massa atoomsoort × 100%",
        "massa atoomsoort × molecuulmassa",
        "massa atoomsoort − molecuulmassa"
      ],
      "antwoord": 0,
      "uitleg": "Massapercentage = (massa van de atoomsoort in het molecuul / molecuulmassa) × 100%."
    },
    {
      "type": "waaronwaar",
      "vraag": "De systematische naam van CO<sub>2</sub> is monokoolstofdioxide.",
      "antwoord": false,
      "uitleg": "Niet waar: komt de eerste atoomsoort maar één keer voor, dan gebruik je daar geen 'mono'. Het is koolstofdioxide."
    },
    {
      "type": "waaronwaar",
      "vraag": "De systematische naam van Br<sub>2</sub>S is dibroommonosulfide.",
      "antwoord": true,
      "uitleg": "Waar: 'di' bij broom (index 2) en 'mono' bij sulfide (index 1, tweede atoomsoort)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een cafeïnemolecuul, C<sub>8</sub>H<sub>10</sub>N<sub>4</sub>O<sub>2</sub>, bestaat uit in totaal 24 atomen.",
      "antwoord": true,
      "uitleg": "Waar: 8 + 10 + 4 + 2 = 24 atomen."
    },
    {
      "type": "waaronwaar",
      "vraag": "De massa van atomen in het periodiek systeem staat uitgedrukt in gram.",
      "antwoord": false,
      "uitleg": "Niet waar: de massa staat in u (atomaire massa-eenheden), omdat gram veel te groot is voor één atoom."
    },
    {
      "type": "waaronwaar",
      "vraag": "In experiment 2.6 zet je zelf moleculen in elkaar.",
      "antwoord": true,
      "uitleg": "Waar: experiment 2.6 heet 'Moleculen bouwen'; je zet daarin zelf moleculen in elkaar."
    },
    {
      "type": "invul",
      "vraag": "Bereken de molecuulmassa van koolstofdioxide (C = 12,01 u; O = 16,00 u). Geef alleen het getal, met twee decimalen.",
      "antwoord": "44,01|44.01",
      "uitleg": "CO<sub>2</sub>: 1 × 12,01 + 2 × 16,00 = 12,01 + 32,00 = 44,01 u."
    },
    {
      "type": "invul",
      "vraag": "Bereken het massapercentage koolstof in glucose, C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> (C = 12,01 u; molecuulmassa glucose = 180,16 u). Geef alleen het getal, met twee decimalen.",
      "antwoord": "40,00|40,0|40|40.00|40.0",
      "uitleg": "Massa C = 6 × 12,01 = 72,06 u. Massapercentage = 72,06 / 180,16 × 100% = 40,00%."
    },
    {
      "type": "invul",
      "vraag": "Schrijf de formule van dizwaveldichloride (schrijf de index als gewoon cijfer, bijvoorbeeld H2O).",
      "antwoord": "S2Cl2|S₂Cl₂",
      "uitleg": "'di' bij zwavel (index 2) en 'di' bij chloride (index 2): S<sub>2</sub>Cl<sub>2</sub>."
    },
    {
      "type": "open",
      "vraag": "Leg uit waarom de systematische naam van CO<sub>2</sub> koolstofdioxide is en niet monokoolstofdioxide.",
      "sleutelwoorden": [
        "eerste atoomsoort/eerste atoom/eerste element",
        "één keer/maar één/1 keer/één atoom"
      ],
      "minTreffers": 2,
      "modelantwoord": "Bij de eerste atoomsoort in de formule gebruik je geen 'mono' als die maar één keer voorkomt. Koolstof komt maar één keer voor in het molecuul, dus 'mono' laat je weg.",
      "uitleg": "Komt de eerste atoomsoort in de formule maar één keer voor, dan zet je er geen 'mono' voor. Bij de tweede atoomsoort (mono-oxide) moet 'mono' wel."
    },
    {
      "type": "open",
      "vraag": "Bereken het massapercentage zuurstof in CO<sub>2</sub> (C = 12,01 u; O = 16,00 u; twee decimalen). Laat zien hoe je rekent.",
      "sleutelwoorden": [
        "44,01/44.01",
        "32,00/32",
        "72,71/72,7/72.71"
      ],
      "minTreffers": 2,
      "modelantwoord": "Molecuulmassa CO<sub>2</sub> = 12,01 + 2 × 16,00 = 44,01 u. Massa zuurstof = 2 × 16,00 = 32,00 u. Massapercentage O = 32,00 / 44,01 × 100% = 72,71%.",
      "uitleg": "Eerst de totale molecuulmassa (44,01 u), dan de massa van de gevraagde atoomsoort (32,00 u), deel en vermenigvuldig met 100%: 72,71%."
    }
  ]
});

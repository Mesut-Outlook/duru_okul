/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 16 — §1.3 Formules substitueren
   Bron: Noordhoff H1 Lineaire en exponentiële formules, §1.3 (voorbeeld 1–2, opgave 15–22)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-h1-6",
  "hoofdstuk": 1,
  "paragraaf": "1.3",
  "titel": "Proeftoets 16 — §1.3 Substitueren in context",
  "vak": "Wiskunde · H1 Lineaire en exponentiële formules",
  "icoon": "🔁",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Een fabrikant produceert in t weken a = 400t apparaten (formule B). De kosten k in euro's zijn k = 6a + 900 (formule A). Stel door substitueren een formule op voor k in t. Welke formule krijg je?",
      "opties": [
        "k = 2400t + 900",
        "k = −2400t + 900",
        "k = 2400t + 906",
        "k = 2400t"
      ],
      "antwoord": 0,
      "uitleg": "<b>Stap 2 – substitueren:</b> Vervang a in k = 6a + 900 door de uitdrukking. k = 6(400t) + 900.<br><b>Stap 3 – haakjes wegwerken:</b> Hier zijn geen haakjes nodig: je vult maar één term in. Er valt niets weg te werken.<br><b>Stap 4 – vereenvoudigen:</b> Tel de getallen zonder letter bij elkaar op. k = 2400t + 900.<br>💡 <i>Haakjes zijn alleen nodig bij een uitdrukking met meer termen of met een minteken; een enkele term zoals 3p hoeft niet.</i>"
    },
    {
      "type": "invul",
      "vraag": "Een belabonnement kost K = 0,09m + 6 euro bij m belminuten (formule A). Je belt per dag 40 minuten, dus m = 40d bij d dagen (formule B). Substitueer formule B in formule A en vereenvoudig. De eindformule heeft de vorm K = (getal)d + (getal). Welk getal staat vóór de d? ____",
      "antwoord": "3,6|3.6",
      "uitleg": "<b>Stap 2 – substitueren:</b> Vervang m in K = 0,09m + 6 door de uitdrukking. K = 0,09(40d) + 6.<br><b>Stap 3 – haakjes wegwerken:</b> Hier zijn geen haakjes nodig: je vult maar één term in. Er valt niets weg te werken.<br><b>Stap 4 – vereenvoudigen:</b> Tel de getallen zonder letter bij elkaar op. K = 3,6d + 6.<br>💡 <i>Haakjes zijn alleen nodig bij een uitdrukking met meer termen of met een minteken; een enkele term zoals 3p hoeft niet.</i>"
    },
    {
      "type": "invul",
      "vraag": "Een fabrikant produceert in t weken a = 400t apparaten (formule B). De kosten k in euro's zijn k = 6a + 900 (formule A). Bereken k als t = 5. k = ____",
      "antwoord": "12900",
      "uitleg": "Via de eindformule: k = 2400t + 900 met t = 5 geeft k = 2400 × 5 + 900 = 12900. Controle in twee stappen: a = 2000, dus k = 12900.<br><b>Stap 2 – substitueren:</b> Vervang a in k = 6a + 900 door de uitdrukking. k = 6(400t) + 900.<br><b>Stap 3 – haakjes wegwerken:</b> Hier zijn geen haakjes nodig: je vult maar één term in. Er valt niets weg te werken.<br><b>Stap 4 – vereenvoudigen:</b> Tel de getallen zonder letter bij elkaar op. k = 2400t + 900.<br>💡 <i>Haakjes zijn alleen nodig bij een uitdrukking met meer termen of met een minteken; een enkele term zoals 3p hoeft niet.</i>"
    },
    {
      "type": "waaronwaar",
      "vraag": "Een taxirit van k kilometer kost p = 1,75k + 3 euro (formule A). De taxi rijdt in t minuten k = 0,6t kilometer (formule B). Na substitueren en vereenvoudigen krijg je p = 1,05t − 3.",
      "antwoord": false,
      "uitleg": "Onwaar. De juiste eindformule is p = 1,05t + 3; p = 1,05t − 3 bevat een rekenfout.<br><b>Stap 2 – substitueren:</b> Vervang k in p = 1,75k + 3 door de uitdrukking. p = 1,75(0,6t) + 3.<br><b>Stap 3 – haakjes wegwerken:</b> Hier zijn geen haakjes nodig: je vult maar één term in. Er valt niets weg te werken.<br><b>Stap 4 – vereenvoudigen:</b> Tel de getallen zonder letter bij elkaar op. p = 1,05t + 3.<br>💡 <i>Haakjes zijn alleen nodig bij een uitdrukking met meer termen of met een minteken; een enkele term zoals 3p hoeft niet.</i>"
    },
    {
      "type": "mc",
      "vraag": "Op h meter hoogte is de temperatuur T = 20 − 0,006h graden Celsius (formule A). Een wandelaar is na k kwartier wandelen op hoogte h = 9k + 150 meter (formule B). Stel door substitueren een formule op voor T in k. Welke formule krijg je?",
      "opties": [
        "T = −0,054k − 20,9",
        "T = −0,054k + 170",
        "T = −0,054k + 19,1",
        "T = 9k + 19,1"
      ],
      "antwoord": 2,
      "uitleg": "<b>Stap 2 – substitueren:</b> Vervang h in T = 20 − 0,006h door de hele uitdrukking tussen haakjes. T = 20 − 0,006(9k + 150).<br><b>Stap 3 – haakjes wegwerken:</b> Vermenigvuldig elke term binnen de haakjes met −0,006 (denk aan de tekens). T = 20 − 0,054k − 0,9.<br><b>Stap 4 – vereenvoudigen:</b> Tel de getallen zonder letter bij elkaar op. T = −0,054k + 19,1.<br>💡 <i>Let op de tekens: min maal min is plus, min maal plus is min.</i>"
    },
    {
      "type": "mc",
      "vraag": "Een bakker gebruikt per dag 2a + 3b = 24 kilo meel voor a broden en b taarten (formule B). De kosten in euro's zijn K = 8a + 20 (formule A). Herleid formule B zodat a wordt uitgedrukt in b. Welke formule krijg je?",
      "opties": [
        "a = −1,5b + 12",
        "a = 1,5b + 12",
        "a = 3b − 24",
        "a = −3b + 24"
      ],
      "antwoord": 0,
      "uitleg": "<b>Stap 1 – herleiden:</b> Maak a vrij met de balansmethode (trek de b-term aan beide kanten af en deel alles door 2). 2a + 3b = 24 → 2a = −3b + 24, daarna delen door 2: a = −1,5b + 12.<br><b>Stap 2 – substitueren:</b> Vervang a in K = 8a + 20 door de hele uitdrukking tussen haakjes. K = 8(−1,5b + 12) + 20.<br><b>Stap 3 – haakjes wegwerken:</b> Vermenigvuldig elke term binnen de haakjes met 8 (denk aan de tekens). K = −12b + 96 + 20.<br><b>Stap 4 – vereenvoudigen:</b> Tel de getallen zonder letter bij elkaar op. K = −12b + 116.<br>💡 <i>Herleid eerst: deel bij de balansmethode ook het getal rechts door hetzelfde getal.</i>"
    },
    {
      "type": "waaronwaar",
      "vraag": "Een belabonnement kost K = 0,09m + 6 euro bij m belminuten (formule A). Je belt per dag 40 minuten, dus m = 40d bij d dagen (formule B). Na substitueren en vereenvoudigen krijg je K = 3,6d + 6.",
      "antwoord": true,
      "uitleg": "Waar. <b>Stap 2 – substitueren:</b> Vervang m in K = 0,09m + 6 door de uitdrukking. K = 0,09(40d) + 6.<br><b>Stap 3 – haakjes wegwerken:</b> Hier zijn geen haakjes nodig: je vult maar één term in. Er valt niets weg te werken.<br><b>Stap 4 – vereenvoudigen:</b> Tel de getallen zonder letter bij elkaar op. K = 3,6d + 6.<br>💡 <i>Haakjes zijn alleen nodig bij een uitdrukking met meer termen of met een minteken; een enkele term zoals 3p hoeft niet.</i>"
    },
    {
      "type": "mc",
      "vraag": "Een tank bevat na t kwartier leegpompen V = 800 − 25t liter (formule A). Het aantal kwartieren is t = 4u + 1 na u uur (formule B). Stel door substitueren een formule op voor V in u. Welke formule krijg je?",
      "opties": [
        "V = −100u + 825",
        "V = −100u + 775",
        "V = −100u − 825",
        "V = 4u + 775"
      ],
      "antwoord": 1,
      "uitleg": "<b>Stap 2 – substitueren:</b> Vervang t in V = 800 − 25t door de hele uitdrukking tussen haakjes. V = 800 − 25(4u + 1).<br><b>Stap 3 – haakjes wegwerken:</b> Vermenigvuldig elke term binnen de haakjes met −25 (denk aan de tekens). V = 800 − 100u − 25.<br><b>Stap 4 – vereenvoudigen:</b> Tel de getallen zonder letter bij elkaar op. V = −100u + 775.<br>💡 <i>Let op de tekens: min maal min is plus, min maal plus is min.</i>"
    },
    {
      "type": "invul",
      "vraag": "Een verhuurbedrijf rekent met k − 3d = 60 voor het aantal kilometers k bij d dagen (formule B). De prijs in euro's is P = 40 + 0,5k (formule A). Herleid formule B tot k = (getal)d + (getal). Welk getal staat voor de d? ____",
      "antwoord": "3",
      "uitleg": "<b>Stap 1 – herleiden:</b> Maak k vrij met de balansmethode (trek de d-term aan beide kanten af). k − 3d = 60 → k = 3d + 60.<br><b>Stap 2 – substitueren:</b> Vervang k in P = 40 + 0,5k door de hele uitdrukking tussen haakjes. P = 40 + 0,5(3d + 60).<br><b>Stap 3 – haakjes wegwerken:</b> Vermenigvuldig elke term binnen de haakjes met 0,5 (denk aan de tekens). P = 40 + 1,5d + 30.<br><b>Stap 4 – vereenvoudigen:</b> Tel de getallen zonder letter bij elkaar op. P = 1,5d + 70.<br>💡 <i>Herleid eerst: deel bij de balansmethode ook het getal rechts door hetzelfde getal.</i>"
    },
    {
      "type": "invul",
      "vraag": "Op h meter hoogte is de temperatuur T = 20 − 0,006h graden Celsius (formule A). Een wandelaar is na k kwartier wandelen op hoogte h = 9k + 150 meter (formule B). Bereken T als k = 10. T = ____",
      "antwoord": "18,56|18.56",
      "uitleg": "Via de eindformule: T = −0,054k + 19,1 met k = 10 geeft T = 0,054 × 10 + 19,1 = 18,56. Controle in twee stappen: h = 240, dus T = 18,56.<br><b>Stap 2 – substitueren:</b> Vervang h in T = 20 − 0,006h door de hele uitdrukking tussen haakjes. T = 20 − 0,006(9k + 150).<br><b>Stap 3 – haakjes wegwerken:</b> Vermenigvuldig elke term binnen de haakjes met −0,006 (denk aan de tekens). T = 20 − 0,054k − 0,9.<br><b>Stap 4 – vereenvoudigen:</b> Tel de getallen zonder letter bij elkaar op. T = −0,054k + 19,1.<br>💡 <i>Let op de tekens: min maal min is plus, min maal plus is min.</i>"
    },
    {
      "type": "mc",
      "vraag": "Een appel weegt a gram en een banaan b gram. Een weegschaal in evenwicht geeft a + 2b = 240 (formule B). Een pakket met drie appels en verpakking weegt w = 3a + 50 gram (formule A). Herleid formule B zodat a wordt uitgedrukt in b. Welke formule krijg je?",
      "opties": [
        "a = −2b − 240",
        "a = 2b − 240",
        "a = −2b + 240",
        "a = 2b + 240"
      ],
      "antwoord": 2,
      "uitleg": "<b>Stap 1 – herleiden:</b> Maak a vrij met de balansmethode (trek de b-term aan beide kanten af). a + 2b = 240 → a = −2b + 240.<br><b>Stap 2 – substitueren:</b> Vervang a in w = 3a + 50 door de hele uitdrukking tussen haakjes. w = 3(−2b + 240) + 50.<br><b>Stap 3 – haakjes wegwerken:</b> Vermenigvuldig elke term binnen de haakjes met 3 (denk aan de tekens). w = −6b + 720 + 50.<br><b>Stap 4 – vereenvoudigen:</b> Tel de getallen zonder letter bij elkaar op. w = −6b + 770.<br>💡 <i>Herleid eerst: deel bij de balansmethode ook het getal rechts door hetzelfde getal.</i>"
    },
    {
      "type": "mc",
      "vraag": "Een taxirit van k kilometer kost p = 1,75k + 3 euro (formule A). De taxi rijdt in t minuten k = 0,6t kilometer (formule B). Stel door substitueren een formule op voor p in t. Welke formule krijg je?",
      "opties": [
        "p = 1,05t − 3",
        "p = −1,05t + 3",
        "p = 2,35t + 3",
        "p = 1,05t + 3"
      ],
      "antwoord": 3,
      "uitleg": "<b>Stap 2 – substitueren:</b> Vervang k in p = 1,75k + 3 door de uitdrukking. p = 1,75(0,6t) + 3.<br><b>Stap 3 – haakjes wegwerken:</b> Hier zijn geen haakjes nodig: je vult maar één term in. Er valt niets weg te werken.<br><b>Stap 4 – vereenvoudigen:</b> Tel de getallen zonder letter bij elkaar op. p = 1,05t + 3.<br>💡 <i>Haakjes zijn alleen nodig bij een uitdrukking met meer termen of met een minteken; een enkele term zoals 3p hoeft niet.</i>"
    },
    {
      "type": "invul",
      "vraag": "Een verhuurbedrijf rekent met k − 3d = 60 voor het aantal kilometers k bij d dagen (formule B). De prijs in euro's is P = 40 + 0,5k (formule A). Herleid, substitueer en vereenvoudig. De eindformule heeft de vorm P = (getal)d + (getal). Welk getal staat zonder letter (mét teken)? ____",
      "antwoord": "70",
      "uitleg": "<b>Stap 1 – herleiden:</b> Maak k vrij met de balansmethode (trek de d-term aan beide kanten af). k − 3d = 60 → k = 3d + 60.<br><b>Stap 2 – substitueren:</b> Vervang k in P = 40 + 0,5k door de hele uitdrukking tussen haakjes. P = 40 + 0,5(3d + 60).<br><b>Stap 3 – haakjes wegwerken:</b> Vermenigvuldig elke term binnen de haakjes met 0,5 (denk aan de tekens). P = 40 + 1,5d + 30.<br><b>Stap 4 – vereenvoudigen:</b> Tel de getallen zonder letter bij elkaar op. P = 1,5d + 70.<br>💡 <i>Herleid eerst: deel bij de balansmethode ook het getal rechts door hetzelfde getal.</i>"
    },
    {
      "type": "invul",
      "vraag": "Een tank bevat na t kwartier leegpompen V = 800 − 25t liter (formule A). Het aantal kwartieren is t = 4u + 1 na u uur (formule B). Bereken V als u = 3. V = ____",
      "antwoord": "475",
      "uitleg": "Via de eindformule: V = −100u + 775 met u = 3 geeft V = 100 × 3 + 775 = 475. Controle in twee stappen: t = 13, dus V = 475.<br><b>Stap 2 – substitueren:</b> Vervang t in V = 800 − 25t door de hele uitdrukking tussen haakjes. V = 800 − 25(4u + 1).<br><b>Stap 3 – haakjes wegwerken:</b> Vermenigvuldig elke term binnen de haakjes met −25 (denk aan de tekens). V = 800 − 100u − 25.<br><b>Stap 4 – vereenvoudigen:</b> Tel de getallen zonder letter bij elkaar op. V = −100u + 775.<br>💡 <i>Let op de tekens: min maal min is plus, min maal plus is min.</i>"
    },
    {
      "type": "waaronwaar",
      "vraag": "Een appel weegt a gram en een banaan b gram. Een weegschaal in evenwicht geeft a + 2b = 240 (formule B). Een pakket met drie appels en verpakking weegt w = 3a + 50 gram (formule A). Als je formule B herleidt, krijg je a = −2b − 240.",
      "antwoord": false,
      "uitleg": "Onwaar. De juiste herleiding is a = −2b + 240. Controle: a + 2b = 240 met b = 1 geeft a = 238.<br><b>Stap 1 – herleiden:</b> Maak a vrij met de balansmethode (trek de b-term aan beide kanten af). a + 2b = 240 → a = −2b + 240.<br><b>Stap 2 – substitueren:</b> Vervang a in w = 3a + 50 door de hele uitdrukking tussen haakjes. w = 3(−2b + 240) + 50.<br><b>Stap 3 – haakjes wegwerken:</b> Vermenigvuldig elke term binnen de haakjes met 3 (denk aan de tekens). w = −6b + 720 + 50.<br><b>Stap 4 – vereenvoudigen:</b> Tel de getallen zonder letter bij elkaar op. w = −6b + 770.<br>💡 <i>Herleid eerst: deel bij de balansmethode ook het getal rechts door hetzelfde getal.</i>"
    },
    {
      "type": "mc",
      "vraag": "Een bakker gebruikt per dag 2a + 3b = 24 kilo meel voor a broden en b taarten (formule B). De kosten in euro's zijn K = 8a + 20 (formule A). Herleid eerst formule B en stel daarna door substitueren een formule op voor K in b. Welke formule krijg je?",
      "opties": [
        "K = −12b − 116",
        "K = −12b + 116",
        "K = −12b + 32",
        "K = −1,5b + 116"
      ],
      "antwoord": 1,
      "uitleg": "<b>Stap 1 – herleiden:</b> Maak a vrij met de balansmethode (trek de b-term aan beide kanten af en deel alles door 2). 2a + 3b = 24 → 2a = −3b + 24, daarna delen door 2: a = −1,5b + 12.<br><b>Stap 2 – substitueren:</b> Vervang a in K = 8a + 20 door de hele uitdrukking tussen haakjes. K = 8(−1,5b + 12) + 20.<br><b>Stap 3 – haakjes wegwerken:</b> Vermenigvuldig elke term binnen de haakjes met 8 (denk aan de tekens). K = −12b + 96 + 20.<br><b>Stap 4 – vereenvoudigen:</b> Tel de getallen zonder letter bij elkaar op. K = −12b + 116.<br>💡 <i>Herleid eerst: deel bij de balansmethode ook het getal rechts door hetzelfde getal.</i>"
    },
    {
      "type": "open",
      "vraag": "In een opgave heb je 2a + 3b = 24 en K = 8a + 20. Wat moet je eerst doen voordat je kunt substitueren, en waarom?",
      "sleutelwoorden": [
        "herleid/herleiden/omschrijven/omvormen/herschrijven/balansmethode",
        "vrij/alleen/apart/links/uitdrukken in/isoleren"
      ],
      "minTreffers": 2,
      "modelantwoord": "Eerst formule 2a + 3b = 24 herleiden tot a = −1,5b + 12, zodat a alleen staat (uitgedrukt in b). Dan kun je die uitdrukking voor a in K = 8a + 20 invullen.",
      "uitleg": "Je substitueert een formule van de vorm a = …. Daarom herleid je eerst met de balansmethode: a = −1,5b + 12. Daarna K = 8(−1,5b + 12) + 20 = −12b + 116."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een verhuurbedrijf rekent met k − 3d = 60 voor het aantal kilometers k bij d dagen (formule B). De prijs in euro's is P = 40 + 0,5k (formule A). Na herleiden, substitueren en vereenvoudigen krijg je P = 1,5d + 100.",
      "antwoord": false,
      "uitleg": "Onwaar. De juiste eindformule is P = 1,5d + 70; P = 1,5d + 100 bevat een rekenfout.<br><b>Stap 1 – herleiden:</b> Maak k vrij met de balansmethode (trek de d-term aan beide kanten af). k − 3d = 60 → k = 3d + 60.<br><b>Stap 2 – substitueren:</b> Vervang k in P = 40 + 0,5k door de hele uitdrukking tussen haakjes. P = 40 + 0,5(3d + 60).<br><b>Stap 3 – haakjes wegwerken:</b> Vermenigvuldig elke term binnen de haakjes met 0,5 (denk aan de tekens). P = 40 + 1,5d + 30.<br><b>Stap 4 – vereenvoudigen:</b> Tel de getallen zonder letter bij elkaar op. P = 1,5d + 70.<br>💡 <i>Herleid eerst: deel bij de balansmethode ook het getal rechts door hetzelfde getal.</i>"
    },
    {
      "type": "mc",
      "vraag": "Een appel weegt a gram en een banaan b gram. Een weegschaal in evenwicht geeft a + 2b = 240 (formule B). Een pakket met drie appels en verpakking weegt w = 3a + 50 gram (formule A). Herleid eerst formule B en stel daarna door substitueren een formule op voor w in b. Welke formule krijg je?",
      "opties": [
        "w = −2b + 770",
        "w = −6b + 290",
        "w = −6b + 670",
        "w = −6b + 770"
      ],
      "antwoord": 3,
      "uitleg": "<b>Stap 1 – herleiden:</b> Maak a vrij met de balansmethode (trek de b-term aan beide kanten af). a + 2b = 240 → a = −2b + 240.<br><b>Stap 2 – substitueren:</b> Vervang a in w = 3a + 50 door de hele uitdrukking tussen haakjes. w = 3(−2b + 240) + 50.<br><b>Stap 3 – haakjes wegwerken:</b> Vermenigvuldig elke term binnen de haakjes met 3 (denk aan de tekens). w = −6b + 720 + 50.<br><b>Stap 4 – vereenvoudigen:</b> Tel de getallen zonder letter bij elkaar op. w = −6b + 770.<br>💡 <i>Herleid eerst: deel bij de balansmethode ook het getal rechts door hetzelfde getal.</i>"
    },
    {
      "type": "open",
      "vraag": "Een fabrikant heeft een formule voor de kosten in apparaten en een formule voor het aantal apparaten in weken. Waarom is een formule die de kosten rechtstreeks in weken geeft handig?",
      "sleutelwoorden": [
        "tussenstap/tussenresultaat/tussenantwoord/eerst",
        "in één keer/één formule/één stap/direct/meteen/hoeft niet"
      ],
      "minTreffers": 1,
      "modelantwoord": "Je hoeft niet eerst het aantal apparaten uit te rekenen. Je vult het aantal weken in één keer in en krijgt direct de kosten.",
      "uitleg": "Door te substitueren gebruik je één formule: k = 2400t + 900. Je slaat de tussenstap (eerst a berekenen) over."
    }
  ]
});

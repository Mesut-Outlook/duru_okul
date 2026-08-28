/* Proeftoets 25 — Natuurkunde HAVO 3: Hoofdstuk 8 (Krachten gebruiken - Integrale Eindtoets)
   Focus: Volledig Hoofdstuk 8 (§8.1 t/m §8.5) — Integrale toets over hefbomen, momenten, overbrengingen, druk en hydraulica.
   20 vragen conform DURU ENGINE_SPEC. */
DURU.registerExamen({
  id: "ex-h3-natuurkunde-25",
  titel: "Toets 25 — Integrale Eindtoets Hoofdstuk 8 (Krachten gebruiken)",
  vak: "Natuurkunde · HAVO 3 (H8)",
  icoon: "🏆",
  duurMin: 35,
  vragen: [
    {
      type: "mc",
      vraag: "Wat is het moment van een kracht van 60 N die loodrecht aangrijpt op een hefboomarm van 35 cm?",
      opties: [
        "21 Nm",
        "2100 Nm",
        "1,71 Nm",
        "171 Nm"
      ],
      antwoord: 0,
      uitleg: "35 cm = 0,35 m. M = F × r = 60 N × 0,35 m = 21 Nm."
    },
    {
      type: "mc",
      vraag: "Welk type hefboom is een <b>notenkraker</b>?",
      opties: [
        "Een dubbelzijdige hefboom",
        "Een enkelzijdige hefboom (het scharnier zit aan het uiteinde en de noot zit tussen scharnier en hand)",
        "Een hydraulische hefboom",
        "Een vaste katrol"
      ],
      antwoord: 1,
      uitleg: "Scharnier aan uiteinde, last in het midden, spierkracht aan andere uiteinde = enkelzijdige hefboom."
    },
    {
      type: "invul",
      vraag: "Een hijskraan tilt een vrachtcontainer van 24.000 N op met behulp van een takel met 4 dragende kabels. Welke trekkracht in Newton moet de lierkabel minimaal leveren?",
      antwoord: "6000|6000 N|6.000|6.000 N",
      uitleg: "F_lier = 24.000 N / 4 = 6000 N."
    },
    {
      type: "mc",
      vraag: "Een aquarium met bodemoppervlakte van 0,40 m² weegt gevuld met water 800 N. Hoe groot is de druk van het aquarium op het meubel in Pascal?",
      opties: [
        "800 Pa",
        "320 Pa",
        "2000 Pa",
        "200 Pa"
      ],
      antwoord: 2,
      uitleg: "p = F / A = 800 N / 0,40 m² = 2000 Pa."
    },
    {
      type: "waaronwaar",
      vraag: "Als je een spijker in een houten plank slaat, zorgt de scherpe punt voor een extreem hoge druk waardoor de houtvezels makkelijk wijken.",
      antwoord: true,
      uitleg: "Waar. Zeer klein oppervlak A -> zeer hoge druk p."
    },
    {
      type: "invul",
      vraag: "In een tandwielkast drijft een tandwiel met 18 tanden een tandwiel met 54 tanden aan. Hoeveel omwentelingen maakt het kleine tandwiel als het grote tandwiel 5 omwentelingen maakt?",
      antwoord: "15|15 omwentelingen",
      uitleg: "Verhouding = 54 / 18 = 3. Het kleine tandwiel draait 3× zo snel: 5 × 3 = 15 omwentelingen."
    },
    {
      type: "mc",
      vraag: "Wat is de arm van een kracht als de krachtlijn schuin onder een hoek van 30° op een staaf van 2,0 m lengte staat?",
      opties: [
        "0 m",
        "Altijd 2,0 m",
        "4,0 m",
        "De loodrechte afstand van het draaipunt tot de stippellijn van de kracht (r = 2,0 × sin(30°) = 1,0 m)"
      ],
      antwoord: 3,
      uitleg: "De arm is altijd de loodrechte afstand van het draaipunt tot de werklijn."
    },
    {
      type: "invul",
      vraag: "Op een wipwap zit Thomas ( = 450\text{ N}$) op 1,6 m van het draaipunt. Aan de andere kant zit Lisa op 2,0 m van het draaipunt in evenwicht. Hoe zwaar is Lisa in Newton?",
      antwoord: "360|360 N",
      uitleg: "F₂ = (450 N × 1,6 m) / 2,0 m = 720 / 2,0 = 360 N."
    },
    {
      type: "waaronwaar",
      vraag: "Bij een vaste katrol hoef je slechts de helft van de touwlengte binnen te halen vergeleken met de hoogte waarover de last stijgt.",
      antwoord: false,
      uitleg: "Niet waar. Een vaste katrol verandert alleen de richting; s_touw is exact gelijk aan s_last (geen afstandswinst en geen krachtwinst).",
      uitleg: "Waar. Een vaste katrol verandert alleen de richting, niet de kracht en niet de afstand."
    },
    {
      type: "mc",
      vraag: "Welke wet ligt ten grondslag aan de werking van een hydraulische graafmachinearm?",
      opties: [
        "De Wet van Pascal (druk in een afgesloten vloeistof plant zich in alle richtingen gelijk voort)",
        "De Wet van Ohm",
        "De Wet van Archimedes",
        "De Wet van behoud van massa van Lavoisier"
      ],
      antwoord: 0,
      uitleg: "Pascal: p = F₁/A₁ = F₂/A₂."
    },
    {
      type: "invul",
      vraag: "Een hydraulische pers heeft zuigers met oppervlakten van 5 cm² en 150 cm² (verhouding 1 : 30). Met welke spierkracht in Newton moet je op de kleine zuiger duwen om een auto van 15.000 N op te tillen?",
      antwoord: "500|500 N",
      uitleg: "F₁ = F₂ / 30 = 15.000 N / 30 = 500 N."
    },
    {
      type: "waaronwaar",
      vraag: "Volgens de Gouden Regel van de Mechanica kun je met een machine wel kracht besparen, maar nooit arbeid (energie) besparen.",
      antwoord: true,
      uitleg: "Waar. Wat je wint aan kracht moet je altijd inleveren aan weg/afstand (W = F × s)."
    },
    {
      type: "mc",
      vraag: "Waarom zijn de banden van een racefiets heel smal en worden ze op zeer hoge druk (bijv. 8 bar) gepompt?",
      opties: [
        "Om de fiets zwaarder te maken",
        "Om het contactoppervlak met het asfalt zo klein mogelijk te maken, waardoor de rolweerstand minimaal is",
        "Zodat de banden niet nat worden",
        "Om meer grip in mul zand te hebben"
      ],
      antwoord: 1,
      uitleg: "Kleine contactvlek en hoge druk verminderen de vervorming van de band en verlagen de rolweerstand drastisch."
    },
    {
      type: "invul",
      vraag: "Reken om: een druk van 0,75 N/cm² is gelijk aan hoeveel Pascal (Pa)?",
      antwoord: "7500|7500 Pa|7.500|7.500 Pa",
      uitleg: "0,75 × 10.000 = 7500 Pa."
    },
    {
      type: "mc",
      vraag: "Waar bevindt zich het zwaartepunt van een massieve, homogene houten kubus?",
      opties: [
        "In de bovenste hoek",
        "Op het grondvlak",
        "Precies in het geometrische middelpunt van de kubus",
        "Aan de zijkant"
      ],
      antwoord: 2,
      uitleg: "Bij een symmetrisch homogeen lichaam ligt het zwaartepunt in het centrum."
    },
    {
      type: "waaronwaar",
      vraag: "Een schroevendraaier met een dunner handvat levert bij dezelfde handkracht een groter draaimoment dan een met een dik handvat.",
      antwoord: false,
      uitleg: "Niet waar. Een dikker handvat heeft een grotere straal (arm r), waardoor het moment M = F × r juist groter is.",
      uitleg: "Waar. De straal (arm r) van het dikke handvat is groter, waardoor M = F × r toeneemt."
    },
    {
      type: "invul",
      vraag: "Een kracht van 250 N oefent een moment van 75 Nm uit op een hefboom. Hoe groot is de arm van deze kracht in meter?",
      antwoord: "0,3|0,3 m|0,30|0,30 m",
      uitleg: "r = M / F = 75 Nm / 250 N = 0,30 m (30 cm)."
    },
    {
      type: "mc",
      vraag: "Wat is het effect van een losse katrol op de richting van de trekkracht?",
      opties: [
        "Er is geen touw nodig",
        "Je trekt altijd omlaag",
        "De richting verandert horizontaal",
        "Je moet in dezelfde richting trekken als de beweging van de last (omhoog trekken om de last omhoog te krijgen)"
      ],
      antwoord: 3,
      uitleg: "Bij een losse katrol trek je aan het touweinde omhoog, terwijl de last ook omhoog beweegt."
    },
    {
      type: "open",
      vraag: "Vergelijk een <b>vaste katrol</b>, een <b>losse katrol</b> en een <b>takel met 4 touwen</b> op het gebied van: 1) de benodigde spierkracht om een last van 800 N op te tillen, 2) de benodigde touwlengte om de last 1,0 m op te tillen.",
      sleutelwoorden: ["800", "400", "200"],
      minTreffers: 3,
      modelantwoord: "1. Vaste katrol: - Spierkracht:  = 800\text{ N}$ (geen krachtwinst, alleen richtingsverandering). - Touwlengte:  = 1{,}0\text{ m}$. 2. Losse katrol (2 dragende touwdelen): - Spierkracht:  = 800 / 2 = 400\text{ N}$ (kracht gehalveerd). - Touwlengte:  = 2 \times 1{,}0 = 2{,}0\text{ m}$. 3. Takel met 4 touwdelen: - Spierkracht:  = 800 / 4 = 200\text{ N}$ (kracht 4× kleiner). - Touwlengte:  = 4 \times 1{,}0 = 4{,}0\text{ m}$.",
      uitleg: "Vergelijking van hefwerktuigen."
    },
    {
      type: "open",
      vraag: "Een olifant van 36.000 N staat op 4 poten (elk 50\text{ cm}^2$). Een circusartieste van 540 N balanceert op de punt van één stilettohak (bash{,}30\text{ cm}^2$). Bereken voor beide de druk in N/cm² en leg uit wie van de twee de grootste kans heeft om een houten parketvloer te beschadigen (deukjes te maken).",
      sleutelwoorden: ["20", "1800", "artieste/stiletto"],
      minTreffers: 3,
      modelantwoord: "Berekening olifant: - Totaal oppervlak =  \times 450 = 1800\text{ cm}^2$. - Druk =  / A = 36.000\text{ N} / 1800\text{ cm}^2 = 20\text{ N/cm}^2$. Berekening artieste op stilettohak: - Oppervlak = bash{,}30\text{ cm}^2$. - Druk =  / A = 540\text{ N} / 0{,}30\text{ cm}^2 = 1800\text{ N/cm}^2$. Conclusie: De druk onder de stilettohak (800\text{ N/cm}^2$) is maar liefst 90 keer zo groot als de druk onder de poten van de olifant (0\text{ N/cm}^2$). De artieste op de stilettohak zal dus veel eerder deukjes en putjes in het houten parket drukken.",
      uitleg: "Drukvergelijking tussen grote kracht / groot oppervlak en kleine kracht / miniem oppervlak."
    }
  ]
});

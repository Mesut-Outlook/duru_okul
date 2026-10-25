/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Toets 61 — §1.4 Veiligheid, Remweg & Stopafstand — Toets A
   Gebaseerd op Overal Natuurkunde 3 HAVO (Hoofdstuk 1 Kracht en beweging)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-h3-natuurkunde-61",
  "hoofdstuk": 1,
  "paragraaf": "1.4",
  "titel": "Toets 61 — §1.4 Veiligheid, Remweg & Stopafstand — Toets A",
  "vak": "Natuurkunde · HAVO 3 (H1)",
  "icoon": "🚗",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat wordt in de natuurkunde precies verstaan onder de <b>reactietijd</b> van een bestuurder?",
      "opties": [
        "De totale tijd die nodig is om een voertuig vanaf topsnelheid stil te zetten",
        "De tijdsduur tussen het zien van het gevaar en het intrappen van het rempedaal",
        "De tijd waarin de remmen van het voertuig maximale remkracht uitoefenen",
        "De tijd waarin het voertuig een eenparig vertraagde beweging uitvoert"
      ],
      "antwoord": 1,
      "uitleg": "De reactietijd is de tijd tussen het waarnemen van een onverwachte gebeurtenis en het daadwerkelijk beginnen met remmen."
    },
    {
      "type": "mc",
      "vraag": "Een auto rijdt met een snelheid van 72 km/h. Wat is deze snelheid uitgedrukt in meter per seconde (m/s)?",
      "opties": [
        "25 m/s",
        "15 m/s",
        "7,2 m/s",
        "20 m/s"
      ],
      "antwoord": 3,
      "uitleg": "Om te rekenen van km/h naar m/s deel je de snelheid door 3,6: 72 / 3,6 = 20 m/s."
    },
    {
      "type": "mc",
      "vraag": "Welke bewegingssoort voert een auto uit tijdens de <b>reactietijd</b> vóórdat de bestuurder remt?",
      "opties": [
        "Een eenparige beweging met constante snelheid",
        "Een eenparig versnelde beweging met constante versnelling",
        "Een eenparig vertraagde beweging doordat het gas wordt losgelaten",
        "Een willekeurige beweging met afnemende kinetische energie"
      ],
      "antwoord": 0,
      "uitleg": "Tijdens de reactietijd raakt de bestuurder de remmen nog niet aan, waardoor de auto met onverminderde, constante snelheid doorrijdt."
    },
    {
      "type": "mc",
      "vraag": "Wat gebeurt er met de <b>remweg</b> van een auto als de rijsnelheid verdubbelt (van v naar 2v)?",
      "opties": [
        "De remweg verdubbelt eveneens",
        "De remweg blijft exact gelijk",
        "De remweg wordt vier keer zo lang",
        "De remweg wordt drie keer zo lang"
      ],
      "antwoord": 2,
      "uitleg": "De remweg is evenredig met het kwadraat van de snelheid: (2)² = 4 keer zo lang."
    },
    {
      "type": "mc",
      "vraag": "Uit welke twee afstanden is de totale <b>stopafstand</b> van een auto opgebouwd?",
      "opties": [
        "De reactieafstand opgeteld bij de remweg",
        "De remweg verminderd met de kreukelzone-afstand",
        "De remweg vermenigvuldigd met de reactietijd",
        "De reactieafstand gedeeld door de remtijd"
      ],
      "antwoord": 0,
      "uitleg": "De stopafstand is de totale afstand vanaf het moment van zien tot volledige stilstand: s_stop = s_reactie + s_rem."
    },
    {
      "type": "mc",
      "vraag": "Welke factor heeft <b>geen enkele directe invloed</b> op de lengte van de remweg van een auto?",
      "opties": [
        "De toestand van het wegdek (droog asfalt of natte klinkers)",
        "De profieldiepte en spanning van de autobanden",
        "De massa van de auto inclusief bagage en passagiers",
        "Het vasthouden van een smartphone door de bestuurder"
      ],
      "antwoord": 3,
      "uitleg": "Afleiding door een telefoon vergroot de reactietijd en reactieafstand, maar verandert niets aan de technische remweg van het voertuig zelf."
    },
    {
      "type": "mc",
      "vraag": "Wat is het belangrijkste natuurkundige doel van een <b>kreukelzone</b> aan de voorzijde van een moderne auto?",
      "opties": [
        "De massa van de auto aanzienlijk vergroten tijdens een botsing",
        "De botstijd (Δt) verlengen waardoor de resulterende botskracht op de inzittenden afneemt",
        "De auto na de botsing sneller in tegengestelde richting terug laten veren",
        "De zwaartekracht op de auto ombuigen naar een voorwaartse stuwkracht"
      ],
      "antwoord": 1,
      "uitleg": "Door gecontroleerd te vervormen verlengt de kreukelzone de botstijd. Volgens F = m · Δv / Δt wordt de uitgeoefende kracht daardoor veel kleiner."
    },
    {
      "type": "mc",
      "vraag": "Een auto rijdt met 10 m/s en remt eenparig af tot stilstand in 4,0 seconden. Hoe groot is de gemiddelde snelheid tijdens het remmen?",
      "opties": [
        "10 m/s",
        "2,5 m/s",
        "5,0 m/s",
        "0 m/s"
      ],
      "antwoord": 2,
      "uitleg": "Bij een eenparig vertraagde beweging tot stilstand is de gemiddelde snelheid: v_gem = (v_begin + v_eind) / 2 = (10 + 0) / 2 = 5,0 m/s."
    },
    {
      "type": "mc",
      "vraag": "Een automobilist rijdt met 15 m/s. Zijn reactietijd bedraagt 0,80 seconde. Hoeveel meter legt hij af tijdens zijn reactietijd?",
      "opties": [
        "18,75 meter",
        "15 meter",
        "9,6 meter",
        "12 meter"
      ],
      "antwoord": 3,
      "uitleg": "De reactieafstand bereken je met s_reactie = v · t_r = 15 m/s · 0,80 s = 12 m."
    },
    {
      "type": "mc",
      "vraag": "Waarom mag de <b>veiligheidskooi</b> (het passagierscompartiment) van een auto juist <b>niet</b> vervormen of kreukelen?",
      "opties": [
        "Om de overlevingsruimte voor de inzittenden te behouden en beknelling te voorkomen",
        "Omdat de deuren anders niet meer met de autosleutel geopend kunnen worden",
        "Omdat een stijve kooi ervoor zorgt dat de airbags sneller kunnen leeglopen",
        "Om te voorkomen dat de autoruit beslaat door temperatuurverschillen"
      ],
      "antwoord": 0,
      "uitleg": "De veiligheidskooi moet extreem sterk en vormvast zijn zodat de inzittenden niet worden geplet en beschermd blijven tegen binnendringende onderdelen."
    },
    {
      "type": "mc",
      "vraag": "Een bromfietser rijdt met 36 km/h (10 m/s) en heeft een remweg van 6,0 meter. Wat wordt de remweg als hij zijn snelheid opvoert naar 72 km/h (20 m/s)?",
      "opties": [
        "12 meter",
        "18 meter",
        "24 meter",
        "36 meter"
      ],
      "antwoord": 2,
      "uitleg": "De snelheid verdubbelt (van 10 naar 20 m/s). De remweg schaalt kwadratisch: (2)² = 4 keer zo groot. Dus 6,0 m · 4 = 24 m."
    },
    {
      "type": "mc",
      "vraag": "Hoe helpt het elastisch meerekken van een veiligheidsgordel bij een frontale aanrijding?",
      "opties": [
        "Het zorgt ervoor dat de passagier direct naar de achterbank schuift",
        "Het verlengt de afremweg van het lichaam waardoor de piekbelasting daalt",
        "Het vermindert het totale gewicht van de passagier tijdens de klap",
        "Het activeert automatisch het antiblokkeersysteem (ABS) van de wielen"
      ],
      "antwoord": 1,
      "uitleg": "Doordat de gordel gecontroleerd een klein stukje meerekt, wordt de afremtijd van het lichaam verlengd en de piekkracht op de borstkas aanzienlijk verlaagd."
    },
    {
      "type": "waaronwaar",
      "vraag": "Op een nat of beijzeld wegdek is de remweg van een auto aanzienlijk langer doordat de maximale wrijvingskracht tussen banden en wegdek veel kleiner is.",
      "antwoord": true,
      "uitleg": "Waar: Gladheid vermindert de wrijving drastisch, waardoor de wielen minder remkracht kunnen leveren en de remweg fors toeneemt."
    },
    {
      "type": "waaronwaar",
      "vraag": "Wanneer een bestuurder vermoeid is of alcohol heeft gedronken, wordt zijn remweg langer.",
      "antwoord": false,
      "uitleg": "Onwaar: Alcohol en vermoeidheid verlengen de reactietijd en reactieafstand, maar hebben geen invloed op de mechanische remweg van de auto."
    },
    {
      "type": "waaronwaar",
      "vraag": "De binnenkant van een fietshelm bevat een harde schuimlaag (EPS) die bij een val blijvend indeukt om de botstijd van het hoofd te verlengen.",
      "antwoord": true,
      "uitleg": "Waar: Het samendrukken van het schuim absorbeert energie en verlengt de vertragingstijd, waardoor gevaarlijke piekversnellingen van de hersenen worden voorkomen."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als een auto een noodstop maakt met constante vertraging, is de remtijd omgekeerd evenredig met de beginsnelheid.",
      "antwoord": false,
      "uitleg": "Onwaar: Bij constante remkracht en vertraging is de remtijd juist recht evenredig met de beginsnelheid: twee keer zo snel betekent twee keer zo lang remmen."
    },
    {
      "type": "invul",
      "vraag": "Een scooter rijdt met een snelheid van 12 m/s. De bestuurder heeft een reactietijd van 0,75 s. Hoeveel meter bedraagt de reactieafstand?",
      "antwoord": "9|9 m|9 meter",
      "uitleg": "s_reactie = v · t_r = 12 m/s · 0,75 s = 9 meter."
    },
    {
      "type": "invul",
      "vraag": "Een auto heeft bij een noodstop een reactieafstand van 14 meter en een remweg van 26 meter. Wat is de totale stopafstand in meters?",
      "antwoord": "40|40 m|40 meter",
      "uitleg": "s_stop = s_reactie + s_rem = 14 m + 26 m = 40 meter."
    },
    {
      "type": "open",
      "vraag": "Leg uit waarom de remweg van een auto vier keer zo lang wordt als de rijsnelheid slechts twee keer zo hoog is.",
      "modelantwoord": "De bewegingsenergie (kinetische energie) van een voorwerp hangt kwadratisch af van de snelheid (E_k = 0,5 · m · v²). Bij een dubbele snelheid heeft de auto vier keer zoveel energie die door de remmen moet worden weggewerkt. Omdat de maximale remkracht gelijk blijft en arbeid W = F · s is, moet de afstand (de remweg) vier keer zo groot worden.",
      "minTreffers": 1,
      "sleutelwoorden": [
        "kwadratisch/kwadraat",
        "kinetische energie/bewegingsenergie"
      ],
      "uitleg": "De kinetische energie hangt af van het kwadraat van de snelheid; om 4× zoveel bewegingsenergie met gelijke remkracht om te zetten is 4× zoveel remafstand nodig."
    },
    {
      "type": "open",
      "vraag": "Benoem twee voorzieningen in een auto die ervoor zorgen dat de vertragingstijd tijdens een botsing wordt verlengd.",
      "modelantwoord": "1. De kreukelzone (die gecontroleerd indeukt).\n2. De veiligheidsgordel (die gecontroleerd meeveert/uitrekt) of de airbag.",
      "minTreffers": 2,
      "sleutelwoorden": [
        "kreukelzone/kreukel",
        "veiligheidsgordel/gordel/airbag"
      ],
      "uitleg": "Zowel de kreukelzone aan de carrosserie als de veiligheidsgordels en airbags zorgen voor een langere botstijd Δt waardoor de piekbelasting F daalt."
    }
  ]
});

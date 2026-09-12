/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Toets 29 — Toets 29 — §1.2 Soorten beweging & Diagrammen — Toets A
   Gebaseerd op Overal Natuurkunde 3 HAVO (Hoofdstuk 1 Kracht en beweging)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-h3-natuurkunde-29",
  "hoofdstuk": 1,
  "paragraaf": "1.2",
  "titel": "Toets 29 — §1.2 Soorten beweging & Diagrammen — Toets A",
  "vak": "Natuurkunde · HAVO 3 (H1)",
  "icoon": "📈",
  "duurMin": 30,
  "vragen": [
    {
        "type": "mc",
        "vraag": "Met welke formule bereken je de gemiddelde snelheid (vgem) als de afstand s en de tijdsduur t bekend zijn?",
        "opties": [
            "vgem = s / t",
            "vgem = s · t",
            "vgem = t / s",
            "vgem = 1/2 · s · t²"
        ],
        "antwoord": 0,
        "uitleg": "De gemiddelde snelheid is de afstand gedeeld door de tijd: vgem = s / t (blz. 14 in het theorieboek)."
    },
    {
        "type": "mc",
        "vraag": "Hoe reken je een snelheid van kilometer per uur (km/h) correct om naar meter per seconde (m/s)?",
        "opties": [
            "Vermenigvuldigen met 3,6",
            "Delen door 3,6",
            "Vermenigvuldigen met 1000",
            "Delen door 60"
        ],
        "antwoord": 1,
        "uitleg": "Omdat 1 km = 1000 m en 1 uur = 3600 s, geldt: 3600 / 1000 = 3,6. Van km/h naar m/s moet je dus altijd delen door 3,6."
    },
    {
        "type": "mc",
        "vraag": "Een auto rijdt met 72 km/h over een provinciale weg. Hoeveel meter legt deze auto per seconde af?",
        "opties": [
            "7,2 m/s",
            "259,2 m/s",
            "20 m/s",
            "25 m/s"
        ],
        "antwoord": 2,
        "uitleg": "72 km/h omrekenen naar m/s: 72 / 3,6 = 20 m/s (zie opdracht 23a)."
    },
    {
        "type": "mc",
        "vraag": "Wat betekent de steilheid (helling) van de grafiek in een (s,t)-diagram?",
        "opties": [
            "De totale massa van het voertuig",
            "De resulterende tegenwerkende kracht",
            "De verstreken tijd tot aan de finish",
            "De snelheid van het voorwerp op dat moment"
        ],
        "antwoord": 3,
        "uitleg": "In een (s,t)-diagram geldt: hoe steiler de lijn loopt, des te meer meters er per seconde worden afgelegd. De steilheid stelt dus de snelheid voor (blz. 14)."
    },
    {
        "type": "mc",
        "vraag": "Het Formule 1-circuit van Zandvoort is 4259 m lang. Max Verstappen rijdt een ronde in 1 minuut en 20,4 seconden (80,4 s). Wat is zijn gemiddelde snelheid?",
        "opties": [
            "53,0 m/s (ongeveer 191 km/h)",
            "34,2 m/s (ongeveer 123 km/h)",
            "80,4 m/s (ongeveer 289 km/h)",
            "12,5 m/s (ongeveer 45 km/h)"
        ],
        "antwoord": 0,
        "uitleg": "vgem = s / t = 4259 m / 80,4 s = 52,97 m/s ≈ 53,0 m/s (voorbeeld in theorieboek op blz. 14)."
    },
    {
        "type": "mc",
        "vraag": "Hoe herken je stilstand in een (s,t)-diagram?",
        "opties": [
            "Een stijgende rechte lijn vanuit de oorsprong",
            "Een horizontale rechte lijn (de afstand s verandert niet)",
            "Een dalende rechte lijn naar de tijdas",
            "Een kromme lijn die steeds steiler wordt"
        ],
        "antwoord": 1,
        "uitleg": "Als de afstand s gedurende een tijdinterval gelijk blijft (horizontale lijn), beweegt het voorwerp niet: het staat stil (snelheid v = 0)."
    },
    {
        "type": "mc",
        "vraag": "Wat stelt de oppervlakte onder de grafiek in een (v,t)-diagram voor?",
        "opties": [
            "De gemiddelde versnelling in m/s²",
            "De benodigde motorkracht in newton",
            "De afgelegde afstand (s) in meters",
            "Het brandstofverbruik in liters"
        ],
        "antwoord": 2,
        "uitleg": "Omdat snelheid × tijd = afstand (m/s × s = m), stelt de oppervlakte onder de grafiek in een (v,t)-diagram precies de afgelegde afstand s voor (blz. 15)."
    },
    {
        "type": "mc",
        "vraag": "Een scooter rijdt gedurende 8,0 seconden met een constante snelheid van 6,0 m/s. Hoeveel afstand legt de scooter af?",
        "opties": [
            "14 m",
            "24 m",
            "1,33 m",
            "48 m"
        ],
        "antwoord": 3,
        "uitleg": "Bij constante snelheid bereken je de oppervlakte van de rechthoek: s = v · t = 6,0 m/s × 8,0 s = 48 m."
    },
    {
        "type": "mc",
        "vraag": "Een fietser versnelt eenparig vanuit stilstand (0 m/s) in 6,0 seconden naar een eindsnelheid van 8,0 m/s. Hoe bereken je de afgelegde afstand met de oppervlaktemethode?",
        "opties": [
            "Oppervlakte driehoek = 1/2 × basis × hoogte = 1/2 × 6,0 × 8,0 = 24 m",
            "Oppervlakte rechthoek = 6,0 × 8,0 = 48 m",
            "Afstand = eindsnelheid / tijd = 8,0 / 6,0 = 1,33 m",
            "Afstand = 6,0 + 8,0 = 14 m"
        ],
        "antwoord": 0,
        "uitleg": "Bij eenparige versnelling vanuit stilstand vormt de grafiek een driehoek met basis t = 6,0 s en hoogte v = 8,0 m/s: s = 1/2 × 6,0 × 8,0 = 24 m (of s = vgem · t = 4,0 × 6,0 = 24 m)."
    },
    {
        "type": "mc",
        "vraag": "Wat is sneller: een fietser die 10 m/s rijdt of een brommer die 30 km/h rijdt?",
        "opties": [
            "De brommer met 30 km/h is sneller",
            "De fietser met 10 m/s is sneller (want 10 m/s = 36 km/h)",
            "Ze gaan precies even snel",
            "Dat kun je niet vergelijken omdat de eenheden anders zijn"
        ],
        "antwoord": 1,
        "uitleg": "10 m/s omrekenen naar km/h: 10 × 3,6 = 36 km/h. 36 km/h is sneller dan 30 km/h (zie opdracht 21 uit het boek)."
    },
    {
        "type": "mc",
        "vraag": "Welke eenheid hoort bij de grootheid versnelling (a)?",
        "opties": [
            "Meter per seconde (m/s)",
            "Newton per kilogram (N/kg)",
            "Meter per seconde kwadraat (m/s²)",
            "Kilometer per uur (km/h)"
        ],
        "antwoord": 2,
        "uitleg": "Versnelling geeft aan hoeveel m/s de snelheid per seconde verandert: (m/s) / s = m/s² (blz. 16)."
    },
    {
        "type": "mc",
        "vraag": "Een hardloper rent 1500 m in 5 minuten (300 s). Wat is zijn gemiddelde snelheid in m/s?",
        "opties": [
            "300 m/s",
            "10 m/s",
            "3 m/s",
            "5 m/s"
        ],
        "antwoord": 3,
        "uitleg": "vgem = s / t = 1500 m / 300 s = 5,0 m/s."
    },
    {
        "type": "waaronwaar",
        "vraag": "In een (s,t)-diagram stelt een schuine rechte lijn een beweging met constante snelheid voor.",
        "antwoord": true,
        "uitleg": "Waar. Omdat de steilheid constant is, legt het voorwerp in elk gelijk tijdsinterval evenveel meters af."
    },
    {
        "type": "waaronwaar",
        "vraag": "De oppervlakte onder een (v,t)-diagram is gelijk aan de afgelegde afstand s.",
        "antwoord": true,
        "uitleg": "Waar. Dit is een fundamentele rekenregel in de natuurkunde: oppervlakte onder (v,t) = afstand."
    },
    {
        "type": "waaronwaar",
        "vraag": "Om van m/s naar km/h om te rekenen, moet je de waarde delen door 3,6.",
        "antwoord": false,
        "uitleg": "Onwaar. Van m/s naar km/h moet je vermenigvuldigen met 3,6 (bijvoorbeeld 10 m/s × 3,6 = 36 km/h)."
    },
    {
        "type": "waaronwaar",
        "vraag": "Een horizontale lijn in een (s,t)-diagram betekent dat het voorwerp met constante snelheid doorrijdt.",
        "antwoord": false,
        "uitleg": "Onwaar. In een (s,t)-diagram betekent een horizontale lijn dat de afstand niet verandert: het voorwerp staat stil."
    },
    {
        "type": "invul",
        "vraag": "Reken om: een snelheid van 54 km/h is gelijk aan ... m/s.",
        "antwoord": "15",
        "uitleg": "54 / 3,6 = 15 m/s."
    },
    {
        "type": "invul",
        "vraag": "Een auto rijdt 4,0 seconden met een constante snelheid van 25 m/s. De afgelegde afstand is ... meter.",
        "antwoord": "100",
        "uitleg": "s = v · t = 25 m/s × 4,0 s = 100 m."
    },
    {
        "type": "open",
        "vraag": "Leg uit waarom de omrekenfactor tussen meter per seconde en kilometer per uur precies 3,6 is.",
        "sleutelwoorden": [
            "1000 meter",
            "3600 seconden",
            "delen/verhouding"
        ],
        "minTreffers": 2,
        "modelantwoord": "In één kilometer zit 1000 meter en in één uur zitten 3600 seconden. De verhouding is 3600 / 1000 = 3,6.",
        "uitleg": "1 km = 1000 m en 1 h = 3600 s. Dus 3600 / 1000 = 3,6."
    },
    {
        "type": "open",
        "vraag": "Een wandelaar legt 1800 meter af in 20 minuten tijd. Bereken zijn gemiddelde snelheid in m/s.",
        "sleutelwoorden": [
            "1,5",
            "1200 seconden"
        ],
        "minTreffers": 1,
        "modelantwoord": "20 minuten = 20 × 60 = 1200 seconden. vgem = s / t = 1800 m / 1200 s = 1,5 m/s.",
        "uitleg": "Tijd omrekenen naar seconden (1200 s) en dan delen: 1800 / 1200 = 1,5 m/s."
    }
]
});

/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Toets 31 — Toets 31 — §1.2 Soorten beweging & Diagrammen — Toets C
   Gebaseerd op Overal Natuurkunde 3 HAVO (Hoofdstuk 1 Kracht en beweging)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-h3-natuurkunde-31",
  "hoofdstuk": 1,
  "paragraaf": "1.2",
  "titel": "Toets 31 — §1.2 Soorten beweging & Diagrammen — Toets C",
  "vak": "Natuurkunde · HAVO 3 (H1)",
  "icoon": "📈",
  "duurMin": 30,
  "vragen": [
    {
        "type": "mc",
        "vraag": "In figuur 1.7 van het boek bestaat een beweging uit twee delen: interval 1 (0 tot 2 s, van 0 naar 10 m) en interval 2 (2 tot 6 s, van 10 naar 15 m). Wat is de snelheid in interval 1?",
        "opties": [
            "5,0 m/s",
            "1,25 m/s",
            "10 m/s",
            "2,5 m/s"
        ],
        "antwoord": 0,
        "uitleg": "v1 = s / t = 10 m / 2,0 s = 5,0 m/s (zie voorbeeld 3 op blz. 15 van het theorieboek)."
    },
    {
        "type": "mc",
        "vraag": "Wat is de snelheid van dezelfde beweging in interval 2 (van 2 tot 6 s, waarin de afstand toeneemt van 10 naar 15 m)?",
        "opties": [
            "5,0 m/s",
            "1,25 m/s",
            "3,75 m/s",
            "0,80 m/s"
        ],
        "antwoord": 1,
        "uitleg": "Δs = 15 - 10 = 5,0 m en Δt = 6,0 - 2,0 = 4,0 s. v2 = 5,0 / 4,0 = 1,25 m/s (voorbeeld 3b)."
    },
    {
        "type": "mc",
        "vraag": "Wat is de totale gemiddelde snelheid over de gehele beweging van 0 tot 6,0 seconden (totale afstand 15 m)?",
        "opties": [
            "3,13 m/s",
            "5,0 m/s",
            "2,5 m/s",
            "1,25 m/s"
        ],
        "antwoord": 2,
        "uitleg": "vgem,totaal = stotaal / ttotaal = 15 m / 6,0 s = 2,5 m/s."
    },
    {
        "type": "mc",
        "vraag": "In opdracht 26 fietsen Peter en Yvonne naar hun werk. Peter fietst met 18 m/s en Yvonne met 13 m/s. Wat moet je als eerste doen als de tijd op de x-as in minuten is gegeven?",
        "opties": [
            "De snelheid delen door 60",
            "De afstand direct schatten zonder omrekenen",
            "De snelheid vermenigvuldigen met 3,6",
            "De tijd in minuten omrekenen naar seconden (vermenigvuldigen met 60)"
        ],
        "antwoord": 3,
        "uitleg": "Omdat de snelheid in meter per seconde (m/s) staat, moet de tijd in seconden staan: 1 minuut = 60 s."
    },
    {
        "type": "mc",
        "vraag": "Een sprinter trekt in 2,5 seconden op van 0 naar 10 m/s. Hoeveel meter legt hij in deze 2,5 seconden af?",
        "opties": [
            "12,5 m",
            "25 m",
            "4 m",
            "8 m"
        ],
        "antwoord": 0,
        "uitleg": "s = 1/2 · t · veind = 1/2 × 2,5 s × 10 m/s = 12,5 m."
    },
    {
        "type": "mc",
        "vraag": "Waarom is de grafiek van een optrekkende auto in een (s,t)-diagram een kromme lijn die steeds steiler omhoog buigt?",
        "opties": [
            "Omdat de auto steeds zwaarder wordt",
            "Omdat de snelheid toeneemt, waardoor er per seconde steeds meer meters worden afgelegd",
            "Omdat de wrijving met het asfalt toeneemt",
            "Omdat de klok sneller gaat lopen"
        ],
        "antwoord": 1,
        "uitleg": "In een (s,t)-diagram is de steilheid de snelheid. Als de auto versnelt, wordt de snelheid groter en dus wordt de grafiek steeds steiler (blz. 16)."
    },
    {
        "type": "mc",
        "vraag": "Een auto rijdt met 108 km/h. Hoeveel meter legt deze auto af in 0,80 seconden reactietijd?",
        "opties": [
            "86,4 m",
            "30 m",
            "24 m",
            "18 m"
        ],
        "antwoord": 2,
        "uitleg": "108 km/h = 108 / 3,6 = 30 m/s. Afstand s = v · t = 30 m/s × 0,80 s = 24 m."
    },
    {
        "type": "mc",
        "vraag": "Wat gebeurt er met de versnelling als de snelheid van een voorwerp in een (v,t)-diagram volgens een rechte stijgende lijn toeneemt?",
        "opties": [
            "De versnelling neemt elke seconde toe",
            "De versnelling neemt elke seconde af",
            "De versnelling is exact gelijk aan nul",
            "De versnelling is constant"
        ],
        "antwoord": 3,
        "uitleg": "Een rechte lijn in een (v,t)-diagram betekent dat de helling constant is. De versnelling a is dus constant (eenparig versneld)."
    },
    {
        "type": "mc",
        "vraag": "Een goederentrein remt af met een constante vertraging van 0,50 m/s². De beginsnelheid is 20 m/s. Hoeveel seconden duurt het voordat de trein stilstaat?",
        "opties": [
            "40 s",
            "10 s",
            "20 s",
            "5 s"
        ],
        "antwoord": 0,
        "uitleg": "t = Δv / a = 20 m/s / 0,50 m/s² = 40 s."
    },
    {
        "type": "mc",
        "vraag": "Welke afstand legt deze goederentrein af tijdens het remmen (beginsnelheid 20 m/s, remtijd 40 s tot stilstand)?",
        "opties": [
            "800 m",
            "400 m",
            "200 m",
            "100 m"
        ],
        "antwoord": 1,
        "uitleg": "Oppervlakte driehoek = 1/2 × basis × hoogte = 1/2 × 40 s × 20 m/s = 400 m (of vgem = 10 m/s; s = 10 × 40 = 400 m)."
    },
    {
        "type": "mc",
        "vraag": "Welke van de onderstaande snelheden is het grootst?",
        "opties": [
            "18 km/h",
            "12 m/s",
            "15 m/s",
            "50 km/h"
        ],
        "antwoord": 2,
        "uitleg": "Omrekenen naar km/h: 18 km/h; 12 m/s = 43,2 km/h; 50 km/h; 15 m/s = 15 × 3,6 = 54 km/h. 15 m/s is dus de grootste snelheid."
    },
    {
        "type": "mc",
        "vraag": "Wat voor lijn zie je in een (v,t)-diagram van een voorwerp dat stilstaat?",
        "opties": [
            "Een verticale lijn langs de y-as",
            "Een stijgende lijn onder een hoek van 45 graden",
            "Een horizontale lijn op hoogte v = 1",
            "Een lijn die precies op de horizontale tijdas ligt (v = 0)"
        ],
        "antwoord": 3,
        "uitleg": "Bij stilstand is v = 0 m/s voor elk tijdstip; de grafiek valt precies samen met de horizontale tijdas."
    },
    {
        "type": "waaronwaar",
        "vraag": "De gemiddelde snelheid van een voorwerp kan berekend worden door de totale afstand te delen door de totale tijd.",
        "antwoord": true,
        "uitleg": "Waar. vgem = stotaal / ttotaal."
    },
    {
        "type": "waaronwaar",
        "vraag": "Bij een eenparig vertraagde beweging tot stilstand is de gemiddelde snelheid gelijk aan de helft van de beginsnelheid.",
        "antwoord": true,
        "uitleg": "Waar. vgem = (vbegin + veind) / 2 = (vbegin + 0) / 2 = 1/2 · vbegin."
    },
    {
        "type": "waaronwaar",
        "vraag": "Een voorwerp met een negatieve versnelling beweegt altijd achteruit.",
        "antwoord": false,
        "uitleg": "Onwaar. Een negatieve versnelling betekent dat de voorwaartse snelheid afneemt (vertraging), het voorwerp beweegt nog steeds voorwaarts."
    },
    {
        "type": "waaronwaar",
        "vraag": "In een (s,t)-diagram geeft de oppervlakte onder de lijn de versnelling aan.",
        "antwoord": false,
        "uitleg": "Onwaar. In een (s,t)-diagram heeft de oppervlakte onder de lijn geen natuurkundige betekenis; de helling is de snelheid."
    },
    {
        "type": "invul",
        "vraag": "Een fietser rijdt in 2,0 uur een afstand van 36 km. Zijn gemiddelde snelheid is ... km/h.",
        "antwoord": "18",
        "uitleg": "vgem = 36 / 2,0 = 18 km/h."
    },
    {
        "type": "invul",
        "vraag": "Een auto versnelt in 5,0 seconden van 10 m/s naar 25 m/s. De versnelling is ... m/s².",
        "antwoord": "3",
        "uitleg": "a = (25 - 10) / 5,0 = 15 / 5,0 = 3,0 m/s²."
    },
    {
        "type": "open",
        "vraag": "Leg uit hoe je aan de vorm van een lijn in een afstand-tijd-grafiek kunt zien of een beweging eenparig versneld is.",
        "sleutelwoorden": [
            "steiler omhoog/steeds steiler",
            "parabool/kromme lijn"
        ],
        "minTreffers": 1,
        "modelantwoord": "De grafiek is een kromme lijn die steeds steiler omhoog loopt omdat de snelheid per seconde toeneemt.",
        "uitleg": "Een toenemende helling betekent een toenemende snelheid."
    },
    {
        "type": "open",
        "vraag": "Een wielrenner fietst met 36 km/h. Bepaal hoeveel meter hij aflegt in tien seconden tijd.",
        "sleutelwoorden": [
            "100 meter",
            "100 m"
        ],
        "minTreffers": 1,
        "modelantwoord": "36 km/h = 10 m/s. s = v · t = 10 m/s × 10 s = 100 meter.",
        "uitleg": "Eerst omrekenen naar 10 m/s en dan vermenigvuldigen met 10 s."
    }
]
});

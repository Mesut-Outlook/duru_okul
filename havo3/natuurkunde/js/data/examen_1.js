/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Toets 1 — Krachten, Resulterende Kracht & Bewegingssoorten
   ========================================================= */
DURU.registerExamen({
  "id": "ex-h3-natuurkunde-1",
  "titel": "Toets 1 — Krachten, Resulterende Kracht & Bewegingssoorten",
  "vak": "Natuurkunde · HAVO 3 (H1)",
  "icoon": "🏎️",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat is de officiële SI-eenheid van <b>kracht</b>?",
      "opties": [
        "Newton (N)",
        "Joule (J)",
        "Watt (W)",
        "Kilogram (kg)"
      ],
      "antwoord": 0,
      "uitleg": "Kracht wordt gemeten in Newton (N). Joule is voor energie/arbeid, Watt voor vermogen en kilogram voor massa."
    },
    {
      "type": "mc",
      "vraag": "Een auto rijdt naar rechts met een motorkracht van 1200 N. De tegenwerkende wrijvingskrachten bedragen samen 800 N. Hoe groot is de <b>resulterende kracht (F_res)</b> en wat gebeurt er met de beweging?",
      "opties": [
        "400 N naar links; de auto vertraagt",
        "400 N naar rechts; de auto versnelt",
        "2000 N naar rechts; de auto rijdt met constante snelheid",
        "0 N; de auto staat stil"
      ],
      "antwoord": 1,
      "uitleg": "F_res = F_motor - F_tegen = 1200 N - 800 N = 400 N naar rechts. Omdat de resulterende kracht in de bewegingsrichting werkt, versnelt de auto."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als de resulterende kracht op een bewegend voorwerp gelijk is aan <b>0 N</b>, komt het voorwerp onmiddellijk tot stilstand.",
      "antwoord": false,
      "uitleg": "Niet waar. Als F_res = 0 N, blijft de snelheid constant (eenparige beweging). Het voorwerp behoudt zijn snelheid en richting."
    },
    {
      "type": "invul",
      "vraag": "Reken om: een fietser rijdt met een snelheid van <b>18 km/h</b>. Hoeveel meter per seconde (m/s) is dat?",
      "antwoord": "5|5,0|5 m/s",
      "uitleg": "Om te rekenen van km/h naar m/s deel je door 3,6: 18 / 3,6 = 5 m/s."
    },
    {
      "type": "mc",
      "vraag": "Wat voor soort beweging stelt een <b>horizontale rechte lijn</b> in een <b>(v,t)-diagram</b> voor?",
      "opties": [
        "Eenparig versnelde beweging",
        "Stilstand",
        "Eenparige beweging (constante snelheid)",
        "Eenparig vertraagde beweging"
      ],
      "antwoord": 2,
      "uitleg": "In een (v,t)-diagram staat de snelheid op de verticale as. Een horizontale lijn betekent dat de snelheid niet verandert: de beweging is eenparig (constante snelheid)."
    },
    {
      "type": "invul",
      "vraag": "Reken om: een hardloper rent met <b>4,5 m/s</b>. Hoeveel km/h is dat?",
      "antwoord": "16,2|16,2 km/h",
      "uitleg": "Om te rekenen van m/s naar km/h vermenigvuldig je met 3,6: 4,5 × 3,6 = 16,2 km/h."
    },
    {
      "type": "mc",
      "vraag": "Twee personen trekken aan een touw. Anna trekt naar links met 150 N, Bram trekt naar rechts met 150 N. Wat is de resulterende kracht?",
      "opties": [
        "300 N naar links",
        "300 N naar rechts",
        "150 N naar rechts",
        "0 N"
      ],
      "antwoord": 3,
      "uitleg": "De krachten zijn even groot maar tegengesteld gericht: 150 N - 150 N = 0 N. Ze heffen elkaar precies op."
    },
    {
      "type": "waaronwaar",
      "vraag": "In een <b>(s,t)-diagram</b> betekent een steilere lijn dat de snelheid groter is.",
      "antwoord": false,
      "uitleg": "Onwaar: Waar. De helling (steilheid) in een (s,t)-diagram geeft aan hoeveel afstand er per seconde wordt afgelegd, oftewel de snelheid."
    },
    {
      "type": "mc",
      "vraag": "Een scooter rijdt in 15 seconden een afstand van 180 meter met constante snelheid. Wat is zijn snelheid in m/s?",
      "opties": [
        "12 m/s",
        "10 m/s",
        "8 m/s",
        "15 m/s"
      ],
      "antwoord": 0,
      "uitleg": "v = s / t = 180 m / 15 s = 12 m/s."
    },
    {
      "type": "invul",
      "vraag": "Als een voorwerp iedere seconde met <b>dezelfde hoeveelheid snelheid toeneemt</b>, noem je de beweging … versneld.",
      "antwoord": "eenparig|eenparig versneld",
      "uitleg": "Als de snelheid gelijkmatig (met een vast aantal m/s per seconde) toeneemt, heet dat een eenparig versnelde beweging."
    },
    {
      "type": "mc",
      "vraag": "Welke twee krachten vormen samen de belangrijkste <b>tegenwerkende kracht</b> op een rijdende fietser?",
      "opties": [
        "Zwaartekracht en normaalkracht",
        "Luchtweerstand en rolweerstand",
        "Spierkracht en veerkracht",
        "Motorkracht en zwaartekracht"
      ],
      "antwoord": 1,
      "uitleg": "De tegenwerkende wrijvingskrachten bij fietsen zijn de luchtweerstand (wrijving met de lucht) en de rolweerstand (wrijving van de banden met de weg)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als je twee keer zo snel fietst, wordt de <b>luchtweerstand</b> ongeveer vier keer zo groot.",
      "antwoord": true,
      "uitleg": "Waar. De luchtweerstand stijgt kwadratisch met de snelheid (als de snelheid verdubbelt, wordt de luchtweerstand 2² = 4 keer zo groot)."
    },
    {
      "type": "mc",
      "vraag": "Hoe bepaal je de <b>afgelegde afstand</b> uit een <b>(v,t)-diagram</b>?",
      "opties": [
        "Door de hoogste snelheid af te lezen",
        "Door de helling van de lijn te bepalen",
        "Door de oppervlakte onder de grafieklijn te berekenen",
        "Door de eindsnelheid te delen door de tijd"
      ],
      "antwoord": 2,
      "uitleg": "De afgelegde afstand s is gelijk aan de oppervlakte onder de (v,t)-grafiek (bijv. rechthoek: v × t of driehoek: 0,5 × v × t)."
    },
    {
      "type": "invul",
      "vraag": "Een auto trekt eenparig op vanuit stilstand (v = 0 m/s) naar 20 m/s in 8,0 seconden. Bereken de afgelegde afstand s in meters (gebruik de oppervlakte van de driehoek onder de grafiek).",
      "antwoord": "80|80 m|80,0",
      "uitleg": "Afstand = oppervlakte onder de driehoek = 0,5 × basis × hoogte = 0,5 × 8,0 s × 20 m/s = 80 meter."
    },
    {
      "type": "mc",
      "vraag": "Wat stelt een <b>horizontale rechte lijn</b> in een <b>(s,t)-diagram</b> voor?",
      "opties": [
        "Het voorwerp vertraagt",
        "Het voorwerp beweegt met constante snelheid",
        "Het voorwerp versnelt",
        "Het voorwerp staat stil"
      ],
      "antwoord": 3,
      "uitleg": "In een (s,t)-diagram staat de afstand op de y-as. Een horizontale lijn betekent dat de afstand niet verandert in de tijd: het voorwerp staat stil."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een kracht is een vectorgrootheid, wat betekent dat een kracht zowel een <b>grootte</b> als een <b>richting</b> heeft.",
      "antwoord": false,
      "uitleg": "Onwaar: Waar. Kracht heeft een grootte (aantal Newton), een richting (waarheen) en een aangrijpingspunt."
    },
    {
      "type": "mc",
      "vraag": "Een trein rijdt met een constante snelheid van 90 km/h gedurende 20 minuten. Welke afstand legt de trein af?",
      "opties": [
        "30 km",
        "18 km",
        "45 km",
        "60 km"
      ],
      "antwoord": 0,
      "uitleg": "20 minuten = 1/3 uur (of 20/60 = 0,333 uur). Afstand s = v × t = 90 km/h × (20/60) h = 30 km."
    },
    {
      "type": "invul",
      "vraag": "Drie kinderen duwen samen een kano vooruit met krachten van 45 N, 55 N en 60 N. Het water oefent een tegenwerkende wrijvingskracht uit van 110 N. Hoe groot is de resulterende kracht in Newton?",
      "antwoord": "50|50 N",
      "uitleg": "Totale voorwaartse kracht = 45 + 55 + 60 = 160 N. Tegenwerkende kracht = 110 N. F_res = 160 N - 110 N = 50 N."
    },
    {
      "type": "open",
      "vraag": "Leg uit wat het verschil is tussen een <b>versnelde beweging</b> en een <b>eenparig versnelde beweging</b>.",
      "sleutelwoorden": [
        "toeneemt/groter wordt",
        "gelijkmatig/iedere seconde evenveel/constante versnelling"
      ],
      "minTreffers": 2,
      "modelantwoord": "Bij een versnelde beweging neemt de snelheid in de loop van de tijd toe. Bij een eenparig versnelde beweging neemt de snelheid gelijkmatig toe, wat betekent dat er iedere seconde precies evenveel snelheid bij komt (de versnelling is constant).",
      "uitleg": "Kernpunten: beide bewegingen gaan sneller, maar 'eenparig' betekent dat de toename per tijdseenheid constant (gelijkmatig) is."
    },
    {
      "type": "open",
      "vraag": "Een parachutist springt uit een vliegtuig. Na enige tijd bereikt hij een constante eindsnelheid (nog vóór hij zijn parachute opent). Leg uit welke <b>krachten</b> er op hem werken en waarom zijn snelheid niet meer toeneemt.",
      "sleutelwoorden": [
        "zwaartekracht",
        "luchtweerstand",
        "gelijk/opheffen/nul/resulterende kracht 0"
      ],
      "minTreffers": 2,
      "modelantwoord": "Tijdens het vallen neemt door de toenemende snelheid de luchtweerstand steeds verder toe, totdat de omhooggerichte luchtweerstand precies even groot is als de omlaaggerichte zwaartekracht. De resulterende kracht wordt dan 0 N, waardoor de snelheid constant blijft en niet meer toeneemt.",
      "uitleg": "Als F_lucht = F_zwaartekracht, is F_res = 0 N en versnelt de springer niet meer."
    }
  ]
});

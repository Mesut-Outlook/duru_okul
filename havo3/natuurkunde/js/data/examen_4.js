/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Toets 4 — Arbeid, Kracht & Energieomzetting
   ========================================================= */
DURU.registerExamen({
  "id": "ex-h3-natuurkunde-4",
  "titel": "Toets 4 — Arbeid, Kracht & Energieomzetting",
  "vak": "Natuurkunde · HAVO 3 (H1)",
  "icoon": "⚙️",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat is de officiële eenheid van <b>arbeid (W)</b> en energie in de natuurkunde?",
      "opties": [
        "Joule (J)",
        "Watt (W)",
        "Newton (N)",
        "Pascal (Pa)"
      ],
      "antwoord": 0,
      "uitleg": "Arbeid is de hoeveelheid overgedragen energie en wordt gemeten in Joule (J) of Newton-meter (N·m)."
    },
    {
      "type": "mc",
      "vraag": "Welke formule gebruik je om de verrichte <b>arbeid (W)</b> te berekenen bij een kracht F over een afstand s?",
      "opties": [
        "W = F / s",
        "W = F × s",
        "W = m × a",
        "W = s / t"
      ],
      "antwoord": 1,
      "uitleg": "W = F × s, waarbij W de arbeid in Joule is, F de kracht in Newton in de bewegingsrichting, en s de verplaatsing in meter."
    },
    {
      "type": "invul",
      "vraag": "Een paard trekt een kar met een constante kracht van 400 N over een afstand van 25 meter. Hoeveel Joule arbeid verricht het paard?",
      "antwoord": "10000|10.000|10000 J|10.000 J|10 kJ",
      "uitleg": "W = F × s = 400 N × 25 m = 10.000 J (of 10 kJ)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als je 10 minuten lang uit alle macht tegen een zware stenen muur duwt die niet van zijn plek komt, heb je in de natuurkunde <b>geen arbeid</b> verricht.",
      "antwoord": true,
      "uitleg": "Waar. Omdat de verplaatsing s = 0 m is, geldt W = F × 0 = 0 Joule. Er is natuurkundig gezien geen arbeid verricht, ook al voel je je moe."
    },
    {
      "type": "mc",
      "vraag": "In welke van de volgende situaties wordt er <b>negatieve arbeid</b> verricht?",
      "opties": [
        "Een trekker die een ploeg vooruit trekt",
        "De zwaartekracht op een appel die van een boom naar beneden valt",
        "De wrijvingskracht van de remmen die een auto tot stilstand brengt",
        "Een gewichtheffer die een halter omhoog drukt"
      ],
      "antwoord": 2,
      "uitleg": "De wrijvings- of remkracht werkt tegen de bewegingsrichting in en verricht daardoor negatieve arbeid: het onttrekt bewegingsenergie en zet dit om in warmte."
    },
    {
      "type": "invul",
      "vraag": "Reken om: hoeveel Joule is <b>18,5 kJ</b>?",
      "antwoord": "18500|18.500|18500 J|18.500 J",
      "uitleg": "1 kJ (kilojoule) = 1000 Joule. Dus 18,5 × 1000 = 18.500 J."
    },
    {
      "type": "mc",
      "vraag": "Iemand tilt een doos van 15 kg verticaal 2,0 meter omhoog (neem g = 10 N/kg). Hoeveel arbeid verricht de spierkracht?",
      "opties": [
        "30 J",
        "75 J",
        "150 J",
        "300 J"
      ],
      "antwoord": 3,
      "uitleg": "Eerst de zwaartekracht: F_z = m × g = 15 kg × 10 N/kg = 150 N. Arbeid: W = F × s = 150 N × 2,0 m = 300 Joule."
    },
    {
      "type": "waaronwaar",
      "vraag": "Wanneer je een zware tas vasthoudt en horizontaal op gelijke hoogte recht vooruit loopt, verricht de opwaartse tilkracht van je arm arbeid op de tas.",
      "antwoord": false,
      "uitleg": "Niet waar. De tilkracht staat loodrecht (90°) op de horizontale bewegingsrichting. Een kracht loodrecht op de verplaatsing verricht geen arbeid."
    },
    {
      "type": "invul",
      "vraag": "Een fietser verricht 2400 J arbeid door over een afstand van 60 meter te trappen. Hoe groot was de gemiddelde voorwaartse kracht in Newton?",
      "antwoord": "40|40 N|40,0",
      "uitleg": "F = W / s = 2400 J / 60 m = 40 Newton."
    },
    {
      "type": "mc",
      "vraag": "Welke <b>energieomzetting</b> vindt er plaats als een kogelstoter zijn spieren gebruikt om een kogel met kracht weg te stoten?",
      "opties": [
        "Chemische energie (uit voedsel) → bewegingsenergie (kinetische energie)",
        "Kernenergie → warmte",
        "Zwaarte-energie → chemische energie",
        "Elektrische energie → stralingsenergie"
      ],
      "antwoord": 0,
      "uitleg": "Spieren zetten opgeslagen chemische energie uit voedsel om in mechanische arbeid, waardoor de kogel bewegingsenergie (kinetische energie) krijgt."
    },
    {
      "type": "waaronwaar",
      "vraag": "Volgens de <b>wet van behoud van energie</b> kan energie niet verdwijnen of uit het niets ontstaan, maar alleen van vorm veranderen.",
      "antwoord": true,
      "uitleg": "Waar. Energie blijft altijd behouden: totale energie voor = totale energie na."
    },
    {
      "type": "invul",
      "vraag": "Bij het heien slaat een heiblok met een kracht van 50.000 N op een paal. De paal zakt bij één klap 0,08 m de grond in. Hoeveel Joule arbeid is er bij die klap verricht?",
      "antwoord": "4000|4000 J|4.000|4.000 J|4 kJ",
      "uitleg": "W = F × s = 50.000 N × 0,08 m = 4000 Joule (4 kJ)."
    },
    {
      "type": "mc",
      "vraag": "Een windsurfer vaart met <b>constante snelheid</b>. De windkracht in het zeil is 250 N voorwaarts. De surfer legt 100 m af. Hoeveel arbeid verricht de <b>tegenwerkende waterweerstand</b>?",
      "opties": [
        "+25.000 J",
        "-25.000 J",
        "0 J",
        "+250 J"
      ],
      "antwoord": 1,
      "uitleg": "Bij constante snelheid is F_wrijving even groot als de voorwaartse kracht (250 N), maar tegengesteld gericht. W_wrijving = -250 N × 100 m = -25.000 J (-25 kJ)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Bij het afremmen van een auto wordt de bewegingsenergie door wrijvingsarbeid in de remmen omgezet in warmte-energie.",
      "antwoord": false,
      "uitleg": "Onwaar: Waar. De remblokken wrijven tegen de remschijven en zetten de kinetische energie van de auto om in warmte."
    },
    {
      "type": "mc",
      "vraag": "Waarom neemt een speerwerper een flinke aanloop voordat hij de speer werpt?",
      "opties": [
        "Om de speer zwaarder te maken",
        "Om de luchtweerstand tijdens de vlucht te verminderen",
        "Om de afstand s waarover spierkracht op de speer kan worden uitgeoefend te vergroten, zodat er meer arbeid wordt verricht",
        "Om de zwaartekracht tijdelijk uit te schakelen"
      ],
      "antwoord": 2,
      "uitleg": "Door de aanloop en het strekken van het lichaam kan de kracht over een grotere afstand s worden uitgeoefend (W = F × s), waardoor de speer meer bewegingsenergie en een hogere afwerpsnelheid krijgt."
    },
    {
      "type": "invul",
      "vraag": "Een kraan hijst een container van 2000 kg over een hoogte van 15 meter omhoog (neem g = 9,81 N/kg). Hoeveel kJ arbeid verricht de kraan? (Rond af op een geheel getal).",
      "antwoord": "294|294 kJ|294,3|294,3 kJ|300",
      "uitleg": "F_z = 2000 kg × 9,81 N/kg = 19.620 N. W = F × s = 19.620 N × 15 m = 294.300 J = 294,3 kJ (afgerond 294 kJ). Met g = 10 is het 300 kJ."
    },
    {
      "type": "mc",
      "vraag": "Een wielrenner fietst een heuvel op. Welke vorm van energie bouwt de wielrenner op tijdens het klimmen?",
      "opties": [
        "Chemische energie",
        "Elektrische energie",
        "Kernenergie",
        "Zwaarte-energie (potentiële energie)"
      ],
      "antwoord": 3,
      "uitleg": "Door hoogte te winnen tegen de zwaartekracht in, wordt de verrichte arbeid omgezet in zwaarte-energie (hoogte-energie / potentiële energie)."
    },
    {
      "type": "invul",
      "vraag": "Een boogschutter trekt een pees naar achteren met een gemiddelde kracht van 120 N over een afstand van 0,50 m. Hoeveel Joule spankracht-arbeid (veerenergie) zit er in de boog opgeslagen?",
      "antwoord": "60|60 J|60,0",
      "uitleg": "W = F × s = 120 N × 0,50 m = 60 Joule."
    },
    {
      "type": "open",
      "vraag": "Leg uit hoe de energieomzetting verloopt bij een skateboarder die van een helling (halfpipe) naar beneden rijdt en aan de overkant weer omhoog gaat. <b>Benoem zelf de energiesoorten</b> die daarbij een rol spelen, en verklaar waarom hij zonder bijsteppen telkens iets minder hoog komt.",
      "sleutelwoorden": [
        "zwaarte-energie/potentiële energie",
        "bewegingsenergie/kinetische energie",
        "omgezet in warmte/wrijving/energieverlies"
      ],
      "minTreffers": 2,
      "modelantwoord": "Bovenaan de helling heeft de skateboarder maximale zwaarte-energie en geen bewegingsenergie. Tijdens het naar beneden rijden wordt zwaarte-energie omgezet in bewegingsenergie (hoogste snelheid onderaan). Als hij weer omhoog rijdt, wordt bewegingsenergie weer omgezet in zwaarte-energie. Door wrijving wordt een klein deel van de energie omgezet in warmte, waardoor hij zonder bijsteppen telkens iets minder hoog komt.",
      "uitleg": "Zwaarte-energie ↔ bewegingsenergie met een klein energieverlies aan wrijvingswarmte."
    },
    {
      "type": "open",
      "vraag": "Een sporter tilt een halter van 80 kg op vanaf de grond tot boven zijn hoofd (2,0 meter hoog) en houdt hem daar 5 seconden stil. Leg uit in welke fase hij <b>natuurkundige arbeid verricht</b> en in welke fase <b>niet</b>, en verklaar waarom.",
      "sleutelwoorden": [
        "optillen/omhoog bewegen wel arbeid",
        "stilhouden geen arbeid/verplaatsing is nul",
        "W = F * s"
      ],
      "minTreffers": 2,
      "modelantwoord": "Tijdens het optillen van de halter is er een kracht omhoog én een verplaatsing van 2,0 m omhoog (s > 0), dus verricht hij positieve arbeid (W = F × s = 800 N × 2 m = 1600 J). Tijdens het 5 seconden stilhouden boven zijn hoofd is de verplaatsing s = 0 meter; volgens de formule W = F × s verricht hij dan natuurkundig gezien 0 Joule arbeid.",
      "uitleg": "Alleen wanneer er een verplaatsing is in de richting van de kracht, is er sprake van natuurkundige arbeid."
    }
  ]
});

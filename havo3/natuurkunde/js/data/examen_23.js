/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Toets 23 — Overbrengingen, Katrollen & Tandwielen
   ========================================================= */
DURU.registerExamen({
  "id": "ex-h3-natuurkunde-23",
  "titel": "Toets 23 — Overbrengingen, Katrollen & Tandwielen",
  "vak": "Natuurkunde · HAVO 3 (H8)",
  "icoon": "⚙️",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat doet een <b>vaste katrol</b> met de uitgeoefende spierkracht?",
      "opties": [
        "Verandert alleen de richting van de kracht; de spierkracht blijft even groot als het gewicht van de last (F_spier = F_last)",
        "Halveert de benodigde spierkracht",
        "Verdubbelt de benodigde spierkracht",
        "Maakt de spierkracht nul"
      ],
      "antwoord": 0,
      "uitleg": "Een vaste katrol zit aan het plafond vast en verandert alleen de trekrichting (omlaag trekken om iets op te tillen). De kracht blijft gelijk."
    },
    {
      "type": "mc",
      "vraag": "Wat is het voordeel van een <b>losse katrol</b>?",
      "opties": [
        "Je hoeft minder touw binnen te halen",
        "De benodigde spierkracht wordt gehalveerd (F_spier = 1/2 × F_last), omdat de last door twee touwdelen gedragen wordt",
        "De richting verandert naar beneden",
        "Het voorwerp beweegt twee keer zo snel"
      ],
      "antwoord": 1,
      "uitleg": "Bij een losse katrol hangt het voorwerp aan de katrol in een touwlus. Elk touwdeel draagt de helft van de last."
    },
    {
      "type": "mc",
      "vraag": "Wat stelt de <b>Gouden Regel van de Mechanica</b>?",
      "opties": [
        "Wrijving maakt alle energie nutteloos",
        "Kracht maal arm is altijd constant in een motor",
        "Wat je wint aan kracht, verlies je aan afstand (je moet over een evenredig langere afstand trekken)",
        "Met tandwielen verdwijnt er nooit energie"
      ],
      "antwoord": 2,
      "uitleg": "Gouden regel: als de kracht 2× zo klein wordt, moet je 2× zoveel touw binnenhalen (de arbeid W = F × s blijft gelijk)."
    },
    {
      "type": "invul",
      "vraag": "Je tilt een last van 600 N op met een losse katrol. Hoeveel spierkracht in Newton moet je uitoefenen (verwaarloos het gewicht van de katrol en wrijving)?",
      "antwoord": "300|300 N",
      "uitleg": "F_spier = F_last / 2 = 600 N / 2 = 300 N."
    },
    {
      "type": "invul",
      "vraag": "In de vorige situatie wil je de last 1,5 m omhoog hijsen. Hoeveel meter touw moet je dan binnenhalen?",
      "antwoord": "3|3 m|3 meter|3,0|3,0 m",
      "uitleg": "s_touw = 2 × s_last = 2 × 1,5 m = 3,0 m."
    },
    {
      "type": "mc",
      "vraag": "Een takel (katrolstelsel) heeft <b>4 dragende touwdelen</b>. Een last heeft een gewicht van 1200 N. Hoe groot is de benodigde spierkracht?",
      "opties": [
        "2400 N",
        "600 N",
        "1200 N",
        "300 N"
      ],
      "antwoord": 3,
      "uitleg": "F_spier = F_last / n = 1200 N / 4 = 300 N."
    },
    {
      "type": "invul",
      "vraag": "Hoeveel meter touw moet je binnenhalen bij de takel uit de vorige vraag (met 4 dragende touwdelen) om de last 2,0 m omhoog te hijsen?",
      "antwoord": "8|8 m|8 meter|8,0|8,0 m",
      "uitleg": "s_touw = n × s_last = 4 × 2,0 m = 8,0 m."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als twee tandwielen direct in elkaar grijpen, draaien ze altijd in precies dezelfde richting.",
      "antwoord": false,
      "uitleg": "Waar. Tandwiel 1 draait met de klok mee -> tandwiel 2 draait tegen de klok in."
    },
    {
      "type": "mc",
      "vraag": "Wat gebeurt er als je een derde tandwiel (een tussenwiel) tussen twee tandwielen in plaatst?",
      "opties": [
        "Het eerste en derde tandwiel draaien nu weer in dezelfde richting",
        "De overbrengingsverhouding wordt verdubbeld",
        "De tandwielen blokkeren",
        "De snelheid wordt gehalveerd"
      ],
      "antwoord": 0,
      "uitleg": "Een tussenwiel keert de draairichting nogmaals om, waardoor ingang en uitgang in dezelfde richting draaien."
    },
    {
      "type": "invul",
      "vraag": "Tandwiel A heeft 40 tanden en drijft tandwiel B met 10 tanden aan. Als tandwiel A 1 omwenteling maakt, hoeveel omwentelingen maakt tandwiel B dan?",
      "antwoord": "4|4 omwentelingen|4x",
      "uitleg": "Omwentelingen B = tanden A / tanden B = 40 / 10 = 4 omwentelingen (tandwiel B draait 4× zo snel)."
    },
    {
      "type": "mc",
      "vraag": "Wat gebeurt er met de uitgeoefende kracht op de as van tandwiel B in de vorige vraag (waarbij tandwiel B 4× zo snel draait als A)?",
      "opties": [
        "De kracht op tandwiel B is 4 keer zo groot geworden",
        "De kracht op tandwiel B is 4 keer zo klein geworden",
        "De kracht blijft gelijk",
        "Er is geen kracht meer"
      ],
      "antwoord": 1,
      "uitleg": "Volgens de gouden regel: sneller draaien = minder kracht. Kracht op B is 4× kleiner."
    },
    {
      "type": "waaronwaar",
      "vraag": "Bij een racefiets kies je bij het beklimmen van een steile berg juist het allergrootste voortandwiel en kleinste achtertandwiel om lichter te kunnen trappen.",
      "antwoord": false,
      "uitleg": "Onwaar: Waar. Hierdoor hoef je minder spierkracht te zetten, maar moet je vaker trappen (meer omwentelingen maken)."
    },
    {
      "type": "mc",
      "vraag": "Hoe noem je een overbrenging waarbij de draaibeweging van twee assen op afstand via een ketting of riem wordt overgebracht?",
      "opties": [
        "Een hydraulische pers",
        "Een hefboomkoppeling",
        "Een kettingoverbrenging (of riemoverbrenging)",
        "Een vaste katrol"
      ],
      "antwoord": 2,
      "uitleg": "Bijvoorbeeld de ketting op een fiets verbindt het voortandwiel met het achtertandwiel."
    },
    {
      "type": "waaronwaar",
      "vraag": "Bij een kettingoverbrenging (zoals op een fiets) draaien beide tandwielen in dezelfde richting.",
      "antwoord": true,
      "uitleg": "Waar. Omdat de ketting aan de buitenkant over beide tandwielen loopt, draaien ze allebei met de klok mee (vooruit)."
    },
    {
      "type": "invul",
      "vraag": "Een hijskraan gebruikt een takel met 6 dragende touwen om een betonblok van 18.000 N op te hijsen. Welke trekkracht in Newton moet de elektromotor van de lier minimaal leveren?",
      "antwoord": "3000|3000 N|3.000|3.000 N",
      "uitleg": "F_motor = F_last / n = 18.000 N / 6 = 3000 N."
    },
    {
      "type": "mc",
      "vraag": "Waarom telt het uiteinde van het touw waar je zelf aan trekt bij een takel soms WEL en soms NIET mee als dragend touwdeel?",
      "opties": [
        "Het telt nooit mee",
        "Het telt alleen mee als het touw rood is",
        "Het telt altijd mee",
        "Als je omhoog trekt vanaf de losse katrol draagt het touw mee (telt wel mee); als het touw via een vaste katrol naar beneden loopt draagt het niet mee omhoog (telt niet mee)"
      ],
      "antwoord": 3,
      "uitleg": "Alleen touwdelen die een opwaartse trekkracht uitoefenen op de losse katrol/last tellen als dragend deel."
    },
    {
      "type": "waaronwaar",
      "vraag": "In de praktijk moet je bij een takel altijd iets meer spierkracht zetten dan theoretisch berekend door wrijving in de lagers en het eigen gewicht van de losse katrollen.",
      "antwoord": false,
      "uitleg": "Onwaar: Waar. Rendement is in de werkelijkheid kleiner dan 100%."
    },
    {
      "type": "invul",
      "vraag": "Een tandwiel met 12 tanden drijft een tandwiel met 36 tanden aan. Wat is de overbrengingsverhouding (vertraging van het toerental)?",
      "antwoord": "1:3|3|3 keer|1 op 3",
      "uitleg": "36 / 12 = 3. Het grote tandwiel draait 3× zo langzaam, maar levert 3× zoveel koppel (kracht)."
    },
    {
      "type": "open",
      "vraag": "Beredeneer waarom een hefboom met een driemaal langere arm de benodigde handkracht met een factor drie verlaagt bij gelijkblijvende last.",
      "sleutelwoorden": [
        "momentenwet/kracht maal arm",
        "kracht driemaal kleiner"
      ],
      "minTreffers": 2,
      "modelantwoord": "1. Bij een takel met n dragende touwdelen wordt het gewicht van de last gelijkmatig verdeeld over alle dragende touwen. Daardoor is de benodigde trekkracht n keer zo klein als het gewicht van de last ({\text{spier}} = F_{\text{last}} / n$). 2. Volgens de Gouden Regel van de Mechanica (behoud van arbeid) moet je echter n keer zoveel touw binnenhalen om de last omhoog te bewegen ({\text{touw}} = n \times s_{\text{last}}$). Wat je aan spierkracht wint, moet je compenseren in trekafstand.",
      "uitleg": "Krachtverdeling en touwverplaatsing bij takels."
    },
    {
      "type": "open",
      "vraag": "Verklaar hoe een tandwieloverbrenging met verhouding 1:4 het toerental en koppel van een motor transformeert.",
      "sleutelwoorden": [
        "toerental 4x kleiner/trager",
        "koppel 4x groter/sterker"
      ],
      "minTreffers": 2,
      "modelantwoord": "Berekening: Overbrengingsverhouding = 44 / 22 = 2. Bij 1 pedaalomwenteling draait het achterwiel 2 keer rond. Bij 10 omwentelingen van de trappers maakt het achterwiel dus 0 \times 2 = 20\text{ omwentelingen}$. Uitleg: Omdat het achterwiel twee keer zo snel draait als de trappers, is de benodigde trapkracht twee keer zo groot (zwaarder trappen), maar leg je per pedaalslag een dubbele afstand af.",
      "uitleg": "Overbrenging bij fietsversnelling."
    }
  ]
});

/* Proeftoets 24 — Natuurkunde HAVO 3: Hoofdstuk 8 (Krachten gebruiken - Deel 4)
   Focus: Paragraaf 8.4 & 8.5 — Druk, formule p = F / A, eenheden (Pa, N/cm²), druk vergroten/verkleinen en vloeistofdruk (hydraulica).
   20 vragen conform DURU ENGINE_SPEC. */
DURU.registerExamen({
  id: "ex-h3-natuurkunde-24",
  titel: "Toets 24 — Druk & Vloeistofdruk (Hydraulica)",
  vak: "Natuurkunde · HAVO 3 (H8)",
  icoon: "💧",
  duurMin: 30,
  vragen: [
    {
      type: "mc",
      vraag: "Wat is de natuurkundige definitie van <b>druk ($)</b>?",
      opties: [
        "De loodrechte kracht die per oppervlakte-eenheid (per m² of cm²) wordt uitgeoefend (p = F / A)",
        "Het totale gewicht van een voorwerp",
        "De snelheid waarmee vloeistof stroomt",
        "De wrijvingskracht tussen twee oppervlakken"
      ],
      antwoord: 0,
      uitleg: "Druk p = F / A (kracht gedeeld door oppervlakte)."
    },
    {
      type: "mc",
      vraag: "Welke eenheid hoort bij de standaard SI-eenheid <b>Pascal (Pa)</b>?",
      opties: [
        "1 N/cm²",
        "1 N/m² (één Newton per vierkante meter)",
        "1 kg/m³",
        "1 Nm"
      ],
      antwoord: 1,
      uitleg: "1 Pa = 1 N/m², want druk is per definitie kracht gedeeld door oppervlakte (p = F / A) en de SI-eenheid van kracht is de Newton en die van oppervlakte de vierkante meter. 1 N/cm² is dus géén Pascal, maar juist 10.000 keer zo groot."
    },
    {
      type: "invul",
      vraag: "Hoeveel Pascal (Pa) is gelijk aan <b>1 N/cm²</b>?",
      antwoord: "10000|10.000|10000 Pa|10.000 Pa",
      uitleg: "1 m² = 10.000 cm², dus 1 N/cm² = 10.000 N/m² = 10.000 Pa."
    },
    {
      type: "mc",
      vraag: "Een kist met een gewicht van 600 N staat op een grondoppervlak van 0,50 m². Hoe groot is de druk op de vloer in Pascal?",
      opties: [
        "600 Pa",
        "300 Pa",
        "1200 Pa",
        "12.000 Pa"
      ],
      antwoord: 2,
      uitleg: "p = F / A = 600 N / 0,50 m² = 1200 Pa."
    },
    {
      type: "invul",
      vraag: "Een naaldpunt heeft een oppervlakte van 0,001 cm² (0^{-7}\text{ m}^2$). Je drukt met een vingerkracht van 5,0 N op de naald. Hoe groot is de druk onder de naaldpunt in N/cm²?",
      antwoord: "5000|5000 N/cm²|5.000|5.000 N/cm²",
      uitleg: "p = F / A = 5,0 N / 0,001 cm² = 5000 N/cm² (dat is maar liefst 50.000.000 Pa!)."
    },
    {
      type: "mc",
      vraag: "Waarom zak je met gewone schoenen diep weg in de sneeuw, maar blijf je met brede sneeuwschoenen op de sneeuw lopen?",
      opties: [
        "De zwaartekracht werkt niet op sneeuwschoenen",
        "Sneeuwschoenen maken je lichter",
        "Sneeuwschoenen smelten de sneeuw",
        "Sneeuwschoenen hebben een veel groter oppervlak (A), waardoor de druk (p = F/A) op de sneeuw veel kleiner is"
      ],
      antwoord: 3,
      uitleg: "Groter oppervlak A verdeelt dezelfde gewichtskracht F, waardoor de druk p onder de drempelwaarde van het sneeuwdek blijft."
    },
    {
      type: "waaronwaar",
      vraag: "Om een taart makkelijk door te snijden, moet het mes een zo breed en stomp mogelijk lemmet (groot oppervlak) hebben.",
      antwoord: false,
      uitleg: "Niet waar. Een stomp mes heeft een groot oppervlak waardoor de druk te klein is; een mes moet juist vlijmscherp (miniem oppervlak) zijn voor maximale druk.",
      uitleg: "Waar. Klein oppervlak A -> zeer hoge druk p."
    },
    {
      type: "mc",
      vraag: "Een olifant van 40.000 N staat op 4 poten. Elke poot heeft een voetoppervlak van 500 cm². Wat is de druk onder één poot in N/cm²?",
      opties: [
        "20 N/cm²",
        "80 N/cm²",
        "5 N/cm²",
        "200 N/cm²"
      ],
      antwoord: 0,
      uitleg: "Kracht per poot = 40.000 / 4 = 10.000 N. p = 10.000 N / 500 cm² = 20 N/cm²."
    },
    {
      type: "invul",
      vraag: "Een vrouw van 60 kg ( = 600\text{ N}$) staat op naaldhakken. Het oppervlak van één naaldhak is 0,5 cm². Als ze op één hak balanceert met al haar gewicht, hoe groot is dan de druk onder die hak in N/cm²?",
      antwoord: "1200|1200 N/cm²|1.200|1.200 N/cm²",
      uitleg: "p = 600 N / 0,5 cm² = 1200 N/cm² (veel groter dan de druk van de olifant!)."
    },
    {
      type: "waaronwaar",
      vraag: "Vloeistoffen zijn nauwelijks samendrukbaar, waardoor een uitgeoefende druk zich in een afgesloten vloeistofsysteem naar alle kanten onverminderd voortplant.",
      antwoord: true,
      uitleg: "Waar. Dit is de Wet van Pascal, het basisprincipe van hydraulische systemen."
    },
    {
      type: "mc",
      vraag: "Hoe werkt een <b>hydraulische krik of hefbrug</b>?",
      opties: [
        "Door luchtdruk uit de omgeving op te zuigen",
        "Door vloeistof onder druk van een kleine zuiger naar een grote zuiger te persen, waardoor de kracht evenredig met de oppervlakte toeneemt (F₂ = F₁ × A₂ / A₁)",
        "Door een grote veer uit te rekken",
        "Door magnetische afstoting van de vloeistof"
      ],
      antwoord: 1,
      uitleg: "Omdat de druk p overal gelijk is (p = F₁/A₁ = F₂/A₂), is de werkkracht op de grote zuiger zoveel malen groter als het oppervlak A₂/A₁."
    },
    {
      type: "invul",
      vraag: "In een hydraulische pers heeft zuiger 1 een oppervlakte van 4 cm² en zuiger 2 een oppervlakte van 80 cm². De oppervlakte van zuiger 2 is dus 20× zo groot. Als je op zuiger 1 duwt met een kracht van 50 N, welke hefkracht in Newton levert zuiger 2 dan?",
      antwoord: "1000|1000 N|1.000|1.000 N",
      uitleg: "F₂ = F₁ × (A₂ / A₁) = 50 N × (80 / 4) = 50 N × 20 = 1000 N."
    },
    {
      type: "mc",
      vraag: "Wat gebeurt er met de verplaatsing van de grote zuiger 2 in de vorige vraag als je de kleine zuiger 1 over een afstand van 10 cm omlaag duwt?",
      opties: [
        "Zuiger 2 gaat 200 cm omhoog",
        "Zuiger 2 gaat 10 cm omhoog",
        "Zuiger 2 gaat 0,5 cm omhoog (20 keer zo weinig)",
        "Zuiger 2 beweegt niet"
      ],
      antwoord: 2,
      uitleg: "Het verplaatste vloeistofvolume V = A × s blijft gelijk. s₂ = s₁ / 20 = 10 cm / 20 = 0,5 cm (Gouden regel!)."
    },
    {
      type: "waaronwaar",
      vraag: "Lucht is in tegenstelling tot hydraulische olie heel makkelijk samendrukbaar, daarom gebruikt men in remsystemen van auto's remolie en geen lucht.",
      antwoord: true,
      uitleg: "Waar. Als er luchtbellen in de remleiding zitten, veert het pedaal in zonder dat de remblokken direct bekrachtigd worden (gevaarlijk!)."
    },
    {
      type: "mc",
      vraag: "Waarom hebben zware landbouwtractoren en vrachtwagens in het bos hele brede lagedrukbanden?",
      opties: [
        "Dat is verplicht voor de kleur",
        "Om sneller te kunnen rijden op de snelweg",
        "Om minder brandstof te verbruiken op asfalt",
        "Om de druk op de zachte ondergrond te verkleinen, zodat de bodemstructuur niet wordt vernield en het voertuig niet vastrijdt in de modder"
      ],
      antwoord: 3,
      uitleg: "Groot bandoppervlak A -> lage bodemdruk p."
    },
    {
      type: "invul",
      vraag: "Een blok beton oefent een druk van 4000 Pa uit op de vloer. Het contactoppervlak met de vloer is 0,25 m². Hoe groot is het gewicht van het blok beton in Newton?",
      antwoord: "1000|1000 N|1.000|1.000 N",
      uitleg: "F = p × A = 4000 Pa × 0,25 m² = 1000 N."
    },
    {
      type: "mc",
      vraag: "Welke van de volgende voorbeelden is bedoeld om de <b>druk te VERGROTEN</b>?",
      opties: [
        "De scherpe punt van een spijker of injectienaald",
        "De brede rupsbanden van een graafmachine",
        "De brede bandjes van een zware rugzak",
        "Sneeuwschoenen"
      ],
      antwoord: 0,
      uitleg: "Scherpe punt = zeer klein oppervlak -> enorme druk om gemakkelijk ergens in te dringen."
    },
    {
      type: "waaronwaar",
      vraag: "Als je een rechthoekige baksteen op zijn smalle kant zet in plaats van op zijn platte kant, wordt de druk op de tafel kleiner omdat het gewicht gelijk blijft.",
      antwoord: false,
      uitleg: "Niet waar. Het gewicht blijft gelijk, maar het contactoppervlak A is veel kleiner op de smalle kant. Daardoor wordt de druk (p = F/A) juist groter!",
      uitleg: "Waar. Het gewicht F blijft gelijk, maar het contactoppervlak A is kleiner, dus p = F / A neemt toe."
    },
    {
      type: "open",
      vraag: "Leg het werkingsprincipe van een <b>hydraulisch remsysteem</b> in een auto uit. Vertel wat er gebeurt vanaf het intrappen van het rempedaal tot het klemmen van de remblokken op de wielen.",
      sleutelwoorden: ["rempedaal duwt kleine zuiger in de hoofdremcilinder", "druk plant zich via de remvloeistof gelijkmatig voort", "grotere zuigers bij de wielen drukken met grote kracht de remblokken vast"],
      minTreffers: 2,
      modelantwoord: "1. Wanneer de bestuurder op het rempedaal trapt, duwt een hefboom een kleine zuiger in de hoofdremcilinder naar binnen. 2. De remvloeistof (remolie) wordt samengeperst; omdat vloeistoffen niet samendrukbaar zijn, plant deze druk zich ogenblikkelijk en gelijkmatig door alle remleidingen voort naar de wielen. 3. Bij de wielen duwt de vloeistofdruk tegen grotere wielremcilinders (remklauwen). Doordat deze zuigers een groter oppervlak hebben, ontstaat er een sterk vergrote klemkracht waarmee de remblokken tegen de remschijven worden gedrukt om de auto af te remmen.",
      uitleg: "Hydraulische krachtvergroting in voertuigremmen."
    },
    {
      type: "open",
      vraag: "Een bergwandelaar van 80 kg zakt met zijn wandelschoenen (totaal oppervlak  = 400\text{ cm}^2$) diep weg in het zachte ijs. Hij besluit sneeuwschoenen onder te binden (totaal oppervlak  = 2000\text{ cm}^2$). Bereken voor beide situaties de druk in N/cm² en leg uit waarom hij nu niet meer wegzakt. (neem g = 10 N/kg)",
      sleutelwoorden: ["F = 800 N", "p_schoenen = 800 / 400 = 2,0 N/cm²", "p_sneeuwschoenen = 800 / 2000 = 0,4 N/cm²", "druk is 5x zo klein geworden"],
      minTreffers: 3,
      modelantwoord: "Gewicht wandelaar:  = m \times g = 80\text{ kg} \times 10\text{ N/kg} = 800\text{ N}$. 1. Met gewone wandelschoenen:  = F / A = 800\text{ N} / 400\text{ cm}^2 = 2{,}0\text{ N/cm}^2$ (oftewel 0.000\text{ Pa}$). 2. Met sneeuwschoenen:  = F / A = 800\text{ N} / 2000\text{ cm}^2 = 0{,}4\text{ N/cm}^2$ (oftewel 000\text{ Pa}$). Verklaring: Doordat het oppervlak met een factor 5 is vergroot, is de druk op de sneeuw met een factor 5 gedaald van 2,0 naar 0,4 N/cm². Deze druk is lager dan de draagkracht van het sneeuwdek, waardoor hij niet meer wegzakt.",
      uitleg: "Drukberekening en vergelijking bij sneeuwschoenen."
    }
  ]
});

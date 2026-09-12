import json
import os
import subprocess

from generate_h1_natuurkunde_exams import validate_exam

exam_1 = {
  "id": "ex-h3-natuurkunde-1",
  "hoofdstuk": 1,
  "titel": "Toets 1 — Begrippen, Formules & Basiskennis (§1.1, §1.2 & §1.3)",
  "vak": "Natuurkunde · HAVO 3 (H1)",
  "icoon": "🎯",
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
      "uitleg": "Kracht wordt in het SI-stelsel gemeten in Newton (N). Joule is de eenheid voor energie en arbeid, Watt voor vermogen en kilogram voor massa."
    },
    {
      "type": "mc",
      "vraag": "Welk meetinstrument gebruik je in het natuurkundelokaal om rechtstreeks een trekkracht te meten?",
      "opties": [
        "Een voltmeter",
        "Een dynamometer (veerkrachtmeter)",
        "Een barometer",
        "Een chronometer"
      ],
      "antwoord": 1,
      "uitleg": "Een dynamometer bevat een spiraalveer die uitrekt als er een kracht op werkt. Op de schaalverdeling lees je de kracht rechtstreeks af in Newton."
    },
    {
      "type": "mc",
      "vraag": "Wat stelt het symbool <b>v</b> voor in natuurkundige formules en welke SI-eenheid hoort hier standaard bij?",
      "opties": [
        "Versnelling in m/s²",
        "Vermogen in Watt",
        "Snelheid in m/s",
        "Verplaatsing in km"
      ],
      "antwoord": 2,
      "uitleg": "Het symbool v staat voor snelheid (van het Latijnse velocitas). De standaard SI-eenheid van snelheid is meter per seconde (m/s)."
    },
    {
      "type": "mc",
      "vraag": "Hoe noem je een beweging waarbij de snelheid iedere seconde met exact dezelfde hoeveelheid toeneemt?",
      "opties": [
        "Een eenparige beweging",
        "Een eenparig vertraagde beweging",
        "Een niet-eenparige beweging",
        "Een eenparig versnelde beweging"
      ],
      "antwoord": 3,
      "uitleg": "Als de snelheid elke seconde met een vaste hoeveelheid stijgt, is de versnelling constant. Dit heet een eenparig versnelde beweging."
    },
    {
      "type": "mc",
      "vraag": "Wat gebeurt er met de toestand van een voorwerp wanneer de resulterende kracht gelijk is aan 0 N ($F_{res} = 0\\text{ N}$)?",
      "opties": [
        "De snelheid en bewegingsrichting blijven onveranderd (constante snelheid of stilstand)",
        "Het voorwerp komt altijd direct tot stilstand",
        "Het voorwerp begint direct te versnellen",
        "De massa van het voorwerp neemt geleidelijk af"
      ],
      "antwoord": 0,
      "uitleg": "Als alle krachten elkaar opheffen ($F_{res} = 0\\text{ N}$), verandert er niets aan de snelheid. Een stilstaand voorwerp blijft stilstaan en een bewegend voorwerp behoudt zijn constante snelheid (eenparige beweging)."
    },
    {
      "type": "mc",
      "vraag": "Wat geeft de <b>steilheid (helling)</b> van de grafieklijn aan in een <b>(s,t)-diagram</b>?",
      "opties": [
        "De versnelling van het voorwerp",
        "De snelheid van het voorwerp",
        "De uitgeoefende wrijvingskracht",
        "De totale verstreken tijdsduur"
      ],
      "antwoord": 1,
      "uitleg": "In een (s,t)-diagram staat afstand verticaal en tijd horizontaal. De helling $\\Delta s / \\Delta t$ is gelijk aan de snelheid: hoe steiler de lijn, hoe groter de snelheid."
    },
    {
      "type": "mc",
      "vraag": "Welke twee tegenwerkende weerstandskrachten werken samen als totale tegenkracht op een rijdende fietser?",
      "opties": [
        "De zwaartekracht en de normaalkracht",
        "De motorkracht en de spierkracht",
        "De luchtweerstand en de rolweerstand",
        "De spankracht en de veerkracht"
      ],
      "antwoord": 2,
      "uitleg": "Op een rijdende fietser werken horizontaal twee weerstandskrachten tegen: de luchtweerstand (wrijving met de lucht) en de rolweerstand (vervorming van band en wegdek)."
    },
    {
      "type": "mc",
      "vraag": "Welke formule geeft de Tweede wet van Newton correct weer?",
      "opties": [
        "v = s / t",
        "s = v × t",
        "a = Δv / t",
        "Fres = m × a"
      ],
      "antwoord": 3,
      "uitleg": "De tweede wet van Newton luidt $F_{res} = m \\cdot a$: de resulterende kracht (in N) is gelijk aan de massa (in kg) vermenigvuldigd met de versnelling (in m/s²)."
    },
    {
      "type": "mc",
      "vraag": "Hoe reken je een snelheid in kilometer per uur (km/h) correct om naar meter per seconde (m/s)?",
      "opties": [
        "Delen door 3,6",
        "Vermenigvuldigen met 3,6",
        "Delen door 60",
        "Vermenigvuldigen met 10"
      ],
      "antwoord": 0,
      "uitleg": "Omdat 1 uur 3600 seconden heeft en 1 km 1000 meter is, geldt: $1\\text{ m/s} = 3,6\\text{ km/h}$. Omrekenen van km/h naar m/s doe je dus door te delen door 3,6."
    },
    {
      "type": "mc",
      "vraag": "Hoe heet de eigenschap van materie waardoor een voorwerp zich verzet tegen iedere verandering van zijn snelheid of bewegingsrichting?",
      "opties": [
        "Veerkracht",
        "Traagheid (inertie)",
        "Elasticiteit",
        "Zwaartekracht"
      ],
      "antwoord": 1,
      "uitleg": "Massa bezit traagheid (of inertie). Een zwaar voorwerp verzet zich sterker tegen snelheidsveranderingen dan een licht voorwerp."
    },
    {
      "type": "mc",
      "vraag": "Hoe kun je in een <b>(v,t)-diagram</b> de totale afgelegde afstand bepalen?",
      "opties": [
        "Door de helling van de lijn te berekenen",
        "Door de eindsnelheid te delen door de verstreken tijd",
        "Door de oppervlakte onder de grafieklijn te berekenen",
        "Door de gemiddelde versnelling te vermenigvuldigen met de massa"
      ],
      "antwoord": 2,
      "uitleg": "De oppervlakte onder de (v,t)-grafiek heeft als eenheid $\\text{m/s} \\times \\text{s} = \\text{meter}$. De oppervlakte stelt dus de afgelegde afstand $s$ voor."
    },
    {
      "type": "mc",
      "vraag": "Wat is de officiële eenheid van <b>versnelling (a)</b> in het SI-stelsel?",
      "opties": [
        "m/s",
        "km/h",
        "N/kg",
        "m/s²"
      ],
      "antwoord": 3,
      "uitleg": "Versnelling is de snelheidsverandering per seconde: $(\\text{m/s}) / \\text{s} = \\text{m/s}^2$ (meter per seconde kwadraat)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een raceauto die met een constante snelheid van 240 km/h over een recht stuk rijdt, ondervindt een resulterende kracht van exact 0 N.",
      "antwoord": True,
      "uitleg": "Waar. Omdat de snelheid constant is en de auto in een rechte lijn rijdt, is er geen versnelling ($a = 0$). Volgens $F_{res} = m \\cdot a$ is de resulterende kracht dan precies 0 N."
    },
    {
      "type": "waaronwaar",
      "vraag": "In een (s,t)-diagram betekent een horizontale rechte lijn dat het voorwerp met een constante, gelijkmatige snelheid beweegt.",
      "antwoord": False,
      "uitleg": "Niet waar. In een (s,t)-diagram betekent een horizontale lijn dat de afstand niet verandert in de tijd: het voorwerp staat dus stil ($v = 0\\text{ m/s}$)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Volgens de formule $F_{res} = m \\cdot a$ krijgt een voorwerp met een twee keer zo grote massa bij dezelfde kracht een twee keer zo kleine versnelling.",
      "antwoord": True,
      "uitleg": "Waar. De versnelling is omgekeerd evenredig met de massa ($a = F_{res} / m$). Hoe zwaarder het voorwerp, hoe kleiner de versnelling bij gelijke kracht."
    },
    {
      "type": "waaronwaar",
      "vraag": "Om een snelheid van meter per seconde (m/s) om te rekenen naar kilometer per uur (km/h) moet je de waarde delen door 3,6.",
      "antwoord": False,
      "uitleg": "Niet waar. Van m/s naar km/h moet je juist vermenigvuldigen met 3,6 (bijvoorbeeld $10\\text{ m/s} = 36\\text{ km/h}$)."
    },
    {
      "type": "invul",
      "vraag": "Reken om: een stadsbus rijdt met een constante snelheid van <b>54 km/h</b>. Hoeveel meter per seconde (m/s) is dat?",
      "antwoord": "15|15 m/s|15,0|15,0 m/s",
      "uitleg": "Om te rekenen van km/h naar m/s deel je door 3,6: $54 / 3,6 = 15\\text{ m/s}$."
    },
    {
      "type": "invul",
      "vraag": "Welke eenheid hoort bij de versnelling in de formule $a = \\Delta v / t$? Typ het symbool (zoals m/s²).",
      "antwoord": "m/s2|m/s^2|m/s²",
      "uitleg": "De eenheid van versnelling is meter per seconde kwadraat, genoteerd als m/s² of m/s^2."
    },
    {
      "type": "open",
      "vraag": "Leg uit wat er wordt bedoeld met de 'resulterende kracht' (of somkracht) als er tegelijkertijd meerdere krachten op een voorwerp werken.",
      "sleutelwoorden": [
        "alle krachten samen/som van de krachten/optelsom",
        "hetzelfde effect/vervangende kracht"
      ],
      "minTreffers": 1,
      "modelantwoord": "De resulterende kracht is de som van alle afzonderlijke krachten die op een voorwerp werken. Deze ene denkbeeldige kracht heeft precies hetzelfde effect op de beweging als alle losse krachten bij elkaar.",
      "uitleg": "De resulterende kracht vervangt alle afzonderlijke krachten en bepaalt de uiteindelijke versnelling of vertraging van het voorwerp."
    },
    {
      "type": "open",
      "vraag": "Waarom kost het aanzienlijk meer spierkracht om een zware bakfiets op gang te brengen dan een lichte racefiets? Benoem het natuurkundige verschijnsel.",
      "sleutelwoorden": [
        "traagheid/inertie",
        "grotere massa/veel massa"
      ],
      "minTreffers": 1,
      "modelantwoord": "Een bakfiets heeft een veel grotere massa dan een racefiets. Door de grotere traagheid (inertie) verzet de bakfiets zich veel sterker tegen een verandering van snelheid. Volgens $F = m \\cdot a$ is er daardoor een grotere kracht nodig om dezelfde versnelling te krijgen.",
      "uitleg": "Massa bezit traagheid: hoe groter de massa, des te meer kracht nodig is om het voorwerp op gang te brengen."
    }
  ]
}

exam_2 = {
  "id": "ex-h3-natuurkunde-2",
  "hoofdstuk": 1,
  "titel": "Toets 2 — Krachten, Weerstand & Resulterende Kracht (Mix §1.1 t/m §1.3)",
  "vak": "Natuurkunde · HAVO 3 (H1)",
  "icoon": "🏎️",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Een personenauto rijdt op de weg. De motor levert een voorwaartse kracht van 1400 N. De tegenwerkende luchtweerstand is 900 N en de rolweerstand is 300 N. Hoe groot is de resulterende kracht en wat gebeurt er?",
      "opties": [
        "200 N naar voren; de auto versnelt",
        "200 N naar achteren; de auto vertraagt",
        "1200 N naar voren; de auto rijdt met constante snelheid",
        "0 N; de auto staat stil"
      ],
      "antwoord": 0,
      "uitleg": "De totale tegenkracht is $900 + 300 = 1200\\text{ N}$. $F_{res} = F_{motor} - F_{tegen} = 1400 - 1200 = 200\\text{ N}$ naar voren. Omdat $F_{res} > 0$ in de rijrichting is, versnelt de auto."
    },
    {
      "type": "mc",
      "vraag": "Twee sleepboten trekken in exact dezelfde richting aan een containerschip. Boot A trekt met 25 kN en boot B trekt met 35 kN. Hoe groot is de totale resulterende trekkracht op het schip?",
      "opties": [
        "10 kN",
        "60 kN",
        "30 kN",
        "70 kN"
      ],
      "antwoord": 1,
      "uitleg": "Krachten die in dezelfde richting werken, mag je bij elkaar optellen: $25\\text{ kN} + 35\\text{ kN} = 60\\text{ kN}$."
    },
    {
      "type": "mc",
      "vraag": "Waardoor wordt de luchtweerstand van een rijdend voertuig in de praktijk vooral veel groter?",
      "opties": [
        "Door zachtere autobanden te monteren",
        "Door het voertuig zwaarder te beladen",
        "Door sneller te gaan rijden of een minder gestroomlijnde vorm te hebben",
        "Door op een nat wegdek te rijden"
      ],
      "antwoord": 2,
      "uitleg": "Luchtweerstand hangt sterk af van de snelheid (kwadratisch) en het frontale oppervlak/stroomlijn. Hoe harder je rijdt, hoe meer luchtmoleculen per seconde weggeduwd moeten worden."
    },
    {
      "type": "mc",
      "vraag": "Een wielrenster fietst met een constante snelheid van 36 km/h. De totale tegenwerkende weerstandskracht is 65 N. Hoe groot is de voorwaartse spierkracht die zij uitoefent?",
      "opties": [
        "0 N",
        "130 N",
        "32,5 N",
        "65 N"
      ],
      "antwoord": 3,
      "uitleg": "Bij een constante snelheid is de versnelling nul, waardoor de resulterende kracht 0 N moet zijn. De voorwaartse trapkracht moet daarom precies gelijk zijn aan de totale tegenkracht: 65 N."
    },
    {
      "type": "mc",
      "vraag": "Een parachutist zweeft na het openen van de parachute met een constante snelheid recht naar beneden. Wat geldt er voor de zwaartekracht ($F_z$) en de opwaartse luchtweerstand ($F_l$)?",
      "opties": [
        "Fl is exact even groot als Fz, waardoor de resulterende kracht 0 N is",
        "Fz is veel groter dan Fl",
        "Fl is groter dan Fz waardoor hij omhoog beweegt",
        "Er werkt helemaal geen zwaartekracht meer op de parachutist"
      ],
      "antwoord": 0,
      "uitleg": "Bij constante daalsnelheid heffen de opwaartse luchtweerstand en de neerwaartse zwaartekracht elkaar volledig op ($F_{res} = 0\\text{ N}$)."
    },
    {
      "type": "mc",
      "vraag": "Wanneer een automobilist op een vlakke weg het gaspedaal loslaat en niet remt, rolt de auto uit. Welke kracht zorgt ervoor dat de auto afremt?",
      "opties": [
        "De motorkracht",
        "De tegenwerkende rol- en luchtweerstandskracht",
        "De zwaartekracht",
        "De normaalkracht van het wegdek"
      ],
      "antwoord": 1,
      "uitleg": "Omdat de motor geen voorwaartse kracht meer levert, werken alleen de rolweerstand en luchtweerstand tegen de bewegingsrichting in. Hierdoor ontstaat een vertraging."
    },
    {
      "type": "mc",
      "vraag": "Twee groepen spelen touwtrekken. Groep Blauw trekt naar links met 520 N. Groep Rood trekt naar rechts met 480 N. Wat is de resulterende kracht?",
      "opties": [
        "1000 N naar rechts",
        "40 N naar rechts",
        "40 N naar links",
        "0 N"
      ],
      "antwoord": 2,
      "uitleg": "Tegengestelde krachten trek je van elkaar af: $520\\text{ N} - 480\\text{ N} = 40\\text{ N}$. De richting is naar de kant van de grootste kracht, dus naar links."
    },
    {
      "type": "mc",
      "vraag": "Welke handeling zorgt voor een merkbare verlaging van de <b>rolweerstand</b> van een fiets?",
      "opties": [
        "Een strakke aerodynamische jas dragen",
        "Het spatbord en de kettingkast demonteren",
        "Diep voorovergebogen over het stuur gaan liggen",
        "De fietsbanden oppompen tot de aanbevolen maximale druk"
      ],
      "antwoord": 3,
      "uitleg": "Harde banden vervormen veel minder tijdens het rollen over het wegdek, waardoor de rolweerstand aanzienlijk afneemt."
    },
    {
      "type": "mc",
      "vraag": "Een scooter met bestuurder (totale massa 120 kg) trekt op met een versnelling van 1,5 m/s². Hoe groot is de resulterende kracht die op de scooter werkt?",
      "opties": [
        "180 N",
        "80 N",
        "120 N",
        "270 N"
      ],
      "antwoord": 0,
      "uitleg": "$F_{res} = m \\times a = 120\\text{ kg} \\times 1,5\\text{ m/s}^2 = 180\\text{ N}$."
    },
    {
      "type": "mc",
      "vraag": "Bij de wintersport curling vegen teamgenoten het ijs fanatiek vlak vóór de glijdende curlingsteen. Wat is het natuurkundige doel hiervan?",
      "opties": [
        "De massa van de steen tijdelijk verkleinen",
        "De wrijvingskracht verkleinen zodat de steen minder vertraagt en verder glijdt",
        "Een extra voorwaartse luchtdruk opwekken",
        "De zwaartekracht op de steen verminderen"
      ],
      "antwoord": 1,
      "uitleg": "Door het vegen smelt het ijs heel licht en ontstaat een dun waterlaagje dat de schuifwrijving sterk verlaagt, zodat de steen minder snel afremt."
    },
    {
      "type": "mc",
      "vraag": "Een voorwerp met een massa van 40 kg ondervindt een voorwaartse kracht van 300 N en een tegenkracht van 100 N. Wat is de versnelling van het voorwerp?",
      "opties": [
        "10 m/s²",
        "7,5 m/s²",
        "5,0 m/s²",
        "2,5 m/s²"
      ],
      "antwoord": 2,
      "uitleg": "Eerst $F_{res} = 300 - 100 = 200\\text{ N}$. Vervolgens $a = F_{res} / m = 200 / 40 = 5,0\\text{ m/s}^2$."
    },
    {
      "type": "mc",
      "vraag": "Wat gebeurt er met de resulterende kracht als een fietser vanuit stilstand steeds sneller gaat fietsen terwijl hij met een constante trapkracht blijft duwen?",
      "opties": [
        "De resulterende kracht blijft exact gelijk",
        "De resulterende kracht wordt steeds groter",
        "De resulterende kracht springt direct naar nul",
        "De resulterende kracht wordt steeds kleiner doordat de luchtweerstand toeneemt"
      ],
      "antwoord": 3,
      "uitleg": "Als de fietser versnelt, neemt de luchtweerstand toe. Omdat de spierkracht gelijk blijft en de tegenkracht groeit, wordt $F_{res} = F_{spier} - F_{tegen}$ steeds kleiner totdat $F_{res} = 0$ bij topsnelheid."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als de voorwaartse motorkracht kleiner is dan de totale weerstandskracht ($F_{motor} < F_{tegen}$), is de beweging van een auto vertraagd.",
      "antwoord": True,
      "uitleg": "Waar. De resulterende kracht werkt dan tegen de bewegingsrichting in, waardoor de auto snelheid verliest (vertraging)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een voorwerp dat met een constante snelheid beweegt, heeft altijd een resulterende kracht die groter is dan nul in de bewegingsrichting.",
      "antwoord": False,
      "uitleg": "Niet waar. Bij een constante snelheid is de versnelling nul, en dus is de resulterende kracht altijd exact 0 N."
    },
    {
      "type": "waaronwaar",
      "vraag": "Rolweerstand ontstaat doordat de banden van een voertuig en het wegdek tijdens het rijden voortdurend een beetje indeuken en vervormen.",
      "antwoord": True,
      "uitleg": "Waar. Deze voortdurende vervorming kost energie en veroorzaakt de rolweerstandskracht."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als twee krachten van 50 N in precies tegengestelde richting op hetzelfde voorwerp werken, is de somkracht 100 N.",
      "antwoord": False,
      "uitleg": "Niet waar. Omdat ze tegengesteld gericht zijn trek je ze af: $50 - 50 = 0\\text{ N}$. Ze heffen elkaar op."
    },
    {
      "type": "invul",
      "vraag": "Een vrachtwagen met een massa van 8000 kg ondervindt een resulterende kracht van 16.000 N. Bereken de versnelling in m/s².",
      "antwoord": "2|2,0|2 m/s2|2 m/s²|2,0 m/s2|2,0 m/s²",
      "uitleg": "$a = F_{res} / m = 16.000 / 8000 = 2,0\\text{ m/s}^2$."
    },
    {
      "type": "invul",
      "vraag": "Een wielrenner levert 140 N voorwaartse trapkracht. De rolweerstand is 25 N. Als hij met constante snelheid rijdt, hoe groot is dan de luchtweerstand in Newton?",
      "antwoord": "115|115 N|115,0|115,0 N",
      "uitleg": "Bij constante snelheid is $F_{res} = 0$, dus $F_{spier} = F_{rol} + F_{lucht}$. $140 = 25 + F_{lucht} \\implies F_{lucht} = 115\\text{ N}$."
    },
    {
      "type": "open",
      "vraag": "Waarom neemt de topsnelheid van een auto nauwelijks toe als je het motorvermogen verdubbelt? Leg uit wat er met de tegenkracht gebeurt bij hogere snelheden.",
      "sleutelwoorden": [
        "luchtweerstand",
        "kwadratisch/sterk toeneemt/veel groter wordt"
      ],
      "minTreffers": 1,
      "modelantwoord": "Bij hogere snelheden neemt de luchtweerstand heel sterk toe (kwadratisch met de snelheid). Om nog een klein beetje sneller te kunnen rijden, moet de motor tegen een enorm toegenomen luchtweerstand opboksen.",
      "uitleg": "De luchtweerstand groeit zeer snel bij hoge snelheid, waardoor een verdubbeling van de motorkracht maar een bescheiden snelheidswinst oplevert."
    },
    {
      "type": "open",
      "vraag": "Een zware doos staat stil op de vloer. Je duwt horizontaal tegen de doos, maar deze komt niet van zijn plek. Wat kun je concluderen over de grootte en richting van de wrijvingskracht ten opzichte van jouw duwkracht?",
      "sleutelwoorden": [
        "even groot/dezelfde grootte/gelijk",
        "tegengestelde richting/tegengesteld gericht",
        "heffen elkaar op/resulterende kracht nul"
      ],
      "minTreffers": 2,
      "modelantwoord": "De wrijvingskracht is precies even groot als jouw duwkracht, maar werkt in tegengestelde richting. Omdat de doos stil blijft staan is de versnelling nul, waardoor beide krachten elkaar opheffen en de resulterende kracht 0 N is.",
      "uitleg": "Bij stilstand is de statische wrijving exact gelijk en tegengesteld aan de duwkracht."
    }
  ]
}

exam_3 = {
  "id": "ex-h3-natuurkunde-3",
  "hoofdstuk": 1,
  "titel": "Toets 3 — Snelheid, Bewegingen & Diagrammen (Mix §1.1 t/m §1.3)",
  "vak": "Natuurkunde · HAVO 3 (H1)",
  "icoon": "📈",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Een hardloopster legt een afstand van 1500 meter af in 5,0 minuten (300 seconden). Wat is haar gemiddelde snelheid in m/s?",
      "opties": [
        "5,0 m/s",
        "3,0 m/s",
        "6,0 m/s",
        "15 m/s"
      ],
      "antwoord": 0,
      "uitleg": "$v_{gem} = s / t = 1500\\text{ m} / 300\\text{ s} = 5,0\\text{ m/s}$."
    },
    {
      "type": "mc",
      "vraag": "In een (s,t)-diagram zie je een lijn die vanaf de oorsprong steeds steiler omhoog buigt. Wat voor beweging stelt deze kromme lijn voor?",
      "opties": [
        "Een eenparige beweging met constante snelheid",
        "Een versnelde beweging",
        "Een eenparig vertraagde beweging",
        "Een voorwerp in rust"
      ],
      "antwoord": 1,
      "uitleg": "De helling in een (s,t)-diagram is de snelheid. Als de grafiek steeds steiler wordt, neemt de snelheid toe: de beweging is dus versneld."
    },
    {
      "type": "mc",
      "vraag": "Max rijdt op het circuit van Zandvoort (lengte 4259 m) een ronde in 1 minuut en 10,0 seconden (70,0 s). Wat is zijn gemiddelde snelheid in m/s afgerond op één decimaal?",
      "opties": [
        "42,6 m/s",
        "52,1 m/s",
        "60,8 m/s",
        "71,0 m/s"
      ],
      "antwoord": 2,
      "uitleg": "$v_{gem} = s / t = 4259 / 70,0 = 60,84... \\approx 60,8\\text{ m/s}$ (dat is ongeveer $219\\text{ km/h}$!)."
    },
    {
      "type": "mc",
      "vraag": "Wat zie je in een (v,t)-diagram als een automobilist gedurende 10 seconden stilstaat voor een rood stoplicht?",
      "opties": [
        "Een verticale streep omhoog",
        "Een schuin dalende rechte lijn",
        "Een horizontale lijn op een hoogte van 10 m/s",
        "Een horizontale lijn op de tijdas waar v = 0 m/s"
      ],
      "antwoord": 3,
      "uitleg": "Bij stilstand is de snelheid 0 m/s. In een (v,t)-diagram zie je dan een horizontale lijn die precies op de horizontale as ($v = 0$) ligt."
    },
    {
      "type": "mc",
      "vraag": "In een (v,t)-diagram stijgt de snelheid van een scooter vanuit stilstand in 4,0 s gelijkmatig naar 12 m/s. Hoeveel meter legt de scooter af in die 4,0 seconden?",
      "opties": [
        "24 m",
        "48 m",
        "12 m",
        "36 m"
      ],
      "antwoord": 0,
      "uitleg": "De oppervlakte van de driehoek onder de grafiek is: $\\text{oppervlakte} = 0,5 \\times \\text{basis} \\times \\text{hoogte} = 0,5 \\times 4,0\\text{ s} \\times 12\\text{ m/s} = 24\\text{ m}$ (of via $v_{gem} = 6\\text{ m/s} \\times 4\\text{ s} = 24\\text{ m}$)."
    },
    {
      "type": "mc",
      "vraag": "Een fietser fietst 10 minuten (600 seconden) met een constante snelheid van 18 km/h (5,0 m/s). Welke afstand legt hij af?",
      "opties": [
        "1800 m",
        "3000 m",
        "600 m",
        "5000 m"
      ],
      "antwoord": 1,
      "uitleg": "$s = v \\times t = 5,0\\text{ m/s} \\times 600\\text{ s} = 3000\\text{ m}$ (oftewel 3 km)."
    },
    {
      "type": "mc",
      "vraag": "In een (s,t)-diagram loopt een rechte lijn van t = 0 tot t = 5,0 s van s = 0 naar s = 25 m. Hoe groot is de snelheid tijdens dit interval?",
      "opties": [
        "125 m/s",
        "0,20 m/s",
        "5,0 m/s",
        "20 m/s"
      ],
      "antwoord": 2,
      "uitleg": "$v = \\Delta s / \\Delta t = (25 - 0) / (5,0 - 0) = 5,0\\text{ m/s}$."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent het als de grafieklijn in een (v,t)-diagram een rechte lijn schuin naar beneden is?",
      "opties": [
        "De afgelegde afstand neemt af",
        "Het voorwerp rijdt achteruit",
        "De versnelling van het voorwerp neemt toe",
        "De beweging is eenparig vertraagd (constante vertraging)"
      ],
      "antwoord": 3,
      "uitleg": "Een rechte dalende lijn in een (v,t)-diagram betekent dat de snelheid iedere seconde met dezelfde hoeveelheid afneemt. Dit is een eenparig vertraagde beweging."
    },
    {
      "type": "mc",
      "vraag": "Een sprinter loopt met een constante snelheid van 10 m/s gedurende 6,0 seconden. Welke oppervlaktevorm hoort hierbij in het (v,t)-diagram en wat is de afstand?",
      "opties": [
        "Een rechthoek van 10 bij 6; afstand is 60 m",
        "Een driehoek van 10 bij 6; afstand is 30 m",
        "Een cirkelsector; afstand is 36 m",
        "Een trapezium; afstand is 80 m"
      ],
      "antwoord": 0,
      "uitleg": "Bij constante snelheid is de lijn horizontaal. De oppervlakte onder de lijn is een rechthoek: $\\text{basis} \\times \\text{hoogte} = 6,0\\text{ s} \\times 10\\text{ m/s} = 60\\text{ meter}$."
    },
    {
      "type": "mc",
      "vraag": "Twee wandelaars lopen op hetzelfde pad. In het (s,t)-diagram loopt de lijn van wandelaar A steiler dan die van wandelaar B. Welke conclusie is juist?",
      "opties": [
        "Wandelaar B loopt met een grotere snelheid dan wandelaar A",
        "Wandelaar A loopt met een grotere snelheid dan wandelaar B",
        "Beide wandelaars lopen met exact dezelfde snelheid",
        "Wandelaar A staat stil"
      ],
      "antwoord": 1,
      "uitleg": "De helling van de lijn in een (s,t)-diagram geeft de snelheid aan. Hoe steiler de lijn, hoe groter de snelheid."
    },
    {
      "type": "mc",
      "vraag": "Een auto rijdt met 72 km/h (20 m/s). Voor een stopbord remt de auto in 4,0 seconden gelijkmatig af tot stilstand (0 m/s). Wat is de gemiddelde snelheid tijdens het remmen?",
      "opties": [
        "20 m/s",
        "15 m/s",
        "10 m/s",
        "5,0 m/s"
      ],
      "antwoord": 2,
      "uitleg": "Bij een eenparige vertraging is de gemiddelde snelheid precies het midden tussen begin- en eindsnelheid: $v_{gem} = (20 + 0) / 2 = 10\\text{ m/s}$."
    },
    {
      "type": "mc",
      "vraag": "Wat is het belangrijkste verschil tussen een (s,t)-diagram en een (v,t)-diagram van dezelfde eenparige beweging?",
      "opties": [
        "In het (s,t)-diagram is de lijn horizontaal en in het (v,t)-diagram schuin omhoog",
        "Er is geen enkel verschil tussen beide diagrammen",
        "In beide diagrammen zie je altijd een stijgende kromme lijn",
        "In het (s,t)-diagram zie je een schuine rechte lijn en in het (v,t)-diagram een horizontale lijn"
      ],
      "antwoord": 3,
      "uitleg": "Bij constante snelheid neemt de afstand gelijkmatig toe (schuine rechte lijn in s,t), terwijl de snelheid constant blijft (horizontale rechte lijn in v,t)."
    },
    {
      "type": "waaronwaar",
      "vraag": "De oppervlakte onder de grafiek in een (v,t)-diagram heeft als eenheid meters (m) en stelt de afgelegde afstand voor.",
      "antwoord": True,
      "uitleg": "Waar. Vermenigvuldig je de eenheid van de verticale as (m/s) met die van de horizontale as (s), dan krijg je $\\text{m/s} \\times \\text{s} = \\text{m}$ (meter)."
    },
    {
      "type": "waaronwaar",
      "vraag": "In een (s,t)-diagram kun je de afgelegde afstand berekenen door de oppervlakte onder de grafieklijn te bepalen.",
      "antwoord": False,
      "uitleg": "Niet waar. In een (s,t)-diagram lees je de afstand rechtstreeks af op de verticale as. Oppervlakte bepalen doe je alleen in een (v,t)-diagram."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een eenparig versnelde beweging vanuit stilstand heeft in een (s,t)-diagram een steeds steiler wordende kromme lijn en in een (v,t)-diagram een rechte stijgende lijn.",
      "antwoord": True,
      "uitleg": "Waar. In (s,t) wordt de helling (snelheid) steeds groter (paraboolvormig), terwijl in (v,t) de snelheid gelijkmatig toeneemt (rechte schuine lijn)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als de helling van de grafiek in een (v,t)-diagram gelijk is aan nul (een horizontale lijn), betekent dit dat het voorwerp stilstaat.",
      "antwoord": False,
      "uitleg": "Niet waar. Een horizontale lijn in een (v,t)-diagram betekent dat de snelheid constant is ($a = 0$). Het voorwerp staat alleen stil als die lijn op $v = 0$ ligt."
    },
    {
      "type": "invul",
      "vraag": "Reken om: een zwemmer zwemt met een snelheid van <b>2,5 m/s</b>. Hoeveel km/h is dat?",
      "antwoord": "9|9 km/h|9,0|9,0 km/h",
      "uitleg": "Van m/s naar km/h vermenigvuldig je met 3,6: $2,5 \\times 3,6 = 9,0\\text{ km/h}$."
    },
    {
      "type": "invul",
      "vraag": "Een speelgoedauto legt met constante snelheid een afstand van 18 meter af in 12 seconden. Bereken de snelheid in m/s.",
      "antwoord": "1,5|1,5 m/s",
      "uitleg": "$v = s / t = 18 / 12 = 1,5\\text{ m/s}$."
    },
    {
      "type": "open",
      "vraag": "Hoe kun je aan de vorm van de lijn in een (s,t)-diagram direct zien of een fietser sneller gaat rijden of juist afremt?",
      "sleutelwoorden": [
        "steiler/helling groter",
        "vlakker/helling kleiner"
      ],
      "minTreffers": 1,
      "modelantwoord": "Als de lijn steeds steiler omhoog buigt (de helling neemt toe), rijdt de fietser sneller (versnelling). Als de lijn afvlakt en minder steil wordt (de helling neemt af), remt de fietser af (vertraging).",
      "uitleg": "De steilheid van de grafiek in een (s,t)-diagram stelt de snelheid voor."
    },
    {
      "type": "open",
      "vraag": "Leg uit hoe je de totale afstand berekent van een beweging die in een (v,t)-diagram eerst 4 seconden eenparig versnelt van 0 naar 8 m/s en daarna 6 seconden met 8 m/s constant doorrijdt.",
      "sleutelwoorden": [
        "driehoek",
        "rechthoek"
      ],
      "minTreffers": 2,
      "modelantwoord": "Je berekent de oppervlakte onder de grafiek in twee delen: Deel 1 is een driehoek ($0,5 \\times 4\\text{ s} \\times 8\\text{ m/s} = 16\\text{ m}$). Deel 2 is een rechthoek ($6\\text{ s} \\times 8\\text{ m/s} = 48\\text{ m}$). De totale afstand is de optelsom: $16 + 48 = 64\\text{ meter}$.",
      "uitleg": "De totale afstand is de som van de oppervlaktes van de driehoek en de rechthoek."
    }
  ]
}

exam_4 = {
  "id": "ex-h3-natuurkunde-4",
  "hoofdstuk": 1,
  "titel": "Toets 4 — Versnelling, Massa & Wet van Newton (Mix §1.1 t/m §1.3)",
  "vak": "Natuurkunde · HAVO 3 (H1)",
  "icoon": "⚡",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Een sportauto trekt vanuit stilstand in 3,0 seconden op naar een snelheid van 27 m/s (bijna 100 km/h). Wat is de gemiddelde versnelling van de auto?",
      "opties": [
        "9,0 m/s²",
        "3,0 m/s²",
        "27 m/s²",
        "81 m/s²"
      ],
      "antwoord": 0,
      "uitleg": "$a = \\Delta v / \\Delta t = (27 - 0) / 3,0 = 9,0\\text{ m/s}^2$."
    },
    {
      "type": "mc",
      "vraag": "Een goederentrein heeft een massa van 50.000 kg. De locomotief levert een voorwaartse trekkracht van 40 kN (40.000 N) en de tegenwerkende wrijving is 5000 N. Hoe groot is de versnelling van de trein?",
      "opties": [
        "0,80 m/s²",
        "0,70 m/s²",
        "0,90 m/s²",
        "1,4 m/s²"
      ],
      "antwoord": 1,
      "uitleg": "$F_{res} = 40.000 - 5000 = 35.000\\text{ N}$. $a = F_{res} / m = 35.000 / 50.000 = 0,70\\text{ m/s}^2$."
    },
    {
      "type": "mc",
      "vraag": "Een skateboarder rijdt met 16 m/s en remt in 4,0 seconden gelijkmatig af tot stilstand (0 m/s). Wat is zijn versnelling (vertraging)?",
      "opties": [
        "4,0 m/s²",
        "0,25 m/s²",
        "-4,0 m/s²",
        "-16 m/s²"
      ],
      "antwoord": 2,
      "uitleg": "$a = (v_{eind} - v_{begin}) / t = (0 - 16) / 4,0 = -4,0\\text{ m/s}^2$. Het minteken geeft aan dat het een vertraging is."
    },
    {
      "type": "mc",
      "vraag": "Andy Green verbrak het wereldsnelheidsrecord op land met de straalwagen ThrustSSC. Waarom was ondanks de enorme straalmotoren een zeer lange woestijnbaan nodig?",
      "opties": [
        "Omdat straalmotoren alleen werken bij temperaturen boven 40 graden",
        "Omdat de raketauto geen wielen had",
        "Omdat de massa van de wagen extreem klein was",
        "Omdat de zware wagen door zijn grote traagheid tijd en afstand nodig heeft om op topsnelheid te komen"
      ],
      "antwoord": 3,
      "uitleg": "Massa heeft traagheid: ook met gigantische stuwkracht kost het versnellen van een zware wagen naar 1228 km/h flink wat tijd en een lange aanloop."
    },
    {
      "type": "mc",
      "vraag": "Een lift met passagiers heeft een totale massa van 800 kg. De hijskabel trekt omhoog met 9600 N en de zwaartekracht naar beneden is 8000 N. Wat is de opwaartse versnelling van de lift?",
      "opties": [
        "2,0 m/s²",
        "1,2 m/s²",
        "9,6 m/s²",
        "12 m/s²"
      ],
      "antwoord": 0,
      "uitleg": "$F_{res} = 9600 - 8000 = 1600\\text{ N}$ omhoog. $a = F_{res} / m = 1600 / 800 = 2,0\\text{ m/s}^2$."
    },
    {
      "type": "mc",
      "vraag": "Waarom schuift een losliggende koffer in een plotseling krachtig remmende bus naar voren over de vloer?",
      "opties": [
        "Omdat er een geheimzinnige kracht naar voren op de koffer gaat werken",
        "Omdat de koffer door zijn traagheid zijn snelheid wil behouden terwijl de bus vertraagt",
        "Omdat de zwaartekracht plotseling naar voren kantelt",
        "Omdat de luchtdruk achterin de bus opeens sterk stijgt"
      ],
      "antwoord": 1,
      "uitleg": "Volgens het traagheidsbeginsel wil een voorwerp zijn snelheid en richting behouden. Als de bus remt, schiet de koffer door als er niet genoeg wrijving is."
    },
    {
      "type": "mc",
      "vraag": "Op een slee met een kind (totale massa 30 kg) werkt een resulterende kracht van 45 N. Hoe groot is de versnelling van de slee?",
      "opties": [
        "0,67 m/s²",
        "1350 m/s²",
        "1,5 m/s²",
        "3,0 m/s²"
      ],
      "antwoord": 2,
      "uitleg": "$a = F_{res} / m = 45 / 30 = 1,5\\text{ m/s}^2$."
    },
    {
      "type": "mc",
      "vraag": "Hoe kun je de formule $F_{res} = m \\cdot a$ omschrijven als je de massa ($m$) wilt berekenen?",
      "opties": [
        "m = Fres × a",
        "m = a / Fres",
        "m = Fres + a",
        "m = Fres / a"
      ],
      "antwoord": 3,
      "uitleg": "Deel beide kanten van de formule door $a$: $m = F_{res} / a$."
    },
    {
      "type": "mc",
      "vraag": "Een schaatser met een massa van 70 kg glijdt over het ijs en ondervindt een constante remmende wrijvingskracht van 14 N. Wat is de vertraging van de schaatser?",
      "opties": [
        "-0,20 m/s²",
        "-5,0 m/s²",
        "-0,50 m/s²",
        "-2,0 m/s²"
      ],
      "antwoord": 0,
      "uitleg": "$a = F_{res} / m = -14 / 70 = -0,20\\text{ m/s}^2$ (een vertraging van $0,20\\text{ m/s}^2$)."
    },
    {
      "type": "mc",
      "vraag": "Een kogel van 0,050 kg (50 gram) wordt in een loop versneld met een versnelling van 8000 m/s². Hoe groot is de kracht van de gassen op de kogel?",
      "opties": [
        "160.000 N",
        "400 N",
        "40 N",
        "80 N"
      ],
      "antwoord": 1,
      "uitleg": "$F = m \\times a = 0,050\\text{ kg} \\times 8000\\text{ m/s}^2 = 400\\text{ N}$."
    },
    {
      "type": "mc",
      "vraag": "Een zware vrachtwagen (20.000 kg) en een lichte auto (1000 kg) rijden even snel. Wat is er nodig om de vrachtwagen in dezelfde tijd tot stilstand te brengen als de auto?",
      "opties": [
        "Een 20 keer kleinere remkracht",
        "Een precies even grote remkracht",
        "Een 20 keer grotere remkracht",
        "Dat is fysisch volstrekt onmogelijk"
      ],
      "antwoord": 2,
      "uitleg": "De vereiste vertraging $a$ is hetzelfde. Omdat de massa van de vrachtwagen 20 keer zo groot is, is volgens $F = m \\cdot a$ ook een 20 keer zo grote remkracht nodig."
    },
    {
      "type": "mc",
      "vraag": "Een auto heeft een versnelling van 2,5 m/s². Wat betekent deze waarde in de praktijk?",
      "opties": [
        "De auto legt elke seconde 2,5 meter af",
        "De auto weegt 2500 kg",
        "De motorkracht is 2,5 Newton",
        "De snelheid van de auto neemt iedere seconde met 2,5 m/s toe"
      ],
      "antwoord": 3,
      "uitleg": "Versnelling geeft de toename van de snelheid per seconde aan: elke seconde komt er 2,5 m/s bij."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als een voorwerp vertraagt (afremt), wijst de resulterende kracht in tegengestelde richting aan de bewegingsrichting.",
      "antwoord": True,
      "uitleg": "Waar. Een kracht tegen de bewegingsrichting in zorgt ervoor dat de snelheid afneemt."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een lichte carbon racefiets heeft meer traagheid dan een zware stadsfiets met fietstassen.",
      "antwoord": False,
      "uitleg": "Niet waar. Traagheid hangt rechtstreeks af van de massa: hoe groter de massa, hoe groter de traagheid."
    },
    {
      "type": "waaronwaar",
      "vraag": "Volgens $F_{res} = m \\cdot a$ is de kracht recht evenredig met de versnelling: dubbel zoveel kracht levert bij gelijke massa een dubbele versnelling op.",
      "antwoord": True,
      "uitleg": "Waar. Bij een constante massa zorgt een twee keer zo grote kracht voor een twee keer zo grote versnelling."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een stilstaand voorwerp bezit geen enkele traagheid; traagheid ontstaat pas op het moment dat een voorwerp gaat bewegen.",
      "antwoord": False,
      "uitleg": "Niet waar. Elk voorwerp met massa heeft traagheid, ook als het stilstaat. De traagheid verzet zich er juist tegen om vanuit stilstand in beweging te komen."
    },
    {
      "type": "invul",
      "vraag": "Een drone heeft een massa van 2,4 kg en versnelt omhoog met 3,5 m/s². Bereken de resulterende kracht in Newton.",
      "antwoord": "8,4|8,4 N",
      "uitleg": "$F_{res} = m \\times a = 2,4\\text{ kg} \\times 3,5\\text{ m/s}^2 = 8,4\\text{ N}$."
    },
    {
      "type": "invul",
      "vraag": "Een fietser versnelt gelijkmatig van 2,0 m/s naar 8,0 m/s in een tijdsduur van 4,0 seconden. Bereken de gemiddelde versnelling in m/s².",
      "antwoord": "1,5|1,5 m/s2|1,5 m/s²",
      "uitleg": "$a = \\Delta v / t = (8,0 - 2,0) / 4,0 = 6,0 / 4,0 = 1,5\\text{ m/s}^2$."
    },
    {
      "type": "open",
      "vraag": "Waarom is het wettelijk verplicht om zware goederen op een open laadbak stevig vast te zetten met spanbanden? Benoem het fysische verschijnsel van de lading.",
      "sleutelwoorden": [
        "traagheid/inertie",
        "doorschieten/naar voren schuiven/losraken"
      ],
      "minTreffers": 1,
      "modelantwoord": "Bij plotseling krachtig remmen wil de zware lading door haar eigen traagheid (inertie) met dezelfde snelheid vooruit blijven bewegen. Zonder stevige spanbanden schuift de lading naar voren van de laadbak af, wat grote schade en ongelukken veroorzaakt.",
      "uitleg": "Traagheid zorgt ervoor dat losliggende lading bij remmen rechtdoor wil blijven bewegen."
    },
    {
      "type": "open",
      "vraag": "Een auto van 1200 kg trekt op. De motorkracht is 3000 N en de gezamenlijke rol- en luchtweerstand is 600 N. Bereken in twee stappen de versnelling.",
      "sleutelwoorden": [
        "2400 N/2400 newton",
        "2 m/s2/2,0 m/s2/2 m/s²/2,0 m/s²"
      ],
      "minTreffers": 2,
      "modelantwoord": "Stap 1: Bereken de resulterende kracht: $F_{res} = F_{motor} - F_{weerstand} = 3000 - 600 = 2400\\text{ N}$. Stap 2: Bereken de versnelling: $a = F_{res} / m = 2400 / 1200 = 2,0\\text{ m/s}^2$.",
      "uitleg": "Eerst de tegenwerkende krachten aftrekken om $F_{res}$ te vinden, en dan delen door de massa $m$."
    }
  ]
}

exam_5 = {
  "id": "ex-h3-natuurkunde-5",
  "hoofdstuk": 1,
  "titel": "Toets 5 — Integrale Examentraining Paragrafen 1.1 t/m 1.3 (Mix)",
  "vak": "Natuurkunde · HAVO 3 (H1)",
  "icoon": "🏆",
  "duurMin": 35,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Een wielrenner fietst over een wielerbaan. In de eerste 10 s versnelt hij eenparig van 0 naar 14 m/s. Daarna rijdt hij 30 s met 14 m/s constante snelheid door. Welke totale afstand legt hij af in die 40 s?",
      "opties": [
        "490 m",
        "560 m",
        "420 m",
        "280 m"
      ],
      "antwoord": 0,
      "uitleg": "Deel 1 (driehoek): $0,5 \\times 10\\text{ s} \\times 14\\text{ m/s} = 70\\text{ m}$. Deel 2 (rechthoek): $30\\text{ s} \\times 14\\text{ m/s} = 420\\text{ m}$. Totale afstand $s = 70 + 420 = 490\\text{ meter}$."
    },
    {
      "type": "mc",
      "vraag": "Een elektrische auto van 1500 kg rijdt met 108 km/h (30 m/s). De bestuurder remt krachtig af tot stilstand in 5,0 seconden. Hoe groot is de remmende resulterende kracht op de auto?",
      "opties": [
        "6000 N",
        "9000 N",
        "4500 N",
        "15.000 N"
      ],
      "antwoord": 1,
      "uitleg": "De vertraging is $a = \\Delta v / t = (0 - 30) / 5,0 = -6,0\\text{ m/s}^2$. De benodigde remkracht is $F_{res} = m \\times a = 1500\\text{ kg} \\times 6,0\\text{ m/s}^2 = 9000\\text{ N}$."
    },
    {
      "type": "mc",
      "vraag": "Bekijk een (v,t)-diagram van een brommer: tussen t = 0 en t = 5 s rijdt hij met constante snelheid van 15 m/s; tussen t = 5 s en t = 8 s remt hij gelijkmatig af naar 0 m/s. Wat is de totale afstand?",
      "opties": [
        "75 m",
        "120 m",
        "97,5 m",
        "105 m"
      ],
      "antwoord": 2,
      "uitleg": "Rechthoek: $5\\text{ s} \\times 15\\text{ m/s} = 75\\text{ m}$. Driehoek: $0,5 \\times (8 - 5)\\text{ s} \\times 15\\text{ m/s} = 0,5 \\times 3 \\times 15 = 22,5\\text{ m}$. Totale afstand $= 75 + 22,5 = 97,5\\text{ meter}$."
    },
    {
      "type": "mc",
      "vraag": "Waarom heeft een tijdrijder in aerodynamische houding op een tijdritfiets bij 50 km/h veel minder trapkracht nodig dan een gewone fietser?",
      "opties": [
        "Doordat de zwaartekracht op de tijdrijder afneemt",
        "Doordat de rolweerstand van de banden halveert bij aerodynamica",
        "Doordat de massa van de fiets tijdens het rijden daalt",
        "Doordat het frontaal oppervlak kleiner is en de luchtweerstand daardoor sterk afneemt"
      ],
      "antwoord": 3,
      "uitleg": "Luchtweerstand is bij 50 km/h veruit de grootste tegenkracht. Een diepe zithouding verkleint het frontaal oppervlak, waardoor de luchtweerstand enorm daalt."
    },
    {
      "type": "mc",
      "vraag": "Een weersraket met een massa van 4000 kg heeft een motor die een opwaartse stuwkracht levert van 60.000 N. De neerwaartse zwaartekracht is 40.000 N. Met welke versnelling stijgt de raket op?",
      "opties": [
        "5,0 m/s²",
        "15 m/s²",
        "10 m/s²",
        "2,5 m/s²"
      ],
      "antwoord": 0,
      "uitleg": "$F_{res} = 60.000 - 40.000 = 20.000\\text{ N}$ omhoog. $a = F_{res} / m = 20.000 / 4000 = 5,0\\text{ m/s}^2$."
    },
    {
      "type": "mc",
      "vraag": "Een fietser rijdt met 18 km/h. Plotseling steekt er een flinke tegenwind op, terwijl hij met dezelfde trapkracht blijft trappen. Wat gebeurt er direct?",
      "opties": [
        "De fietser versnelt",
        "De fietser vertraagt totdat er een nieuw evenwicht ontstaat bij een lagere snelheid",
        "De fietser rijdt met exact dezelfde snelheid door",
        "De fietser komt direct abrupt tot stilstand"
      ],
      "antwoord": 1,
      "uitleg": "Door de tegenwind wordt de luchtweerstand groter dan de trapkracht ($F_{tegen} > F_{spier}$). Daardoor ontstaat een negatieve resulterende kracht en vertraagt de fietser tot de krachten weer in evenwicht zijn."
    },
    {
      "type": "mc",
      "vraag": "In een (s,t)-diagram legt een brommer in 10 s een afstand van 80 m af. Vervolgens staat hij stil van t = 10 s tot t = 25 s. Wat is de gemiddelde snelheid over het hele interval van 25 seconden?",
      "opties": [
        "8,0 m/s",
        "5,3 m/s",
        "3,2 m/s",
        "2,5 m/s"
      ],
      "antwoord": 2,
      "uitleg": "Totale afstand $s = 80\\text{ m}$, totale tijd $t = 25\\text{ s}$. $v_{gem} = s / t = 80 / 25 = 3,2\\text{ m/s}$."
    },
    {
      "type": "mc",
      "vraag": "Welke van de onderstaande situaties beschrijft een eenparig vertraagde beweging?",
      "opties": [
        "Een steen die vanaf een toren naar beneden valt",
        "Een sprinter die krachtig optrekt uit het startblok",
        "Een intercity die met 140 km/h over een recht spoor raast",
        "Een auto die voor een rood verkeerslicht gelijkmatig afremt tot stilstand"
      ],
      "antwoord": 3,
      "uitleg": "Gelijkmatig afremmen betekent dat de snelheid iedere seconde met dezelfde hoeveelheid afneemt. Dat is de definitie van eenparig vertraagd."
    },
    {
      "type": "mc",
      "vraag": "Een kist met een massa van 6,0 kg ondervindt twee horizontale krachten: $F_1 = 35\\text{ N}$ naar rechts en $F_2 = 17\\text{ N}$ naar links. Wat is de versnelling van de kist?",
      "opties": [
        "3,0 m/s² naar rechts",
        "3,0 m/s² naar links",
        "8,7 m/s² naar rechts",
        "1,5 m/s² naar links"
      ],
      "antwoord": 0,
      "uitleg": "$F_{res} = 35 - 17 = 18\\text{ N}$ naar rechts. $a = F_{res} / m = 18 / 6,0 = 3,0\\text{ m/s}^2$ naar rechts."
    },
    {
      "type": "mc",
      "vraag": "Een sprinter rent de 100 meter in 10,0 seconden en finisht met een topsnelheid van 12,0 m/s. Welke uitspraak over zijn gemiddelde snelheid ($v_{gem}$) en topsnelheid ($v_{max}$) is juist?",
      "opties": [
        "v_gem = 12,0 m/s en v_max = 10,0 m/s",
        "v_gem = 10,0 m/s en v_max = 12,0 m/s",
        "Beide snelheden zijn exact gelijk aan 10,0 m/s",
        "Beide snelheden zijn exact gelijk aan 12,0 m/s"
      ],
      "antwoord": 1,
      "uitleg": "$v_{gem} = 100\\text{ m} / 10,0\\text{ s} = 10,0\\text{ m/s}$. Zijn topsnelheid ligt hoger omdat hij vanuit stilstand moest versnellen."
    },
    {
      "type": "mc",
      "vraag": "In een (v,t)-diagram is de stijgende lijn van motorfiets A steiler dan die van scooter B. Welke conclusie is juist?",
      "opties": [
        "Scooter B versnelt sneller dan motorfiets A",
        "Beide voertuigen rijden met dezelfde snelheid",
        "Motorfiets A heeft een grotere versnelling dan scooter B",
        "Motorfiets A rijdt met een constante snelheid"
      ],
      "antwoord": 2,
      "uitleg": "In een (v,t)-diagram geeft de steilheid van de grafiek de versnelling aan ($a = \\Delta v / \\Delta t$). Een steilere lijn betekent een grotere versnelling."
    },
    {
      "type": "mc",
      "vraag": "Hoe groot is de resulterende kracht op een skydiver van 80 kg die met constante daalsnelheid door de lucht zweeft?",
      "opties": [
        "800 N naar beneden",
        "80 N naar boven",
        "9,8 N naar beneden",
        "0 N"
      ],
      "antwoord": 3,
      "uitleg": "Constante snelheid betekent altijd dat de resulterende kracht gelijk is aan 0 N. De opwaartse luchtweerstand is exact gelijk aan de zwaartekracht."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als een auto met 90 km/h (25 m/s) rijdt en in 5,0 seconden versnelt naar 126 km/h (35 m/s), dan is de versnelling gelijk aan 2,0 m/s².",
      "antwoord": True,
      "uitleg": "Waar. $a = \\Delta v / t = (35 - 25) / 5,0 = 10 / 5,0 = 2,0\\text{ m/s}^2$."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een zware vrachtwagen en een lichte motorfiets met dezelfde remkracht hebben bij dezelfde beginsnelheid dezelfde remvertraging.",
      "antwoord": False,
      "uitleg": "Niet waar. Omdat de vrachtwagen een veel grotere massa heeft, is zijn vertraging bij dezelfde remkracht veel kleiner ($a = F / m$)."
    },
    {
      "type": "waaronwaar",
      "vraag": "In een (s,t)-diagram betekent een horizontale lijn stilstand, terwijl een horizontale lijn in een (v,t)-diagram een constante snelheid voorstelt.",
      "antwoord": True,
      "uitleg": "Waar. In een (s,t)-diagram verandert de positie niet (stilstand). In een (v,t)-diagram verandert de snelheid niet (constante snelheid)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als de motorkracht van een rijdende auto 1000 N is en de auto versnelt, dan is de tegenwerkende weerstandskracht ook 1000 N.",
      "antwoord": False,
      "uitleg": "Niet waar. Als de auto versnelt moet $F_{res} > 0$ zijn, wat betekent dat de motorkracht groter moet zijn dan de weerstandskracht ($F_{motor} > F_{tegen}$)."
    },
    {
      "type": "invul",
      "vraag": "Een speedboot heeft een massa van 800 kg. De motor levert 4400 N stuwkracht en de waterweerstand is 2000 N. Bereken de versnelling in m/s².",
      "antwoord": "3|3,0|3 m/s2|3 m/s²|3,0 m/s2|3,0 m/s²",
      "uitleg": "$F_{res} = 4400 - 2000 = 2400\\text{ N}$. $a = F_{res} / m = 2400 / 800 = 3,0\\text{ m/s}^2$."
    },
    {
      "type": "invul",
      "vraag": "Een schaatser rijdt 5 rondjes van 400 meter (totaal 2000 m) in een tijd van 2 minuten en 40 seconden (160 s). Bereken zijn gemiddelde snelheid in m/s.",
      "antwoord": "12,5|12,5 m/s",
      "uitleg": "$v_{gem} = s / t = 2000\\text{ m} / 160\\text{ s} = 12,5\\text{ m/s}$."
    },
    {
      "type": "open",
      "vraag": "Een auto rijdt met 100 km/h. De bestuurder trapt het gaspedaal dieper in om te versnellen naar 120 km/h. Beschrijf wat er gebeurt met de voorwaartse kracht en de tegenkrachten totdat de auto weer een constante snelheid heeft bereikt.",
      "sleutelwoorden": [
        "motorkracht groter/voorwaartse kracht groter",
        "luchtweerstand stijgt/luchtweerstand groter",
        "heffen elkaar op/resulterende kracht nul"
      ],
      "minTreffers": 2,
      "modelantwoord": "De bestuurder vergroot de motorkracht waardoor $F_{motor} > F_{tegen}$, er ontstaat een positieve resulterende kracht en de auto versnelt. Doordat de snelheid toeneemt, stijgt de luchtweerstand. Bij 120 km/h is de luchtweerstand weer precies even groot geworden als de motorkracht, waardoor de resulterende kracht weer nul wordt ($F_{res} = 0$) en de snelheid constant blijft.",
      "uitleg": "Bij het intrappen van het gas versnelt de auto, de luchtweerstand stijgt tot er een nieuw evenwicht is bij 120 km/h."
    },
    {
      "type": "open",
      "vraag": "Op een wrijvingsloze baan worden twee wagentjes gelijktijdig afgeschoten met exact dezelfde kracht. Wagentje 1 heeft een massa van 800 gram en wagentje 2 heeft een massa van 150 gram. Beargumenteer natuurkundig waarom het lichte wagentje na de afstoot een veel hogere snelheid heeft.",
      "sleutelwoorden": [
        "grotere versnelling/hogere versnelling",
        "F = m * a/Fres = m . a/tweede wet van newton/Newton",
        "traagheid/minder traagheid/minder verzet"
      ],
      "minTreffers": 2,
      "modelantwoord": "Voorwerp B bereikt een veel hogere snelheid. Volgens $a = F / m$ krijgt voorwerp B door zijn veel kleinere massa een enorm veel grotere versnelling bij dezelfde kracht van 20 N. Daardoor wint voorwerp B in dezelfde 0,2 seconden veel meer snelheid dan het zware voorwerp A.",
      "uitleg": "Kleinere massa betekent bij gelijke kracht een grotere versnelling en dus een hogere eindsnelheid."
    }
  ]
}

# Begrippen module
begrippen_onderwerp = {
  "id": "h1-begrippen",
  "hoofdstuk": 1,
  "paragraaf": "1.0",
  "titel": "Kernbegrippen & Formules (§1.1 t/m §1.3)",
  "korteUitleg": "Volledig overzicht van definities, eenheden, formules en wetten van paragraaf 1.1, 1.2 en 1.3.",
  "icoon": "🔑",
  "kleur": "h1-thema",
  "theorie": """<h3>Kernbegrippen & Formules — Hoofdstuk 1 (§1.1, §1.2 & §1.3)</h3>
<p>Dit overzicht bevat alle essentiële theorie, definities, formules en rekenregels uit de eerste drie paragrafen van <i>Overal Natuurkunde 3 HAVO</i>. Leer deze begrippen grondig voor de toetsen!</p>

<div class=\"formule-box\">
  <strong>Belangrijkste Formules & Rekenregels:</strong><br>
  • <b>Gemiddelde snelheid:</b> $v_{gem} = \\frac{s}{t}$ &nbsp;|&nbsp; $s = v_{gem} \\cdot t$ &nbsp;|&nbsp; $t = \\frac{s}{v_{gem}}$<br>
  • <b>Eenheden omrekenen:</b> van $\\text{km/h}$ naar $\\text{m/s}$ deel je door $3,6$. Van $\\text{m/s}$ naar $\\text{km/h}$ vermenigvuldig je met $3,6$.<br>
  • <b>Versnelling:</b> $a = \\frac{\\Delta v}{\\Delta t} = \\frac{v_{eind} - v_{begin}}{t}$ (in $\\text{m/s}^2$)<br>
  • <b>Tweede wet van Newton:</b> $F_{res} = m \\cdot a$ &nbsp;|&nbsp; $m = \\frac{F_{res}}{a}$ &nbsp;|&nbsp; $a = \\frac{F_{res}}{m}$<br>
  • <b>Resulterende kracht:</b> krachten in dezelfde richting optellen ($F_{res} = F_1 + F_2$), in tegengestelde richting aftrekken ($F_{res} = F_{vooruit} - F_{tegen}$).
</div>

<h4>1. Grootheden, Symbolen en SI-Eenheden</h4>
<table class=\"nask\" style=\"width:100%; border-collapse: collapse; margin: 12px 0;\">
  <thead>
    <tr style=\"background: var(--grijs-licht, #f1f5f9); text-align: left;\">
      <th style=\"padding: 6px;\">Grootheid</th>
      <th style=\"padding: 6px;\">Symbool</th>
      <th style=\"padding: 6px;\">Standaard SI-eenheid</th>
      <th style=\"padding: 6px;\">Andere gebruikte eenheid</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style=\"padding: 6px;\">Afstand / Verplaatsing</td><td style=\"padding: 6px;\"><b>s</b></td><td style=\"padding: 6px;\">meter (m)</td><td style=\"padding: 6px;\">kilometer (km)</td></tr>
    <tr><td style=\"padding: 6px;\">Tijd</td><td style=\"padding: 6px;\"><b>t</b></td><td style=\"padding: 6px;\">seconde (s)</td><td style=\"padding: 6px;\">uur (h), minuut (min)</td></tr>
    <tr><td style=\"padding: 6px;\">Snelheid</td><td style=\"padding: 6px;\"><b>v</b></td><td style=\"padding: 6px;\">meter per seconde (m/s)</td><td style=\"padding: 6px;\">kilometer per uur (km/h)</td></tr>
    <tr><td style=\"padding: 6px;\">Versnelling</td><td style=\"padding: 6px;\"><b>a</b></td><td style=\"padding: 6px;\">meter per seconde kwadraat (m/s²)</td><td style=\"padding: 6px;\">-</td></tr>
    <tr><td style=\"padding: 6px;\">Massa</td><td style=\"padding: 6px;\"><b>m</b></td><td style=\"padding: 6px;\">kilogram (kg)</td><td style=\"padding: 6px;\">gram (g)</td></tr>
    <tr><td style=\"padding: 6px;\">Kracht</td><td style=\"padding: 6px;\"><b>F</b></td><td style=\"padding: 6px;\">Newton (N)</td><td style=\"padding: 6px;\">kilonewton (kN)</td></tr>
  </tbody>
</table>

<h4>2. Bewegingssoorten & Diagrammen</h4>
<ul>
  <li><b>Eenparige beweging:</b> De snelheid is constant ($a = 0$). In het (s,t)-diagram is dit een rechte schuine lijn; in het (v,t)-diagram een rechte horizontale lijn.</li>
  <li><b>Eenparig versnelde beweging:</b> De snelheid neemt iedere seconde met een vaste hoeveelheid toe ($a$ is constant positief). In het (s,t)-diagram een steeds steiler wordende kromme; in het (v,t)-diagram een rechte stijgende lijn.</li>
  <li><b>Eenparig vertraagde beweging:</b> De snelheid neemt iedere seconde met een vaste hoeveelheid af ($a$ is constant negatief). In het (s,t)-diagram vlakt de lijn af; in het (v,t)-diagram een rechte dalende lijn.</li>
  <li><b>Helling in (s,t)-diagram:</b> De steilheid geeft de snelheid aan. Horizontaal betekent stilstand ($v = 0$).</li>
  <li><b>Oppervlakte in (v,t)-diagram:</b> De oppervlakte onder de grafiek is gelijk aan de afgelegde afstand ($s$). Voor een rechthoek $s = v \\cdot t$, voor een driehoek $s = 0,5 \\cdot v_{top} \\cdot t$.</li>
</ul>

<h4>3. Krachten & De Wetten van Newton</h4>
<div class=\"begrippen-box\">
  <b>Kernbegrippen:</b>
  <ul>
    <li><b>Resulterende kracht ($F_{res}$):</b> De somkracht die alle op een voorwerp werkende krachten vervangt. Als $F_{res} = 0\\text{ N}$, heffen de krachten elkaar op en verandert de snelheid niet (Eerste wet van Newton).</li>
    <li><b>Tweede wet van Newton:</b> Een resulterende kracht veroorzaakt een versnelling ($F_{res} = m \\cdot a$). Hoe groter de massa, des te meer kracht er nodig is voor dezelfde versnelling.</li>
    <li><b>Traagheid (inertie):</b> De natuurlijke eigenschap van massa waardoor een voorwerp zich verzet tegen verandering van beweging of richting.</li>
    <li><b>Tegenwerkende krachten:</b> Bij beweging spelen <i>rolweerstand</i> (vervorming van banden/wegdek) en <i>luchtweerstand</i> (botsing met luchtdeeltjes) een centrale rol. Luchtweerstand stijgt kwadratisch met de snelheid!</li>
  </ul>
</div>""",
  "vragen": [
    {
      "type": "mc",
      "niveau": 1,
      "vraag": "Wat is de officiële SI-eenheid van versnelling?",
      "opties": [
        "m/s²",
        "m/s",
        "km/h",
        "Newton"
      ],
      "antwoord": 0,
      "uitleg": "De eenheid van versnelling is m/s² (meter per seconde kwadraat)."
    },
    {
      "type": "mc",
      "niveau": 1,
      "vraag": "Wat stelt de oppervlakte onder de grafieklijn voor in een (v,t)-diagram?",
      "opties": [
        "De versnelling",
        "De afgelegde afstand",
        "De resulterende kracht",
        "De massa"
      ],
      "antwoord": 1,
      "uitleg": "Oppervlakte in een (v,t)-diagram = snelheid × tijd = afstand in meters."
    },
    {
      "type": "mc",
      "niveau": 2,
      "vraag": "Hoe groot is de resulterende kracht op een fietser die met een constante snelheid van 20 km/h fietst?",
      "opties": [
        "20 N",
        "Afhankelijk van zijn massa",
        "Exact 0 N",
        "Gelijk aan de zwaartekracht"
      ],
      "antwoord": 2,
      "uitleg": "Bij constante snelheid is er geen versnelling, dus Fres = 0 N."
    },
    {
      "type": "mc",
      "niveau": 2,
      "vraag": "Hoe reken je een snelheid in km/h om naar m/s?",
      "opties": [
        "Vermenigvuldigen met 3,6",
        "Delen door 60",
        "Vermenigvuldigen met 10",
        "Delen door 3,6"
      ],
      "antwoord": 3,
      "uitleg": "Omrekenen van km/h naar m/s doe je door te delen door 3,6."
    },
    {
      "type": "waaronwaar",
      "vraag": "In een (s,t)-diagram betekent een horizontale rechte lijn dat het voorwerp stilstaat.",
      "antwoord": True,
      "uitleg": "Waar. De afstand s verandert niet in de tijd, dus v = 0 m/s."
    },
    {
      "type": "waaronwaar",
      "vraag": "Volgens $F_{res} = m \\cdot a$ levert een twee keer zo grote massa bij gelijke kracht een twee keer zo grote versnelling op.",
      "antwoord": False,
      "uitleg": "Niet waar. Meer massa betekent meer traagheid, dus juist een twee keer zo kleine versnelling."
    },
    {
      "type": "invoer",
      "niveau": 1,
      "vraag": "Reken om: 72 km/h is gelijk aan hoeveel m/s? Vul alleen het getal in.",
      "antwoord": "20|20,0",
      "uitleg": "72 / 3,6 = 20 m/s."
    },
    {
      "type": "invoer",
      "niveau": 2,
      "vraag": "Een voorwerp met een massa van 5 kg versnelt met 3 m/s². Hoe groot is de resulterende kracht in Newton? Vul alleen het getal in.",
      "antwoord": "15|15,0",
      "uitleg": "Fres = m × a = 5 × 3 = 15 N."
    }
  ]
}

validate_exam(exam_1, "examen_1.js")
validate_exam(exam_2, "examen_2.js")
validate_exam(exam_3, "examen_3.js")
validate_exam(exam_4, "examen_4.js")
validate_exam(exam_5, "examen_5.js")

# Write out the exams
def write_exam_file(exam_obj, path):
    content = f"/* =========================================================\n   Duru's Natuurkunde (HAVO 3) — {exam_obj['titel']}\n   ========================================================= */\nDURU.registerExamen({json.dumps(exam_obj, indent=2, ensure_ascii=False)});\n"
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written {path}")

def write_onderwerp_file(ow_obj, path):
    content = f"/* =========================================================\n   Duru's Natuurkunde (HAVO 3) — {ow_obj['titel']}\n   ========================================================= */\nDURU.register({json.dumps(ow_obj, indent=2, ensure_ascii=False)});\n"
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written {path}")

write_exam_file(exam_1, "havo3/natuurkunde/js/data/examen_1.js")
write_exam_file(exam_2, "havo3/natuurkunde/js/data/examen_2.js")
write_exam_file(exam_3, "havo3/natuurkunde/js/data/examen_3.js")
write_exam_file(exam_4, "havo3/natuurkunde/js/data/examen_4.js")
write_exam_file(exam_5, "havo3/natuurkunde/js/data/examen_5.js")
write_onderwerp_file(begrippen_onderwerp, "havo3/natuurkunde/js/data/h1_begrippen.js")

print("All 5 exams and begrippen file written successfully!")

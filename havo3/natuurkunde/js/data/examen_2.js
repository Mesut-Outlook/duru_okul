/* Proeftoets 2 — Natuurkunde HAVO 3: Hoofdstuk 1 (Kracht en beweging - Deel 2)
   Focus: Paragraaf 1.2 & 1.3 — Versnelling, massa, traagheid en Tweede wet van Newton (Fres = m * a).
   20 vragen conform DURU ENGINE_SPEC. */
DURU.registerExamen({
  id: "ex-h3-natuurkunde-2",
  titel: "Toets 2 — Versnelling, Massa & Wet van Newton",
  vak: "Natuurkunde · HAVO 3 (H1)",
  icoon: "⚡",
  duurMin: 30,
  vragen: [
    {
      type: "mc",
      vraag: "Wat is de officiële eenheid van <b>versnelling (a)</b>?",
      opties: [
        "m/s²",
        "m/s",
        "km/h",
        "N/kg"
      ],
      antwoord: 0,
      uitleg: "De eenheid van versnelling is meter per seconde kwadraat (m/s²). Dit geeft aan met hoeveel m/s de snelheid iedere seconde toeneemt."
    },
    {
      type: "mc",
      vraag: "Een motorrijder versnelt vanuit stilstand naar 24 m/s in 6,0 seconden. Wat is zijn gemiddelde versnelling?",
      opties: [
        "2,0 m/s²",
        "4,0 m/s²",
        "3,0 m/s²",
        "6,0 m/s²"
      ],
      antwoord: 1,
      uitleg: "a = Δv / Δt = (24 m/s - 0 m/s) / 6,0 s = 4,0 m/s²."
    },
    {
      type: "invul",
      vraag: "Welke formule gebruik je om de resulterende kracht te berekenen uit de massa (m) en versnelling (a)? Typ de formule (bijv. F = ...).",
      antwoord: "F=m*a|F=m.a|F=mxa|Fres=m*a|Fres=m.a|Fres=mxa|F=m a",
      uitleg: "De 2e wet van Newton luidt: F_res = m × a (kracht = massa × versnelling)."
    },
    {
      type: "mc",
      vraag: "Een winkelwagentje met een totale massa van 25 kg krijgt een versnelling van 1,5 m/s². Hoe groot is de resulterende kracht die erop werkt?",
      opties: [
        "16,7 N",
        "25 N",
        "37,5 N",
        "50 N"
      ],
      antwoord: 2,
      uitleg: "F_res = m × a = 25 kg × 1,5 m/s² = 37,5 N."
    },
    {
      type: "waaronwaar",
      vraag: "Hoe groter de <b>massa</b> van een voorwerp, des te moeilijker het is om de snelheid of bewegingsrichting van dat voorwerp te veranderen. Deze eigenschap heet <b>traagheid</b>.",
      antwoord: true,
      uitleg: "Waar. Massa bezit traagheid (inertie): een grotere massa verzet zich sterker tegen verandering van snelheid."
    },
    {
      type: "invul",
      vraag: "Op een doos met een massa van 8,0 kg werkt een resulterende kracht van 32 N. Bereken de versnelling in m/s².",
      antwoord: "4|4,0|4 m/s²|4,0 m/s²",
      uitleg: "a = F_res / m = 32 N / 8,0 kg = 4,0 m/s²."
    },
    {
      type: "mc",
      vraag: "Een auto van 1200 kg remt af met een vertraging van 3,5 m/s². Hoe groot is de remkracht die hiervoor nodig is?",
      opties: [
        "343 N",
        "1200 N",
        "3500 N",
        "4200 N"
      ],
      antwoord: 3,
      uitleg: "F = m × a = 1200 kg × 3,5 m/s² = 4200 N (oftewel 4,2 kN)."
    },
    {
      type: "waaronwaar",
      vraag: "Als je de resulterende kracht op een voorwerp twee keer zo groot maakt, wordt de versnelling gehalveerd.",
      antwoord: false,
      uitleg: "Niet waar. Volgens F_res = m × a zijn kracht en versnelling recht evenredig: dubbele kracht betekent dubbele versnelling."
    },
    {
      type: "mc",
      vraag: "Een fietser rijdt met een snelheid van 10 m/s en remt in 4,0 seconden gelijkmatig af tot stilstand. Wat is de (rem)vertraging?",
      opties: [
        "2,5 m/s²",
        "1,5 m/s²",
        "4,0 m/s²",
        "5,0 m/s²"
      ],
      antwoord: 0,
      uitleg: "a = Δv / Δt = 10 m/s / 4,0 s = 2,5 m/s²."
    },
    {
      type: "invul",
      vraag: "Bereken de zwaartekracht F_z (in N) op een persoon met een massa van 65 kg op aarde (neem g = 9,81 N/kg, rond af op 1 decimaal of geheel getal).",
      antwoord: "637,65|637,7|638|650|637,65 N|637,7 N|638 N|650 N",
      uitleg: "F_z = m × g = 65 kg × 9,81 N/kg = 637,7 N (met g = 10 N/kg is het 650 N)."
    },
    {
      type: "mc",
      vraag: "In een (v,t)-diagram is de lijn een <b>schuine rechte lijn omhoog</b>. Wat kun je zeggen over de versnelling?",
      opties: [
        "De versnelling is 0 m/s²",
        "De versnelling is constant",
        "De versnelling neemt toe",
        "De versnelling neemt af"
      ],
      antwoord: 1,
      uitleg: "De helling van de (v,t)-grafiek is de versnelling a. Een rechte lijn heeft een constante helling, dus de versnelling is constant (eenparig versneld)."
    },
    {
      type: "mc",
      vraag: "Twee voorwerpen A en B worden met dezelfde kracht F voortgeduwd. Voorwerp A heeft een massa van 10 kg, voorwerp B heeft een massa van 20 kg. Wat geldt voor hun versnellingen?",
      opties: [
        "Beide voorwerpen krijgen dezelfde versnelling",
        "Versnelling van B is twee keer zo groot als die van A",
        "Versnelling van A is twee keer zo groot als die van B",
        "Voorwerp B versnelt vier keer zo snel"
      ],
      antwoord: 2,
      uitleg: "Omdat a = F / m, is de versnelling omgekeerd evenredig met de massa. Het lichtere voorwerp A (10 kg) krijgt een twee keer zo grote versnelling als B (20 kg)."
    },
    {
      type: "waaronwaar",
      vraag: "Bij een vrije val op aarde (zonder luchtweerstand) vallen een zware steen en een lichte veer even snel en met dezelfde versnelling (valversnelling g).",
      antwoord: true,
      uitleg: "Waar. Zonder luchtweerstand vallen alle voorwerpen met dezelfde valversnelling (g ≈ 9,81 m/s²), ongeacht hun massa."
    },
    {
      type: "invul",
      vraag: "Een trein van 80.000 kg rijdt met constante snelheid. De wrijving bedraagt 15.000 N. Hoeveel Newton is de voorwaartse trekkracht van de locomotief?",
      antwoord: "15000|15.000|15000 N|15.000 N|15 kN",
      uitleg: "Omdat de snelheid constant is (a = 0), is F_res = 0 N. De trekkracht moet dus precies gelijk zijn aan de wrijvingskracht: 15.000 N."
    },
    {
      type: "mc",
      vraag: "Een auto versnelt van 36 km/h naar 72 km/h in 5,0 seconden. Bereken eerst de snelheden in m/s en bepaal daarna de versnelling.",
      opties: [
        "1,0 m/s²",
        "7,2 m/s²",
        "3,6 m/s²",
        "2,0 m/s²"
      ],
      antwoord: 3,
      uitleg: "v_begin = 36 / 3,6 = 10 m/s; v_eind = 72 / 3,6 = 20 m/s. Δv = 20 - 10 = 10 m/s. a = Δv / Δt = 10 / 5,0 = 2,0 m/s²."
    },
    {
      type: "waaronwaar",
      vraag: "Als de motorkracht groter is dan de tegenwerkende wrijvingskracht, is de resulterende kracht positief en versnelt de auto.",
      antwoord: true,
      uitleg: "Waar. Als F_motor > F_wrijving, is F_res in de rijrichting en versnelt het voertuig."
    },
    {
      type: "invul",
      vraag: "Een hardloper (massa = 60 kg) start en oefent gedurende 2,0 s een gemiddelde voorwaartse kracht uit van 180 N. Welke snelheid bereikt de loper vanuit stilstand in m/s?",
      antwoord: "6|6,0|6 m/s|6,0 m/s",
      uitleg: "Versnelling a = F / m = 180 N / 60 kg = 3,0 m/s². Snelheid na 2 s: v = a × t = 3,0 m/s² × 2,0 s = 6,0 m/s."
    },
    {
      type: "mc",
      vraag: "Wat gebeurt er met de versnelling van een optrekkende auto als de motorkracht constant blijft, maar de luchtweerstand toeneemt naarmate de auto sneller gaat?",
      opties: [
        "De versnelling wordt steeds kleiner",
        "De versnelling wordt steeds groter",
        "De versnelling blijft gelijk",
        "De versnelling wordt meteen negatief"
      ],
      antwoord: 0,
      uitleg: "Omdat de luchtweerstand toeneemt, wordt F_res = F_motor - F_lucht steeds kleiner. Volgens a = F_res / m wordt de versnelling dus ook steeds kleiner."
    },
    {
      type: "open",
      vraag: "Leg uit waarom een passagier in een bus naar voren schiet als de bus plotseling heel hard moet remmen. Gebruik het begrip <b>traagheid</b> (of eerste wet van Newton).",
      sleutelwoorden: ["traagheid/massa", "snelheid behouden/doorbewegen/vooruit blijven gaan"],
      minTreffers: 2,
      modelantwoord: "Door de traagheid (massa) van de passagier wil het lichaam zijn voorwaartse snelheid behouden. De bus remt af door de remmen, maar op de passagier werkt op dat moment nog geen achterwaartse kracht, waardoor de passagier met zijn oorspronkelijke snelheid naar voren doorglijdt/doorschiet.",
      uitleg: "Een lichaam in beweging wil door traagheid zijn snelheid en richting behouden totdat een kracht (zoals een gordel of leuning) het afremt."
    },
    {
      type: "open",
      vraag: "Een vrachtwagen van 15.000 kg en een kleine personenauto van 1000 kg rijden beiden met 50 km/h. Leg uit waarom de vrachtwagen een veel grotere remkracht nodig heeft om in dezelfde remtijd tot stilstand te komen.",
      sleutelwoorden: ["massa", "F = m * a / grotere massa vereist grotere kracht", "traagheid"],
      minTreffers: 2,
      modelantwoord: "Beide voertuigen moeten in dezelfde tijd van 50 km/h naar 0 km/h, dus ze hebben dezelfde vertraging (a). Volgens de formule F_rem = m × a is de benodigde remkracht recht evenredig met de massa. Omdat de vrachtwagen een 15 keer zo grote massa heeft, is er ook een 15 keer zo grote remkracht nodig.",
      uitleg: "Gelijke versnelling/vertraging bij veel grotere massa vereist volgens F = m × a een evenredig grotere kracht."
    }
  ]
});

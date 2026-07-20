/* Oefentoets 1 — Snelheid (Hoofdstuk 4), nagebouwd uit de schoolfoto's */
DURU.registerExamen({
  id: "toets-h4-snelheid",
  titel: "Oefentoets H4 — Snelheid",
  vak: "Snelheid · Hoofdstuk 4",
  icoon: "🏎️",
  duurMin: 20,
  vragen: [
    { type: "mc", vraag: "Waar is de snelheid van afhankelijk?",
      opties: ["Afstand en tijd", "Massa en volume", "Temperatuur en druk", "Hoogte en gewicht"], antwoord: 0,
      uitleg: "Snelheid = <b>afstand : tijd</b>. De snelheid hangt dus af van de afstand die je aflegt én de tijd die je daarover doet." },

    { type: "mc", vraag: "Welke formule gebruik je om de snelheid te berekenen?",
      opties: ["Snelheid = Afstand / Tijd", "Snelheid = Afstand × Tijd", "Snelheid = Tijd / Afstand", "Snelheid = Afstand + Tijd"], antwoord: 0,
      uitleg: "De formule is <b>snelheid = afstand : tijd</b> (afstand gedeeld door tijd)." },

    { type: "mc", vraag: "Wat is de eenheid van snelheid als afstand in kilometers en tijd in uren wordt gemeten?",
      opties: ["km/u", "m/s", "cm/s", "mm/s"], antwoord: 0,
      uitleg: "Kilometer (km) gedeeld door uur (u) geeft de eenheid <b>km/u</b> (kilometer per uur)." },

    { type: "mc", vraag: "Een auto rijdt 150 km in 3 uur. Wat is de gemiddelde snelheid?",
      opties: ["50 km/u", "450 km/u", "147 km/u", "153 km/u"], antwoord: 0,
      uitleg: "snelheid = afstand : tijd = 150 : 3 = <b>50 km/u</b>." },

    { type: "mc", vraag: "Een fietser rijdt met een snelheid van 20 km/u. Hoeveel kilometer legt hij af in 1,5 uur?",
      opties: ["30 km", "20 km", "13,3 km", "21,5 km"], antwoord: 0,
      uitleg: "afstand = snelheid × tijd = 20 × 1,5 = <b>30 km</b>." },

    { type: "mc", vraag: "Wat gebeurt er met de snelheid als de afstand groter wordt en de tijd gelijk blijft?",
      opties: ["De snelheid wordt groter", "De snelheid wordt kleiner", "De snelheid blijft gelijk", "De snelheid wordt nul"], antwoord: 0,
      uitleg: "Meer afstand in dezelfde tijd betekent dat je sneller gaat: de snelheid wordt <b>groter</b>." },

    { type: "mc", vraag: "Ellen van Vugt verbeterde haar eigen record door enkele dingen aan haar fiets te veranderen. Welke aanpassing zou haar snelheid NIET verhogen?",
      opties: ["Zwaardere banden", "Lichtere onderdelen", "Meer aerodynamische vorm", "Betere smering van de ketting"], antwoord: 0,
      uitleg: "<b>Zwaardere banden</b> maken de fiets zwaarder en langzamer. De andere drie helpen juist om sneller te gaan." },

    { type: "open", vraag: "Leg uit hoe je de snelheid van een object kunt berekenen. Noem de benodigde gegevens en de formule.",
      sleutelwoorden: ["afstand", "tijd", "deel/delen/gedeeld/:"], minTreffers: 2,
      modelantwoord: "Je deelt de afstand door de tijd: snelheid = afstand : tijd. Je hebt dus de afstand en de tijd nodig.",
      uitleg: "Gebruik de formule <b>snelheid = afstand : tijd</b>. Je hebt twee gegevens nodig: de <b>afstand</b> en de <b>tijd</b>." },

    { type: "open", vraag: "Wat betekent het als een schaatser een 'hoge snelheid' heeft tijdens een wedstrijd?",
      sleutelwoorden: ["snel/snelle", "korte tijd/grote afstand/veel afstand/weinig tijd"], minTreffers: 1,
      modelantwoord: "Hij legt in korte tijd een grote afstand af; hij gaat dus heel snel.",
      uitleg: "Een hoge snelheid = veel afstand afleggen in <b>weinig tijd</b>. De schaatser beweegt dus snel." },

    { type: "open", vraag: "Noem twee factoren die de snelheid van een fietser kunnen beïnvloeden.",
      sleutelwoorden: ["wind", "helling/heuvel/berg", "vermoeidheid/moe/conditie", "kracht/trappen", "fiets/banden", "weg/ondergrond"], minTreffers: 2,
      modelantwoord: "Bijvoorbeeld: de wind, een helling, vermoeidheid, of hoeveel kracht je op de trappers zet.",
      uitleg: "Denk aan <b>wind, helling, vermoeidheid, kracht, het soort fiets of de weg</b>. Twee van deze zijn al goed." },

    { type: "open", vraag: "Wat is het verschil tussen snelheid en afstand?",
      sleutelwoorden: ["afstand", "tijd", "weg"], minTreffers: 2,
      modelantwoord: "Afstand is de afgelegde weg. Snelheid is de afgelegde weg per tijd (afstand : tijd).",
      uitleg: "<b>Afstand</b> = hoeveel weg je hebt afgelegd. <b>Snelheid</b> = die weg gedeeld door de tijd die je erover deed." },

    { type: "open", vraag: "Leg uit waarom een schaatser met de kortste tijd wint bij een schaatswedstrijd.",
      sleutelwoorden: ["zelfde/dezelfde/gelijke afstand", "kortste tijd/snelste/minste tijd", "hoogste/grootste snelheid/snelst"], minTreffers: 1,
      modelantwoord: "Iedereen rijdt dezelfde afstand. Wie daar de kortste tijd over doet, had de hoogste snelheid en wint.",
      uitleg: "Bij dezelfde afstand hoort de <b>kortste tijd</b> bij de <b>hoogste snelheid</b> — en de snelste wint." },

    { type: "open", vraag: "Hoe kan een sporter zijn snelheid verhogen?",
      sleutelwoorden: ["trainen/training/oefenen", "kracht/sterker", "techniek", "licht/lichter/materiaal"], minTreffers: 1,
      modelantwoord: "Door te trainen, meer kracht te zetten, zijn techniek te verbeteren of lichtere uitrusting te gebruiken.",
      uitleg: "Meer <b>trainen</b>, meer <b>kracht</b>, een betere <b>techniek</b> of <b>lichter</b> materiaal maken een sporter sneller." },

    { type: "open", vraag: "Geef een voorbeeld van een situatie waarin het belangrijk is om de snelheid te berekenen.",
      sleutelwoorden: ["auto/verkeer/snelweg/rijden", "sport/wedstrijd/hardlopen", "reis/reistijd/hoelang/aankomst", "trein/bus/vliegtuig"], minTreffers: 1,
      modelantwoord: "Bijvoorbeeld in het verkeer (snelheidslimiet), bij een sportwedstrijd, of om te berekenen hoe lang een reis duurt.",
      uitleg: "Snelheid berekenen is handig bij het <b>verkeer</b>, bij <b>sport</b> of om een <b>reistijd</b> te bepalen." },

    { type: "open", vraag: "Waarom is het belangrijk om de eenheden van afstand en tijd correct te gebruiken bij het berekenen van de snelheid?",
      sleutelwoorden: ["eenheid/eenheden/m/km/s/uur", "klopt/fout/verkeerd/juist", "uitkomst/antwoord/snelheid"], minTreffers: 1,
      modelantwoord: "Anders klopt de uitkomst niet. Meters met seconden geeft m/s, kilometers met uren geeft km/u.",
      uitleg: "De eenheden moeten bij elkaar passen: <b>m met s → m/s</b>, <b>km met uur → km/u</b>. Anders is je antwoord fout." },

    { type: "open", vraag: "Leg uit hoe de snelheid van een object verandert als de afstand verdubbelt en de tijd gelijk blijft.",
      sleutelwoorden: ["verdubbelt/twee keer/dubbel/2x", "groter/hoger"], minTreffers: 1,
      modelantwoord: "De snelheid verdubbelt ook: hij wordt twee keer zo groot.",
      uitleg: "snelheid = afstand : tijd. Twee keer zoveel afstand in dezelfde tijd = <b>twee keer zo'n grote snelheid</b>." },

    { type: "open", vraag: "Bedenk een manier waarop je in het dagelijks leven de snelheid van iets kunt meten. Beschrijf hoe je dit zou aanpakken.",
      sleutelwoorden: ["afstand/meetlint/meten", "tijd/stopwatch/seconden", "deel/delen/gedeeld"], minTreffers: 2,
      modelantwoord: "Meet de afstand (bijv. met een meetlint) en de tijd (met een stopwatch). Deel daarna de afstand door de tijd.",
      uitleg: "Meet de <b>afstand</b> en de <b>tijd</b> (stopwatch), en reken dan: snelheid = afstand : tijd." },

    { type: "waaronwaar", vraag: "Snelheid wordt altijd uitgedrukt in meters per seconde (m/s).", antwoord: false,
      uitleg: "Onwaar. Snelheid mag ook in <b>km/u</b> (en andere eenheden). Niet altijd m/s." },

    { type: "waaronwaar", vraag: "Als je harder fietst, wordt je snelheid lager.", antwoord: false,
      uitleg: "Onwaar. Harder fietsen betekent een <b>hogere</b> snelheid." },

    { type: "waaronwaar", vraag: "Een auto die 100 km/u rijdt, legt in 1 uur 100 kilometer af.", antwoord: true,
      uitleg: "Waar. afstand = snelheid × tijd = 100 × 1 = <b>100 km</b>." },

    { type: "waaronwaar", vraag: "Als de afstand die je aflegt groter wordt, maar de tijd hetzelfde blijft, dan wordt je snelheid kleiner.", antwoord: false,
      uitleg: "Onwaar. Meer afstand in dezelfde tijd → de snelheid wordt juist <b>groter</b>." },

    { type: "waaronwaar", vraag: "De schaatser met de langste tijd wint de schaatswedstrijd.", antwoord: false,
      uitleg: "Onwaar. De schaatser met de <b>kortste tijd</b> is het snelst en wint." },

    { type: "waaronwaar", vraag: "Snelheid is hetzelfde als afstand.", antwoord: false,
      uitleg: "Onwaar. Snelheid is afstand <b>per tijd</b> (afstand : tijd), niet de afstand zelf." },

    { type: "waaronwaar", vraag: "Als je de afstand in kilometers meet en de tijd in uren, dan is de eenheid van snelheid km/u.", antwoord: true,
      uitleg: "Waar. Kilometer per uur = <b>km/u</b>." },

    { type: "open", vraag: "Vul aan: Snelheid bereken je door de ______ te delen door de ______.",
      sleutelwoorden: ["afstand", "tijd"], minTreffers: 2,
      modelantwoord: "Snelheid bereken je door de afstand te delen door de tijd.",
      uitleg: "snelheid = <b>afstand</b> : <b>tijd</b>." },

    { type: "open", vraag: "Vul aan: De eenheid van snelheid is vaak ______ of ______.",
      sleutelwoorden: ["m/s / meter per seconde", "km/u / km/h / kilometer per uur"], minTreffers: 1,
      modelantwoord: "De eenheid van snelheid is vaak m/s of km/u.",
      uitleg: "De twee meest gebruikte eenheden zijn <b>m/s</b> (meter per seconde) en <b>km/u</b> (kilometer per uur)." },

    { type: "invul", vraag: "Vul aan: Als je de afstand in meters meet en de tijd in seconden, dan is de eenheid van snelheid ______.",
      antwoord: "m/s|meter per seconde",
      uitleg: "Meter (m) gedeeld door seconde (s) = <b>m/s</b>." },

    { type: "invul", vraag: "Vul aan: Een hogere snelheid betekent dat je in dezelfde tijd een grotere ______ aflegt.",
      antwoord: "afstand|afgelegde afstand|weg",
      uitleg: "Sneller = in dezelfde tijd een grotere <b>afstand</b> afleggen." }
  ]
});

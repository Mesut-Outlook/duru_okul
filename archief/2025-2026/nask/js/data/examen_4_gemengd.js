/* Oefentoets 4 — Gemengd Examen (Hoofdstuk 4 & 6) */
DURU.registerExamen({
  id: "toets-gemengd-h4-h6",
  titel: "Gemengde Oefentoets H4 & H6",
  vak: "Snelheid & Elektriciteit",
  icoon: "🎓",
  duurMin: 30,
  vragen: [
    /* ── MEERKEUZE (6) ── */
    {
      type: "mc",
      vraag: "Wat is de gemiddelde snelheid van een hardloper die 100 meter rent in 10 seconden?",
      opties: ["10 m/s", "10 km/u", "100 m/s", "1 m/s"],
      antwoord: 0,
      uitleg: "De gemiddelde snelheid bereken je met: <b>snelheid = afstand : tijd</b>. Dus 100 m : 10 s = <b>10 m/s</b>."
    },
    {
      type: "mc",
      vraag: "Hoeveel milliampère (mA) is gelijk aan 0,5 ampère (A)?",
      opties: ["50 mA", "500 mA", "5000 mA", "5 mA"],
      antwoord: 1,
      uitleg: "1 ampère (A) is gelijk aan 1000 milliampère (mA). Dus 0,5 A × 1000 = <b>500 mA</b>."
    },
    {
      type: "mc",
      vraag: "Welke meter sluit je parallel aan in een stroomkring?",
      opties: ["De voltmeter", "De ampèremeter", "Beide meters sluit je parallel aan", "Geen van beide meters"],
      antwoord: 0,
      uitleg: "Een <b>voltmeter</b> meet het spanningsverschil over een onderdeel en moet daarom altijd **parallel** (eroverheen) worden aangesloten."
    },
    {
      type: "mc",
      vraag: "Een auto rijdt met een constante snelheid van 72 km/u. Wat is deze snelheid in m/s?",
      opties: ["20 m/s", "259,2 m/s", "7,2 m/s", "2 m/s"],
      antwoord: 0,
      uitleg: "Om te rekenen van km/u naar m/s moet je delen door 3,6. Dus: 72 : 3,6 = <b>20 m/s</b>."
    },
    {
      type: "mc",
      vraag: "Wat gebeurt er met de lampen in een parallelschakeling als één lampje doorbrandt?",
      opties: ["De andere lampen blijven branden", "De andere lampen gaan ook direct uit", "De andere lampen gaan feller branden", "De stroomkring raakt overbelast"],
      antwoord: 0,
      uitleg: "Bij een parallelschakeling heeft elk lampje een eigen verbinding met de spanningsbron. Als één lampje kapot gaat, blijven de andere lampen gewoon <b>branden</b>."
    },
    {
      type: "mc",
      vraag: "Wat is de remafstand van een scooter?",
      opties: ["De afstand die je aflegt tijdens het remmen zelf", "De afstand die je aflegt tijdens je reactietijd", "De reactieafstand plus de stopafstand", "De totale afstand vanaf het moment dat je gevaar ziet tot stilstand"],
      antwoord: 0,
      uitleg: "De <b>remafstand</b> is de afstand die de scooter aflegt vanaf het moment dat je begint met remmen totdat je helemaal stilstaat."
    },

    /* ── WAAR/ONWAAR (5) ── */
    {
      type: "waaronwaar",
      vraag: "Een ampèremeter moet een heel grote weerstand hebben om de stroom goed te meten.",
      antwoord: false,
      uitleg: "Onwaar. Een ampèremeter sluit je in serie aan, dus alle stroom moet erdoorheen. Daarom moet een ampèremeter juist een <b>zeer kleine weerstand</b> hebben."
    },
    {
      type: "waaronwaar",
      vraag: "Stopafstand is gelijk aan de reactieafstand plus de remafstand.",
      antwoord: true,
      uitleg: "Waar. De totale afstand die je aflegt bij een noodstop (de stopafstand) bestaat uit de afstand die je aflegt tijdens het reageren plus de afstand tijdens het remmen."
    },
    {
      type: "waaronwaar",
      vraag: "Lucht is onder normale omstandigheden een goede elektrische geleider.",
      antwoord: false,
      uitleg: "Onwaar. Lucht geleidt stroom normaal gesproken niet. Lucht is een **isolator**."
    },
    {
      type: "waaronwaar",
      vraag: "In een snelheid-tijddiagram (v,t-diagram) stelt een dalende rechte lijn een vertraging voor.",
      antwoord: true,
      uitleg: "Waar. Een dalende lijn in een v,t-diagram betekent dat de snelheid afneemt met de tijd, wat een vertraging is."
    },
    {
      type: "waaronwaar",
      vraag: "In een serieschakeling is de stroomsterkte overal gelijk.",
      antwoord: true,
      uitleg: "Waar. Omdat er in een serieschakeling maar één stroompad is, moet de stroomsterkte (I) overal in de kring **even groot** zijn."
    },

    /* ── OPEN (6) ── */
    {
      type: "open",
      vraag: "Leg uit waarom de stroomsterkte in een serieschakeling overal even groot is.",
      sleutelwoorden: ["één pad/een pad/dezelfde stroomkring/één stroomkring", "elektronen/stroom/lopen", "splitsen/splitsing"],
      minTreffers: 1,
      modelantwoord: "Er is maar één stroomkring/pad waar de stroom doorheen kan lopen. De stroom kan nergens splitsen en is dus overal even groot.",
      uitleg: "Omdat er bij een serieschakeling maar **één stroomweg** is van de plus- naar de minpool, kan de stroom nergens splitsen. De stroomsterkte is overal gelijk."
    },
    {
      type: "open",
      vraag: "Noem het symbool en de eenheid van stroomsterkte.",
      sleutelwoorden: ["I", "ampère/ampere/A"],
      minTreffers: 2,
      modelantwoord: "Het symbool is I en de eenheid is ampère (A).",
      uitleg: "Stroomsterkte heeft als symbool **I** en de eenheid is **ampère (A)**."
    },
    {
      type: "open",
      vraag: "Een fietser rijdt 6 km in 15 minuten. Bereken de gemiddelde snelheid in km/u. Schrijf je berekening op.",
      sleutelwoorden: ["15 minuten/0,25 uur", "24/vierentwintig", "afstand/tijd/deel"],
      minTreffers: 2,
      modelantwoord: "15 minuten = 0,25 uur. snelheid = 6 : 0,25 = 24 km/u.",
      uitleg: "15 minuten is gelijk aan **0,25 uur** (een kwartier). De gemiddelde snelheid is: 6 km : 0,25 uur = <b>24 km/u</b>."
    },
    {
      type: "open",
      vraag: "Wat is het gevaar als je een voltmeter per ongeluk in serie aansluit in plaats van parallel?",
      sleutelwoorden: ["geen stroom/weinig stroom", "grote weerstand/hoge weerstand", "werkt niet/lamp gaat uit"],
      minTreffers: 1,
      modelantwoord: "Een voltmeter heeft een heel grote weerstand. In serie laat hij bijna geen stroom door, waardoor de lampjes in de kring uitgaan.",
      uitleg: "Een voltmeter heeft een **zeer grote weerstand**. Als je deze in serie aansluit, blokkeert hij de stroomkring bijna volledig, waardoor er geen stroom meer loopt."
    },
    {
      type: "open",
      vraag: "Wat is de gemiddelde snelheid (in m/s) van een auto die in 20 seconden een afstand van 300 meter aflegt?",
      sleutelwoorden: ["15/vijftien", "afstand/tijd/deel"],
      minTreffers: 1,
      modelantwoord: "Gemiddelde snelheid = totale afstand : totale tijd = 300 : 20 = 15 m/s.",
      uitleg: "gemiddelde snelheid = totale afstand : totale tijd = 300 m : 20 s = <b>15 m/s</b>."
    },
    {
      type: "open",
      vraag: "Noem twee stoffen die heel goed elektriciteit geleiden en twee stoffen die dat juist niet doen (isolatoren).",
      sleutelwoorden: ["koper/ijzer/aluminium/goud/zilver/metaal/metalen", "plastic/rubber/hout/glas/steen/lucht"],
      minTreffers: 3,
      modelantwoord: "Geleiders: koper en ijzer. Isolatoren: plastic en rubber.",
      uitleg: "Goede geleiders zijn **metalen** zoals **koper**, **ijzer** of **aluminium**. Goede isolatoren zijn bijvoorbeeld **plastic**, **rubber**, **glas** of **hout**."
    },

    /* ── INVUL (3) ── */
    {
      type: "invul",
      vraag: "Vul aan: Om milliampère (mA) om te rekenen naar ampère (A), moet je het getal delen door ______.",
      antwoord: "1000|1.000|duizend",
      uitleg: "Er gaan 1000 milliampère in 1 ampère. Dus omrekenen van mA naar A doe je door te delen door <b>1000</b>."
    },
    {
      type: "invul",
      vraag: "Vul aan: Een object dat in een afstand-tijddiagram (a,t-diagram) een horizontale rechte lijn heeft, staat ______.",
      antwoord: "stil|stille",
      uitleg: "Als de afstand (plaats) in de loop van de tijd niet verandert, betekent dit dat het object **stil** staat."
    },
    {
      type: "invul",
      vraag: "Vul aan: De spanning van het Nederlandse stopcontact thuis (het lichtnet) is ______ volt.",
      antwoord: "230|tweehonderddertig",
      uitleg: "De standaardspanning van het lichtnet in Nederland is <b>230 volt (V)</b>."
    }
  ]
});

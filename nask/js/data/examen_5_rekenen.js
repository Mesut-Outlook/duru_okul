/* Oefentoets 5 — Rekenen & Formules (Hoofdstuk 4 & 6) */
DURU.registerExamen({
  id: "toets-rekenen",
  titel: "Oefentoets Rekenen & Formules",
  vak: "Formules & Rekensommen",
  icoon: "📐",
  duurMin: 25,
  vragen: [
    /* ── MEERKEUZE (5) ── */
    {
      type: "mc",
      vraag: "Een auto rijdt met een snelheid van 90 km/u. Welke berekening gebruik je om dit om te rekenen naar m/s?",
      opties: ["90 : 3,6", "90 × 3,6", "90 + 3,6", "90 : 1000"],
      antwoord: 0,
      uitleg: "Om om te rekenen van kilometer per uur (km/u) naar meter per seconde (m/s) moet je de snelheid <b>delen door 3,6</b>."
    },
    {
      type: "mc",
      vraag: "Een fietser rijdt 12 m/s. Hoeveel km/u is dat?",
      opties: ["43,2 km/u", "3,3 km/u", "12 km/u", "120 km/u"],
      antwoord: 0,
      uitleg: "Om om te rekenen van m/s naar km/u moet je de snelheid vermenigvuldigen met 3,6. Dus: 12 × 3,6 = <b>43,2 km/u</b>."
    },
    {
      type: "mc",
      vraag: "Een lamp verbruikt een stroomsterkte van 150 mA. Hoeveel ampère (A) is dit?",
      opties: ["0,15 A", "1,5 A", "15 A", "0,015 A"],
      antwoord: 0,
      uitleg: "Om van milliampère naar ampère te rekenen, deel je door 1000. Dus: 150 mA : 1000 = <b>0,15 A</b>."
    },
    {
      type: "mc",
      vraag: "Een brommer rijdt 54 km/u. Hoeveel meter legt de brommer af in 10 seconden?",
      opties: ["150 meter", "540 meter", "5,4 meter", "15 meter"],
      antwoord: 0,
      uitleg: "Reken eerst 54 km/u om naar m/s: 54 : 3,6 = 15 m/s. De afstand bereken je daarna met: snelheid × tijd = 15 m/s × 10 s = <b>150 meter</b>."
    },
    {
      type: "mc",
      vraag: "De spanning over drie identieke in serie geschakelde lampjes is in totaal 12 V. Wat is de spanning over elk afzonderlijk lampje?",
      opties: ["4 V", "12 V", "36 V", "3 V"],
      antwoord: 0,
      uitleg: "Bij een serieschakeling wordt de totale spanning verdeeld over de onderdelen. Omdat de lampjes gelijk zijn, krijgt ieder: 12 V : 3 = <b>4 V</b>."
    },

    /* ── WAAR/ONWAAR (3) ── */
    {
      type: "waaronwaar",
      vraag: "Als je de snelheid (v) vermenigvuldigt met de tijd (t), bereken je de afstand (s).",
      antwoord: true,
      uitleg: "Waar. De formule voor afstand is: <b>afstand = snelheid × tijd</b> (s = v × t)."
    },
    {
      type: "waaronwaar",
      vraag: "Een reactietijd van 1,2 seconden is sneller (beter) dan een reactietijd van 0,8 seconden.",
      antwoord: false,
      uitleg: "Onwaar. Een langere tijd (1,2 s in plaats van 0,8 s) betekent dat het langer duurt voordat je reageert, dus ben je **trager**."
    },
    {
      type: "waaronwaar",
      vraag: "Drie lampen staan parallel aangesloten op een batterij van 9 V. De spanning over elke lamp is dan 9 V.",
      antwoord: true,
      uitleg: "Waar. In een parallelschakeling staat elk lampje direct in verbinding met de spanningsbron en krijgt dus de **volle spanning** (in dit geval 9 V)."
    },

    /* ── OPEN (4) ── */
    {
      type: "open",
      vraag: "Een wandelaar loopt met een constante snelheid van 5 km/u. Hoeveel kilometer legt hij af in 2 uur en 30 minuten? Schrijf je berekening op.",
      sleutelwoorden: ["2,5 uur/twee en een half uur/2.5 uur", "12,5/12.5/twaalfenhalf", "vermenigvuldig/keer/snelheid * tijd"],
      minTreffers: 2,
      modelantwoord: "2 uur en 30 minuten = 2,5 uur. Afstand = snelheid × tijd = 5 × 2,5 = 12,5 km.",
      uitleg: "Zet eerst de tijd om naar uren: 2 uur en 30 minuten = **2,5 uur**. Bereken daarna de afstand: 5 km/u × 2,5 uur = <b>12,5 km</b>."
    },
    {
      type: "open",
      vraag: "Een hardloper loopt met een snelheid van 4 m/s. Hoeveel seconden doet hij over een afstand van 1 km? Schrijf je berekening op.",
      sleutelwoorden: ["1000 meter/1000m", "250/tweehonderdvijftig", "deel/tijd = afstand / snelheid"],
      minTreffers: 2,
      modelantwoord: "1 km = 1000 meter. Tijd = afstand : snelheid = 1000 : 4 = 250 seconden.",
      uitleg: "Reken eerst de kilometer om naar meters: 1 km = **1000 meter**. Bereken daarna de tijd: 1000 meter : 4 m/s = <b>250 seconden</b> (dat is 4 minuten en 10 seconden)."
    },
    {
      type: "open",
      vraag: "In een parallelschakeling met twee lampen is de totale stroomsterkte van de batterij 1,2 A. De stroom door lamp 1 is 0,4 A. Bereken de stroomsterkte door lamp 2.",
      sleutelwoorden: ["0,8/0.8", "min/er vanaf/1,2 - 0,4"],
      minTreffers: 1,
      modelantwoord: "In een parallelschakeling splitsen de stromen. Dus stroom 2 = totale stroom - stroom 1 = 1,2 - 0,4 = 0,8 A.",
      uitleg: "Bij een parallelschakeling splitsen de stromen zich. De totale stroomsterkte is de som van de takstromen (I_totaal = I1 + I2). Dus: I2 = 1,2 A - 0,4 A = <b>0,8 A</b>."
    },
    {
      type: "open",
      vraag: "Een auto rijdt 25 m/s. De bestuurder ziet gevaar en remt na 0,8 s (reactietijd). De auto staat na nog eens 40 meter remmen stil. Bereken de totale stopafstand.",
      sleutelwoorden: ["20/twintig meter", "60/zestig meter", "stopafstand/reactieafstand/remafstand"],
      minTreffers: 2,
      modelantwoord: "Reactieafstand = 25 × 0,8 = 20 meter. Stopafstand = 20 + 40 = 60 meter.",
      uitleg: "1) Bereken de reactieafstand: 25 m/s × 0,8 s = **20 meter**.<br>2) Tel de remafstand hierbij op voor de stopafstand: 20 m + 40 m = <b>60 meter</b>."
    },

    /* ── INVUL (3) ── */
    {
      type: "invul",
      vraag: "Vul aan: Een fietser die 15 km aflegt in 45 minuten, heeft een gemiddelde snelheid van ______ km/u.",
      antwoord: "20|twintig",
      uitleg: "45 minuten = 0,75 uur. De gemiddelde snelheid is: 15 km : 0,75 uur = <b>20 km/u</b>."
    },
    {
      type: "invul",
      vraag: "Vul aan: Een elektrische stroom van 1500 mA is gelijk aan ______ A.",
      antwoord: "1,5|1.5",
      uitleg: "Van mA naar A deel je door 1000. Dus: 1500 mA : 1000 = <b>1,5 A</b>."
    },
    {
      type: "invul",
      vraag: "Vul aan: s = v × t. Als s = 100 meter en v = 20 m/s, dan is de tijd t = ______ seconden.",
      antwoord: "5|vijf",
      uitleg: "tijd = afstand : snelheid (t = s : v). Dus: 100 : 20 = <b>5 seconden</b>."
    }
  ]
});

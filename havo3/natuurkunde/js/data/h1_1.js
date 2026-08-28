/* Onderwerp 1.1 — Kracht bij beweging */
DURU.register({
  id: "h1-1-kracht-beweging",
  hoofdstuk: 1,
  paragraaf: "1.1",
  titel: "Kracht bij beweging",
  korteUitleg: "Wat doet een kracht met een beweging en hoe bereken je de resulterende kracht?",
  icoon: "🎯",
  kleur: "h1-thema",
  theorie: "<h3>1.1 Kracht bij beweging</h3><div class=\"formule-box\"><strong>Resulterende kracht (F_res):</strong><br>De som van alle krachten die op een voorwerp werken.<br>• Krachten in dezelfde richting: optellen (F_res = F1 + F2)<br>• Krachten in tegengestelde richting: aftrekken (F_res = F_vooruit - F_tegen)</div><h4>Wat doet een kracht met de snelheid?</h4><ul><li><b>F_res > 0 in de bewegingsrichting:</b> De snelheid neemt toe (de beweging is <b>versneld</b>).</li><li><b>F_res > 0 tegen de bewegingsrichting in:</b> De snelheid neemt af (de beweging is <b>vertraagd</b>).</li><li><b>F_res = 0 N (krachten heffen elkaar op):</b> De snelheid blijft constant (de beweging is <b>eenparig</b>) of het voorwerp blijft stilstaan.</li></ul><h4>Tegenwerkende krachten</h4><p>Bij bewegende voorwerpen werken meestal twee belangrijke wrijvingskrachten tegen: de <b>luchtweerstand (F_l)</b> en de <b>rolweerstand (F_r)</b>.</p>",
  vragen: [
    {
      type: "mc",
      niveau: 1,
      vraag: "Wat is de eenheid van kracht?",
      opties: ["Newton", "Joule", "Watt", "Kilogram"],
      antwoord: 0,
      uitleg: "Kracht wordt aangeduid met F en gemeten in Newton (N)."
    },
    {
      type: "mc",
      niveau: 1,
      vraag: "Een fietser trapt met 80 N voorwaarts. De tegenwerkende wrijving is 50 N. Wat is de resulterende kracht?",
      opties: ["130 N voorwaarts", "30 N voorwaarts", "50 N tegenwerkend", "0 N"],
      antwoord: 1,
      uitleg: "Fres = 80 N - 50 N = 30 N voorwaarts."
    },
    {
      type: "waaronwaar",
      niveau: 1,
      vraag: "Als de resulterende kracht 0 N is, moet een voorwerp altijd stilstaan.",
      antwoord: false,
      uitleg: "Niet waar: het kan ook met constante snelheid in een rechte lijn blijven bewegen (eenparige beweging)."
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "Een auto heeft een motorkracht van 1500 N en beweegt met constante snelheid. Hoeveel Newton is de totale tegenwerkende wrijvingskracht?",
      antwoord: "1500|1500 N|1500N",
      uitleg: "Bij constante snelheid is Fres = 0, dus de tegenwerkende kracht is gelijk aan de motorkracht: 1500 N."
    },
    {
      type: "mc",
      niveau: 2,
      vraag: "Welke twee krachten vormen samen de tegenwerkende kracht bij een rijdende auto?",
      opties: ["Zwaartekracht en motorkracht", "Spierkracht en veerkracht", "Luchtweerstand en rolweerstand", "Massa en versnelling"],
      antwoord: 2,
      uitleg: "Luchtweerstand (wrijving met lucht) en rolweerstand (wrijving tussen banden en wegdek)."
    },
    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "Als je twee keer zo snel fietst, wordt de luchtweerstand vier keer zo groot.",
      antwoord: true,
      uitleg: "Waar: luchtweerstand stijgt kwadratisch met de snelheid (2² = 4)."
    },
    {
      type: "invoer",
      niveau: 3,
      vraag: "Drie sleepboten trekken aan een schip naar voren met krachten van 20 kN, 35 kN en 25 kN. De waterweerstand is 60 kN. Hoeveel kN is de resulterende kracht?",
      antwoord: "20|20 kN|20kN",
      uitleg: "Totale voorwaartse kracht = 20 + 35 + 25 = 80 kN. Fres = 80 - 60 = 20 kN."
    }
  ]
});

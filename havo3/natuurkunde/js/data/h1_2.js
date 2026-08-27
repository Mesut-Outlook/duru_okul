/* Onderwerp 1.2 — Soorten beweging */
DURU.register({
  id: "h1-2-soorten-beweging",
  hoofdstuk: 1,
  paragraaf: "1.2",
  titel: "Soorten beweging & Diagrammen",
  korteUitleg: "Herken bewegingssoorten in (s,t)- en (v,t)-diagrammen en reken met snelheid en afstand.",
  icoon: "📈",
  kleur: "h1-thema",
  theorie: "<h3>1.2 Soorten beweging</h3><div class=\"formule-box\"><strong>Snelheid berekenen:</strong><br>v_gem = s / t &nbsp;&nbsp;|&nbsp;&nbsp; s = v × t &nbsp;&nbsp;|&nbsp;&nbsp; t = s / v<br><br><strong>Omrekenen eenheden:</strong><br>• m/s → vermenigvuldig met 3,6 → km/h<br>• km/h → deel door 3,6 → m/s</div><h4>Diagrammen herkennen</h4><ul><li><b>(s,t)-diagram:</b> De helling stelt de <b>snelheid</b> voor. Een rechte schuine lijn = constante snelheid; horizontale lijn = stilstand.</li><li><b>(v,t)-diagram:</b> De helling stelt de <b>versnelling</b> voor. Horizontale lijn = constante snelheid; schuin omhoog = eenparig versneld; schuin omlaag = eenparig vertraagd.</li><li><b>Afstand uit (v,t)-diagram:</b> De <b>oppervlakte</b> onder de grafiek is gelijk aan de afgelegde afstand s.</li></ul>",
  vragen: [
    {
      type: "mc",
      niveau: 1,
      vraag: "Wat betekent een horizontale rechte lijn in een (v,t)-diagram?",
      opties: ["Het voorwerp staat stil", "Het voorwerp beweegt met constante snelheid", "Het voorwerp versnelt", "Het voorwerp vertraagt"],
      antwoord: 1,
      uitleg: "In een (v,t)-diagram geeft een horizontale lijn aan dat de snelheid v niet verandert (constante snelheid)."
    },
    {
      type: "invoer",
      niveau: 1,
      vraag: "Reken om: 90 km/h is gelijk aan hoeveel m/s?",
      antwoord: "25|25 m/s|25,0",
      uitleg: "90 / 3,6 = 25 m/s."
    },
    {
      type: "invoer",
      niveau: 1,
      vraag: "Reken om: 15 m/s is gelijk aan hoeveel km/h?",
      antwoord: "54|54 km/h|54,0",
      uitleg: "15 × 3,6 = 54 km/h."
    },
    {
      type: "mc",
      niveau: 2,
      vraag: "Hoe bereken je de afgelegde afstand s uit een (v,t)-diagram?",
      opties: ["Eindsnelheid vermenigvuldigen met de helling", "De oppervlakte onder de grafieklijn bepalen", "De hoogste snelheid aflezen", "De tijd delen door de eindsnelheid"],
      antwoord: 1,
      uitleg: "De oppervlakte onder de (v,t)-grafiek stelt de afgelegde afstand s voor."
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "Een scooter trekt eenparig op van stilstand naar 12 m/s in 6,0 s. Bereken de afgelegde afstand in meters (oppervlakte van de driehoek = 0,5 × v × t).",
      antwoord: "36|36 m|36,0",
      uitleg: "s = 0,5 × basis × hoogte = 0,5 × 6,0 s × 12 m/s = 36 meter."
    },
    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "In een (s,t)-diagram betekent een kromme lijn die steeds steiler omhoog loopt dat de beweging versnelt.",
      antwoord: true,
      uitleg: "Waar: steiler worden in een (s,t)-diagram betekent dat de snelheid toeneemt."
    },
    {
      type: "invoer",
      niveau: 3,
      vraag: "Een fietser rijdt 20 seconden met 6,0 m/s en remt daarna in 4,0 seconden gelijkmatig af tot stilstand. Wat is de totale afgelegde afstand in meters?",
      antwoord: "132|132 m|132,0",
      uitleg: "Deel 1 (rechthoek): 20 s × 6,0 m/s = 120 m. Deel 2 (driehoek): 0,5 × 4,0 s × 6,0 m/s = 12 m. Totaal = 120 + 12 = 132 meter."
    }
  ]
});

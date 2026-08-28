/* Onderwerp 8.2 — Rekenen aan hefbomen */
DURU.register({
  id: "h8-2-rekenen-hefbomen",
  hoofdstuk: 8,
  paragraaf: "8.2",
  titel: "Rekenen aan Hefbomen & Momenten",
  korteUitleg: "Het moment van een kracht (M = F × r), de momentenwet en het zwaartepunt.",
  icoon: "⚖️",
  kleur: "h8-thema",
  theorie: "<h3>8.2 Rekenen aan hefbomen</h3><div class='formule-box'><strong>Formules:</strong><br>• <b>Moment van een kracht ($):</b> 89565M = F \times r89565 ($ in $\text{Nm}$, $ in $\text{N}$, $ in $\text{m}$)<br>• <b>Hefboomwet / Momentenwet in evenwicht:</b> 89565M_{\text{links}} = M_{\text{rechts}} \iff F_1 \times r_1 = F_2 \times r_289565<br>• <b>Zwaartekracht:</b>  = m \times g$ ( \approx 10\text{ N/kg}$ of {,}8\text{ N/kg}$)</div><h4>Het Zwaartepunt ($)</h4><p>Het zwaartepunt is het punt waar je de totale zwaartekracht op het voorwerp geconcentreerd kunt denken. Een hefboom is stabiel als het zwaartepunt zich recht onder het ophangpunt bevindt.</p>",
  vragen: [
    {
      type: "invoer",
      niveau: 1,
      vraag: "Een kracht van 50 N werkt op een arm van 0,40 m. Hoe groot is het moment in Nm?",
      antwoord: "20|20 Nm",
      uitleg: "M = F × r = 50 N × 0,40 m = 20 Nm."
    },
    {
      type: "invoer",
      niveau: 1,
      vraag: "Welke eenheid hoort bij het moment van een kracht (symbool)?",
      antwoord: "Nm|Newtonmeter",
      uitleg: "Nm = Newtonmeter."
    },
    {
      type: "mc",
      niveau: 2,
      vraag: "Op een wipwap zit Daan (400 N) op 1,5 m van het draaipunt. Sophie weegt 300 N. Op welke afstand moet Sophie zitten voor evenwicht?",
      opties: ["2,0 m", "1,8 m", "2,5 m", "1,2 m"],
      antwoord: 0,
      uitleg: "r_Sophie = (400 × 1,5) / 300 = 600 / 300 = 2,0 m."
    },
    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "In evenwicht is de som van alle linksdraaiende momenten gelijk aan de som van alle rechtsdraaiende momenten.",
      antwoord: true,
      uitleg: "Waar: de momentenwet."
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "Een kruiwagen bevat 600 N zand op een arm van 30 cm van het wiel. De handvatten zitten op 90 cm. Welke tilkracht in Newton is nodig?",
      antwoord: "200|200 N",
      uitleg: "F = (600 × 30) / 90 = 18.000 / 90 = 200 N."
    },
    {
      type: "waaronwaar",
      niveau: 3,
      vraag: "Als je de spierkracht verdubbelt en de arm halveert, blijft het moment exact gelijk.",
      antwoord: true,
      uitleg: "Waar: (2F) × (0,5r) = F × r."
    }
  ]
});

/* Onderwerp 8.5 — Vloeistofdruk & Hydraulica */
DURU.register({
  id: "h8-5-vloeistofdruk",
  hoofdstuk: 8,
  paragraaf: "8.5",
  titel: "Vloeistofdruk & Hydraulica",
  korteUitleg: "De Wet van Pascal, werking van hydraulische persen, krikken en voertuigremmen.",
  icoon: "💧",
  kleur: "h8-thema",
  theorie: "<h3>8.5 Vloeistofdruk en hydraulica</h3><div class='formule-box'><strong>De Wet van Pascal:</strong><br>In een afgesloten vloeistofsysteem plant een uitgeoefende druk zich in alle richtingen gelijkmatig voort.<br><br>89565p = \frac{F_1}{A_1} = \frac{F_2}{A_2} \implies F_2 = F_1 \times \frac{A_2}{A_1}89565</div><h4>Eigenschappen van hydraulische systemen</h4><ul><li>Vloeistoffen (zoals hydraulische olie) zijn <b>niet samendrukbaar</b>.</li><li>Als zuiger 2 een 0\times$ groter oppervlak heeft ( = 10 \times A_1$), levert het een 0\times$ grotere kracht ( = 10 \times F_1$).</li><li>Volgens de Gouden Regel verplaatst zuiger 2 zich dan wel 0\times$ minder ver ( = s_1 / 10$).</li><li>Toepassingen: autoremmen, hydraulische krik, graafmachines, laadkleppen.</li></ul>",
  vragen: [
    {
      type: "mc",
      niveau: 1,
      vraag: "Welke stof is in tegenstelling tot gassen vrijwel NIET samendrukbaar?",
      opties: ["Vloeistoffen (zoals olie en water)", "Lucht", "Zuurstofgas", "Stoom"],
      antwoord: 0,
      uitleg: "Vloeistofmoleculen zitten al dicht op elkaar en zijn niet samendrukbaar."
    },
    {
      type: "invoer",
      niveau: 1,
      vraag: "In een hydraulische pers is zuiger 2 tien keer zo groot als zuiger 1 (A₂ = 10 × A₁). Je duwt op zuiger 1 met 40 N. Hoeveel Newton kracht levert zuiger 2?",
      antwoord: "400|400 N",
      uitleg: "40 N × 10 = 400 N."
    },
    {
      type: "mc",
      niveau: 2,
      vraag: "In de vorige vraag duw je zuiger 1 over een afstand van 20 cm omlaag. Hoeveel cm gaat zuiger 2 omhoog?",
      opties: ["20 cm", "2 cm", "200 cm", "10 cm"],
      antwoord: 1,
      uitleg: "s₂ = s₁ / 10 = 20 / 10 = 2 cm (Gouden Regel)."
    },
    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "Als er luchtbellen in de remvloeistof van een auto zitten, voelt het rempedaal sponzig aan en remt de auto slecht.",
      antwoord: true,
      uitleg: "Waar: lucht wordt eerst samengedrukt waardoor de remkracht niet direct overkomt."
    },
    {
      type: "mc",
      niveau: 2,
      vraag: "Wie formuleerde de wet over drukvoortplanting in vloeistoffen?",
      opties: ["James Watt", "Isaac Newton", "Blaise Pascal", "Albert Einstein"],
      antwoord: 2,
      uitleg: "Blaise Pascal (Wet van Pascal)."
    },
    {
      type: "waaronwaar",
      niveau: 3,
      vraag: "Met een hydraulisch systeem kun je kracht vergroten, maar niet de verrichte arbeid.",
      antwoord: true,
      uitleg: "Waar: W = F × s blijft constant."
    }
  ]
});

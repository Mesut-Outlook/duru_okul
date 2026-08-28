/* Onderwerp 8.3 — Overbrengingen */
DURU.register({
  id: "h8-3-overbrengingen",
  hoofdstuk: 8,
  paragraaf: "8.3",
  titel: "Overbrengingen: Katrollen & Tandwielen",
  korteUitleg: "Vaste en losse katrollen, takels, de gouden regel van de mechanica en tandwieloverbrengingen.",
  icoon: "⚙️",
  kleur: "h8-thema",
  theorie: "<h3>8.3 Overbrengingen</h3><div class='formule-box'><strong>Katrollen & Takels:</strong><br>• <b>Vaste katrol:</b> {\text{spier}} = F_{\text{last}}$ en {\text{touw}} = s_{\text{last}}$ (alleen richting verandert).<br>• <b>Losse katrol:</b> {\text{spier}} = \frac{1}{2} F_{\text{last}}$ en {\text{touw}} = 2 \times s_{\text{last}}$ (kracht halveert, afstand verdubbelt).<br>• <b>Takel met $ dragende touwen:</b> 89565F_{\text{spier}} = \frac{F_{\text{last}}}{n} \quad \text{en} \quad s_{\text{touw}} = n \times s_{\text{last}}89565</div><div class='info-box let-op'><span class='kop'>✨ De Gouden Regel van de Mechanica</span>Wat je wint aan kracht, verlies je aan afstand (arbeid  = F \times s$ blijft behouden).</div>",
  vragen: [
    {
      type: "mc",
      niveau: 1,
      vraag: "Wat doet een vaste katrol?",
      opties: ["Verandert alleen de trekrichting van de kracht", "Halveert de benodigde kracht", "Vergroot de afstand", "Verlaagt het gewicht"],
      antwoord: 0,
      uitleg: "Vaste katrol verandert alleen de richting."
    },
    {
      type: "invoer",
      niveau: 1,
      vraag: "Je tilt 800 N op met een losse katrol. Hoeveel spierkracht in Newton is nodig?",
      antwoord: "400|400 N",
      uitleg: "800 / 2 = 400 N."
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "Bij een takel met 4 touwen wil je de last 3 meter hijsen. Hoeveel meter touw moet je binnenhalen?",
      antwoord: "12|12 m|12 meter",
      uitleg: "4 × 3 m = 12 m."
    },
    {
      type: "mc",
      niveau: 2,
      vraag: "Tandwiel 1 (30 tanden) drijft tandwiel 2 (10 tanden) aan. Als tandwiel 1 één omwenteling maakt, hoeveel omwentelingen maakt tandwiel 2 dan?",
      opties: ["1 omwenteling", "3 omwentelingen", "0,33 omwentelingen", "30 omwentelingen"],
      antwoord: 1,
      uitleg: "30 / 10 = 3 omwentelingen."
    },
    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "Twee tandwielen die in elkaar grijpen draaien in dezelfde richting.",
      antwoord: false,
      uitleg: "Niet waar: ze draaien in tegengestelde richting."
    },
    {
      type: "waaronwaar",
      niveau: 3,
      vraag: "Volgens de gouden regel kun je met een takel wel kracht besparen maar geen arbeid (energie).",
      antwoord: true,
      uitleg: "Waar: arbeid W = F × s blijft constant."
    }
  ]
});

DURU.register({
  id: "h2-1-verhoudingstabel",
  hoofdstuk: 2,
  paragraaf: "2.1",
  titel: "2.1 Verhoudingstabel & Percentages",
  korteUitleg: "Berekeningen met verhoudingstabellen, via 1 rekenen, korting ve bedrag/aantal.",
  icoon: "➗",
  theorie: `
    <h3>Paragraaf 2.1 — Verhoudingstabel & Percentages</h3>
    <p>In de statistiek en dagelijks leven (zoals kortingen in winkel of stijging van aantallen) bereken je vaak percentages met een <strong>verhoudingstabel</strong>.</p>

    <div class="formule-box">
      <strong>Stappenplan berekening met verhoudingstabel:</strong><br>
      1. Maak een verhoudingstabel en vul de bekende gegevens in.<br>
      2. Reken altijd eerst via <strong>1</strong> (in het midden).<br>
      3. Bepaal de vermenigvuldiging en deling (de pijlen boven en onder).<br>
      4. Reken met niet-afgeronde tussenantwoorden op je rekenmachine en rond alleen de einduitkomst af!
    </div>

    <div class="voorbeeld">
      <div class="vb-kop">Voorbeeld 1: Kortingspercentage berekenen</div>
      <p>José krijgt € 20,- korting op een e-reader van € 109,10. Hoeveel procent korting is dat?</p>
      <div class="stap">
        <strong>Uitwerking:</strong><br>
        • De oude prijs (€ 109,10) komt overeen met 100%.<br>
        • Reken van 109,10 naar 1 (delen door 109,10) en dan naar 20 (keer 20).<br>
        • Percentage: <code>100 ÷ 109,10 × 20 = 18,331...%</code> → Afgerond <strong>18,3%</strong> korting.
      </div>
    </div>

    <div class="info-box let-op">
      <strong>Let op:</strong> Als het totaal gegeven is, hoort dat totaal altijd bij <strong>100%</strong>. Vraag je naar het originele bedrag voordat er korting/btw op kwam? Dan is de originele prijs 100%!
    </div>
  `,
  vragen: [
    {
      type: "mc",
      niveau: 1,
      vraag: "Een trui kost normaal € 40,-. Je krijgt € 12,- korting. Hoeveel procent korting is dit?",
      opties: ["25%", "30%", "33,3%", "40%"],
      antwoord: 1,
      uitleg: "12 ÷ 40 × 100% = 30%. Via de verhoudingstabel: 100% ÷ 40 × 12 = 30%."
    },
    {
      type: "waaronwaar",
      niveau: 1,
      vraag: "Bij tussenberekeningen in een verhoudingstabel op je rekenmachine moet je tussendoor al afronden op hele getallen.",
      antwoord: false,
      uitleg: "Onwaar. Je moet op je rekenmachine altijd verder rekenen met niet-afgeronde tussenantwoorden om afrondfouten te voorkomen!"
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "Op een jas van € 16,50 krijgt Margriet 40% korting. Hoeveel euro korting krijgt Margriet?",
      antwoord: "6,60|6,6",
      eenheid: "€",
      tolerantie: 0.05,
      uitleg: "16,50 ÷ 100 × 40 = € 6,60 korting."
    },
    {
      type: "mc",
      niveau: 2,
      vraag: "Een BMX-club heeft 103 leden jonger dan 16 jaar. Dat is 77% van alle leden van de club. Hoeveel leden heeft de club in totaal? (Rond af op een geheel getal).",
      opties: ["130", "134", "138", "142"],
      antwoord: 1,
      uitleg: "77% corresponds to 103 members. 100% = 103 ÷ 77 × 100 = 133,76... → afgerond 134 leden."
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "Een trui kost in de uitverkoop € 34,20 na 10% korting (dus 90% van de originele prijs). Wat was de originele prijs in euro's?",
      antwoord: "38|38,00",
      eenheid: "€",
      tolerantie: 0.05,
      uitleg: "34,20 corresponds to 90%. 100% = 34,20 ÷ 90 × 100 = € 38,-."
    },
    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "Als een getal van 169 stijgt naar 242, is de stijging in procenten gelijk aan (73 ÷ 169) × 100%.",
      antwoord: true,
      uitleg: "Waar. De absolute stijging is 242 - 169 = 73. Procentuele stijging = (toename ÷ oud) × 100% = (73 ÷ 169) × 100% = 43,2%."
    },
    {
      type: "mc",
      niveau: 3,
      vraag: "Een flatscreen tv kost inclusief 21% btw € 242,-. Wat is de prijs exclusief btw?",
      opties: ["€ 191,18", "€ 200,-", "€ 205,-", "€ 210,-"],
      antwoord: 1,
      uitleg: "Inclusief 21% btw betekent dat € 242,- overeenkomt met 121%. Exclusief btw (100%) = 242 ÷ 121 × 100 = € 200,-."
    },
    {
      type: "invoer",
      niveau: 3,
      vraag: "In een aquarium van 50 liter zit 33,5 liter water. Voor hoeveel procent is het aquarium gevuld?",
      antwoord: "67",
      eenheid: "%",
      tolerantie: 0.1,
      uitleg: "(33,5 ÷ 50) × 100% = 67%."
    }
  ]
});

DURU.register({
  id: "h2-3-frequentietabel",
  hoofdstuk: 2,
  paragraaf: "2.3",
  titel: "2.3 Frequentietabel, Staafdiagram & Lijndiagram",
  korteUitleg: "Frequenties, frequentietabellen maken/aflezen, staafdiagrammen en lijndiagrammen (tijdverloop).",
  icoon: "📈",
  theorie: `
    <h3>Paragraaf 2.3 — Frequentietabel & Diagrammen</h3>
    <p>Als je onderzoek doet en gegevens verzamelt, orden je de gegevens in een tabel of grafiek.</p>

    <div class="formule-box">
      <strong>Kernbegrippen:</strong><br>
      • <strong>Frequentie:</strong> Het aantal keren dat een waarde voorkomt.<br>
      • <strong>Frequentietabel:</strong> Een tabel waarin de waarden en hun bijbehorende frequentie vermeld staan.<br>
      • <strong>Staafdiagram:</strong> Een diagram waarin de hoogtes van de staven de frequenties aangeven. De staven staan los van elkaar.<br>
      • <strong>Lijndiagram:</strong> Wordt vooral gebruikt om te laten zien hoe aantallen <em>in de loop van de tijd veranderen</em> (tijdverloop).
    </div>

    <div class="voorbeeld">
      <div class="vb-kop">Voorbeeld: Frequentie tellen</div>
      <p>Sandra haalde voor wiskunde de cijfers: 7, 5, 8, 6, 6, 7, 5, 7, 7, 6.</p>
      <div class="stap">
        • Cijfer 5 komt 2 keer voor → Frequentie van 5 is <strong>2</strong>.<br>
        • Cijfer 6 komt 3 keer voor → Frequentie van 6 is <strong>3</strong>.<br>
        • Cijfer 7 komt 4 keer voor → Frequentie van 7 is <strong>4</strong>.<br>
        • Cijfer 8 komt 1 keer voor → Frequentie van 8 is <strong>1</strong>.<br>
        • Totale frequentie (aantal proefwerken) = 2 + 3 + 4 + 1 = <strong>10</strong>.
      </div>
    </div>
  `,
  vragen: [
    {
      type: "mc",
      niveau: 1,
      vraag: "Wat betekent het woord 'frequentie' in de statistiek?",
      opties: [
        "Het gemiddelde van alle getallen",
        "Het aantal keren dat een waarde voorkomt",
        "Het verschil tussen de hoogste en laagste waarde",
        "Het middelste getal van een rij"
      ],
      antwoord: 1,
      uitleg: "Frequentie is het aantal keren dat een bepaalde waarde voorkomt."
    },
    {
      type: "mc",
      niveau: 1,
      vraag: "Welk diagram gebruik je bij voorkeur om te laten zien hoe de temperatuur in de loop van een dag verandert?",
      opties: ["Cirkeldiagram", "Staafdiagram", "Lijndiagram", "Beelddiagram"],
      antwoord: 2,
      uitleg: "Een lijndiagram is uitermate geschikt om verandering in de loop van de tijd (tijdverloop) weer te geven."
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "Een fietshandelaar verkoopt 15 blauwe, 22 rode en 17 gele fietsen. Wat is de totale frequentie van de verkochte fietsen?",
      antwoord: "54",
      tolerantie: 0.1,
      uitleg: "Totale frequentie = 15 + 22 + 17 = 54 fietsen."
    },
    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "In een staafdiagram moeten de staven tegen elkaar aan getekend worden zonder ruimte er tussen.",
      antwoord: false,
      uitleg: "Onwaar. Bij een staafdiagram staan de staven los van elkaar (losse categorieën)."
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "Arjan verkocht in 2020 racefietsen van merken: Cannondale (85), Felt (57), Giant (115), Specialized (97) en Trek (72). Hoe groot is de frequentie van Giant?",
      antwoord: "115",
      tolerantie: 0.1,
      uitleg: "Giant is 115 keer verkocht, dus de frequentie is 115."
    },
    {
      type: "mc",
      niveau: 3,
      vraag: "In een lijndiagram staat de verkoop van jus d'orange in pakken: Jan (120), Feb (150), Maart (180), April (240). Hoeveel pakken zijn er in het 1e kwartaal (Jan+Feb+Maart) totaal verkocht?",
      opties: ["390", "450", "510", "690"],
      antwoord: 1,
      uitleg: "1e kwartaal = Jan + Feb + Maart = 120 + 150 + 180 = 450 pakken."
    }
  ]
});

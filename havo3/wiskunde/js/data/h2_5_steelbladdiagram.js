DURU.register({
  id: "h2-5-steelbladdiagram",
  hoofdstuk: 2,
  paragraaf: "2.5",
  titel: "2.5 Steelbladdiagram",
  korteUitleg: "Gegevens overzichtelijk ordenen in steel en bladeren, aflezen van getallen en centrummaten.",
  icoon: "🌿",
  theorie: `
    <h3>Paragraaf 2.5 — Steelbladdiagram</h3>
    <p>Een <strong>steelbladdiagram</strong> (stem-and-leaf plot) is een overzichtelijke manier om veel getallen geordend weer te geven zonder informatie te verliezen.</p>

    <div class="formule-box">
      <strong>Opbouw van een steelbladdiagram:</strong><br>
      • De <strong>steel</strong> (links van de verticale streep) bevat bijvoorbeeld de tientallen (of uren/gehele getallen).<br>
      • De <strong>bladeren</strong> (rechts van de streep) bevatten de eenheden (of minuten/decimalen), altijd gesorteerd van klein naar groot!<br>
      • Elk blad stelt één waarneming/waarde voor. Het totaal aantal bladeren is gelijk aan het totaal aantal gegevens.
    </div>

    <div class="voorbeeld">
      <div class="vb-kop">Voorbeeld: Aflezen van een steelbladdiagram</div>
      <p>Lengten van een voetbalteam in cm:</p>
      <pre style="background:#f1f5f9; padding:8px; border-radius:6px; font-family:monospace;">
14 | 5 8 8 8
15 | 2 6 9
16 | 3 3 4 7
      </pre>
      <div class="stap">
        • De steel <code>14</code> met bladeren <code>5 8 8 8</code> betekent de lengten: 145 cm, 148 cm, 148 cm, 148 cm.<br>
        • De steel <code>15</code> met bladeren <code>2 6 9</code> betekent: 152 cm, 156 cm, 159 cm.<br>
        • Het kortste meisje is <strong>145 cm</strong>; het langste meisje is <strong>167 cm</strong>.<br>
        • Aantal meisjes = tel alle bladeren = 4 + 3 + 4 = <strong>11 meisjes</strong>.<br>
        • Modus = <strong>148 cm</strong> (komt 3 keer voor).
      </div>
    </div>
  `,
  vragen: [
    {
      type: "mc",
      niveau: 1,
      vraag: "In een steelbladdiagram staat aan de linkerkant van de streep '15' en aan de rechterkant het blad '7'. Welk getal stelt dit voor als de steel de tientallen zijn?",
      opties: ["15", "57", "157", "175"],
      antwoord: 2,
      uitleg: "Steel 15 (tientallen/honderdtallen) en blad 7 (eenheid) vormt samen 157."
    },
    {
      type: "invoer",
      niveau: 1,
      vraag: "Een steelbladdiagram heeft in totaal 15 bladeren. Uit hoeveel waarnemingen bestaat de dataset?",
      antwoord: "15",
      tolerantie: 0.1,
      uitleg: "Elk blad stelt precies één getal/waarneming voor. 15 bladeren = 15 waarnemingen."
    },
    {
      type: "mc",
      niveau: 2,
      vraag: "In een steelbladdiagram staan bij steel 4 de bladeren: 5, 5, 7, 8, 9 en bij steel 5 de bladeren: 2, 3, 3, 3, 8. Wat is de modus van deze getallen?",
      opties: ["45", "52", "53", "58"],
      antwoord: 2,
      uitleg: "Blad 3 komt bij steel 5 het vaakst voor (3 keer), wat overeenkomt met het getal 53."
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "Bij steel 16 staan bladeren: 0, 1, 3, 3, 8. Wat is het grootste getal in deze rij?",
      antwoord: "168",
      tolerantie: 0.1,
      uitleg: "Steel 16 met het grootste blad 8 geeft het getal 168."
    },
    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "De bladeren in een steelbladdiagram horen altijd van klein naar groot op volgorde te staan.",
      antwoord: true,
      uitleg: "Waar. De bladeren worden per steel altijd in oplopende volgorde van klein naar groot genoteerd."
    },
    {
      type: "invoer",
      niveau: 3,
      vraag: "Gegeven steelbladdiagram met 11 getallen: 145, 148, 148, 148, 152, 156, 159, 163, 163, 164, 167. Wat is de mediaan?",
      antwoord: "156",
      tolerantie: 0.5,
      uitleg: "Met n = 11 getallen op volgorde is het 6e getal de mediaan. Het 6e getal is 156."
    }
  ]
});

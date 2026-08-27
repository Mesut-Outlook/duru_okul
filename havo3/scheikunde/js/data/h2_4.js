/* Onderwerp 2.4 — Atoombouw en isotopen */
DURU.register({
  id: "sch-h2-4-atoombouw",
  hoofdstuk: 2,
  paragraaf: "2.4",
  titel: "Atoombouw, Schillen & Isotopen",
  korteUitleg: "Protonen, neutronen, elektronen, atoomnummer (Z), massagetal (A) en atoommodellen.",
  icoon: "⚛️",
  kleur: "h2-thema",
  theorie: "<h3>2.4 Atoombouw en isotopen</h3><div class='formule-box'><strong>Deeltjes in een atoom:</strong><br>• <b>Protonen (p⁺):</b> In de kern, lading +1, massa 1 u.<br>• <b>Neutronen (n⁰):</b> In de kern, lading 0, massa 1 u.<br>• <b>Elektronen (e⁻):</b> In schillen (K=2, L=8, M=18), lading -1, massa ≈ 0 u.<br><br><strong>Getallen:</strong><br>• <b>Atoomnummer (Z):</b> Aantal protonen (= aantal elektronen in neutraal atoom).<br>• <b>Massagetal (A):</b> Protonen + neutronen (A = p + n -> n = A - Z).</div>",
  vragen: [
    {
      type: "mc",
      niveau: 1,
      vraag: "Waaruit bestaat de atoomkern?",
      opties: ["Protonen en neutronen", "Alleen elektronen", "Protonen en elektronen", "Alleen neutronen"],
      antwoord: 0,
      uitleg: "In de kern zitten positieve protonen en ongeladen neutronen."
    },
    {
      type: "invoer",
      niveau: 1,
      vraag: "Een neutraal atoom heeft 8 protonen. Hoeveel elektronen heeft dit atoom?",
      antwoord: "8|acht",
      uitleg: "In een neutraal atoom is aantal p⁺ = aantal e⁻ = 8."
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "Fluor heeft atoomnummer 9 en massagetal 19. Hoeveel neutronen zitten er in de kern?",
      antwoord: "10|tien",
      uitleg: "Neutronen = massagetal - atoomnummer = 19 - 9 = 10."
    },
    {
      type: "mc",
      niveau: 2,
      vraag: "Wat zijn isotopen?",
      opties: ["Atomen van hetzelfde element met een verschillend aantal neutronen", "Atomen met verschillend aantal protonen", "Moleculen met zout", "Atomen zonder elektronen"],
      antwoord: 0,
      uitleg: "Isotopen hebben hetzelfde atoomnummer maar een ander massagetal."
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "Hoeveel elektronen passen er maximaal in de binnenste K-schil?",
      antwoord: "2|twee",
      uitleg: "K-schil = max 2 elektronen."
    },
    {
      type: "mc",
      niveau: 3,
      vraag: "Wat is de elektronenverdeling over de schillen van Chloor (atoomnummer 17)?",
      opties: ["2, 8, 7", "2, 7, 8", "2, 10, 5", "8, 8, 1"],
      antwoord: 0,
      uitleg: "K=2, L=8, M=7 -> (2, 8, 7)."
    }
  ]
});

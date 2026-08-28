/* Onderwerp 2.1 — Elektriciteit en lading */
DURU.register({
  id: "h2-1-lading-spanning",
  hoofdstuk: 2,
  paragraaf: "2.1",
  titel: "Lading, Spanning & Stroomkring",
  korteUitleg: "Elektrische lading, statische elektriciteit, spanning (V), stroomsterkte (A) en meters aansluiten.",
  icoon: "🔋",
  kleur: "h2-thema",
  theorie: "<h3>2.1 Elektriciteit en lading</h3><div class=\"formule-box\"><strong>Grootheden en eenheden:</strong><br>• <b>Spanning (U):</b> in <b>Volt (V)</b> — 'energie meegegeven aan de lading'<br>• <b>Stroomsterkte (I):</b> in <b>Ampère (A)</b> of <b>milliampère (mA)</b> — 1 A = 1000 mA</div><h4>Lading en krachten</h4><ul><li>Gelijksoortige ladingen stoten elkaar af (+ en + of - en -).</li><li>Ongelijksoortige ladingen trekken elkaar aan (+ en -).</li><li>Stroom in metaaldraden bestaat uit bewegende <b>negatieve elektronen</b>.</li></ul><h4>Meetinstrumenten aansluiten</h4><ul><li><b>Stroommeter (Ampèremeter):</b> Altijd <b>IN SERIE</b> geschakeld (zeer lage weerstand).</li><li><b>Spanningsmeter (Voltmeter):</b> Altijd <b>PARALLEL</b> over het onderdeel (zeer hoge weerstand).</li></ul>",
  vragen: [
    {
      type: "mc",
      niveau: 1,
      vraag: "Welke deeltjes bewegen door een koperdraad als er stroom loopt?",
      opties: ["Elektronen", "Protonen", "Neutronen", "Moleculen"],
      antwoord: 0,
      uitleg: "Elektrische stroom is een stroom van vrije elektronen."
    },
    {
      type: "mc",
      niveau: 1,
      vraag: "Hoe moet een spanningsmeter worden aangesloten?",
      opties: ["In serie", "Parallel over het component", "Direct tussen plus en min zonder belasting", "In plaats van de schakelaar"],
      antwoord: 1,
      uitleg: "Een voltmeter sluit je altijd parallel aan over het onderdeel waarvan je de spanning wilt meten."
    },
    {
      type: "invoer",
      niveau: 1,
      vraag: "Reken om: 450 mA is hoeveel Ampère?",
      antwoord: "0,45|0,45 A|0,45A",
      uitleg: "450 / 1000 = 0,45 A."
    },
    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "Twee positief geladen voorwerpen trekken elkaar aan.",
      antwoord: false,
      uitleg: "Niet waar: gelijke ladingen (+ en +) stoten elkaar juist af."
    },
    {
      type: "mc",
      niveau: 2,
      vraag: "Welke stof is een goede elektrische isolator?",
      opties: ["Koper", "Aluminium", "Rubber", "IJzer"],
      antwoord: 2,
      uitleg: "Rubber laat geen stroom door en is een uitstekende isolator."
    },
    {
      type: "invoer",
      niveau: 3,
      vraag: "Hoeveel Volt is de standaard netspanning op een stopcontact in Nederland?",
      antwoord: "230|230 V|230 volt",
      uitleg: "De netspanning in Europa is standaard 230 V."
    }
  ]
});

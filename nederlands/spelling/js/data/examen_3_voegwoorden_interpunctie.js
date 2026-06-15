DURU.registerExamen({
  id: "ex-sp-3",
  titel: "Proeftoets 3 — Voegwoorden & Interpunctie",
  vak: "Nederlands Spelling",
  icoon: "✍️",
  duurMin: 15,
  vragen: [
    {
      type: "invul",
      vraag: "Vul het juiste voegwoord in (reden/oorzaak): 'Ik blijf vandaag binnen ___ het hard regent.'",
      antwoord: "omdat",
      uitleg: "<b>Omdat</b> geeft een reden of oorzaak aan."
    },
    {
      type: "invul",
      vraag: "Vul het juiste voegwoord in (tegenstelling): 'Het is koud, ___ de zon schijnt wel.'",
      antwoord: "maar",
      uitleg: "Het voegwoord <b>maar</b> geeft een tegenstelling aan."
    },
    {
      type: "mc",
      vraag: "Welke zin heeft de juiste interpunctie?",
      opties: [
        "Nadat hij had gegeten ging hij naar bed.",
        "Nadat hij had gegeten, ging hij naar bed.",
        "Nadat, hij had gegeten ging hij naar bed."
      ],
      antwoord: 1,
      uitleg: "Tussen twee persoonsvormen (had gegeten, ging) hoort een komma te staan."
    },
    {
      type: "waaronwaar",
      vraag: "Voor het voegwoord 'want' hoort meestal geen komma.",
      antwoord: false,
      uitleg: "Onwaar: voor 'want' en 'maar' plaatsen we juist wél een komma."
    },
    {
      type: "invul",
      vraag: "Typ de zin correct over met de juiste leestekens (komma en punt): 'hoewel zij moe was ging ze toch trainen'",
      antwoord: "Hoewel zij moe was, ging ze toch trainen.",
      uitleg: "Begin met een hoofdletter, plaats een komma tussen de bijzin og de hoofdzin, en eindig met een punt."
    },
    {
      type: "mc",
      vraag: "Welk voegwoord geeft een voorwaarde aan?",
      opties: [
        "toen",
        "indien",
        "omdat",
        "dus"
      ],
      antwoord: 1,
      uitleg: "<b>Indien</b> (oftewel 'als') geeft een voorwaarde aan."
    },
    {
      type: "invul",
      vraag: "Vul het juiste voegwoord in (tijd): 'We gaan eten ___ mijn vader thuis is.'",
      antwoord: "zodra",
      uitleg: "<b>Zodra</b> geeft het tijdstip aan waarop iets gebeurt."
    },
    {
      type: "waaronwaar",
      vraag: "In de zin: 'Ik vraag me af, of we morgen vrij zijn.' staat de komma op de juiste plek.",
      antwoord: false,
      uitleg: "Onwaar: er hoort geen komma voor 'of' te staan als het een directe aanvulling van de hoofdzin is."
    },
    {
      type: "invul",
      vraag: "Vul het juiste voegwoord in (gevolg): 'Het is al laat, ___ we moeten snel vertrekken.'",
      antwoord: "dus",
      uitleg: "<b>Dus</b> geeft het logische gevolg aan."
    },
    {
      type: "mc",
      vraag: "Waar moet de komma staan in deze zin?<br>'Als je klaar bent met eten mag je opstaan.'",
      opties: [
        "Na 'eten'",
        "Na 'klaar'",
        "Er hoort geen komma in deze zin"
      ],
      antwoord: 0,
      uitleg: "De komma staat tussen de bijzin en de hoofdzin: 'Als je klaar bent met eten, mag je...'"
    }
  ]
});

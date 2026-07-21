/* Proeftoets 1 — Nederlands HAVO 3: taalbasis (woordsoorten, spelling/werkwoord, leesvaardigheid).
   Smoke-test: 5 vragen (2 mc / 1 waaronwaar / 1 invul / 1 open). */
DURU.registerExamen({
  id: "ex-h3-nederlands-1",
  titel: "Proeftoets 1 — Nederlands: taalbasis",
  vak: "Nederlands · HAVO 3",
  icoon: "📖",
  duurMin: 10,
  vragen: [
    {
      type: "mc",
      vraag: "Welk woord in de zin is een <b>zelfstandig naamwoord</b>?<br>'De vrolijke hond rent snel door de tuin.'",
      opties: [
        "vrolijke",
        "hond",
        "rent",
        "snel"
      ],
      antwoord: 1,
      uitleg: "'Hond' is een zelfstandig naamwoord: het is de naam van een dier/ding. 'Vrolijke' is een bijvoeglijk naamwoord, 'rent' is een werkwoord en 'snel' is een bijwoord."
    },
    {
      type: "mc",
      vraag: "Welke werkwoordsvorm hoort er in de zin? 'Zij ___ (worden) gisteren ziek.'",
      opties: [
        "wordt",
        "werd",
        "worden",
        "geworden"
      ],
      antwoord: 1,
      uitleg: "'Gisteren' laat zien dat het in de verleden tijd (onvoltooid verleden tijd) staat. Enkelvoud + verleden tijd van 'worden' is 'werd'."
    },
    {
      type: "waaronwaar",
      vraag: "In de zin 'Hij heeft het boek gelezen' staat het werkwoord in de <b>voltooide tijd</b>.",
      antwoord: true,
      uitleg: "Waar. 'Heeft gelezen' is een vorm van hebben/zijn + voltooid deelwoord — dat is de voltooide tijd (hier: voltooid tegenwoordige tijd)."
    },
    {
      type: "invul",
      vraag: "Het bijvoeglijk naamwoord in 'de grote hond' is … .",
      antwoord: "grote|groot",
      uitleg: "'Grote' (van 'groot') zegt iets over het zelfstandig naamwoord 'hond' — dat maakt het een bijvoeglijk naamwoord."
    },
    {
      type: "open",
      vraag: "Leg uit wat het verschil is tussen een <b>synoniem</b> en een <b>antoniem</b>. Geef bij allebei een voorbeeld.",
      sleutelwoorden: ["synoniem/zelfde betekenis/hetzelfde betekent", "antoniem/tegenovergestelde/tegengestelde", "voorbeeld"],
      minTreffers: 2,
      modelantwoord: "Een synoniem is een woord met (bijna) dezelfde betekenis als een ander woord, bijvoorbeeld 'blij' en 'vrolijk'. Een antoniem is een woord met de tegenovergestelde betekenis, bijvoorbeeld 'blij' en 'verdrietig'.",
      uitleg: "Synoniem = zelfde/vergelijkbare betekenis (bijv. mooi/fraai). Antoniem = tegenovergestelde betekenis (bijv. groot/klein). Een goed voorbeeld bij elk begrip maakt het antwoord compleet."
    }
  ]
});

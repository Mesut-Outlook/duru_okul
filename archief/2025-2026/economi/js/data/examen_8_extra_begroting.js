/* Extra Proeftoets 3 — Rijksbegroting & Staatsschuld (6.4) */
DURU.registerExamen({
  id: "ex-extra-begroting-schuld",
  titel: "Extra Proeftoets 3 — Rijksbegroting & Staatsschuld",
  vak: "Economie · H6 (6.4)",
  icoon: "📊",
  duurMin: 15,
  vragen: [
    {
      type: "mc",
      vraag: "Op welke dag biedt de Minister van Financiën de Miljoenennota aan de Tweede Kamer aan?",
      opties: [
        "Nieuwjaarsdag (1 januari)",
        "De eerste maandag van oktober",
        "De derde dinsdag van september (Prinsjesdag)",
        "De laatste vrijdag van mei"
      ],
      antwoord: 2,
      uitleg: "De Minister van Financiën biedt de Rijksbegroting en de Miljoenennota op <b>Prinsjesdag</b> (de derde dinsdag van september) aan."
    },
    {
      type: "mc",
      vraag: "Wat is de functie van de Miljoenennota?",
      opties: [
        "Een overzicht van alle miljonairs in Nederland.",
        "Een toelichting op de Rijksbegroting waarin de regering uitlegt welke keuzes zij maakt.",
        "De wet waarin staat hoeveel btw winkels moeten rekenen.",
        "De troonrede die door de koning wordt voorgelezen."
      ],
      antwoord: 1,
      uitleg: "De <b>Miljoenennota</b> geeft tekst en uitleg bij de cijfers van de Rijksbegroting. Het legt uit hoe de economie er voor staat en waar het geld heen gaat."
    },
    {
      type: "mc",
      vraag: "Wanneer heeft de overheid een begrotingsoverschot?",
      opties: [
        "Als de overheid meer uitgeeft aan defensie dan aan onderwijs.",
        "Als de inkomsten uit belastingen en premies groter zijn dan de uitgaven.",
        "Als de staatsschuld stijgt.",
        "Als de koning zijn plannen wijzigt."
      ],
      antwoord: 1,
      uitleg: "Een <b>overschot</b> betekent dat er meer geld binnenkomt dan er uitgaat. Dit geld kan gebruikt worden om de staatsschuld af te lossen."
    },
    {
      type: "mc",
      vraag: "Wat is de grootste inkomstenbron van de Nederlandse overheid?",
      opties: [
        "De verkoop van aardgas",
        "Leningen van banken",
        "Belastingen en sociale premies",
        "Boetes voor verkeersovertredingen"
      ],
      antwoord: 2,
      uitleg: "De overheid haalt veruit het meeste geld binnen via <b>belastingen</b> (zoals btw en loonbelasting) en <b>sociale premies</b> (voor volksverzekeringen)."
    },
    {
      type: "mc",
      vraag: "Wat is het belangrijkste risico van een zeer hoge staatsschuld?",
      opties: [
        "De overheid mag dan geen wetten meer maken van de koning.",
        "De overheid moet veel rente betalen, waardoor er minder geld overblijft voor zorg en onderwijs.",
        "De btw moet automatisch naar 100%.",
        "De provincies worden dan opgeheven."
      ],
      antwoord: 1,
      uitleg: "Over de <b>staatsschuld</b> moet rente betaald worden. Als de schuld te hoog is, drukken de <b>rentelasten</b> zwaar op de begroting, wat ten koste gaat van andere uitgaven."
    },
    {
      type: "waaronwaar",
      vraag: "De Troonrede wordt voorgelezen door de Minister-President.",
      antwoord: false,
      uitleg: "Onwaar. De <b>Troonrede</b> wordt op Prinsjesdag voorgelezen door de <b>Koning</b>, hoewel de tekst door de ministers is geschreven."
    },
    {
      type: "waaronwaar",
      vraag: "De Rijksbegroting is een schatting van de inkomsten en uitgaven van de overheid voor het komende jaar.",
      antwoord: true,
      uitleg: "Waar. Het is een begroting (vooruitblik) voor het komende jaar. De werkelijke inkomsten en uitgaven kunnen er achteraf iets van afwijken."
    },
    {
      type: "invul",
      vraag: "De minister die op Prinsjesdag met het bekende koffertje naar de Tweede Kamer loopt is de minister van ______.",
      antwoord: "Financiën|financiën|financien",
      uitleg: "De minister van <b>Financiën</b> beheert de staatskas en presenteert de begroting."
    },
    {
      type: "open",
      vraag: "Leg uit wat het verschil is tussen een begrotingstekort en de staatsschuld.",
      sleutelwoorden: ["tekort/begrotingstekort/jaar/uitgaven/inkomsten", "schuld/staatsschuld/totaal/opgebouwd/totaalbedrag"],
      minTreffers: 2,
      modelantwoord: "Een begrotingstekort gaat over één jaar: het is het bedrag dat de overheid in dat jaar meer uitgeeft dan zij aan inkomsten ontvangt. De staatsschuld is de totale schuld (alle leningen bij elkaar) die de overheid in de loop der jaren heeft opgebouwd.",
      uitleg: "Tekort = per jaar (stroomgrootheid). Staatsschuld = het totale opgebouwde bedrag aan leningen (voorraadgrootheid)."
    },
    {
      type: "open",
      vraag: "Wat is de Troonrede en wat staat daarin beschreven?",
      sleutelwoorden: ["koning", "plannen/plannen van de regering", "komende jaar/volgende jaar"],
      minTreffers: 2,
      modelantwoord: "De Troonrede is een toespraak die de koning op Prinsjesdag voorleest namens de regering. Hierin blikt de regering terug op het afgelopen jaar en legt zij de belangrijkste plannen en doelen uit voor het komende jaar.",
      uitleg: "De <b>Troonrede</b> zet de grote politieke lijnen en plannen van de regering uiteen."
    }
  ]
});

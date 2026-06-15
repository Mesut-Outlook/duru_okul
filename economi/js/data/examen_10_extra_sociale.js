/* Extra Proeftoets 5 — Sociale Zekerheid & Zorg */
DURU.registerExamen({
  id: "ex-extra-sociale-zekerheid",
  titel: "Extra Proeftoets 5 — Sociale Zekerheid & Zorg",
  vak: "Economie · Sociale Zekerheid",
  icoon: "🏥",
  duurMin: 15,
  vragen: [
    {
      type: "mc",
      vraag: "Wat is het belangrijkste verschil tussen een volksverzekering en een werknemersverzekering?",
      opties: [
        "Een volksverzekering geldt voor iedereen in Nederland, een werknemersverzekering alleen voor mensen die in loondienst werken (of gewerkt hebben).",
        "Volksverzekeringen worden door de koning betaald, werknemersverzekeringen door de baas.",
        "Werknemersverzekeringen gelden alleen voor ambtenaren.",
        "Er is geen verschil, het zijn twee woorden voor hetzelfde."
      ],
      antwoord: 0,
      uitleg: "De **volksverzekeringen** (zoals de AOW) beschermen alle inwoners. **Werknemersverzekeringen** (zoals de WW of de WIA) beschermen specifiek mensen in loondienst."
    },
    {
      type: "mc",
      vraag: "Welke uitkering ontvangt een inwoner van Nederland die de pensioengerechtigde leeftijd heeft bereikt?",
      opties: [
        "Bijstand (Participatiewet)",
        "WW-uitkering",
        "AOW (Algemene Ouderdomswet)",
        "WIA-uitkering"
      ],
      antwoord: 2,
      uitleg: "De **AOW** is het basispensioen van de overheid voor iedereen die de pensioengerechtigde leeftijd bereikt en in Nederland heeft gewoond."
    },
    {
      type: "mc",
      vraag: "Wanneer heeft een persoon recht op een WW-uitkering?",
      opties: [
        "Als hij vrijwillig ontslag neemt om vakantie te vieren.",
        "Als hij buiten zijn schuld om (onvrijwillig) zijn baan verliest.",
        "Zodra hij 18 jaar oud wordt en nog studeert.",
        "Als hij weigert om te solliciteren."
      ],
      antwoord: 1,
      uitleg: "De <b>WW (Werkloosheidswet)</b> keert tijdelijk geld uit aan werknemers die onvrijwillig werkloos zijn geworden, mits zij actief solliciteren."
    },
    {
      type: "mc",
      vraag: "Wat verstaan we onder de sociale bijstand (Participatiewet)?",
      opties: [
        "Een verplichte premie die je betaalt aan de zorgverzekering.",
        "Het geld dat de provincie uitgeeft aan wegenonderhoud.",
        "Een sociaal vangnet voor mensen die niet genoeg inkomen of vermogen hebben en nergens anders recht op hebben.",
        "Het loon dat je ontvangt als je stage loopt."
      ],
      antwoord: 2,
      uitleg: "De **bijstand** is de allerlaatste uitkering (vangnet) voor mensen die geen werk en geen andere uitkeringen hebben, om te kunnen voorzien in de minimale kosten van levensonderhoud."
    },
    {
      type: "mc",
      vraag: "Hoe wordt de sociale bijstand (Participatiewet) gefinancierd?",
      opties: [
        "Volledig uit de premies die werknemers betalen.",
        "Uit de algemene belastingopbrengsten van de overheid.",
        "Door leningen bij buitenlandse banken.",
        "Door donaties van de koninklijke familie."
      ],
      antwoord: 1,
      uitleg: "In tegenstelling tot sociale verzekeringen (die uit premies worden betaald), wordt de **sociale bijstand** betaald uit **belastinggeld** (sociale voorziening)."
    },
    {
      type: "waaronwaar",
      vraag: "Iedereen die in Nederland woont of werkt is wettelijk verplicht om een basiszorgverzekering af te sluiten.",
      antwoord: true,
      uitleg: "Waar. Dit is de **acceptatieplicht** en **verzekeringsplicht** om te zorgen dat de zorg voor iedereen betaalbaar blijft via solidariteit."
    },
    {
      type: "waaronwaar",
      vraag: "Omdat de AOW een volksverzekering is, heeft ook iemand die nog nooit heeft gewerkt er recht op vanaf zijn pensioenleeftijd.",
      antwoord: true,
      uitleg: "Waar. De **AOW** is gekoppeld aan het aantal jaren dat je in Nederland hebt gewoond (opgebouwd met 2% per jaar), niet aan je werkverleden."
    },
    {
      type: "invul",
      vraag: "Het totale stelsel waarmee we via premies en belastingen zorgen voor ouderen, zieken en werklozen noemen we de sociale _______.",
      antwoord: "zekerheid",
      uitleg: "De **sociale zekerheid** garandeert dat iedereen een basisinkomen heeft bij ziekte, ouderdom of werkloosheid."
    },
    {
      type: "open",
      vraag: "Leg uit wat het solidariteitsbeginsel inhoudt in ons socialezekerheidsstelsel.",
      sleutelwoorden: ["samen/elkaar/helpen", "betalen/premies/sterken/gezonden", "zwakken/zieken/ouders/ontvangen"],
      minTreffers: 2,
      modelantwoord: "Het solidariteitsbeginsel houdt in dat we met z'n allen de lasten delen. Iedereen die werkt betaalt premies, en met dat geld worden de uitkeringen betaald voor de mensen die dat op dat moment nodig hebben (zoals zieken, ouderen en werklozen).",
      uitleg: "Gezonden en werkenden betalen voor zieken, ouderen en werklozen."
    },
    {
      type: "open",
      vraag: "Wat is het verschil tussen een sociale verzekering en een sociale voorziening?",
      sleutelwoorden: ["verzekering/premie/werkenden", "voorziening/belasting/overheid/bijstand", "geen premie/vangnet"],
      minTreffers: 2,
      modelantwoord: "Een sociale verzekering wordt betaald uit premies die werkenden verplicht afdragen (zoals AOW en WW). Een sociale voorziening (zoals de bijstand) wordt betaald uit de algemene belastingen en is bedoeld voor mensen die geen recht hebben op een verzekering.",
      uitleg: "Verzekering = premie. Voorziening = belasting."
    }
  ]
});

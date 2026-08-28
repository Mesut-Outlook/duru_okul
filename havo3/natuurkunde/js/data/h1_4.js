/* Onderwerp 1.4 — Veiligheidsmaatregelen in het verkeer */
DURU.register({
  id: "h1-4-veiligheid-verkeer",
  hoofdstuk: 1,
  paragraaf: "1.4",
  titel: "Veiligheid, Remweg & Stopafstand",
  korteUitleg: "Reactietijd, remweg, stopafstand en de werking van kreukelzones, airbags en gordels.",
  icoon: "🚗",
  kleur: "h1-thema",
  theorie: "<h3>1.4 Veiligheidsmaatregelen in het verkeer</h3><div class=\"formule-box\"><strong>Stopafstand:</strong><br>s_stop = s_reactie + s_rem<br><br>• <b>Reactieafstand (s_reactie):</b> Afstand tijdens de reactietijd (t_r): s_reactie = v × t_r<br>• <b>Remweg (s_rem):</b> Afstand tijdens het remmen: s_rem = 0,5 × v × t_rem<br>• <b>Kwadratisch effect:</b> Als de snelheid <b>2×</b> zo groot wordt, wordt de remweg <b>4× (2²)</b> zo lang!</div><h4>Veiligheidsvoorzieningen</h4><p><b>Kreukelzone, gordel, airbag en helm</b> zorgen ervoor dat de <b>remtijd / botstijd (Δt)</b> wordt verlengd. Volgens F = m × (Δv / Δt) wordt de botskracht F daardoor aanzienlijk kleiner!</p>",
  vragen: [
    {
      type: "mc",
      niveau: 1,
      vraag: "Wat is de stopafstand?",
      opties: ["Reactieafstand plus remweg", "Alleen de remweg", "Reactieafstand maal remweg", "Remweg min reactieafstand"],
      antwoord: 0,
      uitleg: "s_stop = s_reactie + s_rem."
    },
    {
      type: "invoer",
      niveau: 1,
      vraag: "Een auto rijdt met 15 m/s. De bestuurder heeft een reactietijd van 0,8 s. Bereken de reactieafstand in meters.",
      antwoord: "12|12 m|12,0",
      uitleg: "s_reactie = 15 m/s × 0,8 s = 12 meter."
    },
    {
      type: "mc",
      niveau: 2,
      vraag: "Als de snelheid van een auto verdubbelt van 40 km/h naar 80 km/h, wat gebeurt er met de remweg?",
      opties: ["Wordt 2× zo lang", "Wordt 4× zo lang", "Blijft gelijk", "Wordt 8× zo lang"],
      antwoord: 1,
      uitleg: "De remweg schaalt met het kwadraat van de snelheid: 2² = 4 keer zo lang."
    },
    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "Afleiding door een smartphone vergroot de mechanische remweg van de auto.",
      antwoord: false,
      uitleg: "Niet waar: het vergroot de reactietijd en reactieafstand, niet de mechanische remweg van de remmen zelf."
    },
    {
      type: "mc",
      niveau: 2,
      vraag: "Hoe vermindert een kreukelzone de letselkans bij een aanrijding?",
      opties: ["Door de auto zwaarder te maken", "Door de snelheid van tevoren te verlagen", "Door de botstijd te verlengen, waardoor de botskracht kleiner wordt", "Door de remmen te blokkeren"],
      antwoord: 2,
      uitleg: "Door in te deuken verlengt de kreukelzone de vertragingstijd Δt, waardoor de piek-botskracht F daalt."
    },
    {
      type: "invoer",
      niveau: 3,
      vraag: "Een auto rijdt 20 m/s. Reactietijd is 1,0 s en de remweg is 25 m. Wat is de totale stopafstand in meters?",
      antwoord: "45|45 m|45,0",
      uitleg: "s_reactie = 20 × 1,0 = 20 m. s_stop = 20 + 25 = 45 meter."
    }
  ]
});

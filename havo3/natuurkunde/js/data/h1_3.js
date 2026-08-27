/* Onderwerp 1.3 — Kracht en versnelling */
DURU.register({
  id: "h1-3-kracht-versnelling",
  hoofdstuk: 1,
  paragraaf: "1.3",
  titel: "Kracht en Versnelling (F = m · a)",
  korteUitleg: "De tweede wet van Newton, versnelling berekenen en de traagheid van massa.",
  icoon: "⚡",
  kleur: "h1-thema",
  theorie: "<h3>1.3 Kracht en versnelling</h3><div class=\"formule-box\"><strong>Tweede wet van Newton:</strong><br>Fres = m × a<br><br>• Fres = resulterende kracht in Newton (N)<br>• m = massa in kilogram (kg)<br>• a = versnelling in meter per seconde kwadraat (m/s²)<br><br><strong>Versnelling:</strong> a = Δv / Δt = (veind - vbegin) / t</div><h4>Traagheid (inertie)</h4><p>Massa heeft de eigenschap dat het zich verzet tegen verandering van beweging. Dit heet <b>traagheid</b>. Een zwaar voorwerp heeft een grote kracht nodig om te versnellen of af te remmen.</p>",
  vragen: [
    {
      type: "mc",
      niveau: 1,
      vraag: "Wat is de officiële eenheid van versnelling?",
      opties: ["m/s", "m/s²", "km/h", "N/kg"],
      antwoord: 1,
      uitleg: "Versnelling wordt gemeten in m/s²."
    },
    {
      type: "invoer",
      niveau: 1,
      vraag: "Een voorwerp van 4,0 kg krijgt een versnelling van 3,0 m/s². Hoe groot is de resulterende kracht in Newton?",
      antwoord: "12|12 N|12,0",
      uitleg: "Fres = m × a = 4,0 kg × 3,0 m/s² = 12 N."
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "Een auto versnelt van 0 naar 20 m/s in 5,0 seconden. Bereken de versnelling a in m/s².",
      antwoord: "4|4,0|4 m/s²|4,0 m/s²",
      uitleg: "a = Δv / Δt = 20 / 5,0 = 4,0 m/s²."
    },
    {
      type: "mc",
      niveau: 2,
      vraag: "Twee voorwerpen worden met dezelfde kracht geduwd. Voorwerp A heeft een massa van 5 kg, voorwerp B van 10 kg. Wat geldt voor de versnelling?",
      opties: ["A versnelt 2× zo snel als B", "B versnelt 2× zo snel als A", "Beide versnellen even snel", "A versnelt 4× zo snel"],
      antwoord: 0,
      uitleg: "a = F / m: het lichtere voorwerp A (5 kg) krijgt een twee keer zo grote versnelling."
    },
    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "Als de massa van een auto verdubbelt, is er twee keer zoveel remkracht nodig voor dezelfde vertraging.",
      antwoord: true,
      uitleg: "Waar: F = m × a; bij dubbele massa is dubbele kracht vereist."
    },
    {
      type: "invoer",
      niveau: 3,
      vraag: "Een motorrijder met motor (totale massa = 250 kg) trekt op vanuit stilstand en bereikt na 4,0 s een snelheid van 72 km/h (20 m/s). Bereken de resulterende motorkracht in Newton.",
      antwoord: "1250|1250 N|1250N",
      uitleg: "a = 20 m/s / 4,0 s = 5,0 m/s². Fres = m × a = 250 kg × 5,0 m/s² = 1250 N."
    }
  ]
});

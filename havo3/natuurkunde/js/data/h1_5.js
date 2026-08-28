/* Onderwerp 1.5 — Arbeid */
DURU.register({
  id: "h1-5-arbeid",
  hoofdstuk: 1,
  paragraaf: "1.5",
  titel: "Arbeid en Energieomzetting",
  korteUitleg: "Bereken de verrichte arbeid met W = F·s en ontdek positieve en negatieve arbeid.",
  icoon: "⚙️",
  kleur: "h1-thema",
  theorie: "<h3>1.5 Arbeid</h3><div class=\"formule-box\"><strong>Arbeid berekenen:</strong><br>W = F × s<br><br>• W = arbeid in Joule (J) of Newton-meter (N·m)<br>• F = kracht in Newton (N) in de bewegingsrichting<br>• s = verplaatsing in meter (m)</div><h4>Positieve, negatieve en geen arbeid</h4><ul><li><b>Positieve arbeid:</b> De kracht werkt in de bewegingsrichting mee (voegt bewegingsenergie toe).</li><li><b>Negatieve arbeid:</b> De kracht werkt tegen de beweging in, zoals wrijving of remmen (onttrekt bewegingsenergie en zet deze om in warmte).</li><li><b>Geen arbeid (W = 0 J):</b> Als er geen verplaatsing is (s = 0 m) of als de kracht loodrecht op de verplaatsing staat.</li></ul>",
  vragen: [
    {
      type: "mc",
      niveau: 1,
      vraag: "Wat is de eenheid van arbeid in de natuurkunde?",
      opties: ["Joule (J)", "Watt (W)", "Newton (N)", "Pascal (Pa)"],
      antwoord: 0,
      uitleg: "Arbeid is een vorm van overgedragen energie en wordt gemeten in Joule (J)."
    },
    {
      type: "invoer",
      niveau: 1,
      vraag: "Een trekker trekt met 1200 N over een afstand van 15 meter. Hoeveel Joule arbeid is verricht?",
      antwoord: "18000|18.000|18000 J|18.000 J|18 kJ",
      uitleg: "W = F × s = 1200 N × 15 m = 18.000 J (18 kJ)."
    },
    {
      type: "waaronwaar",
      niveau: 1,
      vraag: "Als je 5 minuten tegen een zware muur duwt die niet beweegt, verricht je natuurkundig gezien geen arbeid.",
      antwoord: true,
      uitleg: "Waar: verplaatsing s = 0, dus W = F × 0 = 0 Joule."
    },
    {
      type: "mc",
      niveau: 2,
      vraag: "Welke kracht verricht negatieve arbeid bij een rijdende auto?",
      opties: ["De motorkracht", "De remkracht/wrijving", "De zwaartekracht", "De normaalkracht"],
      antwoord: 1,
      uitleg: "De remkracht/wrijving werkt tegen de bewegingsrichting in en verricht negatieve arbeid (zet kinetische energie om in warmte)."
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "Iemand tilt een doos van 10 kg over 1,5 meter omhoog (neem g = 10 N/kg). Hoeveel Joule arbeid verricht de tilkracht?",
      antwoord: "150|150 J|150,0",
      uitleg: "Fz = 10 kg × 10 N/kg = 100 N. W = F × s = 100 N × 1,5 m = 150 Joule."
    },
    {
      type: "invoer",
      niveau: 3,
      vraag: "Een fietser verricht 3600 J arbeid en oefent een gemiddelde trapkracht uit van 45 N. Welke afstand in meters heeft hij afgelegd?",
      antwoord: "80|80 m|80,0",
      uitleg: "s = W / F = 3600 J / 45 N = 80 meter."
    }
  ]
});

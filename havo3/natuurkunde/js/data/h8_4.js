/* Onderwerp 8.4 — Druk */
DURU.register({
  id: "h8-4-druk",
  hoofdstuk: 8,
  paragraaf: "8.4",
  titel: "Druk & Oppervlakte",
  korteUitleg: "De formule p = F / A, eenheden Pascal (Pa) en N/cm², druk vergroten en verkleinen.",
  icoon: "📐",
  kleur: "h8-thema",
  theorie: "<h3>8.4 Druk</h3><div class='formule-box'><strong>Drukformule:</strong><br>89565p = \frac{F}{A}89565<br>• $ = druk in Pascal ($\text{Pa} = \text{N/m}^2$) of $\text{N/cm}^2$<br>• $ = kracht loodrecht op het oppervlak in Newton ($\text{N}$)<br>• $ = oppervlakte in $\text{m}^2$ (of $\text{cm}^2$)<br><br><strong>Omrekenen:</strong> \text{ N/cm}^2 = 10.000\text{ N/m}^2 = 10.000\text{ Pa}$.</div><h4>Druk beïnvloeden</h4><ul><li><b>Druk verkleinen (groot oppervlak $):</b> Sneeuwschoenen, rupsbanden, brede trekkerbanden.</li><li><b>Druk vergroten (klein oppervlak $):</b> Naaldpunt, scherp mes, schaatsen, spijker.</li></ul>",
  vragen: [
    {
      type: "invoer",
      niveau: 1,
      vraag: "Een kracht van 800 N staat op een oppervlak van 2 m². Hoeveel Pascal (Pa) is de druk?",
      antwoord: "400|400 Pa",
      uitleg: "p = 800 / 2 = 400 Pa."
    },
    {
      type: "invoer",
      niveau: 1,
      vraag: "Hoeveel Pascal (Pa) is gelijk aan 1 N/cm²?",
      antwoord: "10000|10.000|10000 Pa|10.000 Pa",
      uitleg: "1 N/cm² = 10.000 Pa."
    },
    {
      type: "mc",
      niveau: 2,
      vraag: "Waarom hebben sneeuwschoenen een groot oppervlak?",
      opties: ["Om de druk op de sneeuw te verkleinen zodat je niet wegzakt", "Om sneller te glijden", "Om de wrijving te verhogen", "Voor warmte"],
      antwoord: 0,
      uitleg: "Groot oppervlak = lage druk."
    },
    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "Een scherp mes heeft een heel dun snijvlak om met weinig spierkracht een enorme druk uit te oefenen.",
      antwoord: true,
      uitleg: "Waar: klein oppervlak A -> grote druk p."
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "Een blok oefent 5000 Pa druk uit op een oppervlak van 0,3 m². Hoeveel Newton weegt het blok?",
      antwoord: "1500|1500 N|1.500|1.500 N",
      uitleg: "F = p × A = 5000 × 0,3 = 1500 N."
    },
    {
      type: "waaronwaar",
      niveau: 3,
      vraag: "Als je een baksteen op zijn smalle kant zet, wordt de uitgeoefende druk op tafel groter.",
      antwoord: true,
      uitleg: "Waar: kleiner contactoppervlak A bij gelijk gewicht F."
    }
  ]
});

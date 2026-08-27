/* Onderwerp 4.4 — Soortelijke weerstand */
DURU.register({
  id: "h4-4-soortelijke-weerstand",
  hoofdstuk: 4,
  paragraaf: "4.4",
  titel: "Soortelijke Weerstand (R = ρ · l / A)",
  korteUitleg: "Bereken de weerstand van stroomdraden uit lengte, dikte en materiaalsoort.",
  icoon: "📏",
  kleur: "h4-thema",
  theorie: "<h3>4.4 Soortelijke weerstand</h3><div class='formule-box'><strong>Draadweerstand formule:</strong><br>R = (ρ × l) / A<br><br>• R = weerstand in <b>Ohm (Ω)</b><br>• ρ (rho) = soortelijke weerstand in Ω·mm²/m (koper: 0,017; constantaan: 0,45)<br>• l = lengte van de draad in <b>meter (m)</b><br>• A = doorsnede (oppervlakte) in <b>mm²</b></div><h4>Eigenschappen</h4><ul><li>Draad 2× zo lang -> R wordt 2× zo groot (R ~ l).</li><li>Draad 2× zo dik (A) -> R wordt 2× zo klein (R ~ 1/A).</li></ul>",
  vragen: [
    {
      type: "mc",
      niveau: 1,
      vraag: "Welke formule gebruik je om de weerstand van een draad te berekenen?",
      opties: ["R = (ρ × l) / A", "R = (ρ × A) / l", "R = ρ × l × A", "R = U × I"],
      antwoord: 0,
      uitleg: "R = (ρ · l) / A."
    },
    {
      type: "invoer",
      niveau: 1,
      vraag: "Koper heeft ρ = 0,017 Ω·mm²/m. Bereken de weerstand van 100 m koperdraad met doorsnede 1,7 mm² in Ohm.",
      antwoord: "1|1 Ω|1 ohm|1,0",
      uitleg: "R = (0,017 × 100) / 1,7 = 1,0 Ω."
    },
    {
      type: "mc",
      niveau: 2,
      vraag: "Welke draad heeft de kleinste elektrische weerstand?",
      opties: ["Een lange, dunne draad", "Een lange, dikke draad", "Een korte, dunne draad", "Een korte, dikke draad"],
      antwoord: 3,
      uitleg: "Kort (kleine l) en dik (grote A) geeft de laagste weerstand."
    },
    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "Constantaan heeft een veel hogere soortelijke weerstand dan koper.",
      antwoord: true,
      uitleg: "Waar: koper (0,017) geleidt veel beter dan constantaan (0,45)."
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "Een draad van 5 m heeft een weerstand van 2,0 Ω. Wat is de weerstand van 15 m van dezelfde draad in Ohm?",
      antwoord: "6|6 Ω|6 ohm|6,0",
      uitleg: "3× zo lang -> 3× zoveel weerstand: 2,0 × 3 = 6,0 Ω."
    },
    {
      type: "waaronwaar",
      niveau: 3,
      vraag: "Een kabelhaspel moet je bij zware belasting helemaal afrollen om oververhitting door draadweerstand te voorkomen.",
      antwoord: true,
      uitleg: "Waar: opgerold kan de I²·R warmte niet weg, waardoor de haspel kan smelten."
    }
  ]
});

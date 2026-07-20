# SPEC — Duru's Wiskunde Academie · Hoofdstuk 8: Vergelijkingen

Je schrijft **één JavaScript-bestand** voor **één onderwerp** van een Nederlandse
wiskunde-oefensite voor een 14-jarig meisje (Duru) in **MAVO 2**. Alles in het
**Nederlands**, vriendelijk, duidelijk en leuk. Toon: bemoedigend, niet kinderachtig.

Het bestand registreert het onderwerp via `DURU.register({...})`. Format:

```js
DURU.register({
  id: "h8-1",                 // exact id dat in je opdracht staat
  hoofdstuk: 8,               // altijd 8 voor dit vak
  paragraaf: "8.1",           // paragraafnummer als string
  titel: "Gelijksoortige termen",  // korte titel
  korteUitleg: "Termen samenvoegen en vereenvoudigen.", // 1 zin voor de kaart op de homepage
  icoon: "🔢",                // 1 emoji
  theorie: `...HTML-string...`,
  vragen: [ /* zie hieronder */ ]
});
```

## Onderwerpen (Hoofdstuk 8 — Vergelijkingen)

| Bestand                             | id     | Paragraaf | Titel                       |
|-------------------------------------|--------|-----------|-----------------------------|
| `h8_1_gelijksoortige_termen.js`     | `h8-1` | `8.1`     | Gelijksoortige termen       |
| `h8_2_de_balans.js`                 | `h8-2` | `8.2`     | De balans                   |
| `h8_3_vergelijkingen_oplossen.js`   | `h8-3` | `8.3`     | Vergelijkingen oplossen     |
| `h8_4_het_snijpunt.js`              | `h8-4` | `8.4`     | Het snijpunt                |

## Proeftoetsen

| Bestand                         | id                  | Titel                              |
|---------------------------------|---------------------|------------------------------------|
| `examen_1_gemengd.js`           | `ex-w-1`            | Proeftoets 1 — Gemengd             |
| `examen_2_vergelijkingen.js`    | `ex-w-2`            | Proeftoets 2 — Vergelijkingen      |

Proeftoetsen registreer je via `DURU.registerExamen({...})`. Format:

```js
DURU.registerExamen({
  id: "ex-w-1",
  titel: "Proeftoets 1 — Gemengd",
  vak: "Wiskunde H8",
  icoon: "📝",
  duurMin: 20,
  vragen: [ /* mix van alle types, zie hieronder */ ]
});
```

## Theorie (het `theorie`-veld = HTML-string)

Schrijf heldere uitleg op MAVO-2-niveau. Gebruik deze KANT-EN-KLARE CSS-klassen
(ze bestaan al in style.css — verzin geen nieuwe):

- `<h3>Kopje</h3>` en `<h4>Subkopje</h4>` voor structuur.
- `<p>...</p>` voor tekst, `<ul><li>` voor lijstjes.
- **Formule** (belangrijk, opvallend):
  ```html
  <div class="formule-box"><span class="formule">ax + b = c</span>
  <small>a, b en c zijn getallen · x is de onbekende</small></div>
  ```
- **Uitgewerkt voorbeeld** (laat een berekening stap voor stap zien):
  ```html
  <div class="voorbeeld"><div class="vb-kop">📐 Voorbeeld</div>
  <div class="stap"><b>Gegeven:</b> 3x + 5 = 17</div>
  <div class="stap"><b>Stap 1:</b> 3x = 17 − 5 = 12</div>
  <div class="stap"><b>Stap 2:</b> x = 12 : 3 = 4</div>
  <div class="stap"><b>Antwoord:</b> x = 4</div></div>
  ```
- **Info / let op / tip**:
  ```html
  <div class="info-box teal"><span class="kop">💡 Onthoud</span> tekst...</div>
  <div class="info-box let-op"><span class="kop">⚠️ Let op</span> tekst...</div>
  <div class="info-box tip"><span class="kop">✅ Handige tip</span> tekst...</div>
  ```
- **Tabel**: `<table class="nask"><tr><th>..</th></tr><tr><td>..</td></tr></table>`
- **Figuur** met bijschrift: `<figure class="bron">...SVG of img...<figcaption>...</figcaption></figure>`

### Visuals = inline SVG (AANBEVOLEN)
Maak waar nuttig **eigen, schone inline SVG-tekeningen** (balansschema's, getallenlijn,
assen/grafieken voor snijpunten). Houd ze simpel en kleurrijk. Gebruik `width="100%"` met
een `viewBox` zodat het responsive is, max ±420px breed.

## Vragen (array `vragen`)

Maak **minimaal 14, liefst 16 vragen**. Varieer de types en moeilijkheid.
Verdeling moeilijkheid (`niveau`): ~5× niveau 1, ~6× niveau 2, ~4× niveau 3.
Mix de types: ongeveer de helft meerkeuze (`mc`), een paar `waaronwaar`, en een
flink deel `invoer` (zelf uitrekenen — dit is het belangrijkst voor toetsoefening!).
Bij rekenonderwerpen: maak veel `invoer`-rekenvragen met **verschillende getallen**.

Elke vraag heeft een `uitleg` (korte uitgewerkte oplossing / waarom het zo is).
`uitleg` mag HTML bevatten (bijv. `<b>`). Voeg bij lastige vragen een `hint` toe.

### Type 1 — meerkeuze
```js
{
  type: "mc", niveau: 1,
  vraag: "Welke termen zijn gelijksoortig?",
  opties: ["3x en 5x", "3x en 5", "3 en 5x", "x en x²"],
  antwoord: 0,                        // INDEX (0-based) van het juiste antwoord
  uitleg: "<b>3x</b> en <b>5x</b> zijn gelijksoortig: ze bevatten allebei de letter x.",
  hint: "Kijk welke termen dezelfde letter (en macht) hebben."   // optioneel
}
```

### Type 2 — waar / onwaar
```js
{
  type: "waaronwaar", niveau: 1,
  vraag: "3x + 2x = 5x²",
  antwoord: false,                    // true = Waar, false = Onwaar
  uitleg: "Onwaar: 3x + 2x = <b>5x</b>, niet 5x². Je telt de coëfficiënten op, de letter blijft hetzelfde."
}
```

### Type 3 — invoer (zelf antwoord intypen) — GEBRUIK VEEL
```js
{
  type: "invoer", niveau: 2,
  vraag: "Los de vergelijking op: 2x + 6 = 14. Wat is x?",
  antwoord: "4",        // string; getal met punt of komma mag, engine normaliseert
  tolerantie: 0,        // optioneel; standaard 2%. Gebruik 0 bij exacte gehele uitkomsten.
  uitleg: "2x = 14 − 6 = 8 → x = 8 : 2 = <b>4</b>.",
  hint: "Haal eerst het getal rechts weg, dan deel je door de coëfficiënt."
}
```
- Voor invoer met meerdere goede schrijfwijzen: `antwoord: "4|4,0"` (gescheiden met `|`).
- Vermeld eventuele eenheden in `eenheid`, NIET in het antwoord.
- `vraag` mag een `figuur` hebben: `figuur: "<svg ...></svg>"` (los veld, naast `vraag`).

## Regels
- **Alles in correct Nederlands.** Gebruik komma als decimaalteken in tekst/uitleg
  (bijv. "3,5"), maar in het `antwoord`-veld mag punt of komma.
- Reken alles na zodat antwoorden kloppen! Houd getallen MAVO-2-vriendelijk
  (nette uitkomsten, max 1 decimaal waar nodig).
- Spreek Duru af en toe direct aan ("Reken maar uit, Duru!") — spaarzaam.
- Varieer de contexten: gebruik praktische situaties (zakgeld, punten sparen,
  afstanden, leeftijden, rechthoeken) naast puur wiskundige vergelijkingen.
- Schrijf ALLEEN het ene `DURU.register({...})`-statement in het bestand, niets eromheen.
- Geen externe libraries, geen import/export. Puur ES5/ES6 dat in elke browser werkt.
- De engine herkent alle typen: `mc`, `waaronwaar`, `invoer` (oefen-quiz) en
  `mc`, `waaronwaar`, `invul`, `open` (examen-modus). Gebruik `invoer` in de
  oefen-data, en `invul` of `open` in proeftoetsen als je tekst wilt.

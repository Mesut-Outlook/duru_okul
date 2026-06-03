# SPEC — Duru's NASK Academie (databestanden)

Je schrijft **één JavaScript-bestand** voor **één onderwerp** van een Nederlandse
natuurkunde-oefensite voor een 14-jarig meisje (Duru) in **MAVO 2**. Alles in het
**Nederlands**, vriendelijk, duidelijk en leuk. Toon: bemoedigend, niet kinderachtig.

Het bestand registreert het onderwerp via `DURU.register({...})`. Format:

```js
DURU.register({
  id: "h4-1",                 // exact id dat in je opdracht staat
  hoofdstuk: 4,               // 4 of 6
  paragraaf: "4.1",           // paragraafnummer als string
  titel: "Wat is snelheid?",  // korte titel
  korteUitleg: "Snelheid, m/s en km/h.", // 1 zin voor de kaart op de homepage
  icoon: "🏎️",                // 1 emoji
  theorie: `...HTML-string...`,
  vragen: [ /* zie hieronder */ ]
});
```

## Theorie (de `theorie` veld = HTML-string)

Schrijf heldere uitleg op MAVO-2-niveau. Gebruik deze KANT-EN-KLARE CSS-klassen
(ze bestaan al in style.css — verzin geen nieuwe):

- `<h3>Kopje</h3>` en `<h4>Subkopje</h4>` voor structuur.
- `<p>...</p>` voor tekst, `<ul><li>` voor lijstjes.
- **Formule** (belangrijk, opvallend):
  ```html
  <div class="formule-box"><span class="formule">snelheid = afstand : tijd</span>
  <small>v in m/s · s = afstand in m · t = tijd in s</small></div>
  ```
- **Uitgewerkt voorbeeld** (laat een berekening stap voor stap zien):
  ```html
  <div class="voorbeeld"><div class="vb-kop">📐 Voorbeeld</div>
  <div class="stap"><b>Gegeven:</b> afstand = 100 m, tijd = 20 s</div>
  <div class="stap"><b>Formule:</b> snelheid = afstand : tijd</div>
  <div class="stap"><b>Berekening:</b> 100 : 20 = 5 m/s</div>
  <div class="stap"><b>Antwoord:</b> de snelheid is 5 m/s</div></div>
  ```
- **Info / let op / tip**:
  ```html
  <div class="info-box"><span class="kop">💡 Onthoud</span> tekst...</div>
  <div class="info-box let-op"><span class="kop">⚠️ Let op</span> tekst...</div>
  <div class="info-box tip"><span class="kop">✅ Handige tip</span> tekst...</div>
  ```
- **Tabel**: `<table class="nask"><tr><th>..</th></tr><tr><td>..</td></tr></table>`
- **Figuur** met bijschrift: `<figure class="bron">...SVG of img...<figcaption>...</figcaption></figure>`

### Visuals = inline SVG (BELANGRIJK)
Maak waar nuttig **eigen, schone inline SVG-tekeningen** (stroomkringen, grafieken,
snelheidsmeters, verhoudingstabellen). Houd ze simpel en kleurrijk. Voorbeeld van
een stroomkring-stijl: rechthoekige draad (`<rect fill=none stroke>`), batterij met
twee streepjes (lang +, kort −), lampje als cirkel met ✕ of een kruis erin.
Gebruik `width="100%"` met een `viewBox` zodat het responsive is, max ±420px breed.
Je mag ook de originele boekpagina's tonen via:
`<img src="extracted_pages/XX.png">` — maar **eigen SVG heeft de voorkeur** (mooier).

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
  vraag: "Wat is de eenheid van snelheid?",
  opties: ["meter (m)", "meter per seconde (m/s)", "seconde (s)", "kilogram (kg)"],
  antwoord: 1,                        // INDEX (0-based) van het juiste antwoord
  uitleg: "Snelheid meet je in <b>m/s</b> of km/h.",
  hint: "Het gaat om afstand én tijd."   // optioneel
}
```

### Type 2 — waar / onwaar
```js
{
  type: "waaronwaar", niveau: 1,
  vraag: "Een voltmeter sluit je in serie aan.",
  antwoord: false,                    // true = Waar, false = Onwaar
  uitleg: "Onwaar: een voltmeter sluit je <b>parallel</b> aan."
}
```

### Type 3 — invoer (zelf antwoord intypen) — GEBRUIK VEEL
```js
{
  type: "invoer", niveau: 2,
  vraag: "Een auto rijdt 150 m in 10 s. Bereken de snelheid.",
  antwoord: "15",        // string; getal met PUNT of komma mag, engine normaliseert
  eenheid: "m/s",        // optioneel; wordt naast het invoerveld getoond
  tolerantie: 0.1,       // optioneel; standaard 2%. Gebruik bij afrondingen.
  uitleg: "snelheid = afstand : tijd = 150 : 10 = <b>15 m/s</b>.",
  hint: "Gebruik snelheid = afstand : tijd."
}
```
- Voor invoer met meerdere goede schrijfwijzen: `antwoord: "15|15,0"` (gescheiden met `|`).
- Vermeld de eenheid in `eenheid`, NIET in het antwoord (de leerling typt alleen het getal).
- `vraag` mag een `figuur` hebben: `figuur: "<svg ...></svg>"` (los veld, naast `vraag`).

## Regels
- **Alles in correct Nederlands.** Gebruik komma als decimaalteken in tekst/uitleg
  (bijv. "13,4 m/s"), maar in het `antwoord`-veld mag punt of komma.
- Reken alles na zodat antwoorden kloppen! Houd getallen MAVO-2-vriendelijk
  (mooie uitkomsten, max 1 decimaal waar kan).
- Spreek Duru af en toe direct aan ("Reken maar uit, Duru!") — spaarzaam, in een paar vragen.
- Verzin afwisselende, herkenbare contexten (fietsen, schaatsen, auto, trein, sprint,
  kerstverlichting, telefoon opladen, zaklamp...). Sluit aan bij het boek.
- Schrijf ALLEEN het ene `DURU.register({...})`-statement in het bestand, niets eromheen.
- Geen externe libraries, geen import/export. Puur ES5/ES6 dat in elke browser werkt.

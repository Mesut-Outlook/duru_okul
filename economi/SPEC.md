# SPEC — Duru's Economie Academie (databestanden)

Je schrijft **één JavaScript-bestand** voor **één onderwerp (paragraaf)** van een
Nederlandse **economie / maatschappijleer**-oefensite voor een 14-jarig meisje (Duru)
in **MAVO 2**. Onderwerp: **Hoofdstuk 6 — De overheid**. Alles in het **Nederlands**,
vriendelijk, duidelijk en leuk. Toon: bemoedigend, niet kinderachtig.

> Dit is een **begrippen-/inzicht-hoofdstuk** (geen rekenvak zoals natuurkunde).
> De meeste vragen zijn dus `mc` en `waaronwaar`, met een paar `invoer`-rekenvragen
> bij btw en de begroting. Decimaalteken in tekst = **komma** (bijv. "€ 21,50").

Het bestand registreert het onderwerp via `DURU.register({...})`. Format:

```js
DURU.register({
  id: "h6-1",                 // exact id dat in je opdracht staat
  hoofdstuk: 6,               // altijd 6
  paragraaf: "6.1",           // paragraafnummer als string
  titel: "Wie is de overheid?",
  korteUitleg: "Rijk, provincie en gemeente.", // 1 zin voor de kaart op de homepage
  icoon: "🏛️",                // 1 emoji
  theorie: `...HTML-string...`,
  vragen: [ /* zie hieronder */ ]
});
```

## Theorie (de `theorie` veld = HTML-string)

Schrijf heldere uitleg op MAVO-2-niveau. Gebruik deze KANT-EN-KLARE CSS-klassen
(ze bestaan al in style.css — verzin geen nieuwe):

- `<h3>Kopje</h3>` en `<h4>Subkopje</h4>` voor structuur.
- `<p>...</p>` voor tekst, `<ul><li>` voor lijstjes.
- **Kernbegrip / definitie** (belangrijk, opvallend) — gebruik de formule-box als "begripkader":
  ```html
  <div class="formule-box"><span class="formule">Collectieve voorzieningen</span>
  <small>spullen en diensten die de overheid voor iedereen regelt en betaalt</small></div>
  ```
- **Uitgewerkt voorbeeld** (bijv. een btw- of begrotingsberekening stap voor stap):
  ```html
  <div class="voorbeeld"><div class="vb-kop">📐 Voorbeeld</div>
  <div class="stap"><b>Gegeven:</b> een spelcomputer kost € 200 (zonder btw), btw is 21%</div>
  <div class="stap"><b>Bereken btw:</b> 21% van € 200 = 0,21 × 200 = € 42</div>
  <div class="stap"><b>Antwoord:</b> je betaalt € 200 + € 42 = <b>€ 242</b></div></div>
  ```
- **Info / let op / tip**:
  ```html
  <div class="info-box"><span class="kop">💡 Onthoud</span> tekst...</div>
  <div class="info-box let-op"><span class="kop">⚠️ Let op</span> tekst...</div>
  <div class="info-box tip"><span class="kop">✅ Handige tip</span> tekst...</div>
  ```
- **Tabel**: `<table class="nask"><tr><th>..</th></tr><tr><td>..</td></tr></table>`
  (gebruik dit bijv. voor "Rijk / provincie / gemeente — wie doet wat").
- **Figuur** met bijschrift: `<figure class="bron">...SVG of img...<figcaption>...</figcaption></figure>`

### Visuals = inline SVG (BELANGRIJK)
Maak waar nuttig **eigen, schone inline SVG-tekeningen** (telijfvrij, geen scans):
- 6.1: een **piramide/lagen-schema** van de overheid: Rijk (Den Haag) bovenaan →
  Provincie → Gemeente onderaan; eventueel iconen.
- 6.2: een rondje "overheid" met pijlen naar voorzieningen (politie, wegen, school, zorg).
- 6.3: een **belastingstroom**: burger/bedrijf → Belastingdienst → voorzieningen terug;
  en/of een kassabon met btw-regel.
- 6.4: een **rijksbegroting** als donut of staafdiagram (inkomsten vs uitgaven),
  en het idee van begrotingstekort (uitgaven > inkomsten) → lenen → staatsschuld.

Gebruik `width="100%"` met een `viewBox` zodat het responsive is, max ±440px breed.
Houd ze simpel en kleurrijk. Je mag ook de originele boekpagina's tonen via
`<img src="extracted_pages/h6_pXX.png">` — maar **eigen SVG heeft de voorkeur** (mooier).

## Vragen (array `vragen`)

Maak **minimaal 14, liefst 16 vragen**. Varieer types en moeilijkheid.
Verdeling moeilijkheid (`niveau`): ~5× niveau 1, ~6× niveau 2, ~4× niveau 3.
Mix de types: ongeveer de helft `mc`, een flink deel `waaronwaar`, en (waar het past)
enkele `invoer`-rekenvragen (vooral bij 6.3 btw en 6.4 begroting — reken alles na!).

Elke vraag heeft een `uitleg` (korte uitgewerkte oplossing / waarom het zo is).
`uitleg` mag HTML bevatten (bijv. `<b>`). Voeg bij lastige vragen een `hint` toe.

### Type 1 — meerkeuze
```js
{
  type: "mc", niveau: 1,
  vraag: "Welke overheidslaag bestuurt heel Nederland?",
  opties: ["De gemeente", "De provincie", "De rijksoverheid", "De waterschappen"],
  antwoord: 2,                        // INDEX (0-based) van het juiste antwoord
  uitleg: "De <b>rijksoverheid</b> (de regering in Den Haag) bestuurt heel het land.",
  hint: "Denk aan Den Haag."          // optioneel
}
```

### Type 2 — waar / onwaar
```js
{
  type: "waaronwaar", niveau: 1,
  vraag: "Btw is een voorbeeld van een directe belasting.",
  antwoord: false,                    // true = Waar, false = Onwaar
  uitleg: "Onwaar: btw is een <b>indirecte</b> belasting (je betaalt het via je aankopen)."
}
```

### Type 3 — invoer (zelf antwoord intypen) — gebruik bij reken-vragen (btw, begroting)
```js
{
  type: "invoer", niveau: 2,
  vraag: "Een spel kost € 200 zonder btw. De btw is 21%. Hoeveel btw betaal je?",
  antwoord: "42",        // string; getal met PUNT of komma mag, engine normaliseert
  eenheid: "euro",       // optioneel; wordt naast het invoerveld getoond
  tolerantie: 0.5,       // optioneel; standaard 2%. Gebruik bij afrondingen.
  uitleg: "21% van € 200 = 0,21 × 200 = <b>€ 42</b>.",
  hint: "Reken 0,21 × 200."
}
```
- Meerdere goede schrijfwijzen: `antwoord: "42|42,00"` (gescheiden met `|`).
- Vermeld de eenheid in `eenheid`, NIET in het antwoord (de leerling typt alleen het getal).
- `vraag` mag een `figuur` hebben: `figuur: "<svg ...></svg>"` (los veld, naast `vraag`).

## Regels
- **Alles in correct Nederlands.** Komma als decimaalteken in tekst/uitleg ("€ 21,50"),
  maar in het `antwoord`-veld mag punt of komma.
- Houd getallen MAVO-2-vriendelijk en reken alles na zodat antwoorden kloppen.
- Spreek Duru af en toe direct aan ("Denk maar mee, Duru!") — spaarzaam, in een paar vragen.
- Verzin herkenbare, actuele contexten (gemeente, paspoort/ID, btw op een telefoon,
  politie & brandweer, wegen & fietspaden, school, AOW/zorg, Prinsjesdag, staatsschuld).
- Schrijf ALLEEN het ene `DURU.register({...})`-statement in het bestand, niets eromheen.
- Geen externe libraries, geen import/export. Puur ES5/ES6 dat in elke browser werkt.

---

## Proeftoets-contract (alleen voor examen_*.js)
Examenbestanden roepen `DURU.registerExamen({...})` aan (niet `register`):
```js
DURU.registerExamen({
  id, titel, vak, icoon, duurMin,      // duurMin = geldig afteltijd in minuten (gebruik 20)
  vragen: [
    { type:"mc",         vraag, opties:[...], antwoord:<index>, uitleg },
    { type:"waaronwaar", vraag, antwoord:<bool>, uitleg },
    { type:"open",       vraag, sleutelwoorden:["a/alt","b"], minTreffers:1,
                         modelantwoord, uitleg },   // automatisch: telt sleutelwoorden
    { type:"invul",      vraag, antwoord:"gemeente|de gemeente", uitleg },
    // elke vraag mag optioneel: figuur:"<svg ...>"
  ]
});
```
`open`: in `sleutelwoorden` betekent `/` = alternatieve schrijfwijzen voor dezelfde sleutel;
`minTreffers` = hoeveel er gevonden moeten worden. Alles gevonden = "goed",
tussen `minTreffers` en alles = "deels" (telt ook als punt). Maak **min. 20, liefst ~24 vragen**.

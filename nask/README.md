# ⚡ Duru's NASK Academie

Een Nederlandse oefensite voor **natuurkunde (NASK)** op **MAVO 2**-niveau, gemaakt
speciaal voor Duru. Met uitleg, uitgewerkte voorbeelden, honderden oefenvragen,
punten (XP), een reeks-teller 🔥 en medailles 🏅.

## Onderwerpen
Gebaseerd op het lesboek (Hoofdstuk 4 & 6):

**Hoofdstuk 4 — Snelheid**
- 4.1 Wat is snelheid? (m/s, km/h, verhoudingstabel)
- 4.2 Snelheid berekenen met de formule (v = s : t)
- 4.2 Eenheden omrekenen: m/s ↔ km/h (÷3,6 en ×3,6)
- 4.2 Gemiddelde snelheid
- 4.3 Reactieafstand, remafstand & stopafstand
- 4.4 Snelheid,tijd- en afstand,tijd-diagram

**Hoofdstuk 6 — Elektriciteit**
- 6.1 Spanning & spanningsbronnen (volt, voltmeter)
- 6.2 Stroomkring & stroomsterkte (ampère, geleider/isolator, schakelsymbolen)
- 6.3 Serie- en parallelschakeling

## 📝 Oefentoetsen (proeftoetsen op tijd)
Naast het oefenen per onderwerp zijn er **3 echte proeftoetsen** (knop "Oefentoetsen"
op de startpagina of in de hero):
- **Oefentoets H4 — Snelheid** (28 vragen)
- **Oefentoets H4 — Snelheid & Beweging** (28 vragen)
- **Oefentoets H6 — Elektriciteit** (28 vragen)

Elke toets heeft een **timer** (20 min), gemengde vraagtypes (meerkeuze, waar/onwaar,
open en invul), navigatie heen-en-weer met genummerde stippen, en aan het eind een
**cijfer (1–10)** plus een **nakijk-scherm** dat bij elke vraag het goede antwoord én
*"zo doe je het"* laat zien.

> De toetsscores worden apart bewaard (sleutel `duru_nask_examens_v1`) en raken de
> XP/medailles/oefen-scores **niet** aan.

## Starten
**Makkelijkste manier:** dubbelklik op **`Duru_NASK_Baslat.command`**.
De site opent vanzelf in je browser. Laat het zwarte venster open tijdens het oefenen.

**Of:** open gewoon `index.html` in een browser (Chrome, Safari, Edge).

## Hoe werkt het?
1. Kies op de startpagina een onderwerp.
2. Lees eerst de **theorie** (uitleg + voorbeelden).
3. Klik op **Start de oefentoets** en beantwoord de vragen.
4. Bij elke vraag krijg je meteen uitleg. Verzamel XP, houd je 🔥-reeks vast en
   vang alle medailles!
5. Je voortgang (beste scores + medailles) wordt automatisch op deze computer bewaard.

## Voor de maker (techniek)
- Pure HTML/CSS/JavaScript, geen build-stap, geen dependencies.
- Quizmotor: `js/engine.js` · startobject: `js/bootstrap.js`.
- Content per onderwerp: `js/data/*.js` (elk roept `DURU.register({...})` aan).
- Het contract voor de databestanden staat in `SPEC.md`.
- Originele boekpagina's (scans) staan in `extracted_pages/` als referentie.

### Een onderwerp toevoegen / aanpassen
Maak een nieuw bestand in `js/data/`, volg `SPEC.md`, en voeg een `<script>`-regel
toe in `index.html` (bij de andere data-scripts). Klaar.

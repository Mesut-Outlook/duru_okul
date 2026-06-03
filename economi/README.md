# 🏛️ Duru's Economie Academie

Een Nederlandse oefensite voor **economie / maatschappijleer** op **MAVO 2**-niveau,
gemaakt speciaal voor Duru. Met uitleg, voorbeelden, honderden oefenvragen, punten (XP),
een reeks-teller 🔥 en medailles 🏅.

## Onderwerpen
Gebaseerd op het lesboek **Hoofdstuk 6 — De overheid**:

- **6.1 Wie is de overheid?** — Rijksoverheid (Den Haag), provincie en gemeente: wie doet wat.
- **6.2 Waar zorgt de overheid voor?** — collectieve voorzieningen: veiligheid, wegen,
  onderwijs, zorg — en waarom de overheid dat doet.
- **6.3 Betalen aan de overheid** — belastingen: inkomstenbelasting, loonbelasting en btw;
  directe en indirecte belasting; waarom we belasting betalen.
- **6.4 Is de schatkist goed gevuld?** — de rijksbegroting: inkomsten en uitgaven,
  begrotingstekort/-overschot, lenen en de staatsschuld.

## 📝 Oefentoetsen (proeftoetsen op tijd)
Naast het oefenen per onderwerp zijn er **proeftoetsen** met een **timer** (20 min),
gemengde vraagtypes (meerkeuze, waar/onwaar, open en invul), navigatie met genummerde
stippen, en aan het eind een **cijfer (1–10)** plus een **nakijk-scherm** dat bij elke
vraag het goede antwoord én *"zo doe je het"* laat zien.

> De toetsscores worden apart bewaard (sleutel `duru_economi_examens_v1`) en raken de
> XP/medailles/oefen-scores **niet** aan.

## Starten
**Makkelijkste manier:** dubbelklik op **`Duru_Economi_Baslat.command`**.
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
- Quizmotor: `js/engine.js` · startobject: `js/bootstrap.js` · toetsmotor: `js/exams.js`.
- Content per onderwerp: `js/data/*.js` (elk roept `DURU.register({...})` aan).
- Het contract voor de databestanden staat in `SPEC.md`.
- Afgeleid van het zusterproject **Duru's NASK Academie** (zelfde motor, andere inhoud).

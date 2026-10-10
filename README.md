# Duru's School

Eén plek met al Duru's oefensites, onder één link. Pure HTML/CSS/JS — geen installatie, geen build.

**Online:** https://mesut-outlook.github.io/duru_okul/ — werkt ook op de telefoon.

## Vakken — schooljaar 2026-2027 · HAVO 3

Twaalf vakken, elk met uitleg per onderwerp en proeftoetsen per hoofdstuk, in `havo3/<vak>/`:

| Talen | Exact | Mens & maatschappij |
|---|---|---|
| Nederlands | Wiskunde | Geschiedenis |
| Engels | Natuurkunde | Aardrijkskunde |
| Frans | Scheikunde | Economie |
| Duits | Biologie | Maatschappijleer |

Vorige schooljaren staan in `archief/<schooljaar>/` (bv. `archief/2025-2026/` = MAVO 2) en zijn
op de startpagina te openen via **"Archief — vorige schooljaren"**. Resultaten van toen blijven zichtbaar.

## Gebruiken

- **Inloggen:** Duru met haar eigen knop; **Baba** (ouder) met een eigen wachtwoord.
- Klik op een vak → de oefensite opent in de hub. Terug: **"← Terug naar de vakken"**, de **Escape**-toets
  of de **terugknop** van de browser.
- **Mijn prestaties:** Duru's voortgang — wat nu te oefenen, cijfers per vak en hoofdstuk, logboek.
- **Ouderpaneel** (alleen Baba, in het Turks): gemiddelde, aandachtspunten, open toetsen, tijd per toets,
  en per poging de vragen met Duru's antwoorden.
- Resultaten worden via de cloud gesynchroniseerd tussen apparaten.

## Lokaal starten

Dubbelklik op **`Duru_Okul_Baslat.command`**, of in deze map:

```bash
python3 -m http.server 8125     # → http://localhost:8125/
```

Vanaf de telefoon in hetzelfde wifi-netwerk: `http://<ip-van-de-computer>:8125/`.

## Hosting

Elke `git push` naar `main` publiceert de site automatisch via GitHub Actions op GitHub Pages
(`.github/workflows/deploy.yml`).

Voor ontwikkelaars: zie `CLAUDE.md` (architectuur, regels, commando's) en `docs/`.

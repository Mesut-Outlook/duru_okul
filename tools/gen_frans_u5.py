#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator voor Frans Unité 5 (Au resto!)
Boek: Grandes Lignes 3 HAVO, Chapitre 5 (p. 194-198)

Genereert:
- 4 Oefenlessen / Onderwerpen (h5_1.js t/m h5_4.js):
  - 5.1 Vocabulaire A & B: Eten, drinken, bestellingen & restauranttermen
  - 5.2 Vocabulaire E & F: Tafelgerei, sauzen, smaakmakers & milieu
  - 5.3 Phrases-clés C & G: Gespreksvaardigheid: bestellen, vragen stellen & problemen oplossen
  - 5.4 Grammaire D & H: Het delend lidwoord (article partitif) & Het werkwoord venir
- 5 Begrippentoetsen / Proeftoetsen (examen_u5_vocab_1.js t/m examen_u5_vocab_5.js)
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "havo3", "frans", "js", "data")

ONDERWERPEN = [
    # H5 §5.1
    {
        "id": "fr-u5-1",
        "hoofdstuk": 5,
        "paragraaf": "5.1",
        "titel": "Vocabulaire A & B · Eten, drinken, maaltijden & restauranttermen",
        "korteUitleg": "De kernwoordenschat van Unité 5 Blok A en B: etenswaren, drinken, het uitdrukken van honger en dorst, en handige werkwoorden rond bestellen en eten.",
        "icoon": "🍽️",
        "kleur": "oranje",
        "theorie": """
    <h3>5.1 Vocabulaire A & B: Eten, drinken & bestellen</h3>
    <div class="info-box">
      <b>Bienvenue au resto!</b> In dit hoofdstuk leer je hoe je in Frankrijk eten en drinken bestelt in een bistro, café of restaurant. We beginnen met de belangrijkste basiswoorden uit Blok A en B (p. 194).
    </div>

    <h4>1. Vaste uitdrukkingen met avoir (hebben)</h4>
    <p>In het Frans gebruik je het werkwoord <b>avoir</b> (hebben) voor lichamelijke gewaarwordingen waar wij in het Nederlands 'zijn' gebruiken:</p>
    <ul>
      <li><b>avoir faim</b> = honger hebben (<i>J'ai très faim!</i> = Ik heb erge honger!)</li>
      <li><b>avoir soif</b> = dorst hebben (<i>Tu as soif?</i> = Heb je dorst?)</li>
      <li><b>avoir besoin de</b> = nodig hebben (<i>J'ai besoin d'eau.</i> = Ik heb water nodig.)</li>
      <li><b>avoir l'air</b> = eruitzien (<i>Ce plat a l'air délicieux!</i> = Dit gerecht ziet er heerlijk uit!)</li>
    </ul>

    <h4>2. Eten en drinken (La nourriture et les boissons)</h4>
    <table class="vocab-table">
      <thead><tr><th>Frans</th><th>Nederlands</th><th>Genre / Type</th></tr></thead>
      <tbody>
        <tr><td><b>la viande</b></td><td>het vlees</td><td>vrouwelijk (la)</td></tr>
        <tr><td><b>le bœuf</b></td><td>het rundvlees</td><td>mannelijk (le)</td></tr>
        <tr><td><b>le poisson</b></td><td>de vis</td><td>mannelijk (le)</td></tr>
        <tr><td><b>la crêpe</b></td><td>de pannenkoek</td><td>vrouwelijk (la)</td></tr>
        <tr><td><b>le fromage</b></td><td>de kaas</td><td>mannelijk (le)</td></tr>
        <tr><td><b>la glace</b></td><td>het ijs</td><td>vrouwelijk (la)</td></tr>
        <tr><td><b>le lait</b></td><td>de melk</td><td>mannelijk (le)</td></tr>
        <tr><td><b>le verre</b></td><td>het glas</td><td>mannelijk (le)</td></tr>
        <tr><td><b>la bouteille</b></td><td>de fles</td><td>vrouwelijk (la)</td></tr>
        <tr><td><b>la tasse</b></td><td>het kopje</td><td>vrouwelijk (la)</td></tr>
        <tr><td><b>la boîte</b></td><td>de doos, het blik</td><td>vrouwelijk (la)</td></tr>
      </tbody>
    </table>

    <h4>3. Belangrijke werkwoorden en signaalwoorden (Blok A & B)</h4>
    <ul>
      <li><b>manger</b> = eten | <b>commander</b> = bestellen | <b>sauver</b> = redden | <b>hésiter</b> = twijfelen</li>
      <li><b>travailler</b> = werken | <b>raconter</b> = vertellen | <b>apprendre</b> = leren | <b>devenir</b> = worden</li>
      <li><b>il faut</b> = je moet / het is nodig dat | <b>mettre</b> = zetten, leggen, aandoen</li>
      <li><b>enfin</b> = (uit)eindelijk | <b>peut-être</b> = misschien | <b>trop (de)</b> = te (veel) | <b>quelque chose</b> = iets</li>
      <li><b>d'abord</b> = ten eerste, eerst | <b>ensuite</b> = daarna | <b>car</b> = want | <b>donc</b> = dus</li>
      <li><b>le cuisinier</b> = de kok | <b>le repas</b> = de maaltijd | <b>le conseil</b> = het advies | <b>la formation</b> = de opleiding</li>
    </ul>
""",
        "vragen": [
            {
                "type": "mc",
                "vraag": "Wat betekent de Franse uitdrukking <b>'avoir faim'</b>?",
                "opties": [
                    "dorst hebben",
                    "honger hebben",
                    "het koud hebben",
                    "slaap hebben"
                ],
                "antwoord": 1,
                "uitleg": "'Avoir faim' betekent honger hebben in het Frans."
            },
            {
                "type": "mc",
                "vraag": "Welk Frans woord betekent <b>'het rundvlees'</b>?",
                "opties": [
                    "le poisson",
                    "la viande",
                    "le bœuf",
                    "le poulet"
                ],
                "antwoord": 2,
                "uitleg": "'Le bœuf' is het Franse woord voor rundvlees."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse werkwoord <b>'commander'</b> in een restaurant?",
                "opties": [
                    "afwassen",
                    "klaarmaken",
                    "betalen",
                    "bestellen"
                ],
                "antwoord": 3,
                "uitleg": "'Commander' betekent bestellen (bijv. commander un repas)."
            },
            {
                "type": "mc",
                "vraag": "Wat is de juiste betekenis van het Franse woord <b>'le cuisinier'</b>?",
                "opties": [
                    "de kok",
                    "de ober",
                    "de bakker",
                    "de eigenaar"
                ],
                "antwoord": 0,
                "uitleg": "'Le cuisinier' is de kok in de keuken."
            },
            {
                "type": "waaronwaar",
                "vraag": "De Franse uitdrukking 'avoir soif' betekent 'haast hebben'.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Avoir soif' betekent dorst hebben. Haast hebben is 'être pressé'."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Franse zelfstandig naamwoord 'la bouteille' betekent 'de fles'.",
                "antwoord": True,
                "uitleg": "Waar! 'La bouteille' is de fles (bijv. une bouteille d'eau)."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Franse woord 'le verre' betekent uitsluitend 'de lepel'.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Le verre' betekent het glas. De lepel is 'la cuillère'."
            },
            {
                "type": "invoer",
                "vraag": "Vertaal de uitdrukking tussen haakjes: 'J'ai très (dorst), je voudrais de l'eau.' Vul het Franse woord in (soif):",
                "antwoord": "soif",
                "uitleg": "Dorst hebben is 'avoir soif'."
            },
            {
                "type": "invoer",
                "vraag": "Vertaal het Franse woord voor 'de pannenkoek' (vrouwelijk met lidwoord, la crêpe):",
                "antwoord": "la crêpe|la crepe|crêpe|crepe",
                "uitleg": "De pannenkoek is in het Frans 'la crêpe'."
            },
            {
                "type": "invoer",
                "vraag": "Vul de juiste vorm in: 'Ce dessert a l'____ (ziet eruit) délicieux!' Vul het ontbrekende woord in (air):",
                "antwoord": "air",
                "uitleg": "Eruitzien is de vaste uitdrukking 'avoir l'air'."
            }
        ]
    },

    # H5 §5.2
    {
        "id": "fr-u5-2",
        "hoofdstuk": 5,
        "paragraaf": "5.2",
        "titel": "Vocabulaire E & F · Tafelgerei, sauzen, smaakmakers & milieu",
        "korteUitleg": "Woordenschat van Unité 5 Blok E en F: alles over de gedekte tafel (bestek, servet, bord), sauzen en smaakmakers, én maatschappelijke thema's zoals de zee, vervuiling en bescherming.",
        "icoon": "🧂",
        "kleur": "blauw",
        "theorie": """
    <h3>5.2 Vocabulaire E & F: Tafelgerei, sauzen & milieu</h3>
    <div class="info-box">
      <b>Mettre la table:</b> In Blok E en F leer je alle benodigdheden op tafel te benoemen, van vork tot pepermolen, én lees je Franse teksten over duurzaamheid en oceaanbescherming.
    </div>

    <h4>1. Tafelgerei en bestek (Les couverts et la table)</h4>
    <table class="vocab-table">
      <thead><tr><th>Frans</th><th>Nederlands</th><th>Voorbeeld</th></tr></thead>
      <tbody>
        <tr><td><b>le couteau</b></td><td>het mes</td><td><i>Je n'ai pas de couteau.</i></td></tr>
        <tr><td><b>la fourchette</b></td><td>de vork</td><td><i>Manger avec une fourchette.</i></td></tr>
        <tr><td><b>la cuillère</b></td><td>de lepel</td><td><i>Une cuillère à soupe.</i></td></tr>
        <tr><td><b>l'assiette</b> (v)</td><td>het bord</td><td><i>Une assiette propre.</i></td></tr>
        <tr><td><b>la serviette</b></td><td>het servet</td><td><i>Essuyer la bouche avec la serviette.</i></td></tr>
        <tr><td><b>la carte</b></td><td>de menukaart</td><td><i>Vous désirez la carte?</i></td></tr>
        <tr><td><b>le pourboire</b></td><td>de fooi</td><td><i>Laisser un pourboire au serveur.</i></td></tr>
        <tr><td><b>le petit boulot</b></td><td>het bijbaantje</td><td><i>Travailler comme petit boulot.</i></td></tr>
      </tbody>
    </table>

    <h4>2. Sauzen en smaakmakers (Condiments et sauces)</h4>
    <ul>
      <li><b>le sel</b> = het zout | <b>le poivre</b> = de peper</li>
      <li><b>la moutarde</b> = de mosterd | <b>le beurre</b> = de boter</li>
      <li><b>la sauce</b> = de saus | <b>le ketchup</b> = de ketchup</li>
      <li><b>râler</b> = klagen, mopperen | <b>apporter</b> = brengen | <b>retourner</b> = teruggaan</li>
      <li><b>ce n'est pas grave</b> = het is niet erg</li>
    </ul>

    <h4>3. De zee, natuur en milieu (Blok F)</h4>
    <p>In het thematische deel van Blok F ontdek je Franse maatschappelijke thema's:</p>
    <ul>
      <li><b>la mer</b> = de zee | <b>le bateau</b> = de boot | <b>le poisson</b> = de vis</li>
      <li><b>la pollution</b> = de vervuiling | <b>protéger</b> = beschermen | <b>menacer</b> = bedreigen</li>
      <li><b>tuer</b> = doden | <b>attirer l'attention</b> = de aandacht trekken | <b>la construction</b> = de bouw</li>
      <li><b>délicieux, délicieuse</b> = heerlijk | <b>cassé(e)</b> = gebroken, kapot | <b>chaud(e)</b> = warm</li>
      <li><b>rencontrer</b> = ontmoeten | <b>rêver</b> = dromen | <b>nager</b> = zwemmen | <b>décrire</b> = beschrijven</li>
      <li><b>surtout</b> = vooral | <b>seulement</b> = alleen (maar) | <b>un peu (de)</b> = een beetje</li>
    </ul>
""",
        "vragen": [
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'la fourchette'</b>?",
                "opties": [
                    "de vork",
                    "het servet",
                    "het mes",
                    "de lepel"
                ],
                "antwoord": 0,
                "uitleg": "'La fourchette' is de vork in het Frans."
            },
            {
                "type": "mc",
                "vraag": "Welk Frans woord betekent <b>'de fooi'</b> voor een kelner?",
                "opties": [
                    "la facture",
                    "le pourboire",
                    "l'addition",
                    "la carte"
                ],
                "antwoord": 1,
                "uitleg": "'Le pourboire' is de fooi die je achterlaat voor goede bediening."
            },
            {
                "type": "mc",
                "vraag": "Wat is de betekenis van het Franse zelfstandig naamwoord <b>'le sel'</b>?",
                "opties": [
                    "de suiker",
                    "de peper",
                    "het zout",
                    "de mosterd"
                ],
                "antwoord": 2,
                "uitleg": "'Le sel' betekent het zout."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse werkwoord <b>'protéger'</b>?",
                "opties": [
                    "vervuilen",
                    "beschrijven",
                    "onderzoeken",
                    "beschermen"
                ],
                "antwoord": 3,
                "uitleg": "'Protéger' betekent beschermen (bijvoorbeeld la nature)."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Franse woord 'l'assiette' is een mannelijk zelfstandig naamwoord.",
                "antwoord": False,
                "uitleg": "Onwaar! 'L'assiette' is vrouwelijk: une assiette."
            },
            {
                "type": "waaronwaar",
                "vraag": "De uitdrukking 'ce n'est pas grave' betekent in het Nederlands 'het is niet erg'.",
                "antwoord": True,
                "uitleg": "Waar! 'Ce n'est pas grave' stelt iemand gerust: het geeft niet / het is niet erg."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Franse werkwoord 'râler' betekent feestvieren en juichen.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Râler' is een typisch Frans werkwoord dat klagen of mopperen betekent."
            },
            {
                "type": "invoer",
                "vraag": "Vertaal het woord voor 'het mes' in het Frans (met lidwoord, le couteau):",
                "antwoord": "le couteau|couteau",
                "uitleg": "Het mes is 'le couteau'."
            },
            {
                "type": "invoer",
                "vraag": "Vertaal het woord tussen haakjes: 'Il mange du pain avec du (boter).' Vul het Franse woord in (beurre):",
                "antwoord": "beurre",
                "uitleg": "Boter is 'le beurre'."
            },
            {
                "type": "invoer",
                "vraag": "Vertaal het woord voor 'de vervuiling' in het Frans (vrouwelijk met lidwoord, la pollution):",
                "antwoord": "la pollution|pollution",
                "uitleg": "De vervuiling is 'la pollution'."
            }
        ]
    },

    # H5 §5.3
    {
        "id": "fr-u5-3",
        "hoofdstuk": 5,
        "paragraaf": "5.3",
        "titel": "Phrases-clés C & G · Gesprekken in het restaurant (Bestellen & Problemen oplossen)",
        "korteUitleg": "Gespreksvaardigheid in een Frans restaurant (Phrases-clés p. 196): een bestelling doorgeven, vragen naar het dagmenu, en beleefd reageren bij vergissingen of ontbrekend bestek.",
        "icoon": "🗣️",
        "kleur": "paars",
        "theorie": """
    <h3>5.3 Phrases-clés C & G: Gesprekken in het restaurant</h3>
    <div class="info-box">
      <b>Parler au restaurant:</b> In deze paragraaf oefen je levensechte Franse dialogen: met vrienden overleggen wat je bestelt (Blok C) en de ober aanspreken als er iets ontbreekt of misgaat (Blok G).
    </div>

    <h4>1. Blok C: Aller au restaurant avec un ami (Overleggen & Bestellen)</h4>
    <table class="vocab-table">
      <thead><tr><th>Nederlands</th><th>Français</th></tr></thead>
      <tbody>
        <tr><td>Wat wil je drinken?</td><td><b>Qu'est-ce que tu veux boire?</b></td></tr>
        <tr><td>Ik wil graag een glas water.</td><td><b>Je voudrais un verre d'eau.</b></td></tr>
        <tr><td>Wat neem jij?</td><td><b>Qu'est-ce que tu prends?</b></td></tr>
        <tr><td>Ik neem het dagmenu.</td><td><b>Je prends le plat du jour.</b></td></tr>
        <tr><td>Wat is het dagmenu?</td><td><b>Qu'est-ce que c'est le plat du jour?</b></td></tr>
        <tr><td>Dat is kip met olijven.</td><td><b>C'est le poulet aux olives.</b></td></tr>
        <tr><td>Neem je ook een toetje?</td><td><b>Tu prends aussi un dessert?</b></td></tr>
        <tr><td>Ik weet het nog niet.</td><td><b>Je ne sais pas encore.</b></td></tr>
        <tr><td>Zullen we bestellen?</td><td><b>Alors, on commande?</b></td></tr>
        <tr><td>Ja, ik heb honger.</td><td><b>Oui, j'ai faim.</b></td></tr>
      </tbody>
    </table>

    <h4>2. Blok G: Se débrouiller au restaurant (Problemen & Vragen oplossen)</h4>
    <p>Als een gerecht niet klopt of koud is, los je dat beleefd op in het Frans:</p>
    <ul>
      <li><b>Excusez-moi, il y a une erreur. Je n'ai pas commandé de poisson.</b> = Pardon, er is een foutje. Ik heb geen vis besteld.</li>
      <li><b>Je peux avoir de la mayonnaise?</b> = Mag ik mayonaise?</li>
      <li><b>Je n'ai pas de couteau.</b> = Ik heb geen mes.</li>
      <li><b>Vous avez encore du pain?</b> = Heeft u nog brood?</li>
      <li><b>Il y a des noix dans ce plat?</b> = Zitten er noten in dit gerecht? (Cruciaal bij allergieën!)</li>
      <li><b>Mes frites sont froides.</b> = Mijn frietjes zijn koud.</li>
      <li><b>Une carafe d'eau, s'il vous plaît.</b> = Een karaf water, alstublieft. (Gratis kraanwater in Frankrijk!)</li>
    </ul>

    <div class="tip-box">
      <b>Tip voor Frankrijk:</b> Als je <i>"une carafe d'eau"</i> vraagt, krijg je een karaf gratis kraanwater. Vraag je <i>"une bouteille d'eau"</i>, dan betaal je voor bronwater!
    </div>
""",
        "vragen": [
            {
                "type": "mc",
                "vraag": "Hoe vraag je in het Frans beleefd om een karaf kraanwater?",
                "opties": [
                    "Une carafe d'eau, s'il vous plaît.",
                    "Je veux du jus d'orange tout de suite.",
                    "Apportez-moi une bière froide.",
                    "Où sont les toilettes du restaurant?"
                ],
                "antwoord": 0,
                "uitleg": "'Une carafe d'eau, s'il vous plaît' is de standaard Franse beleefdheidszin voor kraanwater."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de Franse zin <b>'Je prends le plat du jour'</b>?",
                "opties": [
                    "Ik betaal de rekening vandaag.",
                    "Ik neem het dagmenu.",
                    "Ik wil alleen een toetje.",
                    "Ik ga vandaag koken."
                ],
                "antwoord": 1,
                "uitleg": "'Le plat du jour' is het dagmenu of de dagschotel."
            },
            {
                "type": "mc",
                "vraag": "Hoe meld je aan de ober dat je frietjes koud geserveerd zijn?",
                "opties": [
                    "Mes frites sont trop chaudes.",
                    "J'adore ces frites délicieuses.",
                    "Mes frites sont froides.",
                    "Il n'y a pas de sel sur mes frites."
                ],
                "antwoord": 2,
                "uitleg": "'Mes frites sont froides' betekent dat de friet koud is."
            },
            {
                "type": "mc",
                "vraag": "Wat vraag je als je allergisch bent en wilt weten of er noten in het eten zitten?",
                "opties": [
                    "Vous avez du poisson sans arêtes?",
                    "Est-ce qu'il y a du sel dans la soupe?",
                    "Je peux avoir du ketchup?",
                    "Il y a des noix dans ce plat?"
                ],
                "antwoord": 3,
                "uitleg": "'Des noix' zijn noten (walnoten/noten)."
            },
            {
                "type": "waaronwaar",
                "vraag": "De Franse zin 'Alors, on commande?' betekent 'Gaan we nu afrekenen?'.",
                "antwoord": False,
                "uitleg": "Onwaar! Het betekent 'Zullen we bestellen?' (commander = bestellen)."
            },
            {
                "type": "waaronwaar",
                "vraag": "Met de zin 'Je peux avoir de la mayonnaise?' vraag je vriendelijk om mayonaise.",
                "antwoord": True,
                "uitleg": "Waar! 'Je peux avoir...' betekent 'Mag ik... / Kan ik ... krijgen?'."
            },
            {
                "type": "waaronwaar",
                "vraag": "Als er een fout in de bestelling zit, zeg je 'Excusez-moi, il y a une erreur'.",
                "antwoord": True,
                "uitleg": "Waar! 'Il y a une erreur' betekent 'er is een vergissing/foutje gemaakt'."
            },
            {
                "type": "invoer",
                "vraag": "Vul het ontbrekende woord in voor 'een foutje': 'Excusez-moi, il y a une ____.' (erreur)",
                "antwoord": "erreur",
                "uitleg": "Er is een vergissing gemaakt = 'il y a une erreur'."
            },
            {
                "type": "invoer",
                "vraag": "Vertaal de zin tussen haakjes: '(Ik weet het nog niet)' ➔ 'Je ne sais pas ____.'",
                "antwoord": "encore",
                "uitleg": "Nog niet = 'pas encore'."
            },
            {
                "type": "invoer",
                "vraag": "Hoe vraag je 'Heeft u nog brood?' Vul het Franse woord voor 'brood' in: 'Vous avez encore du ____?'",
                "antwoord": "pain",
                "uitleg": "Brood is in het Frans 'le pain'."
            }
        ]
    },

    # H5 §5.4
    {
        "id": "fr-u5-4",
        "hoofdstuk": 5,
        "paragraaf": "5.4",
        "titel": "Grammaire D & H · Het delend lidwoord & Het onregelmatige werkwoord venir",
        "korteUitleg": "De twee grammatica-pijlers van Unité 5: het delend lidwoord (du, de la, de l', des en uitzonderingen na hoeveelheden/ontkenningen) én de vervoeging van venir in de présent en passé composé.",
        "icoon": "🧀",
        "kleur": "groen",
        "theorie": """
    <h3>5.4 Grammaire D & H: Delend lidwoord & Werkwoord venir</h3>
    <div class="info-box">
      <b>Grammatica Unité 5 (p. 197):</b> Twee essentiële grammaticatheorieën die elke HAVO 3-leerling foutloos moet beheersen: wanneer gebruik je <i>du, de la, de l', des</i> en hoe vervoeg je <i>venir</i>?
    </div>

    <h4>1. Het delend lidwoord (L'article partitif)</h4>
    <p>Als je in het Nederlands géén lidwoord gebruikt bij een onbepaalde hoeveelheid (zoals <i>"Ik koop vis, vlees en water"</i>), staat er in het Frans <b>verplicht</b> een delend lidwoord:</p>
    <ul>
      <li>Mannelijk enkelvoud: <b>du</b> ➔ <i>J'achète <b>du</b> poisson / <b>du</b> fromage.</i></li>
      <li>Vrouwelijk enkelvoud: <b>de la</b> ➔ <i>J'achète <b>de la</b> viande / <b>de la</b> confiture.</i></li>
      <li>Vóór klinker of stomme h: <b>de l'</b> ➔ <i>J'achète <b>de l'</b>eau / <b>de l'</b>huile.</i></li>
      <li>Meervoud: <b>des</b> ➔ <i>J'achète <b>des</b> légumes / <b>des</b> frites.</i></li>
    </ul>

    <h4>2. Uitzonderingen: wanneer verandert het in alleen de of d'?</h4>
    <div class="formule-box">
      <b>Regel 1: Na een woord van hoeveelheid gebruik je altijd alleen DE of D' (nooit du/des)!</b><br>
      • <i>un verre <b>d'</b>eau</i> (een glas water)<br>
      • <i>un kilo <b>de</b> pommes</i> (een kilo appels)<br>
      • <i>beaucoup <b>de</b> temps</i> (veel tijd) | <i>trop <b>de</b> sucre</i> (te veel suiker) | <i>un peu <b>de</b> sel</i> (een beetje zout)<br>
      • <i>une bouteille <b>de</b> vin</i> (een fles wijn)<br><br>
      <b>Regel 2: In een ontkenning (ne ... pas) wordt het delend lidwoord ook DE of D'!</b><br>
      • <i>Je prends du sucre.</i> ➔ <i>Je ne prends <b>pas de</b> sucre.</i><br>
      • <i>Elle a des amis.</i> ➔ <i>Elle n'a <b>pas d'</b>amis.</i><br><br>
      <b>Regel 3: Na werkwoorden van waardering (aimer, adorer, préférer, détester) gebruik je LE, LA, L', LES!</b><br>
      • <i>J'aime <b>le</b> poisson, mais je préfère <b>la</b> viande.</i> (Geen 'du', want het gaat om vis/vlees in het algemeen).
    </div>

    <h4>3. Het onregelmatige werkwoord venir (komen)</h4>
    <p>Het werkwoord <b>venir</b> is onregelmatig. Leer deze vormen uit je hoofd:</p>
    <table class="vocab-table">
      <thead><tr><th>Persoon</th><th>Présent (tegenwoordige tijd)</th><th>Vertaling</th></tr></thead>
      <tbody>
        <tr><td>je</td><td><b>viens</b></td><td>ik kom</td></tr>
        <tr><td>tu</td><td><b>viens</b></td><td>jij komt</td></tr>
        <tr><td>il / elle / on</td><td><b>vient</b></td><td>hij / zij / men komt</td></tr>
        <tr><td>nous</td><td><b>venons</b></td><td>wij komen</td></tr>
        <tr><td>vous</td><td><b>venez</b></td><td>jullie komen / u komt</td></tr>
        <tr><td>ils / elles</td><td><b>viennent</b></td><td>zij komen</td></tr>
      </tbody>
    </table>

    <p><b>Passé composé van venir:</b> wordt gevormd met <b>être</b> en het voltooid deelwoord <b>venu</b>. Let op het accord (geslacht en getal):</p>
    <ul>
      <li><i>Il est venu en train.</i> (mannelijk enkelvoud)</li>
      <li><i>Elle est venue à trois heures.</i> (vrouwelijk enkelvoud: +e)</li>
      <li><i>Ils sont venus ensemble.</i> (mannelijk meervoud: +s)</li>
      <li><i>Elles sont venues en bus.</i> (vrouwelijk meervoud: +es)</li>
    </ul>
""",
        "vragen": [
            {
                "type": "mc",
                "vraag": "Kies het juiste delend lidwoord: 'Tous les matins, je bois ____ (melk, m).'",
                "opties": [
                    "de la",
                    "des",
                    "de",
                    "du"
                ],
                "antwoord": 3,
                "uitleg": "'Lait' is mannelijk (le lait), dus het delend lidwoord is 'du lait'."
            },
            {
                "type": "mc",
                "vraag": "Kies de juiste vorm na een hoeveelheid: 'Je voudrais un verre ____ (water).'",
                "opties": [
                    "d'",
                    "de l'",
                    "du",
                    "des"
                ],
                "antwoord": 0,
                "uitleg": "Na een hoeveelheid (un verre) gebruik je de of d' voor een klinker: 'un verre d'eau'."
            },
            {
                "type": "mc",
                "vraag": "Welk lidwoord gebruik je na 'aimer': 'J'aime beaucoup ____ (chocolade, m).'",
                "opties": [
                    "du",
                    "le",
                    "de la",
                    "de"
                ],
                "antwoord": 1,
                "uitleg": "Na voorkeurswerkwoorden (aimer, adorer, préférer) gebruik je het bepaald lidwoord: 'le chocolat'."
            },
            {
                "type": "mc",
                "vraag": "Wat is de juiste vorm van het werkwoord 'venir' bij 'ils' in de tegenwoordige tijd?",
                "opties": [
                    "ils venons",
                    "ils venez",
                    "ils viennent",
                    "ils vient"
                ],
                "antwoord": 2,
                "uitleg": "Bij ils/elles is de vorm 'viennent' (ils viennent)."
            },
            {
                "type": "waaronwaar",
                "vraag": "In een ontkennende zin (ne ... pas) verandert het delend lidwoord 'du' in 'de' of 'd''.",
                "antwoord": True,
                "uitleg": "Waar! 'Je ne prends pas de sucre' (in plaats van du sucre)."
            },
            {
                "type": "waaronwaar",
                "vraag": "De passé composé van 'venir' wordt gevormd met het hulpwerkwoord 'avoir' (j'ai venu).",
                "antwoord": False,
                "uitleg": "Onwaar! Venir is een werkwoord van beweging en vervoegt met être: 'je suis venu(e)'."
            },
            {
                "type": "waaronwaar",
                "vraag": "In de zin 'Elles sont venues' krijgt 'venues' de uitgang -es omdat het onderwerp vrouwelijk meervoud is.",
                "antwoord": True,
                "uitleg": "Waar! Bij être past het voltooid deelwoord zich aan aan het onderwerp (accord)."
            },
            {
                "type": "invoer",
                "vraag": "Vul het juiste delend lidwoord in voor 'viande' (vrouwelijk enkelvoud): 'Elle mange ____ viande tous les soirs.'",
                "antwoord": "de la",
                "uitleg": "Viande is vrouwelijk, dus 'de la viande'."
            },
            {
                "type": "invoer",
                "vraag": "Vul de juiste persoonsvorm in van 'venir' bij 'nous' in de présent: 'Nous ____ (komen) à six heures.'",
                "antwoord": "venons",
                "uitleg": "Bij nous is de vorm 'venons'."
            },
            {
                "type": "invoer",
                "vraag": "Vul het juiste woord in na de ontkenning: 'Non merci, je ne prends pas ____ (geen) sucre.'",
                "antwoord": "de",
                "uitleg": "Na 'ne ... pas' gebruik je 'de' (pas de sucre)."
            }
        ]
    }
]

EXAMENS = [
    # Toets 1 (ex-h3-frans-u5-v1)
    {
        "id": "ex-h3-frans-u5-v1",
        "hoofdstuk": 5,
        "hoofdstukTitel": "Unité 5 — Au resto!",
        "titel": "Woordenschat 1 · Au resto: Eten, drinken & bestellingen (Vocabulaire A & B)",
        "duurMin": 20,
        "vak": "Frans · HAVO 3 (U5)",
        "icoon": "🍽️",
        "vragen": [
            # 12 MC: 3x0, 3x1, 3x2, 3x3
            {
                "type": "mc",
                "vraag": "Wat betekent de Franse uitdrukking <b>'avoir soif'</b>?",
                "opties": [
                    "dorst hebben",
                    "honger hebben",
                    "slaap hebben",
                    "kou vatten"
                ],
                "antwoord": 0,
                "uitleg": "'Avoir soif' betekent dorst hebben."
            },
            {
                "type": "mc",
                "vraag": "Welk Frans woord betekent <b>'de pannenkoek'</b>?",
                "opties": [
                    "le fromage",
                    "la crêpe",
                    "la viande",
                    "le dessert"
                ],
                "antwoord": 1,
                "uitleg": "'La crêpe' is de pannenkoek."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'le fromage'</b>?",
                "opties": [
                    "de boter",
                    "de jam",
                    "de kaas",
                    "het ei"
                ],
                "antwoord": 2,
                "uitleg": "'Le fromage' is de kaas."
            },
            {
                "type": "mc",
                "vraag": "Wat is de betekenis van het Franse zelfstandig naamwoord <b>'le cuisinier'</b>?",
                "opties": [
                    "de ober",
                    "de gastheer",
                    "de bakker",
                    "de kok"
                ],
                "antwoord": 3,
                "uitleg": "'Le cuisinier' is de kok."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de Franse uitdrukking <b>'ça me fait plaisir'</b>?",
                "opties": [
                    "dat vind ik leuk / dat doet me plezier",
                    "dat vind ik vreselijk",
                    "dat kost te veel geld",
                    "dat duurt te lang"
                ],
                "antwoord": 0,
                "uitleg": "'Ça me fait plaisir' betekent dat vind ik leuk of dat doet me plezier."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse zelfstandig naamwoord <b>'la bouteille'</b>?",
                "opties": [
                    "het glas",
                    "de fles",
                    "het bord",
                    "de beker"
                ],
                "antwoord": 1,
                "uitleg": "'La bouteille' betekent de fles."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het werkwoord <b>'hésiter'</b>?",
                "opties": [
                    "haasten",
                    "schreeuwen",
                    "twijfelen",
                    "bestellen"
                ],
                "antwoord": 2,
                "uitleg": "'Hésiter' betekent twijfelen of aarzelen."
            },
            {
                "type": "mc",
                "vraag": "Welk Frans woord betekent <b>'de maaltijd'</b>?",
                "opties": [
                    "la cuisine",
                    "la recette",
                    "le travail",
                    "le repas"
                ],
                "antwoord": 3,
                "uitleg": "'Le repas' is de maaltijd."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de vaste uitdrukking <b>'avoir besoin de'</b>?",
                "opties": [
                    "nodig hebben",
                    "dorst hebben",
                    "zin hebben in",
                    "bang zijn voor"
                ],
                "antwoord": 0,
                "uitleg": "'Avoir besoin de' betekent nodig hebben."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'le rêve'</b>?",
                "opties": [
                    "de werkelijkheid",
                    "de droom",
                    "de ruzie",
                    "de smaak"
                ],
                "antwoord": 1,
                "uitleg": "'Le rêve' betekent de droom."
            },
            {
                "type": "mc",
                "vraag": "Wat is de Nederlandse vertaling van de uitdrukking <b>'il faut'</b>?",
                "opties": [
                    "het mag",
                    "het kan",
                    "je moet / het is nodig",
                    "het hoeft niet"
                ],
                "antwoord": 2,
                "uitleg": "'Il faut' betekent je moet of het is nodig."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'le métier'</b>?",
                "opties": [
                    "het salaris",
                    "het diploma",
                    "het bedrijf",
                    "het beroep"
                ],
                "antwoord": 3,
                "uitleg": "'Le métier' betekent het beroep of het vak."
            },
            # 4 Waaronwaar: 2 waar, 2 onwaar
            {
                "type": "waaronwaar",
                "vraag": "Het Franse zelfstandig naamwoord 'le bœuf' betekent 'het rundvlees'.",
                "antwoord": True,
                "uitleg": "Waar! 'Le bœuf' is het Franse woord voor rundvlees."
            },
            {
                "type": "waaronwaar",
                "vraag": "De uitdrukking 'avoir l'air' betekent in het Nederlands 'koude lucht inademen'.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Avoir l'air' betekent eruitzien of schijnen (bijv. il a l'air fatigué)."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Franse woord 'le verre' betekent 'de lepel'.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Le verre' betekent het glas. De lepel is 'la cuillère'."
            },
            {
                "type": "waaronwaar",
                "vraag": "De uitroep 'vas-y!' betekent 'ga je gang!' of 'kom op!'.",
                "antwoord": True,
                "uitleg": "Waar! 'Vas-y!' moedigt iemand aan: ga je gang of doe maar."
            },
            # 2 Invul
            {
                "type": "invul",
                "vraag": "Vul het juiste Franse woord in voor 'eten': 'Nous adorons ____ (eten) au restaurant le samedi.'",
                "antwoord": "manger",
                "uitleg": "Eten is 'manger'."
            },
            {
                "type": "invul",
                "vraag": "Vertaal de uitdrukking tussen haakjes: 'J'ai très (honger), allons manger!' Vul het Franse woord in (faim):",
                "antwoord": "faim",
                "uitleg": "Honger hebben is 'avoir faim'."
            },
            # 2 Open
            {
                "type": "open",
                "vraag": "Noem twee Franse zelfstandige naamwoorden voor vlees- of visproducten uit de woordenlijst van Unité 5.",
                "modelantwoord": "Twee voorbeelden zijn la viande, le bœuf of le poisson.",
                "sleutelwoorden": [
                    "viande/boeuf/bœuf/poisson",
                    "poisson/boeuf/bœuf/viande"
                ],
                "minTreffers": 1,
                "uitleg": "Woorden voor dierlijke etenswaren zijn bijvoorbeeld la viande (vlees), le bœuf (rundvlees) en le poisson (vis)."
            },
            {
                "type": "open",
                "vraag": "Welke twee vaste Franse uitdrukkingen met het werkwoord 'avoir' gebruik je om aan te geven dat je behoefte hebt aan eten of drinken?",
                "modelantwoord": "Dat zijn avoir faim en avoir soif.",
                "sleutelwoorden": [
                    "faim",
                    "soif"
                ],
                "minTreffers": 2,
                "uitleg": "De uitdrukkingen zijn avoir faim (honger hebben) en avoir soif (dorst hebben)."
            }
        ]
    },

    # Toets 2 (ex-h3-frans-u5-v2)
    {
        "id": "ex-h3-frans-u5-v2",
        "hoofdstuk": 5,
        "hoofdstukTitel": "Unité 5 — Au resto!",
        "titel": "Woordenschat 2 · Au resto: Tafelgerei, sauzen & milieu (Vocabulaire E & F)",
        "duurMin": 20,
        "vak": "Frans · HAVO 3 (U5)",
        "icoon": "🧂",
        "vragen": [
            # 12 MC: 3x0, 3x1, 3x2, 3x3
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'le couteau'</b>?",
                "opties": [
                    "het mes",
                    "de vork",
                    "de lepel",
                    "het bord"
                ],
                "antwoord": 0,
                "uitleg": "'Le couteau' is het mes."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'la cuillère'</b>?",
                "opties": [
                    "het glas",
                    "de lepel",
                    "de vork",
                    "het servet"
                ],
                "antwoord": 1,
                "uitleg": "'La cuillère' is de lepel."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'la serviette'</b>?",
                "opties": [
                    "het tafelkleed",
                    "de theedoek",
                    "het servet",
                    "de menukaart"
                ],
                "antwoord": 2,
                "uitleg": "'La serviette' is het servet."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de Franse uitdrukking <b>'le petit boulot'</b>?",
                "opties": [
                    "de kleine rekening",
                    "de korte pauze",
                    "de stageplek",
                    "het bijbaantje"
                ],
                "antwoord": 3,
                "uitleg": "'Le petit boulot' is het bijbaantje."
            },
            {
                "type": "mc",
                "vraag": "Welk Frans woord betekent <b>'de mosterd'</b>?",
                "opties": [
                    "la moutarde",
                    "le beurre",
                    "le poivre",
                    "le sel"
                ],
                "antwoord": 0,
                "uitleg": "'La moutarde' is de mosterd."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'le beurre'</b>?",
                "opties": [
                    "de kaas",
                    "de boter",
                    "het zout",
                    "de olie"
                ],
                "antwoord": 1,
                "uitleg": "'Le beurre' is de boter."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'la pollution'</b>?",
                "opties": [
                    "de bescherming",
                    "de bevolking",
                    "de vervuiling",
                    "de ontbossing"
                ],
                "antwoord": 2,
                "uitleg": "'La pollution' betekent de vervuiling."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het werkwoord <b>'menacer'</b>?",
                "opties": [
                    "beschermen",
                    "redden",
                    "schoonmaken",
                    "bedreigen"
                ],
                "antwoord": 3,
                "uitleg": "'Menacer' betekent bedreigen."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het bijvoeglijk naamwoord <b>'délicieux'</b> (vrouwelijk: délicieuse)?",
                "opties": [
                    "heerlijk",
                    "vies / oneetbaar",
                    "bitter",
                    "te zout"
                ],
                "antwoord": 0,
                "uitleg": "'Délicieux' betekent heerlijk of verrukkelijk."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse werkwoord <b>'râler'</b>?",
                "opties": [
                    "genieten",
                    "klagen / mopperen",
                    "betalen",
                    "vragen"
                ],
                "antwoord": 1,
                "uitleg": "'Râler' betekent klagen of mopperen."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het woord <b>'le pourboire'</b>?",
                "opties": [
                    "de menukaart",
                    "de kassabon",
                    "de fooi",
                    "het voorgerecht"
                ],
                "antwoord": 2,
                "uitleg": "'Le pourboire' is de fooi."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'le sel'</b>?",
                "opties": [
                    "de peper",
                    "de suiker",
                    "de azijn",
                    "het zout"
                ],
                "antwoord": 3,
                "uitleg": "'Le sel' betekent het zout."
            },
            # 4 Waaronwaar: 2 waar, 2 onwaar
            {
                "type": "waaronwaar",
                "vraag": "Het Franse zelfstandig naamwoord 'l'assiette' betekent 'het bord'.",
                "antwoord": True,
                "uitleg": "Waar! 'L'assiette' is het bord (vrouwelijk: une assiette)."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Franse woord 'la mer' betekent 'de berg'.",
                "antwoord": False,
                "uitleg": "Onwaar! 'La mer' is de zee. De berg is 'la montagne'."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het bijvoeglijk naamwoord 'cassé' betekent dat iets kapot of gebroken is.",
                "antwoord": True,
                "uitleg": "Waar! 'Cassé' betekent gebroken of kapot."
            },
            {
                "type": "waaronwaar",
                "vraag": "De uitdrukking 'ce n'est pas grave' betekent 'dat is een groot schandaal'.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Ce n'est pas grave' betekent juist 'het is niet erg / het geeft niet'."
            },
            # 2 Invul
            {
                "type": "invul",
                "vraag": "Vertaal het woord voor 'de vork' in het Frans (met lidwoord, la fourchette):",
                "antwoord": "la fourchette|fourchette",
                "uitleg": "De vork is 'la fourchette'."
            },
            {
                "type": "invul",
                "vraag": "Vertaal het werkwoord tussen haakjes: 'Il faut (beschermen) les océans contre le plastique.' Vul het Franse werkwoord in (protéger):",
                "antwoord": "protéger|proteger",
                "uitleg": "Beschermen is 'protéger'."
            },
            # 2 Open
            {
                "type": "open",
                "vraag": "Noem de Franse benamingen voor de drie belangrijkste basisonderdelen van het bestek (mes, vork en lepel).",
                "modelantwoord": "Dat zijn le couteau, la fourchette en la cuillère.",
                "sleutelwoorden": [
                    "couteau",
                    "fourchette",
                    "cuillère/cuillere"
                ],
                "minTreffers": 2,
                "uitleg": "Het bestek bestaat uit le couteau (mes), la fourchette (vork) en la cuillère (lepel)."
            },
            {
                "type": "open",
                "vraag": "Welke twee smaakmakers vind je vrijwel altijd samen in een stelletje op een Franse eettafel?",
                "modelantwoord": "Dat zijn peper en zout, oftewel le sel en le poivre.",
                "sleutelwoorden": [
                    "sel",
                    "poivre"
                ],
                "minTreffers": 2,
                "uitleg": "Op tafel staan le sel (zout) en le poivre (peper)."
            }
        ]
    },

    # Toets 3 (ex-h3-frans-u5-v3)
    {
        "id": "ex-h3-frans-u5-v3",
        "hoofdstuk": 5,
        "hoofdstukTitel": "Unité 5 — Au resto!",
        "titel": "Woordenschat 3 · Au resto: Gesprekken in het restaurant (Phrases-clés C & G)",
        "duurMin": 20,
        "vak": "Frans · HAVO 3 (U5)",
        "icoon": "🗣️",
        "vragen": [
            # 12 MC: 3x0, 3x1, 3x2, 3x3
            {
                "type": "mc",
                "vraag": "Hoe vraag je aan je tafelgenoot wat hij of zij wil drinken?",
                "opties": [
                    "Qu'est-ce que tu veux boire?",
                    "Qu'est-ce que tu prends comme dessert?",
                    "Où se trouve la cuisine?",
                    "Combien coûte ce repas?"
                ],
                "antwoord": 0,
                "uitleg": "'Qu'est-ce que tu veux boire?' betekent 'Wat wil je drinken?'."
            },
            {
                "type": "mc",
                "vraag": "Wat is de Nederlandse vertaling van: <b>'Je prends le plat du jour'</b>?",
                "opties": [
                    "Ik kook vandaag zelf.",
                    "Ik neem het dagmenu.",
                    "Ik wil alleen een toetje.",
                    "Ik vraag om de rekening."
                ],
                "antwoord": 1,
                "uitleg": "'Le plat du jour' is de dagschotel of het dagmenu."
            },
            {
                "type": "mc",
                "vraag": "Hoe zeg je beleefd dat je graag een glas water wilt?",
                "opties": [
                    "Donne-moi une bière.",
                    "Je n'aime pas l'eau.",
                    "Je voudrais un verre d'eau.",
                    "Une bouteille de vin rouge, s'il vous plaît."
                ],
                "antwoord": 2,
                "uitleg": "'Je voudrais un verre d'eau' betekent 'Ik wil graag een glas water'."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de vraag <b>'Tu prends aussi un dessert?'</b>?",
                "opties": [
                    "Drink je ook koffie?",
                    "Heb je al betaald?",
                    "Wil je nog brood?",
                    "Neem je ook een toetje?"
                ],
                "antwoord": 3,
                "uitleg": "'Un dessert' is een toetje of nagerecht."
            },
            {
                "type": "mc",
                "vraag": "Wat zeg je als je nog niet hebt gekozen: <b>'Je ne sais pas encore'</b>?",
                "opties": [
                    "Ik weet het nog niet.",
                    "Ik heb geen honger.",
                    "Ik vind het niet lekker.",
                    "Ik wil niets bestellen."
                ],
                "antwoord": 0,
                "uitleg": "'Je ne sais pas encore' betekent 'Ik weet het nog niet'."
            },
            {
                "type": "mc",
                "vraag": "Hoe vraag je of er noten in een gerecht verwerkt zijn?",
                "opties": [
                    "Ce plat est très salé?",
                    "Il y a des noix dans ce plat?",
                    "Vous avez de la viande bio?",
                    "C'est un plat végétarien?"
                ],
                "antwoord": 1,
                "uitleg": "'Il y a des noix dans ce plat?' vraagt naar noten in het eten."
            },
            {
                "type": "mc",
                "vraag": "Hoe meld je aan de bediening dat je frietjes koud zijn?",
                "opties": [
                    "Mes frites sont trop chaudes.",
                    "Il n'y a pas assez de sel.",
                    "Mes frites sont froides.",
                    "Je n'aime pas les frites."
                ],
                "antwoord": 2,
                "uitleg": "'Mes frites sont froides' betekent 'Mijn frietjes zijn koud'."
            },
            {
                "type": "mc",
                "vraag": "Wat zeg je als de ober een verkeerd gerecht brengt: <b>'Excusez-moi, il y a une erreur'</b>?",
                "opties": [
                    "Pardon, ik wil nu vertrekken.",
                    "Pardon, mag ik de menukaart zien?",
                    "Pardon, waar is het toilet?",
                    "Pardon, er is een foutje / vergissing gemaakt."
                ],
                "antwoord": 3,
                "uitleg": "'Il y a une erreur' betekent er is een foutje gemaakt."
            },
            {
                "type": "mc",
                "vraag": "Hoe vraag je om mayonaise in een bistro?",
                "opties": [
                    "Je peux avoir de la mayonnaise?",
                    "Donnez-moi du ketchup.",
                    "Où est la moutarde?",
                    "Je n'aime pas la sauce."
                ],
                "antwoord": 0,
                "uitleg": "'Je peux avoir de la mayonnaise?' is de correcte beleefde vraag."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de zin <b>'Je n'ai pas de couteau'</b>?",
                "opties": [
                    "Ik wil geen lepel.",
                    "Ik heb geen mes.",
                    "Mijn vork is vies.",
                    "Ik heb geen servet."
                ],
                "antwoord": 1,
                "uitleg": "'Je n'ai pas de couteau' betekent 'Ik heb geen mes'."
            },
            {
                "type": "mc",
                "vraag": "Hoe vraag je om gratis kraanwater aan tafel in Frankrijk?",
                "opties": [
                    "Une bouteille de soda, s'il vous plaît.",
                    "Un coca avec des glaçons.",
                    "Une carafe d'eau, s'il vous plaît.",
                    "Un café noir sans sucre."
                ],
                "antwoord": 2,
                "uitleg": "'Une carafe d'eau, s'il vous plaît' levert een karaf gratis kraanwater op."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het voorstel <b>'Alors, on commande?'</b>?",
                "opties": [
                    "Zullen we nu betalen?",
                    "Gaan we naar huis?",
                    "Zullen we een toetje nemen?",
                    "Zullen we bestellen?"
                ],
                "antwoord": 3,
                "uitleg": "'Alors, on commande?' betekent 'Zullen we bestellen?'."
            },
            # 4 Waaronwaar: 2 waar, 2 onwaar
            {
                "type": "waaronwaar",
                "vraag": "De zin 'Vous avez encore du pain?' betekent 'Wilt u geen brood meer?'.",
                "antwoord": False,
                "uitleg": "Onwaar! Het betekent 'Heeft u nog brood?' (encore = nog)."
            },
            {
                "type": "waaronwaar",
                "vraag": "In de zin 'C'est le poulet aux olives' betekent 'le poulet' kip.",
                "antwoord": True,
                "uitleg": "Waar! 'Le poulet' is kip."
            },
            {
                "type": "waaronwaar",
                "vraag": "Met de uitroep 'Oui, j'ai faim!' geef je aan dat je erg veel dorst hebt.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Avoir faim' is honger hebben. Dorst hebben is 'avoir soif'."
            },
            {
                "type": "waaronwaar",
                "vraag": "In Frankrijk is een 'carafe d'eau' in een eetgelegenheid gebruikelijk en kosteloos.",
                "antwoord": True,
                "uitleg": "Waar! Een karaf kraanwater (une carafe d'eau) wordt kosteloos geserveerd."
            },
            # 2 Invul
            {
                "type": "invul",
                "vraag": "Vul het ontbrekende woord in voor 'fout/vergissing': 'Excusez-moi, il y a une ____.' (erreur)",
                "antwoord": "erreur",
                "uitleg": "Een foutje = 'une erreur'."
            },
            {
                "type": "invul",
                "vraag": "Vertaal het woord tussen haakjes: 'Je voudrais une carafe (water), s'il vous plaît.' Vul het Franse woord in (d'eau):",
                "antwoord": "d'eau|de l'eau|eau",
                "uitleg": "Een karaf water = 'une carafe d'eau'."
            },
            # 2 Open
            {
                "type": "open",
                "vraag": "Hoe vraag je in het Frans aan de ober of je mayonaise mag krijgen?",
                "modelantwoord": "Je zegt: Je peux avoir de la mayonnaise?",
                "sleutelwoorden": [
                    "peux avoir",
                    "mayonnaise"
                ],
                "minTreffers": 2,
                "uitleg": "De vraag luidt: 'Je peux avoir de la mayonnaise?'."
            },
            {
                "type": "open",
                "vraag": "Noem de Franse zin waarmee je aan de bediening meldt dat jouw frietjes koud geserveerd zijn.",
                "modelantwoord": "Dat zeg je met: Mes frites sont froides.",
                "sleutelwoorden": [
                    "frites",
                    "froides"
                ],
                "minTreffers": 2,
                "uitleg": "Je meldt dit met 'Mes frites sont froides.'."
            }
        ]
    },

    # Toets 4 (ex-h3-frans-u5-v4)
    {
        "id": "ex-h3-frans-u5-v4",
        "hoofdstuk": 5,
        "hoofdstukTitel": "Unité 5 — Au resto!",
        "titel": "Grammatica 4 · Au resto: Het delend lidwoord (du, de la, de l', des & de)",
        "duurMin": 20,
        "vak": "Frans · HAVO 3 (U5)",
        "icoon": "🧀",
        "vragen": [
            # 12 MC: 3x0, 3x1, 3x2, 3x3
            {
                "type": "mc",
                "vraag": "Kies het juiste delend lidwoord: 'Mon père achète ____ (vis, m) au marché.'",
                "opties": [
                    "du",
                    "de la",
                    "des",
                    "de"
                ],
                "antwoord": 0,
                "uitleg": "'Poisson' is mannelijk (le poisson), dus het delend lidwoord is 'du'."
            },
            {
                "type": "mc",
                "vraag": "Kies het juiste delend lidwoord: 'Elle mange ____ (vlees, v) le soir.'",
                "opties": [
                    "du",
                    "de la",
                    "de l'",
                    "des"
                ],
                "antwoord": 1,
                "uitleg": "'Viande' is vrouwelijk (la viande), dus 'de la viande'."
            },
            {
                "type": "mc",
                "vraag": "Kies het juiste delend lidwoord vóór een klinker: 'Je bois ____ (water) pendant le repas.'",
                "opties": [
                    "du",
                    "de la",
                    "de l'",
                    "des"
                ],
                "antwoord": 2,
                "uitleg": "Voor een klinker (eau) gebruik je 'de l''."
            },
            {
                "type": "mc",
                "vraag": "Kies het juiste delend lidwoord voor een meervoudig woord: 'Les enfants mangent ____ (groenten, mv).'",
                "opties": [
                    "du",
                    "de la",
                    "de l'",
                    "des"
                ],
                "antwoord": 3,
                "uitleg": "Bij meervoud (légumes) gebruik je 'des'."
            },
            {
                "type": "mc",
                "vraag": "Wat gebeurt er met het delend lidwoord na een ontkenning: 'Je ne prends pas ____ (suiker)?'",
                "opties": [
                    "de",
                    "du",
                    "de la",
                    "des"
                ],
                "antwoord": 0,
                "uitleg": "Na de ontkenning 'ne ... pas' verandert het delend lidwoord in 'de'."
            },
            {
                "type": "mc",
                "vraag": "Wat gebruik je na een woord van hoeveelheid: 'Elle achète un kilo ____ (appels)?'",
                "opties": [
                    "des",
                    "de",
                    "du",
                    "de la"
                ],
                "antwoord": 1,
                "uitleg": "Na een aanduiding van hoeveelheid (un kilo) gebruik je 'de' of 'd''."
            },
            {
                "type": "mc",
                "vraag": "Welk lidwoord gebruik je na het werkwoord 'adorer': 'J'adore ____ (kaas, m)?'",
                "opties": [
                    "du",
                    "de",
                    "le",
                    "de la"
                ],
                "antwoord": 2,
                "uitleg": "Na waarderingswerkwoorden (aimer, adorer, préférer, détester) gebruik je le, la, l', les."
            },
            {
                "type": "mc",
                "vraag": "Kies de juiste vorm: 'Il boit beaucoup ____ (thee, m) chaque jour.'",
                "opties": [
                    "du",
                    "des",
                    "de la",
                    "de"
                ],
                "antwoord": 3,
                "uitleg": "Na 'beaucoup' gebruik je altijd 'de' (beaucoup de thé)."
            },
            {
                "type": "mc",
                "vraag": "Kies de juiste combinatie: 'C'est une bouteille ____ (mineraalwater).'",
                "opties": [
                    "d'eau minérale",
                    "de l'eau minérale",
                    "du eau minérale",
                    "des eau minérale"
                ],
                "antwoord": 0,
                "uitleg": "Na une bouteille (hoeveelheid) komt d' voor een klinker: 'une bouteille d'eau'."
            },
            {
                "type": "mc",
                "vraag": "Kies het juiste delend lidwoord: 'Tu veux ____ (kaas, m) avec ton pain?'",
                "opties": [
                    "de la",
                    "du",
                    "des",
                    "de"
                ],
                "antwoord": 1,
                "uitleg": "'Fromage' is mannelijk (le fromage), dus 'du fromage'."
            },
            {
                "type": "mc",
                "vraag": "Kies de juiste vorm bij de ontkenning: 'Nous n'avons pas ____ (frietjes, mv).'",
                "opties": [
                    "des",
                    "du",
                    "de",
                    "de la"
                ],
                "antwoord": 2,
                "uitleg": "Na 'ne ... pas' verandert ook een meervoudig delend lidwoord in 'de'."
            },
            {
                "type": "mc",
                "vraag": "Welk lidwoord hoort in deze zin: 'Je déteste ____ (vlees, v)?'",
                "opties": [
                    "de la",
                    "du",
                    "de",
                    "la"
                ],
                "antwoord": 3,
                "uitleg": "Na 'détester' gebruik je het bepaald lidwoord: 'la viande'."
            },
            # 4 Waaronwaar: 2 waar, 2 onwaar
            {
                "type": "waaronwaar",
                "vraag": "In het Frans zeg je 'un verre du vin' als je 'een glas wijn' bedoelt.",
                "antwoord": False,
                "uitleg": "Onwaar! Na een hoeveelheidswoord gebruik je alleen 'de': 'un verre de vin'."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het delend lidwoord voor vrouwelijke enkelvoudige woorden is 'de la'.",
                "antwoord": True,
                "uitleg": "Waar! Bijvoorbeeld 'de la viande' of 'de la confiture'."
            },
            {
                "type": "waaronwaar",
                "vraag": "Na het werkwoord 'préférer' gebruik je altijd het delend lidwoord 'du' of 'de la'.",
                "antwoord": False,
                "uitleg": "Onwaar! Na werkwoorden van voorkeur gebruik je le, la, l', les (bijv. je préfère le thé)."
            },
            {
                "type": "waaronwaar",
                "vraag": "Vóór een zelfstandig naamwoord dat begint met een klinker wordt het delend lidwoord 'de l''.",
                "antwoord": True,
                "uitleg": "Waar! Bijvoorbeeld 'de l'eau' of 'de l'huile'."
            },
            # 2 Invul
            {
                "type": "invul",
                "vraag": "Vul het juiste delend lidwoord in: 'Je voudrais ____ (melk, m) dans mon café.'",
                "antwoord": "du",
                "uitleg": "Melk is mannelijk, dus 'du lait'."
            },
            {
                "type": "invul",
                "vraag": "Vul de juiste vorm in na 'trop': 'Il y a trop ____ (suiker) dans ce gâteau.'",
                "antwoord": "de",
                "uitleg": "Na 'trop' volgt altijd 'de' (trop de sucre)."
            },
            # 2 Open
            {
                "type": "open",
                "vraag": "Noem de vier basisvormen van het Franse delend lidwoord in het enkelvoud en meervoud.",
                "modelantwoord": "De vier vormen zijn du, de la, de l' en des.",
                "sleutelwoorden": [
                    "du",
                    "de la",
                    "de l'",
                    "des"
                ],
                "minTreffers": 3,
                "uitleg": "De vier vormen van het delend lidwoord zijn du, de la, de l' en des."
            },
            {
                "type": "open",
                "vraag": "In welke twee belangrijke grammatica-situaties verandert het delend lidwoord verplicht in alleen de of d'?",
                "modelantwoord": "Dat gebeurt na een ontkenning (zoals ne...pas) en na een aanduiding van hoeveelheid (zoals un verre de, beaucoup de).",
                "sleutelwoorden": [
                    "ontkenning/ontkennende/pas",
                    "hoeveelheid/hoeveelheden/kilo/verre/beaucoup"
                ],
                "minTreffers": 2,
                "uitleg": "Het delend lidwoord wordt de/d' na een ontkenning en na een aanduiding van hoeveelheid."
            }
        ]
    },

    # Toets 5 (ex-h3-frans-u5-v5)
    {
        "id": "ex-h3-frans-u5-v5",
        "hoofdstuk": 5,
        "hoofdstukTitel": "Unité 5 — Au resto!",
        "titel": "Grammatica & Vocabulaire 5 · Au resto: Werkwoord venir & Integrale herhaling",
        "duurMin": 20,
        "vak": "Frans · HAVO 3 (U5)",
        "icoon": "🧀",
        "vragen": [
            # 12 MC: 3x0, 3x1, 3x2, 3x3
            {
                "type": "mc",
                "vraag": "Wat is de vervoeging van het werkwoord 'venir' bij 'je' in de présent?",
                "opties": [
                    "je viens",
                    "je vient",
                    "je venons",
                    "je venez"
                ],
                "antwoord": 0,
                "uitleg": "Bij 'je' is de vorm 'viens' (je viens)."
            },
            {
                "type": "mc",
                "vraag": "Wat is de juiste vorm van 'venir' bij 'vous' in de tegenwoordige tijd?",
                "opties": [
                    "vous vient",
                    "vous venez",
                    "vous venons",
                    "vous viennent"
                ],
                "antwoord": 1,
                "uitleg": "Bij 'vous' is de vorm 'venez' (vous venez)."
            },
            {
                "type": "mc",
                "vraag": "Met welk hulpwerkwoord vormt 'venir' de passé composé?",
                "opties": [
                    "avoir",
                    "faire",
                    "être",
                    "aller"
                ],
                "antwoord": 2,
                "uitleg": "Venir is een werkwoord van beweging en vormt de passé composé met être."
            },
            {
                "type": "mc",
                "vraag": "Kies de juiste vorm van het voltooid deelwoord bij être: 'Elle est ____ (gekomen) hier soir.'",
                "opties": [
                    "venu",
                    "venus",
                    "venues",
                    "venue"
                ],
                "antwoord": 3,
                "uitleg": "'Elle' is vrouwelijk enkelvoud, dus bij être krijgt venu een extra e: 'venue'."
            },
            {
                "type": "mc",
                "vraag": "Kies de juiste vorm van het voltooid deelwoord: 'Mes amis sont ____ (gekomen) en vélo.'",
                "opties": [
                    "venus",
                    "venu",
                    "venue",
                    "venues"
                ],
                "antwoord": 0,
                "uitleg": "'Mes amis' is mannelijk meervoud, dus bij être krijgt venu een extra s: 'venus'."
            },
            {
                "type": "mc",
                "vraag": "Wat is de vervoeging van 'venir' bij 'nous' in de tegenwoordige tijd?",
                "opties": [
                    "nous viens",
                    "nous venons",
                    "nous venez",
                    "nous viennent"
                ],
                "antwoord": 1,
                "uitleg": "Bij 'nous' is de vorm 'venons' (nous venons)."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de Franse uitdrukking <b>'ce n'est pas grave'</b>?",
                "opties": [
                    "het is heel zwaar",
                    "het is verboden",
                    "het is niet erg",
                    "het is niet waar"
                ],
                "antwoord": 2,
                "uitleg": "'Ce n'est pas grave' betekent het is niet erg."
            },
            {
                "type": "mc",
                "vraag": "Welk delend lidwoord hoort in deze zin: 'Je voudrais ____ (boter, m) pour mon pain.'?",
                "opties": [
                    "de la",
                    "des",
                    "de",
                    "du"
                ],
                "antwoord": 3,
                "uitleg": "'Beurre' is mannelijk, dus 'du beurre'."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'le pourboire'</b>?",
                "opties": [
                    "de fooi",
                    "het voorgerecht",
                    "het dessert",
                    "het aperitief"
                ],
                "antwoord": 0,
                "uitleg": "'Le pourboire' is de fooi."
            },
            {
                "type": "mc",
                "vraag": "Wat is de vervoeging van 'venir' bij 'ils' in de présent?",
                "opties": [
                    "ils vient",
                    "ils viennent",
                    "ils venons",
                    "ils venez"
                ],
                "antwoord": 1,
                "uitleg": "Bij 'ils' is de vorm 'viennent' (ils viennent)."
            },
            {
                "type": "mc",
                "vraag": "Kies de juiste vorm van het voltooid deelwoord: 'Mes sœurs sont ____ (gekomen) en train.'",
                "opties": [
                    "venu",
                    "venus",
                    "venues",
                    "venue"
                ],
                "antwoord": 2,
                "uitleg": "'Mes sœurs' is vrouwelijk meervoud, dus bij être krijgt venu -es: 'venues'."
            },
            {
                "type": "mc",
                "vraag": "Wat vraag je als je geen mes hebt gekregen aan tafel?",
                "opties": [
                    "Je n'ai pas de fourchette.",
                    "Je n'ai pas de cuillère.",
                    "Je n'ai pas de serviette.",
                    "Je n'ai pas de couteau."
                ],
                "antwoord": 3,
                "uitleg": "'Je n'ai pas de couteau' betekent dat je geen mes hebt."
            },
            # 4 Waaronwaar: 2 waar, 2 onwaar
            {
                "type": "waaronwaar",
                "vraag": "De vervoeging van het werkwoord 'venir' bij 'il' in de tegenwoordige tijd is 'il vient'.",
                "antwoord": True,
                "uitleg": "Waar! Bij il/elle/on is de persoonsvorm 'vient'."
            },
            {
                "type": "waaronwaar",
                "vraag": "In de zin 'Ils sont venus' eindigt 'venus' op een -s wegens het mannelijk meervoudig onderwerp.",
                "antwoord": True,
                "uitleg": "Waar! Bij être past het voltooid deelwoord zich aan aan het meervoud (accord)."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het werkwoord 'aimer' wordt altijd gevolgd door het delend lidwoord 'du' of 'de la'.",
                "antwoord": False,
                "uitleg": "Onwaar! Na 'aimer' gebruik je het bepaald lidwoord le, la, l', les."
            },
            {
                "type": "waaronwaar",
                "vraag": "De uitdrukking 'avoir soif' betekent dat je graag een warme maaltijd wilt eten.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Avoir soif' betekent dorst hebben (drinken). Honger hebben is 'avoir faim'."
            },
            # 2 Invul
            {
                "type": "invul",
                "vraag": "Vul de persoonsvorm in van 'venir' bij 'tu' in de présent: 'Tu ____ (komt) avec nous ce soir?'",
                "antwoord": "viens",
                "uitleg": "Bij 'tu' is de vorm 'viens' (tu viens)."
            },
            {
                "type": "invul",
                "vraag": "Vul het juiste delend lidwoord in voor 'fromage' (m): 'Il prend toujours ____ fromage à la fin du repas.'",
                "antwoord": "du",
                "uitleg": "Kaas is mannelijk, dus 'du fromage'."
            },
            # 2 Open
            {
                "type": "open",
                "vraag": "Noem de twee persoonsvormen van het werkwoord 'venir' in de tegenwoordige tijd voor de meervoudsvormen 'wij' en 'jullie/u'.",
                "modelantwoord": "Dat zijn venons (nous venons) en venez (vous venez).",
                "sleutelwoorden": [
                    "venons",
                    "venez"
                ],
                "minTreffers": 2,
                "uitleg": "Bij nous is de vorm venons, en bij vous is de vorm venez."
            },
            {
                "type": "open",
                "vraag": "Leg uit welk hulpwerkwoord je gebruikt bij de passé composé van 'venir' en wat het Franse mannelijk enkelvoudige voltooid deelwoord is.",
                "modelantwoord": "Je gebruikt het hulpwerkwoord être en het voltooid deelwoord is venu.",
                "sleutelwoorden": [
                    "être/etre",
                    "venu"
                ],
                "minTreffers": 2,
                "uitleg": "De passé composé van venir wordt gevormd met être en het deelwoord venu (bijv. il est venu)."
            }
        ]
    }
]

def generate():
    for item in ONDERWERPEN:
        fname = f"h{item['hoofdstuk']}_{item['paragraaf'].split('.')[1]}.js"
        fpath = os.path.join(DATA_DIR, fname)
        code = f"/* Onderwerp {item['paragraaf']} — {item['titel']}\n   Grandes Lignes 3 HAVO Unité {item['hoofdstuk']} */\nDURU.register({json.dumps(item, indent=2, ensure_ascii=False)});\n"
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Geschreven onderwerp: {fname}")

    for item in EXAMENS:
        idx = item['id'].replace("ex-h3-frans-u5-v", "")
        fname = f"examen_u5_vocab_{idx}.js"
        fpath = os.path.join(DATA_DIR, fname)
        code = f"/* Proeftoets {item['id']} — {item['titel']}\n   Grandes Lignes 3 HAVO Unité {item['hoofdstuk']} */\nDURU.registerExamen({json.dumps(item, indent=2, ensure_ascii=False)});\n"
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Geschreven examen: {fname}")

if __name__ == "__main__":
    generate()

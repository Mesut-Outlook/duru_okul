#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator voor Frans Unité 7 (À tout prix!)
Boek: Grandes Lignes 3 HAVO, Chapitre 7 (p. 266-270)

Genereert:
- 4 Oefenlessen / Onderwerpen (h7_1.js t/m h7_4.js):
  - 7.1 Vocabulaire A & B: Zakgeld, bijbaantjes, geld & economie
  - 7.2 Vocabulaire E & F: Kleuren, materialen, vormen & eigenschappen
  - 7.3 Phrases-clés C & G: Praten over geld & Voorwerpen omschrijven
  - 7.4 Grammaire D & H: De gebiedende wijs (impératif) & De ontkenningen (ne...pas/plus/jamais/rien)
- 5 Begrippentoetsen / Proeftoetsen (examen_u7_vocab_1.js t/m examen_u7_vocab_5.js)
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "havo3", "frans", "js", "data")

ONDERWERPEN = [
    # H7 §7.1
    {
        "id": "fr-u7-1",
        "hoofdstuk": 7,
        "paragraaf": "7.1",
        "titel": "Vocabulaire A & B · Zakgeld, bijbaantjes, geld & economie",
        "korteUitleg": "De kernwoordenschat van Unité 7 Blok A en B (p. 266): zakgeld, bijbaantjes (oppassen, vakken vullen, hond uitlaten), geld verdienen, sparen en uitgeven.",
        "icoon": "💶",
        "kleur": "oranje",
        "theorie": """
    <h3>7.1 Vocabulaire A & B: Zakgeld, bijbaantjes & sparen</h3>
    <div class="info-box">
      <b>À tout prix!</b> In dit hoofdstuk leer je alles over geldzaken: hoeveel zakgeld krijg je, wat kosten kleren en gadgets, hoe verdien je een centje bij en wat doe je om te sparen? (Blok A en B, p. 266).
    </div>

    <h4>1. Geld en financieel beheer (L'argent et les finances)</h4>
    <table class="vocab-table">
      <thead><tr><th>Frans</th><th>Nederlands</th><th>Toelichting</th></tr></thead>
      <tbody>
        <tr><td><b>l'argent de poche</b> (m)</td><td>het zakgeld</td><td><i>Combien d'argent de poche reçois-tu?</i></td></tr>
        <tr><td><b>gagner de l'argent</b></td><td>geld verdienen</td><td><i>Travailler pour gagner de l'argent.</i></td></tr>
        <tr><td><b>dépenser</b></td><td>uitgeven</td><td><i>Dépenser tout son argent en bonbons.</i></td></tr>
        <tr><td><b>payer</b></td><td>betalen</td><td><i>Payer l'addition au café.</i></td></tr>
        <tr><td><b>faire des économies</b></td><td>sparen</td><td><i>Faire des économies pour un scooter.</i></td></tr>
        <tr><td><b>le portemonnaie</b></td><td>de portemonnee</td><td><i>Mon portemonnaie est vide!</i></td></tr>
        <tr><td><b>la monnaie</b></td><td>het kleingeld / wisselgeld</td><td><i>Vous avez de la monnaie?</i></td></tr>
        <tr><td><b>gratuit(e)</b></td><td>gratis</td><td><i>L'entrée au musée est gratuite.</i></td></tr>
        <tr><td><b>cher, chère</b></td><td>duur</td><td><i>Ce blouson est trop cher.</i></td></tr>
      </tbody>
    </table>

    <h4>2. Bijbaantjes voor jongeren (Les petits boulots, Blok A)</h4>
    <ul>
      <li><b>faire du baby-sitting</b> = oppassen op kinderen</li>
      <li><b>sortir un chien</b> = een hond uitlaten</li>
      <li><b>remplir les rayons</b> = vakken vullen in de supermarkt</li>
      <li><b>faire la vaisselle</b> = de afwas doen</li>
      <li><b>le vendeur, la vendeuse</b> = de verkoper, de verkoopster</li>
      <li><b>le serveur, la serveuse</b> = de ober, de serveerster</li>
      <li><b>la caissière</b> = de caissière (bij de kassa)</li>
    </ul>

    <h4>3. Handige werkwoorden en uitdrukkingen (Blok B)</h4>
    <ul>
      <li><b>acheter</b> = kopen | <b>connaître</b> = kennen | <b>apprendre</b> = leren</li>
      <li><b>demander</b> = vragen | <b>prêter</b> = lenen (aan iemand) | <b>compter</b> = tellen</li>
      <li><b>s'amuser</b> = zich vermaken | <b>profiter</b> = genieten van</li>
      <li><b>l'avenir</b> (m) = de toekomst | <b>le nombre</b> = het aantal | <b>la chose</b> = het ding</li>
      <li><b>utile</b> = nuttig | <b>vide</b> = leeg | <b>généreux, généreuse</b> = gul, vrijgevig</li>
      <li><b>pendant</b> = tijdens | <b>bientôt</b> = binnenkort | <b>dommage</b> = jammer</li>
    </ul>
""",
        "vragen": [
            {
                "type": "mc",
                "vraag": "Wat betekent de Franse uitdrukking <b>'l'argent de poche'</b>?",
                "opties": [
                    "het zakgeld",
                    "de spaarrekening",
                    "het salaris",
                    "de lening"
                ],
                "antwoord": 0,
                "uitleg": "'L'argent de poche' is het zakgeld."
            },
            {
                "type": "mc",
                "vraag": "Welk Frans bijbaantje betekent <b>'vakken vullen'</b> in de supermarkt?",
                "opties": [
                    "faire la vaisselle",
                    "remplir les rayons",
                    "sortir un chien",
                    "faire du baby-sitting"
                ],
                "antwoord": 1,
                "uitleg": "'Remplir les rayons' betekent de schappen / vakken vullen."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de Franse uitdrukking <b>'faire des économies'</b>?",
                "opties": [
                    "veel geld uitgeven",
                    "een lening aanvragen",
                    "sparen / bezuinigen",
                    "economie studeren"
                ],
                "antwoord": 2,
                "uitleg": "'Faire des économies' betekent sparen of geld opzij leggen."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'gratuit'</b> (vrouwelijk: gratuite)?",
                "opties": [
                    "duur",
                    "waardevol",
                    "uitverkocht",
                    "gratis"
                ],
                "antwoord": 3,
                "uitleg": "'Gratuit' betekent gratis."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Franse werkwoord 'dépenser' betekent geld verdienen.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Dépenser' betekent uitgeven. Geld verdienen is 'gagner de l'argent'."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Franse zelfstandig naamwoord 'le portemonnaie' betekent 'de portemonnee'.",
                "antwoord": True,
                "uitleg": "Waar! 'Le portemonnaie' is de portemonnee."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Franse bijvoeglijk naamwoord 'cher' (vrouwelijk: chère) betekent goedkoop.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Cher' betekent duur. Goedkoop is 'bon marché'."
            },
            {
                "type": "invoer",
                "vraag": "Vertaal het werkwoord tussen haakjes: 'Elle doit (betalen) son nouveau smartphone.' Vul het Franse werkwoord in (payer):",
                "antwoord": "payer",
                "uitleg": "Betalen is 'payer'."
            },
            {
                "type": "invoer",
                "vraag": "Vertaal het bijbaantje voor 'oppassen': 'faire du ____.' Vul het ontbrekende woord in (baby-sitting):",
                "antwoord": "baby-sitting|babysitting",
                "uitleg": "Oppassen is 'faire du baby-sitting'."
            },
            {
                "type": "invoer",
                "vraag": "Vertaal het woord voor 'kleingeld' in het Frans (vrouwelijk met lidwoord, la monnaie):",
                "antwoord": "la monnaie|monnaie",
                "uitleg": "Het kleingeld is 'la monnaie'."
            }
        ]
    },

    # H7 §7.2
    {
        "id": "fr-u7-2",
        "hoofdstuk": 7,
        "paragraaf": "7.2",
        "titel": "Vocabulaire E & F · Kleuren, materialen, vormen & eigenschappen",
        "korteUitleg": "Woordenschat van Unité 7 Blok E en F (p. 267): materialen (hout, metaal, glas, plastic), kleuren, vormen (rond, vierkant), gewicht en wetenschappelijke termen rond het brein en experimenten.",
        "icoon": "🎨",
        "kleur": "blauw",
        "theorie": """
    <h3>7.2 Vocabulaire E & F: Kleuren, materialen & vormen</h3>
    <div class="info-box">
      <b>Décrire un objet:</b> Om een voorwerp precies te omschrijven of aan te prijzen, heb je kleuren, materialen en vormen nodig. Deze woorden vind je in Blok E en F (p. 267).
    </div>

    <h4>1. Kleuren (Les couleurs)</h4>
    <p>Let op de spelling van de vrouwelijke vormen van Franse kleuren:</p>
    <ul>
      <li><b>blanc, blanche</b> = wit | <b>noir(e)</b> = zwart | <b>rouge</b> = rood</li>
      <li><b>bleu(e)</b> = blauw | <b>vert(e)</b> = groen | <b>jaune</b> = geel</li>
      <li><b>violet, violette</b> = paars | <b>rose</b> = roze | <b>orange</b> = oranje (onveranderlijk)</li>
    </ul>

    <h4>2. Materialen (Les matières)</h4>
    <p>Voor een materiaal gebruik je altijd het voorzetsel <b>en</b>:</p>
    <table class="vocab-table">
      <thead><tr><th>Frans</th><th>Nederlands</th><th>Voorbeeld</th></tr></thead>
      <tbody>
        <tr><td><b>en bois</b></td><td>van hout</td><td><i>Une table en bois.</i></td></tr>
        <tr><td><b>en métal</b></td><td>van metaal</td><td><i>Une boîte en métal.</i></td></tr>
        <tr><td><b>en tissu</b></td><td>van stof</td><td><i>Un sac en tissu.</i></td></tr>
        <tr><td><b>en plastique</b></td><td>van plastic</td><td><i>Une bouteille en plastique.</i></td></tr>
        <tr><td><b>en verre</b></td><td>van glas</td><td><i>Un verre en verre.</i></td></tr>
      </tbody>
    </table>

    <h4>3. Vormen en eigenschappen (Formes et caractéristiques)</h4>
    <ul>
      <li><b>rond(e)</b> = rond | <b>carré(e)</b> = vierkant</li>
      <li><b>lourd(e)</b> = zwaar | <b>léger, légère</b> = licht</li>
      <li><b>la mémoire</b> = het geheugen | <b>le cerveau</b> = de hersenen</li>
      <li><b>l'expérience</b> (v) = het experiment / de ervaring | <b>la patience</b> = het geduld</li>
      <li><b>la frontière</b> = de grens | <b>la condition</b> = de voorwaarde</li>
      <li><b>scientifique</b> = wetenschappelijk | <b>marcher</b> = werken (van een apparaat) / lopen</li>
    </ul>
""",
        "vragen": [
            {
                "type": "mc",
                "vraag": "Hoe zeg je in het Frans dat een stoel <b>'van hout'</b> is gemaakt?",
                "opties": [
                    "en bois",
                    "en métal",
                    "en verre",
                    "en tissu"
                ],
                "antwoord": 0,
                "uitleg": "'En bois' betekent van hout."
            },
            {
                "type": "mc",
                "vraag": "Wat is de vrouwelijke vorm van de kleur <b>'blanc'</b> (wit)?",
                "opties": [
                    "blance",
                    "blanche",
                    "blanquet",
                    "blanchette"
                ],
                "antwoord": 1,
                "uitleg": "De vrouwelijke vorm van blanc is 'blanche'."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'carré'</b>?",
                "opties": [
                    "rond",
                    "driehoekig",
                    "vierkant",
                    "ovaal"
                ],
                "antwoord": 2,
                "uitleg": "'Carré' (vrouwelijk: carrée) betekent vierkant."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het bijvoeglijk naamwoord <b>'lourd'</b> (vrouwelijk: lourde)?",
                "opties": [
                    "licht",
                    "snel",
                    "duur",
                    "zwaar"
                ],
                "antwoord": 3,
                "uitleg": "'Lourd' betekent zwaar."
            },
            {
                "type": "waaronwaar",
                "vraag": "De uitdrukking 'en plastique' betekent in het Nederlands 'van glas'.",
                "antwoord": False,
                "uitleg": "Onwaar! 'En plastique' is van plastic. Van glas is 'en verre'."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Franse zelfstandig naamwoord 'le cerveau' betekent 'de hersenen'.",
                "antwoord": True,
                "uitleg": "Waar! 'Le cerveau' zijn de hersenen."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Franse woord 'léger' (vrouwelijk: légère) betekent 'loodzwaar'.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Léger' betekent licht van gewicht."
            },
            {
                "type": "invoer",
                "vraag": "Vertaal het materiaal 'van metaal' in het Frans (twee woorden, en métal):",
                "antwoord": "en métal|en metal",
                "uitleg": "Van metaal is 'en métal'."
            },
            {
                "type": "invoer",
                "vraag": "Vertaal de kleur tussen haakjes: 'Elle porte une robe (paars).' Vul de vrouwelijke Franse vorm in (violette):",
                "antwoord": "violette",
                "uitleg": "De vrouwelijke vorm van violet is 'violette'."
            },
            {
                "type": "invoer",
                "vraag": "Vertaal het woord voor 'de vorm rond' (mannelijk enkelvoud, rond):",
                "antwoord": "rond",
                "uitleg": "Rond is in het Frans 'rond'."
            }
        ]
    },

    # H7 §7.3
    {
        "id": "fr-u7-3",
        "hoofdstuk": 7,
        "paragraaf": "7.3",
        "titel": "Phrases-clés C & G · Praten over geld & Voorwerpen omschrijven",
        "korteUitleg": "Gespreksvaardigheid in Unité 7 (p. 268): vertellen over je zakgeld, wat je koopt en spaart (Blok C) én een nieuw voorwerp in detail omschrijven (Blok G).",
        "icoon": "🗣️",
        "kleur": "paars",
        "theorie": """
    <h3>7.3 Phrases-clés C & G: Geldzaken & Voorwerpen omschrijven</h3>
    <div class="info-box">
      <b>Communiquer au quotidien:</b> In deze paragraaf combineren we geldgesprekken (hoeveel krijg je en waaraan geef je het uit?) met het beschrijven van spullen (vorm, materiaal en functie) (p. 268).
    </div>

    <h4>1. Blok C: Parler d'argent (Praten over geld en zakgeld)</h4>
    <table class="vocab-table">
      <thead><tr><th>Nederlands</th><th>Français</th></tr></thead>
      <tbody>
        <tr><td>Krijg jij zakgeld?</td><td><b>Tu as de l'argent de poche?</b></td></tr>
        <tr><td>Ja, ... euro per maand.</td><td><b>Oui, ... euros par mois.</b></td></tr>
        <tr><td>Nee, maar ik heb een bijbaantje.</td><td><b>Non, mais j'ai un petit boulot.</b></td></tr>
        <tr><td>Wat doe je ermee?</td><td><b>Qu'est-ce que tu fais avec?</b></td></tr>
        <tr><td>Ik koop kleren.</td><td><b>J'achète des vêtements.</b></td></tr>
        <tr><td>Ik betaal mijn telefoonabonnement.</td><td><b>Je paye mon abonnement de téléphone.</b></td></tr>
        <tr><td>Ik ga naar de bioscoop.</td><td><b>Je vais au cinéma.</b></td></tr>
        <tr><td>Spaar jij ook?</td><td><b>Tu fais aussi des économies?</b></td></tr>
        <tr><td>Ja, om een scooter te kopen.</td><td><b>Oui, pour m'acheter un scooter.</b></td></tr>
      </tbody>
    </table>

    <h4>2. Blok G: Décrire quelque chose (Een voorwerp omschrijven)</h4>
    <p>Als je een gadget of voorwerp wilt beschrijven aan een vriend:</p>
    <ul>
      <li><b>Tu as un nouveau portable?</b> = Heb je een nieuwe mobiel?</li>
      <li><b>Oui, regarde! Il est super.</b> = Ja, kijk! Hij is super.</li>
      <li><b>Je l'utilise pour...</b> = Ik gebruik het om te...</li>
      <li><b>C'est pratique pour...</b> = Het is handig om te...</li>
      <li><b>C'est un truc en plastique pour...</b> = Het is een plastic dingetje om te...</li>
      <li><b>Tu peux décrire...?</b> = Kun je ... omschrijven?</li>
      <li><b>C'est une sorte de...</b> = Het is een soort van...</li>
      <li><b>C'est rond / C'est bleu / C'est grand.</b> = Het is rond / Het is blauw / Het is groot.</li>
    </ul>
""",
        "vragen": [
            {
                "type": "mc",
                "vraag": "Hoe vraag je in het Frans of iemand zakgeld krijgt?",
                "opties": [
                    "Tu as de l'argent de poche?",
                    "Combien coûte ce pantalon?",
                    "Tu as acheté un nouveau vélo?",
                    "Où se trouve la banque?"
                ],
                "antwoord": 0,
                "uitleg": "'Tu as de l'argent de poche?' vraagt naar zakgeld."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de Franse zin <b>'Je paye mon abonnement de téléphone'</b>?",
                "opties": [
                    "Ik koop een nieuwe telefoon.",
                    "Ik betaal mijn telefoonabonnement.",
                    "Mijn telefoon is kapot gegaan.",
                    "Ik bel mijn ouders op."
                ],
                "antwoord": 1,
                "uitleg": "'Abonnement de téléphone' is het telefoonabonnement."
            },
            {
                "type": "mc",
                "vraag": "Hoe zeg je in het Frans: 'Het is een soort van... '?",
                "opties": [
                    "C'est fait de...",
                    "Je ne sais pas...",
                    "C'est une sorte de...",
                    "Je préfère le..."
                ],
                "antwoord": 2,
                "uitleg": "'C'est une sorte de...' betekent het is een soort van."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de Franse zin <b>'C'est pratique pour voyager'</b>?",
                "opties": [
                    "Het is te zwaar om mee te nemen.",
                    "Het is verboden in het vliegtuig.",
                    "Het kost veel geld op vakantie.",
                    "Het is handig / praktisch om mee te reizen."
                ],
                "antwoord": 3,
                "uitleg": "'Pratique' betekent handig of praktisch."
            },
            {
                "type": "waaronwaar",
                "vraag": "De Franse zin 'J'achète des vêtements' betekent 'ik verkoop oude spullen'.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Acheter des vêtements' betekent kleren kopen."
            },
            {
                "type": "waaronwaar",
                "vraag": "De uitdrukking 'un truc en plastique' betekent 'een plastic dingetje'.",
                "antwoord": True,
                "uitleg": "Waar! 'Un truc' is spreektaal voor een ding of dingetje."
            },
            {
                "type": "waaronwaar",
                "vraag": "De Franse zin 'Tu fais aussi des économies?' vraagt of je een wiskundetoets hebt.",
                "antwoord": False,
                "uitleg": "Onwaar! Het betekent 'Spaar jij ook?' (faire des économies = sparen)."
            },
            {
                "type": "invoer",
                "vraag": "Vertaal het Franse woord voor 'kleren': 'J'achète des ____.' (vêtements)",
                "antwoord": "vêtements|vetements",
                "uitleg": "Kleren zijn 'des vêtements'."
            },
            {
                "type": "invoer",
                "vraag": "Vul het ontbrekende woord in voor 'gebruiken': 'Je l'____ pour écouter de la musique.' (utilise)",
                "antwoord": "utilise",
                "uitleg": "Gebruiken is 'utiliser' ➔ 'je l'utilise'."
            },
            {
                "type": "invoer",
                "vraag": "Vertaal het woord tussen haakjes: 'C'est un objet très (handig) au collège.' (pratique)",
                "antwoord": "pratique",
                "uitleg": "Handig is 'pratique'."
            }
        ]
    },

    # H7 §7.4
    {
        "id": "fr-u7-4",
        "hoofdstuk": 7,
        "paragraaf": "7.4",
        "titel": "Grammaire D & H · De gebiedende wijs & De verschillende ontkenningen",
        "korteUitleg": "De twee grote grammaticablokken van Unité 7 (p. 269): de gebiedende wijs (impératif: tu-, nous- en vous-vorm) én alle Franse ontkenningen (ne...pas, plus, jamais, rien, pas encore) met de/d'.",
        "icoon": "🛑",
        "kleur": "groen",
        "theorie": """
    <h3>7.4 Grammaire D & H: Gebiedende wijs & Ontkenningen</h3>
    <div class="info-box">
      <b>Grammatica Unité 7 (p. 269):</b> Twee absolute kernonderdelen voor HAVO 3: opdrachten en voorstellen doen met de <b>impératif</b> én de volledige waaier van <b>Franse ontkenningen</b> beheersen.
    </div>

    <h4>1. De gebiedende wijs (L'impératif, Grammaire D)</h4>
    <p>Je gebruikt de gebiedende wijs om een opdracht, bevel of advies te geven, of een voorstel te doen. Er is <b>geen onderwerp</b> (geen tu, nous of vous in de zin):</p>
    <ul>
      <li><b>Je richt je tot één bekende persoon (jij-vorm):</b> gebruik de <i>je-vorm</i> van de présent (zonder -s bij -er werkwoorden!).<br>
        ➔ <i>Cherche un petit boulot!</i> (Zoek een baantje!) | <i>Reste à la maison!</i> (Blijf thuis!) | <i>Finis tes devoirs!</i></li>
      <li><b>Je doet een voorstel waar je zelf bij hoort (wij-vorm = 'laten we...'):</b> gebruik de <i>nous-vorm</i>.<br>
        ➔ <i>Allons à la plage!</i> (Laten we naar het strand gaan!) | <i>Faisons des économies!</i></li>
      <li><b>Je richt je tot meerdere personen (jullie) of een beleefde 'u':</b> gebruik de <i>vous-vorm</i>.<br>
        ➔ <i>Cherchez un petit boulot!</i> (Zoek een baantje!) | <i>Regardez cette photo!</i></li>
      <li><b>Uitzondering bij gaan:</b> 'Ga!' tegen één persoon vertaal je met <b>Va!</b> (nooit 'vais'). Bv: <i>Va à l'école!</i></li>
    </ul>

    <h4>2. De Franse ontkenningen (Les négations, Grammaire H)</h4>
    <p>Een Franse ontkenning bestaat uit twee delen: <b>ne / n'</b> vóór de persoonsvorm en het tweede woord direct erachter:</p>
    <table class="vocab-table">
      <thead><tr><th>Ontkenning</th><th>Betekenis</th><th>Voorbeeld</th></tr></thead>
      <tbody>
        <tr><td><b>ne ... pas</b></td><td>niet / geen</td><td><i>Je ne veux pas aller au cinéma.</i></td></tr>
        <tr><td><b>ne ... plus</b></td><td>niet meer</td><td><i>Je n'ai plus d'argent.</i></td></tr>
        <tr><td><b>ne ... jamais</b></td><td>nooit</td><td><i>Il n'est jamais à l'heure.</i></td></tr>
        <tr><td><b>ne ... rien</b></td><td>niets</td><td><i>Je ne comprends rien.</i></td></tr>
        <tr><td><b>ne ... pas encore</b></td><td>nog niet</td><td><i>Le magasin n'est pas encore ouvert.</i></td></tr>
      </tbody>
    </table>

    <div class="formule-box">
      <b>Belangrijke ontkenningsregels:</b><br>
      • Ontkenning van <i>c'est</i> ➔ <b>ce n'est pas</b>.<br>
      • Ontkenning van <i>il y a</i> ➔ <b>il n'y a pas</b> (<i>Il n'y a pas de problème.</i>)<br>
      • <b>De/d' na ontkenning:</b> De lidwoorden <i>un, une, du, de la, de l', des</i> veranderen na een ontkenning altijd in <b>de</b> of <b>d'</b>!<br>
      <i>Tu as du travail? ➔ Non, je n'ai pas <b>de</b> travail.</i>
    </div>
""",
        "vragen": [
            {
                "type": "mc",
                "vraag": "Wat is de juiste gebiedende wijs (impératif) tegen één vriend van het werkwoord 'rester'?",
                "opties": [
                    "Reste à la maison!",
                    "Restes à la maison!",
                    "Restez à la maison!",
                    "Restons à la maison!"
                ],
                "antwoord": 0,
                "uitleg": "Bij regelmatige -er werkwoorden valt de -s weg in de jij-vorm van de impératif: 'Reste!'."
            },
            {
                "type": "mc",
                "vraag": "Hoe vertaal je het voorstel: 'Laten we naar het strand gaan!'?",
                "opties": [
                    "Va à la plage!",
                    "Allons à la plage!",
                    "Allez à la plage!",
                    "Nous allons à la plage!"
                ],
                "antwoord": 1,
                "uitleg": "'Laten we...' druk je uit met de nous-vorm van de impératif: 'Allons!'."
            },
            {
                "type": "mc",
                "vraag": "Welke Franse ontkenning betekent <b>'nooit'</b>?",
                "opties": [
                    "ne ... plus",
                    "ne ... rien",
                    "ne ... jamais",
                    "ne ... pas encore"
                ],
                "antwoord": 2,
                "uitleg": "'Ne ... jamais' betekent nooit."
            },
            {
                "type": "mc",
                "vraag": "Wat gebeurt er met 'du' in de ontkenning: 'Il prend du sucre ➔ Il ne prend pas ____ sucre.'?",
                "opties": [
                    "het blijft 'du'",
                    "het verandert in 'des'",
                    "het wordt 'le'",
                    "het verandert in 'de'"
                ],
                "antwoord": 3,
                "uitleg": "Na een ontkenning verandert een delend lidwoord altijd in 'de' of 'd''."
            },
            {
                "type": "waaronwaar",
                "vraag": "De uitzonderlijke gebiedende wijs van 'aller' tegen één persoon is 'Vais!'.",
                "antwoord": False,
                "uitleg": "Onwaar! De vorm is 'Va!' zonder -s (Va à l'école!)."
            },
            {
                "type": "waaronwaar",
                "vraag": "De ontkenning 'ne ... rien' betekent 'niets' in het Nederlands.",
                "antwoord": True,
                "uitleg": "Waar! 'Je ne sais rien' = ik weet niets."
            },
            {
                "type": "waaronwaar",
                "vraag": "De ontkenning van 'il y a' is 'il n'y a rien pas'.",
                "antwoord": False,
                "uitleg": "Onwaar! De ontkenning van 'il y a' is 'il n'y a pas'."
            },
            {
                "type": "invoer",
                "vraag": "Vertaal de ontkenning voor 'niet meer': 'Je ne veux ____ (niet meer) manger.' (plus)",
                "antwoord": "plus",
                "uitleg": "Niet meer = 'ne ... plus'."
            },
            {
                "type": "invoer",
                "vraag": "Vul de gebiedende wijs in voor één persoon: '____ (Zoek) un petit boulot!' (Cherche)",
                "antwoord": "Cherche|cherche",
                "uitleg": "De jij-vorm van chercher in de impératif is 'Cherche' (zonder -s)."
            },
            {
                "type": "invoer",
                "vraag": "Vertaal de ontkenning voor 'nog niet': 'Le magasin n'est ____ (nog niet) ouvert.' (pas encore)",
                "antwoord": "pas encore",
                "uitleg": "Nog niet is 'ne ... pas encore'."
            }
        ]
    }
]

EXAMENS = [
    # Toets 1 (ex-h3-frans-u7-v1)
    {
        "id": "ex-h3-frans-u7-v1",
        "hoofdstuk": 7,
        "hoofdstukTitel": "Unité 7 — À tout prix!",
        "titel": "Woordenschat 1 · À tout prix: Zakgeld, bijbaantjes & geld (Vocabulaire A & B)",
        "duurMin": 20,
        "vak": "Frans · HAVO 3 (U7)",
        "icoon": "💶",
        "vragen": [
            # 12 MC: 3x0, 3x1, 3x2, 3x3
            {
                "type": "mc",
                "vraag": "Wat is de Nederlandse betekenis van het Franse begrip <b>'l'argent de poche'</b>?",
                "opties": [
                    "het zakgeld",
                    "het kleingeld",
                    "de spaarpot",
                    "het maandsalaris"
                ],
                "antwoord": 0,
                "uitleg": "'L'argent de poche' is het zakgeld."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse werkwoord <b>'dépenser'</b>?",
                "opties": [
                    "sparen",
                    "uitgeven",
                    "verdienen",
                    "lenen"
                ],
                "antwoord": 1,
                "uitleg": "'Dépenser' betekent uitgeven."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de uitdrukking <b>'faire des économies'</b>?",
                "opties": [
                    "een winkel beginnen",
                    "schulden maken",
                    "sparen / bezuinigen",
                    "economie leren"
                ],
                "antwoord": 2,
                "uitleg": "'Faire des économies' betekent sparen."
            },
            {
                "type": "mc",
                "vraag": "Welk Frans woord betekent <b>'het bijbaantje'</b>?",
                "opties": [
                    "le métier",
                    "le travail",
                    "la formation",
                    "le petit boulot"
                ],
                "antwoord": 3,
                "uitleg": "'Le petit boulot' is het bijbaantje."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de Franse bijbaan <b>'faire du baby-sitting'</b>?",
                "opties": [
                    "oppassen op kinderen",
                    "in een café werken",
                    "kranten bezorgen",
                    "honden wassen"
                ],
                "antwoord": 0,
                "uitleg": "'Faire du baby-sitting' betekent oppassen."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'le portemonnaie'</b>?",
                "opties": [
                    "de kassa",
                    "de portemonnee",
                    "het biljet",
                    "de bankpas"
                ],
                "antwoord": 1,
                "uitleg": "'Le portemonnaie' is de portemonnee."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het woord <b>'gratuit'</b> (vrouwelijk: gratuite)?",
                "opties": [
                    "duur",
                    "zeldzaam",
                    "gratis",
                    "kapot"
                ],
                "antwoord": 2,
                "uitleg": "'Gratuit' betekent gratis."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse bijvoeglijk naamwoord <b>'cher'</b> (vrouwelijk: chère)?",
                "opties": [
                    "goedkoop",
                    "leeg",
                    "nuttig",
                    "duur"
                ],
                "antwoord": 3,
                "uitleg": "'Cher' betekent duur."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'la monnaie'</b>?",
                "opties": [
                    "het kleingeld / wisselgeld",
                    "het bankafschrift",
                    "de prijs",
                    "de rekening"
                ],
                "antwoord": 0,
                "uitleg": "'La monnaie' is het kleingeld of wisselgeld."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de Franse uitdrukking <b>'remplir les rayons'</b>?",
                "opties": [
                    "de vloer vegen",
                    "vakken / schappen vullen in de supermarkt",
                    "de kassa bedienen",
                    "klanten begroeten"
                ],
                "antwoord": 1,
                "uitleg": "'Remplir les rayons' is vakken vullen."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse werkwoord <b>'prêter'</b>?",
                "opties": [
                    "kopen",
                    "stelen",
                    "lenen (aan iemand)",
                    "bewaren"
                ],
                "antwoord": 2,
                "uitleg": "'Prêter' betekent uitlenen / lenen aan iemand."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'l'avenir'</b> (m)?",
                "opties": [
                    "het verleden",
                    "het heden",
                    "de jeugd",
                    "de toekomst"
                ],
                "antwoord": 3,
                "uitleg": "'L'avenir' is de toekomst."
            },
            # 4 Waaronwaar: 2 waar, 2 onwaar
            {
                "type": "waaronwaar",
                "vraag": "Het Franse werkwoord 'gagner de l'argent' betekent 'geld verliezen bij een gokspel'.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Gagner de l'argent' betekent geld verdienen of winnen."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Franse woord 'utile' betekent 'nuttig' of 'bruikbaar'.",
                "antwoord": True,
                "uitleg": "Waar! 'Utile' betekent nuttig."
            },
            {
                "type": "waaronwaar",
                "vraag": "De uitdrukking 'sortir un chien' betekent dat je een hond koopt in een dierenwinkel.",
                "antwoord": False,
                "uitleg": "Onwaar! Het betekent een hond uitlaten (naar buiten gaan met de hond)."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Franse woord 'vide' betekent 'leeg' (bijvoorbeeld een lege portemonnee).",
                "antwoord": True,
                "uitleg": "Waar! 'Vide' betekent leeg."
            },
            # 2 Invul
            {
                "type": "invul",
                "vraag": "Vertaal het werkwoord tussen haakjes: 'Elle veut (kopen) une nouvelle veste.' Vul het Franse werkwoord in (acheter):",
                "antwoord": "acheter",
                "uitleg": "Kopen is 'acheter'."
            },
            {
                "type": "invul",
                "vraag": "Vertaal het woord voor 'de ober' in het Frans (met lidwoord, le serveur):",
                "antwoord": "le serveur|serveur",
                "uitleg": "De ober is 'le serveur'."
            },
            # 2 Open
            {
                "type": "open",
                "vraag": "Noem twee Franse werkwoorden uit Blok A die respectievelijk 'uitgeven' en 'betalen' betekenen.",
                "modelantwoord": "Dat zijn de werkwoorden dépenser en payer.",
                "sleutelwoorden": [
                    "dépenser/depenser",
                    "payer"
                ],
                "minTreffers": 2,
                "uitleg": "Uitgeven is dépenser en betalen is payer."
            },
            {
                "type": "open",
                "vraag": "Welke twee populaire bijbaantjes voor scholieren uit Blok A hebben betrekking op dieren en kleine kinderen?",
                "modelantwoord": "Dat zijn sortir un chien (hond uitlaten) en faire du baby-sitting (oppassen).",
                "sleutelwoorden": [
                    "chien/sortir un chien",
                    "baby-sitting/babysitting"
                ],
                "minTreffers": 2,
                "uitleg": "De bijbaantjes zijn sortir un chien en faire du baby-sitting."
            }
        ]
    },

    # Toets 2 (ex-h3-frans-u7-v2)
    {
        "id": "ex-h3-frans-u7-v2",
        "hoofdstuk": 7,
        "hoofdstukTitel": "Unité 7 — À tout prix!",
        "titel": "Woordenschat 2 · À tout prix: Kleuren, materialen & vormen (Vocabulaire E & F)",
        "duurMin": 20,
        "vak": "Frans · HAVO 3 (U7)",
        "icoon": "🎨",
        "vragen": [
            # 12 MC: 3x0, 3x1, 3x2, 3x3
            {
                "type": "mc",
                "vraag": "Welk Frans materiaal betekent <b>'van hout'</b>?",
                "opties": [
                    "en bois",
                    "en verre",
                    "en métal",
                    "en tissu"
                ],
                "antwoord": 0,
                "uitleg": "'En bois' is van hout."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de materiaalomschrijving <b>'en verre'</b>?",
                "opties": [
                    "van plastic",
                    "van glas",
                    "van ijzer",
                    "van leer"
                ],
                "antwoord": 1,
                "uitleg": "'En verre' betekent van glas."
            },
            {
                "type": "mc",
                "vraag": "Wat is de betekenis van de vorm <b>'rond'</b> (vrouwelijk: ronde)?",
                "opties": [
                    "vierkant",
                    "rechthoekig",
                    "rond",
                    "puntig"
                ],
                "antwoord": 2,
                "uitleg": "'Rond' betekent rond."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'la mémoire'</b>?",
                "opties": [
                    "het experiment",
                    "de schuld",
                    "de snelheid",
                    "het geheugen"
                ],
                "antwoord": 3,
                "uitleg": "'La mémoire' is het geheugen."
            },
            {
                "type": "mc",
                "vraag": "Wat is de vrouwelijke vorm van de kleur <b>'blanc'</b>?",
                "opties": [
                    "blanche",
                    "blance",
                    "blancse",
                    "blanque"
                ],
                "antwoord": 0,
                "uitleg": "De vrouwelijke vorm van blanc is 'blanche'."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de Franse kleur <b>'jaune'</b>?",
                "opties": [
                    "groen",
                    "geel",
                    "rood",
                    "blauw"
                ],
                "antwoord": 1,
                "uitleg": "'Jaune' is geel."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'la frontière'</b>?",
                "opties": [
                    "de bergketen",
                    "de zeehaven",
                    "de grens",
                    "de landingsbaan"
                ],
                "antwoord": 2,
                "uitleg": "'La frontière' betekent de grens."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'la patience'</b>?",
                "opties": [
                    "het plezier",
                    "het geluk",
                    "de angst",
                    "het geduld"
                ],
                "antwoord": 3,
                "uitleg": "'La patience' betekent het geduld."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse materiaal <b>'en tissu'</b>?",
                "opties": [
                    "van stof / textiel",
                    "van karton",
                    "van rubber",
                    "van steen"
                ],
                "antwoord": 0,
                "uitleg": "'En tissu' betekent van stof."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het bijvoeglijk naamwoord <b>'léger'</b> (vrouwelijk: légère)?",
                "opties": [
                    "zwaar",
                    "licht van gewicht",
                    "breekbaar",
                    "sterk"
                ],
                "antwoord": 1,
                "uitleg": "'Léger' betekent licht van gewicht."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de vorm <b>'carré'</b>?",
                "opties": [
                    "ovaal",
                    "rond",
                    "vierkant",
                    "driehoekig"
                ],
                "antwoord": 2,
                "uitleg": "'Carré' betekent vierkant."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'la faute'</b>?",
                "opties": [
                    "de beloning",
                    "de vraag",
                    "de kans",
                    "de fout / schuld"
                ],
                "antwoord": 3,
                "uitleg": "'La faute' betekent de fout of de schuld."
            },
            # 4 Waaronwaar: 2 waar, 2 onwaar
            {
                "type": "waaronwaar",
                "vraag": "Het Franse woord 'en métal' betekent dat iets gemaakt is van plastic.",
                "antwoord": False,
                "uitleg": "Onwaar! 'En métal' betekent van metaal."
            },
            {
                "type": "waaronwaar",
                "vraag": "De kleur 'orange' blijft in het Frans in het vrouwelijk meervoud onveranderd (des sacs orange).",
                "antwoord": True,
                "uitleg": "Waar! Kleuren afgeleid van vruchten zoals orange en marron zijn onveranderlijk."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Franse woord 'lourd' betekent dat iets heel erg licht en luchtig is.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Lourd' betekent zwaar."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Franse zelfstandig naamwoord 'l'expérience' (v) kan zowel 'ervaring' als 'experiment' betekenen.",
                "antwoord": True,
                "uitleg": "Waar! 'L'expérience' betekent experiment of levenservaring."
            },
            # 2 Invul
            {
                "type": "invul",
                "vraag": "Vertaal het materiaal tussen haakjes: 'Une bouteille (van plastic).' Vul de twee Franse woorden in (en plastique):",
                "antwoord": "en plastique",
                "uitleg": "Van plastic is 'en plastique'."
            },
            {
                "type": "invul",
                "vraag": "Vertaal de kleur tussen haakjes: 'Elle adore sa nouvelle écharpe (groen).' Vul het Franse woord in (verte):",
                "antwoord": "verte",
                "uitleg": "De vrouwelijke vorm van vert is 'verte'."
            },
            # 2 Open
            {
                "type": "open",
                "vraag": "Noem twee Franse materialen die beginnen met het voorzetsel 'en' (bijvoorbeeld voor hout of metaal).",
                "modelantwoord": "Twee voorbeelden zijn en bois, en métal, en verre of en plastique.",
                "sleutelwoorden": [
                    "en bois/en métal/en metal",
                    "en verre/en plastique/en tissu"
                ],
                "minTreffers": 1,
                "uitleg": "Materialen worden aangeduid met en bois (hout), en métal (metaal), en verre (glas) of en plastique (plastic)."
            },
            {
                "type": "open",
                "vraag": "Geef de twee Franse bijvoeglijk naamwoorden die respectievelijk een ronde en een vierkante vorm aanduiden.",
                "modelantwoord": "Dat zijn de woorden rond en carré.",
                "sleutelwoorden": [
                    "rond",
                    "carré/carre"
                ],
                "minTreffers": 2,
                "uitleg": "Rond is 'rond' en vierkant is 'carré'."
            }
        ]
    },

    # Toets 3 (ex-h3-frans-u7-v3)
    {
        "id": "ex-h3-frans-u7-v3",
        "hoofdstuk": 7,
        "hoofdstukTitel": "Unité 7 — À tout prix!",
        "titel": "Woordenschat 3 · À tout prix: Praten over geld & Voorwerpen omschrijven (Phrases-clés C & G)",
        "duurMin": 20,
        "vak": "Frans · HAVO 3 (U7)",
        "icoon": "🗣️",
        "vragen": [
            # 12 MC: 3x0, 3x1, 3x2, 3x3
            {
                "type": "mc",
                "vraag": "Wat betekent de Franse vraag <b>'Tu as de l'argent de poche?'</b>?",
                "opties": [
                    "Krijg jij zakgeld?",
                    "Heb jij een portemonnee bij je?",
                    "Wil je geld lenen?",
                    "Hoeveel kost deze jas?"
                ],
                "antwoord": 0,
                "uitleg": "'Tu as de l'argent de poche?' vraagt naar zakgeld."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de reactie <b>'Non, mais j'ai un petit boulot'</b>?",
                "opties": [
                    "Nee, ik wil geen geld sparen.",
                    "Nee, maar ik heb een bijbaantje.",
                    "Nee, ik heb geen tijd voor school.",
                    "Nee, ik woon niet meer thuis."
                ],
                "antwoord": 1,
                "uitleg": "'J'ai un petit boulot' betekent ik heb een bijbaantje."
            },
            {
                "type": "mc",
                "vraag": "Wat antwoord je als je spaart voor een scooter: <b>'Oui, pour m'acheter un scooter'</b>?",
                "opties": [
                    "Ja, ik heb gisteren een scooter gehuurd.",
                    "Nee, ik vind scooters te gevaarlijk.",
                    "Ja, om een scooter voor mezelf te kopen.",
                    "Ja, mijn broer heeft een scooter gekocht."
                ],
                "antwoord": 2,
                "uitleg": "'Pour m'acheter un scooter' betekent om een scooter te kopen."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de Franse omschrijving <b>'C'est un truc en plastique'</b>?",
                "opties": [
                    "Het is een houten beeldje.",
                    "Het is een glazen vaas.",
                    "Het is een metalen doos.",
                    "Het is een plastic dingetje."
                ],
                "antwoord": 3,
                "uitleg": "'Un truc en plastique' is een plastic dingetje."
            },
            {
                "type": "mc",
                "vraag": "Hoe vraag je in het Frans aan iemand om een voorwerp nader te omschrijven?",
                "opties": [
                    "Tu peux décrire l'objet?",
                    "Tu peux réparer cet appareil?",
                    "Combien pèse cet objet?",
                    "Où as-tu acheté ce truc?"
                ],
                "antwoord": 0,
                "uitleg": "'Tu peux décrire...?' vraagt om iets te omschrijven."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de zin <b>'Je l'utilise pour écouter de la musique'</b>?",
                "opties": [
                    "Ik koop muziek op internet.",
                    "Ik gebruik het om naar muziek te luisteren.",
                    "Ik speel in een muziekbandje.",
                    "Ik zing graag Franse liedjes."
                ],
                "antwoord": 1,
                "uitleg": "'Je l'utilise pour...' betekent ik gebruik het om..."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de uitdrukking <b>'C'est pratique'</b>?",
                "opties": [
                    "Het is goedkoop.",
                    "Het is ingewikkeld.",
                    "Het is handig / praktisch.",
                    "Het is ouderwets."
                ],
                "antwoord": 2,
                "uitleg": "'C'est pratique' betekent het is handig."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de Franse vraag <b>'Qu'est-ce que tu fais avec?'</b>?",
                "opties": [
                    "Wie gaat er met je mee?",
                    "Waar heb je dat vandaan?",
                    "Hoeveel heeft het gekost?",
                    "Wat doe je ermee?"
                ],
                "antwoord": 3,
                "uitleg": "'Qu'est-ce que tu fais avec?' betekent wat doe je ermee."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de Franse uitdrukking <b>'C'est une sorte de boîtier'</b>?",
                "opties": [
                    "Het is een soort van doosje / hoesje.",
                    "Het is een heel zwaar apparaat.",
                    "Het is een kapotte telefoon.",
                    "Het is een cadeautje voor jou."
                ],
                "antwoord": 0,
                "uitleg": "'C'est une sorte de...' betekent het is een soort van..."
            },
            {
                "type": "mc",
                "vraag": "Hoe zeg je in het Frans dat je zakgeld gebruikt om kleren te kopen?",
                "opties": [
                    "Je vends mes vieux vêtements.",
                    "J'achète des vêtements.",
                    "Je donne mes vêtements à mon frère.",
                    "Je lave mes vêtements le weekend."
                ],
                "antwoord": 1,
                "uitleg": "'J'achète des vêtements' betekent ik koop kleren."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de zin <b>'Regarde! Il est super'</b> als je je nieuwe mobiel toont?",
                "opties": [
                    "Kijk eens! Hij is veel te duur.",
                    "Pas op! Hij valt bijna.",
                    "Kijk! Hij is geweldig / super.",
                    "Wacht even! Hij doet het niet."
                ],
                "antwoord": 2,
                "uitleg": "'Il est super' betekent hij is geweldig."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het antwoord <b>'Oui, ... euros par mois'</b> op de vraag naar zakgeld?",
                "opties": [
                    "Ja, ... euro per week.",
                    "Ja, ... euro per jaar.",
                    "Ja, ... euro per dag.",
                    "Ja, ... euro per maand."
                ],
                "antwoord": 3,
                "uitleg": "'Par mois' betekent per maand."
            },
            # 4 Waaronwaar: 2 waar, 2 onwaar
            {
                "type": "waaronwaar",
                "vraag": "De Franse zin 'Je paye mon abonnement de téléphone' betekent dat je ouders jouw abonnement betalen.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Je paye' betekent dat ik het zelf betaal."
            },
            {
                "type": "waaronwaar",
                "vraag": "Met de zin 'Tu fais aussi des économies?' vraag je of de ander ook spaart.",
                "antwoord": True,
                "uitleg": "Waar! 'Faire des économies' is sparen."
            },
            {
                "type": "waaronwaar",
                "vraag": "De Franse zin 'C'est rond et bleu' beschrijft een vierkant groen voorwerp.",
                "antwoord": False,
                "uitleg": "Onwaar! Het betekent 'het is rond en blauw'."
            },
            {
                "type": "waaronwaar",
                "vraag": "De uitdrukking 'un nouveau portable' betekent een nieuwe mobiele telefoon.",
                "antwoord": True,
                "uitleg": "Waar! 'Le portable' is de mobiele telefoon."
            },
            # 2 Invul
            {
                "type": "invul",
                "vraag": "Vul het ontbrekende woord in voor 'sparen': 'Tu fais aussi des ____?' (économies)",
                "antwoord": "économies|economies",
                "uitleg": "Sparen = 'faire des économies'."
            },
            {
                "type": "invul",
                "vraag": "Vertaal het woord tussen haakjes: 'C'est un truc en plastique (om te) charger mon portable.' (pour)",
                "antwoord": "pour",
                "uitleg": "Om te = 'pour'."
            },
            # 2 Open
            {
                "type": "open",
                "vraag": "Hoe vraag je in het Frans aan een vriend of hij of zij maandelijks zakgeld ontvangt?",
                "modelantwoord": "Dat vraag je met: Tu as de l'argent de poche?",
                "sleutelwoorden": [
                    "argent de poche",
                    "tu as/as-tu"
                ],
                "minTreffers": 1,
                "uitleg": "De vraag luidt: 'Tu as de l'argent de poche?'."
            },
            {
                "type": "open",
                "vraag": "Noem de Franse zin waarmee je aangeeft dat een bepaald voorwerp erg handig is voor op reis.",
                "modelantwoord": "Dat zeg je met: C'est pratique pour voyager.",
                "sleutelwoorden": [
                    "pratique",
                    "pour voyager/voyager"
                ],
                "minTreffers": 2,
                "uitleg": "Je zegt: 'C'est pratique pour voyager.'."
            }
        ]
    },

    # Toets 4 (ex-h3-frans-u7-v4)
    {
        "id": "ex-h3-frans-u7-v4",
        "hoofdstuk": 7,
        "hoofdstukTitel": "Unité 7 — À tout prix!",
        "titel": "Grammatica 4 · À tout prix: De gebiedende wijs (L'impératif)",
        "duurMin": 20,
        "vak": "Frans · HAVO 3 (U7)",
        "icoon": "🛑",
        "vragen": [
            # 12 MC: 3x0, 3x1, 3x2, 3x3
            {
                "type": "mc",
                "vraag": "Wat is de regel voor de jij-vorm van de gebiedende wijs bij regelmatige werkwoorden op -er?",
                "opties": [
                    "De vorm eindigt op -e (de -s van de présens valt weg)",
                    "De vorm eindigt altijd verplicht op -es",
                    "De vorm krijgt een uitroepteken achter de infinitief",
                    "Er moet altijd 'tu' vóór het werkwoord staan"
                ],
                "antwoord": 0,
                "uitleg": "Bij regelmatige -er werkwoorden valt de slot -s weg in de jij-vorm van de impératif (bijv. Cherche! Reste!)."
            },
            {
                "type": "mc",
                "vraag": "Hoe vertaal je het bevel tegen één persoon: 'Blijf thuis!'?",
                "opties": [
                    "Restes à la maison!",
                    "Reste à la maison!",
                    "Restez à la maison!",
                    "Restons à la maison!"
                ],
                "antwoord": 1,
                "uitleg": "De jij-vorm van rester in de impératif is 'Reste' (zonder -s)."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de gebiedende wijs in de nous-vorm: <b>'Faisons des économies!'</b>?",
                "opties": [
                    "Jullie moeten sparen!",
                    "Zij sparen veel geld.",
                    "Laten we sparen!",
                    "Ik wil gaan sparen."
                ],
                "antwoord": 2,
                "uitleg": "De nous-vorm in de impératif vertaal je met 'Laten we...': Laten we sparen!"
            },
            {
                "type": "mc",
                "vraag": "Wat is de uitzonderlijke gebiedende wijs van het werkwoord <b>'aller'</b> tegen één persoon?",
                "opties": [
                    "Vais!",
                    "Allez!",
                    "Allons!",
                    "Va!"
                ],
                "antwoord": 3,
                "uitleg": "Tegen één persoon zeg je 'Va!' (zonder -s), bijvoorbeeld: 'Va à l'école!'."
            },
            {
                "type": "mc",
                "vraag": "Hoe zeg je tegen een groep vrienden (jullie): 'Kijk naar deze foto!'?",
                "opties": [
                    "Regardez cette photo!",
                    "Regarde cette photo!",
                    "Regardons cette photo!",
                    "Vous regardez cette photo!"
                ],
                "antwoord": 0,
                "uitleg": "Tegen een groep gebruik je de vous-vorm: 'Regardez!'."
            },
            {
                "type": "mc",
                "vraag": "Kies de juiste ontkennende gebiedende wijs: 'Koop geen chips!' (tegen meer personen):",
                "opties": [
                    "Ne achetez pas de chips!",
                    "N'achetez pas de chips!",
                    "Ne pas achetez de chips!",
                    "N'achète pas de chips!"
                ],
                "antwoord": 1,
                "uitleg": "Vóór een klinker wordt ne 'n'': 'N'achetez pas de chips!'."
            },
            {
                "type": "mc",
                "vraag": "Wat is de gebiedende wijs van 'finir' tegen één persoon?",
                "opties": [
                    "Fini!",
                    "Finisse!",
                    "Finis!",
                    "Finissez!"
                ],
                "antwoord": 2,
                "uitleg": "Bij werkwoorden op -ir blijft de -s wél behouden: 'Finis tes devoirs!'."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het voorstel <b>'Allons au cinéma ce soir!'</b>?",
                "opties": [
                    "Ga vanavond naar de bioscoop!",
                    "Zij gaan vanavond naar de film.",
                    "Ik wil naar de bioscoop.",
                    "Laten we vanavond naar de bioscoop gaan!"
                ],
                "antwoord": 3,
                "uitleg": "'Allons' is de nous-vorm en betekent 'laten we gaan'."
            },
            {
                "type": "mc",
                "vraag": "Staat er een persoonlijk voornaamwoord (zoals tu, nous, vous) als onderwerp in een zin met een impératif?",
                "opties": [
                    "Nee, bij de gebiedende wijs staat er nooit een onderwerp in de zin",
                    "Ja, altijd verplicht direct vóór het werkwoord",
                    "Alleen bij de nous-vorm",
                    "Alleen in ontkennende zinnen"
                ],
                "antwoord": 0,
                "uitleg": "Bij de gebiedende wijs staat er nooit een onderwerp (geen tu, nous of vous)."
            },
            {
                "type": "mc",
                "vraag": "Hoe zeg je tegen een klasgenoot: 'Luister goed!'?",
                "opties": [
                    "Écoutes bien!",
                    "Écoute bien!",
                    "Écoutez bien!",
                    "Écoutons bien!"
                ],
                "antwoord": 1,
                "uitleg": "Bij écouter (op -er) valt de slot -s weg in de jij-vorm: 'Écoute bien!'."
            },
            {
                "type": "mc",
                "vraag": "Hoe vertaal je: 'Laten we een oplossing zoeken!'?",
                "opties": [
                    "Cherche une solution!",
                    "Cherchez une solution!",
                    "Cherchons une solution!",
                    "Nous cherchons une solution!"
                ],
                "antwoord": 2,
                "uitleg": "'Laten we...' is de nous-vorm: 'Cherchons!'."
            },
            {
                "type": "mc",
                "vraag": "Hoe spreek je een volwassene beleefd toe met een verzoek ('Gaat u zitten!')?",
                "opties": [
                    "Assieds-toi!",
                    "Asseyez-nous!",
                    "Assieds-vous!",
                    "Asseyez-vous!"
                ],
                "antwoord": 3,
                "uitleg": "De beleefde vous-vorm is 'Asseyez-vous!'."
            },
            # 4 Waaronwaar: 2 waar, 2 onwaar
            {
                "type": "waaronwaar",
                "vraag": "In de zin 'Mange ta pomme!' is 'Mange' met opzet zonder -s geschreven.",
                "antwoord": True,
                "uitleg": "Waar! Regelmatige werkwoorden op -er verliezen de -s in de jij-vorm van de impératif."
            },
            {
                "type": "waaronwaar",
                "vraag": "De zin 'Allons à la plage' is een bevel dat uitsluitend gericht is aan één vreemde volwassene.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Allons' is de nous-vorm (een voorstel: 'Laten we naar het strand gaan')."
            },
            {
                "type": "waaronwaar",
                "vraag": "De gebiedende wijs van 'aller' tegen één kind is 'Va à ta chambre!'.",
                "antwoord": True,
                "uitleg": "Waar! 'Va' is de onregelmatige vorm zonder -s."
            },
            {
                "type": "waaronwaar",
                "vraag": "Bij de gebiedende wijs schrijf je altijd 'Tu cherche un travail!' met het woord 'tu' ervoor.",
                "antwoord": False,
                "uitleg": "Onwaar! In een gebiedende wijs staat het onderwerp tu nooit in de zin."
            },
            # 2 Invul
            {
                "type": "invul",
                "vraag": "Vul de gebiedende wijs in van 'parler' tegen één vriend: '____ (Praat) français!' (Parle)",
                "antwoord": "Parle|parle",
                "uitleg": "Bij -er werkwoorden valt de -s weg: 'Parle'."
            },
            {
                "type": "invul",
                "vraag": "Vul de vorm van 'laten we' in voor 'partir': '____ (Laten we vertrekken) maintenant!' (Partons)",
                "antwoord": "Partons|partons",
                "uitleg": "De nous-vorm is 'Partons'."
            },
            # 2 Open
            {
                "type": "open",
                "vraag": "Aan welke drie grammaticale personen kun je in het Frans een gebiedende wijs (impératif) richten?",
                "modelantwoord": "Aan de jij-vorm (tu), de wij-vorm (nous voor 'laten we') en de jullie/u-vorm (vous).",
                "sleutelwoorden": [
                    "tu/jij",
                    "nous/wij",
                    "vous/jullie/u"
                ],
                "minTreffers": 2,
                "uitleg": "De impératif bestaat voor tu (jij), nous (laten we) en vous (jullie / u)."
            },
            {
                "type": "open",
                "vraag": "Welke bijzondere spellingsregel geldt voor regelmatige Franse werkwoorden op -er in de jij-vorm van de gebiedende wijs?",
                "modelantwoord": "Bij de jij-vorm valt de eindletter -s van de tegenwoordige tijd weg.",
                "sleutelwoorden": [
                    "eindletter/letter/slotletter",
                    "s/-s",
                    "wegvalt/verdwijnt/weg"
                ],
                "minTreffers": 2,
                "uitleg": "In de jij-vorm van een werkwoord op -er valt de slot -s weg (bijv. Chante!, Regarde!)."
            }
        ]
    },

    # Toets 5 (ex-h3-frans-u7-v5)
    {
        "id": "ex-h3-frans-u7-v5",
        "hoofdstuk": 7,
        "hoofdstukTitel": "Unité 7 — À tout prix!",
        "titel": "Grammatica & Woordenschat 5 · À tout prix: Ontkenningen & Integrale toets U7",
        "duurMin": 20,
        "vak": "Frans · HAVO 3 (U7)",
        "icoon": "🛑",
        "vragen": [
            # 12 MC: 3x0, 3x1, 3x2, 3x3
            {
                "type": "mc",
                "vraag": "Welke Franse ontkenning betekent <b>'niets'</b>?",
                "opties": [
                    "ne ... rien",
                    "ne ... plus",
                    "ne ... jamais",
                    "ne ... pas encore"
                ],
                "antwoord": 0,
                "uitleg": "'Ne ... rien' betekent niets (bijv. je ne comprends rien)."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de ontkenning <b>'ne ... plus'</b> in het Nederlands?",
                "opties": [
                    "nooit meer",
                    "niet meer",
                    "nog niet",
                    "helemaal niets"
                ],
                "antwoord": 1,
                "uitleg": "'Ne ... plus' betekent niet meer."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de Franse ontkenning <b>'ne ... pas encore'</b>?",
                "opties": [
                    "nooit",
                    "niet meer",
                    "nog niet",
                    "nergens"
                ],
                "antwoord": 2,
                "uitleg": "'Ne ... pas encore' betekent nog niet."
            },
            {
                "type": "mc",
                "vraag": "Wat is de ontkenning van de Franse uitdrukking <b>'il y a'</b>?",
                "opties": [
                    "il y a pas",
                    "il ne y a pas",
                    "il n'y pas",
                    "il n'y a pas"
                ],
                "antwoord": 3,
                "uitleg": "De ontkenning van il y a is 'il n'y a pas'."
            },
            {
                "type": "mc",
                "vraag": "Wat gebeurt er met 'des' in: 'J'ai des bonbons ➔ Je n'ai pas ____ bonbons.'?",
                "opties": [
                    "de",
                    "des",
                    "du",
                    "les"
                ],
                "antwoord": 0,
                "uitleg": "Na een ontkenning verandert 'des' in 'de' (pas de bonbons)."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de Franse zin <b>'Je n'ai jamais été en France'</b>?",
                "opties": [
                    "Ik wil niet meer naar Frankrijk.",
                    "Ik ben nog nooit in Frankrijk geweest.",
                    "Ik ga binnenkort naar Frankrijk.",
                    "Ik woon al jaren in Frankrijk."
                ],
                "antwoord": 1,
                "uitleg": "'Ne ... jamais' betekent nooit."
            },
            {
                "type": "mc",
                "vraag": "Kies de juiste ontkenning voor 'nog niet': 'Elle ____ (is nog niet) partie.'",
                "opties": [
                    "n'est plus",
                    "n'est jamais",
                    "n'est pas encore",
                    "n'est rien"
                ],
                "antwoord": 2,
                "uitleg": "'N'est pas encore' betekent is nog niet."
            },
            {
                "type": "mc",
                "vraag": "Wat is de juiste ontkenning van <b>'c'est'</b>?",
                "opties": [
                    "c'est pas",
                    "ce pas est",
                    "ce n'est rien",
                    "ce n'est pas"
                ],
                "antwoord": 3,
                "uitleg": "De ontkenning van c'est is 'ce n'est pas'."
            },
            {
                "type": "mc",
                "vraag": "Kies de juiste vorm na de ontkenning: 'Non, je n'ai pas ____ (geld).'",
                "opties": [
                    "d'argent",
                    "de l'argent",
                    "du argent",
                    "des argent"
                ],
                "antwoord": 0,
                "uitleg": "Voor een klinker (argent) wordt 'de' verplicht 'd'': 'pas d'argent'."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de zin <b>'Il n'y a pas de réduction'</b>?",
                "opties": [
                    "Er is veel korting.",
                    "Er is geen korting.",
                    "De korting geldt morgen.",
                    "Waar is de korting?"
                ],
                "antwoord": 1,
                "uitleg": "'Il n'y a pas de réduction' betekent er is geen korting."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'le casque'</b>?",
                "opties": [
                    "de microfoon",
                    "het computerscherm",
                    "de koptelefoon",
                    "het hoesje"
                ],
                "antwoord": 2,
                "uitleg": "'Le casque' is de koptelefoon."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de uitroep <b>'Dommage!'</b>?",
                "opties": [
                    "Gefeliciteerd!",
                    "Tot ziens!",
                    "Alsjeblieft!",
                    "Jammer!"
                ],
                "antwoord": 3,
                "uitleg": "'Dommage!' betekent jammer."
            },
            # 4 Waaronwaar: 2 waar, 2 onwaar
            {
                "type": "waaronwaar",
                "vraag": "In het Frans plaats je 'ne' vóór de persoonsvorm en 'pas' direct achter de persoonsvorm.",
                "antwoord": True,
                "uitleg": "Waar! De twee delen van de ontkenning omarmen het vervoegde werkwoord."
            },
            {
                "type": "waaronwaar",
                "vraag": "De ontkenning 'ne ... jamais' betekent in het Nederlands 'altijd'.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Ne ... jamais' betekent nooit. Altijd is 'toujours'."
            },
            {
                "type": "waaronwaar",
                "vraag": "Na een ontkenning verandert het lidwoord 'un' in 'de' of 'd''.",
                "antwoord": True,
                "uitleg": "Waar! Bv. 'J'ai un chien ➔ Je n'ai pas de chien'."
            },
            {
                "type": "waaronwaar",
                "vraag": "De Franse zin 'Je ne comprends rien' betekent dat je alles perfect begrijpt.",
                "antwoord": False,
                "uitleg": "Onwaar! Het betekent 'ik begrijp er niets van' (ne ... rien = niets)."
            },
            # 2 Invul
            {
                "type": "invul",
                "vraag": "Vul de juiste ontkenning in voor 'niets': 'Il ne dit ____ (niets) pendant le cours.' (rien)",
                "antwoord": "rien",
                "uitleg": "Niets = 'ne ... rien'."
            },
            {
                "type": "invul",
                "vraag": "Vul de juiste vorm in na de ontkenning: 'Nous n'avons pas ____ (tijd) aujourd'hui.' (de temps)",
                "antwoord": "de temps|de",
                "uitleg": "Na de ontkenning volgt 'de': 'pas de temps'."
            },
            # 2 Open
            {
                "type": "open",
                "vraag": "Noem de twee Franse ontkenningswoorden die samen 'niet meer' en 'nooit' betekenen (elk gecombineerd met ne).",
                "modelantwoord": "Dat zijn plus (voor niet meer) en jamais (voor nooit).",
                "sleutelwoorden": [
                    "plus",
                    "jamais"
                ],
                "minTreffers": 2,
                "uitleg": "De ontkenningen zijn ne...plus (niet meer) en ne...jamais (nooit)."
            },
            {
                "type": "open",
                "vraag": "Noem het Franse woordje dat onbepaalde lidwoorden vervangt na een ontkenning zoals 'pas'.",
                "modelantwoord": "Dat is het woordje de (of d' voor een klinker).",
                "sleutelwoorden": [
                    "de",
                    "d'"
                ],
                "minTreffers": 1,
                "uitleg": "In een ontkenning veranderen onbepaalde lidwoorden in de of d'."
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
        idx = item['id'].replace("ex-h3-frans-u7-v", "")
        fname = f"examen_u7_vocab_{idx}.js"
        fpath = os.path.join(DATA_DIR, fname)
        code = f"/* Proeftoets {item['id']} — {item['titel']}\n   Grandes Lignes 3 HAVO Unité {item['hoofdstuk']} */\nDURU.registerExamen({json.dumps(item, indent=2, ensure_ascii=False)});\n"
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Geschreven examen: {fname}")

if __name__ == "__main__":
    generate()

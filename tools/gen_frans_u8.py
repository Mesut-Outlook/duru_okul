#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator script for Frans Unité 8 (Le pont & Examentraining).
Grandes Lignes 3 HAVO Unité 8.
Produces:
- 4 Onderwerpen (h8_1.js .. h8_4.js) with rich theory (>=1500 chars) and 10 questions each (mc, waaronwaar, invoer)
- 5 Begrippentoetsen (examen_u8_vocab_1.js .. examen_u8_vocab_5.js) with 20 questions each (12 MC, 4 WW, 2 Invul, 2 Open)
"""

import json
import os
import subprocess

OUT_DIR = "havo3/frans/js/data"

onderwerpen = [
    {
        "file": "h8_1.js",
        "id": "fr-u8-1",
        "titel": "Herhaling Ch 1–5: Eten, Vrije tijd & Venir / Partitief",
        "hoofdstuk": 8,
        "theorie": """### Unité 8 §8.1 — Herhaling Chapitres 1 à 5: Eten, Vrije tijd & Werkwoorden

In **Unité 8 (Le pont)** bouw je de brug tussen alle opgedane kennis van de afgelopen hoofdstukken. Het eerste deel van deze grote herhaling richt zich op de essentiële woordenschat en grammatica van **Chapitre 1 tot en met 5**: het dagelijks leven, hobby's, restaurantbezoek, eten en drinken, en centrale werkwoordsvormen.

#### 1. Vocabulaire: Restaurant, Eten & Tafelgerei (Ch 1–5)
Een belangrijk onderdeel van de brugopdrachten is het herkennen en toepassen van Franse termen rondom maaltijden en restaurantbezoek:
- **Les repas & les lieux**: *le restaurant* (het restaurant), *le plat du jour* (de dagschotel), *l'entrée* (het voorgerecht), *le dessert* (het toetje), *le cuisinier* (de kok), *l'équipe* (het team).
- **Les couverts & la table**: *le couteau* (het mes), *la fourchette* (de vork), *la cuillère* (de lepel), *l'assiette* (het bord), *le verre* (het glas), *la serviette* (het servet).
- **La nourriture & les boissons**: *le bœuf* (rundvlees), *le poulet* (kip), *le poisson* (vis), *la viande* (vlees), *les légumes* (groenten), *les frites* (friet), *l'eau* (water), *le jus d'orange* (sinaasappelsap), *le lait* (melk), *le fromage* (kaas).
- **Vaste uitdrukkingen**: *avoir faim* (honger hebben), *avoir soif* (dorst hebben), *avoir envie de* (zin hebben in), *être au régime* (op dieet zijn).

#### 2. Grammatica: Het Delend Lidwoord (L'article partitif)
Wanneer je een onbepaalde hoeveelheid aanduidt van iets dat je niet kunt tellen (zoals eten of drinken), gebruik je het **delend lidwoord**:
- Mannelijk enkelvoud: **du** (*du pain*, *du fromage*, *du poisson*).
- Vrouwelijk enkelvoud: **de la** (*de la viande*, *de la salade*, *de la confiture*).
- Woord beginnend met klinker of stomme h: **de l'** (*de l'eau*, *de l'huile*).
- Meervoud: **des** (*des frites*, *des légumes*, *des fruits*).

**Cruciale uitzonderingen:**
1. Na een **ontkenning** verandert het delend lidwoord altijd in **de** of **d'**: *Je ne mange pas **de** viande*, *Il ne boit pas **d'**eau*.
2. Na een **aanduiding van hoeveelheid** (*beaucoup*, *un kilo*, *un litre*, *une bouteille*, *un peu*, *trop*) gebruik je altijd alleen **de** of **d'**: *un kilo **de** pommes*, *un verre **d'**eau*, *beaucoup **de** sucre*.
3. Na werkwoorden van waardering zoals *aimer*, *adorer*, *préférer*, *détester* gebruik je het **bepaald lidwoord** (*le, la, l', les*): *J'adore **le** chocolat*, *Je déteste **les** épinards*.

#### 3. Werkwoorden: Venir & Basis Hulpwerkwoorden
Het onregelmatige werkwoord **venir** (komen) is herhaald in de tegenwoordige tijd (*présent*) en verleden tijd (*passé composé*):
- **Présent**: *je viens*, *tu viens*, *il/elle vient*, *nous venons*, *vous venez*, *ils/elles viennent*.
- **Passé composé met être**: *je suis venu(e)*, *tu es venu(e)*, *il est venu*, *elle est venue*, *nous sommes venu(e)s*, *vous êtes venu(e)s*, *ils sont venus*, *elles sont venues*. Let op de verplichte aanpassing van het voltooid deelwoord aan het geslacht en getal van het onderwerp!
- **Overige hulpwerkwoorden**: *avoir* (hebben: j'ai, tu as, il a, nous avons, vous avez, ils ont), *être* (zijn: je suis, tu es, il est, nous sommes, vous êtes, ils sont), *aller* (gaan: je vais, tu vas, il va, nous allons, vous allez, ils vont) en *vouloir* (willen: je veux, tu veux, il veut, nous voulons, vous voulez, ils veulent).""",
        "vragen": [
            {
                "type": "mc",
                "vraag": "Welk delend lidwoord gebruik je in de zin: 'Le matin, je bois ____ café au lait'?",
                "opties": ["du", "de la", "de l'", "des"],
                "antwoord": 0,
                "uitleg": "'Café' is een mannelijk enkelvoudig woord, dus delend lidwoord 'du'."
            },
            {
                "type": "mc",
                "vraag": "Wat gebeurt er met het delend lidwoord na de ontkenning 'ne ... pas'?",
                "opties": ["Het blijft altijd 'du' of 'de la'.", "Het verandert altijd in 'de' of 'd''.", "Het verandert in 'des'.", "Het verdwijnt helemaal zonder vervanging."],
                "antwoord": 1,
                "uitleg": "Na een ontkenning gebruikt het Frans altijd alleen 'de' of 'd''."
            },
            {
                "type": "mc",
                "vraag": "Welke vorm is de juiste voor 'nous' van het werkwoord <b>venir</b> in de présent?",
                "opties": ["nous venez", "nous venions", "nous venons", "nous viennent"],
                "antwoord": 2,
                "uitleg": "De présent-vorm van venir voor nous is 'nous venons'."
            },
            {
                "type": "mc",
                "vraag": "Welk lidwoord hoort na een hoeveelheidswoord zoals 'un kilo': 'Je voudrais un kilo ____ fraises'?",
                "opties": ["des", "du", "les", "de"],
                "antwoord": 3,
                "uitleg": "Na een hoeveelheid (un kilo, un litre) volgt altijd 'de' of 'd''."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het voltooid deelwoord van het werkwoord 'venir' wordt in de passé composé vervoegd met het hulpwerkwoord 'avoir'.",
                "antwoord": False,
                "uitleg": "Onwaar: 'venir' vormt de passé composé altijd met het hulpwerkwoord 'être' (bijv. 'elle est venue')."
            },
            {
                "type": "waaronwaar",
                "vraag": "Na het werkwoord 'adorer' gebruik je het delend lidwoord 'du' of 'de la', niet 'le' of 'la'.",
                "antwoord": False,
                "uitleg": "Onwaar: na werkwoorden van voorkeur/mening (aimer, adorer, détester) gebruik je het bepaald lidwoord (le, la, l', les)."
            },
            {
                "type": "waaronwaar",
                "vraag": "In de zin 'Elles sont venues en bus' krijgt het voltooid deelwoord 'venues' een extra -e en -s omdat het onderwerp vrouwelijk meervoud is.",
                "antwoord": True,
                "uitleg": "Waar: bij être past het voltooid deelwoord zich aan aan het geslacht en getal van het onderwerp."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Franse woord 'la fourchette' betekent 'de lepel'.",
                "antwoord": False,
                "uitleg": "Onwaar: 'la fourchette' is de vork, 'la cuillère' is de lepel."
            },
            {
                "type": "invoer",
                "vraag": "Vertaal het Franse woord voor 'het bord' naar het Nederlands (inclusief lidwoord).",
                "antwoord": "het bord",
                "uitleg": "'L'assiette' betekent het bord."
            },
            {
                "type": "invoer",
                "vraag": "Vertaal de Franse uitdrukking voor 'honger hebben': 'avoir ____'.",
                "antwoord": "faim",
                "uitleg": "'Avoir faim' betekent honger hebben."
            }
        ]
    },

    {
        "file": "h8_2.js",
        "id": "fr-u8-2",
        "titel": "Herhaling Ch 1–6: Karakter, Dagindeling & Vergelijkingen / Tijden",
        "hoofdstuk": 8,
        "theorie": """### Unité 8 §8.2 — Herhaling Chapitres 1 à 6: Karakter, Dagindeling, Tijden & Vergelijkingen

In dit onderdeel van de brugmodule herhaal je de woordenschat over identiteit, uiterlijk, school en gewoontes, gecombineerd met de drie hoofdtijden van de werkwoorden en de regels voor de trappen van vergelijking.

#### 1. Vocabulaire: Identiteit, Karakter & Dagritme (Ch 6)
- **Le caractère & la personnalité**: *courageux* (moedig), *drôle* / *marrant* (grappig), *paresseux* (lui), *énervant* (irritant), *calme* (rustig), *timide* (verlegen), *sympa* (aardig), *la confiance* (het vertrouwen).
- **Le rythme de la journée**: *se lever* (opstaan: *je me lève*), *s'habiller* (zich aankleden: *je m'habille*), *partir* (vertrekken), *arriver en retard* (te laat aankomen), *se coucher* (naar bed gaan).
- **L'école & les études**: *le bac* (het eindexamen), *les études* (de studie), *la récré* (de pauze), *la note* (het cijfer), *poser une question* (een vraag stellen), *rater un examen* (zakken voor een examen).

#### 2. Grammatica: De Drie Hoofdtijden (Présent, Passé Composé & Futur Proche)
1. **Le présent (tegenwoordige tijd)**:
   - Regelmatige werkwoorden op **-er** (*donner*: je donne, tu donnes, il donne, nous donnons, vous donnez, ils donnent).
   - Regelmatige werkwoorden op **-ir** (*finir*: je finis, tu finis, il finit, nous finissons, vous finissez, ils finissent).
   - Regelmatige werkwoorden op **-re** (*vendre*: je vends, tu vends, il vend, nous vendons, vous vendez, ils vendent).
2. **Le passé composé (voltooid verleden tijd)**:
   - Hulpwerkwoord *avoir* of *être* + voltooid deelwoord (*participe passé*).
   - Regelmatige uitgangen: -er wordt **-é** (*parlé*), -ir wordt **-i** (*fini*), -re wordt **-u** (*vendu*).
   - Onregelmatige deelwoorden: *eu* (avoir), *été* (être), *fait* (faire), *pris* (prendre), *vu* (voir), *bu* (boire).
3. **Le futur proche (nabije toekomst)**:
   - Vorm van **aller** in de présent + **hele werkwoord (infinitief)**: *Je vais regarder un film*, *Nous allons partir demain*.

#### 3. De Trappen van Vergelijking (Les Comparaisons)
Om personen of zaken met elkaar te vergelijken gebruik je:
- **plus ... que** (meer / ...-er dan): *Lucas est plus grand que Pauline.*
- **moins ... que** (minder ... dan): *Emma est moins sportive que son frère.*
- **aussi ... que** (even ... als / net zo ... als): *Arthur est aussi intelligent que son copain.*

**Let op het bijvoeglijk naamwoord:**
Het bijvoeglijk naamwoord tussen *plus/moins/aussi* en *que* past zich altijd aan het onderwerp aan:
- *Emma est plus petit**e** qu'Arthur.*
- *Les filles sont plus grand**es** que les garçons.*

**Uitzondering bij 'goed / beter':**
Het Franse woord voor 'beter dan' (als vergelijking van *bon*) is **meilleur que** (mannelijk) of **meilleure que** (vrouwelijk), nooit *plus bon que*!""",
        "vragen": [
            {
                "type": "mc",
                "vraag": "Hoe vertaal je: 'Emma is net zo sportief als Pauline'?",
                "opties": ["Emma est aussi sportive que Pauline.", "Emma est plus sportive que Pauline.", "Emma est moins sportive que Pauline.", "Emma est meilleure sportive que Pauline."],
                "antwoord": 0,
                "uitleg": "'Even ... als' vertaal je met 'aussi ... que' (met vrouwelijke vorm sportive)."
            },
            {
                "type": "mc",
                "vraag": "Wat is het voltooid deelwoord van het regelmatige werkwoord <b>finir</b>?",
                "opties": ["finé", "fini", "finu", "finit"],
                "antwoord": 1,
                "uitleg": "Werkwoorden op -ir krijgen in de regel een voltooid deelwoord op -i: 'fini'."
            },
            {
                "type": "mc",
                "vraag": "Hoe vorm je de **futur proche** (nabije toekomst) in het Frans?",
                "opties": ["Met een vorm van 'avoir' + voltooid deelwoord.", "Met de stam van het werkwoord + uitgangen.", "Met een vorm van 'aller' + het hele werkwoord (infinitief).", "Met een vorm van 'être' + voltooid deelwoord."],
                "antwoord": 2,
                "uitleg": "De futur proche bestaat uit aller + infinitief (bijv. 'je vais manger')."
            },
            {
                "type": "mc",
                "vraag": "Welke vorm is de juiste vrouwelijke vergelijking voor 'beter dan'?",
                "opties": ["plus bonne que", "mieux que", "meilleur que", "meilleure que"],
                "antwoord": 3,
                "uitleg": "Voor een vrouwelijk onderwerp is 'beter dan' 'meilleure que'."
            },
            {
                "type": "waaronwaar",
                "vraag": "De uitgang van de 'nous'-vorm bij regelmatige werkwoorden op -ir (zoals finir) is '-issons'.",
                "antwoord": True,
                "uitleg": "Waar: finir wordt in de présent 'nous finissons'."
            },
            {
                "type": "waaronwaar",
                "vraag": "In het Frans zeg je 'plus bon que' om aan te geven dat iets beter is dan iets anders.",
                "antwoord": False,
                "uitleg": "Onwaar: 'plus bon que' bestaat niet; je zegt altijd 'meilleur(e) que'."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Franse woord 'rater' (bijvoorbeeld 'rater un examen') betekent 'slagen voor een examen'.",
                "antwoord": False,
                "uitleg": "Onwaar: 'rater' betekent zakken of missen; slagen is 'réussir'."
            },
            {
                "type": "waaronwaar",
                "vraag": "In een vergelijking met 'plus ... que' moet het bijvoeglijk naamwoord overeenkomen in geslacht en getal met het eerste onderwerp.",
                "antwoord": True,
                "uitleg": "Waar: bijv. 'Pauline est plus grand**e** que Lucas'."
            },
            {
                "type": "invoer",
                "vraag": "Vertaal het Franse woord 'paresseux' naar het Nederlands.",
                "antwoord": "lui",
                "uitleg": "'Paresseux' betekent lui (vrouwelijk: paresseuse)."
            },
            {
                "type": "invoer",
                "vraag": "Vul het juiste ontbrekende hulpwerkwoord in voor de futur proche: 'Nous ____ visiter Paris ce week-end.'",
                "antwoord": "allons",
                "uitleg": "De vorm van aller voor nous is 'allons'."
            }
        ]
    },

    {
        "file": "h8_3.js",
        "id": "fr-u8-3",
        "titel": "Herhaling Ch 1–7: Geld, Materialen, Signaalwoorden & Ontkenningen",
        "hoofdstuk": 8,
        "theorie": """### Unité 8 §8.3 — Herhaling Chapitres 1 à 7: Geld, Materialen, Signaalwoorden & Ontkenningen

In de opdrachten 13 tot en met 18 van Unité 8 maak je de stap naar de integrale stof van Chapitres 1 tot en met 7. Hier komen belangrijke thema's samen zoals bezittingen, geld, materialen, signaalwoorden die verbanden leggen in teksten, en de complexe ontkenningen.

#### 1. Vocabulaire: Geld, Werk & Materialen (Ch 7)
- **L'argent & le travail**: *l'argent de poche* (zakgeld), *dépenser* (uitgeven), *économiser* / *garder* (sparen), *le petit boulot* (het bijbaantje), *gagner de l'argent* (geld verdienen), *le prix* (de prijs), *coûter* (kosten).
- **Les matières**: *en bois* (van hout), *en cuir* (van leer), *en fer* / *en métal* (van ijzer/metaal), *en coton* (van katoen), *en plastique* (van plastic), *en verre* (van glas), *en or* (van goud), *en argent* (van zilver).
- **Les formes & caractéristiques**: *rond* (rond), *carré* (vierkant), *lourd* (zwaar), *léger* (licht van gewicht), *pratique* (handig/praktisch).

#### 2. Signaalwoorden (Les Connecteurs / Mots de liaison)
Signaalwoorden zijn essentieel om Franse teksten goed te begrijpen en zelf logisch opgebouwde brieven of mailtjes te schrijven:
- **Reden / Oorzaak**:
  - *car* (want)
  - *parce que* (omdat)
  - *puisque* (aangezien)
- **Gevolg / Conclusie**:
  - *donc* (dus)
  - *alors* (dan / dus)
- **Tegenstelling**:
  - *mais* (maar)
  - *pourtant* (toch / echter)
  - *par contre* (daarentegen)
- **Tijd / Volgorde**:
  - *d'abord* (eerst)
  - *ensuite* / *puis* (vervolgens / daarna)
  - *enfin* (ten slotte)
  - *depuis* (sinds / al ... lang)
- **Voorbeeld & Verduidelijking**:
  - *par exemple* (bijvoorbeeld)
  - *c'est-à-dire* (dat wil zeggen)

#### 3. Grammatica: Uitgebreide Ontkenningen & De Gebiedende Wijs
1. **De ontkenningen**:
   - *ne ... pas* (niet)
   - *ne ... jamais* (nooit)
   - *ne ... rien* (niets)
   - *ne ... personne* (niemand)
   - *ne ... plus* (niet meer)
   - *ne ... pas encore* (nog niet)
   *Let op:* Na een ontkenning verandert het lidwoord *un, une, des* en het delend lidwoord in **de** of **d'**: *Je n'ai pas **de** monnaie* (ik heb geen kleingeld).
2. **De gebiedende wijs (l'impératif)**:
   - Gebruikt om een bevel, advies of instructie te geven.
   - Heeft maar drie personen: **tu**, **nous** en **vous**, en het onderwerp (*tu/nous/vous*) wordt **niet** uitgesproken of geschreven!
   - Belangrijke regel voor -er werkwoorden: in de **tu-vorm vervalt de slotletter -s** (*Regarde!*, *Mange tes légumes!*, *Fais tes devoirs!*).""",
        "vragen": [
            {
                "type": "mc",
                "vraag": "Welk signaalwoord drukt een **tegenstelling** uit?",
                "opties": ["pourtant", "donc", "parce que", "ensuite"],
                "antwoord": 0,
                "uitleg": "'Pourtant' betekent toch of echter en drukt een tegenstelling uit."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de ontkenning <b>'ne ... rien'</b> in het Nederlands?",
                "opties": ["nooit", "niets", "niemand", "niet meer"],
                "antwoord": 1,
                "uitleg": "'Ne ... rien' betekent niets (bijv. 'Je ne sais rien')."
            },
            {
                "type": "mc",
                "vraag": "Hoe zeg je in de gebiedende wijs tegen één vriend: 'Kijk!' (werkwoord regarder)?",
                "opties": ["Regardes !", "Tu regardes !", "Regarde !", "Regardez !"],
                "antwoord": 2,
                "uitleg": "Bij de gebiedende wijs van werkwoorden op -er vervalt de -s in de tu-vorm: 'Regarde !'."
            },
            {
                "type": "mc",
                "vraag": "Welk materiaal hoort bij schoenen of een riem gemaakt van dierenhuid (<b>'en cuir'</b>)?",
                "opties": ["van hout", "van katoen", "van ijzer", "van leer"],
                "antwoord": 3,
                "uitleg": "'En cuir' betekent van leer (bijv. des chaussures en cuir)."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het signaalwoord 'car' betekent 'omdat/want' en geeft een reden aan.",
                "antwoord": True,
                "uitleg": "Waar: 'car' geeft een reden of oorzaak aan."
            },
            {
                "type": "waaronwaar",
                "vraag": "In de zin 'Je n'ai pas de temps' is het woordje 'de' fout en had er 'du' moeten staan.",
                "antwoord": False,
                "uitleg": "Onwaar: na een ontkenning verandert het delend lidwoord altijd in 'de'."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Franse woord 'économiser' betekent 'veel geld uitgeven'.",
                "antwoord": False,
                "uitleg": "Onwaar: 'économiser' betekent sparen of zuinig aandoen; uitgeven is 'dépenser'."
            },
            {
                "type": "waaronwaar",
                "vraag": "De ontkenning 'ne ... personne' betekent 'niemand'.",
                "antwoord": True,
                "uitleg": "Waar: 'Je ne vois personne' betekent ik zie niemand."
            },
            {
                "type": "invoer",
                "vraag": "Vertaal het Franse signaalwoord 'donc' naar het Nederlands.",
                "antwoord": "dus",
                "uitleg": "'Donc' betekent dus."
            },
            {
                "type": "invoer",
                "vraag": "Vertaal de ontkenning voor 'nooit' in combinatie met ne: 'ne ... ____'.",
                "antwoord": "jamais",
                "uitleg": "'Ne ... jamais' betekent nooit."
            }
        ]
    },

    {
        "file": "h8_4.js",
        "id": "fr-u8-4",
        "titel": "DELF A2 Examentraining: Leesstrategieën & Schrijfvaardigheid",
        "hoofdstuk": 8,
        "theorie": """### Unité 8 §8.4 — DELF A2 Examentraining: Leesstrategieën, Schrijfvaardigheid & Cultuur

In het sluitstuk van Grandes Lignes 3 HAVO maak je kennis met de opzet en eisen van het officiële **DELF A2-examen** (Diplôme d'Études en Langue Française), een internationaal erkend certificaat van het Franse Ministerie van Onderwijs. Op dit niveau kun je eenvoudige teksten begrijpen en praktische alledaagse berichten schrijven.

#### 1. Leesvaardigheid & Examenstrategieën (Compréhension des écrits)
Bij leestoetsen op A2-niveau werk je met authentieke Franse documenten: advertenties (*petites annonces*), folders, e-mails, menus en korte artikelen.
- **Oriënterend lezen**: Bekijk eerst de titel, tussenkopjes, afbeeldingen en bron. Bepaal het teksttype: is het een uitnodiging, een advertentie of een nieuwsbericht?
- **Vraag eerst lezen**: Lees altijd eerst de vraag en markeer de **vraagwoorden** (*qui*, *quand*, *où*, *pourquoi*, *comment*, *combien*). Zoek daarna gericht in de tekst naar synoniemen of verwante begrippen.
- **Sleutelwoorden & Signaalwoorden**: Let op woorden die wendingen aangeven, zoals *mais* (maar), *pourtant* (toch) of tijdsbepalingen (*après*, *avant*, *pendant*). Laat je niet van de wijs brengen door moeilijke woorden die niet relevant zijn voor het beantwoorden van de vraag!

#### 2. Schrijfvaardigheid (Production écrite): E-mail of Sollicitatiebrief
Een vast onderdeel van DELF A2 is het schrijven van een kort bericht (ongeveer 40 tot 60 woorden), zoals een reactie op een advertentie voor een bijbaantje (*baby-sitting*, *serveur*) of een uitnodiging:
- **Aanhef**:
  - Informeel (vriend/kennis): *Salut Hugo, / Bonjour Léa,*
  - Formeel (onbekende werkgever): *Madame, Monsieur,*
- **Aanleiding en introductie**:
  - *J'ai lu votre petite annonce dans le journal.* (Ik heb uw advertentie gelezen.)
  - *Je suis intéressé(e) par le travail de baby-sitter.* (Ik ben geïnteresseerd in het werk.)
- **Jezelf voorstellen & ervaring toelichten**:
  - *Je m'appelle Duru, j'ai 14 ans et je suis néerlandaise.*
  - *Je parle couramment néerlandais et anglais, et un peu français.*
  - *J'ai l'habitude de m'occuper d'enfants.* (Ik ben gewend om op kinderen te passen.)
- **Beschikbaarheid & vragen stellen**:
  - *Je suis disponible du 15 au 30 juillet.* (Ik ben beschikbaar van...)
  - *Quels sont les horaires de travail ?* (Wat zijn de werktijden?)
- **Afsluiting**:
  - Informeel: *À bientôt ! / Amitiés,*
  - Formeel: *Cordialement, / Dans l'attente de votre réponse, cordialement,*

#### 3. Luister- en Spreekvaardigheid (Production et compréhension orales)
- Let bij luisteren op intonatie en getallen/tijden.
- In een mondeling gesprek geef je altijd complete zinnen en vraag je indien nodig om herhaling: *Pardon, vous pouvez répéter, s'il vous plaît ?*""",
        "vragen": [
            {
                "type": "mc",
                "vraag": "Wat is een geschikte formele aanhef voor een e-mail naar een onbekende werkgever?",
                "opties": ["Madame, Monsieur,", "Salut tout le monde,", "Cher copain,", "Coucou,"],
                "antwoord": 0,
                "uitleg": "In een formele Franse brief of mail gebruik je 'Madame, Monsieur,'."
            },
            {
                "type": "mc",
                "vraag": "Welke Franse zin betekent: 'Ik ben geïnteresseerd in het werk van babysitter'?",
                "opties": ["Je cherche un nouveau baby-sitter pour mon frère.", "Je suis intéressé(e) par le travail de baby-sitter.", "J'ai détesté le travail de baby-sitter hier.", "Je refuse de faire du baby-sitting cet été."],
                "antwoord": 1,
                "uitleg": "'Je suis intéressé(e) par...' betekent 'Ik ben geïnteresseerd in...'."
            },
            {
                "type": "mc",
                "vraag": "Wat vraag je met het Franse vraagwoord <b>'Où'</b>?",
                "opties": ["Wanneer", "Wie", "Waar", "Waarom"],
                "antwoord": 2,
                "uitleg": "'Où' met accent grave betekent waar."
            },
            {
                "type": "mc",
                "vraag": "Hoe sluit je een zakelijke of formele e-mail netjes af in het Frans?",
                "opties": ["Bisous,", "Salut,", "Gros bisous,", "Cordialement,"],
                "antwoord": 3,
                "uitleg": "'Cordialement,' is de standaard formele afsluiting (met vriendelijke groet)."
            },
            {
                "type": "waaronwaar",
                "vraag": "Bij het beantwoorden van leesvragen in DELF A2 is het slim om altijd eerst de vragen te lezen voordat je de hele tekst grondig bestudeert.",
                "antwoord": True,
                "uitleg": "Waar: door eerst de vragen te lezen weet je gericht naar welke informatie je zoekt."
            },
            {
                "type": "waaronwaar",
                "vraag": "De Franse uitdrukking 'petite annonce' betekent een kort nieuwsbericht over het weer.",
                "antwoord": False,
                "uitleg": "Onwaar: een 'petite annonce' is een kleine advertentie (bijv. personeel gezocht of te koop)."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het ERK-niveau (Europees Referentiekader) van de Grandes Lignes brug- en examentraining in klas 3 is A2.",
                "antwoord": True,
                "uitleg": "Waar: DELF A2 is het doelniveau voor het einde van klas 3 HAVO."
            },
            {
                "type": "waaronwaar",
                "vraag": "De zin 'Je parle couramment anglais' betekent dat je helemaal geen Engels spreekt.",
                "antwoord": False,
                "uitleg": "Onwaar: 'couramment' betekent vloeiend."
            },
            {
                "type": "invoer",
                "vraag": "Vertaal het Franse vraagwoord voor 'waarom' naar het Frans.",
                "antwoord": "pourquoi",
                "uitleg": "'Pourquoi' betekent waarom."
            },
            {
                "type": "invoer",
                "vraag": "Vertaal het Franse woord 'disponible' (bijv. 'Je suis disponible en juillet') naar het Nederlands.",
                "antwoord": "beschikbaar",
                "uitleg": "'Disponible' betekent beschikbaar."
            }
        ]
    }
]

examens = [
    # Toets 1 (ex-h3-frans-u8-v1)
    {
        "id": "ex-h3-frans-u8-v1",
        "hoofdstuk": 8,
        "hoofdstukTitel": "Unité 8 — Le pont",
        "titel": "Woordenschat 1 · Le pont: Eten, drinken, restaurant & basiswerkwoorden (Ch 1–5)",
        "duurMin": 20,
        "vak": "Frans · HAVO 3 (U8)",
        "icoon": "🍽️",
        "vragen": [
            {
                "type": "mc",
                "vraag": "Wat betekent <b>'le cuisinier'</b> in het Nederlands?",
                "opties": ["de kok", "de ober", "de bakker", "de slager"],
                "antwoord": 0,
                "uitleg": "'Le cuisinier' is de kok."
            },
            {
                "type": "mc",
                "vraag": "Welk tafelgerei betekent <b>'la fourchette'</b>?",
                "opties": ["het mes", "de vork", "de lepel", "het glas"],
                "antwoord": 1,
                "uitleg": "'La fourchette' is de vork."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de uitdrukking <b>'avoir envie de'</b>?",
                "opties": ["bang zijn voor", "haast hebben", "zin hebben in", "honger hebben"],
                "antwoord": 2,
                "uitleg": "'Avoir envie de' betekent zin hebben in."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent <b>'le plat du jour'</b> in een restaurant?",
                "opties": ["de menukaart", "de rekening", "het voorgerecht", "de dagschotel"],
                "antwoord": 3,
                "uitleg": "'Le plat du jour' is de dagschotel."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent <b>'le couteau'</b>?",
                "opties": ["het mes", "de vork", "het servet", "het bord"],
                "antwoord": 0,
                "uitleg": "'Le couteau' is het mes."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de Franse term <b>'le bœuf'</b> op een menukaart?",
                "opties": ["het varkensvlees", "het rundvlees", "de gebraden kip", "de eend"],
                "antwoord": 1,
                "uitleg": "'Le bœuf' is rundvlees."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de vaste uitdrukking <b>'avoir faim'</b>?",
                "opties": ["dorst hebben", "kou vatten", "honger hebben", "slaap hebben"],
                "antwoord": 2,
                "uitleg": "'Avoir faim' betekent honger hebben."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent <b>'l'assiette'</b> op de eettafel?",
                "opties": ["het glas", "het bestek", "de karaf", "het bord"],
                "antwoord": 3,
                "uitleg": "'L'assiette' betekent het bord."
            },
            {
                "type": "mc",
                "vraag": "Welk drankje betekent <b>'le jus d'orange'</b>?",
                "opties": ["sinaasappelsap", "appelsap", "mineraalwater", "citroenlimonade"],
                "antwoord": 0,
                "uitleg": "'Le jus d'orange' is sinaasappelsap."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent <b>'la cuillère'</b>?",
                "opties": ["het mes", "de lepel", "de vork", "het bord"],
                "antwoord": 1,
                "uitleg": "'La cuillère' is de lepel."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de Franse term <b>'au moins'</b> in de zin 'Ils servent au moins 40 repas per jour'?",
                "opties": ["hoogstens", "ongeveer", "minstens", "soms"],
                "antwoord": 2,
                "uitleg": "'Au moins' betekent minstens of ten minste."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het werkwoord <b>'commander'</b> in een café of bistro?",
                "opties": ["betalen", "klaarmaken", "reserveren", "bestellen"],
                "antwoord": 3,
                "uitleg": "'Commander' betekent bestellen."
            },

            # 4 Waaronwaar (2 Waar, 2 Onwaar)
            {
                "type": "waaronwaar",
                "vraag": "Het Franse woord 'le verre' betekent 'het glas'.",
                "antwoord": True,
                "uitleg": "Waar: 'le verre' is het glas."
            },
            {
                "type": "waaronwaar",
                "vraag": "De uitdrukking 'avoir soif' betekent 'het warm hebben'.",
                "antwoord": False,
                "uitleg": "Onwaar: 'avoir soif' betekent dorst hebben (warm hebben is 'avoir chaud')."
            },
            {
                "type": "waaronwaar",
                "vraag": "De term 'les couverts' slaat in een restaurant op het bestek (messen, vorken, lepels).",
                "antwoord": True,
                "uitleg": "Waar: 'les couverts' betekent het bestek."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Franse woord 'la viande' betekent uitsluitend 'vis'.",
                "antwoord": False,
                "uitleg": "Onwaar: 'la viande' betekent vlees; vis is 'le poisson'."
            },

            # 2 Invul
            {
                "type": "invul",
                "vraag": "Vul de juiste vorm van het delend lidwoord in: 'Tu veux ____ (water) minérale ?' (de l')",
                "antwoord": "de l'",
                "uitleg": "'Eau' begint met een klinker, dus 'de l''."
            },
            {
                "type": "invul",
                "vraag": "Vul de juiste présent-vorm van het werkwoord 'venir' in: 'Mes grands-parents ____ (komen) demain chez nous.' (viennent)",
                "antwoord": "viennent",
                "uitleg": "Voor ils/elles is de présent-vorm 'viennent'."
            },

            # 2 Open
            {
                "type": "open",
                "vraag": "Welke twee tafelgerei-voorwerpen gebruik je gewoonlijk om een biefstuk op je bord te snijden en naar je mond te brengen?",
                "modelantwoord": "Dat zijn le couteau (het mes) en la fourchette (de vork).",
                "sleutelwoorden": [
                    "couteau",
                    "fourchette"
                ],
                "minTreffers": 2,
                "uitleg": "Het mes is le couteau en de vork is la fourchette."
            },
            {
                "type": "open",
                "vraag": "Noem de twee Franse uitdrukkingen met avoir die aangeven dat iemand dringend eten respectievelijk drinken nodig heeft.",
                "modelantwoord": "Dat zijn avoir faim en avoir soif.",
                "sleutelwoorden": [
                    "avoir faim/faim",
                    "avoir soif/soif"
                ],
                "minTreffers": 2,
                "uitleg": "Honger hebben is avoir faim en dorst hebben is avoir soif."
            }
        ]
    },

    # Toets 2 (ex-h3-frans-u8-v2)
    {
        "id": "ex-h3-frans-u8-v2",
        "hoofdstuk": 8,
        "hoofdstukTitel": "Unité 8 — Le pont",
        "titel": "Woordenschat 2 · Le pont: Identiteit, school, tijden & vergelijkingen (Ch 1–6)",
        "duurMin": 20,
        "vak": "Frans · HAVO 3 (U8)",
        "icoon": "👤",
        "vragen": [
            {
                "type": "mc",
                "vraag": "Wat betekent <b>'courageux'</b>?",
                "opties": ["moedig", "lui", "onhandig", "vervelend"],
                "antwoord": 0,
                "uitleg": "'Courageux' betekent moedig."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent <b>'le bac'</b> in het Franse schoolsysteem?",
                "opties": ["de brugklas", "het eindexamen", "het rapport", "het schoolplein"],
                "antwoord": 1,
                "uitleg": "'Le bac' (baccalauréat) is het Franse eindexamen."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het werkwoord <b>'se lever'</b> in de ochtend?",
                "opties": ["ontbijten", "douchen", "opstaan", "vertrekken"],
                "antwoord": 2,
                "uitleg": "'Se lever' betekent opstaan (je me lève = ik sta op)."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent <b>'la note'</b> in de context van school?",
                "opties": ["het lesuur", "het schrift", "het huiswerk", "het cijfer"],
                "antwoord": 3,
                "uitleg": "'La note' betekent het cijfer of de beoordeling."
            },
            {
                "type": "mc",
                "vraag": "Welk Frans woord betekent <b>'lui'</b>?",
                "opties": ["paresseux", "actif", "sportif", "gentil"],
                "antwoord": 0,
                "uitleg": "'Paresseux' betekent lui."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent <b>'la confiance'</b>?",
                "opties": ["de angst", "het vertrouwen", "de twijfel", "de vriendschap"],
                "antwoord": 1,
                "uitleg": "'La confiance' betekent het vertrouwen."
            },
            {
                "type": "mc",
                "vraag": "Hoe zeg je: 'Zij is intelligenter dan haar broer'?",
                "opties": ["Elle est aussi intelligente que son frère.", "Elle est moins intelligente que son frère.", "Elle est plus intelligente que son frère.", "Elle est meilleure intelligente que son frère."],
                "antwoord": 2,
                "uitleg": "'Meer ... dan' vertaal je met 'plus ... que'."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent <b>'arriver en retard'</b>?",
                "opties": ["op tijd komen", "te vroeg zijn", "afwezig zijn", "te laat aankomen"],
                "antwoord": 3,
                "uitleg": "'Arriver en retard' betekent te laat aankomen."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent <b>'énervant'</b>?",
                "opties": ["irritant", "vrolijk", "rustig", "grappig"],
                "antwoord": 0,
                "uitleg": "'Énervant' betekent irritant of op de zenuwen werkend."
            },
            {
                "type": "mc",
                "vraag": "Wat is het voltooid deelwoord van <b>'faire'</b>?",
                "opties": ["fais", "fait", "fairé", "faisant"],
                "antwoord": 1,
                "uitleg": "Het voltooid deelwoord van faire is onregelmatig: 'fait'."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent <b>'rater'</b> in de zin 'Il a raté son bus'?",
                "opties": ["besturen", "nemen", "missen", "wachten op"],
                "antwoord": 2,
                "uitleg": "'Rater' betekent missen (of zakken voor een examen)."
            },
            {
                "type": "mc",
                "vraag": "Welke vorm van de trappen van vergelijking gebruik je voor 'net zo groot als' bij een vrouwelijk onderwerp?",
                "opties": ["plus grand que", "plus grande que", "aussi grand que", "aussi grande que"],
                "antwoord": 3,
                "uitleg": "'Aussi grande que' heeft accord met het vrouwelijke onderwerp."
            },

            # 4 Waaronwaar (2 Waar, 2 Onwaar)
            {
                "type": "waaronwaar",
                "vraag": "In de zin 'Arthur est plus fort qu'Hugo' betekent 'plus fort que' sterker dan.",
                "antwoord": True,
                "uitleg": "Waar: 'plus fort que' betekent sterker dan."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Franse woord 'la récré' is de afkorting van 'la récréation' en betekent de les.",
                "antwoord": False,
                "uitleg": "Onwaar: 'la récréation' (la récré) betekent de pauze (speelkwartier)."
            },
            {
                "type": "waaronwaar",
                "vraag": "De futur proche wordt gevormd met het hulpwerkwoord 'aller' gevolgd door de infinitief.",
                "antwoord": True,
                "uitleg": "Waar: bijv. 'je vais manger', 'nous allons partir'."
            },
            {
                "type": "waaronwaar",
                "vraag": "De uitdrukking 'poser une question' betekent 'een antwoord geven'.",
                "antwoord": False,
                "uitleg": "Onwaar: 'poser une question' betekent een vraag stellen; antwoord geven is 'répondre'."
            },

            # 2 Invul
            {
                "type": "invul",
                "vraag": "Vul de juiste comparatief in voor 'minder snel dan' (vrouwelijk): 'Cette voiture est ____ (minder snel dan) le train.' (moins rapide que)",
                "antwoord": "moins rapide que",
                "uitleg": "'Minder ... dan' is 'moins ... que'."
            },
            {
                "type": "invul",
                "vraag": "Vul de juiste vervoeging in van 'se réveiller' (present, je-vorm): 'Chaque matin, ____ (ik word wakker) à sept heures.' (je me réveille)",
                "antwoord": "je me réveille",
                "uitleg": "De je-vorm van het wederkerende werkwoord se réveiller is 'je me réveille'."
            },

            # 2 Open
            {
                "type": "open",
                "vraag": "Welke twee tegenovergestelde karaktereigenschappen betekenen in het Frans respectievelijk 'lui' en 'moedig'?",
                "modelantwoord": "Dat zijn paresseux (lui) en courageux (moedig).",
                "sleutelwoorden": [
                    "paresseux",
                    "courageux"
                ],
                "minTreffers": 2,
                "uitleg": "Paresseux is lui en courageux is moedig."
            },
            {
                "type": "open",
                "vraag": "Noem de twee onderdelen waaruit de Franse 'futur proche' (nabije toekomst) is opgebouwd.",
                "modelantwoord": "De futur proche bestaat uit een vorm van het werkwoord aller en een heel werkwoord (infinitief).",
                "sleutelwoorden": [
                    "aller",
                    "infinitief/hele werkwoord"
                ],
                "minTreffers": 2,
                "uitleg": "De futur proche bestaat uit aller + infinitief."
            }
        ]
    },

    # Toets 3 (ex-h3-frans-u8-v3)
    {
        "id": "ex-h3-frans-u8-v3",
        "hoofdstuk": 8,
        "hoofdstukTitel": "Unité 8 — Le pont",
        "titel": "Woordenschat 3 · Le pont: Geld, materialen & signaalwoorden (Ch 1–7)",
        "duurMin": 20,
        "vak": "Frans · HAVO 3 (U8)",
        "icoon": "💶",
        "vragen": [
            {
                "type": "mc",
                "vraag": "Welke term gebruiken Franse scholieren voor het geld dat ze maandelijks van hun ouders ontvangen?",
                "opties": ["l'argent de poche", "le salaire brut", "la bourse d'études", "la facture"],
                "antwoord": 0,
                "uitleg": "'L'argent de poche' is zakgeld."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het signaalwoord <b>'donc'</b>?",
                "opties": ["maar", "dus", "omdat", "eerst"],
                "antwoord": 1,
                "uitleg": "'Donc' betekent dus."
            },
            {
                "type": "mc",
                "vraag": "Welk materiaal betekent <b>'en bois'</b>?",
                "opties": ["van ijzer", "van leer", "van hout", "van glas"],
                "antwoord": 2,
                "uitleg": "'En bois' betekent van hout."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het werkwoord <b>'dépenser'</b>?",
                "opties": ["sparen", "lenen", "verdienen", "uitgeven"],
                "antwoord": 3,
                "uitleg": "'Dépenser' betekent uitgeven."
            },
            {
                "type": "mc",
                "vraag": "Wat drukt het Franse signaalwoord <b>'pourtant'</b> uit in een tekst?",
                "opties": ["een tegenstelling ('toch / echter')", "een reden ('omdat')", "een opsomming ('en')", "een tijdstip ('gisteren')"],
                "antwoord": 0,
                "uitleg": "'Pourtant' betekent toch of echter en drukt een tegenstelling uit."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent <b>'en fer'</b>?",
                "opties": ["van zilver", "van ijzer", "van plastic", "van katoen"],
                "antwoord": 1,
                "uitleg": "'En fer' betekent van ijzer."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent <b>'un petit boulot'</b>?",
                "opties": ["een vaste baan", "een carriere", "een bijbaantje", "een stage"],
                "antwoord": 2,
                "uitleg": "'Un petit boulot' is een bijbaantje."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het signaalwoord <b>'car'</b>?",
                "opties": ["dus", "maar", "daarna", "want"],
                "antwoord": 3,
                "uitleg": "'Car' betekent want of omdat."
            },
            {
                "type": "mc",
                "vraag": "Wat voor soort materiaal betekent de aanduiding <b>'le cuir'</b> in het Nederlands?",
                "opties": ["leer", "wol", "linnen", "goud"],
                "antwoord": 0,
                "uitleg": "'Le cuir' is leer."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent <b>'économiser'</b>?",
                "opties": ["verspillen", "sparen", "betalen", "uitdelen"],
                "antwoord": 1,
                "uitleg": "'Économiser' betekent sparen of zuinig aandoen."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het signaalwoord <b>'enfin'</b>?",
                "opties": ["eerst", "soms", "ten slotte", "nooit"],
                "antwoord": 2,
                "uitleg": "'Enfin' betekent ten slotte of eindelijk."
            },
            {
                "type": "mc",
                "vraag": "Welke meetkundige vorm heeft een voorwerp dat in het Frans <b>'carré'</b> wordt genoemd?",
                "opties": ["rond", "driehoekig", "langwerpig", "vierkant"],
                "antwoord": 3,
                "uitleg": "'Carré' betekent vierkant."
            },

            # 4 Waaronwaar (2 Waar, 2 Onwaar)
            {
                "type": "waaronwaar",
                "vraag": "Het signaalwoord 'par exemple' betekent 'bijvoorbeeld'.",
                "antwoord": True,
                "uitleg": "Waar: 'par exemple' betekent bijvoorbeeld."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Franse woord 'lourd' betekent licht van gewicht.",
                "antwoord": False,
                "uitleg": "Onwaar: 'lourd' betekent zwaar; licht is 'léger'."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het woord 'le prix' betekent zowel 'de prijs' als 'de beloning'.",
                "antwoord": True,
                "uitleg": "Waar: 'le prix' betekent prijs (bedrag) of onderscheiding/prijs."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het signaalwoord 'puis' betekent 'omdat'.",
                "antwoord": False,
                "uitleg": "Onwaar: 'puis' betekent daarna of vervolgens."
            },

            # 2 Invul
            {
                "type": "invul",
                "vraag": "Vul het juiste voorzetsel in voor materialen: 'Cette table est faite ____ (van hout).' (en bois)",
                "antwoord": "en bois|en",
                "uitleg": "Materialen worden in het Frans aangeduid met 'en' (en bois, en verre, en cuir)."
            },
            {
                "type": "invul",
                "vraag": "Vul het juiste signaalwoord in voor 'sinds': 'J'habite à Amsterdam ____ (sinds) deux ans.' (depuis)",
                "antwoord": "depuis",
                "uitleg": "'Depuis' betekent sinds of al ... lang."
            },

            # 2 Open
            {
                "type": "open",
                "vraag": "Welke twee Franse werkwoorden geven aan dat iemand enerzijds geld spaart en anderzijds geld uitgeeft?",
                "modelantwoord": "Dat zijn économiser (sparen) en dépenser (uitgeven).",
                "sleutelwoorden": [
                    "économiser/economiser",
                    "dépenser/depenser"
                ],
                "minTreffers": 2,
                "uitleg": "Économiser is sparen en dépenser is uitgeven."
            },
            {
                "type": "open",
                "vraag": "Noem twee Franse signaalwoorden die een reden of verklaring aangeven (vertaling van 'want' of 'omdat').",
                "modelantwoord": "Dat zijn car (want) en parce que (omdat).",
                "sleutelwoorden": [
                    "car",
                    "parce que"
                ],
                "minTreffers": 2,
                "uitleg": "De signaalwoorden voor reden zijn car en parce que."
            }
        ]
    },

    # Toets 4 (ex-h3-frans-u8-v4)
    {
        "id": "ex-h3-frans-u8-v4",
        "hoofdstuk": 8,
        "hoofdstukTitel": "Unité 8 — Le pont",
        "titel": "Grammaticaal Overzicht · Werkwoorden, tijden, vergelijkingen & ontkenningen",
        "duurMin": 20,
        "vak": "Frans · HAVO 3 (U8)",
        "icoon": "📐",
        "vragen": [
            {
                "type": "mc",
                "vraag": "Hoe luidt de gebiedende wijs van 'manger' voor de enkelvoudige je-vorm (tu)?",
                "opties": ["Mange !", "Manges !", "Tu manges !", "Mangez !"],
                "antwoord": 0,
                "uitleg": "Bij -er werkwoorden vervalt de -s in de gebiedende wijs voor tu: 'Mange !'."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de ontkenning <b>'ne ... plus'</b>?",
                "opties": ["nog niet", "niet meer", "nooit", "niemand"],
                "antwoord": 1,
                "uitleg": "'Ne ... plus' betekent niet meer."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de ontkenning <b>'ne ... personne'</b>?",
                "opties": ["niets", "nooit", "niemand", "nergens"],
                "antwoord": 2,
                "uitleg": "'Ne ... personne' betekent niemand."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent <b>'ne ... pas encore'</b>?",
                "opties": ["niet meer", "nooit meer", "helemaal niet", "nog niet"],
                "antwoord": 3,
                "uitleg": "'Ne ... pas encore' betekent nog niet."
            },
            {
                "type": "mc",
                "vraag": "Welke vorm is de juiste passé composé voor 'Zij is vertrokken'?",
                "opties": ["Elle est partie", "Elle a parti", "Elle est parti", "Elle a partie"],
                "antwoord": 0,
                "uitleg": "Partir gaat met être en krijgt accord voor vrouwelijk enkelvoud: 'Elle est partie'."
            },
            {
                "type": "mc",
                "vraag": "Welk delend lidwoord hoort in de ontkennende zin: 'Je n'ai pas ____ argent'?",
                "opties": ["de l'", "d'", "du", "des"],
                "antwoord": 1,
                "uitleg": "Na een ontkenning gebruik je 'd'' voor een klinker (argent)."
            },
            {
                "type": "mc",
                "vraag": "Welke vorm is de juiste gebiedende wijs voor 'nous' van het werkwoord 'faire'?",
                "opties": ["Faites !", "Fais !", "Faisons !", "Nous faisons !"],
                "antwoord": 2,
                "uitleg": "De gebiedende wijs voor nous is 'Faisons !' (Laten we doen!)."
            },
            {
                "type": "mc",
                "vraag": "Wat is het voltooid deelwoord van het werkwoord <b>prendre</b> (nemen)?",
                "opties": ["prendu", "prené", "prind", "pris"],
                "antwoord": 3,
                "uitleg": "Het voltooid deelwoord van prendre is 'pris'."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de ontkenning <b>'ne ... jamais'</b>?",
                "opties": ["nooit", "niets", "niemand", "nog niet"],
                "antwoord": 0,
                "uitleg": "'Ne ... jamais' betekent nooit."
            },
            {
                "type": "mc",
                "vraag": "Wat is de juiste vervoeging van <b>vendre</b> (verkopen) voor 'ils' in de présent?",
                "opties": ["ils vend", "ils vendent", "ils vendons", "ils vendez"],
                "antwoord": 1,
                "uitleg": "De ils-vorm van regelmatige -re werkwoorden eindigt op -ent: 'ils vendent'."
            },
            {
                "type": "mc",
                "vraag": "Hoe vervoeg je 'pouvoir' voor de nous-vorm in de présent?",
                "opties": ["nous peuvons", "nous pourrons", "nous pouvons", "nous pouvent"],
                "antwoord": 2,
                "uitleg": "De nous-vorm van pouvoir is 'nous pouvons'."
            },
            {
                "type": "mc",
                "vraag": "Welke uitgang krijgt de vous-vorm van regelmatige werkwoorden op -ir in de présent?",
                "opties": ["-ez", "-ent", "-ons", "-issez"],
                "antwoord": 3,
                "uitleg": "Bij regelmatig -ir (finir) is de vous-vorm 'vous finissez'."
            },

            # 4 Waaronwaar (2 Waar, 2 Onwaar)
            {
                "type": "waaronwaar",
                "vraag": "In een gebiedende wijs (impératif) mag je het onderwerp 'tu' of 'vous' nooit opschrijven.",
                "antwoord": True,
                "uitleg": "Waar: bij de gebiedende wijs vervalt het persoonlijk voornaamwoord."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het hulpwerkwoord van de ontkenning 'ne ... rien' staat altijd achteraan in de zin na het voltooid deelwoord.",
                "antwoord": False,
                "uitleg": "Onwaar: 'rien' komt tussen het hulpwerkwoord en voltooid deelwoord (bijv. 'Je n'ai rien fait')."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het werkwoord 'aller' vormt in de passé composé zijn voltooide tijd met het hulpwerkwoord 'être'.",
                "antwoord": True,
                "uitleg": "Waar: aller is een bewegingswerkwoord en gaat met être (bijv. 'il est allé')."
            },
            {
                "type": "waaronwaar",
                "vraag": "In het Frans schrijf je 'plus bon que' wanneer iets lekkerder of beter smaakt.",
                "antwoord": False,
                "uitleg": "Onwaar: je gebruikt 'meilleur(e) que'."
            },

            # 2 Invul
            {
                "type": "invul",
                "vraag": "Vul de juiste ontkenning in voor 'niets': 'Je n'ai ____ (niets) compris.' (rien)",
                "antwoord": "rien",
                "uitleg": "Niets = 'ne ... rien'."
            },
            {
                "type": "invul",
                "vraag": "Vul de juiste gebiedende wijs in van 'finir' voor jullie (vous): '____ (Maak af) vos devoirs !' (Finissez)",
                "antwoord": "Finissez|finissez",
                "uitleg": "De vous-vorm van finir in de impératif is 'Finissez !'."
            },

            # 2 Open
            {
                "type": "open",
                "vraag": "Noem de twee Franse ontkenningswoorden die respectievelijk 'nooit' en 'niet meer' uitdrukken (elk gecombineerd met ne).",
                "modelantwoord": "Dat zijn jamais (nooit) en plus (niet meer).",
                "sleutelwoorden": [
                    "jamais",
                    "plus"
                ],
                "minTreffers": 2,
                "uitleg": "De ontkenningen zijn ne...jamais (nooit) en ne...plus (niet meer)."
            },
            {
                "type": "open",
                "vraag": "Noem het hulpwerkwoord waarmee bewegingswerkwoorden zoals aller, venir en partir in de passé composé worden vervoegd.",
                "modelantwoord": "Dat hulpwerkwoord is être (zijn).",
                "sleutelwoorden": [
                    "être/etre"
                ],
                "minTreffers": 1,
                "uitleg": "Bewegingswerkwoorden worden in de passé composé met être vervoegd."
            }
        ]
    },

    # Toets 5 (ex-h3-frans-u8-v5)
    {
        "id": "ex-h3-frans-u8-v5",
        "hoofdstuk": 8,
        "hoofdstukTitel": "Unité 8 — Le pont",
        "titel": "DELF A2 & Examentraining · Leesbegrip, uitdrukkingen & schrijfvaardigheid",
        "duurMin": 20,
        "vak": "Frans · HAVO 3 (U8)",
        "icoon": "🎯",
        "vragen": [
            {
                "type": "mc",
                "vraag": "Wat betekent <b>'une petite annonce'</b> in een krant of op internet?",
                "opties": ["een kleine advertentie", "een weerbericht", "een kortingsbon", "een nieuwsbrief"],
                "antwoord": 0,
                "uitleg": "'Une petite annonce' is een advertentie."
            },
            {
                "type": "mc",
                "vraag": "Wat vraag je met het vraagwoord <b>'Quand'</b>?",
                "opties": ["Waar", "Wanneer", "Hoe", "Waarom"],
                "antwoord": 1,
                "uitleg": "'Quand' betekent wanneer."
            },
            {
                "type": "mc",
                "vraag": "Wat vraag je met het vraagwoord <b>'Combien'</b>?",
                "opties": ["Wie", "Waarom", "Hoeveel", "Wat"],
                "antwoord": 2,
                "uitleg": "'Combien' betekent hoeveel."
            },
            {
                "type": "mc",
                "vraag": "Wat vraag je met het vraagwoord <b>'Comment'</b>?",
                "opties": ["Waarom", "Wie", "Wanneer", "Hoe"],
                "antwoord": 3,
                "uitleg": "'Comment' betekent hoe."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent <b>'parler couramment'</b>?",
                "opties": ["vloeiend spreken", "zachtjes praten", "moeite hebben met spreken", "snel fluisteren"],
                "antwoord": 0,
                "uitleg": "'Parler couramment' betekent een taal vloeiend spreken."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de term <b>'disponible'</b> in een sollicitatie?",
                "opties": ["ervaren", "beschikbaar", "geslaagd", "gemotiveerd"],
                "antwoord": 1,
                "uitleg": "'Disponible' betekent beschikbaar."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de zin <b>'J'ai l'habitude de garder des enfants'</b>?",
                "opties": ["Ik wil geen kinderen zien.", "Ik heb zelf kinderen.", "Ik ben gewend op kinderen te passen.", "Ik vind kinderen irritant."],
                "antwoord": 2,
                "uitleg": "'Avoir l'habitude de' betekent gewend zijn om te..."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent <b>'À bientôt'</b>?",
                "opties": ["Goedenavond", "Tot gisteren", "Vaarwel", "Tot snel"],
                "antwoord": 3,
                "uitleg": "'À bientôt' betekent tot snel of tot ziens."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de formulering <b>'Madame, Monsieur,'</b> aan het begin van een e-mail?",
                "opties": ["Geachte heer, mevrouw,", "Beste vrienden,", "Lieve ouders,", "Hallo allemaal,"],
                "antwoord": 0,
                "uitleg": "'Madame, Monsieur,' is de formele aanhef voor 'Geachte heer, mevrouw,'."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de afsluiting <b>'Cordialement'</b> in een formele e-mail?",
                "opties": ["Tot vanavond", "Met vriendelijke groet", "Dikke kus", "Tot snel"],
                "antwoord": 1,
                "uitleg": "'Cordialement' betekent met vriendelijke groet."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent <b>'un CV'</b> (curriculum vitae)?",
                "opties": ["een paspoort", "een cijferlijst", "een overzicht van je opleiding en werkervaring", "een aanbevelingsbrief"],
                "antwoord": 2,
                "uitleg": "Een CV is een levensloop met je opleiding en ervaring."
            },
            {
                "type": "mc",
                "vraag": "Welk werkwoord gebruik je voor 'zich voorstellen' in het Frans?",
                "opties": ["se préparer", "se coucher", "s'amuser", "se présenter"],
                "antwoord": 3,
                "uitleg": "'Se présenter' betekent zich voorstellen."
            },

            # 4 Waaronwaar (2 Waar, 2 Onwaar)
            {
                "type": "waaronwaar",
                "vraag": "Het Frans-diploma DELF A2 is een officieel erkend internationaal taalcertificaat.",
                "antwoord": True,
                "uitleg": "Waar: DELF wordt wereldwijd erkend door het Franse Ministerie van Onderwijs."
            },
            {
                "type": "waaronwaar",
                "vraag": "In een formele Franse brief sluit je altijd af met 'Gros bisous'.",
                "antwoord": False,
                "uitleg": "Onwaar: 'Gros bisous' (dikke zoenen) is uiterst informeel voor familie of geliefden."
            },
            {
                "type": "waaronwaar",
                "vraag": "De vraag 'Quels sont les horaires ?' vraagt naar de werktijden.",
                "antwoord": True,
                "uitleg": "Waar: 'les horaires' zijn de werktijden of dienstregeling."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het vraagwoord 'Qui' betekent 'waarom'.",
                "antwoord": False,
                "uitleg": "Onwaar: 'Qui' betekent wie; waarom is 'pourquoi'."
            },

            # 2 Invul
            {
                "type": "invul",
                "vraag": "Vul het juiste vraagwoord in voor 'Waarom': '____ (Waarom) tu veux travailler à Paris ?' (Pourquoi)",
                "antwoord": "Pourquoi|pourquoi",
                "uitleg": "'Pourquoi' betekent waarom."
            },
            {
                "type": "invul",
                "vraag": "Vul de juiste formule in voor 'Met vriendelijke groet': '____ (Met vriendelijke groet), Duru.' (Cordialement)",
                "antwoord": "Cordialement|cordialement",
                "uitleg": "'Cordialement' betekent met vriendelijke groet."
            },

            # 2 Open
            {
                "type": "open",
                "vraag": "Noem de twee Franse vraagwoorden die in leesteksten informeren naar respectievelijk een plaats (waar) en een tijdstip (wanneer).",
                "modelantwoord": "Dat zijn où (waar) en quand (wanneer).",
                "sleutelwoorden": [
                    "où/ou",
                    "quand"
                ],
                "minTreffers": 2,
                "uitleg": "Waar is où en wanneer is quand."
            },
            {
                "type": "open",
                "vraag": "Welke formele Franse aanhef (twee woorden) gebruik je bovenaan een zakelijke brief wanneer de naam van de geadresseerde niet bekend is?",
                "modelantwoord": "Dat is de aanhef Madame, Monsieur,.",
                "sleutelwoorden": [
                    "Madame",
                    "Monsieur"
                ],
                "minTreffers": 2,
                "uitleg": "De formele aanhef is Madame, Monsieur,."
            }
        ]
    }
]

def scramble_exam_mc(exam, seed_seq):
    mc_questions = [q for q in exam['vragen'] if q['type'] == 'mc']
    for q, target_ans in zip(mc_questions, seed_seq):
        cur_ans = q['antwoord']
        if cur_ans != target_ans:
            q['opties'][cur_ans], q['opties'][target_ans] = q['opties'][target_ans], q['opties'][cur_ans]
            q['antwoord'] = target_ans

def generate_onderwerp(data):
    content = f"""/* Onderwerp: {data['titel']}
   Grandes Lignes 3 HAVO Unité {data['hoofdstuk']} */
DURU.register({{
  "id": "{data['id']}",
  "hoofdstuk": {data['hoofdstuk']},
  "hoofdstukTitel": "Unité {data['hoofdstuk']} — Le pont",
  "titel": "{data['titel']}",
  "vak": "Frans · HAVO 3 (U{data['hoofdstuk']})",
  "theorie": {json.dumps(data['theorie'].strip(), ensure_ascii=False)},
  "vragen": {json.dumps(data['vragen'], ensure_ascii=False, indent=4)}
}});
"""
    filepath = os.path.join(OUT_DIR, data['file'])
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Geschreven onderwerp: {data['file']}")

def generate_examen(data, filename):
    content = f"""/* Proeftoets {data['titel']}
   Grandes Lignes 3 HAVO Unité {data['hoofdstuk']} */
DURU.registerExamen({{
  "id": "{data['id']}",
  "hoofdstuk": {data['hoofdstuk']},
  "hoofdstukTitel": "{data['hoofdstukTitel']}",
  "titel": "{data['titel']}",
  "vak": "{data['vak']}",
  "icoon": "{data['icoon']}",
  "duurMin": {data['duurMin']},
  "vragen": {json.dumps(data['vragen'], ensure_ascii=False, indent=4)}
}});
"""
    filepath = os.path.join(OUT_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Geschreven examen: {filename}")

SEEDS = [
    [0, 2, 1, 3, 0, 1, 3, 2, 3, 0, 2, 1],
    [1, 3, 0, 2, 3, 2, 1, 0, 0, 1, 2, 3],
    [2, 0, 3, 1, 1, 3, 0, 2, 2, 1, 3, 0],
    [3, 1, 2, 0, 2, 0, 1, 3, 1, 2, 0, 3],
    [0, 3, 2, 1, 2, 1, 0, 3, 3, 2, 1, 0]
]

if __name__ == "__main__":
    for ond in onderwerpen:
        generate_onderwerp(ond)
    for i, ex in enumerate(examens, 1):
        scramble_exam_mc(ex, SEEDS[i-1])
        generate_examen(ex, f"examen_u8_vocab_{i}.js")

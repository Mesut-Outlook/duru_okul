#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator voor Frans Unité 6 (C'est moi!)
Boek: Grandes Lignes 3 HAVO, Chapitre 6 (p. 232-236)

Genereert:
- 4 Oefenlessen / Onderwerpen (h6_1.js t/m h6_4.js):
  - 6.1 Vocabulaire A & B: Identiteit, media, uiterlijk & karakter
  - 6.2 Vocabulaire E & F: Dagindeling, klokkijken & schoolleven
  - 6.3 Phrases-clés C & G: Jezelf voorstellen & Praten over gewoontes
  - 6.4 Grammaire D & H: De vergelijkingen (plus/moins/aussi...que) & Woordvolgorde
- 5 Begrippentoetsen / Proeftoetsen (examen_u6_vocab_1.js t/m examen_u6_vocab_5.js)
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "havo3", "frans", "js", "data")

ONDERWERPEN = [
    # H6 §6.1
    {
        "id": "fr-u6-1",
        "hoofdstuk": 6,
        "paragraaf": "6.1",
        "titel": "Vocabulaire A & B · Identiteit, media, uiterlijk & karakter",
        "korteUitleg": "De kernwoordenschat van Unité 6 Blok A en B (p. 232): persoonsbeschrijvingen, karaktertrekken (moedig, lui, grappig), media, gevoelens en de overstap naar volwassenheid.",
        "icoon": "👤",
        "kleur": "oranje",
        "theorie": """
    <h3>6.1 Vocabulaire A & B: Identiteit, media & karakter</h3>
    <div class="info-box">
      <b>C'est moi!</b> In dit hoofdstuk draait alles om jezelf: wie ben je, hoe zie je eruit, wat is je karakter en hoe leef je samen met je familie en vrienden? We starten met de basiswoorden uit Blok A en B (p. 232).
    </div>

    <h4>1. Persoonsbeschrijving & Zelfstandige naamwoorden (Blok A)</h4>
    <table class="vocab-table">
      <thead><tr><th>Frans</th><th>Nederlands</th><th>Voorbeeld</th></tr></thead>
      <tbody>
        <tr><td><b>l'émission</b> (v)</td><td>de uitzending</td><td><i>Regarder une émission à la télé.</i></td></tr>
        <tr><td><b>la célébrité</b></td><td>de beroemdheid</td><td><i>Une grande célébrité française.</i></td></tr>
        <tr><td><b>la voix</b></td><td>de stem</td><td><i>Avoir une belle voix grave.</i></td></tr>
        <tr><td><b>l'adulte</b> (m/v)</td><td>de volwassene</td><td><i>Parler comme un adulte.</i></td></tr>
        <tr><td><b>la dispute</b></td><td>de ruzie</td><td><i>Avoir une dispute avec quelqu'un.</i></td></tr>
        <tr><td><b>la confiance</b></td><td>het vertrouwen</td><td><i>Avoir confiance en ses amis.</i></td></tr>
        <tr><td><b>le mot</b></td><td>het woord</td><td><i>Écrire un petit mot gentil.</i></td></tr>
        <tr><td><b>le pied</b></td><td>de voet</td><td><i>Y aller à pied.</i></td></tr>
      </tbody>
    </table>

    <h4>2. Karakter en eigenschappen (Les adjectifs de personnalité)</h4>
    <ul>
      <li><b>courageux, courageuse</b> = moedig (<i>Il est très courageux.</i>)</li>
      <li><b>paresseux, paresseuse</b> = lui (<i>Ne sois pas si paresseux!</i>)</li>
      <li><b>marrant(e)</b> = grappig | <b>énervant(e)</b> = irritant</li>
      <li><b>mignon, mignonne</b> = schattig, lief</li>
      <li><b>dingue</b> = gek, bizar (informeel Frans)</li>
      <li><b>différent(e)</b> = verschillend | <b>sûr(e)</b> = zeker</li>
      <li><b>couramment</b> = vloeiend (<i>parler français couramment</i>)</li>
    </ul>

    <h4>3. Toekomst, studie en maatschappij (Blok B)</h4>
    <ul>
      <li><b>le bac</b> (le baccalauréat) = het Franse eindexamen van de middelbare school</li>
      <li><b>le travail</b> = het werk | <b>les études</b> (v mv) = de studie / opleiding</li>
      <li><b>le monde</b> = de wereld | <b>la banlieue</b> = de buitenwijk (van een grote stad)</li>
      <li><b>pourtant</b> = toch, echter | <b>à cause de</b> = vanwege, door</li>
      <li><b>refuser</b> = weigeren | <b>quitter</b> = verlaten | <b>arrêter</b> = stoppen</li>
      <li><b>plusieurs</b> = meerdere | <b>ensemble</b> = samen | <b>tous les jours</b> = elke dag</li>
    </ul>
""",
        "vragen": [
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'la dispute'</b>?",
                "opties": [
                    "de ontmoeting",
                    "de ruzie",
                    "de toespraak",
                    "de afspraak"
                ],
                "antwoord": 1,
                "uitleg": "'La dispute' is de ruzie in het Frans."
            },
            {
                "type": "mc",
                "vraag": "Welk bijvoeglijk naamwoord betekent <b>'moedig'</b> in het Frans?",
                "opties": [
                    "paresseux",
                    "énervant",
                    "courageux",
                    "marrant"
                ],
                "antwoord": 2,
                "uitleg": "'Courageux' (vrouwelijk: courageuse) betekent moedig."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de Franse schoolterm <b>'le bac'</b>?",
                "opties": [
                    "het rapportcijfer",
                    "het lesrooster",
                    "de schoolkantine",
                    "het eindexamen"
                ],
                "antwoord": 3,
                "uitleg": "'Le bac' (baccalauréat) is het Franse eindexamen."
            },
            {
                "type": "mc",
                "vraag": "Wat is de Nederlandse betekenis van het Franse woord <b>'la confiance'</b>?",
                "opties": [
                    "het vertrouwen",
                    "de vriendschap",
                    "de jaloezie",
                    "de verlegenheid"
                ],
                "antwoord": 0,
                "uitleg": "'La confiance' betekent het vertrouwen."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Franse woord 'paresseux' betekent 'erg hardwerkend en ijverig'.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Paresseux' betekent lui."
            },
            {
                "type": "waaronwaar",
                "vraag": "De uitdrukking 'parler couramment le français' betekent 'vloeiend Frans spreken'.",
                "antwoord": True,
                "uitleg": "Waar! 'Couramment' betekent vloeiend."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Franse woord 'la banlieue' betekent het historisch stadscentrum.",
                "antwoord": False,
                "uitleg": "Onwaar! 'La banlieue' is de buitenwijk of voorstad."
            },
            {
                "type": "invoer",
                "vraag": "Vertaal het woord voor 'de stem' in het Frans (vrouwelijk met lidwoord, la voix):",
                "antwoord": "la voix|voix",
                "uitleg": "De stem is 'la voix'."
            },
            {
                "type": "invoer",
                "vraag": "Vertaal het bijvoeglijk naamwoord tussen haakjes: 'Ce garçon est très (grappig).' Vul het Franse woord in (marrant):",
                "antwoord": "marrant",
                "uitleg": "Grappig is 'marrant'."
            },
            {
                "type": "invoer",
                "vraag": "Vertaal het woord voor 'de volwassene' in het Frans (met lidwoord, l'adulte):",
                "antwoord": "l'adulte|adulte",
                "uitleg": "De volwassene is 'l'adulte'."
            }
        ]
    },

    # H6 §6.2
    {
        "id": "fr-u6-2",
        "hoofdstuk": 6,
        "paragraaf": "6.2",
        "titel": "Vocabulaire E & F · Dagindeling, klokkijken & schoolleven",
        "korteUitleg": "Woordenschat van Unité 6 Blok E en F (p. 233): je dagelijkse routine beschrijven, de klok lezen in het Frans, en handige termen over cijfers, schoolpauzes en tijd.",
        "icoon": "⏰",
        "kleur": "blauw",
        "theorie": """
    <h3>6.2 Vocabulaire E & F: Dagindeling, klokkijken & school</h3>
    <div class="info-box">
      <b>Ma journée:</b> Hoe ziet jouw dag eruit? In Blok E en F leer je vertellen hoe laat je opstaat, naar school gaat, huiswerk maakt en naar bed gaat. Ook leer je Frans klokkijken!
    </div>

    <h4>1. Dagelijkse routine (La routine quotidienne, Blok E)</h4>
    <table class="vocab-table">
      <thead><tr><th>Frans</th><th>Nederlands</th><th>Toelichting</th></tr></thead>
      <tbody>
        <tr><td><b>je me lève</b></td><td>ik sta op</td><td>Wederkerend werkwoord <i>se lever</i></td></tr>
        <tr><td><b>je m'habille</b></td><td>ik kleed me aan</td><td>Wederkerend werkwoord <i>s'habiller</i></td></tr>
        <tr><td><b>je pars</b></td><td>ik vertrek / ga weg</td><td>Werkwoord <i>partir</i></td></tr>
        <tr><td><b>je prends le bus</b></td><td>ik neem de bus</td><td>Werkwoord <i>prendre</i></td></tr>
        <tr><td><b>je rentre</b></td><td>ik ga naar huis</td><td>Werkwoord <i>rentrer</i></td></tr>
        <tr><td><b>je me couche</b></td><td>ik ga naar bed</td><td>Wederkerend werkwoord <i>se coucher</i></td></tr>
        <tr><td><b>arriver en retard</b></td><td>te laat komen</td><td><i>Je déteste arriver en retard.</i></td></tr>
        <tr><td><b>j'en ai assez</b></td><td>ik heb er genoeg van</td><td>Vaste spreektaaluitdrukking</td></tr>
        <tr><td><b>assieds-toi</b></td><td>ga zitten</td><td>Gebiedende wijs van <i>s'asseoir</i></td></tr>
      </tbody>
    </table>

    <h4>2. De Franse klok (Quelle heure est-il?)</h4>
    <div class="formule-box">
      • <b>midi</b> = 12:00 uur 's middags | <b>minuit</b> = 12:00 uur 's nachts (00:00)<br>
      • <b>à une heure</b> = om één uur<br>
      • <b>une heure et quart</b> = kwart over een (1:15)<br>
      • <b>une heure et demie</b> = half twee (1:30 — let op: letterlijk 'één uur en een half'!)<br>
      • <b>deux heures moins le quart</b> = kwart voor twee (1:45)<br>
      • <b>jusqu'à</b> = tot (<i>jusqu'à cinq heures</i>)
    </div>

    <h4>3. School en studie (Blok F)</h4>
    <ul>
      <li><b>la note</b> = het cijfer (<i>J'ai eu une bonne note en maths!</i>)</li>
      <li><b>la récré</b> (la récréation) = de schoolpauze</li>
      <li><b>poser une question</b> = een vraag stellen</li>
      <li><b>la vitesse</b> = de snelheid | <b>la pluie</b> = de regen | <b>la porte</b> = de deur</li>
      <li><b>tomber</b> = vallen | <b>revenir</b> = terugkomen | <b>perdre</b> = verliezen</li>
      <li><b>quelques</b> = enkele | <b>en plus</b> = bovendien | <b>moyenne</b> = gemiddeld</li>
    </ul>
""",
        "vragen": [
            {
                "type": "mc",
                "vraag": "Hoe laat is het in het Frans als iemand zegt: <b>'une heure et demie'</b>?",
                "opties": [
                    "half twee (1:30)",
                    "half een (12:30)",
                    "kwart over een (1:15)",
                    "kwart voor twee (1:45)"
                ],
                "antwoord": 0,
                "uitleg": "'Une heure et demie' betekent letterlijk 'één uur en een half', oftewel half twee (1:30)."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de Franse uitdrukking <b>'arriver en retard'</b>?",
                "opties": [
                    "op tijd aankomen",
                    "te laat komen",
                    "vroeg vertrekken",
                    "de weg kwijtraken"
                ],
                "antwoord": 1,
                "uitleg": "'Arriver en retard' betekent te laat komen."
            },
            {
                "type": "mc",
                "vraag": "Welk tijdstip geeft het Franse woord <b>'midi'</b> aan?",
                "opties": [
                    "zes uur 's ochtends",
                    "twaalf uur 's nachts",
                    "twaalf uur 's middags",
                    "middernacht"
                ],
                "antwoord": 2,
                "uitleg": "'Midi' is twaalf uur overdag ('s middags). Twaalf uur 's nachts is 'minuit'."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'la récré'</b> op school?",
                "opties": [
                    "het huiswerk",
                    "het examen",
                    "de gymles",
                    "de schoolpauze"
                ],
                "antwoord": 3,
                "uitleg": "'La récré' (afkorting van la récréation) is de schoolpauze."
            },
            {
                "type": "waaronwaar",
                "vraag": "De Franse zin 'je me couche' betekent 'ik sta 's ochtends op'.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Je me couche' betekent ik ga naar bed. Opstaan is 'je me lève'."
            },
            {
                "type": "waaronwaar",
                "vraag": "De uitdrukking 'j'en ai assez' betekent in het Nederlands 'ik heb er genoeg van'.",
                "antwoord": True,
                "uitleg": "Waar! 'J'en ai assez' drukt uit dat je ergens helemaal klaar mee bent."
            },
            {
                "type": "waaronwaar",
                "vraag": "In het Frans betekent 'poser une question' letterlijk 'een antwoord geven'.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Poser une question' betekent een vraag stellen."
            },
            {
                "type": "invoer",
                "vraag": "Vertaal de routinehandeling tussen haakjes: 'Le matin, (ik kleed me aan) rapidement.' Vul de Franse woorden in (je m'habille):",
                "antwoord": "je m'habille|m'habille",
                "uitleg": "Aankleden is 's'habiller' ➔ 'je m'habille'."
            },
            {
                "type": "invoer",
                "vraag": "Vertaal het Franse woord voor 'het schoolcijfer' (met lidwoord, la note):",
                "antwoord": "la note|note",
                "uitleg": "Het cijfer is 'la note'."
            },
            {
                "type": "invoer",
                "vraag": "Welk Frans woord betekent '12 uur 's nachts' (middernacht)? Vul het Franse woord in (minuit):",
                "antwoord": "minuit",
                "uitleg": "Middernacht / 12 uur 's nachts is 'minuit'."
            }
        ]
    },

    # H6 §6.3
    {
        "id": "fr-u6-3",
        "hoofdstuk": 6,
        "paragraaf": "6.3",
        "titel": "Phrases-clés C & G · Jezelf voorstellen & Praten over gewoontes",
        "korteUitleg": "Gespreksvaardigheid in Unité 6 (p. 234): jezelf vlot voorstellen, vertellen over je familie en afkomst, en vertellen over je vaste gewoontes en vrienden.",
        "icoon": "🗣️",
        "kleur": "paars",
        "theorie": """
    <h3>6.3 Phrases-clés C & G: Jezelf voorstellen & Gewoontes</h3>
    <div class="info-box">
      <b>Se présenter et parler de ses habitudes:</b> Deze twee blokken (p. 234) vormen de kern van de spreek- en schrijfvaardigheid in klas 3 HAVO.
    </div>

    <h4>1. Blok C: Se présenter (Jezelf voorstellen)</h4>
    <table class="vocab-table">
      <thead><tr><th>Nederlands</th><th>Français</th></tr></thead>
      <tbody>
        <tr><td>Kun je je voorstellen?</td><td><b>Tu peux te présenter?</b></td></tr>
        <tr><td>Ik heet Leila en ik ben 16 jaar.</td><td><b>Je m'appelle Leila et j'ai 16 ans.</b></td></tr>
        <tr><td>Ik kom uit Amsterdam, in Nederland.</td><td><b>Je viens d'Amsterdam, aux Pays-Bas.</b></td></tr>
        <tr><td>Ik ben van Marokkaanse afkomst.</td><td><b>Je suis d'origine marocaine.</b></td></tr>
        <tr><td>Ik heb een zusje en een halfbroer.</td><td><b>J'ai une petite sœur et un demi-frère.</b></td></tr>
        <tr><td>Ik lijk op mijn zus, maar zij is minder serieus dan ik.</td><td><b>Je ressemble à ma sœur, mais elle est moins sérieuse que moi.</b></td></tr>
        <tr><td>Ik kan goed opschieten met mijn zusje.</td><td><b>Je m'entends bien avec ma petite sœur.</b></td></tr>
        <tr><td>Met mijn halfbroer heb ik de hele tijd ruzie.</td><td><b>Avec mon demi-frère, on se dispute tout le temps.</b></td></tr>
      </tbody>
    </table>

    <h4>2. Blok G: Parler de ses habitudes (Dagindeling & Vrienden)</h4>
    <ul>
      <li><b>Tu te lèves à quelle heure?</b> = Hoe laat sta jij op?</li>
      <li><b>Je me lève à sept heures.</b> = Ik sta om zeven uur op.</li>
      <li><b>À quelle heure, tu pars à l'école?</b> = Hoe laat ga jij naar school?</li>
      <li><b>Je pars à huit heures.</b> = Ik ga om acht uur weg.</li>
      <li><b>Qu'est-ce que tu fais après l'école?</b> = Wat doe jij na schooltijd?</li>
      <li><b>Je vais à la salle de sport.</b> = Ik ga naar de sportschool.</li>
      <li><b>Et le weekend? J'aime sortir.</b> = En in het weekend? Ik vind het leuk om uit te gaan.</li>
      <li><b>Avec qui? Avec mon meilleur copain.</b> = Met wie? Met mijn beste vriend.</li>
    </ul>

    <div class="tip-box">
      <b>Belangrijke uitdrukkingen voor toetsen:</b><br>
      • <i>ressembler à</i> = lijken op (<i>je ressemble à...</i>)<br>
      • <i>s'entendre bien avec</i> = goed opschieten met (<i>je m'entends bien avec...</i>)<br>
      • <i>se disputer</i> = ruzie maken (<i>on se dispute tout le temps</i>)
    </div>
""",
        "vragen": [
            {
                "type": "mc",
                "vraag": "Wat betekent de Franse zin <b>'Je m'entends bien avec ma sœur'</b>?",
                "opties": [
                    "Ik kan goed opschieten met mijn zus.",
                    "Ik lijk erg op mijn zus.",
                    "Ik maak vaak ruzie met mijn zus.",
                    "Mijn zus is ouder dan ik."
                ],
                "antwoord": 0,
                "uitleg": "'S'entendre bien avec' betekent goed opschieten met."
            },
            {
                "type": "mc",
                "vraag": "Hoe vraag je in het Frans hoe laat iemand 's ochtends opstaat?",
                "opties": [
                    "À quelle heure tu te couches?",
                    "Tu te lèves à quelle heure?",
                    "Quand est-ce que tu arrives?",
                    "Pourquoi tu te lèves si tard?"
                ],
                "antwoord": 1,
                "uitleg": "'Tu te lèves à quelle heure?' vraagt naar het tijdstip van opstaan."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de uitdrukking <b>'on se dispute tout le temps'</b>?",
                "opties": [
                    "we spelen altijd samen",
                    "we eten altijd tegelijk",
                    "we hebben de hele tijd ruzie",
                    "we zien elkaar bijna nooit"
                ],
                "antwoord": 2,
                "uitleg": "'On se dispute tout le temps' betekent dat men voortdurend ruzie heeft."
            },
            {
                "type": "mc",
                "vraag": "Hoe zeg je in het Frans dat je van Marokkaanse afkomst bent?",
                "opties": [
                    "J'habite au Maroc maintenant.",
                    "Je vais au Maroc en vacances.",
                    "Je parle arabe couramment.",
                    "Je suis d'origine marocaine."
                ],
                "antwoord": 3,
                "uitleg": "'Je suis d'origine marocaine' geeft de afkomst aan."
            },
            {
                "type": "waaronwaar",
                "vraag": "De Franse uitdrukking 'je ressemble à mon père' betekent 'ik stuur een brief naar mijn vader'.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Ressembler à' betekent lijken op: ik lijk op mijn vader."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Franse woord 'un demi-frère' betekent 'een halfbroer'.",
                "antwoord": True,
                "uitleg": "Waar! 'Un demi-frère' is een halfbroer."
            },
            {
                "type": "waaronwaar",
                "vraag": "De Franse zin 'J'aime sortir' betekent dat je graag thuis op je kamer blijft.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Sortir' betekent uitgaan / naar buiten gaan."
            },
            {
                "type": "invoer",
                "vraag": "Vul de juiste vorm in: 'Je ____ (lijk op) à ma mère.' Vul het Franse werkwoord in (ressemble):",
                "antwoord": "ressemble",
                "uitleg": "Lijken op is 'ressembler à' ➔ 'je ressemble'."
            },
            {
                "type": "invoer",
                "vraag": "Vertaal de Franse uitdrukking voor 'met wie': '____ qui est-ce que tu sors?' (Avec)",
                "antwoord": "Avec|avec",
                "uitleg": "Met wie = 'avec qui'."
            },
            {
                "type": "invoer",
                "vraag": "Vul het ontbrekende woord in voor 'beste': 'Je sors avec mon ____ copain.' (meilleur)",
                "antwoord": "meilleur",
                "uitleg": "Mijn beste vriend = 'mon meilleur copain'."
            }
        ]
    },

    # H6 §6.4
    {
        "id": "fr-u6-4",
        "hoofdstuk": 6,
        "paragraaf": "6.4",
        "titel": "Grammaire D & H · De vergelijkingen & Woordvolgorde in de zin",
        "korteUitleg": "Twee fundamentele grammaticaregels uit Unité 6 (p. 235): vergelijkingen maken met plus/moins/aussi...que (inclusief uitzondering meilleur que) én de Franse woordvolgorde met ontkenningen en bijwoorden.",
        "icoon": "📐",
        "kleur": "groen",
        "theorie": """
    <h3>6.4 Grammaire D & H: Vergelijkingen & Woordvolgorde</h3>
    <div class="info-box">
      <b>Grammatica Unité 6 (p. 235):</b> In deze paragraaf leer je twee essentiële grammaticale vaardigheden: dingen en mensen met elkaar vergelijken (groter dan, minder sportief dan) én hoe je een Franse zin grammaticaal correct opbouwt.
    </div>

    <h4>1. De vergelijkingen (Les comparatifs, Grammaire D)</h4>
    <p>Als je twee personen of zaken vergelijkt, gebruik je:</p>
    <ul>
      <li><b>plus + adjectif + que</b> = ...-er / meer ... dan (<i>Thomas est <b>plus grand que</b> Léo.</i>)</li>
      <li><b>moins + adjectif + que</b> = minder ... dan (<i>Léo est <b>moins grand que</b> Thomas.</i>)</li>
      <li><b>aussi + adjectif + que</b> = even ... als (<i>Léa est <b>aussi grande que</b> Sarah.</i>)</li>
    </ul>

    <div class="formule-box">
      <b>Twee cruciale regels bij de vergelijking:</b><br>
      1. <b>Accord:</b> Het bijvoeglijk naamwoord past zich altijd aan aan het onderwerp!<br>
      • <i>Paul est plus grand que Marie.</i> (mannelijk)<br>
      • <i>Marie est plus grand<b>e</b> que Paul.</i> (vrouwelijk: +e)<br>
      • <i>Mes sœurs sont plus grand<b>es</b> que moi.</i> (vrouwelijk meervoud: +es)<br><br>
      2. <b>Klinkerbotsing:</b> Vóór een klinker of stomme h verandert <i>que</i> in <b>qu'</b>!<br>
      • <i>Julie est plus âgée <b>qu'</b>Emma.</i><br><br>
      3. <b>Onregelmatige uitzondering: Beter dan = MEILLEUR QUE!</b><br>
      Zeg nooit 'plus bon que'! Gebruik altijd <b>meilleur que</b> (vrouwelijk: <b>meilleure que</b>):<br>
      • <i>Mbappé est <b>meilleur que</b> Neymar.</i><br>
      • <i>Ma note est <b>meilleure que</b> ta note.</i>
    </div>

    <h4>2. De Franse woordvolgorde (L'ordre des mots, Grammaire H)</h4>
    <p>In een gewone Franse zin met twee werkwoorden (zoals <i>aller + infinitif</i> of <i>passé composé</i>) <b>blijven de werkwoorden altijd bij elkaar</b>:</p>
    <ul>
      <li><i>Je vais acheter un T-shirt.</i> (Niet: 'Je vais un T-shirt acheter'!)</li>
      <li><i>J'ai acheté un T-shirt hier.</i></li>
    </ul>

    <p><b>De ontkenning omarmt het eerste werkwoord (de persoonsvorm):</b></p>
    <ul>
      <li><i>Je <b>ne</b> vais <b>pas</b> en France.</i> | <i>Il <b>n'</b>est <b>jamais</b> allé en France.</i></li>
    </ul>

    <p><b>Vaste bijwoorden staan direct na de persoonsvorm:</b></p>
    <p>Woorden zoals <b>toujours</b> (altijd), <b>souvent</b> (vaak), <b>déjà</b> (al), <b>encore</b> (nog), <b>bien</b> (goed), <b>mal</b> (slecht) en <b>beaucoup</b> (veel) staan direct achter de persoonsvorm:</p>
    <ul>
      <li><i>J'aide <b>toujours</b> mes amis.</i> (Ik help altijd mijn vrienden.)</li>
      <li><i>Je suis <b>souvent</b> allé à Paris.</i> (Ik ben vaak naar Parijs gegaan.)</li>
    </ul>
""",
        "vragen": [
            {
                "type": "mc",
                "vraag": "Kies de juiste Franse vertaling voor 'Thomas is sportiever dan Léo':",
                "opties": [
                    "Thomas est plus sportif que Léo.",
                    "Thomas est moins sportif que Léo.",
                    "Thomas est aussi sportif que Léo.",
                    "Thomas est meilleur sportif que Léo."
                ],
                "antwoord": 0,
                "uitleg": "'Sportiever dan' vertaal je met 'plus sportif que'."
            },
            {
                "type": "mc",
                "vraag": "Welke vorm is grammaticaal JUIST voor 'beter dan' in het Frans?",
                "opties": [
                    "plus bon que",
                    "meilleur que",
                    "plus bien que",
                    "aussi bien que"
                ],
                "antwoord": 1,
                "uitleg": "'Beter dan' is de vaste onregelmatige vorm 'meilleur que' (nooit 'plus bon que')."
            },
            {
                "type": "mc",
                "vraag": "Wat gebeurt er met 'que' vóór een klinker zoals in de naam Antoine?",
                "opties": [
                    "het blijft gewoon 'que'",
                    "het verandert in 'qui'",
                    "het trekt samen tot 'qu''",
                    "het verandert in 'dont'"
                ],
                "antwoord": 2,
                "uitleg": "Vóór een klinker verandert 'que' in 'qu'' (bijv. plus grand qu'Antoine)."
            },
            {
                "type": "mc",
                "vraag": "Welke zin heeft de JUISTE Franse woordvolgorde met een bijwoord?",
                "opties": [
                    "J'aide mes amis toujours.",
                    "Toujours j'aide mes amis.",
                    "J'aide mes toujours amis.",
                    "J'aide toujours mes amis."
                ],
                "antwoord": 3,
                "uitleg": "Bijwoorden zoals 'toujours' staan direct na de persoonsvorm: 'J'aide toujours mes amis'."
            },
            {
                "type": "waaronwaar",
                "vraag": "In de zin 'Pauline est plus grande que Paul' krijgt 'grande' een extra -e omdat Pauline vrouwelijk is.",
                "antwoord": True,
                "uitleg": "Waar! Het bijvoeglijk naamwoord past zich altijd in geslacht en getal aan aan het onderwerp."
            },
            {
                "type": "waaronwaar",
                "vraag": "De uitdrukking 'aussi grand que' betekent 'minder groot dan'.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Aussi ... que' betekent 'even ... als' (even groot als)."
            },
            {
                "type": "waaronwaar",
                "vraag": "In een Franse ontkenning zoals 'je ne vais pas en France' staat 'ne ... pas' om de persoonsvorm.",
                "antwoord": True,
                "uitleg": "Waar! De persoonsvorm (vais) wordt omarmd door 'ne' en 'pas'."
            },
            {
                "type": "invoer",
                "vraag": "Vertaal het woord voor 'minder' in een vergelijking: 'Léo est ____ (minder) rapide que son frère.' (moins)",
                "antwoord": "moins",
                "uitleg": "Minder ... dan is 'moins ... que'."
            },
            {
                "type": "invoer",
                "vraag": "Vertaal 'even / net zo': 'Sarah est ____ (net zo) intelligente que sa sœur.' (aussi)",
                "antwoord": "aussi",
                "uitleg": "Even / net zo ... als is 'aussi ... que'."
            },
            {
                "type": "invoer",
                "vraag": "Vul de juiste vrouwelijke vorm in van 'beter': 'Sa note est ____ (beter) que la mienne.' (meilleure)",
                "antwoord": "meilleure",
                "uitleg": "De vrouwelijke vorm van 'meilleur' is 'meilleure'."
            }
        ]
    }
]

EXAMENS = [
    # Toets 1 (ex-h3-frans-u6-v1)
    {
        "id": "ex-h3-frans-u6-v1",
        "hoofdstuk": 6,
        "hoofdstukTitel": "Unité 6 — C'est moi!",
        "titel": "Woordenschat 1 · C'est moi: Identiteit, media & karakter (Vocabulaire A & B)",
        "duurMin": 20,
        "vak": "Frans · HAVO 3 (U6)",
        "icoon": "👤",
        "vragen": [
            # 12 MC: 3x0, 3x1, 3x2, 3x3
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse zelfstandig naamwoord <b>'l'émission'</b> (v)?",
                "opties": [
                    "de uitzending",
                    "de bioscoopfilm",
                    "de krant",
                    "het interview"
                ],
                "antwoord": 0,
                "uitleg": "'L'émission' is de televisie- of radiouitzending."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het bijvoeglijk naamwoord <b>'courageux'</b>?",
                "opties": [
                    "verlegen",
                    "moedig",
                    "lui",
                    "onvriendelijk"
                ],
                "antwoord": 1,
                "uitleg": "'Courageux' betekent moedig."
            },
            {
                "type": "mc",
                "vraag": "Wat is de betekenis van het Franse zelfstandig naamwoord <b>'la dispute'</b>?",
                "opties": [
                    "het feest",
                    "de lezing",
                    "de ruzie",
                    "de wedstrijd"
                ],
                "antwoord": 2,
                "uitleg": "'La dispute' betekent de ruzie."
            },
            {
                "type": "mc",
                "vraag": "Welk Frans woord betekent <b>'de beroemdheid'</b>?",
                "opties": [
                    "la confiance",
                    "la banlieue",
                    "l'émission",
                    "la célébrité"
                ],
                "antwoord": 3,
                "uitleg": "'La célébrité' is de beroemdheid of ster."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'le pied'</b>?",
                "opties": [
                    "de voet",
                    "de hand",
                    "de knie",
                    "de arm"
                ],
                "antwoord": 0,
                "uitleg": "'Le pied' is de voet."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het bijvoeglijk naamwoord <b>'paresseux'</b> (vrouwelijk: paresseuse)?",
                "opties": [
                    "sportief",
                    "lui",
                    "aardig",
                    "streng"
                ],
                "antwoord": 1,
                "uitleg": "'Paresseux' betekent lui."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'la voix'</b>?",
                "opties": [
                    "het gezicht",
                    "het oor",
                    "de stem",
                    "de mond"
                ],
                "antwoord": 2,
                "uitleg": "'La voix' is de stem."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de schoolterm <b>'le bac'</b> in Frankrijk?",
                "opties": [
                    "de herkansing",
                    "de studiekeuze",
                    "het lesuur",
                    "het eindexamen"
                ],
                "antwoord": 3,
                "uitleg": "'Le bac' is het Franse eindexamen."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de Franse uitdrukking <b>'avoir confiance'</b>?",
                "opties": [
                    "vertrouwen hebben",
                    "haast hebben",
                    "gelijk hebben",
                    "bang zijn"
                ],
                "antwoord": 0,
                "uitleg": "'Avoir confiance' betekent vertrouwen hebben."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse bijvoeglijk naamwoord <b>'marrant'</b>?",
                "opties": [
                    "moeilijk",
                    "grappig",
                    "saai",
                    "gevaarlijk"
                ],
                "antwoord": 1,
                "uitleg": "'Marrant' betekent grappig of lollig."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'la banlieue'</b>?",
                "opties": [
                    "het stadscentrum",
                    "het platteland",
                    "de buitenwijk",
                    "de kuststrook"
                ],
                "antwoord": 2,
                "uitleg": "'La banlieue' is de buitenwijk."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'pourtant'</b>?",
                "opties": [
                    "omdat",
                    "daarna",
                    "plotseling",
                    "toch / echter"
                ],
                "antwoord": 3,
                "uitleg": "'Pourtant' betekent toch of echter."
            },
            # 4 Waaronwaar: 2 waar, 2 onwaar
            {
                "type": "waaronwaar",
                "vraag": "De uitdrukking 'parler couramment' betekent dat iemand heel langzaam en haperend praat.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Couramment' betekent juist vloeiend."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Franse zelfstandig naamwoord 'l'adulte' kan zowel mannelijk als vrouwelijk zijn.",
                "antwoord": True,
                "uitleg": "Waar! Je zegt 'un adulte' of 'une adulte'."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Franse woord 'le mot' betekent 'de zin'.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Le mot' is het woord. De zin is 'la phrase'."
            },
            {
                "type": "waaronwaar",
                "vraag": "De Franse wens 'Bonne chance!' betekent 'Veel succes!'.",
                "antwoord": True,
                "uitleg": "Waar! 'Bonne chance' wens je iemand die succes nodig heeft."
            },
            # 2 Invul
            {
                "type": "invul",
                "vraag": "Vertaal het woord voor 'het werk' in het Frans (mannelijk met lidwoord, le travail):",
                "antwoord": "le travail|travail",
                "uitleg": "Het werk is 'le travail'."
            },
            {
                "type": "invul",
                "vraag": "Vertaal het werkwoord tussen haakjes: 'Il a décidé de (stoppen) avec le football.' Vul het Franse werkwoord in (arrêter):",
                "antwoord": "arrêter|arreter",
                "uitleg": "Stoppen is 'arrêter'."
            },
            # 2 Open
            {
                "type": "open",
                "vraag": "Noem twee Franse bijvoeglijk naamwoorden uit de woordenlijst van Unité 6 die een positieve of grappige karaktereigenschap beschrijven.",
                "modelantwoord": "Twee voorbeelden zijn courageux, marrant of mignon.",
                "sleutelwoorden": [
                    "courageux/marrant/mignon",
                    "marrant/courageux/mignon"
                ],
                "minTreffers": 1,
                "uitleg": "Positieve karakterwoorden zijn bijvoorbeeld courageux (moedig), marrant (grappig) en mignon (schattig/lief)."
            },
            {
                "type": "open",
                "vraag": "Welke twee Franse werkwoorden uit Blok B betekenen respectievelijk 'weigeren' en 'verlaten'?",
                "modelantwoord": "Dat zijn refuser en quitter.",
                "sleutelwoorden": [
                    "refuser",
                    "quitter"
                ],
                "minTreffers": 2,
                "uitleg": "De werkwoorden zijn refuser (weigeren) en quitter (verlaten)."
            }
        ]
    },

    # Toets 2 (ex-h3-frans-u6-v2)
    {
        "id": "ex-h3-frans-u6-v2",
        "hoofdstuk": 6,
        "hoofdstukTitel": "Unité 6 — C'est moi!",
        "titel": "Woordenschat 2 · C'est moi: Dagindeling, klokkijken & school (Vocabulaire E & F)",
        "duurMin": 20,
        "vak": "Frans · HAVO 3 (U6)",
        "icoon": "⏰",
        "vragen": [
            # 12 MC: 3x0, 3x1, 3x2, 3x3
            {
                "type": "mc",
                "vraag": "Wat betekent de Franse zin <b>'Je me lève à sept heures'</b>?",
                "opties": [
                    "Ik sta om zeven uur op.",
                    "Ik ga om zeven uur naar bed.",
                    "Ik ontbijt om zeven uur.",
                    "Ik vertrek om zeven uur."
                ],
                "antwoord": 0,
                "uitleg": "'Je me lève' betekent ik sta op."
            },
            {
                "type": "mc",
                "vraag": "Hoe laat is het als de Franse klok <b>'midi'</b> aangeeft?",
                "opties": [
                    "twaalf uur 's nachts",
                    "twaalf uur 's middags",
                    "zes uur 's ochtends",
                    "drie uur 's middags"
                ],
                "antwoord": 1,
                "uitleg": "'Midi' is 12:00 uur 's middags."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse tijdstip <b>'deux heures moins le quart'</b>?",
                "opties": [
                    "kwart over twee (2:15)",
                    "half twee (1:30)",
                    "kwart voor twee (1:45)",
                    "twee uur precies (2:00)"
                ],
                "antwoord": 2,
                "uitleg": "'Moins le quart' betekent kwart voor."
            },
            {
                "type": "mc",
                "vraag": "Wat houdt de uitdrukking <b>'arriver en retard'</b> in als je naar school gaat?",
                "opties": [
                    "te vroeg zijn",
                    "op tijd arriveren",
                    "niet komen opdagen",
                    "te laat komen"
                ],
                "antwoord": 3,
                "uitleg": "'En retard' betekent te laat."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'la récré'</b>?",
                "opties": [
                    "de schoolpauze",
                    "het eindexamen",
                    "de huiswerkopdracht",
                    "de kantine"
                ],
                "antwoord": 0,
                "uitleg": "'La récré' is de schoolpauze."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de Franse uitdrukking <b>'j'en ai assez'</b>?",
                "opties": [
                    "ik heb nog dorst",
                    "ik heb er genoeg van",
                    "ik wil nog meer",
                    "ik weet het niet zeker"
                ],
                "antwoord": 1,
                "uitleg": "'J'en ai assez' betekent ik heb er genoeg van."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'la note'</b> op school?",
                "opties": [
                    "het schrift",
                    "de aantekening",
                    "het rapportcijfer",
                    "de bel"
                ],
                "antwoord": 2,
                "uitleg": "'La note' is het cijfer."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de Franse opdracht <b>'assieds-toi'</b>?",
                "opties": [
                    "sta op",
                    "wees stil",
                    "kom binnen",
                    "ga zitten"
                ],
                "antwoord": 3,
                "uitleg": "'Assieds-toi' betekent ga zitten."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het tijdstip <b>'une heure et quart'</b>?",
                "opties": [
                    "kwart over een (1:15)",
                    "kwart voor een (12:45)",
                    "half twee (1:30)",
                    "drie kwartier"
                ],
                "antwoord": 0,
                "uitleg": "'Et quart' betekent kwart over: kwart over een."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de Franse zin <b>'je me couche'</b>?",
                "opties": [
                    "ik sta op",
                    "ik ga naar bed",
                    "ik kleed me om",
                    "ik poets mijn tanden"
                ],
                "antwoord": 1,
                "uitleg": "'Je me couche' betekent ik ga naar bed / slapen."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de Franse uitdrukking <b>'poser une question'</b>?",
                "opties": [
                    "een vraag beantwoorden",
                    "een toets maken",
                    "een vraag stellen",
                    "een vraag overslaan"
                ],
                "antwoord": 2,
                "uitleg": "'Poser une question' betekent een vraag stellen."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'les cheveux'</b> (m mv)?",
                "opties": [
                    "de ogen",
                    "de oren",
                    "de tanden",
                    "het haar"
                ],
                "antwoord": 3,
                "uitleg": "'Les cheveux' betekent het haar."
            },
            # 4 Waaronwaar: 2 waar, 2 onwaar
            {
                "type": "waaronwaar",
                "vraag": "De tijd 'une heure et demie' betekent in het Nederlands 'half twee' (1:30).",
                "antwoord": True,
                "uitleg": "Waar! Letterlijk één uur en een half, dus 1:30 (half twee)."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Franse woord 'minuit' betekent 12 uur 's middags.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Minuit' is 12 uur 's nachts (middernacht). 12 uur 's middags is 'midi'."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Franse woord 'la pluie' betekent 'de zonneschijn'.",
                "antwoord": False,
                "uitleg": "Onwaar! 'La pluie' is de regen."
            },
            {
                "type": "waaronwaar",
                "vraag": "De zin 'je rentre' betekent dat je op weg bent naar huis.",
                "antwoord": True,
                "uitleg": "Waar! 'Rentrer' betekent naar huis gaan."
            },
            # 2 Invul
            {
                "type": "invul",
                "vraag": "Vul de juiste tijdsuitdrukking in voor 'tot': 'Je travaille ____ (tot) six heures.' (jusqu'à)",
                "antwoord": "jusqu'à|jusqu'a|jusqua",
                "uitleg": "Tot is 'jusqu'à'."
            },
            {
                "type": "invul",
                "vraag": "Vertaal het woord tussen haakjes: 'Elle est très (moe) après les cours.' Vul het Franse woord in (fatiguée):",
                "antwoord": "fatiguée|fatiguee",
                "uitleg": "Moe voor een vrouwelijk onderwerp is 'fatiguée'."
            },
            # 2 Open
            {
                "type": "open",
                "vraag": "Geef de twee Franse benamingen voor exact twaalf uur overdag en exact twaalf uur 's nachts.",
                "modelantwoord": "Dat zijn midi voor overdag en minuit voor 's nachts.",
                "sleutelwoorden": [
                    "midi",
                    "minuit"
                ],
                "minTreffers": 2,
                "uitleg": "Twaalf uur overdag is midi, en twaalf uur 's nachts is minuit."
            },
            {
                "type": "open",
                "vraag": "Welke twee Franse werkwoorden uit Blok E geven respectievelijk aan dat je opstaat uit bed en dat je 's avonds naar bed gaat?",
                "modelantwoord": "Dat zijn se lever (je me lève) en se coucher (je me couche).",
                "sleutelwoorden": [
                    "lever/lève/leve",
                    "coucher/couche"
                ],
                "minTreffers": 2,
                "uitleg": "Opstaan is se lever (je me lève) en naar bed gaan is se coucher (je me couche)."
            }
        ]
    },

    # Toets 3 (ex-h3-frans-u6-v3)
    {
        "id": "ex-h3-frans-u6-v3",
        "hoofdstuk": 6,
        "hoofdstukTitel": "Unité 6 — C'est moi!",
        "titel": "Woordenschat 3 · C'est moi: Jezelf voorstellen & Gewoontes (Phrases-clés C & G)",
        "duurMin": 20,
        "vak": "Frans · HAVO 3 (U6)",
        "icoon": "🗣️",
        "vragen": [
            # 12 MC: 3x0, 3x1, 3x2, 3x3
            {
                "type": "mc",
                "vraag": "Wat betekent de vraag <b>'Tu peux te présenter?'</b>?",
                "opties": [
                    "Kun je je voorstellen?",
                    "Kun je me helpen?",
                    "Wil je iets drinken?",
                    "Hoe laat vertrek je?"
                ],
                "antwoord": 0,
                "uitleg": "'Tu peux te présenter?' betekent kun je je voorstellen."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de Franse zin <b>'Je ressemble à ma sœur'</b>?",
                "opties": [
                    "Ik praat met mijn zus.",
                    "Ik lijk op mijn zus.",
                    "Ik wacht op mijn zus.",
                    "Ik help mijn zus."
                ],
                "antwoord": 1,
                "uitleg": "'Ressembler à' betekent lijken op."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de Franse uitdrukking <b>'un demi-frère'</b>?",
                "opties": [
                    "een tweelingbroer",
                    "een neef",
                    "een halfbroer",
                    "een stiefvader"
                ],
                "antwoord": 2,
                "uitleg": "'Un demi-frère' is een halfbroer."
            },
            {
                "type": "mc",
                "vraag": "Hoe zeg je in het Frans dat je goed kunt opschieten met iemand?",
                "opties": [
                    "Je me dispute avec lui.",
                    "Je ne le connais pas.",
                    "Je suis jaloux de lui.",
                    "Je m'entends bien avec lui."
                ],
                "antwoord": 3,
                "uitleg": "'Je m'entends bien avec' betekent ik kan goed opschieten met."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de zin <b>'Avec mon demi-frère, on se dispute tout le temps'</b>?",
                "opties": [
                    "Met mijn halfbroer maak ik de hele tijd ruzie.",
                    "Mijn halfbroer helpt me altijd met huiswerk.",
                    "Ik ga elke dag naar mijn halfbroer toe.",
                    "Mijn halfbroer is twee jaar jonger dan ik."
                ],
                "antwoord": 0,
                "uitleg": "'On se dispute tout le temps' betekent we hebben de hele tijd ruzie."
            },
            {
                "type": "mc",
                "vraag": "Wat vraag je als je wilt weten hoe laat iemand naar school vertrekt?",
                "opties": [
                    "Tu aimes ton école?",
                    "À quelle heure, tu pars à l'école?",
                    "Comment tu vas au collège?",
                    "Pourquoi tu restes à l'école?"
                ],
                "antwoord": 1,
                "uitleg": "'À quelle heure, tu pars à l'école?' vraagt naar het vertrektijdstip."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de vraag <b>'Qu'est-ce que tu fais après l'école?'</b>?",
                "opties": [
                    "Hoe laat begint de school?",
                    "Welke lessen heb je vandaag?",
                    "Wat doe jij na schooltijd?",
                    "Waarom ga je niet naar school?"
                ],
                "antwoord": 2,
                "uitleg": "'Après l'école' betekent na schooltijd."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de Franse bestemming <b>'la salle de sport'</b>?",
                "opties": [
                    "het zwembad",
                    "het voetbalveld",
                    "de kantine",
                    "de sportschool"
                ],
                "antwoord": 3,
                "uitleg": "'La salle de sport' is de sportschool of fitnesszaal."
            },
            {
                "type": "mc",
                "vraag": "Hoe zeg je in het Frans dat je van plan bent om uit te gaan in het weekend?",
                "opties": [
                    "J'aime sortir.",
                    "Je reste à la maison.",
                    "Je me couche tôt.",
                    "Je range ma chambre."
                ],
                "antwoord": 0,
                "uitleg": "'J'aime sortir' betekent ik ga graag uit."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de Franse uitdrukking <b>'mon meilleur copain'</b>?",
                "opties": [
                    "mijn broer",
                    "mijn beste vriend",
                    "mijn buurjongen",
                    "mijn klasgenoot"
                ],
                "antwoord": 1,
                "uitleg": "'Mon meilleur copain' is mijn beste vriend."
            },
            {
                "type": "mc",
                "vraag": "Hoe zeg je in het Frans dat je 16 jaar bent?",
                "opties": [
                    "Je suis seize ans.",
                    "J'habite seize ans.",
                    "J'ai 16 ans.",
                    "Je fais seize ans."
                ],
                "antwoord": 2,
                "uitleg": "Leeftijd druk je uit met avoir: 'J'ai 16 ans'."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de Franse zin <b>'Je viens d'Amsterdam, aux Pays-Bas'</b>?",
                "opties": [
                    "Ik ga op reis naar Amsterdam.",
                    "Ik werk in Amsterdam.",
                    "Ik studeer in Amsterdam.",
                    "Ik kom uit Amsterdam, in Nederland."
                ],
                "antwoord": 3,
                "uitleg": "'Je viens d'Amsterdam' betekent ik kom uit Amsterdam."
            },
            # 4 Waaronwaar: 2 waar, 2 onwaar
            {
                "type": "waaronwaar",
                "vraag": "De Franse zin 'Elle est moins sérieuse que moi' betekent dat zij serieuzer is dan ik.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Moins ... que' betekent minder ... dan (zij is minder serieus dan ik)."
            },
            {
                "type": "waaronwaar",
                "vraag": "In het Frans zeg je 'Je suis d'origine marocaine' om je afkomst aan te duiden.",
                "antwoord": True,
                "uitleg": "Waar! 'Être d'origine...' betekent van ... afkomst zijn."
            },
            {
                "type": "waaronwaar",
                "vraag": "De vraag 'Avec qui?' betekent in het Nederlands 'Waarheen?'.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Avec qui?' betekent 'Met wie?'. Waarheen is 'Où?'."
            },
            {
                "type": "waaronwaar",
                "vraag": "De uitdrukking 'une petite sœur' betekent in het Frans een jonger zusje.",
                "antwoord": True,
                "uitleg": "Waar! 'Une petite sœur' is een jonger zusje."
            },
            # 2 Invul
            {
                "type": "invul",
                "vraag": "Vertaal het woord voor 'halfbroer' in het Frans (met lidwoord, un demi-frère):",
                "antwoord": "un demi-frère|un demi-frere|demi-frère|demi-frere",
                "uitleg": "Een halfbroer is 'un demi-frère'."
            },
            {
                "type": "invul",
                "vraag": "Vul de juiste vorm van het werkwoord in: 'Je m'____ (kan goed opschieten) bien avec ma sœur.' (entends)",
                "antwoord": "entends",
                "uitleg": "Goed opschieten met = 's'entendre bien avec' ➔ 'je m'entends'."
            },
            # 2 Open
            {
                "type": "open",
                "vraag": "Hoe vraag je in het Frans aan iemand hoe laat hij of zij 's ochtends opstaat?",
                "modelantwoord": "Dat vraag je met: Tu te lèves à quelle heure?",
                "sleutelwoorden": [
                    "lèves/leves",
                    "heure"
                ],
                "minTreffers": 2,
                "uitleg": "De vraag luidt: 'Tu te lèves à quelle heure?'."
            },
            {
                "type": "open",
                "vraag": "Noem de Franse zin waarmee je aangeeft dat je goed kunt opschieten met je jongere zusje.",
                "modelantwoord": "Dat zeg je met: Je m'entends bien avec ma petite sœur.",
                "sleutelwoorden": [
                    "entends bien",
                    "petite sœur/petite soeur/sœur/soeur"
                ],
                "minTreffers": 2,
                "uitleg": "De zin is: 'Je m'entends bien avec ma petite sœur.'."
            }
        ]
    },

    # Toets 4 (ex-h3-frans-u6-v4)
    {
        "id": "ex-h3-frans-u6-v4",
        "hoofdstuk": 6,
        "hoofdstukTitel": "Unité 6 — C'est moi!",
        "titel": "Grammatica 4 · C'est moi: De vergelijkingen (plus, moins, aussi, meilleur ... que)",
        "duurMin": 20,
        "vak": "Frans · HAVO 3 (U6)",
        "icoon": "📐",
        "vragen": [
            # 12 MC: 3x0, 3x1, 3x2, 3x3
            {
                "type": "mc",
                "vraag": "Kies de juiste vorm voor 'groter dan' bij een mannelijk onderwerp: 'Paul est ____ (groter dan) Pierre.'",
                "opties": [
                    "plus grand que",
                    "plus grande que",
                    "aussi grand que",
                    "meilleur que"
                ],
                "antwoord": 0,
                "uitleg": "'Paul' is mannelijk, dus 'plus grand que'."
            },
            {
                "type": "mc",
                "vraag": "Kies de juiste vorm voor een vrouwelijk onderwerp: 'Pauline est ____ (kleiner dan) Thomas.'",
                "opties": [
                    "plus petit que",
                    "plus petite que",
                    "aussi petit que",
                    "moins petit que"
                ],
                "antwoord": 1,
                "uitleg": "'Pauline' is vrouwelijk, dus het adjectief krijgt een extra -e: 'plus petite que'."
            },
            {
                "type": "mc",
                "vraag": "Wat is de juiste Franse vertaling voor 'minder sportief dan'?",
                "opties": [
                    "plus sportif que",
                    "aussi sportif que",
                    "moins sportif que",
                    "meilleur sportif que"
                ],
                "antwoord": 2,
                "uitleg": "'Minder ... dan' vertaal je met 'moins ... que'."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de constructie <b>'aussi grand que'</b>?",
                "opties": [
                    "veel groter dan",
                    "minder groot dan",
                    "beter dan",
                    "even groot als"
                ],
                "antwoord": 3,
                "uitleg": "'Aussi ... que' betekent 'even ... als / net zo ... als'."
            },
            {
                "type": "mc",
                "vraag": "Wat is de Franse vertaling van 'beter dan' (nooit 'plus bon que')?",
                "opties": [
                    "meilleur que",
                    "plus bon que",
                    "plus meilleur que",
                    "aussi bon que"
                ],
                "antwoord": 0,
                "uitleg": "'Beter dan' is de onregelmatige vorm 'meilleur que'."
            },
            {
                "type": "mc",
                "vraag": "Kies de juiste vrouwelijke vorm van 'beter dan': 'Sa moyenne est ____ (beter dan) la mienne.'",
                "opties": [
                    "meilleur que",
                    "meilleure que",
                    "plus bonne que",
                    "aussi bonne que"
                ],
                "antwoord": 1,
                "uitleg": "'Moyenne' is vrouwelijk, dus 'meilleure que'."
            },
            {
                "type": "mc",
                "vraag": "Wat gebeurt er met 'que' voor een klinker zoals in 'Alexandre'?",
                "opties": [
                    "het wordt 'qui'",
                    "het blijft 'que'",
                    "het wordt 'qu''",
                    "het valt helemaal weg"
                ],
                "antwoord": 2,
                "uitleg": "Voor een klinker trekt 'que' samen tot 'qu'' (bijv. plus grand qu'Alexandre)."
            },
            {
                "type": "mc",
                "vraag": "Kies de juiste vorm voor vrouwelijk meervoud: 'Ces filles sont ____ (actiever dan) les garçons.'",
                "opties": [
                    "plus actif que",
                    "plus active que",
                    "plus actifs que",
                    "plus actives que"
                ],
                "antwoord": 3,
                "uitleg": "'Ces filles' is vrouwelijk meervoud, dus 'plus actives que'."
            },
            {
                "type": "mc",
                "vraag": "Welk woord ontbreekt in de vergelijking: 'Thomas est plus fort ____ son frère.'?",
                "opties": [
                    "que",
                    "qui",
                    "de",
                    "comme"
                ],
                "antwoord": 0,
                "uitleg": "In een vergelijking gebruik je 'que' (plus fort que)."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de zin <b>'Julie est aussi intelligente que Léa'</b>?",
                "opties": [
                    "Julie is veel slimmer dan Léa.",
                    "Julie is net zo intelligent als Léa.",
                    "Julie is minder slim dan Léa.",
                    "Julie is de allerslimste."
                ],
                "antwoord": 1,
                "uitleg": "'Aussi ... que' betekent net zo / even ... als."
            },
            {
                "type": "mc",
                "vraag": "Kies de juiste vorm: 'Mon frère est moins ____ (serieus) que moi.'",
                "opties": [
                    "sérieuse",
                    "sérieuses",
                    "sérieux",
                    "sérieusement"
                ],
                "antwoord": 2,
                "uitleg": "'Mon frère' is mannelijk enkelvoud, dus 'sérieux'."
            },
            {
                "type": "mc",
                "vraag": "Wat is er fout aan de zin 'Ce plat est plus bon que l'autre'?",
                "opties": [
                    "Plat moet vrouwelijk zijn.",
                    "Het werkwoord 'est' klopt niet.",
                    "De ontkenning ontbreekt.",
                    "'Plus bon que' bestaat niet; het moet 'meilleur que' zijn."
                ],
                "antwoord": 3,
                "uitleg": "'Plus bon que' is foutief Frans; de juiste vorm is 'meilleur que'."
            },
            # 4 Waaronwaar: 2 waar, 2 onwaar
            {
                "type": "waaronwaar",
                "vraag": "Het bijvoeglijk naamwoord in een vergelijking past zich altijd aan het onderwerp aan.",
                "antwoord": True,
                "uitleg": "Waar! Bijv. 'Pauline est plus grande' (+e wegens vrouwelijk onderwerp)."
            },
            {
                "type": "waaronwaar",
                "vraag": "De uitdrukking 'plus petit que' betekent 'groter dan'.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Petit' betekent klein, dus 'kleiner dan'. Groter dan is 'plus grand que'."
            },
            {
                "type": "waaronwaar",
                "vraag": "In het Frans schrijf je 'plus grand que Emma' zonder apostrof.",
                "antwoord": False,
                "uitleg": "Onwaar! Vóór een klinker trekt que verplicht samen tot qu': 'qu'Emma'."
            },
            {
                "type": "waaronwaar",
                "vraag": "De meervoudsvorm van 'meilleur' voor mannelijk meervoud is 'meilleurs'.",
                "antwoord": True,
                "uitleg": "Waar! In het meervoud krijgt meilleur een -s: 'meilleurs'."
            },
            # 2 Invul
            {
                "type": "invul",
                "vraag": "Vul het juiste woord in voor 'meer / -er': 'Lucas est ____ (groter/meer) grand que son cousin.' (plus)",
                "antwoord": "plus",
                "uitleg": "Meer ... dan is 'plus ... que'."
            },
            {
                "type": "invul",
                "vraag": "Vul de juiste vorm van 'meilleur' in voor een mannelijk onderwerp: 'Ce film est ____ (beter) que le livre.' (meilleur)",
                "antwoord": "meilleur",
                "uitleg": "Beter dan is 'meilleur que'."
            },
            # 2 Open
            {
                "type": "open",
                "vraag": "Noem de drie Franse signaalwoorden waarmee je respectievelijk 'meer...dan', 'minder...dan' en 'even...als' uitdrukt vóór een adjectief.",
                "modelantwoord": "Dat zijn de woorden plus, moins en aussi (elk gevolgd door que).",
                "sleutelwoorden": [
                    "plus",
                    "moins",
                    "aussi"
                ],
                "minTreffers": 3,
                "uitleg": "De drie woorden zijn plus (meer), moins (minder) en aussi (even/net zo)."
            },
            {
                "type": "open",
                "vraag": "Waarom mag je in het Frans nooit 'plus bon que' zeggen als je 'beter dan' bedoelt, en welke speciale vorm moet je altijd gebruiken?",
                "modelantwoord": "De combinatie 'plus bon que' is grammaticaal onjuist; in het Frans moet je altijd de vorm meilleur que gebruiken.",
                "sleutelwoorden": [
                    "onjuist/fout/verboden",
                    "meilleur"
                ],
                "minTreffers": 2,
                "uitleg": "In plaats van het foutieve 'plus bon que' gebruik je de vorm 'meilleur que' (beter dan)."
            }
        ]
    },

    # Toets 5 (ex-h3-frans-u6-v5)
    {
        "id": "ex-h3-frans-u6-v5",
        "hoofdstuk": 6,
        "hoofdstukTitel": "Unité 6 — C'est moi!",
        "titel": "Grammatica & Woordenschat 5 · C'est moi: Woordvolgorde & Integrale toets U6",
        "duurMin": 20,
        "vak": "Frans · HAVO 3 (U6)",
        "icoon": "📐",
        "vragen": [
            # 12 MC: 3x0, 3x1, 3x2, 3x3
            {
                "type": "mc",
                "vraag": "Waar staan in een gewone Franse zin met twee werkwoorden (zoals aller + hele werkwoord) de werkwoorden?",
                "opties": [
                    "Altijd direct bij elkaar (onderwerp + pv + infinitief)",
                    "Het hele werkwoord staat helemaal aan het einde van de zin",
                    "Het hele werkwoord staat vóór het onderwerp",
                    "De plaats maakt in het Frans niet uit"
                ],
                "antwoord": 0,
                "uitleg": "In het Frans staan de werkwoorden altijd bij elkaar (je vais acheter un livre)."
            },
            {
                "type": "mc",
                "vraag": "Waar staat het bijwoord <b>'toujours'</b> (altijd) in een Franse zin?",
                "opties": [
                    "Helemaal aan het begin van de zin",
                    "Direct na de persoonsvorm (het eerste werkwoord)",
                    "Achter het lijdend voorwerp",
                    "Altijd aan het einde van de zin"
                ],
                "antwoord": 1,
                "uitleg": "Bijwoorden zoals toujours, souvent en déjà staan direct na de persoonsvorm."
            },
            {
                "type": "mc",
                "vraag": "Welke zin heeft de JUISTE ontkenning bij een samengestelde tijd?",
                "opties": [
                    "Je ne suis allé pas en France.",
                    "Je suis pas allé en France.",
                    "Je ne suis pas allé en France.",
                    "Je suis allé ne pas en France."
                ],
                "antwoord": 2,
                "uitleg": "'Ne ... pas' omarmt de persoonsvorm (suis): 'Je ne suis pas allé'."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse bijwoord <b>'souvent'</b>?",
                "opties": [
                    "nooit",
                    "zelden",
                    "altijd",
                    "vaak"
                ],
                "antwoord": 3,
                "uitleg": "'Souvent' betekent vaak."
            },
            {
                "type": "mc",
                "vraag": "Welke zin is grammaticaal VOLKOMEN CORRECT?",
                "opties": [
                    "Demain, je vais acheter un cadeau.",
                    "Je vais un cadeau demain acheter.",
                    "Acheter je vais un cadeau demain.",
                    "Je vais demain un cadeau acheter."
                ],
                "antwoord": 0,
                "uitleg": "De werkwoorden 'vais acheter' blijven bij elkaar."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de Franse uitdrukking <b>'avoir confiance en quelqu'un'</b>?",
                "opties": [
                    "boos zijn op iemand",
                    "vertrouwen hebben in iemand",
                    "bang zijn voor iemand",
                    "iemand niet kennen"
                ],
                "antwoord": 1,
                "uitleg": "'Avoir confiance en' betekent vertrouwen hebben in iemand."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'énervant'</b>?",
                "opties": [
                    "rustgevend",
                    "grappig",
                    "irritant / ergerlijk",
                    "spannend"
                ],
                "antwoord": 2,
                "uitleg": "'Énervant' betekent irritant of op de zenuwen werkend."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de Franse zin <b>'Je me couche à dix heures'</b>?",
                "opties": [
                    "Ik sta om tien uur op.",
                    "Ik ga om tien uur douchen.",
                    "Ik begin om tien uur met leren.",
                    "Ik ga om tien uur naar bed."
                ],
                "antwoord": 3,
                "uitleg": "'Je me couche' betekent ik ga naar bed."
            },
            {
                "type": "mc",
                "vraag": "Kies de juiste vergelijking: 'Marie est ____ (sportiever dan) son frère.'",
                "opties": [
                    "plus sportive que",
                    "plus sportif que",
                    "aussi sportif que",
                    "meilleur sportive que"
                ],
                "antwoord": 0,
                "uitleg": "'Marie' is vrouwelijk, dus 'plus sportive que'."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'le travail'</b>?",
                "opties": [
                    "de vakantie",
                    "het werk",
                    "het salaris",
                    "het contract"
                ],
                "antwoord": 1,
                "uitleg": "'Le travail' is het werk."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse werkwoord <b>'quitter'</b>?",
                "opties": [
                    "beginnen",
                    "kiezen",
                    "verlaten",
                    "bezoeken"
                ],
                "antwoord": 2,
                "uitleg": "'Quitter' betekent verlaten (bijv. quitter l'école)."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de Franse uitdrukking <b>'parler couramment'</b>?",
                "opties": [
                    "met veel fouten praten",
                    "stil blijven luisteren",
                    "alleen maar korte woordjes zeggen",
                    "vloeiend en soepel spreken"
                ],
                "antwoord": 3,
                "uitleg": "'Parler couramment' betekent vloeiend en vlot een taal spreken."
            },
            # 4 Waaronwaar: 2 waar, 2 onwaar
            {
                "type": "waaronwaar",
                "vraag": "In het Frans mag je een tijdsbepaling zoals 'demain' zowel vooraan als achteraan in de zin zetten.",
                "antwoord": True,
                "uitleg": "Waar! 'Demain, je vais au collège' of 'Je vais au collège demain' zijn beide correct."
            },
            {
                "type": "waaronwaar",
                "vraag": "In een ontkennende zin staat 'pas' altijd helemaal aan het einde van de zin.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Pas' staat direct achter de persoonsvorm (bijv. 'Je ne vais pas au collège')."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Franse woord 'souvent' betekent 'nooit'.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Souvent' betekent 'vaak'. Nooit is 'jamais'."
            },
            {
                "type": "waaronwaar",
                "vraag": "De uitdrukking 'je m'habille' betekent dat je kleren aandoet.",
                "antwoord": True,
                "uitleg": "Waar! 'S'habiller' betekent zich aankleden."
            },
            # 2 Invul
            {
                "type": "invul",
                "vraag": "Vul het ontbrekende Franse bijwoord in voor 'altijd': 'Elle aide ____ (altijd) ses parents.' (toujours)",
                "antwoord": "toujours",
                "uitleg": "Altijd is 'toujours'."
            },
            {
                "type": "invul",
                "vraag": "Vertaal het woord voor 'de schoolpauze' in het Frans (met lidwoord, la récré):",
                "antwoord": "la récré|la recre|récré|recre",
                "uitleg": "De pauze is 'la récré'."
            },
            # 2 Open
            {
                "type": "open",
                "vraag": "Waar plaatsen Franstaligen bijwoorden van tijd en frequentie zoals 'souvent' (vaak) en 'toujours' (altijd) in een gewone zin?",
                "modelantwoord": "Zij plaatsen deze bijwoorden direct na de persoonsvorm (het eerste werkwoord).",
                "sleutelwoorden": [
                    "persoonsvorm/eerste werkwoord/verbo",
                    "direct/meteen/achter"
                ],
                "minTreffers": 1,
                "uitleg": "Bijwoorden zoals souvent en toujours staan direct achter de persoonsvorm in de zin."
            },
            {
                "type": "open",
                "vraag": "Leg uit op welke positie de werkwoorden staan in een Franse toekomende tijd zoals 'aller + infinitif' (bijvoorbeeld 'je vais acheter').",
                "modelantwoord": "De werkwoorden blijven altijd direct bij elkaar staan in de zin.",
                "sleutelwoorden": [
                    "elkaar/samen/aaneen",
                    "direct/naast"
                ],
                "minTreffers": 1,
                "uitleg": "In het Frans blijven de persoonsvorm en de infinitief altijd direct bij elkaar staan."
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
        idx = item['id'].replace("ex-h3-frans-u6-v", "")
        fname = f"examen_u6_vocab_{idx}.js"
        fpath = os.path.join(DATA_DIR, fname)
        code = f"/* Proeftoets {item['id']} — {item['titel']}\n   Grandes Lignes 3 HAVO Unité {item['hoofdstuk']} */\nDURU.registerExamen({json.dumps(item, indent=2, ensure_ascii=False)});\n"
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Geschreven examen: {fname}")

if __name__ == "__main__":
    generate()

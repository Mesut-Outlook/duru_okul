#!/usr/bin/env python3
"""
build_frans_u2.py — Generates Unité 2 Vocabulaire, Phrases-clés, Grammaire modules and exams
for Grandes Lignes 3 HAVO (p. 86-89):
- havo3/frans/js/data/h2_1.js (Blok A & B, p. 86)
- havo3/frans/js/data/h2_2.js (Blok E & F, p. 87)
- havo3/frans/js/data/h2_3.js (Phrases-clés C & G, p. 88)
- havo3/frans/js/data/h2_4.js (Grammaire D & H, p. 89)
- havo3/frans/js/data/examen_u2_vocab_1.js t/m 5.js (5x 20-question exams = 100 questions)
"""

import os
import json

DATA_DIR = "/home/mesuto/Documents/PROJELER/duru_okul/havo3/frans/js/data"
os.makedirs(DATA_DIR, exist_ok=True)

# ---------------------------------------------------------
# ONDERWERPEN (h2_1 t/m h2_4)
# ---------------------------------------------------------

ONDERWERPEN = [
    {
        "id": "fr-u2-1",
        "hoofdstuk": 2,
        "paragraaf": "2.1",
        "titel": "Woordenschat 2.1 · p. 86 (blok A & B) · Vrije tijd, activiteiten & routines",
        "korteUitleg": "Woorden over vrije tijd, activiteiten, uitslapen, ontspannen en dagelijkse bezigheden.",
        "icoon": "🎮",
        "kleur": "blauw",
        "theorie": """
    <h3>2.1 Woordenschat: pagina 86 (Blok A & B)</h3>
    <div class="info-box">
      <b>Leeradvies:</b> Leer de woorden uit het witte blok in <i>beide richtingen</i> (Frans ➔ Nederlands én Nederlands ➔ Frans). De woorden uit het blauwe blok hoef je alleen Frans ➔ Nederlands te kunnen herkennen.
    </div>

    <h4>Blok A: Activiteiten, ontspanning en uitdrukkingen (p. 86)</h4>
    <table class="vocab-tabel" style="width:100%;border-collapse:collapse;margin:12px 0;">
      <tr style="background:var(--blauw-licht);">
        <th style="padding:6px;border:1px solid var(--lijn);">Frans 🇫🇷</th>
        <th style="padding:6px;border:1px solid var(--lijn);">Nederlands 🇳🇱</th>
        <th style="padding:6px;border:1px solid var(--lijn);">Frans 🇫🇷</th>
        <th style="padding:6px;border:1px solid var(--lijn);">Nederlands 🇳🇱</th>
      </tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>commencer</b></td><td style="padding:6px;border:1px solid var(--lijn);">beginnen</td><td style="padding:6px;border:1px solid var(--lijn);"><b>je pourrai</b></td><td style="padding:6px;border:1px solid var(--lijn);">ik zal kunnen</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>passer</b></td><td style="padding:6px;border:1px solid var(--lijn);">doorbrengen</td><td style="padding:6px;border:1px solid var(--lijn);"><b>l'entrée (v)</b></td><td style="padding:6px;border:1px solid var(--lijn);">de ingang</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>avoir l'air</b></td><td style="padding:6px;border:1px solid var(--lijn);">eruit zien</td><td style="padding:6px;border:1px solid var(--lijn);"><b>le cours</b></td><td style="padding:6px;border:1px solid var(--lijn);">de les</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>avoir le temps (de)</b></td><td style="padding:6px;border:1px solid var(--lijn);">tijd hebben (om)</td><td style="padding:6px;border:1px solid var(--lijn);"><b>l'épisode (m)</b></td><td style="padding:6px;border:1px solid var(--lijn);">de aflevering</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>avoir envie (de)</b></td><td style="padding:6px;border:1px solid var(--lijn);">zin hebben (om)</td><td style="padding:6px;border:1px solid var(--lijn);"><b>jusqu'à</b></td><td style="padding:6px;border:1px solid var(--lijn);">tot</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>se reposer</b></td><td style="padding:6px;border:1px solid var(--lijn);">uitrusten</td><td style="padding:6px;border:1px solid var(--lijn);"><b>chez moi</b></td><td style="padding:6px;border:1px solid var(--lijn);">bij mij</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>se retrouver</b></td><td style="padding:6px;border:1px solid var(--lijn);">elkaar treffen</td><td style="padding:6px;border:1px solid var(--lijn);"><b>plutôt</b></td><td style="padding:6px;border:1px solid var(--lijn);">nogal</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>je me lève</b></td><td style="padding:6px;border:1px solid var(--lijn);">ik sta op</td><td style="padding:6px;border:1px solid var(--lijn);"><b>tard / tôt</b></td><td style="padding:6px;border:1px solid var(--lijn);">laat / vroeg</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>jouer à la console</b></td><td style="padding:6px;border:1px solid var(--lijn);">gamen</td><td style="padding:6px;border:1px solid var(--lijn);"><b>déjà</b></td><td style="padding:6px;border:1px solid var(--lijn);">al</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>discuter / rigoler</b></td><td style="padding:6px;border:1px solid var(--lijn);">kletsen / lachen</td><td style="padding:6px;border:1px solid var(--lijn);"><b>dur</b></td><td style="padding:6px;border:1px solid var(--lijn);">hard, moeilijk</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>appeler</b></td><td style="padding:6px;border:1px solid var(--lijn);">bellen</td><td style="padding:6px;border:1px solid var(--lijn);"><b>mort(e)</b></td><td style="padding:6px;border:1px solid var(--lijn);">dood</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>faire les magasins</b></td><td style="padding:6px;border:1px solid var(--lijn);">winkelen</td><td style="padding:6px;border:1px solid var(--lijn);"><b>fatigué(e)</b></td><td style="padding:6px;border:1px solid var(--lijn);">moe</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>faire du sport</b></td><td style="padding:6px;border:1px solid var(--lijn);">sporten</td><td style="padding:6px;border:1px solid var(--lijn);"><b>prochain(e)</b></td><td style="padding:6px;border:1px solid var(--lijn);">volgende</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>faire la grasse matinée</b></td><td style="padding:6px;border:1px solid var(--lijn);">uitslapen</td><td style="padding:6px;border:1px solid var(--lijn);"><b>c'était</b></td><td style="padding:6px;border:1px solid var(--lijn);">het was</td></tr>
    </table>

    <h4>Blok B: Tijd, leven en meningen (p. 86)</h4>
    <ul>
      <li><b>le début:</b> het begin | <b>la vie:</b> het leven | <b>l'argent (m):</b> het geld | <b>le temps libre:</b> de vrije tijd</li>
      <li><b>la fois:</b> de keer | <b>le jeu:</b> het spel | <b>le magazine:</b> het tijdschrift | <b>selon:</b> volgens</li>
      <li><b>aider:</b> helpen | <b>réfléchir:</b> nadenken | <b>lire:</b> lezen | <b>haut(e):</b> hoog | <b>chaque:</b> ieder</li>
      <li><b>comme:</b> als, zoals | <b>parfois:</b> soms | <b>en plus:</b> bovendien</li>
      <li><i>Blauw blok (passief):</i> <b>l'écran (m):</b> het scherm | <b>l'avis (m):</b> de mening | <b>le champion:</b> de kampioen | <b>l'entraînement (m):</b> de training | <b>il faut:</b> je moet | <b>j'avais:</b> ik had | <b>connaître:</b> kennen | <b>même:</b> zelfs</li>
    </ul>
        """,
        "vragen": [
            {"type": "mc", "vraag": "Wat bedoelt een Franse tiener die zegt: <i>'Le weekend, je fais la grasse matinée'</i>?", "opties": ["ontbijt klaarmaken", "uitslapen tot laat in de ochtend", "vroeg gaan hardlopen", "naar de kerk gaan"], "antwoord": 1, "uitleg": "'Faire la grasse matinée' betekent lekker lang uitslapen."},
            {"type": "mc", "vraag": "Welke vrijetijdsbesteding omschrijft de uitdrukking <b>'jouer à la console'</b>?", "opties": ["piano spelen", "huiswerk maken", "gamen op een spelcomputer", "buiten voetballen"], "antwoord": 2, "uitleg": "'Jouer à la console' is gamen op bijvoorbeeld een PlayStation, Xbox of Switch."},
            {"type": "mc", "vraag": "Hoe zeg je in het Frans dat vrienden <b>elkaar ergens ontmoeten / treffen</b>?", "opties": ["se reposer", "commencer", "discuter", "se retrouver"], "antwoord": 3, "uitleg": "'Se retrouver' betekent elkaar ontmoeten of treffen op een afgesproken plek."},
            {"type": "mc", "vraag": "Wat betekent de uitdrukking <b>'avoir envie de faire la fête'</b>?", "opties": ["zin hebben om feest te vieren", "bang zijn voor een feest", "geen tijd hebben voor feest", "moe zijn van een feest"], "antwoord": 0, "uitleg": "'Avoir envie de' betekent zin hebben om iets te doen."},
            {"type": "waaronwaar", "vraag": "Het Franse woordje <b>'tôt'</b> (p. 86) betekent in het Nederlands 'laat'.", "antwoord": False, "uitleg": "Onwaar. 'Tôt' betekent 'vroeg'; 'laat' is 'tard'."},
            {"type": "waaronwaar", "vraag": "In de uitspraak <i>'Tu as l'air fatigué'</i> betekent de uitdrukking 'avoir l'air': eruit zien.", "antwoord": True, "uitleg": "Waar. 'Avoir l'air' betekent eruit zien of lijken."},
            {"type": "waaronwaar", "vraag": "Het Franse woord <b>'le début'</b> betekent 'het einde'.", "antwoord": False, "uitleg": "Onwaar. 'Le début' betekent 'het begin'; 'het einde' is 'la fin'."},
            {"type": "waaronwaar", "vraag": "Het woord <b>'selon'</b> (Blok B) betekent 'volgens' (zoals in <i>selon moi</i>).", "antwoord": True, "uitleg": "Waar. 'Selon' betekent volgens."},
            {"type": "invoer", "vraag": "Hoe noem je in het Frans <i>'de tijd waarin je niet hoeft te werken of naar school hoeft'</i> (inclusief lidwoord)?", "antwoord": "le temps libre", "uitleg": "'De vrije tijd' is in het Frans 'le temps libre'."},
            {"type": "invoer", "vraag": "Vertaal <b>'het geld'</b> naar het Frans (inclusief lidwoord met apostrof):", "antwoord": "l'argent", "uitleg": "'Het geld' is 'l'argent' (mannelijk woord met l')."}
        ]
    },
    {
        "id": "fr-u2-2",
        "hoofdstuk": 2,
        "paragraaf": "2.2",
        "titel": "Woordenschat 2.2 · p. 87 (blok E & F) · Meningen, sport & maatschappij",
        "korteUitleg": "Woorden over oordelen, meningen, fitness, uitgaan, boodschappen en de wereld om je heen.",
        "icoon": "⭐",
        "kleur": "blauw",
        "theorie": """
    <h3>2.2 Woordenschat: pagina 87 (Blok E & F)</h3>
    <div class="info-box">
      <b>Leeradvies:</b> Leer de woorden uit het witte blok in <i>beide richtingen</i>. De woorden uit het blauwe blok hoef je alleen Frans ➔ Nederlands te kunnen herkennen.
    </div>

    <h4>Blok E: Uitgaan, sporten en oordelen (p. 87)</h4>
    <table class="vocab-tabel" style="width:100%;border-collapse:collapse;margin:12px 0;">
      <tr style="background:var(--blauw-licht);">
        <th style="padding:6px;border:1px solid var(--lijn);">Frans 🇫🇷</th>
        <th style="padding:6px;border:1px solid var(--lijn);">Nederlands 🇳🇱</th>
        <th style="padding:6px;border:1px solid var(--lijn);">Frans 🇫🇷</th>
        <th style="padding:6px;border:1px solid var(--lijn);">Nederlands 🇳🇱</th>
      </tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>suivre</b></td><td style="padding:6px;border:1px solid var(--lijn);">volgen</td><td style="padding:6px;border:1px solid var(--lijn);"><b>ça me rend fou</b></td><td style="padding:6px;border:1px solid var(--lijn);">daar word ik gek van</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>garder (quelqu'un)</b></td><td style="padding:6px;border:1px solid var(--lijn);">(op iemand) passen</td><td style="padding:6px;border:1px solid var(--lijn);"><b>plein (de)</b></td><td style="padding:6px;border:1px solid var(--lijn);">een heleboel</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>espérer</b></td><td style="padding:6px;border:1px solid var(--lijn);">hopen</td><td style="padding:6px;border:1px solid var(--lijn);"><b>d'abord</b></td><td style="padding:6px;border:1px solid var(--lijn);">ten eerste</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>aller au restaurant</b></td><td style="padding:6px;border:1px solid var(--lijn);">naar het restaurant gaan</td><td style="padding:6px;border:1px solid var(--lijn);"><b>intéressant(e)</b></td><td style="padding:6px;border:1px solid var(--lijn);">interessant</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>aller à la salle de sport</b></td><td style="padding:6px;border:1px solid var(--lijn);">naar de sportschool gaan</td><td style="padding:6px;border:1px solid var(--lijn);"><b>passionnant(e)</b></td><td style="padding:6px;border:1px solid var(--lijn);">boeiend</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>faire du fitness</b></td><td style="padding:6px;border:1px solid var(--lijn);">fitnessen</td><td style="padding:6px;border:1px solid var(--lijn);"><b>pas mal</b></td><td style="padding:6px;border:1px solid var(--lijn);">niet slecht</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>sortir</b></td><td style="padding:6px;border:1px solid var(--lijn);">uitgaan</td><td style="padding:6px;border:1px solid var(--lijn);"><b>nul(le)</b></td><td style="padding:6px;border:1px solid var(--lijn);">waardeloos</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>faire la vaisselle</b></td><td style="padding:6px;border:1px solid var(--lijn);">afwassen</td><td style="padding:6px;border:1px solid var(--lijn);"><b>ennuyeux, -euse</b></td><td style="padding:6px;border:1px solid var(--lijn);">saai</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>faire les courses</b></td><td style="padding:6px;border:1px solid var(--lijn);">boodschappen doen</td><td style="padding:6px;border:1px solid var(--lijn);"><b>terrible</b></td><td style="padding:6px;border:1px solid var(--lijn);">vreselijk</td></tr>
    </table>

    <h4>Blok F: Mensen, omgeving en gevoelens (p. 87)</h4>
    <ul>
      <li><b>le voyage:</b> de reis | <b>le monde:</b> de wereld | <b>la tête:</b> het hoofd | <b>l'endroit (m):</b> de plek</li>
      <li><b>la vitesse:</b> de snelheid | <b>la victime:</b> het slachtoffer | <b>l'habitant (m):</b> de inwoner | <b>le jour:</b> de dag</li>
      <li><b>déranger:</b> storen | <b>choisir:</b> kiezen | <b>j'en ai assez:</b> ik heb er genoeg van | <b>long, longue:</b> lang</li>
      <li><b>amoureux, -euse:</b> verliefd | <b>curieux, -euse:</b> nieuwsgierig</li>
      <li><i>Blauw blok (passief):</i> <b>l'étoile (v):</b> de ster | <b>le moyen:</b> het middel | <b>le scientifique:</b> de wetenschapper | <b>la trottinette:</b> de step | <b>l'entreprise (v):</b> het bedrijf | <b>l'espace (m):</b> de ruimte | <b>le commerce:</b> de handel | <b>il finira:</b> hij zal eindigen | <b>à l'intérieur:</b> binnen | <b>polluant(e):</b> vervuilend</li>
    </ul>
        """,
        "vragen": [
            {"type": "mc", "vraag": "Wat betekent het Franse bijvoeglijk naamwoord <b>'ennuyeux'</b> (in de vrouwelijke vorm: <i>ennuyeuse</i>)?", "opties": ["saai", "spannend", "grappig", "makkelijk"], "antwoord": 0, "uitleg": "'Ennuyeux / ennuyeuse' betekent saai."},
            {"type": "mc", "vraag": "Wat betekent de uitdrukking <b>'faire la vaisselle'</b> (p. 87)?", "opties": ["koken", "de was doen", "afwassen", "stofzuigen"], "antwoord": 2, "uitleg": "'Faire la vaisselle' betekent de afwas doen / afwassen."},
            {"type": "mc", "vraag": "Vertaal <b>'daar word ik gek van'</b> naar het Frans:", "opties": ["j'en ai assez", "c'est pas mal", "je suis fatigué", "ça me rend fou"], "antwoord": 3, "uitleg": "'Ça me rend fou' (of folle) betekent letterlijk 'dat maakt me gek'."},
            {"type": "mc", "vraag": "Wat ga je doen als je moeder vraagt om <b>'faire les courses au supermarché'</b>?", "opties": ["hardlopen", "boodschappen doen in de supermarkt", "kleding passen", "de auto wassen"], "antwoord": 1, "uitleg": "'Faire les courses' betekent boodschappen doen voor levensmiddelen."},
            {"type": "waaronwaar", "vraag": "Het Franse woord <b>'passionnant'</b> (p. 87) betekent 'waardeloos'.", "antwoord": False, "uitleg": "Onwaar. 'Passionnant' betekent 'boeiend / meeslepend'; 'waardeloos' is 'nul / nulle'."},
            {"type": "waaronwaar", "vraag": "De uitdrukking <b>'j'en ai assez'</b> (Blok F) betekent 'ik heb er genoeg van / ik ben het zat'.", "antwoord": True, "uitleg": "Waar. 'J'en ai assez' drukt uit dat je er helemaal klaar mee bent."},
            {"type": "waaronwaar", "vraag": "Het woord <b>'le monde'</b> betekent 'de maan'.", "antwoord": False, "uitleg": "Onwaar. 'Le monde' betekent 'de wereld' (en 'tout le monde' = iedereen)."},
            {"type": "waaronwaar", "vraag": "Het Franse werkwoord <b>'choisir'</b> (Blok F) betekent 'kiezen'.", "antwoord": True, "uitleg": "Waar. 'Choisir' is een regelmatig werkwoord op -ir dat 'kiezen' betekent."},
            {"type": "invoer", "vraag": "Geef de Franse vertaling van het zelfstandig naamwoord <b>'de reis'</b> (inclusief lidwoord):", "antwoord": "le voyage", "uitleg": "'De reis' is 'le voyage' (mannelijk)."},
            {"type": "invoer", "vraag": "Vertaal het bijvoeglijk naamwoord <b>'verliefd'</b> (mannelijke vorm) naar het Frans:", "antwoord": "amoureux", "uitleg": "'Verliefd' is 'amoureux' (m) of 'amoureuse' (v)."}
        ]
    },
    {
        "id": "fr-u2-3",
        "hoofdstuk": 2,
        "paragraaf": "2.3",
        "titel": "Phrases-clés 2.3 · p. 88 (C & G) · Praten over je vrije tijd & hobby's",
        "korteUitleg": "Sleutelzinnen over weekendactiviteiten, lievelingsseries, sport, bioscoop en wat je wel en niet leuk vindt.",
        "icoon": "💬",
        "kleur": "blauw",
        "theorie": """
    <h3>2.3 Phrases-clés: pagina 88 (C & G)</h3>
    <div class="info-box">
      <b>Spreken & Schrijven:</b> Deze zinnen moet je vlot Frans ➔ Nederlands én Nederlands ➔ Frans kunnen gebruiken in dialogen en schrijfopdrachten over je weekend en vrije tijd!
    </div>

    <h4>Phrases-clés C: Parler de son temps libre (Deel 1 - Weekend & Series)</h4>
    <table class="vocab-tabel" style="width:100%;border-collapse:collapse;margin:12px 0;">
      <tr style="background:var(--blauw-licht);">
        <th style="padding:6px;border:1px solid var(--lijn);width:50%;">Nederlands 🇳🇱</th>
        <th style="padding:6px;border:1px solid var(--lijn);width:50%;">Frans 🇫🇷</th>
      </tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);">Wat doe je in het weekend?</td><td style="padding:6px;border:1px solid var(--lijn);"><b>Qu'est-ce que tu fais le weekend?</b></td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);">'s Ochtends slaap ik uit.</td><td style="padding:6px;border:1px solid var(--lijn);"><b>Le matin, je fais la grasse matinée.</b></td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);">En daarna?</td><td style="padding:6px;border:1px solid var(--lijn);"><b>Et après?</b></td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);">Ik vind het leuk om naar de stad te gaan met mijn vrienden.</td><td style="padding:6px;border:1px solid var(--lijn);"><b>J'aime aller en ville avec mes copains.</b></td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);">Wat doe je nog meer?</td><td style="padding:6px;border:1px solid var(--lijn);"><b>Qu'est-ce que tu fais d'autre?</b></td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);">Ik kijk naar online series.</td><td style="padding:6px;border:1px solid var(--lijn);"><b>Je regarde des séries sur Internet.</b></td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);">Wat is je lievelingsserie?</td><td style="padding:6px;border:1px solid var(--lijn);"><b>Quelle est ta série préférée?</b></td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);">Dat is Plan Coeur, een serie over vriendschap.</td><td style="padding:6px;border:1px solid var(--lijn);"><b>C'est Plan Coeur, une série sur l'amitié.</b></td></tr>
    </table>

    <h4>Phrases-clés G: Parler de son temps libre (Deel 2 - Voorkeuren & Redenen)</h4>
    <table class="vocab-tabel" style="width:100%;border-collapse:collapse;margin:12px 0;">
      <tr style="background:var(--blauw-licht);">
        <th style="padding:6px;border:1px solid var(--lijn);width:50%;">Nederlands 🇳🇱</th>
        <th style="padding:6px;border:1px solid var(--lijn);width:50%;">Frans 🇫🇷</th>
      </tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);">Wat vind je leuk om te doen?</td><td style="padding:6px;border:1px solid var(--lijn);"><b>Qu'est-ce que tu aimes faire?</b></td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);">Ik vind het leuk om te sporten.</td><td style="padding:6px;border:1px solid var(--lijn);"><b>J'aime faire du sport.</b></td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);">Ik vind het leuk om naar de bioscoop te gaan.</td><td style="padding:6px;border:1px solid var(--lijn);"><b>J'aime aller au cinéma.</b></td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);">Waarom vind je dat leuk (om te doen)?</td><td style="padding:6px;border:1px solid var(--lijn);"><b>Pourquoi tu aimes (faire) ça?</b></td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);">Omdat ik met mijn vrienden sport.</td><td style="padding:6px;border:1px solid var(--lijn);"><b>Parce que je fais du sport avec mes amis.</b></td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);">Omdat het super is.</td><td style="padding:6px;border:1px solid var(--lijn);"><b>Parce que c'est super.</b></td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);">Omdat ik sportief ben.</td><td style="padding:6px;border:1px solid var(--lijn);"><b>Parce que je suis sportif.</b></td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);">Wat vind je niet leuk om te doen?</td><td style="padding:6px;border:1px solid var(--lijn);"><b>Qu'est-ce que tu n'aimes pas faire?</b></td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);">Ik heb een hekel aan mijn kamer opruimen.</td><td style="padding:6px;border:1px solid var(--lijn);"><b>Je déteste ranger ma chambre.</b></td></tr>
    </table>
        """,
        "vragen": [
            {"type": "mc", "vraag": "Hoe vraag je in het Frans: <i>'Wat doe je in het weekend?'</i>", "opties": ["Qu'est-ce que tu fais le weekend?", "Où vas-tu pendant les vacances?", "Comment tu trouves le weekend?", "Quel est ton sport préféré?"], "antwoord": 0, "uitleg": "'Qu'est-ce que tu fais le weekend?' betekent 'Wat doe je in het weekend?'."},
            {"type": "mc", "vraag": "Welke Franse zin betekent: <i>'Ik vind het leuk om naar de stad te gaan met mijn vrienden'</i>?", "opties": ["Je vais seul en ville.", "J'aime aller en ville avec mes copains.", "Mes amis habitent en ville.", "Je déteste aller en ville."], "antwoord": 1, "uitleg": "'J'aime aller en ville avec mes copains' betekent dat je graag met je vrienden naar de stad gaat."},
            {"type": "mc", "vraag": "Hoe zeg je in het Frans: <i>'Ik heb een hekel aan mijn kamer opruimen'</i>?", "opties": ["J'aime ranger ma chambre.", "Je ne peux pas ranger ma chambre.", "Je déteste ranger ma chambre.", "Ma chambre est altijd schoon."], "antwoord": 2, "uitleg": "'Je déteste ranger ma chambre' ('détester' = een hekel hebben aan, haten)."},
            {"type": "mc", "vraag": "Wat betekent de vraag: <b>'Quelle est ta série préférée?'</b>", "opties": ["Hoe laat begint de serie?", "Heb je gisteren een serie gekeken?", "Waar kijk je naar series?", "Wat is je lievelingsserie?"], "antwoord": 3, "uitleg": "'Quelle est ta série préférée?' vraagt naar iemands favoriete serie."},
            {"type": "waaronwaar", "vraag": "In de zin <b>'Parce que c'est super'</b> betekent 'parce que' in het Nederlands 'daarom'.", "antwoord": False, "uitleg": "Onwaar. 'Parce que' betekent 'omdat' (als antwoord op de vraag 'Pourquoi?')."},
            {"type": "waaronwaar", "vraag": "De zin <b>'Le matin, je fais la grasse matinée'</b> betekent dat je 's ochtends vroeg naar school gaat.", "antwoord": False, "uitleg": "Onwaar. Het betekent: ''s Ochtends slaap ik lekker uit.'"},
            {"type": "waaronwaar", "vraag": "De uitdrukking <b>'aller au cinéma'</b> betekent 'naar de bioscoop gaan'.", "antwoord": True, "uitleg": "Waar. 'Le cinéma' is de bioscoop."},
            {"type": "waaronwaar", "vraag": "De vraag <b>'Qu'est-ce que tu fais d'autre?'</b> betekent 'Wat doe je nog meer?'.", "antwoord": True, "uitleg": "Waar. 'D'autre' betekent 'anders / nog meer / overig'."},
            {"type": "invoer", "vraag": "Vertaal naar het Frans (En daarna?): <i>... ?</i>", "antwoord": "Et après|Et après?", "uitleg": "'En daarna?' vertaal je met 'Et après?'."},
            {"type": "invoer", "vraag": "Vertaal het Franse woord voor 'omdat' (in antwoord op pourquoi):", "antwoord": "parce que|parce qu'", "uitleg": "'Omdat' is in het Frans 'parce que'."}
        ]
    },
    {
        "id": "fr-u2-4",
        "hoofdstuk": 2,
        "paragraaf": "2.4",
        "titel": "Grammatica 2.4 · p. 89 (D & H) · à/de + lidwoord & werkwoorden op -ir",
        "korteUitleg": "Samentrekking van à/de met le/les (au, aux, du, des) en vervoeging van regelmatige werkwoorden op -ir (finir).",
        "icoon": "📐",
        "kleur": "blauw",
        "theorie": """
    <h3>2.4 Grammatica: pagina 89 (Grammaire D & H)</h3>
    <div class="info-box">
      <b>Twee cruciale grammaticaregels van Unité 2:</b><br>
      1. Het samentrekken van de voorzetsels <b>à</b> en <b>de</b> met bepaalde lidwoorden.<br>
      2. De vervoeging van regelmatige werkwoorden op <b>-ir</b> in de tegenwoordige tijd (présent) en verleden tijd (passé composé).
    </div>

    <h4>Grammaire D: à / de + bepaald lidwoord</h4>
    <p>Als het voorzetsel <b>à</b> (= in, naar, op, bij) of <b>de</b> (= van, over, uit) vóór een mannelijk lidwoord (<code>le</code>) of meervoudslidwoord (<code>les</code>) komt, smelt het samen tot één woord:</p>
    <table class="vocab-tabel" style="width:100%;border-collapse:collapse;margin:12px 0;">
      <tr style="background:var(--blauw-licht);">
        <th style="padding:6px;border:1px solid var(--lijn);">Voorzetsel</th>
        <th style="padding:6px;border:1px solid var(--lijn);">+ Lidwoord</th>
        <th style="padding:6px;border:1px solid var(--lijn);">Wordt</th>
        <th style="padding:6px;border:1px solid var(--lijn);">Voorbeeldzin</th>
      </tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);">à</td><td style="padding:6px;border:1px solid var(--lijn);">le</td><td style="padding:6px;border:1px solid var(--lijn);"><b>au</b></td><td style="padding:6px;border:1px solid var(--lijn);">Je suis <b>au</b> club de foot. (bij de voetbalclub)</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);">à</td><td style="padding:6px;border:1px solid var(--lijn);">les</td><td style="padding:6px;border:1px solid var(--lijn);"><b>aux</b></td><td style="padding:6px;border:1px solid var(--lijn);">Il va <b>aux</b> matchs. (naar de wedstrijden)</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);">à</td><td style="padding:6px;border:1px solid var(--lijn);">la / l'</td><td style="padding:6px;border:1px solid var(--lijn);"><b>à la / à l'</b></td><td style="padding:6px;border:1px solid var(--lijn);">Je vais <b>à la</b> piscine / <b>à l'</b>école. (blijft los!)</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);">de</td><td style="padding:6px;border:1px solid var(--lijn);">le</td><td style="padding:6px;border:1px solid var(--lijn);"><b>du</b></td><td style="padding:6px;border:1px solid var(--lijn);">C'est l'entrée <b>du</b> collège. (van de school)</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);">de</td><td style="padding:6px;border:1px solid var(--lijn);">les</td><td style="padding:6px;border:1px solid var(--lijn);"><b>des</b></td><td style="padding:6px;border:1px solid var(--lijn);">C'est le chien <b>des</b> voisins. (van de buren)</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);">de</td><td style="padding:6px;border:1px solid var(--lijn);">la / l'</td><td style="padding:6px;border:1px solid var(--lijn);"><b>de la / de l'</b></td><td style="padding:6px;border:1px solid var(--lijn);">Elle parle <b>de la</b> musique / <b>de l'</b>argent. (blijft los!)</td></tr>
    </table>

    <h4>Grammaire H: Regelmatige werkwoorden op -ir (model: finir)</h4>
    <p>Regelmatige werkwoorden op <b>-ir</b> verliezen de uitgang <i>-ir</i> om de stam te vinden. Achter de stam komen de uitgangen van de <i>finir</i>-groep:</p>
    <ul>
      <li><b>je finis</b> (uitgang: <b>-is</b>) — ik beëindig / ik ben klaar</li>
      <li><b>tu finis</b> (uitgang: <b>-is</b>) — jij beëindigt</li>
      <li><b>il / elle / on finit</b> (uitgang: <b>-it</b>) — hij / zij / men beëindigt</li>
      <li><b>nous finissons</b> (uitgang: <b>-issons</b>) — wij beëindigen</li>
      <li><b>vous finissez</b> (uitgang: <b>-issez</b>) — jullie beëindigen / u beëindigt</li>
      <li><b>ils / elles finissent</b> (uitgang: <b>-issent</b>) — zij beëindigen</li>
    </ul>
    <p><b>Passé composé:</b> Hulpwerkwoord <code>avoir</code> + voltooid deelwoord op <b>-i</b> (zonder accent!):<br>
    <code>J'ai fini</code> (ik heb beëindigd), <code>Tu as choisi</code> (jij hebt gekozen), <code>Il a réfléchi</code> (hij heeft nagedacht).</p>
    <p>Andere werkwoorden uit deze groep: <b>choisir</b> (kiezen), <b>réfléchir</b> (nadenken), <b>réussir</b> (slagen), <b>remplir</b> (invullen), <b>grandir</b> (groeien), <b>rougir</b> (blozen).</p>
        """,
        "vragen": [
            {"type": "mc", "vraag": "Wat is de juiste samentrekking van <b>à + le</b> in het Frans?", "opties": ["au", "aux", "du", "à le"], "antwoord": 0, "uitleg": "à + le trekt altijd verplicht samen tot 'au' (bijv. au cinéma)."},
            {"type": "mc", "vraag": "Wat is de juiste samentrekking van <b>de + les</b> in het Frans?", "opties": ["du", "des", "dels", "de les"], "antwoord": 1, "uitleg": "de + les smelt samen tot 'des' (bijv. le chien des voisins)."},
            {"type": "mc", "vraag": "Welke vorm van het werkwoord <b>choisir</b> hoort bij <b>nous</b>?", "opties": ["nous choisent", "nous choisis", "nous choisissons", "nous choisiez"], "antwoord": 2, "uitleg": "Bij regelmatige -ir werkwoorden krijgt nous de uitgang -issons: nous choisissons."},
            {"type": "mc", "vraag": "Wat is het voltooid deelwoord van <b>finir</b> in de passé composé (<i>J'ai ...</i>)?", "opties": ["finu", "finé", "finissant", "fini"], "antwoord": 3, "uitleg": "Werkwoorden op -ir krijgen in de passé composé een voltooid deelwoord op -i: fini (zonder accent)."},
            {"type": "waaronwaar", "vraag": "De combinatie <b>à + la</b> smelt in het Frans samen tot één enkel woord.", "antwoord": False, "uitleg": "Onwaar. Alleen à + le (au) en à + les (aux) smelten samen; à la en à l' blijven altijd twee losse woorden."},
            {"type": "waaronwaar", "vraag": "Bij het werkwoord <b>finir</b> is de vorm voor <b>il</b> en <b>elle</b> 'finit' (met een -t).", "antwoord": True, "uitleg": "Waar. Il/elle finit eindigt op -it."},
            {"type": "waaronwaar", "vraag": "De combinatie <b>de + le</b> wordt in het Frans geschreven als 'du'.", "antwoord": True, "uitleg": "Waar. Bijvoorbeeld: l'entrée du collège."},
            {"type": "waaronwaar", "vraag": "Werkwoorden op -ir krijgen in de passé composé een voltooid deelwoord dat eindigt op -é.", "antwoord": False, "uitleg": "Onwaar. Werkwoorden op -er krijgen -é (parlé); regelmatige werkwoorden op -ir krijgen -i (fini, choisi)."},
            {"type": "invoer", "vraag": "Vul de juiste samentrekking in van à + les (<i>Il va ... toilettes</i>):", "antwoord": "aux", "uitleg": "à + les wordt 'aux'."},
            {"type": "invoer", "vraag": "Vul de juiste vorm van finir in bij 'tu' (présent): <i>Tu ... tes devoirs?</i>", "antwoord": "finis", "uitleg": "De vorm bij 'tu' is 'tu finis'."}
        ]
    }
]

# ---------------------------------------------------------
# EXAMENS (examen_u2_vocab_1.js t/m 5.js)
# ---------------------------------------------------------

EXAMENS = [
    {
        "id": "ex-h3-frans-u2-v1",
        "hoofdstuk": 2,
        "hoofdstukTitel": "Unité 2 — Du temps pour moi",
        "titel": "Woordenschat 1 · p. 86 (blok A & B) · FR ⇄ NL",
        "vak": "Frans · HAVO 3 (U2)",
        "icoon": "🔤",
        "duurMin": 20,
        "vragen": [
            # 12 MC (balanced: exactly 3 A, 3 B, 3 C, 3 D)
            {"type": "mc", "vraag": "Wat betekent het Franse werkwoord <b>'commencer'</b> (p. 86)?", "opties": ["beginnen", "eindigen", "wachten", "proberen"], "antwoord": 0, "uitleg": "'Commencer' betekent beginnen."},
            {"type": "mc", "vraag": "Wat is de juiste Franse vertaling van <b>'uitslapen'</b> (p. 86)?", "opties": ["faire du sport", "faire la grasse matinée", "se coucher tard", "faire attention"], "antwoord": 1, "uitleg": "'Faire la grasse matinée' betekent uitslapen."},
            {"type": "mc", "vraag": "Wat betekent de activiteit <b>'jouer à la console'</b> (p. 86)?", "opties": ["gitaar spelen", "voetballen", "gamen / op de spelcomputer spelen", "muziek luisteren"], "antwoord": 2, "uitleg": "'Jouer à la console' betekent gamen op een console."},
            {"type": "mc", "vraag": "Welk Frans werkwoord betekent <b>'elkaar treffen'</b> (p. 86)?", "opties": ["se reposer", "se lever", "discuter", "se retrouver"], "antwoord": 3, "uitleg": "'Se retrouver' betekent elkaar ontmoeten of treffen."},
            {"type": "mc", "vraag": "Wat betekent de Franse uitdrukking <b>'avoir envie (de)'</b>?", "opties": ["zin hebben (om)", "bang zijn (voor)", "tijd hebben (om)", "nodig hebben"], "antwoord": 0, "uitleg": "'Avoir envie de' betekent zin hebben om iets te doen."},
            {"type": "mc", "vraag": "Wat betekent het woordje <b>'tôt'</b> (p. 86)?", "opties": ["laat", "vroeg", "nooit", "altijd"], "antwoord": 1, "uitleg": "'Tôt' betekent vroeg (tegenovergestelde van 'tard')."},
            {"type": "mc", "vraag": "Wat betekent het zelfstandig naamwoord <b>'l'argent'</b> (mannelijk, p. 86)?", "opties": ["het zilver", "het goud", "het geld", "de bank"], "antwoord": 2, "uitleg": "'L'argent' betekent het geld (en als materiaal: zilver)."},
            {"type": "mc", "vraag": "Vertaal het woordje <b>'volgens'</b> naar het Frans (p. 86, Blok B):", "opties": ["comme", "chaque", "parfois", "selon"], "antwoord": 3, "uitleg": "'Selon' betekent volgens ('selon moi' = volgens mij)."},
            {"type": "mc", "vraag": "Wat betekent het werkwoord <b>'réfléchir'</b> (p. 86)?", "opties": ["nadenken", "kiezen", "helpen", "lezen"], "antwoord": 0, "uitleg": "'Réfléchir' betekent nadenken."},
            {"type": "mc", "vraag": "Wat is de Nederlandse betekenis van <b>'l'entrée'</b> (vrouwelijk)?", "opties": ["de uitgang", "de ingang", "de gang", "de trap"], "antwoord": 1, "uitleg": "'L'entrée' is de ingang van een gebouw of lokaal."},
            {"type": "mc", "vraag": "Wat betekent het Franse bijvoeglijk naamwoord <b>'fatigué(e)'</b>?", "opties": ["blij", "boos", "moe", "ziek"], "antwoord": 2, "uitleg": "'Fatigué(e)' betekent moe."},
            {"type": "mc", "vraag": "Wat betekent de uitdrukking <b>'chez moi'</b> (p. 86)?", "opties": ["op school", "in de stad", "bij vrienden", "bij mij (thuis)"], "antwoord": 3, "uitleg": "'Chez moi' betekent bij mij thuis."},
            # 4 Waaronwaar (at least 2 false)
            {"type": "waaronwaar", "vraag": "Het Franse woord <b>'dur'</b> betekent 'zacht en gemakkelijk'.", "antwoord": False, "uitleg": "Onwaar. 'Dur' betekent 'hard / moeilijk'."},
            {"type": "waaronwaar", "vraag": "De uitdrukking <b>'avoir l'air'</b> betekent 'eruit zien / lijken'.", "antwoord": True, "uitleg": "Waar. 'Tu as l'air content' betekent 'je ziet er tevreden uit'."},
            {"type": "waaronwaar", "vraag": "Het woord <b>'tard'</b> betekent in het Nederlands 'vroeg'.", "antwoord": False, "uitleg": "Onwaar. 'Tard' betekent 'laat'; 'vroeg' is 'tôt'."},
            {"type": "waaronwaar", "vraag": "Het woord <b>'le début'</b> betekent 'het begin'.", "antwoord": True, "uitleg": "Waar. 'Le début' is het begin van iets."},
            # 2 Invul
            {"type": "invul", "vraag": "Vertaal het woord <i>'de les'</i> naar het Frans (p. 86): <i>Pendant ... de français, nous parlons beaucoup.</i>", "antwoord": "le cours", "uitleg": "'De les' is 'le cours'."},
            {"type": "invul", "vraag": "Vertaal <i>'de vrije tijd'</i> naar het Frans (inclusief lidwoord):", "antwoord": "le temps libre", "uitleg": "'De vrije tijd' vertaal je met 'le temps libre'."},
            # 2 Open
            {"type": "open", "vraag": "Wat betekenen de twee tegenovergestelde Franse tijdsaanduidingen <b>'tôt'</b> en <b>'tard'</b>?", "sleutelwoorden": ["vroeg", "laat"], "minTreffers": 2, "modelantwoord": "'Tôt' betekent vroeg en 'tard' betekent laat.", "uitleg": "'Tôt' is vroeg en 'tard' is laat."},
            {"type": "open", "vraag": "Leg uit wat de Franse uitdrukking <b>'faire la grasse matinée'</b> letterlijk en figuurlijk betekent.", "sleutelwoorden": ["uitslapen/lang slapen", "ochtend/matinée"], "minTreffers": 2, "modelantwoord": "Het betekent uitslapen in de ochtend, letterlijk 'de vette ochtend maken' door lekker lang in bed te blijven liggen.", "uitleg": "'Faire la grasse matinée' is de vaste Franse uitdrukking voor uitslapen."}
        ]
    },
    {
        "id": "ex-h3-frans-u2-v2",
        "hoofdstuk": 2,
        "hoofdstukTitel": "Unité 2 — Du temps voor moi",
        "titel": "Woordenschat 2 · p. 87 (blok E & F) · FR ⇄ NL",
        "vak": "Frans · HAVO 3 (U2)",
        "icoon": "⭐",
        "duurMin": 20,
        "vragen": [
            # 12 MC (balanced: 3 A, 3 B, 3 C, 3 D)
            {"type": "mc", "vraag": "Wat betekent het Franse werkwoord <b>'suivre'</b> (p. 87)?", "opties": ["volgen", "verliezen", "zoeken", "vinden"], "antwoord": 0, "uitleg": "'Suivre' betekent volgen (bijv. een les of een account)."},
            {"type": "mc", "vraag": "Wat betekent het Franse woord <b>'ennuyeux'</b> (p. 87)?", "opties": ["spannend", "saai", "vrolijk", "moeilijk"], "antwoord": 1, "uitleg": "'Ennuyeux' betekent saai."},
            {"type": "mc", "vraag": "Wat is de betekenis van de Franse uitdrukking <b>'ça me rend fou'</b>?", "opties": ["dat vind ik geweldig", "daar moet ik om lachen", "daar word ik gek van", "dat maakt me verdrietig"], "antwoord": 2, "uitleg": "'Ça me rend fou' betekent letterlijk 'dat maakt me gek'."},
            {"type": "mc", "vraag": "Wat betekent de huishoudelijke taak <b>'faire la vaisselle'</b>?", "opties": ["boodschappen doen", "koken", "stofzuigen", "afwassen"], "antwoord": 3, "uitleg": "'Faire la vaisselle' is de afwas doen / afwassen."},
            {"type": "mc", "vraag": "Wat betekent het Franse woord <b>'passionnant(e)'</b>?", "opties": ["boeiend / meeslepend", "saai", "waardeloos", "duur"], "antwoord": 0, "uitleg": "'Passionnant(e)' betekent boeiend of meeslepend."},
            {"type": "mc", "vraag": "Vertaal <b>'boodschappen doen'</b> naar het Frans (p. 87):", "opties": ["faire du sport", "faire les courses", "faire les magasins", "faire la fête"], "antwoord": 1, "uitleg": "'Faire les courses' betekent boodschappen doen (voor eten en dagelijkse benodigdheden)."},
            {"type": "mc", "vraag": "Wat betekent het werkwoord <b>'garder'</b> in de context van <i>'garder des enfants'</i>?", "opties": ["lesgeven aan", "spelen met", "oppassen (op)", "straffen"], "antwoord": 2, "uitleg": "'Garder des enfants' betekent op kinderen passen (oppassen / babysitten)."},
            {"type": "mc", "vraag": "Wat betekent het spreektaalwoord <b>'nul(le)'</b> (p. 87)?", "opties": ["geweldig", "interessant", "duur", "waardeloos / stom"], "antwoord": 3, "uitleg": "'Nul' of 'nulle' betekent waardeloos of heel stom."},
            {"type": "mc", "vraag": "Wat betekent het Franse zelfstandig naamwoord <b>'le monde'</b>?", "opties": ["de wereld", "de maan", "de stad", "de straat"], "antwoord": 0, "uitleg": "'Le monde' betekent de wereld."},
            {"type": "mc", "vraag": "Wat betekent de uitdrukking <b>'j'en ai assez'</b>?", "opties": ["ik heb er trek in", "ik heb er genoeg van", "ik heb er geen tijd voor", "ik heb er veel van"], "antwoord": 1, "uitleg": "'J'en ai assez' betekent dat je het zat bent / er genoeg van hebt."},
            {"type": "mc", "vraag": "Wat betekent het bijvoeglijk naamwoord <b>'amoureux / amoureuse'</b>?", "opties": ["boos", "blij", "verliefd", "jaloers"], "antwoord": 2, "uitleg": "'Amoureux / amoureuse' betekent verliefd."},
            {"type": "mc", "vraag": "Wat betekent het Franse werkwoord <b>'déranger'</b> (p. 87)?", "opties": ["helpen", "verhuizen", "bellen", "storen"], "antwoord": 3, "uitleg": "'Déranger' betekent storen ('Ne pas déranger' = niet storen)."},
            # 4 Waaronwaar (at least 2 false)
            {"type": "waaronwaar", "vraag": "De uitdrukking <b>'sortir'</b> (p. 87) betekent 'binnenblijven'.", "antwoord": False, "uitleg": "Onwaar. 'Sortir' betekent 'uitgaan / naar buiten gaan'."},
            {"type": "waaronwaar", "vraag": "Het Franse woord <b>'la victime'</b> betekent 'het slachtoffer'.", "antwoord": True, "uitleg": "Waar. 'La victime' betekent het slachtoffer."},
            {"type": "waaronwaar", "vraag": "Het woord <b>'terrible'</b> (Blok E) betekent 'erg goedkoop'.", "antwoord": False, "uitleg": "Onwaar. 'Terrible' betekent 'vreselijk / verschrikkelijk'."},
            {"type": "waaronwaar", "vraag": "Het woord <b>'curieux / curieuse'</b> betekent 'nieuwsgierig'.", "antwoord": True, "uitleg": "Waar. 'Curieux' betekent nieuwsgierig."},
            # 2 Invul
            {"type": "invul", "vraag": "Vertaal het woord <i>'de reis'</i> naar het Frans (p. 87): <i>Bon ... à Paris!</i>", "antwoord": "voyage", "uitleg": "'De reis' is 'le voyage'."},
            {"type": "invul", "vraag": "Vertaal <i>'de plek / de plaats'</i> naar het Frans (inclusief lidwoord met apostrof):", "antwoord": "l'endroit", "uitleg": "'De plek' is 'l'endroit' (mannelijk)."},
            # 2 Open
            {"type": "open", "vraag": "Wat is het verschil in betekenis tussen <b>'faire les magasins'</b> en <b>'faire les courses'</b>?", "sleutelwoorden": ["winkelen/kleding/shoppen", "boodschappen/eten"], "minTreffers": 2, "modelantwoord": "'Faire les magasins' betekent winkelen of shoppen (voor kleding en plezier), terwijl 'faire les courses' specifiek boodschappen doen betekent (zoals eten in de supermarkt).", "uitleg": "'Faire les magasins' is shoppen; 'faire les courses' is boodschappen doen."},
            {"type": "open", "vraag": "Vertaal de zin <b>'Je déteste sortir quand il pleut'</b> naar goed Nederlands.", "sleutelwoorden": ["hekel/haat", "uitgaan/naar buiten", "regent"], "minTreffers": 2, "modelantwoord": "Ik heb er een hekel aan om uit te gaan als het regent.", "uitleg": "'Je déteste sortir quand il pleut' = Ik haat het om uit te gaan als het regent."}
        ]
    },
    {
        "id": "ex-h3-frans-u2-v3",
        "hoofdstuk": 2,
        "hoofdstukTitel": "Unité 2 — Du temps pour moi",
        "titel": "Phrases-clés 3 · p. 88 (C & G) · Praten over je vrije tijd",
        "vak": "Frans · HAVO 3 (U2)",
        "icoon": "💬",
        "duurMin": 20,
        "vragen": [
            # 12 MC (balanced: 3 A, 3 B, 3 C, 3 D)
            {"type": "mc", "vraag": "Welke Franse zin betekent: <i>'Wat doe je in het weekend?'</i>", "opties": ["Qu'est-ce que tu fais le weekend?", "Comment vas-tu ce weekend?", "Où passes-tu le weekend?", "Quel est ton jour préféré?"], "antwoord": 0, "uitleg": "'Qu'est-ce que tu fais le weekend?' betekent 'Wat doe je in het weekend?'."},
            {"type": "mc", "vraag": "Hoe zeg je in het Frans: <i>''s Ochtends slaap ik uit'</i>?", "opties": ["Le matin, je me lève tôt.", "Le matin, je fais la grasse matinée.", "Le matin, je fais du sport.", "Le matin, je pars à l'école."], "antwoord": 1, "uitleg": "'Le matin, je fais la grasse matinée' betekent ''s ochtends slaap ik uit'."},
            {"type": "mc", "vraag": "Wat betekent de Franse vraag: <b>'Qu'est-ce que tu fais d'autre?'</b>", "opties": ["Waar ga je naartoe?", "Met wie doe je dat?", "Wat doe je nog meer?", "Hoe laat begin je?"], "antwoord": 2, "uitleg": "'Qu'est-ce que tu fais d'autre?' vraagt wat je verder nog doet."},
            {"type": "mc", "vraag": "Hoe vraag je in het Frans naar iemands lievelingsserie?", "opties": ["Tu aimes les séries?", "Regardes-tu souvent la télé?", "Quelle heure est-il pour la série?", "Quelle est ta série préférée?"], "antwoord": 3, "uitleg": "'Quelle est ta série préférée?' betekent 'Wat is je lievelingsserie?'."},
            {"type": "mc", "vraag": "Wat betekent het antwoord: <b>'Parce que c'est super'</b>?", "opties": ["Omdat het super is", "Waarom is het super?", "Ik vind het niet super", "Het is te duur"], "antwoord": 0, "uitleg": "'Parce que c'est super' betekent 'Omdat het super is'."},
            {"type": "mc", "vraag": "Welke zin betekent: <i>'Ik heb een hekel aan mijn kamer opruimen'</i>?", "opties": ["J'aime nettoyer ma chambre.", "Je déteste ranger ma chambre.", "Ma chambre est trop petite.", "Je range ma chambre tous les jours."], "antwoord": 1, "uitleg": "'Je déteste ranger ma chambre' betekent dat je een hekel hebt aan je kamer opruimen."},
            {"type": "mc", "vraag": "Hoe zeg je in het Frans: <i>'Ik vind het leuk om naar de bioscoop te gaan'</i>?", "opties": ["Je vais souvent au cinéma.", "Le cinéma est très grand.", "J'aime aller au cinéma.", "Je regarde un film."], "antwoord": 2, "uitleg": "'J'aime aller au cinéma' betekent 'Ik vind het leuk om naar de bioscoop te gaan'."},
            {"type": "mc", "vraag": "Wat betekent: <b>'J'aime aller en ville avec mes copains'</b>?", "opties": ["Ik woon met mijn vrienden in de stad", "Mijn vrienden werken in de stad", "De stad is erg gezellig", "Ik vind het leuk om met mijn vrienden naar de stad te gaan"], "antwoord": 3, "uitleg": "Deze zin betekent dat je graag met je vrienden naar de stad gaat."},
            {"type": "mc", "vraag": "Met welk Frans woord begin je het antwoord op een <b>'Pourquoi... ?'</b> vraag?", "opties": ["Parce que", "Pourquoi", "Comment", "Quand"], "antwoord": 0, "uitleg": "Op 'Pourquoi?' antwoord je met 'Parce que...' (omdat...)."},
            {"type": "mc", "vraag": "Wat betekent de vraag: <b>'Qu'est-ce que tu n'aimes pas faire?'</b>", "opties": ["Wat vind je leuk om te doen?", "Wat vind je niet leuk om te doen?", "Waar hou je het meeste van?", "Wat kun je niet doen?"], "antwoord": 1, "uitleg": "Door de ontkenning 'n'... pas' betekent dit: 'Wat vind je NIET leuk om te doen?'."},
            {"type": "mc", "vraag": "Hoe zeg je in het Frans: <i>'Omdat ik sportief ben'</i>?", "opties": ["Parce que j'aime les jeux", "Je suis très fatigué", "Parce que je suis sportif", "Parce que le sport est dur"], "antwoord": 2, "uitleg": "'Parce que je suis sportif' betekent 'Omdat ik sportief ben'."},
            {"type": "mc", "vraag": "Wat betekent: <b>'C'est une série sur l'amitié'</b>?", "opties": ["Het is een serie over school", "Het is een film over liefde", "Het is een serie over sport", "Het is een serie over vriendschap"], "antwoord": 3, "uitleg": "'L'amitié' betekent de vriendschap."},
            # 4 Waaronwaar (at least 2 false)
            {"type": "waaronwaar", "vraag": "De uitdrukking <b>'Et après?'</b> betekent in het Nederlands 'En daarvoor?'.", "antwoord": False, "uitleg": "Onwaar. 'Et après?' betekent 'En daarna?' ('après' = na/daarna)."},
            {"type": "waaronwaar", "vraag": "In de zin <b>'Je regarde des séries sur Internet'</b> betekent 'regarder' luisteren.", "antwoord": False, "uitleg": "Onwaar. 'Regarder' betekent 'kijken naar'; 'luisteren' is 'écouter'."},
            {"type": "waaronwaar", "vraag": "De vraag <b>'Qu'est-ce que tu aimes faire?'</b> betekent 'Wat vind je leuk om te doen?'.", "antwoord": True, "uitleg": "Waar. Dit is de standaardzin om naar iemands hobby's te vragen."},
            {"type": "waaronwaar", "vraag": "Het Franse woord <b>'copains'</b> betekent vrienden of maatjes.", "antwoord": True, "uitleg": "Waar. 'Les copains' zijn vrienden of maten."},
            # 2 Invul
            {"type": "invul", "vraag": "Vul het ontbrekende woord in (lievelingsserie): <i>Quelle est ta série ... ?</i>", "antwoord": "préférée", "uitleg": "'Ta série préférée' = jouw lievelingsserie."},
            {"type": "invul", "vraag": "Vertaal het woord <i>'waarom'</i> naar het Frans: <i>... tu aimes faire ça?</i>", "antwoord": "Pourquoi", "uitleg": "'Waarom' vertaal je met 'Pourquoi'."},
            # 2 Open
            {"type": "open", "vraag": "Geef de Franse vertaling van de vraag: <b>'Wat doe je in het weekend?'</b>", "sleutelwoorden": ["qu'est-ce que tu fais/fais-tu", "le weekend/le week-end"], "minTreffers": 2, "modelantwoord": "Qu'est-ce que tu fais le weekend?", "uitleg": "'Qu'est-ce que tu fais le weekend?' is de standaardvraag."},
            {"type": "open", "vraag": "Vertaal naar het Frans: <b>'Omdat ik met mijn vrienden sport.'</b>", "sleutelwoorden": ["parce que", "fais du sport/sport", "mes amis/copains"], "minTreffers": 2, "modelantwoord": "Parce que je fais du sport avec mes amis (of: avec mes copains).", "uitleg": "'Parce que je fais du sport avec mes amis.'"}
        ]
    },
    {
        "id": "ex-h3-frans-u2-v4",
        "hoofdstuk": 2,
        "hoofdstukTitel": "Unité 2 — Du temps pour moi",
        "titel": "Grammatica 4 · p. 89 (D & H) · à/de + lidwoord & werkwoorden op -ir",
        "vak": "Frans · HAVO 3 (U2)",
        "icoon": "📐",
        "duurMin": 20,
        "vragen": [
            # 12 MC (balanced: 3 A, 3 B, 3 C, 3 D)
            {"type": "mc", "vraag": "Wat is de juiste samentrekking van <b>à + les</b> in het Frans?", "opties": ["aux", "au", "des", "à les"], "antwoord": 0, "uitleg": "à + les wordt altijd verplicht samengetrokken tot 'aux'."},
            {"type": "mc", "vraag": "Kies de juiste vorm: <i>Je vais ... supermarché (le supermarché).</i>", "opties": ["à la", "au", "aux", "à l'"], "antwoord": 1, "uitleg": "Omdat 'supermarché' mannelijk is (le), wordt à + le samengetrokken tot 'au'."},
            {"type": "mc", "vraag": "Kies de juiste vorm: <i>C'est la voiture ... voisins (les voisins).</i>", "opties": ["du", "de la", "des", "de les"], "antwoord": 2, "uitleg": "de + les voisins wordt samengetrokken tot 'des voisins'."},
            {"type": "mc", "vraag": "Wat gebeurt er met <b>à</b> wanneer het voor een vrouwelijk woord staat (bijv. <i>la maison</i>)?", "opties": ["Het wordt 'au'", "Het wordt 'aux'", "Het wordt 'ala'", "Het blijft onveranderd 'à la'"], "antwoord": 3, "uitleg": "Alleen bij le en les treedt samentrekking op; bij la blijft het los 'à la maison'."},
            {"type": "mc", "vraag": "Wat is de juiste vorm van het werkwoord <b>finir</b> bij <b>nous</b> (présent)?", "opties": ["nous finissons", "nous finis", "nous finissent", "nous finissez"], "antwoord": 0, "uitleg": "De uitgang voor nous bij regelmatige -ir werkwoorden is -issons: nous finissons."},
            {"type": "mc", "vraag": "Wat is de juiste vorm van het werkwoord <b>choisir</b> bij <b>tu</b> (présent)?", "opties": ["tu choisies", "tu choisis", "tu choisit", "tu choisissons"], "antwoord": 1, "uitleg": "Bij 'tu' is de uitgang -is: tu choisis."},
            {"type": "mc", "vraag": "Wat is de juiste vorm van <b>réfléchir</b> bij <b>ils</b> (présent)?", "opties": ["ils réfléchit", "ils réfléchissons", "ils réfléchissent", "ils réfléchi"], "antwoord": 2, "uitleg": "Bij ils/elles is de uitgang -issent: ils réfléchissent."},
            {"type": "mc", "vraag": "Hoe maak je de passé composé van het werkwoord <b>choisir</b> (<i>Ik heb gekozen</i>)?", "opties": ["Je choisissais", "J'ai choisit", "J'ai choisu", "J'ai choisi"], "antwoord": 3, "uitleg": "De passé composé van kiezen is 'avoir' + 'choisi' (voltooid deelwoord op -i)."},
            {"type": "mc", "vraag": "Kies het juiste voorzetsel met lidwoord: <i>C'est l'entrée ... collège (le collège).</i>", "opties": ["du", "de la", "des", "de l'"], "antwoord": 0, "uitleg": "de + le collège wordt samengetrokken tot 'du collège'."},
            {"type": "mc", "vraag": "Kies de juiste vorm: <i>Elle va ... piscine (la piscine).</i>", "opties": ["au", "à la", "aux", "à l'"], "antwoord": 1, "uitleg": "Voor een vrouwelijk woord blijft het 'à la piscine'."},
            {"type": "mc", "vraag": "Wat is de stam van het werkwoord <b>finir</b>?", "opties": ["f-", "fini-", "fin-", "finis-"], "antwoord": 2, "uitleg": "Haal de letters '-ir' weg en je houdt de stam 'fin-' over."},
            {"type": "mc", "vraag": "Welk ander Frans werkwoord wordt op exact dezelfde wijze vervoegd als <b>finir</b>?", "opties": ["partir", "sortir", "dormir", "réussir"], "antwoord": 3, "uitleg": "'Réussir' (slagen) hoort bij de regelmatige groep van finir (réussis, réussissons). Partir, sortir en dormir zijn onregelmatig."},
            # 4 Waaronwaar (at least 2 false)
            {"type": "waaronwaar", "vraag": "Het voltooid deelwoord van regelmatige -ir werkwoorden (zoals finir en choisir) eindigt op -i zonder accent.", "antwoord": True, "uitleg": "Waar. Fini en choisi eindigen op een gewone -i."},
            {"type": "waaronwaar", "vraag": "De combinatie <b>de + la</b> wordt in het Frans samengetrokken tot 'dula'.", "antwoord": False, "uitleg": "Onwaar. 'De la' trekt nooit samen en blijft altijd twee losse woorden."},
            {"type": "waaronwaar", "vraag": "Bij <b>vous</b> eindigt de tegenwoordige tijd van finir op <b>-issez</b> (vous finissez).", "antwoord": True, "uitleg": "Waar. De uitgang bij vous is -issez."},
            {"type": "waaronwaar", "vraag": "De combinatie <b>à + le</b> blijft in het Frans altijd als 'à le' geschreven.", "antwoord": False, "uitleg": "Onwaar. 'À le' bestaat niet in goed Frans; het moet verplicht worden samengetrokken tot 'au'."},
            # 2 Invul
            {"type": "invul", "vraag": "Vul de juiste samentrekking van de + le in (<i>C'est le prof ... lycée</i>):", "antwoord": "du", "uitleg": "de + le trekt samen tot 'du'."},
            {"type": "invul", "vraag": "Vul de juiste vorm van het werkwoord finir in bij 'il' (présent): <i>Il ... son travail.</i>", "antwoord": "finit", "uitleg": "De vorm bij il/elle is 'finit' (met een -t)."},
            # 2 Open
            {"type": "open", "vraag": "Leg uit welke samentrekkingen ontstaan wanneer het voorzetsel <b>à</b> wordt gevolgd door <b>le</b> en wanneer het wordt gevolgd door <b>les</b>.", "sleutelwoorden": ["au", "aux"], "minTreffers": 2, "modelantwoord": "à + le wordt samengetrokken tot 'au' en à + les wordt samengetrokken tot 'aux'.", "uitleg": "à + le = au; à + les = aux."},
            {"type": "open", "vraag": "Geef de vervoeging van het werkwoord <b>choisir</b> bij de personen <b>nous</b> en <b>vous</b> in de tegenwoordige tijd.", "sleutelwoorden": ["nous choisissons", "vous choisissez"], "minTreffers": 2, "modelantwoord": "Nous choisissons en vous choisissez.", "uitleg": "De vormen zijn nous choisissons en vous choisissez."}
        ]
    },
    {
        "id": "ex-h3-frans-u2-v5",
        "hoofdstuk": 2,
        "hoofdstukTitel": "Unité 2 — Du temps pour moi",
        "titel": "Integrale Toets Unité 2 · Vocabulaire, Phrases-clés & Grammaire",
        "vak": "Frans · HAVO 3 (U2)",
        "icoon": "🎯",
        "duurMin": 25,
        "vragen": [
            # 12 MC (balanced: 3 A, 3 B, 3 C, 3 D)
            {"type": "mc", "vraag": "Wat betekent de uitspraak in de tekst: <i>'Pendant les vacances, les élèves font la grasse matinée'</i>?", "opties": ["uitslapen in de ochtend", "vroeg ontbijten", "iedere ochtend sporten", "kranten bezorgen"], "antwoord": 0, "uitleg": "'Faire la grasse matinée' betekent lekker uitslapen in de ochtend."},
            {"type": "mc", "vraag": "Welke samentrekking past in de zin: <i>Je vais ... cinéma avec mes copains.</i>", "opties": ["à la", "au", "aux", "de"], "antwoord": 1, "uitleg": "Le cinéma is mannelijk, dus à + le wordt 'au cinéma'."},
            {"type": "mc", "vraag": "In een recensie staat: <i>'Ce film était vraiment ennuyeux'</i>. Wat vond de recensent van de film?", "opties": ["heel spannend", "ontzettend grappig", "heel saai", "buitengewoon leerzaam"], "antwoord": 2, "uitleg": "'Ennuyeux' betekent saai."},
            {"type": "mc", "vraag": "Wat is de juiste vorm van het werkwoord <b>finir</b> bij <b>ils</b>?", "opties": ["ils finit", "ils finis", "ils finissons", "ils finissent"], "antwoord": 3, "uitleg": "Bij ils/elles is de uitgang -issent: ils finissent."},
            {"type": "mc", "vraag": "Wat wil Sophie zeggen met: <i>'J'ai envie d'un grand chocolat chaud'</i>?", "opties": ["ik heb zin in een grote warme chocolademelk", "ik heb tijd voor warme chocolademelk", "ik ben bang voor warme chocolademelk", "ik heb chocolademelk nodig"], "antwoord": 0, "uitleg": "'Avoir envie de' betekent zin hebben in / om."},
            {"type": "mc", "vraag": "Hoe vertaal je: <i>'Ik heb er een hekel aan om mijn kamer op te ruimen'</i>?", "opties": ["J'aime ranger ma chambre", "Je déteste ranger ma chambre", "Je range ma chambre", "Ma chambre est propre"], "antwoord": 1, "uitleg": "'Je déteste ranger ma chambre' betekent dat je een hekel hebt aan opruimen."},
            {"type": "mc", "vraag": "Kies de juiste samentrekking: <i>C'est le livre ... professeur (le professeur).</i>", "opties": ["de la", "des", "du", "de l'"], "antwoord": 2, "uitleg": "de + le professeur wordt 'du professeur'."},
            {"type": "mc", "vraag": "In een strip roept iemand uit: <i>'Ce bruit me rend fou !'</i> Wat betekent dat?", "opties": ["dat geluid is erg mooi", "ik hoor dat geluid niet", "dat geluid maakt me blij", "van dat geluid word ik helemaal gek"], "antwoord": 3, "uitleg": "'Ça me rend fou' betekent letterlijk 'dat maakt me gek'."},
            {"type": "mc", "vraag": "Wat is de passé composé van <b>choisir</b> bij 'j'ai'?", "opties": ["choisi", "choisu", "choisé", "choisissant"], "antwoord": 0, "uitleg": "Regelmatige -ir werkwoorden krijgen een voltooid deelwoord op -i: j'ai choisi."},
            {"type": "mc", "vraag": "Wat betekent de Franse term <b>'passer son temps libre'</b>?", "opties": ["je werktijd inhalen", "je vrije tijd doorbrengen", "je schooljaar plannen", "je wekker zetten"], "antwoord": 1, "uitleg": "'Passer son temps libre' betekent je vrije tijd doorbrengen."},
            {"type": "mc", "vraag": "Wat vraagt Thomas wanneer hij zegt: <i>'Qu'est-ce que tu fais d'autre le mercredi?'</i>", "opties": ["Waarom ga je op woensdag weg?", "Met wie fiets je op woensdag?", "Wat doe je nog meer op woensdag?", "Hoeveel kost sporten op woensdag?"], "antwoord": 2, "uitleg": "'Qu'est-ce que tu fais d'autre?' vraagt wat je daarnaast/verder nog doet."},
            {"type": "mc", "vraag": "Wat is de betekenis van het Franse tijdwoordje <b>'tôt'</b>?", "opties": ["laat", "nooit", "soms", "vroeg"], "antwoord": 3, "uitleg": "'Tôt' betekent vroeg."},
            # 4 Waaronwaar (at least 2 false)
            {"type": "waaronwaar", "vraag": "De combinatie <b>de + les</b> wordt in het Frans samengetrokken tot <b>des</b>.", "antwoord": True, "uitleg": "Waar. Bijvoorbeeld: le chien des voisins."},
            {"type": "waaronwaar", "vraag": "Het Franse woord <b>'passionnant'</b> betekent 'saai en slaapverwekkend'.", "antwoord": False, "uitleg": "Onwaar. 'Passionnant' betekent 'boeiend / meeslepend'; 'saai' is 'ennuyeux'."},
            {"type": "waaronwaar", "vraag": "Bij het werkwoord <b>finir</b> is de vorm bij <b>nous</b> 'nous finissons'.", "antwoord": True, "uitleg": "Waar. De uitgang bij nous is -issons."},
            {"type": "waaronwaar", "vraag": "De uitdrukking <b>'faire les courses'</b> betekent uitsluitend hardlopen in een stadion.", "antwoord": False, "uitleg": "Onwaar. 'Faire les courses' is de vaste uitdrukking voor dagelijkse boodschappen doen."},
            # 2 Invul
            {"type": "invul", "vraag": "Vul de juiste samentrekking van à + les in: <i>Nous allons ... Pays-Bas.</i>", "antwoord": "aux", "uitleg": "à + les wordt 'aux'."},
            {"type": "invul", "vraag": "Vertaal het woord <i>'gamen'</i> naar het Frans (p. 86): <i>jouer à la ...</i>", "antwoord": "console", "uitleg": "'Gamen' is 'jouer à la console'."},
            # 2 Open
            {"type": "open", "vraag": "Hoe vraag je in het Frans naar iemands favoriete serie?", "sleutelwoorden": ["quelle est", "série préférée/serie preferee"], "minTreffers": 2, "modelantwoord": "Quelle est ta série préférée?", "uitleg": "'Quelle est ta série préférée?' is de vaste formulering."},
            {"type": "open", "vraag": "Vertaal naar het Frans: <b>'Ik vind het leuk om te sporten.'</b>", "sleutelwoorden": ["j'aime", "faire du sport/le sport"], "minTreffers": 2, "modelantwoord": "J'aime faire du sport.", "uitleg": "'J'aime faire du sport' betekent 'Ik vind het leuk om te sporten'."}
        ]
    }
]

def generate():
    # 1. Write onderwerpen (h2_1 t/m h2_4)
    for o in ONDERWERPEN:
        p_num = o["paragraaf"].split(".")[1]
        filename = f"h2_{p_num}.js"
        filepath = os.path.join(DATA_DIR, filename)
        content = f"/* =========================================================\n"
        content += f"   Duru's Frans Academie — §{o['paragraaf']} {o['titel']}\n"
        content += f"   Grandes Lignes 3 HAVO — Unité 2 (p. 86-89)\n"
        content += f"   ========================================================= */\n"
        content += f"DURU.register({json.dumps(o, ensure_ascii=False, indent=2)});\n"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated {filepath}")

    # 2. Write examens (examen_u2_vocab_1 t/m 5)
    for i, ex in enumerate(EXAMENS, start=1):
        filename = f"examen_u2_vocab_{i}.js"
        filepath = os.path.join(DATA_DIR, filename)
        content = f"/* =========================================================\n"
        content += f"   Duru's Frans Academie — {ex['titel']}\n"
        content += f"   Grandes Lignes 3 HAVO — Unité 2\n"
        content += f"   ========================================================= */\n"
        content += f"DURU.registerExamen({json.dumps(ex, ensure_ascii=False, indent=2)});\n"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated {filepath}")

if __name__ == "__main__":
    generate()

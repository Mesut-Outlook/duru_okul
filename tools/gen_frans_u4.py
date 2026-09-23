#!/usr/bin/env python3
"""
gen_frans_u4.py — Volledige generator voor Frans Unité 4 (Le pont)
onderwerpen (h4_1..h4_4) en proeftoetsen (examen_u4_vocab_1..5)
op basis van Grandes Lignes 3 HAVO Unité 4 (TASK-15).
"""
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "havo3", "frans", "js", "data")

ONDERWERPEN = [
    # H4 §4.1
    {
        "id": "fr-u4-1",
        "hoofdstuk": 4,
        "paragraaf": "4.1",
        "titel": "Herhaling Ch 1 · Sociale media, bijvoeglijk naamwoord & werkwoorden op -er",
        "korteUitleg": "Herhaling van Unité 1: woordenschat rond communicatie en vriendschap, de vorm en plaats van het bijvoeglijk naamwoord, en regelmatige werkwoorden op -er.",
        "icoon": "📱",
        "kleur": "blauw",
        "theorie": """
    <h3>4.1 Herhaling Ch 1: Sociale media, bijvoeglijk naamwoord & werkwoorden op -er</h3>
    <div class="info-box">
      <b>Le pont (De brug):</b> In Unité 4 herhaal en verdiep je de kernstof uit de eerste drie hoofdstukken van <i>Grandes Lignes 3 HAVO</i>. In deze eerste paragraaf ligt de focus op de woordenschat en grammatica van <b>Unité 1 (Poste, like, partage)</b>.
    </div>

    <h4>1. Kernwoordenschat Unité 1 (Sociale media & communicatie)</h4>
    <table class="vocab-tabel" style="width:100%;border-collapse:collapse;margin:12px 0;">
      <tr style="background:#e8f0fe;">
        <th style="padding:6px;border:1px solid #ccc;">Frans 🇫🇷</th>
        <th style="padding:6px;border:1px solid #ccc;">Nederlands 🇳🇱</th>
        <th style="padding:6px;border:1px solid #ccc;">Voorbeeldzin</th>
      </tr>
      <tr><td style="padding:6px;border:1px solid #ccc;"><b>le message</b></td><td style="padding:6px;border:1px solid #ccc;">het bericht / appje</td><td style="padding:6px;border:1px solid #ccc;">J'ai reçu un message sur mon portable.</td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc;"><b>l'appli (v) / l'application</b></td><td style="padding:6px;border:1px solid #ccc;">de app / applicatie</td><td style="padding:6px;border:1px solid #ccc;">Cette appli est très populaire chez les jeunes.</td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc;"><b>l'écran (m)</b></td><td style="padding:6px;border:1px solid #ccc;">het scherm</td><td style="padding:6px;border:1px solid #ccc;">Il passe trop d'heures devant l'écran.</td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc;"><b>le portable</b></td><td style="padding:6px;border:1px solid #ccc;">de mobiele telefoon</td><td style="padding:6px;border:1px solid #ccc;">N'oublie pas ton portable à la maison!</td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc;"><b>discuter / bavarder</b></td><td style="padding:6px;border:1px solid #ccc;">discussiëren / kletsen</td><td style="padding:6px;border:1px solid #ccc;">Nous bavardons souvent pendant la récréation.</td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc;"><b>les réseaux sociaux (m mv)</b></td><td style="padding:6px;border:1px solid #ccc;">de sociale media</td><td style="padding:6px;border:1px solid #ccc;">Les ados sont très actifs sur les réseaux sociaux.</td></tr>
    </table>

    <h4>2. Grammatica: Vorm en plaats van het bijvoeglijk naamwoord (l'adjectif)</h4>
    <p>In het Frans past het bijvoeglijk naamwoord zich aan in <b>geslacht</b> (mannelijk/vrouwelijk) en <b>getal</b> (enkelvoud/meervoud):</p>
    <ul>
      <li>Vrouwelijk krijgt meestal een <b>-e</b>: <i>un ami sportif ➔ une amie sportive</i>; <i>un garçon intelligent ➔ une fille intelligente</i>.</li>
      <li>Meervoud krijgt meestal een <b>-s</b>: <i>des amis sportifs</i>; <i>des filles intelligentes</i>.</li>
      <li>Onregelmatige vrouwelijke vormen: <i>ambitieux ➔ ambitieuse</i>; <i>délicieux ➔ délicieuse</i>; <i>beau ➔ belle</i>; <i>vieux ➔ vieille</i>; <i>nouveau ➔ nouvelle</i>; <i>bon ➔ bonne</i>.</li>
    </ul>
    <div class="formule-box">
      <b>Plaats van het bijvoeglijk naamwoord:</b><br>
      • De <i>meeste</i> Franse bijvoeglijk naamwoorden staan <b>ACHTER</b> het zelfstandig naamwoord (kleuren, nationaliteiten, vorm): <i>une robe rouge, une famille algérienne</i>.<br>
      • Een klein groepje korte, veelgebruikte bijvoeglijk naamwoorden staat <b>VÓÓR</b> het zelfstandig naamwoord (ezelsbruggetje BAGS: Beauty, Age, Goodness, Size): <b>beau, joli, jeune, vieux, bon, mauvais, grand, petit</b>.<br>
      <i>Voorbeeld:</i> <code>une grande maison</code>, <code>un bonbon délicieux</code>, <code>un beau jour</code>.
    </div>

    <h4>3. Regelmatige werkwoorden op -er (Présent)</h4>
    <p>De uitgangen in de tegenwoordige tijd (Présent) voor werkwoorden zoals <i>regarder, parler, aimer, partager</i>:</p>
    <ul>
      <li>je regard<b>e</b> | tu regard<b>es</b> | il/elle/on regard<b>e</b></li>
      <li>nous regard<b>ons</b> | vous regard<b>ez</b> | ils/elles regard<b>ent</b> (de uitgang -ent spreek je niet uit!)</li>
    </ul>
""",
        "vragen": [
            {
                "type": "mc",
                "vraag": "Kies de juiste vrouwelijke vorm: 'Leila est une fille très ____ (sportief).'",
                "opties": [
                    "sportif",
                    "sportive",
                    "sportifs",
                    "sportives"
                ],
                "antwoord": 1,
                "uitleg": "Bij een vrouwelijk zelfstandig naamwoord (une fille) wordt 'sportif' veranderd in 'sportive'."
            },
            {
                "type": "mc",
                "vraag": "Welk bijvoeglijk naamwoord staat in het Frans gewoonlijk VÓÓR het zelfstandig naamwoord?",
                "opties": [
                    "algérien",
                    "rouge",
                    "grand",
                    "délicieux"
                ],
                "antwoord": 2,
                "uitleg": "'Grand' hoort bij de korte veelgebruikte adjectieven die vóór het zelfstandig naamwoord staan (une grande maison)."
            },
            {
                "type": "mc",
                "vraag": "Wat is de juiste vorm voor 'wij kletsen' van het regelmatige werkwoord bavarder?",
                "opties": [
                    "nous bavardez",
                    "nous bavardent",
                    "nous bavarde",
                    "nous bavardons"
                ],
                "antwoord": 3,
                "uitleg": "De uitgang bij 'nous' in de tegenwoordige tijd van een -er werkwoord is altijd '-ons'."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de Franse uitdrukking 'les réseaux sociaux'?",
                "opties": [
                    "de sociale media",
                    "de mobiele abonnementen",
                    "de computerkabels",
                    "de internetbrowsers"
                ],
                "antwoord": 0,
                "uitleg": "'Les réseaux sociaux' zijn de sociale media (zoals Instagram, TikTok, Snapchat)."
            },
            {
                "type": "waaronwaar",
                "vraag": "In het Frans staan alle bijvoeglijk naamwoorden zonder uitzondering altijd achter het zelfstandig naamwoord.",
                "antwoord": False,
                "uitleg": "Onwaar! Korte adjectieven zoals grand, petit, beau, vieux en bon staan vóór het zelfstandig naamwoord."
            },
            {
                "type": "waaronwaar",
                "vraag": "De vrouwelijke vorm van het Franse bijvoeglijk naamwoord 'ambitieux' is 'ambitieuse'.",
                "antwoord": True,
                "uitleg": "Waar! Mannelijk -eux wordt in het vrouwelijk -euse (ambitieux ➔ ambitieuse)."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Franse zelfstandig naamwoord 'le message' is een vrouwelijk woord.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Le message' is mannelijk (le message, un message)."
            },
            {
                "type": "invoer",
                "vraag": "Vul de juiste vorm van het bijvoeglijk naamwoord 'beau' in voor een vrouwelijk enkelvoud: 'Elle porte une ____ (mooie) robe le jour de son mariage.'",
                "antwoord": "belle",
                "uitleg": "De vrouwelijke vorm van 'beau' is 'belle'."
            },
            {
                "type": "invoer",
                "vraag": "Vertaal het woord tussen haakjes: 'Il passe beaucoup de temps devant (het scherm).' Vul het Franse woord in met lidwoord (l'écran).",
                "antwoord": "l'écran|l'ecran|ecran|écran",
                "uitleg": "Het scherm is in het Frans 'l'écran'."
            },
            {
                "type": "invoer",
                "vraag": "Vul de juiste vervoeging in van 'partager' bij 'ils': 'Ils ____ (delen) des photos sur Instagram.'",
                "antwoord": "partagent",
                "uitleg": "Bij 'ils/elles' is de uitgang van een -er werkwoord '-ent' (partagent)."
            }
        ]
    },

    # H4 §4.2
    {
        "id": "fr-u4-2",
        "hoofdstuk": 4,
        "paragraaf": "4.2",
        "titel": "Herhaling Ch 2 · Vrije tijd, series, werkwoorden op -ir & samentrekkingen à/de",
        "korteUitleg": "Herhaling van Unité 2: woordenschat rond series en televisie, regelmatige werkwoorden op -ir (finir/choisir) en samentrekkingen met à (au/aux) en de (du/des).",
        "icoon": "🎸",
        "kleur": "oranje",
        "theorie": """
    <h3>4.2 Herhaling Ch 2: Vrije tijd, series, werkwoorden op -ir & samentrekkingen à/de</h3>
    <div class="info-box">
      <b>Focus:</b> Herhaling en synthese van <b>Unité 2 (Du temps pour moi)</b>. We bestuderen de woordenschat over televisieseries en vrije tijd, de regelmatige werkwoorden op <i>-ir</i> (zoals <i>finir</i> en <i>choisir</i>), en het correct samentrekken van de voorzetsels <i>à</i> en <i>de</i> met lidwoorden.
    </div>

    <h4>1. Woordenschat: Series, Televisie & Bezigheden (p. 138-140)</h4>
    <ul>
      <li><b>la série:</b> de televisieserie | <b>l'épisode (m):</b> de aflevering</li>
      <li><b>la saison:</b> het seizoen (van een serie) | <b>passionnant(e):</b> boeiend, meeslepend</li>
      <li><b>beaucoup de gens:</b> veel mensen | <b>le monde entier:</b> de hele wereld</li>
      <li><b>avoir du succès:</b> succes hebben | <b>attendre:</b> wachten op (<i>j'attends la suite</i>)</li>
      <li><b>le cerveau:</b> de hersenen | <b>la tête:</b> het hoofd | <b>l'argent (m):</b> het geld</li>
    </ul>

    <h4>2. Regelmatige werkwoorden op -ir (Présent & Passé composé)</h4>
    <p>Werkwoorden zoals <i>finir</i> (eindigen), <i>choisir</i> (kiezen), <i>réussir</i> (slagen/lukken), <i>rougir</i> (blozen) en <i>obéir</i> (gehoorzamen) volgen een vast schema:</p>
    <table class="vocab-tabel" style="width:100%;border-collapse:collapse;margin:12px 0;">
      <tr style="background:#fff3e0;">
        <th style="padding:6px;border:1px solid #ccc;">Persoon</th>
        <th style="padding:6px;border:1px solid #ccc;">Présent (finir)</th>
        <th style="padding:6px;border:1px solid #ccc;">Présent (choisir)</th>
        <th style="padding:6px;border:1px solid #ccc;">Passé composé</th>
      </tr>
      <tr><td style="padding:6px;border:1px solid #ccc;">je / j'</td><td style="padding:6px;border:1px solid #ccc;">je fin<b>is</b></td><td style="padding:6px;border:1px solid #ccc;">je chois<b>is</b></td><td style="padding:6px;border:1px solid #ccc;">j'ai fin<b>i</b></td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc;">tu</td><td style="padding:6px;border:1px solid #ccc;">tu fin<b>is</b></td><td style="padding:6px;border:1px solid #ccc;">tu chois<b>is</b></td><td style="padding:6px;border:1px solid #ccc;">tu as fin<b>i</b></td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc;">il / elle / on</td><td style="padding:6px;border:1px solid #ccc;">il fin<b>it</b></td><td style="padding:6px;border:1px solid #ccc;">il chois<b>it</b></td><td style="padding:6px;border:1px solid #ccc;">il a fin<b>i</b></td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc;">nous</td><td style="padding:6px;border:1px solid #ccc;">nous fin<b>issons</b></td><td style="padding:6px;border:1px solid #ccc;">nous chois<b>issons</b></td><td style="padding:6px;border:1px solid #ccc;">nous avons fin<b>i</b></td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc;">vous</td><td style="padding:6px;border:1px solid #ccc;">vous fin<b>issez</b></td><td style="padding:6px;border:1px solid #ccc;">vous chois<b>issez</b></td><td style="padding:6px;border:1px solid #ccc;">vous avez fin<b>i</b></td></tr>
      <tr><td style="padding:6px;border:1px solid #ccc;">ils / elles</td><td style="padding:6px;border:1px solid #ccc;">ils fin<b>issent</b></td><td style="padding:6px;border:1px solid #ccc;">ils chois<b>issent</b></td><td style="padding:6px;border:1px solid #ccc;">ils ont fin<b>i</b></td></tr>
    </table>
    <p><i>Het voltooid deelwoord (participe passé) eindigt altijd op <b>-i</b>: fini, choisi, réussi, rougi, grandi.</i></p>

    <h4>3. Grammatica: Samentrekkingen met à en de (les articles contractés)</h4>
    <div class="formule-box">
      <b>Samentrekkingen met à (naar / aan / in):</b><br>
      • à + le ➔ <b>au</b>: <i>Je vais <b>au</b> collège / <b>au</b> restaurant / <b>au</b> parc.</i><br>
      • à + la ➔ <b>à la</b>: <i>Je vais <b>à la</b> boulangerie / <b>à la</b> piscine.</i><br>
      • à + l' ➔ <b>à l'</b>: <i>Je vais <b>à l'</b>école / <b>à l'</b>hôtel / <b>à l'</b>entraînement.</i><br>
      • à + les ➔ <b>aux</b>: <i>Je vais <b>aux</b> toilettes / <b>aux</b> tournois de tennis.</i><br><br>
      <b>Samentrekkingen met de (van / uit):</b><br>
      • de + le ➔ <b>du</b>: <i>Le chien <b>du</b> voisin / le prof <b>du</b> collège.</i><br>
      • de + la ➔ <b>de la</b>: <i>La maison <b>de la</b> famille Bélier.</i><br>
      • de + l' ➔ <b>de l'</b>: <i>Le vélo <b>de l'</b>élève / la porte <b>de l'</b>hôtel.</i><br>
      • de + les ➔ <b>des</b>: <i>Les affaires <b>des</b> enfants / les amis <b>des</b> filles.</i>
    </div>
""",
        "vragen": [
            {
                "type": "mc",
                "vraag": "Kies de juiste samentrekking: 'Tous les samedis, les enfants vont ____ (naar de) piscine.'",
                "opties": [
                    "à la",
                    "au",
                    "aux",
                    "à l'"
                ],
                "antwoord": 0,
                "uitleg": "'Piscine' is vrouwelijk (la piscine), dus à + la blijft 'à la piscine'."
            },
            {
                "type": "mc",
                "vraag": "Wat is de juiste vorm van het werkwoord 'choisir' bij 'vous' in de tegenwoordige tijd?",
                "opties": [
                    "vous choisis",
                    "vous choisissez",
                    "vous choisissons",
                    "vous choisit"
                ],
                "antwoord": 1,
                "uitleg": "Bij 'vous' krijgt een regelmatig -ir werkwoord de uitgang '-issez' (vous choisissez)."
            },
            {
                "type": "mc",
                "vraag": "Kies de juiste vorm: 'C'est le cahier ____ (van de) élève.'",
                "opties": [
                    "du",
                    "de la",
                    "de l'",
                    "des"
                ],
                "antwoord": 2,
                "uitleg": "Voor een klinker (élève) gebruik je 'de l''."
            },
            {
                "type": "mc",
                "vraag": "Wat is het voltooid deelwoord (participe passé) van het werkwoord 'réussir'?",
                "opties": [
                    "réussé",
                    "réussu",
                    "réussissant",
                    "réussi"
                ],
                "antwoord": 3,
                "uitleg": "Regelmatige werkwoorden op -ir hebben een voltooid deelwoord op -i: 'réussi'."
            },
            {
                "type": "waaronwaar",
                "vraag": "In het Frans schrijf je 'à le restaurant' als je 'naar het restaurant' bedoelt.",
                "antwoord": False,
                "uitleg": "Onwaar! 'à + le' trekt verplicht samen tot 'au' (au restaurant)."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Franse zelfstandig naamwoord 'l'épisode' is een mannelijk woord.",
                "antwoord": True,
                "uitleg": "Waar! Je zegt 'un épisode' (mannelijk)."
            },
            {
                "type": "waaronwaar",
                "vraag": "De uitgang bij 'ils/elles' voor het werkwoord 'finir' in de présent is '-ent' (ils finent).",
                "antwoord": False,
                "uitleg": "Onwaar! De uitgang is '-issent': 'ils finissent'."
            },
            {
                "type": "invoer",
                "vraag": "Vul de juiste samentrekking van 'à + le' in: 'Mon père va tous les jours ____ collège à vélo.'",
                "antwoord": "au",
                "uitleg": "De combinatie van het voorzetsel à met het mannelijk lidwoord le trekt verplicht samen tot 'au'."
            },
            {
                "type": "invoer",
                "vraag": "Vul de persoonsvorm in van 'finir' bij 'tu' in de tegenwoordige tijd: 'Tu ____ (eindigt) à quelle heure aujourd'hui?'",
                "antwoord": "finis",
                "uitleg": "Bij 'tu' is de uitgang -is: 'tu finis'."
            },
            {
                "type": "invoer",
                "vraag": "Vul de juiste samentrekking van 'de + les' in: 'Voilà les chambres ____ enfants.'",
                "antwoord": "des",
                "uitleg": "de + les = 'des'."
            }
        ]
    },

    # H4 §4.3
    {
        "id": "fr-u4-3",
        "hoofdstuk": 4,
        "paragraaf": "4.3",
        "titel": "Herhaling Ch 3 · Reizen, passé composé met avoir/être & lijdend voorwerp (le/la/l'/les)",
        "korteUitleg": "Herhaling van Unité 3: reizen en steden, de vorming van de passé composé met avoir en être (inclusief accord), en persoonlijke voornaamwoorden als lijdend voorwerp.",
        "icoon": "🚆",
        "kleur": "groen",
        "theorie": """
    <h3>4.3 Herhaling Ch 3: Reizen, passé composé met avoir/être & lijdend voorwerp</h3>
    <div class="info-box">
      <b>Synthese Unité 3 (En route!):</b> In deze paragraaf combineren we de reistermen met de belangrijkste werkwoordstijd in de onderbouw: de <b>passé composé</b> met zowel <i>avoir</i> als <i>être</i>, én het lijdend voorwerp (COD: <i>le, la, l', les</i>).
    </div>

    <h4>1. Passé composé met avoir vs. être</h4>
    <p>De meeste Franse werkwoorden vormen de passé composé met <b>avoir</b> (hebben):</p>
    <ul>
      <li><i>j'ai regardé</i> (ik heb gekeken) | <i>tu as attendu</i> (jij hebt gewacht) | <i>il a choisi</i> (hij heeft gekozen)</li>
      <li>Belangrijke onregelmatige deelwoorden: <b>eu</b> (gehad), <b>été</b> (geweest), <b>fait</b> (gedaan/gemaakt), <b>pris</b> (genomen), <b>vu</b> (gezien), <b>bu</b> (gedronken).</li>
    </ul>

    <p>Een vaste groep werkwoorden van <b>beweging en verandering van toestand</b> vormt de passé composé met <b>être</b> (zijn):</p>
    <div class="formule-box">
      <b>Être-werkwoorden (met accord van het onderwerp!):</b><br>
      • <b>aller</b> (gaan) ➔ <i>Hugo est allé au cinéma. / Laura est allé<b>e</b> au musée.</i><br>
      • <b>rester</b> (blijven) ➔ <i>Elles sont resté<b>es</b> à la maison.</i><br>
      • <b>monter</b> (naar boven gaan) ➔ <i>Ils sont monté<b>s</b> au troisième étage de la tour Eiffel.</i><br>
      • <b>descendre</b> (naar beneden gaan) ➔ <i>Nous sommes descendu<b>s</b> du train.</i><br>
      • <b>partir</b> (vertrekken) ➔ <i>Mes cousines sont parti<b>es</b> hier.</i><br>
      • <b>arriver</b> (aankomen), <b>entrer</b> (binnengaan), <b>sortir</b> (naar buiten gaan), <b>venir</b> (komen), <b>tomber</b> (vallen).
    </div>
    <div class="info-box">
      <b>Het accord bij être:</b><br>
      Vrouwelijk enkelvoud krijgt een extra <b>-e</b> (<i>allée, restée</i>).<br>
      Mannelijk meervoud krijgt een extra <b>-s</b> (<i>allés, restés</i>).<br>
      Vrouwelijk meervoud krijgt <b>-es</b> (<i>allées, restées</i>).
    </div>

    <h4>2. Persoonlijk voornaamwoord als lijdend voorwerp (le, la, l', les)</h4>
    <p>Om herhaling van zelfstandige naamwoorden te voorkomen, gebruik je een voornaamwoord:</p>
    <ul>
      <li><b>le</b> = hem / het (mannelijk): <i>Tu regardes le film? ➔ Oui, je <b>le</b> regarde.</i></li>
      <li><b>la</b> = haar / het (vrouwelijk): <i>Tu aimes cette série? ➔ Oui, je <b>la</b> trouve passionnante.</i></li>
      <li><b>l'</b> = hem / haar / het (vóór een klinker of stomme h): <i>Il aime son prof? ➔ Non, il ne <b>l'</b>aime pas.</i></li>
      <li><b>les</b> = hen / ze (meervoud): <i>Tu fais les devoirs? ➔ Oui, je <b>les</b> fais tous les jours.</i></li>
    </ul>
    <p><b>Plaatsing:</b> Het voornaamwoord staat <b>DIRECT VÓÓR DE PERSOONSVORM</b> (of vóór de infinitief als er twee werkwoorden staan): <i>Je vais <b>la</b> regarder demain.</i></p>
""",
        "vragen": [
            {
                "type": "mc",
                "vraag": "Kies de juiste vorm van het voltooid deelwoord bij être: 'Manon et sa sœur sont ____ (gegaan) à Paris.'",
                "opties": [
                    "allé",
                    "allée",
                    "allés",
                    "allées"
                ],
                "antwoord": 3,
                "uitleg": "Het onderwerp 'Manon et sa sœur' is vrouwelijk meervoud, dus bij être krijgt allé de uitgang -es: 'allées'."
            },
            {
                "type": "mc",
                "vraag": "Vervang het lijdend voorwerp: 'Tu as vu le nouveau journal hier? ➔ Oui, je ____ ai vu.'",
                "opties": [
                    "l'",
                    "le",
                    "la",
                    "les"
                ],
                "antwoord": 0,
                "uitleg": "'Le journal' is mannelijk, maar voor de klinker 'a' van ai verandert 'le' in 'l''."
            },
            {
                "type": "mc",
                "vraag": "Welk hulpwerkwoord gebruikt het Franse werkwoord 'rester' in de passé composé?",
                "opties": [
                    "avoir",
                    "être",
                    "faire",
                    "aller"
                ],
                "antwoord": 1,
                "uitleg": "'Rester' vormt de passé composé altijd met être: 'Elle est restée'."
            },
            {
                "type": "mc",
                "vraag": "Waar plaats je het lijdend voorwerp 'les' in de zin 'Je vais regarder les épisodes demain'?",
                "opties": [
                    "Achteraan de zin: Je vais regarder demain les.",
                    "Voor de persoonsvorm: Je les vais regarder demain.",
                    "Direct vóór de infinitief: Je vais les regarder demain.",
                    "Tussen de twee werkwoorden met een koppelteken: Je vais-les-regarder."
                ],
                "antwoord": 2,
                "uitleg": "Als er een infinitief in de zin staat, komt het voornaamwoord direct vóór de infinitief te staan."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het werkwoord 'faire' heeft in de passé composé als voltooid deelwoord 'faisé'.",
                "antwoord": False,
                "uitleg": "Onwaar! Het voltooid deelwoord van faire is onregelmatig: 'fait' (j'ai fait)."
            },
            {
                "type": "waaronwaar",
                "vraag": "Bij werkwoorden die met 'avoir' vervoegd worden, krijgt het voltooid deelwoord normaal gesproken géén -e of -s voor het onderwerp.",
                "antwoord": True,
                "uitleg": "Waar! Bij avoir richt het voltooid deelwoord zich niet naar het onderwerp (Laura a mangé, ils ont mangé)."
            },
            {
                "type": "waaronwaar",
                "vraag": "In de zin 'Je ne l'aime pas' verwijst 'l'' naar een meervoudig zinsdeel.",
                "antwoord": False,
                "uitleg": "Onwaar! Voor een meervoud gebruik je 'les' (Je ne les aime pas). 'L'' is voor enkelvoud."
            },
            {
                "type": "invoer",
                "vraag": "Vul de juiste vorm van het voltooid deelwoord van 'rester' in: 'Emma est ____ (gebleven) chez sa grand-mère.' Denk aan het accord bij être!",
                "antwoord": "restée|restee",
                "uitleg": "Omdat Emma vrouwelijk enkelvoud is, krijgt resté een extra e: 'restée'."
            },
            {
                "type": "invoer",
                "vraag": "Vervang het onderstreepte woord door le, la, l' of les: 'Je regarde <u>la télévision</u> tous les soirs ➔ Je ____ regarde tous les soirs.'",
                "antwoord": "la",
                "uitleg": "'La télévision' is vrouwelijk enkelvoud, dus je vervangt het door 'la'."
            },
            {
                "type": "invoer",
                "vraag": "Vul het juiste hulpwerkwoord in (être of avoir in de juiste vorm): 'Ils ____ pris le bus pour aller au centre-ville.'",
                "antwoord": "ont",
                "uitleg": "'Prendre' vormt de passé composé met avoir: 'ils ont pris'."
            }
        ]
    },

    # H4 §4.4
    {
        "id": "fr-u4-4",
        "hoofdstuk": 4,
        "paragraaf": "4.4",
        "titel": "Le pont · DELF Vaardigheden, Literatuur (Résistance) & Cultuur (Stromae)",
        "korteUitleg": "DELF luister- en schrijfvaardigheid, Franse jeugdliteratuur over het Franse verzet en hedendaagse cultuur met chansonkritiek op sociale media.",
        "icoon": "🗼",
        "kleur": "paars",
        "theorie": """
    <h3>4.4 Le pont: DELF Vaardigheden, Literatuur (Résistance) & Cultuur (Stromae)</h3>
    <div class="info-box">
      <b>Doel van Le pont:</b> Naast grammatica en woordenschat test Unité 4 je praktische <b>Cito- en DELF-vaardigheden</b>. Je leert hoe je luisterfragmenten aanpakt, een persoonlijke Franse brief/e-mail opstelt en Franse cultuur en literatuur begrijpt.
    </div>

    <h4>1. DELF Examentraining: Luisteren & Schrijven (p. 150-154)</h4>
    <p>Bij het officiële Franse taalexamen <b>DELF (Diplôme d'Études en Langue Française)</b> let de examinator op vaste beoordelingscriteria:</p>
    <ul>
      <li><b>Compréhension orale (Luisteren):</b> Lees <i>altijd eerst de vragen</i> door voordat het geluidsfragment begint. Let op kernwoorden: wie praat er, waar zijn ze (gare, restaurant, école) en wat is de reden van het bericht?</li>
      <li><b>Production écrite (Schrijven):</b> Schrijf minimaal het gevraagde aantal woorden (bijv. 40-50 woorden voor niveau A1/A2). Gebruik vaste beleefdheidsvormen:
        <ul>
          <li>Aanhef informeel: <i>Cher Lucas / Chère Léa / Salut tout le monde!</i></li>
          <li>Inleiding: <i>Merci pour ton message / Comment vas-tu? Moi, je vais bien.</i></li>
          <li>Afsluiting: <i>Écris-moi vite! / À bientôt! / Bises / Amicalement.</i></li>
        </ul>
      </li>
    </ul>

    <h4>2. Literatuur: 'Les enfants de la résistance' & 'Silence' (p. 156-159)</h4>
    <p>In het literatuurgedeelte van Unité 4 lees je authentieke Franse fragmenten:</p>
    <ul>
      <li><b>Les enfants de la résistance:</b> Een beroemd Frans-Belgisch stripverhaal (BD) over drie dorpskinderen (François, Eusèbe en Lisa) die tijdens de Tweede Wereldoorlog in Frankrijk in het geheim verzet plegen tegen de Duitse bezetter (<i>l'occupant</i>). Ze verspreiden geheime krantjes en helpen vluchtelingen.</li>
      <li><b>Silence (p. 158):</b> Een gedicht en verhaal over het schoolleven, waar de lerares plotseling schreeuwt: <i>"Silence! Taisez-vous!"</i> (Stilte! Houd je mond!). Het toont de alledaagse emoties en humor van Franse scholieren.</li>
    </ul>

    <h4>3. Hedendaagse Franse Cultuur: Stromae — 'Carmen' (p. 162)</h4>
    <p>De Frans-Belgische artiest <b>Stromae</b> schreef het nummer <i>Carmen</i>, geïnspireerd op de beroemde opera van Georges Bizet:</p>
    <div class="formule-box">
      <i>"L'amour est comme l'oiseau de Twitter: on est bleu de lui, seulement pour 48 heures. D'abord on s'affilie, ensuite on se follow, on en devient fêlé, et puis on finit solo..."</i>
    </div>
    <p>Stromae levert scherpe maatschappijkritiek: we denken dat sociale media ons vrienden opleveren, maar in werkelijkheid maken ze ons verslaafd, eenzaam en oppervlakkig.</p>
""",
        "vragen": [
            {
                "type": "mc",
                "vraag": "Wat is een passende informele aanhef voor een Franse brief aan een vriendin bij een DELF-opdracht?",
                "opties": [
                    "Monsieur le Directeur,",
                    "Chère Léa,",
                    "À bientôt,",
                    "Bises,"
                ],
                "antwoord": 1,
                "uitleg": "'Chère Léa,' is de juiste informele aanhef voor een brief of e-mail aan een vriendin."
            },
            {
                "type": "mc",
                "vraag": "Waarover gaat het stripverhaal 'Les enfants de la résistance' (p. 156)?",
                "opties": [
                    "Over astronauten die naar Mars reizen",
                    "Over een Franse voetbalclub in de Champions League",
                    "Over drie dorpskinderen die in de Tweede Wereldoorlog in het verzet gaan",
                    "Over koks die een nieuw Frans restaurant openen"
                ],
                "antwoord": 2,
                "uitleg": "Het stripverhaal gaat over jongeren die in de bezettingstijd dapper verzet bieden tegen de nazi's."
            },
            {
                "type": "mc",
                "vraag": "Welke maatschappijkritiek levert zanger Stromae in zijn bekende nummer 'Carmen'?",
                "opties": [
                    "Dat klassieke muziek te moeilijk is voor scholieren",
                    "Dat vliegreizen verboden moeten worden wegens milieuvervuiling",
                    "Dat scholen te veel huiswerk opgeven aan jongeren",
                    "Dat Twitter en sociale media mensen verslaafd en oppervlakkig eenzaam maken"
                ],
                "antwoord": 3,
                "uitleg": "Stromae bekritiseert de oppervlakkigheid en verslavende werking van sociale media."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de uitroep van de Franse docente: 'Silence! Taisez-vous!'?",
                "opties": [
                    "Stilte! Wees stil / houd je mond!",
                    "Welkom! Ga alsjeblieft zitten!",
                    "Gefeliciteerd met je goede cijfer!",
                    "Tot ziens en een fijn weekend!"
                ],
                "antwoord": 0,
                "uitleg": "'Taisez-vous!' betekent 'wees stil' of 'zwijg'."
            },
            {
                "type": "waaronwaar",
                "vraag": "Bij een luisteropdracht voor DELF is het slim om de vragen pas na het luisteren voor het eerst te lezen.",
                "antwoord": False,
                "uitleg": "Onwaar! Cito en DELF adviseren om altijd eerst de vragen te lezen om gericht te kunnen luisteren."
            },
            {
                "type": "waaronwaar",
                "vraag": "De afsluiting 'À bientôt!' betekent 'Tot snel!' of 'Tot gauw!' in het Frans.",
                "antwoord": True,
                "uitleg": "Waar! 'À bientôt' is een veelgebruikte vriendelijke afsluiting van een bericht."
            },
            {
                "type": "waaronwaar",
                "vraag": "In 'Les enfants de la résistance' werken de hoofdpersonen vrijwillig samen met de bezetter.",
                "antwoord": False,
                "uitleg": "Onwaar! Zij plegen juist moedig verzet tegen de bezetter (l'occupant)."
            },
            {
                "type": "invoer",
                "vraag": "Vertaal de Franse afsluiting voor 'tot snel' (twee woorden: à ...):",
                "antwoord": "à bientôt|a bientot|a bientôt",
                "uitleg": "Tot snel is in het Frans 'à bientôt'."
            },
            {
                "type": "invoer",
                "vraag": "Welke vogel (en sociaal netwerk) vergelijkt Stromae met de liefde in Carmen? Vul het Franse woord in voor 'de vogel' (l'oiseau):",
                "antwoord": "l'oiseau|oiseau",
                "uitleg": "'L'oiseau' betekent de vogel (l'oiseau de Twitter)."
            },
            {
                "type": "invoer",
                "vraag": "Wat betekent het Franse woord 'bises' onderaan een informeel bericht aan een goede vriendin? Vul de Nederlandse vertaling in (liefs/kusjes):",
                "antwoord": "kusjes|liefs|kussen",
                "uitleg": "'Bises' betekent liefs of kusjes onderaan een e-mail of brief."
            }
        ]
    }
]

EXAMENS = [
    # Toets 1 (ex-h3-frans-u4-v1)
    {
        "id": "ex-h3-frans-u4-v1",
        "hoofdstuk": 4,
        "hoofdstukTitel": "Unité 4 — Le pont",
        "titel": "Woordenschat 1 · Le pont: Herhaling Ch 1 (Sociale media & Adjectifs)",
        "duurMin": 20,
        "vak": "Frans · HAVO 3 (U4)",
        "icoon": "📱",
        "vragen": [
            # 12 MC: 3x0, 3x1, 3x2, 3x3
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'le portable'</b>?",
                "opties": [
                    "de mobiele telefoon",
                    "de brievenbus",
                    "de laptophoes",
                    "het tablet-toetsenbord"
                ],
                "antwoord": 0,
                "uitleg": "'Le portable' is de mobiele telefoon (smartphone)."
            },
            {
                "type": "mc",
                "vraag": "Kies de juiste vorm van het bijvoeglijk naamwoord: 'Ce sont des filles très ____ (ambitieus).'",
                "opties": [
                    "ambitieux",
                    "ambitieuses",
                    "ambitieuse",
                    "ambitieus"
                ],
                "antwoord": 1,
                "uitleg": "Vrouwelijk meervoud van ambitieux is 'ambitieuses'."
            },
            {
                "type": "mc",
                "vraag": "Welk bijvoeglijk naamwoord hoort volgens de regels VÓÓR het zelfstandig naamwoord te staan?",
                "opties": [
                    "intéressant",
                    "algérien",
                    "vieux",
                    "sportif"
                ],
                "antwoord": 2,
                "uitleg": "'Vieux' is een kort basisadjectief dat vóór het zelfstandig naamwoord staat (un vieux livre)."
            },
            {
                "type": "mc",
                "vraag": "Wat is de betekenis van het Franse werkwoord <b>'bavarder'</b>?",
                "opties": [
                    "huilen",
                    "schreeuwen",
                    "reizen",
                    "kletsen / gezellig praten"
                ],
                "antwoord": 3,
                "uitleg": "'Bavarder' betekent kletsen."
            },
            {
                "type": "mc",
                "vraag": "Kies de juiste vrouwelijke vorm: 'C'est une ____ (goede) amie de ma sœur.'",
                "opties": [
                    "bonne",
                    "bon",
                    "bons",
                    "bonnes"
                ],
                "antwoord": 0,
                "uitleg": "De vrouwelijke vorm van 'bon' is 'bonne'."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent <b>'l'écran'</b> (m) in het dagelijks taalgebruik?",
                "opties": [
                    "de toetsen",
                    "het beeldscherm",
                    "de batterij",
                    "de oplader"
                ],
                "antwoord": 1,
                "uitleg": "'L'écran' is het beeldscherm."
            },
            {
                "type": "mc",
                "vraag": "Welke zin heeft de juiste woordvolgorde voor het bijvoeglijk naamwoord?",
                "opties": [
                    "J'ai acheté une rouge voiture.",
                    "Elle porte une délicieuse robe.",
                    "J'ai préparé un couscous délicieux.",
                    "Il a un grand nez rouge jamais."
                ],
                "antwoord": 2,
                "uitleg": "Kleur en smaak/beoordeling zoals 'délicieux' staan achter het zelfstandig naamwoord: 'un couscous délicieux'."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de werkwoordsvorm <b>'nous partageons'</b>?",
                "opties": [
                    "wij vertrekken",
                    "wij ontmoeten",
                    "wij vergeten",
                    "wij delen"
                ],
                "antwoord": 3,
                "uitleg": "'Partager' betekent delen (nous partageons des photos)."
            },
            {
                "type": "mc",
                "vraag": "Wat is de mannelijke vorm die hoort bij het vrouwelijke <b>'nouvelle'</b>?",
                "opties": [
                    "nouveau",
                    "nouvels",
                    "neufe",
                    "noveau"
                ],
                "antwoord": 0,
                "uitleg": "'Nouveau' is mannelijk, 'nouvelle' is vrouwelijk."
            },
            {
                "type": "mc",
                "vraag": "Vertaal het cursieve woord: 'Elle a reçu un <i>message</i> important.'",
                "opties": [
                    "cadeau",
                    "bericht",
                    "brief",
                    "rapportcijfer"
                ],
                "antwoord": 1,
                "uitleg": "'Un message' is een bericht."
            },
            {
                "type": "mc",
                "vraag": "Kies de juiste vervoeging van 'aimer' in 'Les jeunes ____ les réseaux sociaux.'",
                "opties": [
                    "aime",
                    "aimons",
                    "aiment",
                    "aimez"
                ],
                "antwoord": 2,
                "uitleg": "Bij 'les jeunes' (ils) hoort de uitgang -ent: 'aiment'."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'l'appli'</b>?",
                "opties": [
                    "het telefoongesprek",
                    "het wachtwoord",
                    "de camera",
                    "de mobiele applicatie"
                ],
                "antwoord": 3,
                "uitleg": "'L'appli' is de afkorting voor applicatie / app."
            },
            # 4 Waaronwaar: 2 waar, 2 onwaar
            {
                "type": "waaronwaar",
                "vraag": "Het Franse bijvoeglijk naamwoord 'sportif' wordt in het vrouwelijk geschreven als 'sportive'.",
                "antwoord": True,
                "uitleg": "Waar! Woorden op -if veranderen in -ive in het vrouwelijk."
            },
            {
                "type": "waaronwaar",
                "vraag": "Bijvoeglijk naamwoorden die een kleur aangeven (zoals bleu of vert) staan vóór het zelfstandig naamwoord.",
                "antwoord": False,
                "uitleg": "Onwaar! Kleuren staan in het Frans vrijwel altijd achter het zelfstandig naamwoord (un vélo bleu)."
            },
            {
                "type": "waaronwaar",
                "vraag": "De uitgang van regelmatige werkwoorden op -er bij 'vous' is '-ez'.",
                "antwoord": True,
                "uitleg": "Waar! Bij vous eindigt het werkwoord op -ez (vous parlez, vous regardez)."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Franse woord 'le réseau' betekent uitsluitend een visnet in zee.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Le réseau' betekent netwerk (bijv. le réseau social = het sociale netwerk)."
            },
            # 2 Invul
            {
                "type": "invul",
                "vraag": "Vul de vrouwelijke vorm van 'beau' in: 'C'est une très ____ (mooie) photo de vacances.'",
                "antwoord": "belle",
                "uitleg": "De vrouwelijke vorm van beau is 'belle'."
            },
            {
                "type": "invul",
                "vraag": "Vertaal het woord tussen haakjes: 'Elle a envoyé un (bericht) à sa copine.' Vul het Franse woord in.",
                "antwoord": "message",
                "uitleg": "Bericht is 'message'."
            },
            # 2 Open
            {
                "type": "open",
                "vraag": "Noem twee Franse adjectieven die volgens de regels vóór het zelfstandig naamwoord geplaatst worden.",
                "modelantwoord": "Twee voorbeelden zijn grand, petit, beau, bon of vieux.",
                "sleutelwoorden": [
                    "grand/petit/beau/bon/vieux/joli",
                    "petit/grand/beau/bon/vieux/joli"
                ],
                "minTreffers": 1,
                "uitleg": "Korte adjectieven zoals grand, petit, beau, bon, vieux staan vóór het zelfstandig naamwoord."
            },
            {
                "type": "open",
                "vraag": "Leg uit hoe de vrouwelijke vorm van een Frans bijvoeglijk naamwoord dat eindigt op -eux (zoals ambitieux) gevormd wordt.",
                "modelantwoord": "De uitgang -eux verandert in -euse, zoals ambitieuse of délicieuse.",
                "sleutelwoorden": [
                    "euse",
                    "ambitieuse/délicieuse/verandert"
                ],
                "minTreffers": 1,
                "uitleg": "Mannelijk -eux wordt vrouwelijk -euse (bijv. ambitieuse)."
            }
        ]
    },

    # Toets 2 (ex-h3-frans-u4-v2)
    {
        "id": "ex-h3-frans-u4-v2",
        "hoofdstuk": 4,
        "hoofdstukTitel": "Unité 4 — Le pont",
        "titel": "Woordenschat 2 · Le pont: Herhaling Ch 2 (Series, Werkwoorden op -ir & Lidwoorden)",
        "duurMin": 20,
        "vak": "Frans · HAVO 3 (U4)",
        "icoon": "🎸",
        "vragen": [
            # 12 MC: 3x0, 3x1, 3x2, 3x3
            {
                "type": "mc",
                "vraag": "Kies de juiste samentrekking: 'Le professeur va ____ (naar het) collège à huit heures.'",
                "opties": [
                    "au",
                    "à la",
                    "aux",
                    "à l'"
                ],
                "antwoord": 0,
                "uitleg": "Collège is mannelijk, dus à + le wordt 'au collège'."
            },
            {
                "type": "mc",
                "vraag": "Wat is de juiste vorm van 'finir' bij 'nous' in de tegenwoordige tijd?",
                "opties": [
                    "nous finissons",
                    "nous finissiez",
                    "nous finis",
                    "nous finissent"
                ],
                "antwoord": 0,
                "uitleg": "Bij 'nous' krijgt finir de uitgang -issons: 'nous finissons'."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'l'argent'</b> (m)?",
                "opties": [
                    "het goud",
                    "het geld / zilver",
                    "het koper",
                    "het salaris"
                ],
                "antwoord": 1,
                "uitleg": "'L'argent' betekent het geld of zilver."
            },
            {
                "type": "mc",
                "vraag": "Kies de juiste samentrekking van 'de + les': 'Ce sont les vélos ____ (van de) élèves.'",
                "opties": [
                    "du",
                    "des",
                    "de la",
                    "de l'"
                ],
                "antwoord": 1,
                "uitleg": "De + les trekt altijd samen tot 'des'."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'passionnant'</b>?",
                "opties": [
                    "vervelend",
                    "moeilijk",
                    "boeiend / meeslepend",
                    "gevaarlijk"
                ],
                "antwoord": 2,
                "uitleg": "'Passionnant' betekent boeiend of heel spannend."
            },
            {
                "type": "mc",
                "vraag": "Wat is het voltooid deelwoord van het werkwoord <b>'choisir'</b> in de passé composé?",
                "opties": [
                    "choisié",
                    "choisu",
                    "choisi",
                    "choisis"
                ],
                "antwoord": 2,
                "uitleg": "Het voltooid deelwoord van regelmatige -ir werkwoorden eindigt op -i: 'choisi'."
            },
            {
                "type": "mc",
                "vraag": "Kies de juiste samentrekking van 'à + les': 'Elle doit aller ____ toilettes.'",
                "opties": [
                    "à la",
                    "au",
                    "à l'",
                    "aux"
                ],
                "antwoord": 3,
                "uitleg": "Toilettes is meervoud, dus à + les wordt 'aux'."
            },
            {
                "type": "mc",
                "vraag": "Wat is de Nederlandse betekenis van het Franse zelfstandig naamwoord <b>'le cerveau'</b>?",
                "opties": [
                    "het hart",
                    "de maag",
                    "de longen",
                    "de hersenen"
                ],
                "antwoord": 3,
                "uitleg": "'Le cerveau' zijn de hersenen."
            },
            {
                "type": "mc",
                "vraag": "Vul de juiste vorm in: 'Tu ____ (kiest) quel film pour ce soir?'",
                "opties": [
                    "choisis",
                    "choisit",
                    "choisissez",
                    "choisissent"
                ],
                "antwoord": 0,
                "uitleg": "Bij 'tu' is de uitgang van een -ir werkwoord '-is': 'tu choisis'."
            },
            {
                "type": "mc",
                "vraag": "Kies de juiste samentrekking: 'C'est la sœur ____ (van de) copain de Lucas.'",
                "opties": [
                    "de la",
                    "du",
                    "des",
                    "de l'"
                ],
                "antwoord": 1,
                "uitleg": "'Copain' is mannelijk (le copain), dus de + le wordt 'du copain'."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de uitdrukking <b>'avoir du succès'</b>?",
                "opties": [
                    "geld verliezen",
                    "hard werken",
                    "succes hebben",
                    "populair willen worden"
                ],
                "antwoord": 2,
                "uitleg": "'Avoir du succès' betekent succes hebben."
            },
            {
                "type": "mc",
                "vraag": "Wat is het Franse woord voor 'de aflevering' van een televisieserie?",
                "opties": [
                    "la saison",
                    "le cinéma",
                    "le spectacle",
                    "l'épisode"
                ],
                "antwoord": 3,
                "uitleg": "'L'épisode' is de aflevering."
            },
            # 4 Waaronwaar: 2 waar, 2 onwaar
            {
                "type": "waaronwaar",
                "vraag": "De combinatie 'de + la' trekt in het Frans samen tot 'dula'.",
                "antwoord": False,
                "uitleg": "Onwaar! 'de + la' trekt niet samen en blijft gewoon 'de la' (de la maison)."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het werkwoord 'réussir' (slagen) vervoegt in de présent bij 'il' als 'il réussit'.",
                "antwoord": True,
                "uitleg": "Waar! Bij il/elle/on krijgt een -ir werkwoord de uitgang -it: 'il réussit'."
            },
            {
                "type": "waaronwaar",
                "vraag": "De samentrekking 'au' gebruik je voor vrouwelijke zelfstandige naamwoorden.",
                "antwoord": False,
                "uitleg": "Onwaar! 'au' is de samentrekking van à + le voor mannelijke woorden."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Franse zelfstandig naamwoord 'la tête' betekent het hoofd.",
                "antwoord": True,
                "uitleg": "Waar! 'La tête' betekent het hoofd (avoir mal à la tête = hoofdpijn hebben)."
            },
            # 2 Invul
            {
                "type": "invul",
                "vraag": "Vul de juiste samentrekking in: 'Nous allons ____ (naar de) restaurant italien.'",
                "antwoord": "au",
                "uitleg": "à + le restaurant = 'au restaurant'."
            },
            {
                "type": "invul",
                "vraag": "Vul de persoonsvorm in van 'finir' bij 'ils' in de tegenwoordige tijd: 'Ils ____ (eindigen) leurs devoirs à cinq heures.'",
                "antwoord": "finissent",
                "uitleg": "De uitgang bij ils is -issent: 'finissent'."
            },
            # 2 Open
            {
                "type": "open",
                "vraag": "Geef de twee Franse samentrekkingen die ontstaan uit de voorzetsels à en de gecombineerd met het mannelijk enkelvoudig lidwoord le.",
                "modelantwoord": "Dat zijn de vormen au en du.",
                "sleutelwoorden": [
                    "au",
                    "du"
                ],
                "minTreffers": 2,
                "uitleg": "à + le = au en de + le = du."
            },
            {
                "type": "open",
                "vraag": "Welke twee vaste uitgangen krijgen regelmatige Franse werkwoorden op -ir bij de meervoudsvormen 'nous' en 'vous' in de présent?",
                "modelantwoord": "De uitgangen zijn -issons en -issez.",
                "sleutelwoorden": [
                    "issons/-issons",
                    "issez/-issez"
                ],
                "minTreffers": 2,
                "uitleg": "Bij regelmatige werkwoorden op -ir zijn de uitgangen bij nous en vous respectievelijk -issons en -issez (zoals nous finissons, vous choisissez)."
            }
        ]
    },

    # Toets 3 (ex-h3-frans-u4-v3)
    {
        "id": "ex-h3-frans-u4-v3",
        "hoofdstuk": 4,
        "hoofdstukTitel": "Unité 4 — Le pont",
        "titel": "Woordenschat 3 · Le pont: Herhaling Ch 3 (Passé composé & Lijdend voorwerp)",
        "duurMin": 20,
        "vak": "Frans · HAVO 3 (U4)",
        "icoon": "🚆",
        "vragen": [
            # 12 MC: 3x0, 3x1, 3x2, 3x3
            {
                "type": "mc",
                "vraag": "Kies het juiste voltooid deelwoord bij être: 'Léa et sa mère sont ____ (aangekomen) à la gare.'",
                "opties": [
                    "arrivées",
                    "arrivé",
                    "arrivée",
                    "arrivés"
                ],
                "antwoord": 0,
                "uitleg": "Léa et sa mère is vrouwelijk meervoud, dus bij être krijgt arrivé de uitgang -es: 'arrivées'."
            },
            {
                "type": "mc",
                "vraag": "Vervang het lijdend voorwerp: 'Tu aimes ces séries? ➔ Oui, je ____ adore!'",
                "opties": [
                    "la",
                    "les",
                    "le",
                    "l'"
                ],
                "antwoord": 1,
                "uitleg": "'Ces séries' is meervoud, dus je vervangt het door 'les'."
            },
            {
                "type": "mc",
                "vraag": "Welk werkwoord vormt de passé composé met het hulpwerkwoord <b>être</b>?",
                "opties": [
                    "manger",
                    "regarder",
                    "partir",
                    "acheter"
                ],
                "antwoord": 2,
                "uitleg": "'Partir' (vertrekken) is een bewegingswerkwoord en wordt vervoegd met être."
            },
            {
                "type": "mc",
                "vraag": "Wat is het onregelmatige voltooid deelwoord van het Franse werkwoord <b>'prendre'</b>?",
                "opties": [
                    "prendu",
                    "prené",
                    "prendé",
                    "pris"
                ],
                "antwoord": 3,
                "uitleg": "Het voltooid deelwoord van prendre is 'pris' (j'ai pris le bus)."
            },
            {
                "type": "mc",
                "vraag": "Vervang het lijdend voorwerp: 'Tu regardes <u>la télé</u>? ➔ Oui, je ____ regarde tous les soirs.'",
                "opties": [
                    "la",
                    "le",
                    "les",
                    "l'"
                ],
                "antwoord": 0,
                "uitleg": "'La télé' is vrouwelijk enkelvoud, dus je gebruikt 'la'."
            },
            {
                "type": "mc",
                "vraag": "Kies het juiste hulpwerkwoord: 'Victor et son copain ____ allés à l'entraînement.'",
                "opties": [
                    "ont",
                    "sont",
                    "vont",
                    "font"
                ],
                "antwoord": 1,
                "uitleg": "'Aller' wordt in de passé composé vervoegd met être: 'ils sont allés'."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'le centre-ville'</b>?",
                "opties": [
                    "het treinstation",
                    "de buitenwijk",
                    "het stadscentrum",
                    "het gemeentehuis"
                ],
                "antwoord": 2,
                "uitleg": "'Le centre-ville' is het stadscentrum."
            },
            {
                "type": "mc",
                "vraag": "Wat is het voltooid deelwoord van <b>'avoir'</b> (hebben) in de passé composé?",
                "opties": [
                    "avé",
                    "été",
                    "avu",
                    "eu"
                ],
                "antwoord": 3,
                "uitleg": "Het voltooid deelwoord van avoir is 'eu' (j'ai eu un problème)."
            },
            {
                "type": "mc",
                "vraag": "Waar plaats je het lijdend voorwerp 'le' in een ontkennende zin met één werkwoord?",
                "opties": [
                    "Tussen ne en de persoonsvorm: Je ne le connais pas.",
                    "Helemaal achteraan: Je ne connais pas le.",
                    "Vóór ne: Je le ne connais pas.",
                    "Achter het onderwerp: Le je ne connais pas."
                ],
                "antwoord": 0,
                "uitleg": "Het voornaamwoord staat direct vóór de persoonsvorm: 'Je ne le connais pas'."
            },
            {
                "type": "mc",
                "vraag": "Kies de juiste vorm van monter bij être: 'Elles sont ____ (naar boven gegaan) au troisième étage.'",
                "opties": [
                    "monté",
                    "montées",
                    "montée",
                    "montés"
                ],
                "antwoord": 1,
                "uitleg": "Vrouwelijk meervoud (elles) krijgt bij être de uitgang -es: 'montées'."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de voorzetseluitdrukking <b>'en face de'</b>?",
                "opties": [
                    "naast",
                    "achter",
                    "tegenover",
                    "bovenop"
                ],
                "antwoord": 2,
                "uitleg": "'En face de' betekent tegenover."
            },
            {
                "type": "mc",
                "vraag": "Wat is het voltooid deelwoord van <b>'être'</b> (zijn) in de passé composé?",
                "opties": [
                    "essé",
                    "sont",
                    "étu",
                    "été"
                ],
                "antwoord": 3,
                "uitleg": "Het voltooid deelwoord van être is 'été' (j'ai été à Paris)."
            },
            # 4 Waaronwaar: 2 waar, 2 onwaar
            {
                "type": "waaronwaar",
                "vraag": "Het Franse werkwoord 'rester' wordt in de passé composé vervoegd met het hulpwerkwoord avoir.",
                "antwoord": False,
                "uitleg": "Onwaar! 'Rester' vormt de passé composé altijd met être: 'elle est restée'."
            },
            {
                "type": "waaronwaar",
                "vraag": "Vóór een klinker verandert het lijdend voorwerp 'le' of 'la' in 'l''.",
                "antwoord": True,
                "uitleg": "Waar! Bijvoorbeeld: 'Je l'aime' in plaats van 'Je le aime'."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het voltooid deelwoord van 'boire' is 'boiré'.",
                "antwoord": False,
                "uitleg": "Onwaar! Het voltooid deelwoord van boire is 'bu' (j'ai bu un café)."
            },
            {
                "type": "waaronwaar",
                "vraag": "Bij werkwoorden met 'être' krijgt het voltooid deelwoord een extra -e als het onderwerp vrouwelijk enkelvoud is.",
                "antwoord": True,
                "uitleg": "Waar! Bij être past het voltooid deelwoord zich aan aan het onderwerp (bijv. elle est allée)."
            },
            # 2 Invul
            {
                "type": "invul",
                "vraag": "Vul het juiste hulpwerkwoord in: 'Laura ____ restée à la maison ce weekend.'",
                "antwoord": "est",
                "uitleg": "Rester gaat met être: 'Laura est restée'."
            },
            {
                "type": "invul",
                "vraag": "Vervang het onderstreepte woord door le, la, l' of les: 'Je connais bien <u>ce quartier</u> ➔ Je ____ connais bien.'",
                "antwoord": "le",
                "uitleg": "'Ce quartier' is mannelijk enkelvoud, dus je gebruikt 'le'."
            },
            # 2 Open
            {
                "type": "open",
                "vraag": "Wat voeg je toe aan het Franse voltooid deelwoord bij het hulpwerkwoord être als het onderwerp vrouwelijk meervoud (zoals 'elles') is?",
                "modelantwoord": "Je voegt de uitgang -es toe aan het voltooid deelwoord.",
                "sleutelwoorden": [
                    "es/-es",
                    "uitgang/toevoeging/accord"
                ],
                "minTreffers": 1,
                "uitleg": "Bij vrouwelijk meervoud voeg je -es toe aan het voltooid deelwoord bij het hulpwerkwoord être (bijvoorbeeld elles sont allées, elles zijn gegaan)."
            },
            {
                "type": "open",
                "vraag": "Noem het Franse voltooid deelwoord van de onregelmatige werkwoorden 'faire' en 'prendre'.",
                "modelantwoord": "De voltooide deelwoorden zijn fait en pris.",
                "sleutelwoorden": [
                    "fait",
                    "pris"
                ],
                "minTreffers": 2,
                "uitleg": "Het voltooid deelwoord van faire is fait en van prendre is pris."
            }
        ]
    },

    # Toets 4 (ex-h3-frans-u4-v4)
    {
        "id": "ex-h3-frans-u4-v4",
        "hoofdstuk": 4,
        "hoofdstukTitel": "Unité 4 — Le pont",
        "titel": "Woordenschat 4 · Le pont: DELF Vaardigheden & Schrijfstrategieën",
        "duurMin": 20,
        "vak": "Frans · HAVO 3 (U4)",
        "icoon": "🗼",
        "vragen": [
            # 12 MC: 3x0, 3x1, 3x2, 3x3
            {
                "type": "mc",
                "vraag": "Wat betekent de beleefdheidsafsluiting <b>'À bientôt'</b> onderaan een Franse e-mail?",
                "opties": [
                    "Tot snel! / Tot gauw!",
                    "Met vriendelijke groet,",
                    "Dank voor de moeite,",
                    "Alstublieft,"
                ],
                "antwoord": 0,
                "uitleg": "'À bientôt' betekent tot snel of tot gauw."
            },
            {
                "type": "mc",
                "vraag": "Welke aanhef gebruik je voor een informele Franse brief aan een vriend?",
                "opties": [
                    "Madame la Directrice,",
                    "Cher Thomas,",
                    "Chère Julie,",
                    "À plus tard,"
                ],
                "antwoord": 1,
                "uitleg": "Voor een mannelijke vriend gebruik je 'Cher ...,' (Cher Thomas)."
            },
            {
                "type": "mc",
                "vraag": "Wat is de belangrijkste Cito/DELF-strategie vóór het afspelen van een luisterfragment?",
                "opties": [
                    "De antwoorden alvast willekeurig invullen",
                    "De Franse docent om de vertaling vragen",
                    "Eerst de vragen en meerkeuzeopties aandachtig doorlezen",
                    "Je ogen sluiten en pas na afloop de vragen bekijken"
                ],
                "antwoord": 2,
                "uitleg": "Door eerst de vragen te lezen weet je precies waar je tijdens het luisteren op moet letten."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'bises'</b> onderaan een informeel berichtje?",
                "opties": [
                    "handtekening",
                    "postscriptum (ps)",
                    "telefoonnummer",
                    "liefs / kusjes"
                ],
                "antwoord": 3,
                "uitleg": "'Bises' betekent liefs of dikke kussen onderaan een informeel bericht."
            },
            {
                "type": "mc",
                "vraag": "Hoe vraag je in een Franse brief beleefd 'Hoe gaat het met jou?'",
                "opties": [
                    "Comment vas-tu?",
                    "Comment t'appelles-tu?",
                    "Où habites-tu?",
                    "Quel âge as-tu?"
                ],
                "antwoord": 0,
                "uitleg": "'Comment vas-tu?' betekent 'Hoe gaat het met jou?'."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de Franse zin <b>'Écris-moi vite!'</b> aan het einde van een e-mail?",
                "opties": [
                    "Bel me snel op!",
                    "Schrijf me snel terug!",
                    "Kom snel op bezoek!",
                    "Vergeet me niet!"
                ],
                "antwoord": 1,
                "uitleg": "'Écris-moi vite!' betekent 'Schrijf me snel!'."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'l'occupant'</b> in historische context van de Tweede Wereldoorlog?",
                "opties": [
                    "de vluchteling",
                    "de soldaat van het verzet",
                    "de bezetter",
                    "de dorpsbewoner"
                ],
                "antwoord": 2,
                "uitleg": "'L'occupant' is de bezetter."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de oproep <b>'Taisez-vous!'</b> in het klaslokaal?",
                "opties": [
                    "Ga staan!",
                    "Pak je boek erbij!",
                    "Kom naar het bord!",
                    "Zwijg! / Houd je mond!"
                ],
                "antwoord": 3,
                "uitleg": "'Taisez-vous!' betekent 'wees stil' of 'houd je mond'."
            },
            {
                "type": "mc",
                "vraag": "Hoe bedank je iemand in het Frans voor een ontvangen e-mail of bericht?",
                "opties": [
                    "Merci pour ton message.",
                    "Pardon pour le retard.",
                    "Je suis désolé.",
                    "Bienvenue chez moi."
                ],
                "antwoord": 0,
                "uitleg": "'Merci pour ton message' betekent 'Bedankt voor je bericht'."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'le témoin'</b> in een politieverslag of ooggetuigenverslag?",
                "opties": [
                    "de dader",
                    "de getuige",
                    "de agent",
                    "het slachtoffer"
                ],
                "antwoord": 1,
                "uitleg": "'Le témoin' is de getuige."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'l'événement'</b> (m)?",
                "opties": [
                    "het gebouw",
                    "het diploma",
                    "de gebeurtenis",
                    "het landschap"
                ],
                "antwoord": 2,
                "uitleg": "'L'événement' is de gebeurtenis."
            },
            {
                "type": "mc",
                "vraag": "Hoe noem je een stripboek in het Frans (afkorting BD)?",
                "opties": [
                    "le roman",
                    "le journal",
                    "la poésie",
                    "la bande dessinée"
                ],
                "antwoord": 3,
                "uitleg": "'BD' staat voor 'la bande dessinée' (het stripverhaal)."
            },
            # 4 Waaronwaar: 2 waar, 2 onwaar
            {
                "type": "waaronwaar",
                "vraag": "De aanhef 'Chère Julie,' gebruik je als je een brief schrijft aan een jongen.",
                "antwoord": False,
                "uitleg": "Onwaar! Voor een meisje gebruik je 'Chère' (met -e); voor een jongen gebruik je 'Cher'."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het Franse woord 'le silence' betekent stilte.",
                "antwoord": True,
                "uitleg": "Waar! 'Le silence' is de stilte (bijv. silence en classe)."
            },
            {
                "type": "waaronwaar",
                "vraag": "Bij een DELF-schrijfopdracht mag je het aantal gevraagde woorden met 50% inkorten zonder puntenverlies.",
                "antwoord": False,
                "uitleg": "Onwaar! Het halen van de minimumlengte is een officieel beoordelingscriterium bij DELF."
            },
            {
                "type": "waaronwaar",
                "vraag": "De term 'la résistance' verwijst historisch naar het georganiseerde verzet tegen onderdrukking.",
                "antwoord": True,
                "uitleg": "Waar! 'La résistance' is het verzet."
            },
            # 2 Invul
            {
                "type": "invul",
                "vraag": "Vul de juiste aanhef in voor een vriendin genaamd Manon: '____ (Lieve/Beste) Manon,'",
                "antwoord": "Chère|Chere",
                "uitleg": "Voor een vrouwelijk persoon is het 'Chère'."
            },
            {
                "type": "invul",
                "vraag": "Vertaal het woord tussen haakjes: 'Merci pour ta (brief).' Vul het Franse woord in (lettre).",
                "antwoord": "lettre",
                "uitleg": "Brief is 'la lettre'."
            },
            # 2 Open
            {
                "type": "open",
                "vraag": "Noem twee beleefde manieren om een informele Franse brief of e-mail af te sluiten.",
                "modelantwoord": "Twee manieren zijn bijvoorbeeld: À bientôt, Bises of Amicalement.",
                "sleutelwoorden": [
                    "À bientôt/bientot/bises/amicalement",
                    "bises/amicalement/salut"
                ],
                "minTreffers": 1,
                "uitleg": "Informele afsluitingen zijn bijvoorbeeld 'À bientôt!', 'Bises' of 'Amicalement'."
            },
            {
                "type": "open",
                "vraag": "Waarom is het verstandig om bij Cito- en DELF-luistertoetsen de opgaven vooraf grondig door te nemen?",
                "modelantwoord": "Hierdoor weet je al op welke specifieke details of kernwoorden je moet letten tijdens het luisterfragment.",
                "sleutelwoorden": [
                    "detail/kernwoord/focus/gericht",
                    "weten/letten/aandacht/audio"
                ],
                "minTreffers": 1,
                "uitleg": "Door vooraf de opgaven te lezen weet je precies op welke aspecten je in het audiofragment moet letten."
            }
        ]
    },

    # Toets 5 (ex-h3-frans-u4-v5)
    {
        "id": "ex-h3-frans-u4-v5",
        "hoofdstuk": 4,
        "hoofdstukTitel": "Unité 4 — Le pont",
        "titel": "Woordenschat 5 · Le pont: Integrale Oefentoets Unité 1 t/m 3",
        "duurMin": 20,
        "vak": "Frans · HAVO 3 (U4)",
        "icoon": "🗼",
        "vragen": [
            # 12 MC: 3x0, 3x1, 3x2, 3x3
            {
                "type": "mc",
                "vraag": "Wat betekent de uitdrukking <b>'rendre visite à quelqu'un'</b>?",
                "opties": [
                    "iemand bezoeken",
                    "iemand opbellen",
                    "iemand uitnodigen",
                    "iemand feliciteren"
                ],
                "antwoord": 0,
                "uitleg": "'Rendre visite à' betekent iemand bezoeken."
            },
            {
                "type": "mc",
                "vraag": "Kies de juiste vorm van het werkwoord 'partir' bij être: 'Mes cousines sont ____ (vertrokken) hier.'",
                "opties": [
                    "parti",
                    "parties",
                    "partie",
                    "partis"
                ],
                "antwoord": 1,
                "uitleg": "'Mes cousines' is vrouwelijk meervoud, dus bij être krijgt parti de uitgang -es: 'parties'."
            },
            {
                "type": "mc",
                "vraag": "Kies de juiste samentrekking: 'Ils parlent souvent ____ (over de) problèmes des jeunes.'",
                "opties": [
                    "du",
                    "de la",
                    "des",
                    "de l'"
                ],
                "antwoord": 2,
                "uitleg": "'Problèmes' is meervoud, dus de + les wordt 'des'."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'l'aller-retour'</b> (m)?",
                "opties": [
                    "de enkele reis",
                    "de overstap",
                    "de tussenstop",
                    "het retourtje"
                ],
                "antwoord": 3,
                "uitleg": "'L'aller-retour' is het retourtje."
            },
            {
                "type": "mc",
                "vraag": "Kies de juiste vrouwelijke meervoudsvorm: 'Ce sont des sportives très ____ (actief).'",
                "opties": [
                    "actives",
                    "actif",
                    "active",
                    "actifs"
                ],
                "antwoord": 0,
                "uitleg": "Vrouwelijk meervoud van actif is 'actives'."
            },
            {
                "type": "mc",
                "vraag": "Vervang het lijdend voorwerp: 'Tu as fait tes devoirs? ➔ Oui, je ____ ai faits.'",
                "opties": [
                    "l'",
                    "les",
                    "la",
                    "le"
                ],
                "antwoord": 1,
                "uitleg": "'Tes devoirs' is meervoud, dus je gebruikt 'les'."
            },
            {
                "type": "mc",
                "vraag": "Wat is het juiste voltooid deelwoord van het werkwoord <b>'voir'</b> (zien)?",
                "opties": [
                    "voisé",
                    "voisi",
                    "vu",
                    "vais"
                ],
                "antwoord": 2,
                "uitleg": "Het voltooid deelwoord van voir is 'vu' (j'ai vu ce film)."
            },
            {
                "type": "mc",
                "vraag": "Kies de juiste samentrekking: 'Mon frère adore aller ____ (naar het) parc le weekend.'",
                "opties": [
                    "à la",
                    "aux",
                    "à l'",
                    "au"
                ],
                "antwoord": 3,
                "uitleg": "Parc is mannelijk (le parc), dus à + le wordt 'au'."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent het Franse woord <b>'le quartier'</b>?",
                "opties": [
                    "de wijk / de buurt",
                    "het kwartier van een uur",
                    "het stadhuis",
                    "de supermarkt"
                ],
                "antwoord": 0,
                "uitleg": "'Le quartier' betekent de wijk of de buurt."
            },
            {
                "type": "mc",
                "vraag": "Wat is de vervoeging van 'finir' bij 'ils' in de présent?",
                "opties": [
                    "ils finisent",
                    "ils finissent",
                    "ils finissons",
                    "ils finissez"
                ],
                "antwoord": 1,
                "uitleg": "De uitgang bij ils/elles is -issent: 'finissent'."
            },
            {
                "type": "mc",
                "vraag": "Welke zin heeft het bijvoeglijk naamwoord op de JUISTE plaats?",
                "opties": [
                    "Il a une noire voiture.",
                    "Elle a un bleu pantalon.",
                    "C'est un beau village en France.",
                    "J'habite dans une moderne maison."
                ],
                "antwoord": 2,
                "uitleg": "'Beau' staat vóór het zelfstandig naamwoord: 'un beau village'."
            },
            {
                "type": "mc",
                "vraag": "Wat betekent de uitdrukking <b>'en face de'</b>?",
                "opties": [
                    "naast",
                    "boven",
                    "achter",
                    "tegenover"
                ],
                "antwoord": 3,
                "uitleg": "'En face de' betekent tegenover."
            },
            # 4 Waaronwaar: 2 waar, 2 onwaar
            {
                "type": "waaronwaar",
                "vraag": "In de zin 'Elle est allée à la gare' heeft 'allée' een extra -e omdat het onderwerp vrouwelijk is.",
                "antwoord": True,
                "uitleg": "Waar! Bij être past het voltooid deelwoord zich aan aan het onderwerp (accord)."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het lijdend voorwerp 'les' verandert vóór een klinker in 'l''.",
                "antwoord": False,
                "uitleg": "Onwaar! Alleen 'le' en 'la' veranderen in 'l''. 'Les' blijft altijd 'les' (bijv. je les adore)."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het voltooid deelwoord van 'boire' is 'bu'.",
                "antwoord": True,
                "uitleg": "Waar! 'J'ai bu de l'eau' (ik heb water gedronken)."
            },
            {
                "type": "waaronwaar",
                "vraag": "De combinatie 'de + le' blijft in het Frans ongewijzigd 'de le'.",
                "antwoord": False,
                "uitleg": "Onwaar! 'de + le' trekt altijd verplicht samen tot 'du'."
            },
            # 2 Invul
            {
                "type": "invul",
                "vraag": "Vul de juiste vorm van het voltooid deelwoord in: 'Sarah est ____ (binnengegaan) dans la salle de classe.' Denk aan het accord bij être!",
                "antwoord": "entrée|entree",
                "uitleg": "Sarah is vrouwelijk enkelvoud, dus bij être krijgt entré een extra e: 'entrée'."
            },
            {
                "type": "invul",
                "vraag": "Vertaal de uitdrukking voor 'over een uur' (drie woorden: dans ... heure):",
                "antwoord": "dans une heure",
                "uitleg": "Over een uur is 'dans une heure'."
            },
            # 2 Open
            {
                "type": "open",
                "vraag": "Noem de vier Franse vormen van het lijdend voorwerp (COD) die de woorden 'hem', 'haar', 'het' en 'hen/ze' vertalen.",
                "modelantwoord": "Dat zijn de voornaamwoorden le, la, l' en les.",
                "sleutelwoorden": [
                    "le",
                    "la",
                    "l'",
                    "les"
                ],
                "minTreffers": 3,
                "uitleg": "De vier vormen zijn le, la, l' en les."
            },
            {
                "type": "open",
                "vraag": "Leg uit wat er gebeurt met het voorzetsel à wanneer het gecombineerd wordt met de lidwoorden le en les.",
                "modelantwoord": "De combinaties trekken samen tot respectievelijk au en aux.",
                "sleutelwoorden": [
                    "au",
                    "aux"
                ],
                "minTreffers": 2,
                "uitleg": "à + le wordt au, en à + les wordt aux."
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
        idx = item['id'].replace("ex-h3-frans-u4-v", "")
        fname = f"examen_u4_vocab_{idx}.js"
        fpath = os.path.join(DATA_DIR, fname)
        code = f"/* Proeftoets {item['id']} — {item['titel']}\n   Grandes Lignes 3 HAVO Unité {item['hoofdstuk']} */\nDURU.registerExamen({json.dumps(item, indent=2, ensure_ascii=False)});\n"
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Geschreven examen: {fname}")

if __name__ == "__main__":
    generate()

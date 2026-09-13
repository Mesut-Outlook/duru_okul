# -*- coding: utf-8 -*-
import os, json, random

DATA_DIR = "/home/mesuto/Documents/PROJELER/duru_okul/havo3/frans/js/data"
os.makedirs(DATA_DIR, exist_ok=True)

def balance_mc(questions):
    """mc-cevapindex spreiden zodat geen enkele letter >40% van het bestand is
    (zelfde aanpak als gen_frans_vocab.py -> tools/gate.js regel 3)."""
    # Gebalanceerd maar zonder vaste cyclus (0,1,2,3,0,1,... was voorspelbaar, 2026-09-13):
    # elk blok van 4 wordt geschud; zaad = eerste vraag, dus opnieuw draaien geeft hetzelfde bestand.
    mc_indices = [i for i, q in enumerate(questions) if q.get("type") == "mc"]
    rnd = random.Random(questions[0].get("vraag", "") if questions else "")
    target_pattern = []
    while len(target_pattern) < len(mc_indices):
        blok = [0, 1, 2, 3]; rnd.shuffle(blok); target_pattern += blok
    for idx, q_idx in enumerate(mc_indices):
        q = questions[q_idx]
        current_ans_idx = q["antwoord"]
        correct_text = q["opties"][current_ans_idx]
        new_ans_idx = target_pattern[idx] % len(q["opties"])
        if new_ans_idx != current_ans_idx:
            opts = [opt for i, opt in enumerate(q["opties"]) if i != current_ans_idx]
            opts.insert(new_ans_idx, correct_text)
            q["opties"] = opts
            q["antwoord"] = new_ans_idx

o1 = {
  "id": "fr-u1-1",
  "hoofdstuk": 1,
  "paragraaf": "1.1",
  "titel": "Woordenschat 1.1 · p. 48 (blok A & B) · Sociale media, acties & mensen",
  "korteUitleg": "Woordenschat en uitdrukkingen over social media, communicatie, apparaten en mensen.",
  "icoon": "📱",
  "kleur": "blauw",
  "theorie": """
    <h3>1.1 Woordenschat: pagina 48 (Blok A & B)</h3>
    <div class="info-box">
      <b>Leeradvies:</b> Leer de woorden uit het witte blok in <i>beide richtingen</i> (Frans ➔ Nederlands én Nederlands ➔ Frans). De woorden uit het blauwe blok hoef je alleen Frans ➔ Nederlands te kunnen herkennen.
    </div>

    <h4>Blok A: Sociale media, apparaten en werkwoorden (p. 48)</h4>
    <table class="vocab-tabel" style="width:100%;border-collapse:collapse;margin:12px 0;">
      <tr style="background:var(--blauw-licht);">
        <th style="padding:6px;border:1px solid var(--lijn);">Frans 🇫🇷</th>
        <th style="padding:6px;border:1px solid var(--lijn);">Nederlands 🇳🇱</th>
        <th style="padding:6px;border:1px solid var(--lijn);">Frans 🇫🇷</th>
        <th style="padding:6px;border:1px solid var(--lijn);">Nederlands 🇳🇱</th>
      </tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>la photo</b></td><td style="padding:6px;border:1px solid var(--lijn);">de foto</td><td style="padding:6px;border:1px solid var(--lijn);"><b>j'y vais</b></td><td style="padding:6px;border:1px solid var(--lijn);">ik ga weg</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>le message</b></td><td style="padding:6px;border:1px solid var(--lijn);">het bericht</td><td style="padding:6px;border:1px solid var(--lijn);"><b>il voit</b></td><td style="padding:6px;border:1px solid var(--lijn);">hij ziet</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>la réaction</b></td><td style="padding:6px;border:1px solid var(--lijn);">de reactie</td><td style="padding:6px;border:1px solid var(--lijn);"><b>donne-moi</b></td><td style="padding:6px;border:1px solid var(--lijn);">geef mij</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>le commentaire</b></td><td style="padding:6px;border:1px solid var(--lijn);">het commentaar</td><td style="padding:6px;border:1px solid var(--lijn);"><b>j'ai vu</b></td><td style="padding:6px;border:1px solid var(--lijn);">ik heb gezien</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>le site (web)</b></td><td style="padding:6px;border:1px solid var(--lijn);">de (web)site</td><td style="padding:6px;border:1px solid var(--lijn);"><b>amuse-toi bien!</b></td><td style="padding:6px;border:1px solid var(--lijn);">veel plezier!</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>l'appli (v)</b></td><td style="padding:6px;border:1px solid var(--lijn);">de app</td><td style="padding:6px;border:1px solid var(--lijn);"><b>on était</b></td><td style="padding:6px;border:1px solid var(--lijn);">wij waren</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>les réseaux sociaux</b></td><td style="padding:6px;border:1px solid var(--lijn);">de social media</td><td style="padding:6px;border:1px solid var(--lijn);"><b>tu vas bien?</b></td><td style="padding:6px;border:1px solid var(--lijn);">gaat het goed met je?</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>le portable</b></td><td style="padding:6px;border:1px solid var(--lijn);">de mobiele telefoon</td><td style="padding:6px;border:1px solid var(--lijn);"><b>bienvenue</b></td><td style="padding:6px;border:1px solid var(--lijn);">welkom</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>l'addition (v)</b></td><td style="padding:6px;border:1px solid var(--lijn);">de rekening</td><td style="padding:6px;border:1px solid var(--lijn);"><b>à plus</b></td><td style="padding:6px;border:1px solid var(--lijn);">tot later</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>dire</b></td><td style="padding:6px;border:1px solid var(--lijn);">zeggen</td><td style="padding:6px;border:1px solid var(--lijn);"><b>grâce à</b></td><td style="padding:6px;border:1px solid var(--lijn);">dankzij</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>penser</b></td><td style="padding:6px;border:1px solid var(--lijn);">denken</td><td style="padding:6px;border:1px solid var(--lijn);"><b>devant / derrière</b></td><td style="padding:6px;border:1px solid var(--lijn);">voor / achter</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>attendre</b></td><td style="padding:6px;border:1px solid var(--lijn);">wachten</td><td style="padding:6px;border:1px solid var(--lijn);"><b>près de</b></td><td style="padding:6px;border:1px solid var(--lijn);">dichtbij</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>utiliser</b></td><td style="padding:6px;border:1px solid var(--lijn);">gebruiken</td><td style="padding:6px;border:1px solid var(--lijn);"><b>heureux, -euse</b></td><td style="padding:6px;border:1px solid var(--lijn);">gelukkig</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>travailler / payer</b></td><td style="padding:6px;border:1px solid var(--lijn);">werken / betalen</td><td style="padding:6px;border:1px solid var(--lijn);"><b>drôle</b></td><td style="padding:6px;border:1px solid var(--lijn);">grappig</td></tr>
    </table>

    <h4>Blok B: Mensen, tijd en herkenning (p. 48)</h4>
    <ul>
      <li><b>les gens (m mv):</b> de mensen | <b>la tête:</b> het hoofd | <b>le temps:</b> de tijd | <b>le truc:</b> het ding</li>
      <li><b>presque:</b> bijna | <b>pourtant:</b> toch | <b>maintenant:</b> nu | <b>avoir besoin (de):</b> nodig hebben</li>
      <li><b>oublier:</b> vergeten | <b>arrêter:</b> stoppen | <b>né(e):</b> geboren | <b>facile:</b> makkelijk</li>
      <li><b>nouveau, nouvelle:</b> nieuw | <b>premier, première:</b> eerste | <b>vieux, vieille:</b> oud | <b>bon, bonne:</b> goed</li>
      <li><i>Blauw blok:</i> <b>le conseil:</b> advies | <b>la raison:</b> reden | <b>la dent:</b> tand | <b>le sens de l'humour:</b> gevoel voor humor | <b>faire attention à:</b> opletten | <b>télécharger:</b> downloaden | <b>garder:</b> bewaren | <b>montrer:</b> laten zien</li>
    </ul>
  """,
  "vragen": [
    {"type": "mc", "vraag": "Wat betekent <b>'le portable'</b>?", "opties": ["de mobiele telefoon", "het scherm", "de computer", "de tablet"], "antwoord": 0, "uitleg": "'Le portable' is de mobiele telefoon."},
    {"type": "mc", "vraag": "Vertaal <b>'de rekening'</b> (in een restaurant/café):", "opties": ["l'addition", "la réaction", "le message", "le prix"], "antwoord": 0, "uitleg": "'L'addition' (vrouwelijk) betekent de rekening."},
    {"type": "invoer","vraag": "Vertaal naar het Frans (de foto): <i>Regarde cette belle ... !</i>", "antwoord": "photo|la photo", "uitleg": "'La photo' = de foto."},
    {"type": "mc", "vraag": "Welk Frans werkwoord betekent <b>'wachten'</b>?", "opties": ["attendre", "entendre", "répondre", "perdre"], "antwoord": 0, "uitleg": "'Attendre' betekent wachten."},
    {"type": "mc", "vraag": "Wat betekent <b>'les réseaux sociaux'</b>?", "opties": ["de social media", "de websites", "de contacten", "de vrienden"], "antwoord": 0, "uitleg": "'Les réseaux sociaux' zijn de sociale media."},
    {"type": "waaronwaar", "vraag": "De uitdrukking <b>'grâce à'</b> betekent 'ondanks'.", "antwoord": False, "uitleg": "Onwaar. 'Grâce à' betekent 'dankzij'."},
    {"type": "invoer","vraag": "Wat betekent het Franse woord <b>'presque'</b> in het Nederlands?", "antwoord": "bijna", "uitleg": "'Presque' betekent bijna."},
    {"type": "mc", "vraag": "Wat is het tegenovergestelde van <b>'devant'</b> (voor)?", "opties": ["derrière (achter)", "près de (dichtbij)", "maintenant (nu)", "pourtant (toch)"], "antwoord": 0, "uitleg": "'Derrière' betekent achter."},
    {"type": "mc", "vraag": "Hoe vertaal je <b>'nodig hebben'</b> in het Frans?", "opties": ["avoir besoin de", "avoir envie de", "avoir peur de", "faire attention à"], "antwoord": 0, "uitleg": "'Avoir besoin de' betekent nodig hebben."},
    {"type": "invoer","vraag": "Vertaal het werkwoord <i>'stoppen'</i> naar het Frans: <i>Tu dois ... !</i>", "antwoord": "arrêter|arreter", "uitleg": "'Arrêter' betekent stoppen."},
    {"type": "mc", "vraag": "Wat betekent <b>'les gens'</b>?", "opties": ["de mensen", "de meisjes", "de leraren", "de buren"], "antwoord": 0, "uitleg": "'Les gens' betekent de mensen."},
    {"type": "mc", "vraag": "Wat is het Franse woord voor <b>'makkelijk'</b>?", "opties": ["facile", "difficile", "nouveau", "rapide"], "antwoord": 0, "uitleg": "'Facile' betekent makkelijk."},
    {"type": "waaronwaar", "vraag": "In het Frans betekent <b>'la tête'</b> 'het hoofd'.", "antwoord": True, "uitleg": "Waar. 'La tête' is het hoofd."},
    {"type": "invoer","vraag": "Wat betekent <b>'j'y vais'</b> in het Nederlands?", "antwoord": "ik ga weg|ik ga|ik ga ervandoor", "uitleg": "'J'y vais' betekent ik ga weg."},
    {"type": "mc", "vraag": "Welk Frans werkwoord betekent <b>'laten zien'</b>?", "opties": ["montrer", "garder", "télécharger", "payer"], "antwoord": 0, "uitleg": "'Montrer' betekent laten zien."}
  ]
}

o2 = {
  "id": "fr-u1-2",
  "hoofdstuk": 1,
  "paragraaf": "1.2",
  "titel": "Woordenschat 1.2 · p. 49 (blok E & F) · Karakter, activiteiten & getallen",
  "korteUitleg": "Woordenschat over karaktereigenschappen, vrienden, activiteiten, getallen en werkwoorden.",
  "icoon": "🎸",
  "kleur": "oranje",
  "theorie": """
    <h3>1.2 Woordenschat: pagina 49 (Blok E & F)</h3>
    <div class="info-box">
      <b>Karakter & Vriendschap (Blok E):</b><br>
      • <b>la meilleure amie:</b> de beste vriendin<br>
      • <b>marrant(e):</b> grappig | <b>intelligent(e):</b> slim | <b>méchant(e):</b> gemeen<br>
      • <b>égoïste:</b> egoïstisch | <b>timide:</b> verlegen | <b>paresseux, -euse:</b> lui<br>
      • <b>souvent:</b> vaak | <b>une fois par semaine:</b> een keer per week<br>
      • <b>au club de sport:</b> op de sportclub | <b>à l'école:</b> op school | <b>chez des amis:</b> bij vrienden<br>
      • <b>regarder la télé:</b> televisie kijken | <b>faire du sport:</b> sporten | <b>jouer de la guitare:</b> gitaar spelen | <b>bavarder:</b> kletsen
    </div>

    <h4>Blok F: Waarde, getallen en werkwoorden (p. 49)</h4>
    <table class="vocab-tabel" style="width:100%;border-collapse:collapse;margin:12px 0;">
      <tr style="background:var(--oranje-licht);">
        <th style="padding:6px;border:1px solid var(--lijn);">Frans 🇫🇷</th>
        <th style="padding:6px;border:1px solid var(--lijn);">Nederlands 🇳🇱</th>
        <th style="padding:6px;border:1px solid var(--lijn);">Frans 🇫🇷</th>
        <th style="padding:6px;border:1px solid var(--lijn);">Nederlands 🇳🇱</th>
      </tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>l'or (m)</b></td><td style="padding:6px;border:1px solid var(--lijn);">het goud</td><td style="padding:6px;border:1px solid var(--lijn);"><b>impossible</b></td><td style="padding:6px;border:1px solid var(--lijn);">onmogelijk</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>l'argent (m)</b></td><td style="padding:6px;border:1px solid var(--lijn);">het geld, het zilver</td><td style="padding:6px;border:1px solid var(--lijn);"><b>pauvre</b></td><td style="padding:6px;border:1px solid var(--lijn);">arm</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>le prix</b></td><td style="padding:6px;border:1px solid var(--lijn);">de prijs</td><td style="padding:6px;border:1px solid var(--lijn);"><b>cher, chère</b></td><td style="padding:6px;border:1px solid var(--lijn);">duur</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>le parfum</b></td><td style="padding:6px;border:1px solid var(--lijn);">de smaak</td><td style="padding:6px;border:1px solid var(--lijn);"><b>américain(e)</b></td><td style="padding:6px;border:1px solid var(--lijn);">Amerikaans</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>par an</b></td><td style="padding:6px;border:1px solid var(--lijn);">per jaar</td><td style="padding:6px;border:1px solid var(--lijn);"><b>mieux</b></td><td style="padding:6px;border:1px solid var(--lijn);">beter</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>cent</b></td><td style="padding:6px;border:1px solid var(--lijn);">100 (honderd)</td><td style="padding:6px;border:1px solid var(--lijn);"><b>vendre</b></td><td style="padding:6px;border:1px solid var(--lijn);">verkopen</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>mille</b></td><td style="padding:6px;border:1px solid var(--lijn);">1.000 (duizend)</td><td style="padding:6px;border:1px solid var(--lijn);"><b>exister</b></td><td style="padding:6px;border:1px solid var(--lijn);">bestaan</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>un million</b></td><td style="padding:6px;border:1px solid var(--lijn);">1.000.000</td><td style="padding:6px;border:1px solid var(--lijn);"><b>savoir</b></td><td style="padding:6px;border:1px solid var(--lijn);">weten</td></tr>
    </table>
    <p><i>Herkenning (blauw blok):</i> <b>le visiteur:</b> bezoeker | <b>le concours:</b> wedstrijd | <b>le cerveau:</b> hersenen | <b>en moyenne:</b> gemiddeld | <b>admirer:</b> bewonderen | <b>prouver:</b> bewijzen | <b>compter:</b> tellen | <b>fêter:</b> vieren.</p>
  """,
  "vragen": [
    {"type": "mc", "vraag": "Wat betekent <b>'la meilleure amie'</b>?", "opties": ["de beste vriendin", "de moeder", "de zus", "de klasgenoot"], "antwoord": 0, "uitleg": "'La meilleure amie' is de beste vriendin."},
    {"type": "mc", "vraag": "Wat is het Franse woord voor <b>'lui'</b>?", "opties": ["paresseux, -euse", "timide", "marrant", "sympa"], "antwoord": 0, "uitleg": "'Paresseux' (m) en 'paresseuse' (v) betekenen lui."},
    {"type": "waaronwaar", "vraag": "Het Franse woord <b>'méchant(e)'</b> betekent 'gemeen'.", "antwoord": True, "uitleg": "Waar. 'Méchant(e)' is gemeen."},
    {"type": "invoer","vraag": "Vertaal het woord <i>'verlegen'</i> naar het Frans: <i>Mon frère est très ... .</i>", "antwoord": "timide", "uitleg": "'Timide' betekent verlegen."},
    {"type": "mc", "vraag": "Wat betekent <b>'souvent'</b>?", "opties": ["vaak", "zelden", "nooit", "altijd"], "antwoord": 0, "uitleg": "'Souvent' betekent vaak."},
    {"type": "mc", "vraag": "Hoe zeg je <b>'een keer per week'</b> in het Frans?", "opties": ["une fois par semaine", "par an", "en moyenne", "tous les jours"], "antwoord": 0, "uitleg": "'Une fois par semaine' = een keer per week."},
    {"type": "waaronwaar", "vraag": "Het Franse werkwoord <b>'bavarder'</b> betekent 'slapen'.", "antwoord": False, "uitleg": "Onwaar. 'Bavarder' betekent kletsen."},
    {"type": "invoer","vraag": "Vul het ontbrekende werkwoord in (sporten): <i>Il aime ... du sport.</i>", "antwoord": "faire", "uitleg": "'Faire du sport' = sporten."},
    {"type": "mc", "vraag": "Wat betekent <b>'l'argent'</b> (m)?", "opties": ["het geld / het zilver", "het goud", "de schat", "de portemonnee"], "antwoord": 0, "uitleg": "'L'argent' is geld en zilver."},
    {"type": "mc", "vraag": "Wat is de Franse vertaling van <b>'duur'</b>?", "opties": ["cher, chère", "pauvre", "mieux", "américain"], "antwoord": 0, "uitleg": "'Cher' (m) en 'chère' (v) betekenen duur."},
    {"type": "invoer","vraag": "Wat is het getal <b>'mille'</b> in cijfers?", "antwoord": "1000|1.000", "uitleg": "'Mille' is 1000."},
    {"type": "mc", "vraag": "Welk Frans werkwoord betekent <b>'weten'</b>?", "opties": ["savoir", "vendre", "dire", "penser"], "antwoord": 0, "uitleg": "'Savoir' betekent weten."},
    {"type": "mc", "vraag": "Welk werkwoord betekent <b>'verkopen'</b>?", "opties": ["vendre", "payer", "exister", "admirer"], "antwoord": 0, "uitleg": "'Vendre' betekent verkopen."},
    {"type": "waaronwaar", "vraag": "Het Franse woord <b>'mieux'</b> betekent 'beter'.", "antwoord": True, "uitleg": "Waar. 'Mieux' = beter."},
    {"type": "invoer","vraag": "Wat betekent <b>'le cerveau'</b> in het Nederlands?", "antwoord": "de hersenen|hersenen", "uitleg": "'Le cerveau' betekent de hersenen."}
  ]
}

o3 = {
  "id": "fr-u1-3",
  "hoofdstuk": 1,
  "paragraaf": "1.3",
  "titel": "Woordenschat 1.3 · p. 50 (phrases-clés C & G) · Social media & vriendschap",
  "korteUitleg": "Belangrijke spreek- en dialoogzinnen over sociale netwerken en praten over vrienden.",
  "icoon": "💬",
  "kleur": "groen",
  "theorie": """
    <h3>1.3 Woordenschat: pagina 50 (Phrases-clés C & G)</h3>
    <div class="info-box">
      <b>Sleutelzinnen uit het hoofd leren:</b> Deze zinnen moet je zowel kunnen begrijpen als zelf kunnen schrijven/zeggen.
    </div>

    <h4>C: Parler des réseaux sociaux (p. 50)</h4>
    <ul>
      <li><b>Quel est le code WiFi?</b> = Wat is de wificode?</li>
      <li><b>C'est ... et le mot de passe c'est ...</b> = Dat is ... en het wachtwoord is ...</li>
      <li><b>Tu as Insta?</b> = Heb je Insta?</li>
      <li><b>Bien sûr, mon compte c'est ...</b> = Natuurlijk, mijn account is ...</li>
      <li><b>Tu publies beaucoup de photos?</b> = Post je veel foto's?</li>
      <li><b>Oui, et je publie aussi des vidéos.</b> = Ja, en ik post ook video's.</li>
      <li><b>Qu'est-ce que tu publies d'autre?</b> = Wat post je nog meer?</li>
      <li><b>Je publie aussi des stories.</b> = Ik post ook stories.</li>
      <li><b>Tu suis Théo Gordy?</b> = Volg je Théo Gordy?</li>
      <li><b>Oui, je regarde ses vidéos.</b> = Ja, ik kijk naar zijn video's.</li>
      <li><b>Non, je ne suis pas de stars.</b> = Nee, ik volg geen sterren.</li>
    </ul>

    <h4>G: Parler de ses amis (p. 50)</h4>
    <ul>
      <li><b>Qui est ton meilleur ami?</b> = Wie is je beste vriend?</li>
      <li><b>Mon meilleur ami, c'est Max.</b> = Mijn beste vriend is Max.</li>
      <li><b>Je le connais depuis dix ans.</b> = Ik ken hem sinds tien jaar.</li>
      <li><b>J'ai rencontré Max au club de sport.</b> = Ik heb Max bij de sportclub ontmoet.</li>
      <li><b>Pourquoi c'est ton meilleur ami?</b> = Waarom is het je beste vriend?</li>
      <li><b>Il est sympa et on peut parler de tout.</b> = Hij is aardig en we kunnen over alles praten.</li>
      <li><b>On aime jouer en ligne ensemble.</b> = We spelen graag samen online.</li>
      <li><b>On se voit presque tous les jours.</b> = We zien elkaar bijna elke dag.</li>
    </ul>
  """,
  "vragen": [
    {"type": "mc", "vraag": "Hoe vraag je in het Frans naar de wificode?", "opties": ["Quel est le code WiFi ?", "Où est le WiFi ?", "Tu as du WiFi ?", "Combien coûte le WiFi ?"], "antwoord": 0, "uitleg": "'Quel est le code WiFi ?' vraagt naar de wificode."},
    {"type": "mc", "vraag": "Wat betekent <b>'le mot de passe'</b>?", "opties": ["het wachtwoord", "het e-mailadres", "de gebruikersnaam", "het telefoonnummer"], "antwoord": 0, "uitleg": "'Le mot de passe' is het wachtwoord."},
    {"type": "invoer","vraag": "Vul aan (volgen): <i>Tu ... Théo Gordy ?</i>", "antwoord": "suis", "uitleg": "'Tu suis' (van suivre) = jij volgt."},
    {"type": "mc", "vraag": "Wat betekent <b>'Non, je ne suis pas de stars.'</b>?", "opties": ["Nee, ik volg geen sterren.", "Nee, ik ben geen muzikant.", "Nee, ik hou niet van films.", "Nee, ik heb geen vrienden."], "antwoord": 0, "uitleg": "'Suivre' betekent volgen; 'je ne suis pas de stars' = ik volg geen beroemdheden."},
    {"type": "mc", "vraag": "Hoe vraag je: <b>'Wat post je nog meer?'</b>?", "opties": ["Qu'est-ce que tu publies d'autre ?", "Pourquoi tu publies ça ?", "Quand tu publies une photo ?", "Avec qui tu publies ?"], "antwoord": 0, "uitleg": "'Qu'est-ce que tu publies d'autre ?' is de juiste zin."},
    {"type": "waaronwaar", "vraag": "De zin <b>'Je publie aussi des stories'</b> betekent 'Ik post ook stories'.", "antwoord": True, "uitleg": "Waar. 'Aussi' = ook."},
    {"type": "invoer","vraag": "Vul het woord in voor <i>'Natuurlijk'</i>: <i>... sûr, mon compte c'est @duru.</i>", "antwoord": "Bien|bien", "uitleg": "'Bien sûr' betekent natuurlijk."},
    {"type": "mc", "vraag": "Hoe vraag je: <b>'Wie is je beste vriend?'</b>?", "opties": ["Qui est ton meilleur ami ?", "Où est ton meilleur ami ?", "Comment est ton meilleur ami ?", "Quel âge a ton meilleur ami ?"], "antwoord": 0, "uitleg": "'Qui' betekent wie."},
    {"type": "mc", "vraag": "Wat betekent: <b>'Je le connais depuis dix ans.'</b>?", "opties": ["Ik ken hem sinds tien jaar.", "Hij is tien jaar oud.", "We wonen al tien jaar hier.", "Ik zie hem over tien dagen."], "antwoord": 0, "uitleg": "'Depuis dix ans' = sinds tien jaar."},
    {"type": "waaronwaar", "vraag": "In <b>'J'ai rencontré Max au club de sport'</b> betekent 'au club de sport' op school.", "antwoord": False, "uitleg": "Onwaar. 'Au club de sport' is op de sportclub."},
    {"type": "invoer","vraag": "Vul in (Waarom): <i>... c'est ton meilleur ami ?</i>", "antwoord": "Pourquoi|pourquoi", "uitleg": "'Pourquoi' betekent waarom."},
    {"type": "mc", "vraag": "Hoe zeg je: <b>'We spelen graag samen online.'</b>?", "opties": ["On aime jouer en ligne ensemble.", "On ne joue jamais ensemble.", "On préfère étudier seuls.", "On regarde la télé ensemble."], "antwoord": 0, "uitleg": "'On aime jouer en ligne ensemble' is de juiste Franse vertaling."},
    {"type": "waaronwaar", "vraag": "De uitdrukking <b>'tous les jours'</b> betekent 'elke dag / alle dagen'.", "antwoord": True, "uitleg": "Waar. 'Tous les jours' = elke dag."},
    {"type": "invoer","vraag": "Wat betekent het woord <b>'ensemble'</b> in het Nederlands?", "antwoord": "samen", "uitleg": "'Ensemble' betekent samen."},
    {"type": "mc", "vraag": "Wat betekent <b>'On se voit presque tous les jours'</b>?", "opties": ["We zien elkaar bijna elke dag.", "We bellen elkaar nooit.", "We zien elkaar een keer per maand.", "We gaan samen op vakantie."], "antwoord": 0, "uitleg": "'On se voit' = we zien elkaar, 'presque' = bijna, 'tous les jours' = elke dag."}
  ]
}

o4 = {
  "id": "fr-u1-4",
  "hoofdstuk": 1,
  "paragraaf": "1.4",
  "titel": "Woordenschat 1.4 · p. 51 (grammaire D & H) · Bijvoeglijk naamwoord & -re werkwoorden",
  "korteUitleg": "Vrouwelijke vormen van bijvoeglijke naamwoorden, hun plaats in de zin, en regelmatige werkwoorden op -re.",
  "icoon": "⚙️",
  "kleur": "paars",
  "theorie": """
    <h3>1.4 Woordenschat: pagina 51 (Grammaire D & H)</h3>

    <h4>D: Onregelmatige vrouwelijke vormen van bijvoeglijke naamwoorden (p. 51)</h4>
    <table class="vocab-tabel" style="width:100%;border-collapse:collapse;margin:12px 0;">
      <tr style="background:var(--paars-licht);">
        <th style="padding:6px;border:1px solid var(--lijn);">Mannelijk</th>
        <th style="padding:6px;border:1px solid var(--lijn);">Vrouwelijk</th>
        <th style="padding:6px;border:1px solid var(--lijn);">Voorbeeld</th>
      </tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>-ien</b></td><td style="padding:6px;border:1px solid var(--lijn);"><b>-ienne</b></td><td style="padding:6px;border:1px solid var(--lijn);">italien / italienne</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>-eux</b></td><td style="padding:6px;border:1px solid var(--lijn);"><b>-euse</b></td><td style="padding:6px;border:1px solid var(--lijn);">heureux / heureuse</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>-if</b></td><td style="padding:6px;border:1px solid var(--lijn);"><b>-ive</b></td><td style="padding:6px;border:1px solid var(--lijn);">sportif / sportive</td></tr>
      <tr><td style="padding:6px;border:1px solid var(--lijn);"><b>onregelmatig</b></td><td style="padding:6px;border:1px solid var(--lijn);"><b>onregelmatig</b></td><td style="padding:6px;border:1px solid var(--lijn);">bon / bonne · beau / belle · nouveau / nouvelle · vieux / vieille</td></tr>
    </table>
    <p><b>Plaats vóór het zelfstandig naamwoord:</b> <i>bon, grand, petit, premier, dernier, joli, jeune, vieux, nouveau, mauvais, long, beau</i>.<br>
    Bijv.: <code>C'est un jeune influenceur.</code> | <code>J'ai une nouvelle copine.</code><br>
    Nationaliteiten en kleuren staan er <b>achter</b>: <code>C'est un YouTubeur français.</code></p>

    <h4>H: Regelmatige werkwoorden op -re (p. 51)</h4>
    <p>Haal <b>-re</b> weg van het hele werkwoord. Wat overblijft is de stam. Voeg de vaste uitgangen toe:</p>
    <div class="formule-box">
      <b>répondre (antwoorden):</b><br>
      • je répond<b>s</b><br>
      • tu répond<b>s</b><br>
      • il/elle/on répond (géén uitgang!)<br>
      • nous répond<b>ons</b><br>
      • vous répond<b>ez</b><br>
      • ils/elles répond<b>ent</b><br><br>
      Net zo gaan: <b>attendre</b> (wachten), <b>entendre</b> (horen), <b>vendre</b> (verkopen), <b>perdre</b> (verliezen), <b>défendre</b> (verdedigen).<br>
      <b>Passé composé:</b> <code>Il a perdu son portable.</code> (avoir + voltooid deelwoord op <b>-u</b>).
    </div>
  """,
  "vragen": [
    {"type": "mc", "vraag": "Wat is de vrouwelijke vorm van <b>'italien'</b>?", "opties": ["italienne", "italieuse", "italie", "italive"], "antwoord": 0, "uitleg": "-ien wordt -ienne."},
    {"type": "mc", "vraag": "Wat is de vrouwelijke vorm van <b>'heureux'</b>?", "opties": ["heureuse", "heureusse", "heureuxte", "heureuve"], "antwoord": 0, "uitleg": "-eux wordt -euse."},
    {"type": "waaronwaar", "vraag": "De vrouwelijke vorm van <b>'sportif'</b> is <b>'sportive'</b>.", "antwoord": True, "uitleg": "Waar. -if wordt -ive."},
    {"type": "invoer","vraag": "Wat is de vrouwelijke vorm van <b>'nouveau'</b>?", "antwoord": "nouvelle", "uitleg": "Nouveau wordt nouvelle."},
    {"type": "mc", "vraag": "Wat is de vrouwelijke vorm van <b>'vieux'</b> (oud)?", "opties": ["vieille", "vieuse", "vieuxe", "vieillarde"], "antwoord": 0, "uitleg": "Vieux wordt vieille."},
    {"type": "mc", "vraag": "Wat is de vrouwelijke vorm van <b>'beau'</b> (mooi)?", "opties": ["belle", "beause", "beauté", "beauve"], "antwoord": 0, "uitleg": "Beau wordt belle."},
    {"type": "waaronwaar", "vraag": "Het bijvoeglijk naamwoord <b>'jeune'</b> staat meestal VÓÓR het zelfstandig naamwoord (zoals: <i>un jeune influenceur</i>).", "antwoord": True, "uitleg": "Waar. Jeune staat voor het znw."},
    {"type": "invoer","vraag": "Vul de vrouwelijke vorm in van <i>bon</i>: <i>C'est une ... idée !</i>", "antwoord": "bonne", "uitleg": "Bon wordt bonne."},
    {"type": "mc", "vraag": "Waar hoort de nationaliteit <b>'français'</b> te staan?", "opties": ["Achter het zelfstandig naamwoord (un YouTubeur français)", "Vóór het zelfstandig naamwoord", "Aan het begin van de zin", "Dat maakt niets uit"], "antwoord": 0, "uitleg": "Nationaliteiten staan altijd achter het znw."},
    {"type": "mc", "vraag": "Welke uitgangen horen bij regelmatige werkwoorden op <b>-re</b> (présent)?", "opties": ["-s, -s, -, -ons, -ez, -ent", "-e, -es, -e, -ons, -ez, -ent", "-is, -is, -it, -issons, -issez, -issent", "-x, -x, -t, -ons, -ez, -ent"], "antwoord": 0, "uitleg": "De vaste uitgangen zijn: -s, -s, -, -ons, -ez, -ent."},
    {"type": "waaronwaar", "vraag": "Bij <b>il/elle/on</b> krijgt een -re werkwoord een extra <b>-t</b> (zoals: <i>il répond-t</i>).", "antwoord": False, "uitleg": "Onwaar. Bij il/elle/on is er GEEN uitgang (il répond)."},
    {"type": "invoer","vraag": "Vervoeg <b>répondre</b> voor <i>je</i>: <i>Je ... au message.</i>", "antwoord": "réponds|reponds", "uitleg": "Bij 'je' krijgt een -re werkwoord de uitgang -s: stam 'répond' + 's' = je réponds."},
    {"type": "mc", "vraag": "Vervoeg <b>attendre</b> voor <i>nous</i>:", "opties": ["nous attendons", "nous attendez", "nous attendent", "nous attends"], "antwoord": 0, "uitleg": "Nous attendons."},
    {"type": "mc", "vraag": "Wat betekent <b>'perdre'</b>?", "opties": ["verliezen", "antwoorden", "wachten", "horen"], "antwoord": 0, "uitleg": "'Perdre' betekent verliezen."},
    {"type": "invoer","vraag": "Vul het voltooid deelwoord in van <b>perdre</b>: <i>Il a ... son portable. (verloren)</i>", "antwoord": "perdu", "uitleg": "Het voltooid deelwoord is perdu."}
  ]
}

def save_onderwerp(filename, data):
    balance_mc(data["vragen"])
    path = os.path.join(DATA_DIR, filename)
    content = f"/* Onderwerp {data['paragraaf']} — {data['titel']}\n   Grandes Lignes 3 HAVO Unité {data['hoofdstuk']} */\nDURU.register({json.dumps(data, indent=2, ensure_ascii=False)});\n"
    with open(path, "w", encoding="utf-8") as out:
        out.write(content)
    print(f"  [OK] Onderwerp saved: {filename} ({len(data['vragen'])} vragen)")

if __name__ == "__main__":
    save_onderwerp("h1_1.js", o1)
    save_onderwerp("h1_2.js", o2)
    save_onderwerp("h1_3.js", o3)
    save_onderwerp("h1_4.js", o4)
    print("\n🎉 Alle 4 Unité 1 Oefen-onderwerpen (Quiz & Theorie) succesvol aangemaakt!")


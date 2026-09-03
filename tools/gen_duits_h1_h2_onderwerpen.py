#!/usr/bin/env python3
"""
Generates all 18 Onderwerpen (Theory & Oefenquizzes) for HAVO 3 Duits (Neue Kontakte 3 HAVO)
- Hoofdstuk 1: Umgebung & Wetter (1.1, 1.2, 1.3)
- Hoofdstuk 2: Gesundheit & Körper (2.1, 2.2, 2.3)
- Hoofdstuk 3: Unterwegs (3.1, 3.2, 3.3)
- Hoofdstuk 4: Veranstaltungen (4.1, 4.2, 4.3)
- Hoofdstuk 5: Zukunft & Berufe (5.1, 5.2, 5.3)
- Hoofdstuk 6: In Aktion (6.1, 6.2, 6.3)
"""

import os
import json

BASE_DIR = "/home/mesuto/Documents/PROJELER/duru_okul/havo3/duits"
DATA_DIR = os.path.join(BASE_DIR, "js/data")
os.makedirs(DATA_DIR, exist_ok=True)

def balance_mc(questions):
    mc_indices = [i for i, q in enumerate(questions) if q.get("type") == "mc"]
    target_pattern = [0, 1, 2, 3] * (len(mc_indices) // 4 + 2)
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

def write_onderwerp(filename, data):
    balance_mc(data["vragen"])
    path = os.path.join(DATA_DIR, filename)
    content = f"""/* Onderwerp {data['paragraaf']} — {data['titel']}
   Neue Kontakte 3 HAVO Hoofdstuk {data['hoofdstuk']} */
DURU.register({json.dumps(data, indent=2, ensure_ascii=False)});
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  [✓] Onderwerp saved: {filename}")

# ==========================================
# 1. UMGEBUNG & WETTER
# ==========================================
h1_1 = {
  "id": "dui-h1-1",
  "hoofdstuk": 1,
  "paragraaf": "1.1",
  "titel": "Wortschatz & Sprachmittel: Natur, Wetter & Jahreszeiten",
  "korteUitleg": "Woordenschat over het weer, seizoenen, landschappen en weerberichten in het Duits.",
  "icoon": "🌲",
  "kleur": "blauw",
  "theorie": """
    <h3>1.1 Wortschatz & Sprachmittel: Natur, Wetter & Jahreszeiten</h3>
    <div class="info-box">
      <b>Kernbegrippen:</b> das Wetter (het weer), die Sonne (de zon), der Regen (de regen), der Schnee (de sneeuw), der Wind (de wind), die Wolke (de wolk), das Gewitter (het onweer), der Nebel (de mist), die Temperatur (de temperatuur), der Wald (het bos), die Berge (de bergen), der Fluss (de rivier), der See (het meer), das Meer (de zee), die Jahreszeit (het seizoen).
    </div>
    <h4>1. Het Weer beschrijven (Wetterbericht)</h4>
    <p>In het Duits gebruik je vaak het onpersoonlijke <code>es</code> om het weer te beschrijven:</p>
    <ul>
      <li><code>Es regnet</code> = Het regent. (Zelfstandig naamwoord: <i>der Regen</i>)</li>
      <li><code>Es schneit</code> = Het sneeuwt. (Zelfstandig naamwoord: <i>der Schnee</i>)</li>
      <li><code>Die Sonne scheint</code> = De zon schijnt.</li>
      <li><code>Es ist bewölkt / wolkig</code> = Het is bewolkt.</li>
      <li><code>Es donnert und blitzt</code> = Het dondert en bliksemt. (<i>das Gewitter</i>)</li>
      <li><code>Es ist neblig / windig</code> = Het is mistig / winderig.</li>
      <li><code>Es sind 20 Grad</code> = Het is 20 graden.</li>
    </ul>

    <h4>2. Seizoenen en Maanden (Jahreszeiten & Monate)</h4>
    <p>Alle seizoenen en maanden zijn in het Duits <b>mannelijk (der)</b>. Als je wilt zeggen 'in de lente/zomer' of 'in mei/juli', gebruik je het voorzetsel <b>im</b> (in dem):</p>
    <div class="formule-box">
      <b>Die vier Jahreszeiten:</b><br>
      • <b>der Frühling</b> (de lente) → <i>im Frühling</i><br>
      • <b>der Sommer</b> (de zomer) → <i>im Sommer</i><br>
      • <b>der Herbst</b> (de herfst) → <i>im Herbst</i><br>
      • <b>der Winter</b> (de winter) → <i>im Winter</i><br><br>
      <b>Die zwölf Monate:</b> Januar, Februar, März, April, Mai, Juni, Juli, August, September, Oktober, November, Dezember (bijv. <i>im August</i>).
    </div>

    <h4>3. Sprachmittel: Praten over de natuur en het weer</h4>
    <p>Met de Sprachmittel leer je vaste bouwstenen om een gesprek te voeren:</p>
    <ul>
      <li><i>Wie ist das Wetter heute?</i> — Hoe is het weer vandaag?</li>
      <li><i>Morgen wird es sonnig und warm.</i> — Morgen wordt het zonnig en warm.</li>
      <li><i>In den Bergen liegt noch viel Schnee.</i> — In de bergen ligt nog veel sneeuw.</li>
      <li><i>Wir machen einen Spaziergang im Wald.</i> — We maken een wandeling in het bos.</li>
    </ul>
  """,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat is de juiste Duitse vertaling voor 'De zon schijnt en het is twintig graden'?",
      "opties": ["Die Sonne scheint und es sind zwanzig Grad.", "Der Sonne scheint und es ist zwanzig Grad.", "Die Sonne regnet und es gibt zwanzig Grad.", "Das Wetter scheint zwanzig Grad."],
      "antwoord": 0,
      "uitleg": "In het Duits zeg je 'Die Sonne scheint' en bij temperaturen meervoud 'es sind zwanzig Grad'."
    },
    {
      "type": "mc",
      "vraag": "Welk Duits woord betekent 'het onweer'?",
      "opties": ["das Gewitter", "der Nebel", "die Wolke", "der Schnee"],
      "antwoord": 0,
      "uitleg": "'Das Gewitter' betekent onweer. 'Der Nebel' is mist en 'die Wolke' is wolk."
    },
    {
      "type": "mc",
      "vraag": "Welk lidwoord en voorzetsel horen bij seizoenen zoals 'zomer' (in de zomer)?",
      "opties": ["der Sommer → im Sommer", "das Sommer → am Sommer", "die Sommer → in die Sommer", "der Sommer → zum Sommer"],
      "antwoord": 0,
      "uitleg": "Alle seizoenen zijn mannelijk (der Sommer) en 'in de zomer' vertaal je met 'im Sommer'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de zin: 'Morgen wird es stürmisch und es regnet den ganzen Tag'?",
      "opties": ["Morgen wordt het stormachtig en regent het de hele dag.", "Morgen was het zonnig en viel er geen regen.", "Vandaag sneeuwt het en waait het hard.", "Gisteren was het mistig in het hele land."],
      "antwoord": 0,
      "uitleg": "'Stürmisch' betekent stormachtig en 'es regnet den ganzen Tag' betekent dat het de hele dag regent."
    },
    {
      "type": "waaronwaar",
      "vraag": "In het Duits hebben alle twaalf maanden het mannelijke lidwoord 'der' (bijv. der Mai, der Oktober).",
      "antwoord": True,
      "uitleg": "Waar! Alle maanden en seizoenen zijn in de Duitse taal mannelijk (der)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Duitse woord 'der See' betekent in het Nederlands 'de zee' (de oceaan).",
      "antwoord": False,
      "uitleg": "Onwaar! 'Der See' betekent 'het meer' (zoet water). 'De zee' is in het Duits 'das Meer' of 'die See'."
    },
    {
      "type": "invoer",
      "vraag": "Vertaal het woord tussen haakjes naar het Duits: 'Im Winter liegt viel (sneeuw) auf den Bergen.'",
      "antwoord": "Schnee",
      "uitleg": "'Sneeuw' vertaal je in het Duits met 'Schnee' (met een hoofdletter omdat het een zelfstandig naamwoord is)."
    },
    {
      "type": "invoer",
      "vraag": "Vul het juiste Duitse seizoen in (lente): 'Die Blumen blühen im ____.'",
      "antwoord": "Frühling",
      "uitleg": "De lente is in het Duits 'der Frühling'. In de lente = 'im Frühling'."
    }
  ]
}

h1_2 = {
  "id": "dui-h1-2",
  "hoofdstuk": 1,
  "paragraaf": "1.2",
  "titel": "Grammatik: sein & haben im Präteritum + werden",
  "korteUitleg": "De verleden tijd (onvoltooid verleden tijd) van de hulpwerkwoorden sein en haben, plus de vervoeging van werden.",
  "icoon": "📖",
  "kleur": "blauw",
  "theorie": """
    <h3>1.2 Grammatik: sein & haben im Präteritum + werden</h3>
    <div class="info-box">
      <b>Grammaticafocus:</b> De verleden tijd (Präteritum) van de belangrijkste werkwoorden <i>sein</i> (zijn) en <i>haben</i> (hebben), en de tegenwoordige tijd van <i>werden</i> (worden/zullen).
    </div>
    <h4>1. De verleden tijd van sein (waren / was)</h4>
    <p>Het werkwoord <b>sein</b> is onregelmatig. Let goed op: de vormen voor <code>ich</code> en <code>er/sie/es</code> zijn altijd identiek en hebben <b>geen uitgang</b>:</p>
    <div class="formule-box">
      <b>Präteritum van sein:</b><br>
      • ich <b>war</b> (ik was)<br>
      • du <b>warst</b> (jij was)<br>
      • er / sie / es <b>war</b> (hij / zij / het was)<br>
      • wir <b>waren</b> (wij waren)<br>
      • ihr <b>wart</b> (jullie waren - let op: met één t!)<br>
      • sie / Sie <b>waren</b> (zij waren / u was)
    </div>

    <h4>2. De verleden tijd van haben (hadden / had)</h4>
    <p>Ook bij <b>haben</b> zijn de vormen voor <code>ich</code> en <code>er/sie/es</code> aan elkaar gelijk:</p>
    <div class="formule-box">
      <b>Präteritum van haben:</b><br>
      • ich <b>hatte</b> (ik had)<br>
      • du <b>hattest</b> (jij had)<br>
      • er / sie / es <b>hatte</b> (hij / zij / het had)<br>
      • wir <b>hatten</b> (wij hadden)<br>
      • ihr <b>hattet</b> (jullie hadden)<br>
      • sie / Sie <b>hatten</b> (zij hadden / u had)
    </div>

    <h4>3. Het werkwoord werden (tegenwoordige tijd / Präsens)</h4>
    <p>Het werkwoord <b>werden</b> betekent 'worden'. Bij <code>du</code> en <code>er/sie/es</code> verandert de stamklinker van <i>e</i> naar <i>i</i>:</p>
    <ul>
      <li>ich <b>werde</b> (ik word)</li>
      <li>du <b>wirst</b> (jij wordt - let op: klinkerwisseling naar i!)</li>
      <li>er / sie / es <b>wird</b> (hij / zij / het wordt)</li>
      <li>wir <b>werden</b> (wij worden)</li>
      <li>ihr <b>werdet</b> (jullie worden)</li>
      <li>sie / Sie <b>werden</b> (zij worden / u wordt)</li>
    </ul>
    <p><i>Voorbeeld:</i> Morgen <b>wird</b> das Wetter wieder schön. (Morgen wordt het weer weer mooi.)</p>
  """,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm van 'sein' in de verleden tijd: 'Gestern ____ wir den ganzen Tag am Strand.'",
      "opties": ["waren", "wart", "warst", "hatten"],
      "antwoord": 0,
      "uitleg": "Bij het onderwerp 'wir' hoort de vorm 'waren' (wij waren)."
    },
    {
      "type": "mc",
      "vraag": "Welke vorm van 'haben' past in: 'Lisa ____ gestern keine Zeit für ihre Hausaufgaben.'?",
      "opties": ["hatte", "hattest", "hattet", "waren"],
      "antwoord": 0,
      "uitleg": "Lisa is 'sie' (3e persoon enkelvoud), dus de verleden tijd is 'hatte'."
    },
    {
      "type": "mc",
      "vraag": "Wat is de juiste vorm van 'werden' bij 'du' in de tegenwoordige tijd?",
      "opties": ["du wirst", "du werdest", "du wird", "du werden"],
      "antwoord": 0,
      "uitleg": "Bij 'du' verandert de e in een i: 'du wirst' (jij wordt)."
    },
    {
      "type": "mc",
      "vraag": "Vul aan: 'Ihr ____ letztes Jahr in Berlin, oder?'",
      "opties": ["wart", "waren", "warst", "hattet"],
      "antwoord": 0,
      "uitleg": "Bij 'ihr' (jullie) hoort 'wart' (met één 't' en zonder 'e')."
    },
    {
      "type": "waaronwaar",
      "vraag": "In de verleden tijd (Präteritum) zijn de vormen voor 'ich' en 'er/sie/es' bij sein en haben altijd gelijk (ich war / er war; ich hatte / er hatte).",
      "antwoord": True,
      "uitleg": "Waar! In het Präteritum krijgen noch de 1e persoon (ich) noch de 3e persoon (er/sie/es) een persoonlijke uitgang."
    },
    {
      "type": "waaronwaar",
      "vraag": "De juiste verleden tijdsvorm voor 'ihr' bij sein is 'ihr waart' met dubbel a.",
      "antwoord": False,
      "uitleg": "Onwaar! In het Duits schrijf je 'ihr wart' met één 'a' en één 't'."
    },
    {
      "type": "invoer",
      "vraag": "Vul de juiste vorm van sein (verleden tijd) in: 'Ich ____ gestern sehr müde.'",
      "antwoord": "war",
      "uitleg": "De verleden tijd van sein bij 'ich' is 'war'."
    },
    {
      "type": "invoer",
      "vraag": "Vul de juiste vorm van werden in: 'Es ____ heute Nachmittag sehr warm.'",
      "antwoord": "wird",
      "uitleg": "Bij 'es' (het) hoort de vorm 'wird' (met klinkerwisseling naar i)."
    }
  ]
}

h1_3 = {
  "id": "dui-h1-3",
  "hoofdstuk": 1,
  "paragraaf": "1.3",
  "titel": "Aussprache, Lesen & Landeskunde: Naturräume in Deutschland",
  "korteUitleg": "Uitspraakregels voor klinkers en Umlauten, en Landeskunde over Duitse natuurgebieden (Schwarzwald, Alpen, Harz).",
  "icoon": "🏔️",
  "kleur": "blauw",
  "theorie": """
    <h3>1.3 Aussprache, Lesen & Landeskunde: Naturräume in Deutschland</h3>
    <div class="info-box">
      <b>Thema's:</b> Uitspraak van het alfabet, klinkers (Vokale) en Umlaute (ä, ö, ü), en geografische Landeskunde over de Bondsrepubliek Duitsland.
    </div>
    <h4>1. Ausspracheregeln: Klinkers en Umlaute</h4>
    <p>In het Duits bepalen de puntjes op de klinkers (Umlaut) de uitspraak én betekenis van een woord:</p>
    <ul>
      <li><b>ä</b>: klinkt als de open Nederlandse 'è' (in <i>Wälder</i> = bossen, <i>März</i> = maart).</li>
      <li><b>ö</b>: klinkt als de Nederlandse 'eu' in 'deur' (in <i>schön</i> = mooi, <i>Österreich</i> = Oostenrijk).</li>
      <li><b>ü</b>: klinkt als de Nederlandse 'uu' in 'vuur' (in <i>über</i> = over, <i>Frühling</i> = lente).</li>
      <li><b>ie</b>: spreek je uit als een lange 'ie' (bijv. <i>Wiese</i> = weide, <i>Liebe</i> = liefde).</li>
      <li><b>ei</b>: spreek je uit als 'ai' (bijv. <i>Schnee</i> / <i>Eis</i> = ijs).</li>
      <li><b>eu / äu</b>: spreek je uit als 'oj' (bijv. <i>heute</i> = vandaag, <i>Bäume</i> = bomen).</li>
    </ul>

    <h4>2. Landeskunde: Belangrijke Duitse Natuurgebieden</h4>
    <p>Duitsland kent een grote diversiteit aan landschappen van noord naar zuid:</p>
    <div class="formule-box">
      <b>Van Noord naar Zuid:</b><br>
      • <b>Nord- und Ostseeküste</b>: De Noordzee en Oostzee met de Waddeneilanden (bijv. Sylt, Rügen) en vlak laagland.<br>
      • <b>Die Mittelgebirge</b>: Het middelgebergte in Centraal-Duitsland, zoals de <i>Harz</i>, het <i>Eifel</i>-gebied en het <i>Schwarzwald</i> (Zwarte Woud).<br>
      • <b>Die Alpen</b>: In het zuiden van Beieren (Bayern) liggen de Duitse Alpen met de hoogste berg van Duitsland: de <b>Zugspitze</b> (2.962 meter).<br>
      • <b>Große Flüsse</b>: De bekendste rivieren zijn de <i>Rhein</i> (Rijn), de <i>Donau</i> (Donau) en de <i>Elbe</i>.
    </div>

    <h4>3. Leesstrategie: Signaalwoorden herkennen</h4>
    <p>Bij Duitse leesteksten helpen signaalwoorden je de tekststructuur te begrijpen:</p>
    <ul>
      <li><i>aber</i> = maar | <i>denn / weil</i> = want / omdat</li>
      <li><i>zuerst</i> = eerst | <i>danach / dann</i> = daarna / dan</li>
      <li><i>deshalb</i> = daarom | <i>trotzdem</i> = toch / desondanks</li>
    </ul>
  """,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat is de hoogste berg van Duitsland, gelegen in de Alpen?",
      "opties": ["Die Zugspitze", "Der Brocken", "Der Feldberg", "Der Mont Blanc"],
      "antwoord": 0,
      "uitleg": "De Zugspitze (2.962 meter) in Beieren is de hoogste berg van Duitsland."
    },
    {
      "type": "mc",
      "vraag": "Hoe spreek je de lettercombinatie 'eu' of 'äu' uit in het Duits (zoals in 'heute' of 'Bäume')?",
      "opties": ["Als 'oj'", "Als 'eu'", "Als 'ie'", "Als 'oe'"],
      "antwoord": 0,
      "uitleg": "In het Duits klinkt 'eu' en 'äu' als 'oj' (zoals in het Nederlandse 'hoi')."
    },
    {
      "type": "mc",
      "vraag": "Welk signaalwoord betekent in het Nederlands 'daarom'?",
      "opties": ["deshalb", "obwohl", "trotzdem", "weil"],
      "antwoord": 0,
      "uitleg": "'Deshalb' betekent daarom. 'Weil' betekent omdat en 'trotzdem' betekent toch/desondanks."
    },
    {
      "type": "mc",
      "vraag": "In welk deel van Duitsland ligt het beroemde middelgebergte het Zwarte Woud (Schwarzwald)?",
      "opties": ["In het zuidwesten van Duitsland (Baden-Württemberg).", "Aan de Noordzeekust in het noorden.", "Op de grens met Polen in het oosten.", "In het centrum van Berlijn."],
      "antwoord": 0,
      "uitleg": "Het Schwarzwald ligt in het zuidwesten van Duitsland in de deelstaat Baden-Württemberg."
    },
    {
      "type": "waaronwaar",
      "vraag": "De klinkercombinatie 'ie' in het Duits spreek je uit als een lange 'ie'-klank (zoals in 'Wiese').",
      "antwoord": True,
      "uitleg": "Waar! 'ie' is een lange ie-klank in het Duits, terwijl 'ei' als 'ai' klinkt."
    },
    {
      "type": "waaronwaar",
      "vraag": "De rivier de Donau stroomt naar het noorden en mondt uit in de Oostzee.",
      "antwoord": False,
      "uitleg": "Onwaar! De Donau stroomt naar het oosten en mondt uit in de Zwarte Zee."
    },
    {
      "type": "invoer",
      "vraag": "Wat is het Duitse woord voor 'maar' in een tegenstelling (bijv. 'Es regnet, ____ wir gehen spazieren')?",
      "antwoord": "aber",
      "uitleg": "'Maar' vertaal je in het Duits met het voegwoord 'aber'."
    },
    {
      "type": "invoer",
      "vraag": "Vertaal het signaalwoord 'omdat' naar het Duits: 'Wir bleiben zu Hause, ____ es stürmt.'",
      "antwoord": "weil",
      "uitleg": "'Omdat' vertaal je in het Duits met 'weil' (of 'denn' voor 'want')."
    }
  ]
}

# ==========================================
# 2. GESUNDHEIT & KÖRPER
# ==========================================
h2_1 = {
  "id": "dui-h2-1",
  "hoofdstuk": 2,
  "paragraaf": "2.1",
  "titel": "Wortschatz & Sprachmittel: Körper & Gesundheit",
  "korteUitleg": "Lichaamsdelen, ziektes, klachten omschrijven en een doktersbezoek in het Duits.",
  "icoon": "🩺",
  "kleur": "oranje",
  "theorie": """
    <h3>2.1 Wortschatz & Sprachmittel: Körper & Gesundheit</h3>
    <div class="info-box">
      <b>Kernbegrippen:</b> der Körper (het lichaam), der Kopf (het hoofd), das Auge / die Augen (het oog / de ogen), das Ohr / die Ohren (het oor / de oren), die Nase (de neus), der Mund (de mond), der Hals (de keel/hals), der Rücken (de rug), der Bauch (de buik), der Arm (de arm), die Hand (de hand), das Bein (het been), der Fuß (de voet), der Arzt / die Ärztin (de arts), die Praxis (de dokterspraktijk), das Krankenhaus (het ziekenhuis), die Apotheke (de apotheek), das Medikament (het medicijn).
    </div>
    <h4>1. Klachten en Pijn omschrijven (Schmerzen haben)</h4>
    <p>In het Duits kun je pijn op twee manieren uitdrukken:</p>
    <ul>
      <li><b>Met 'weh tun':</b> <i>Mein Kopf tut weh</i> (Mijn hoofd doet pijn) of in het meervoud: <i>Meine Beine tun weh</i> (Mijn benen doen pijn).</li>
      <li><b>Met 'Schmerzen haben':</b> <i>Ich habe Kopfschmerzen / Halsschmerzen / Bauchschmerzen / Rückenschmerzen.</i></li>
      <li><i>Ich habe Fieber / Husten / Schnupfen / die Grippe.</i> (Ik heb koorts / hoest / verkoudheid / de griep).</li>
    </ul>

    <h4>2. Beim Arzt & in der Apotheke (Bij de dokter en apotheek)</h4>
    <p>Handige zinnen en Sprachmittel:</p>
    <div class="formule-box">
      <b>Sprachmittel Beim Arzt:</b><br>
      • <i>Was fehlt Ihnen? / Was tut dir weh?</i> — Wat scheelt eraan? / Wat doet er pijn?<br>
      • <i>Seit wann haben Sie diese Beschwerden?</i> — Sinds wanneer heeft u deze klachten?<br>
      • <i>Ich fühle mich gar nicht wohl und mir ist schlecht.</i> — Ik voel me helemaal niet lekker en ik ben misselijk.<br>
      • <i>Sie müssen drei Tage im Bett bleiben und viel Tee trinken.</i> — U moet drie dagen in bed blijven en veel thee drinken.<br>
      • <i>Nehmen Sie diese Tabletten zweimal täglich nach dem Essen.</i> — Neem deze tabletten tweemaal per dag na het eten.
    </div>

    <h4>3. Beterschap wensen (Gute Besserung)</h4>
    <p>Als iemand ziek is, wens je diegene beterschap:</p>
    <ul>
      <li><b>Gute Besserung!</b> = Beterschap!</li>
      <li><b>Werd schnell wieder gesund!</b> = Word snel weer beter!</li>
    </ul>
  """,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat betekent de Duitse uitdrukking 'Gute Besserung!'?",
      "opties": ["Beterschap!", "Eet smakelijk!", "Gefeliciteerd!", "Goede reis!"],
      "antwoord": 0,
      "uitleg": "'Gute Besserung!' is de vaste Duitse wens voor beterschap."
    },
    {
      "type": "mc",
      "vraag": "Welke zin is grammaticaal correct als beide benen pijn doen?",
      "opties": ["Meine Beine tun weh.", "Mein Beine tut weh.", "Meine Beine macht Schmerz.", "Mein Bein tun weh."],
      "antwoord": 0,
      "uitleg": "'Beine' is meervoud, dus de persoonsvorm is meervoud: 'tun weh'."
    },
    {
      "type": "mc",
      "vraag": "Wat is het Duitse woord voor 'de dokterspraktijk'?",
      "opties": ["die Praxis", "das Krankenhaus", "die Apotheke", "das Rezept"],
      "antwoord": 0,
      "uitleg": "'Die Praxis' is de praktijk van de arts. 'Das Krankenhaus' is het ziekenhuis."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de klacht: 'Ich habe Schnupfen und Halsschmerzen'?",
      "opties": ["Ik ben verkouden en heb keelpijn.", "Ik heb koorts en buikpijn.", "Ik heb mijn been gebroken.", "Ik heb hoofdpijn en hoest."],
      "antwoord": 0,
      "uitleg": "'Schnupfen' is verkoudheid (loopneus) en 'Halsschmerzen' is keelpijn."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Duitse woord 'der Bauch' betekent 'de rug'.",
      "antwoord": False,
      "uitleg": "Onwaar! 'Der Bauch' betekent 'de buik'. De rug is 'der Rücken'."
    },
    {
      "type": "waaronwaar",
      "vraag": "In het Duits zeg je 'mir ist schlecht' als je wilt aangeven dat je misselijk bent.",
      "antwoord": True,
      "uitleg": "Waar! 'Mir ist schlecht' betekent 'ik ben misselijk / voel me niet goed'."
    },
    {
      "type": "invoer",
      "vraag": "Vertaal het lichaamsdeel naar het Duits: 'Mijn (hoofd) doet pijn.' → 'Mein ____ tut weh.'",
      "antwoord": "Kopf",
      "uitleg": "Het hoofd is in het Duits 'der Kopf'."
    },
    {
      "type": "invoer",
      "vraag": "Vertaal het woord tussen haakjes: 'Er hat 39 Grad (koorts).' → 'Er hat 39 Grad ____.'",
      "antwoord": "Fieber",
      "uitleg": "Koorts is in het Duits 'das Fieber'."
    }
  ]
}

h2_2 = {
  "id": "dui-h2-2",
  "hoofdstuk": 2,
  "paragraaf": "2.2",
  "titel": "Grammatik: Personalpronomen (1e, 3e & 4e naamval)",
  "korteUitleg": "Persoonlijke voornaamwoorden als onderwerp (Nominativ), lijdend voorwerp (Akkusativ) en meewerkend voorwerp (Dativ).",
  "icoon": "📝",
  "kleur": "oranje",
  "theorie": """
    <h3>2.2 Grammatik: Personalpronomen (1e, 3e & 4e naamval)</h3>
    <div class="info-box">
      <b>Grammaticafocus:</b> Persoonlijke voornaamwoorden in de 1e naamval (Nominativ - wie/wat onderwerp), 4e naamval (Akkusativ - wie/wat lijdend voorwerp) en 3e naamval (Dativ - aan wie meewerkend voorwerp).
    </div>
    <h4>1. Het Overzicht van de Persoonlijke Voornaamwoorden</h4>
    <div class="formule-box">
      <table style="width:100%;border-collapse:collapse;font-size:14px;">
        <tr style="border-bottom:2px solid #ccc;text-align:left;">
          <th>Persoon</th><th>1e naamval (Nom)</th><th>4e naamval (Akk)</th><th>3e naamval (Dat)</th><th>Betekenis (4e / 3e)</th>
        </tr>
        <tr><td>ik</td><td><b>ich</b></td><td><b>mich</b></td><td><b>mir</b></td><td>mij / aan mij</td></tr>
        <tr><td>jij</td><td><b>du</b></td><td><b>dich</b></td><td><b>dir</b></td><td>jou / aan jou</td></tr>
        <tr><td>hij</td><td><b>er</b></td><td><b>ihn</b></td><td><b>ihm</b></td><td>hem / aan hem</td></tr>
        <tr><td>zij (ev)</td><td><b>sie</b></td><td><b>sie</b></td><td><b>ihr</b></td><td>haar / aan haar</td></tr>
        <tr><td>het</td><td><b>es</b></td><td><b>es</b></td><td><b>ihm</b></td><td>het / aan het</td></tr>
        <tr><td>wij</td><td><b>wir</b></td><td><b>uns</b></td><td><b>uns</b></td><td>ons / aan ons</td></tr>
        <tr><td>jullie</td><td><b>ihr</b></td><td><b>euch</b></td><td><b>euch</b></td><td>jullie / aan jullie</td></tr>
        <tr><td>zij (mv)</td><td><b>sie</b></td><td><b>sie</b></td><td><b>ihnen</b></td><td>hen / aan hen</td></tr>
        <tr><td>u (beleefd)</td><td><b>Sie</b></td><td><b>Sie</b></td><td><b>Ihnen</b></td><td>u / aan u</td></tr>
      </table>
    </div>

    <h4>2. Hoe kies je de juiste naamval?</h4>
    <ul>
      <li><b>1e naamval (Nominativ):</b> Het onderwerp van de zin (wie doet het?). <i><u>Er</u> hilft mir.</i></li>
      <li><b>4e naamval (Akkusativ):</b> Het lijdend voorwerp (wie/wat ondergaat de actie?). <i>Der Arzt untersucht <u>ihn</u>.</i> (De arts onderzoekt hem.) / <i>Ich liebe <u>dich</u>.</i></li>
      <li><b>3e naamval (Dativ):</b> Het meewerkend voorwerp (aan wie / voor wie?). <i>Wie geht es <u>dir</u>?</i> (Hoe gaat het met jou / aan jou?) / <i>Der Arzt gibt <u>ihr</u> ein Rezept.</i> (De arts geeft haar een recept.)</li>
    </ul>

    <h4>3. Veelvoorkomende vaste combinaties met de 3e naamval (Dativ)</h4>
    <p>Sommige werkwoorden krijgen in het Duits altijd een meewerkend voorwerp (Dativ):</p>
    <ul>
      <li><i>helfen</i>: Kannst du <b>mir</b> helfen? (Kun je mij helpen?)</li>
      <li><i>danken</i>: Ich danke <b>Ihnen</b> sehr. (Ik dank u zeer.)</li>
      <li><i>gefallen</i>: Das Kleid gefällt <b>ihr</b> gut. (De jurk bevalt haar goed.)</li>
      <li><i>fehlen</i>: Was fehlt <b>Ihnen</b>? (Wat scheelt u?)</li>
    </ul>
  """,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Kies het juiste voornaamwoord (4e naamval): 'Ich sehe ____ (hem) jeden Tag in der Schule.'",
      "opties": ["ihn", "ihm", "er", "sie"],
      "antwoord": 0,
      "uitleg": "Lijdend voorwerp (wie zie ik?) van 'er' in de 4e naamval is 'ihn'."
    },
    {
      "type": "mc",
      "vraag": "Kies het juiste voornaamwoord (3e naamval): 'Wie geht es ____ (jou) heute?'",
      "opties": ["dir", "dich", "du", "dein"],
      "antwoord": 0,
      "uitleg": "Bij de vaste vraag 'Wie geht es...?' hoort de 3e naamval: 'dir'."
    },
    {
      "type": "mc",
      "vraag": "Wat is het voornaamwoord voor 'haar' (meewerkend voorwerp / aan haar / 3e naamval)?",
      "opties": ["ihr", "sie", "ihn", "ihnen"],
      "antwoord": 0,
      "uitleg": "De 3e naamval van 'sie' (zij enkelvoud) is 'ihr'."
    },
    {
      "type": "mc",
      "vraag": "Vul aan: 'Können Sie ____ (ons) bitte helfen?'",
      "opties": ["uns", "euch", "wir", "ihnen"],
      "antwoord": 0,
      "uitleg": "Zowel in de 3e als 4e naamval is de vorm voor 'wir' altijd 'uns'."
    },
    {
      "type": "waaronwaar",
      "vraag": "De vormen voor 'mich' (4e naamval) en 'mir' (3e naamval) betekenen allebei 'ik' als onderwerp van de zin.",
      "antwoord": False,
      "uitleg": "Onwaar! Als onderwerp gebruik je 'ich' (1e naamval). 'mich' is 4e naamval (lijdend vw) en 'mir' is 3e naamval (meewerkend vw)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Bij het beleefde 'u' schrijf je de voornaamwoorden Sie en Ihnen met een hoofdletter.",
      "antwoord": True,
      "uitleg": "Waar! De beleefdheidsvormen (Sie, Ihnen) worden in het Duits altijd met een hoofdletter geschreven."
    },
    {
      "type": "invoer",
      "vraag": "Vul het juiste voornaamwoord in (4e naamval van ich): 'Hörst du ____?' (Hoor je mij?)",
      "antwoord": "mich",
      "uitleg": "Het lijdend voorwerp (4e naamval) van 'ich' is 'mich'."
    },
    {
      "type": "invoer",
      "vraag": "Vul het juiste voornaamwoord in (3e naamval van du): 'Ich gebe ____ das Buch.' (Ik geef jou het boek.)",
      "antwoord": "dir",
      "uitleg": "Het meewerkend voorwerp (3e naamval) van 'du' is 'dir'."
    }
  ]
}

h2_3 = {
  "id": "dui-h2-3",
  "hoofdstuk": 2,
  "paragraaf": "2.3",
  "titel": "Aussprache, Lesen & Landeskunde: Zischlaute & Gesundheit",
  "korteUitleg": "Uitspraak van de s-/z-klanken (Zischlaute), sporten en het gezondheidssysteem in Duitsland.",
  "icoon": "🍎",
  "kleur": "oranje",
  "theorie": """
    <h3>2.3 Aussprache, Lesen & Landeskunde: Zischlaute & Gesundheit</h3>
    <div class="info-box">
      <b>Thema's:</b> Uitspraak van de Zischlaute (z, tz, s, ss, ß), Duitse zorg en leefgewoonten, en leesvaardigheid bij gezondheidsadviezen.
    </div>
    <h4>1. Aussprache: De Zischlaute (sis-klanken)</h4>
    <p>Let goed op de Duitse s- en z-klanken, want die verschillen van het Nederlands:</p>
    <ul>
      <li><b>De Duitse z (en tz):</b> Spreek je altijd uit als een scherpe <b>'ts'</b> (zoals in <i>Arzt</i> = arts, <i>Zimmer</i> = kamer, <i>Zahn</i> = tand, <i>Katze</i> = kat).</li>
      <li><b>De enkele s voor een klinker:</b> Spreek je uit als een stemhebbende zachte <b>'z'</b> (zoals in <i>Sonne</i>, <i>Sommer</i>, <i>Suppe</i>).</li>
      <li><b>De ss en ß (Eszett):</b> Spreek je uit als een scherpe stemloze <b>'s'</b> (zoals in <i>Fuß</i> = voet, <i>heißen</i> = heten, <i>Wasser</i> = water).</li>
    </ul>

    <h4>2. Landeskunde: Gezondheid en Zorg in Duitsland</h4>
    <div class="formule-box">
      <b>Het Duitse Gezondheidssysteem:</b><br>
      • <b>Die Apotheke:</b> Herkenbaar aan het grote rode gotische <b>A</b>-logo. Medicijnen (ook lichte pijnstillers zoals paracetamol of ibuprofen) koop je in Duitsland uitsluitend in de apotheek, niet in de supermarkt.<br>
      • <b>Die Krankenversicherung:</b> Iedereen in Duitsland is verplicht verzekerd via een <i>Krankenkasse</i>.<br>
      • <b>Notrufnummern:</b> <b>112</b> voor ambulance (Rettungsdienst) en brandweer (Feuerwehr); <b>110</b> voor politie (Polizei).<br>
      • <b>Die Kur:</b> Duitsland kent een lange traditie van kuuroorden (<i>Kurorte</i> of <i>Heilbäder</i>, herkenbaar aan de naam <i>Bad...</i> zoals Bad Kissingen, Baden-Baden) waar mensen herstellen in thermale bronnen.
    </div>

    <h4>3. Leesvaardigheid: Tips en Adviezen herkennen</h4>
    <p>In leesteksten over gezondheid kom je vaak gebiedende wijzen of modale werkwoorden tegen:</p>
    <ul>
      <li><i>Du solltest mehr schlafen</i> = Je zou meer moeten slapen.</li>
      <li><i>Trinken Sie mindestens zwei Liter Wasser</i> = Drink minimaal twee liter water.</li>
      <li><i>Vermeiden Sie Stress</i> = Vermijd stress.</li>
    </ul>
  """,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Hoe spreek je de letter 'z' in het Duitse woord 'Zahn' of 'Arzt' uit?",
      "opties": ["Als een scherpe 'ts'", "Als een zachte Nederlandse 'z'", "Als een zachte 's'", "Als een 'k'"],
      "antwoord": 0,
      "uitleg": "De Duitse 'z' wordt altijd uitgesproken als 'ts' (zoals in tsunamie of pizza)."
    },
    {
      "type": "mc",
      "vraag": "Waarom heten veel Duitse kuuroorden 'Bad ...' (zoals Bad Pyrmont of Baden-Baden)?",
      "opties": ["Omdat 'Bad' verwijst naar historische thermale bronnen en kuurbaden.", "Omdat het slechte plekken waren in de geschiedenis.", "Omdat het grensplaatsen zijn.", "Omdat het bergtoppen zijn in de Alpen."],
      "antwoord": 0,
      "uitleg": "'Bad' is een eretitel voor erkende kuuroorden met geneeskrachtige minerale bronnen."
    },
    {
      "type": "mc",
      "vraag": "Waar koop je in Duitsland lichte pijnstillers zoals paracetamol of neusspray?",
      "opties": ["Uitsluitend in de Apotheke (met het rode A-logo).", "Bij het tankstation of in de supermarkt.", "Bij de bakkerij.", "Alleen in het ziekenhuis."],
      "antwoord": 0,
      "uitleg": "In Duitsland geldt de apotheekplicht (Apothekenpflicht): geneesmiddelen koop je uitsluitend bij de apotheek."
    },
    {
      "type": "mc",
      "vraag": "Wat is het alarmnummer voor een ambulance (Rettungsdienst) in Duitsland?",
      "opties": ["112", "110", "911", "100"],
      "antwoord": 0,
      "uitleg": "Het alarmnummer voor ambulance en brandweer is 112 (politie is 110)."
    },
    {
      "type": "waaronwaar",
      "vraag": "De letter 'ß' (Eszett) in woorden als 'Fuß' en 'groß' spreek je uit als een scherpe 's'-klank.",
      "antwoord": True,
      "uitleg": "Waar! De ß staat voor een scherpe stemloze s-klank na een lange klinker of tweeklank."
    },
    {
      "type": "waaronwaar",
      "vraag": "In Duitsland bel je 110 voor de brandweer.",
      "antwoord": False,
      "uitleg": "Onwaar! 110 is voor de politie. Brandweer en ambulance bel je met 112."
    },
    {
      "type": "invoer",
      "vraag": "Wat is het Duitse alarmnummer voor de politie?",
      "antwoord": "110",
      "uitleg": "Het politienummer in Duitsland is 110."
    },
    {
      "type": "invoer",
      "vraag": "Wat is het Duitse woord voor de apotheek?",
      "antwoord": "Apotheke",
      "uitleg": "De apotheek is in het Duits 'die Apotheke'."
    }
  ]
}

# Write H1 and H2
write_onderwerp("h1_1.js", h1_1)
write_onderwerp("h1_2.js", h1_2)
write_onderwerp("h1_3.js", h1_3)
write_onderwerp("h2_1.js", h2_1)
write_onderwerp("h2_2.js", h2_2)
write_onderwerp("h2_3.js", h2_3)

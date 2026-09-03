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

# H1.1, H1.2, H1.3
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

# H2.1, H2.2, H2.3
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

# H3.1, H3.2, H3.3
h3_1 = {
  "id": "dui-h3-1",
  "hoofdstuk": 3,
  "paragraaf": "3.1",
  "titel": "Wortschatz & Sprachmittel: Unterwegs, Verkehr & Wegbeschreibung",
  "korteUitleg": "Woordenschat over vervoer, het station, het vliegveld en de weg vragen en wijzen in een Duitse stad.",
  "icoon": "🚆",
  "kleur": "groen",
  "theorie": """
    <h3>3.1 Wortschatz & Sprachmittel: Unterwegs, Verkehr & Wegbeschreibung</h3>
    <div class="info-box">
      <b>Kernbegrippen:</b> der Bahnhof (het treinstation), der Hauptbahnhof / Hbf (het centraal station), der Zug (de trein), das Gleis (het spoor), die Fahrkarte / das Ticket (het kaartje), die Abfahrt (het vertrek), die Ankunft (de aankomst), die Verspätung (de vertraging), das Flugzeug (het vliegtuig), der Flughafen (het vliegveld), der Bus (de bus), die Straßenbahn / Tram (de tram), das Fahrrad (de fiets), das Auto (de auto), die Ampel (het stoplicht), die Kreuzung (de kruising), die Brücke (de brug).
    </div>
    <h4>1. Am Bahnhof (Op het station)</h4>
    <p>Belangrijke termen bij reizen met de trein (Deutsche Bahn / DB):</p>
    <ul>
      <li><i>Auf Gleis 4 fährt der ICE nach Frankfurt ein.</i> — Op spoor 4 komt de ICE naar Frankfurt binnen.</li>
      <li><i>Der Zug hat 15 Minuten Verspätung.</i> — De trein heeft 15 minuten vertraging.</li>
      <li><i>Einfach oder hin und zurück?</i> — Enkele reis of retour?</li>
      <li><i>Muss ich umsteigen?</i> — Moet ik overstappen?</li>
    </ul>

    <h4>2. Nach dem Weg fragen und den Weg beschreiben (Wegwijzen)</h4>
    <p>De belangrijkste richtingen en aanwijzingen in het Duits:</p>
    <div class="formule-box">
      <b>Wegbeschrijving:</b><br>
      • <i>Entschuldigung, wie komme ich zum Bahnhof?</i> — Pardon, hoe kom ik bij het station?<br>
      • <b>geradeaus</b> = rechtdoor (<i>Gehen Sie immer geradeaus.</i>)<br>
      • <b>nach links</b> = naar links (<i>Biegen Sie links ab.</i>)<br>
      • <b>nach rechts</b> = naar rechts (<i>Biegen Sie rechts ab.</i>)<br>
      • <i>an der Ampel</i> = bij het stoplicht | <i>an der Kreuzung</i> = bij de kruising<br>
      • <i>die erste / zweite Straße rechts</i> = de eerste / tweede straat rechts<br>
      • <i>über die Brücke</i> = over de brug
    </div>

    <h4>3. Prepositionele uitdrukkingen: mit + Dativ</h4>
    <p>Als je reist 'met' een vervoermiddel, gebruik je <b>mit</b> altijd met de 3e naamval (Dativ):</p>
    <ul>
      <li><b>mit dem</b> Zug / Bus / Auto / Fahrrad / Flugzeug (mannelijk & onzijdig)</li>
      <li><b>mit der</b> U-Bahn / Straßenbahn / Bahn (vrouwelijk)</li>
      <li><i>zu Fuß</i> = te voet</li>
    </ul>
  """,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat betekent de aanwijzing: 'Biegen Sie an der zweiten Kreuzung nach links ab'?",
      "opties": ["Sla bij de tweede kruising linksaf.", "Ga bij het tweede stoplicht rechtdoor.", "Sla bij de eerste brug rechtsaf.", "Neem de tweede straat aan de rechterkant."],
      "antwoord": 0,
      "uitleg": "'Kreuzung' is kruising en 'nach links abbiegen' is linksaf slaan."
    },
    {
      "type": "mc",
      "vraag": "Wat is het Duitse woord voor 'het treinspoor' (bijv. spoor 3)?",
      "opties": ["das Gleis", "der Bahnsteig", "der Zug", "die Schiene"],
      "antwoord": 0,
      "uitleg": "'Das Gleis' betekent het spoor (bijv. 'auf Gleis 3')."
    },
    {
      "type": "mc",
      "vraag": "Hoe vertaal je: 'Ik reis met de trein' in correct Duits?",
      "opties": ["Ich fahre mit dem Zug.", "Ich fahre mit den Zug.", "Ich reise mit das Zug.", "Ich fahre bei dem Zug."],
      "antwoord": 0,
      "uitleg": "'mit' krijgt altijd de 3e naamval (Dativ): 'mit dem Zug' (der Zug → dem Zug)."
    },
    {
      "type": "mc",
      "vraag": "Wat vraag je als je wilt weten of je moet overstappen?",
      "opties": ["Muss ich umsteigen?", "Muss ich aussteigen?", "Muss ich einsteigen?", "Wann fährt der Zug ab?"],
      "antwoord": 0,
      "uitleg": "'Umsteigen' betekent overstappen. ('Einsteigen' = instappen, 'aussteigen' = uitstappen)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Duitse woord 'die Verspätung' betekent 'de vroege aankomst'.",
      "antwoord": False,
      "uitleg": "Onwaar! 'Die Verspätung' betekent de vertraging."
    },
    {
      "type": "waaronwaar",
      "vraag": "De afkorting 'Hbf' op borden in Duitse steden staat voor 'Hauptbahnhof' (Centraal Station).",
      "antwoord": True,
      "uitleg": "Waar! Hbf staat altijd voor Hauptbahnhof."
    },
    {
      "type": "invoer",
      "vraag": "Wat is het Duitse woord voor 'rechtdoor'?",
      "antwoord": "geradeaus",
      "uitleg": "'Rechtdoor' vertaal je in het Duits met 'geradeaus'."
    },
    {
      "type": "invoer",
      "vraag": "Vertaal het woord tussen haakjes: 'Entschuldigung, wo ist die (halte) für die Straßenbahn?'",
      "antwoord": "Haltestelle",
      "uitleg": "Een halte voor bus of tram is in het Duits 'die Haltestelle'."
    }
  ]
}

h3_2 = {
  "id": "dui-h3-2",
  "hoofdstuk": 3,
  "paragraaf": "3.2",
  "titel": "Grammatik: Modalverben im Präteritum (können, müssen, dürfen, wollen, wissen)",
  "korteUitleg": "De verleden tijd van modale hulpwerkwoorden in het Duits: konnte, musste, durfte, wollte en wusste.",
  "icoon": "📖",
  "kleur": "groen",
  "theorie": """
    <h3>3.2 Grammatik: Modalverben im Präteritum</h3>
    <div class="info-box">
      <b>Grammaticafocus:</b> De verleden tijd (Präteritum) van de modale hulpwerkwoorden <i>können</i> (kunnen), <i>müssen</i> (moeten), <i>dürfen</i> (mogen), <i>wollen</i> (willen) en het onregelmatige werkwoord <i>wissen</i> (weten).
    </div>
    <h4>1. De Regel voor Modale Werkwoorden in de Verleden Tijd</h4>
    <p>In de verleden tijd verliezen modale werkwoorden altijd hun <b>Umlaut</b> (ö → o, ü → u). Bovendien zijn ook hier de vormen voor <code>ich</code> en <code>er/sie/es</code> altijd <b>gelijk en zonder uitgang (-te)</b>!</p>
    <div class="formule-box">
      <b>Overzicht Präteritum van Modalverben:</b><br>
      • <b>können</b> (kon/konden): ich <i>konnte</i>, du <i>konntest</i>, er <i>konnte</i>, wir <i>konnten</i>, ihr <i>konntet</i>, sie <i>konnten</i><br>
      • <b>müssen</b> (moest/moesten): ich <i>musste</i>, du <i>musstest</i>, er <i>musste</i>, wir <i>mussten</i>, ihr <i>musstet</i>, sie <i>mussten</i><br>
      • <b>dürfen</b> (mocht/mochten): ich <i>durfte</i>, du <i>durftest</i>, er <i>durfte</i>, wir <i>durften</i>, ihr <i>durftet</i>, sie <i>durften</i><br>
      • <b>wollen</b> (wilde/wilden): ich <i>wollte</i>, du <i>wolltest</i>, er <i>wollte</i>, wir <i>wollten</i>, ihr <i>wolltet</i>, sie <i>wollten</i><br>
      • <b>wissen</b> (wist/wisten): ich <i>wusste</i>, du <i>wusstest</i>, er <i>wusste</i>, wir <i>wussten</i>, ihr <i>wusstet</i>, sie <i>wussten</i>
    </div>

    <h4>2. Betekenis en Toepassing</h4>
    <ul>
      <li><i>Ich <b>musste</b> gestern lange auf den Bus warten.</i> (Ik moest gisteren lang op de bus wachten.)</li>
      <li><i>Wir <b>konnten</b> die Fahrkarte nicht finden.</i> (We konden het treinkaartje niet vinden.)</li>
      <li><i>Er <b>durfte</b> nicht mit dem Auto fahren.</i> (Hij mocht niet met de auto rijden.)</li>
      <li><i>Ich <b>wusste</b> nicht, wo der Bahnhof war.</i> (Ik wist niet waar het station was.)</li>
    </ul>

    <h4>3. Zinsvolgorde met Modale Hulpwerkwoorden</h4>
    <p>Het modale hulpwerkwoord staat op de 2e plek in de zin en de andere werkwoordsvorm (het hele werkwoord/infinitief) staat <b>helemaal achteraan</b> in de zin:</p>
    <p><i>Wir <b>wollten</b> gestern nach München <b>fahren</b>.</i></p>
  """,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm: 'Gestern ____ (kon) ich leider nicht kommen.'",
      "opties": ["konnte", "könnte", "kann", "konntest"],
      "antwoord": 0,
      "uitleg": "De verleden tijd van können bij 'ich' is 'konnte' (zonder Umlaut)."
    },
    {
      "type": "mc",
      "vraag": "Wat is de verleden tijd van 'dürfen' bij 'wir'?",
      "opties": ["wir durften", "wir dürften", "wir darfen", "wir durftet"],
      "antwoord": 0,
      "uitleg": "De verleden tijd bij 'wir' is 'durften' (zonder Umlaut)."
    },
    {
      "type": "mc",
      "vraag": "Vul aan: 'Warum ____ (moest) du so früh aufstehen?'",
      "opties": ["musstest", "müsstest", "musste", "musst"],
      "antwoord": 0,
      "uitleg": "Bij 'du' hoort de uitgang '-test': 'musstest'."
    },
    {
      "type": "mc",
      "vraag": "Welke vorm van 'wissen' in de verleden tijd past in: 'Er ____ die Antwort nicht.'?",
      "opties": ["wusste", "wusstet", "wies", "weisste"],
      "antwoord": 0,
      "uitleg": "De verleden tijd van wissen bij 'er' is 'wusste'."
    },
    {
      "type": "waaronwaar",
      "vraag": "In de verleden tijd houden modale werkwoorden hun Umlaut (bijv. ich könte, er müste).",
      "antwoord": False,
      "uitleg": "Onwaar! In het Präteritum verliezen modale werkwoorden altijd hun Umlaut (konnte, musste, durfte)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Bij modale werkwoorden staat het tweede werkwoord (het hele werkwoord) achteraan in de hoofdzin.",
      "antwoord": True,
      "uitleg": "Waar! Het infinitief staat aan het einde van de zin (bijv. 'Er wollte nach Hause gehen')."
    },
    {
      "type": "invoer",
      "vraag": "Vul de juiste vorm van 'wollen' in de verleden tijd in: 'Wir ____ gestern ins Kino gehen.'",
      "antwoord": "wollten",
      "uitleg": "De verleden tijd van wollen bij 'wir' is 'wollten'."
    },
    {
      "type": "invoer",
      "vraag": "Vul de juiste vorm van 'müssen' in de verleden tijd in: 'Sie (zij enkelvoud) ____ zum Arzt gehen.'",
      "antwoord": "musste",
      "uitleg": "De verleden tijd van müssen bij 'sie' (3e pers ev) is 'musste'."
    }
  ]
}

h3_3 = {
  "id": "dui-h3-3",
  "hoofdstuk": 3,
  "paragraaf": "3.3",
  "titel": "Aussprache, Lesen & Landeskunde: Klanken & Reizen in DACH",
  "korteUitleg": "Uitspraak van sch-, sp- en st-klanken en Landeskunde over reizen en openbaar vervoer in Duitsland, Oostenrijk en Zwitserland (DACH).",
  "icoon": "🗺️",
  "kleur": "groen",
  "theorie": """
    <h3>3.3 Aussprache, Lesen & Landeskunde: Klanken & Reizen in DACH</h3>
    <div class="info-box">
      <b>Thema's:</b> De uitspraak van de medeklinkercombinaties <i>sch</i>, <i>sp</i> en <i>st</i>, en Landeskunde over de D-A-CH landen (Duitsland, Oostenrijk, Zwitserland).
    </div>
    <h4>1. Aussprache: sch, sp en st</h4>
    <p>In het Duits worden <i>sp</i> en <i>st</i> aan het begin van een woord of lettergreep uitgesproken als <b>'sjp'</b> en <b>'sjt'</b>:</p>
    <ul>
      <li><b>sch</b>: klinkt als de Nederlandse 'sj' (in <i>Schule</i>, <i>Schnee</i>, <i>schön</i>).</li>
      <li><b>sp</b> aan het begin: spreek je uit als <b>'sjp'</b> (in <i>Sport</i> = 'sjport', <i>spät</i> = 'sjpèèt', <i>spielen</i> = 'sjpiielen').</li>
      <li><b>st</b> aan het begin: spreek je uit als <b>'sjt'</b> (in <i>Stadt</i> = 'sjadt', <i>Straße</i> = 'sjtraasse', <i>stehen</i> = 'sjtee-en').</li>
    </ul>

    <h4>2. Landeskunde: Die DACH-Länder</h4>
    <p>De D-A-CH landen zijn de drie Duitstalige landen in het hart van Europa:</p>
    <div class="formule-box">
      <b>Die drei DACH-Länder:</b><br>
      • <b>D (Deutschland):</b> Hoofdstad Berlijn, 84 miljoen inwoners, hogesnelheidstrein: <i>ICE (Intercity Express)</i>.<br>
      • <b>A (Österreich):</b> Hoofdstad Wenen (Wien), de Alpen, beroemde spoorlijn <i>Semmeringbahn</i>, spoorwegmaatschappij: <i>ÖBB</i>.<br>
      • <b>CH (Die Schweiz / Confoederatio Helvetica):</b> Hoofdstad Bern, 4 officiële landstalen (Duits, Frans, Italiaans, Retoromaans), beroemde bergtreinen zoals de <i>Glacier Express</i>, spoorwegmaatschappij: <i>SBB</i>.
    </div>

    <h4>3. Leesvaardigheid: Reisteksten en Dienstregelingen (Fahrplan)</h4>
    <p>Bij het lezen van reisbrochures en treintabellen let je op:</p>
    <ul>
      <li><i>Abfahrt (Abf.)</i> = Vertrektijd | <i>Ankunft (Ank.)</i> = Aankomsttijd</li>
      <li><i>Gleis / Bahnsteig</i> = Spoor / Perron</li>
      <li><i>werktags</i> = op werkdagen (ma-vr) | <i>täglich</i> = dagelijks</li>
      <li><i>Sitzplatzreservierung</i> = Stoelreservering</li>
    </ul>
  """,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Hoe spreek je het Duitse woord 'Sport' of 'Stadt' correct uit?",
      "opties": ["Als 'Sjport' en 'Sjtadt'", "Als een gewone Nederlandse 's'", "Als 'Kport' en 'Ktadt'", "Als 'Zport' en 'Ztadt'"],
      "antwoord": 0,
      "uitleg": "In het Duits worden 'sp' en 'st' aan het begin van een woord uitgesproken als 'sjp' en 'sjt'."
    },
    {
      "type": "mc",
      "vraag": "Waar staat de afkorting 'DACH' voor?",
      "opties": ["Deutschland, Austria (Österreich), Confoederatio Helvetica (Schweiz)", "Dänemark, Amerika, China, Holland", "Duitsland, Alpen, Centraal Europa, Hamburg", "Dortmund, Aachen, Chemnitz, Hannover"],
      "antwoord": 0,
      "uitleg": "DACH staat voor de kentekencodes van Duitsland (D), Oostenrijk (A) en Zwitserland (CH)."
    },
    {
      "type": "mc",
      "vraag": "Wat is de hoofdstad van Zwitserland (die Schweiz)?",
      "opties": ["Bern", "Zürich", "Genève", "Wenen"],
      "antwoord": 0,
      "uitleg": "Bern is de bondsstad en regeringszetel (hoofdstad) van Zwitserland."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de term 'werktags' op een Duits treinschema?",
      "opties": ["Op werkdagen van maandag tot en met zaterdag.", "Alleen op feestdagen.", "Alleen op zondag.", "De hele nacht."],
      "antwoord": 0,
      "uitleg": "'Werktags' betekent op werkdagen (in Duitsland ma t/m za)."
    },
    {
      "type": "waaronwaar",
      "vraag": "De ICE (Intercity Express) is de bekende Duitse hogesnelheidstrein van de Deutsche Bahn.",
      "antwoord": True,
      "uitleg": "Waar! De ICE is het vlaggenschip van de Duitse spoorwegen."
    },
    {
      "type": "waaronwaar",
      "vraag": "In Zwitserland spreekt de hele bevolking uitsluitend Duits.",
      "antwoord": False,
      "uitleg": "Onwaar! Zwitserland heeft 4 officiële talen: Duits, Frans, Italiaans en Retoromaans."
    },
    {
      "type": "invoer",
      "vraag": "Wat is de Duitse term voor 'aankomst' op een reisinformatiebord?",
      "antwoord": "Ankunft",
      "uitleg": "Aankomst is 'die Ankunft' (afgekort als Ank.)."
    },
    {
      "type": "invoer",
      "vraag": "Wat is de hoofdstad van Oostenrijk (Österreich)?",
      "antwoord": "Wien",
      "uitleg": "De hoofdstad van Oostenrijk is Wenen, in het Duits 'Wien'."
    }
  ]
}

# H4.1, H4.2, H4.3
h4_1 = {
  "id": "dui-h4-1",
  "hoofdstuk": 4,
  "paragraaf": "4.1",
  "titel": "Wortschatz & Sprachmittel: Veranstaltungen, Feste & Termine",
  "korteUitleg": "Evenementen, feesten, feestdagen, iemand uitnodigen en afspraken maken in het Duits.",
  "icoon": "🎪",
  "kleur": "paars",
  "theorie": """
    <h3>4.1 Wortschatz & Sprachmittel: Veranstaltungen, Feste & Termine</h3>
    <div class="info-box">
      <b>Kernbegrippen:</b> die Veranstaltung (het evenement), das Fest / die Feier (het feest), die Geburtstagsparty (het verjaardagsfeest), das Konzert (het concert), das Festival (het festival), die Einladung (de uitnodiging), der Termin (de afspraak), die Uhrzeit (de tijd/kloktijd), stattfinden (plaatsvinden), einladen (uitnodigen), feiern (vieren), sich treffen (elkaar ontmoeten), absagen (afzeggen), zusagen (bevestigen).
    </div>
    <h4>1. Sprachmittel: Iemand uitnodigen en reageren</h4>
    <p>Vaste bouwstenen om iemand uit te nodigen voor een feest of uitstapje:</p>
    <ul>
      <li><i>Hast du Lust, am Samstag mitzukommen?</i> — Heb je zin om zaterdag mee te gaan?</li>
      <li><i>Ich lade dich herzlich zu meiner Geburtstagsparty ein.</i> — Ik nodig je van harte uit voor mijn verjaardagsfeest.</li>
      <li><i>Ja, gerne! Das klingt toll!</i> — Ja, graag! Dat klinkt geweldig!</li>
      <li><i>Es tut mir leid, aber ich habe leider keine Zeit.</i> — Het spijt me, maar ik heb helaas geen tijd.</li>
      <li><i>Schade, da kann ich leider nicht.</i> — Jammer, dan kan ik helaas niet.</li>
    </ul>

    <h4>2. Tijdstippen en Afspraken maken (Termine vereinbaren)</h4>
    <div class="formule-box">
      <b>Vragen naar tijd en data:</b><br>
      • <i>Wann fängt das Konzert an?</i> — Wanneer begint het concert?<br>
      • <i>Um wie viel Uhr treffen wir uns?</i> — Hoe laat ontmoeten we elkaar?<br>
      • <i>Wir treffen uns <b>um</b> 19:30 Uhr <b>vor dem</b> Kino.</i> — We ontmoeten elkaar om 19:30 uur voor de bioscoop.<br>
      • <i>Das Festival findet <b>vom</b> 10. <b>bis zum</b> 12. Juli statt.</i> — Het festival vindt plaats van 10 tot 12 juli.<br>
      • <i>Passt es dir am Freitag?</i> — Schikt het jou op vrijdag?
    </div>

    <h4>3. Bekende Duitse Feestdagen (Traditionen)</h4>
    <ul>
      <li><b>Weihnachten (24.-26. Dezember)</b> = Kerstmis (met de traditionele <i>Weihnachtsmärkte</i>)</li>
      <li><b>Silvester (31. Dezember)</b> = Oudjaarsavond</li>
      <li><b>Ostern</b> = Pasen</li>
      <li><b>Karneval / Fasching</b> = Carnaval (vooral uitbundig gevierd in Keulen / Köln en het Rijnland)</li>
      <li><b>Oktoberfest</b> = Het wereldberoemde volksfeest in München (Beieren)</li>
    </ul>
  """,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat betekent de zin: 'Das Festival findet am Wochenende statt'?",
      "opties": ["Het festival vindt plaats in het weekend.", "Het festival wordt afgelast.", "Het festival duurt een hele week.", "Het feest begint pas volgende maand."],
      "antwoord": 0,
      "uitleg": "'Stattfinden' betekent plaatsvinden. 'Am Wochenende' is in het weekend."
    },
    {
      "type": "mc",
      "vraag": "Hoe reageer je beleefd als je niet naar een uitnodiging kunt komen?",
      "opties": ["Es tut mir leid, aber ich habe leider keine Zeit.", "Ja gerne, ich komme sofort vorbei!", "Das ist mir ganz egal.", "Ich will auf jeden Fall mitkommen."],
      "antwoord": 0,
      "uitleg": "'Es tut mir leid, aber ich habe leider keine Zeit' is de beleefde afwijzing."
    },
    {
      "type": "mc",
      "vraag": "In welke Duitse stad vindt het beroemde Oktoberfest plaats?",
      "opties": ["München", "Berlin", "Hamburg", "Köln"],
      "antwoord": 0,
      "uitleg": "Het Oktoberfest wordt gevierd op de Theresienwiese in München (Beieren)."
    },
    {
      "type": "mc",
      "vraag": "Wat is het juiste voorzetsel bij kloktijden (bijv. '... acht uur')?",
      "opties": ["um acht Uhr", "am acht Uhr", "im acht Uhr", "zu acht Uhr"],
      "antwoord": 0,
      "uitleg": "Bij kloktijden gebruik je in het Duits altijd 'um' (um acht Uhr = om acht uur)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Duitse woord 'die Einladung' betekent 'de afwijzing'.",
      "antwoord": False,
      "uitleg": "Onwaar! 'Die Einladung' betekent 'de uitnodiging' (van het werkwoord einladen)."
    },
    {
      "type": "waaronwaar",
      "vraag": "In het Duits zeg je 'Silvester' voor Oudjaarsavond (31 december).",
      "antwoord": True,
      "uitleg": "Waar! Oudejaarsavond heet in Duitstalige landen Silvester."
    },
    {
      "type": "invoer",
      "vraag": "Wat is het Duitse woord voor 'afspraak' (bij de dokter of vrienden)?",
      "antwoord": "Termin",
      "uitleg": "Een afspraak is in het Duits 'der Termin'."
    },
    {
      "type": "invoer",
      "vraag": "Vul het juiste voorzetsel in voor dagen van de week: 'Wir treffen uns ____ Samstag.'",
      "antwoord": "am",
      "uitleg": "Bij dagen van de week gebruik je 'am' (am Samstag, am Montag)."
    }
  ]
}

h4_2 = {
  "id": "dui-h4-2",
  "hoofdstuk": 4,
  "paragraaf": "4.2",
  "titel": "Grammatik: Die der-Gruppe & ein-Gruppe (1e & 4e naamval)",
  "korteUitleg": "Bepaalde en onbepaalde lidwoorden in de 1e naamval (Nominativ) en 4e naamval (Akkusativ).",
  "icoon": "📖",
  "kleur": "paars",
  "theorie": """
    <h3>4.2 Grammatik: Die der-Gruppe & ein-Gruppe (1e & 4e naamval)</h3>
    <div class="info-box">
      <b>Grammaticafocus:</b> De lidwoorden en bezittelijke voornaamwoorden in de 1e naamval (onderwerp) en 4e naamval (lijdend voorwerp). De gouden regel: <b>alleen mannelijk verandert in de 4e naamval!</b>
    </div>
    <h4>1. De der-Gruppe (Bepaalde Lidwoorden & dieser/jeder/welcher)</h4>
    <p>In de 4e naamval (Akkusativ) verandert <b>alleen de mannelijke vorm</b> van <i>der</i> naar <b>den</b>. Vrouwelijk, onzijdig en meervoud blijven hetzelfde!</p>
    <div class="formule-box">
      <table style="width:100%;border-collapse:collapse;font-size:14px;">
        <tr style="border-bottom:2px solid #ccc;text-align:left;">
          <th>Geslacht</th><th>1e naamval (Nominativ)</th><th>4e naamval (Akkusativ)</th><th>Voorbeeld (4e naamval)</th>
        </tr>
        <tr><td>Mannelijk</td><td><b>der</b> / dieser</td><td><b>den</b> / diesen</td><td>Ich kaufe <b>den</b> Rock.</td></tr>
        <tr><td>Vrouwelijk</td><td><b>die</b> / diese</td><td><b>die</b> / diese</td><td>Ich besuche <b>die</b> Party.</td></tr>
        <tr><td>Onzijdig</td><td><b>das</b> / dieses</td><td><b>das</b> / dieses</td><td>Wir sehen <b>das</b> Konzert.</td></tr>
        <tr><td>Meervoud</td><td><b>die</b> / diese</td><td><b>die</b> / diese</td><td>Er kennt <b>die</b> Musiker.</td></tr>
      </table>
    </div>

    <h4>2. De ein-Gruppe (Onbepaalde Lidwoorden & kein/mein/dein/sein/ihr/unser/euer/ihr)</h4>
    <p>Ook bij de ein-groep verandert in de 4e naamval <b>alleen het mannelijke woord</b> naar <b>einen / meinen / keinen</b>:</p>
    <div class="formule-box">
      <table style="width:100%;border-collapse:collapse;font-size:14px;">
        <tr style="border-bottom:2px solid #ccc;text-align:left;">
          <th>Geslacht</th><th>1e naamval (Nominativ)</th><th>4e naamval (Akkusativ)</th><th>Voorbeeld (4e naamval)</th>
        </tr>
        <tr><td>Mannelijk</td><td><b>ein</b> / mein / kein</td><td><b>einen</b> / meinen / keinen</td><td>Ich habe <b>einen</b> Bruder.</td></tr>
        <tr><td>Vrouwelijk</td><td><b>eine</b> / meine / keine</td><td><b>eine</b> / meine / keine</td><td>Sie sucht <b>eine</b> Tasche.</td></tr>
        <tr><td>Onzijdig</td><td><b>ein</b> / mein / kein</td><td><b>ein</b> / mein / kein</td><td>Er kauft <b>ein</b> Ticket.</td></tr>
        <tr><td>Meervoud</td><td><b>-</b> / meine / keine</td><td><b>-</b> / meine / keine</td><td>Wir haben <b>keine</b> Tickets.</td></tr>
      </table>
    </div>

    <h4>3. Handige ezelsbrug voor toetsen</h4>
    <p>Stel jezelf altijd twee vragen:</p>
    <ol>
      <li>Wat is het geslacht van het zelfstandig naamwoord? (der, die of das?)</li>
      <li>Is het onderwerp (wie doet het? → 1e naamval) of lijdend voorwerp (wie/wat ondergaat het? → 4e naamval)?</li>
    </ol>
  """,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Kies het juiste lidwoord (4e naamval mannelijk): 'Ich habe ____ (der Schlüssel) verloren.'",
      "opties": ["den", "der", "das", "die"],
      "antwoord": 0,
      "uitleg": "Schlüssel is mannelijk (der). Als lijdend voorwerp verandert 'der' in 'den'."
    },
    {
      "type": "mc",
      "vraag": "Vul aan (4e naamval mannelijk): 'Lukas sucht ____ (zijn hond - der Hund).'",
      "opties": ["seinen Hund", "sein Hund", "seinem Hund", "seiner Hund"],
      "antwoord": 0,
      "uitleg": "Hund is mannelijk (der Hund), dus in de 4e naamval krijgt het bezittelijk voornaamwoord de uitgang -en: 'seinen Hund'."
    },
    {
      "type": "mc",
      "vraag": "Welk lidwoord verandert er in de 4e naamval (Akkusativ) ten opzichte van de 1e naamval?",
      "opties": ["Alleen het mannelijke lidwoord (der → den / ein → einen).", "Alleen het vrouwelijke lidwoord.", "Alleen het onzijdige lidwoord.", "Alle lidwoorden veranderen."],
      "antwoord": 0,
      "uitleg": "In de 4e naamval verandert uitsluitend het mannelijk geslacht (der → den, ein → einen). Vrouwelijk, onzijdig en meervoud blijven gelijk."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm: 'Wir haben ____ (geen tijd - die Zeit).'",
      "opties": ["keine Zeit", "keinen Zeit", "kein Zeit", "keinem Zeit"],
      "antwoord": 0,
      "uitleg": "'Zeit' is vrouwelijk (die Zeit), dus zowel in de 1e als 4e naamval is het 'keine Zeit'."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het onzijdige lidwoord 'das' verandert in de 4e naamval naar 'den'.",
      "antwoord": False,
      "uitleg": "Onwaar! Onzijdig blijft altijd 'das' (ein / mein) in de 4e naamval. Alleen mannelijk verandert naar 'den'."
    },
    {
      "type": "waaronwaar",
      "vraag": "In de zin 'Der Junge sieht einen Film' staat 'der Junge' in de 1e naamval en 'einen Film' in de 4e naamval.",
      "antwoord": True,
      "uitleg": "Waar! 'Der Junge' is het onderwerp (1e nv) en 'einen Film' is het lijdend voorwerp (4e nv)."
    },
    {
      "type": "invoer",
      "vraag": "Vul het juiste lidwoord in (4e naamval van der Kuchen): 'Er isst ____ Kuchen.'",
      "antwoord": "den",
      "uitleg": "Kuchen is mannelijk (der Kuchen). Lijdend voorwerp = 'den Kuchen'."
    },
    {
      "type": "invoer",
      "vraag": "Vul de juiste vorm van 'ein' in (4e naamval van der Apfel): 'Ich möchte ____ Apfel essen.'",
      "antwoord": "einen",
      "uitleg": "Apfel is mannelijk (der Apfel). In de 4e naamval wordt dit 'einen Apfel'."
    }
  ]
}

h4_3 = {
  "id": "dui-h4-3",
  "hoofdstuk": 4,
  "paragraaf": "4.3",
  "titel": "Aussprache, Lesen & Landeskunde: Klanken & Feste",
  "korteUitleg": "De Ich-klank vs. Ach-klank en -chs, en Landeskunde over beroemde Duitse evenementen en feesttradities.",
  "icoon": "🎭",
  "kleur": "paars",
  "theorie": """
    <h3>4.3 Aussprache, Lesen & Landeskunde: Klanken & Feste</h3>
    <div class="info-box">
      <b>Thema's:</b> De uitspraak van de <i>ch</i> (Ich-Laut en Ach-Laut) en <i>-chs</i>, plus culturele feesten in Duitsland.
    </div>
    <h4>1. Aussprache: Ich-Laut vs. Ach-Laut</h4>
    <p>In het Duits heeft de lettercombinatie <b>ch</b> twee verschillende klanken:</p>
    <ul>
      <li><b>De 'Ich-Laut' (zachte ch):</b> Na de klinkers <i>e, i, ä, ö, ü, eu, ei</i> en na medeklinkers (<i>l, n, r</i>). Het is een zachte, sissende klank voorin de mond (zoals in <i>ich</i>, <i>nicht</i>, <i>welche</i>, <i>Mädchen</i>, <i>Bücher</i>).</li>
      <li><b>De 'Ach-Laut' (harde ch):</b> Na de klinkers <b>a, o, u, au</b>. Dit is een hardere keelklank (zoals in <i>ach</i>, <i>Kuchen</i>, <i>Buch</i>, <i>Nacht</i>, <i>auch</i>).</li>
      <li><b>-chs:</b> Spreek je uit als een <b>'x'</b> of <b>'ks'</b> (in <i>sechs</i> = zesk, <i>Wachs</i> = was, <i>Fuchs</i> = vos).</li>
    </ul>

    <h4>2. Landeskunde: Beroemde Evenementen in Duitsland</h4>
    <div class="formule-box">
      <b>Belangrijke Culturele Feste:</b><br>
      • <b>Karneval in Köln:</b> Begint traditiegetrouw op 11 november om 11:11 uur ('Elfter im Elften'). Hoogtepunt is <i>Rosenmontag</i> met enorme praalwagens en de kreet <i>Kölle Alaaf!</i>.<br>
      • <b>Berlinale (Internationale Filmfestspiele Berlin):</b> Een van de belangrijkste filmfestivals ter wereld, waar de felbegeerde <i>Goldene Bär</i> wordt uitgereikt.<br>
      • <b>Die Weihnachtsmärkte:</b> Wereldberoemde sfeervolle kerstmarkten in steden als Neurenberg (<i>Nürnberger Christkindlesmarkt</i>) en Dresden met <i>Glühwein</i> en <i>Lebkuchen</i>.
    </div>

    <h4>3. Leesstrategie: Advertenties en Evenementprogramma's</h4>
    <p>Bij het lezen van posters en uitnodigingen zoek je gericht naar:</p>
    <ul>
      <li><i>Einlass</i> = Zaal open / Toegang vanaf | <i>Beginn</i> = Aanvang</li>
      <li><i>Eintritt frei</i> = Gratis toegang | <i>Vorverkauf (VVK)</i> = Voorverkoop</li>
      <li><i>Veranstaltungsort / Location</i> = Locatie van het evenement</li>
    </ul>
  """,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wanneer spreek je 'ch' uit als de zachte 'Ich-Laut' (voorin de mond)?",
      "opties": ["Na de klinkers e, i, ä, ö, ü en na medeklinkers (zoals in 'nicht' of 'Milch').", "Alleen na de klinkers a, o en u.", "Aan het begin van elk Duits woord.", "Alleen in leenwoorden uit het Frans."],
      "antwoord": 0,
      "uitleg": "Na e, i, ä, ö, ü en medeklinkers l/n/r klinkt de ch zacht (Ich-Laut)."
    },
    {
      "type": "mc",
      "vraag": "Hoe spreek je het Duitse woord 'sechs' (zes) uit?",
      "opties": ["Als 'zeks' (met een x/ks klank)", "Als 'zecht' (met een harde ch)", "Als 'zechsj'", "Als 'zes'"],
      "antwoord": 0,
      "uitleg": "De combinatie -chs wordt in het Duits als 'ks' uitgesproken (zoals in 'sechs' en 'Fuchs')."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de term 'Eintritt frei' op een festivalposter?",
      "opties": ["De toegang is gratis.", "Toegang alleen voor volwassenen.", "Kaartjes zijn uitverkocht.", "Toegang alleen met een uitnodiging."],
      "antwoord": 0,
      "uitleg": "'Eintritt frei' betekent dat er geen entree betaald hoeft te worden (gratis toegang)."
    },
    {
      "type": "mc",
      "vraag": "Wat is de traditionele feestkreet tijdens het carnaval in Keulen?",
      "opties": ["Kölle Alaaf!", "Prost Neujahr!", "Guten Appetit!", "Auf Wiedersehen!"],
      "antwoord": 0,
      "uitleg": "'Kölle Alaaf!' is de traditionele carnavalsgroet in Keulen."
    },
    {
      "type": "waaronwaar",
      "vraag": "In het woord 'Buch' en 'Kuchen' spreek je de 'ch' uit als een harde 'Ach-Laut' (keelklank).",
      "antwoord": True,
      "uitleg": "Waar! Na de klinkers a, o, u en au is de ch altijd een harde keelklank (Ach-Laut)."
    },
    {
      "type": "waaronwaar",
      "vraag": "De 'Berlinale' is een beroemd Duits bierfestival in Berlijn.",
      "antwoord": False,
      "uitleg": "Onwaar! De Berlinale is een internationaal filmfestival waar de Gouden Beer wordt uitgereikt."
    },
    {
      "type": "invoer",
      "vraag": "Wat betekent de Duitse term 'Vorverkauf' (VVK) bij een concertkaartje?",
      "antwoord": "voorverkoop",
      "uitleg": "'Vorverkauf' betekent voorverkoop van kaartjes."
    },
    {
      "type": "invoer",
      "vraag": "Wat is het Duitse woord voor 'Kerstmis'?",
      "antwoord": "Weihnachten",
      "uitleg": "Kerstmis is in het Duits 'Weihnachten'."
    }
  ]
}

# H5.1, H5.2, H5.3
h5_1 = {
  "id": "dui-h5-1",
  "hoofdstuk": 5,
  "paragraaf": "5.1",
  "titel": "Wortschatz & Sprachmittel: Zukunft, Berufe & Ausbildung",
  "korteUitleg": "Beroepen, opleidingen, schoolvakken, bijbaantjes en praten over toekomstplannen in het Duits.",
  "icoon": "💼",
  "kleur": "roze",
  "theorie": """
    <h3>5.1 Wortschatz & Sprachmittel: Zukunft, Berufe & Ausbildung</h3>
    <div class="info-box">
      <b>Kernbegrippen:</b> der Beruf (het beroep), die Arbeit (het werk), die Ausbildung (de beroepsopleiding), das Studium / studieren (de universitaire studie / studeren), die Schule (de school), der Abschluss (het diploma/diplomering), der Nebenjob (het bijbaantje), das Geld verdienen (geld verdienen), das Praktikum (de stage), die Bewerbung (de sollicitatie), der Lebenslauf (het cv), die Zukunft (de toekomst), der Traum (de droom).
    </div>
    <h4>1. Beroepen in het Mannelijk en Vrouwelijk</h4>
    <p>In het Duits krijgt de vrouwelijke variant van een beroep bijna altijd de uitgang <b>-in</b> (meervoud: <b>-innen</b>):</p>
    <ul>
      <li><i>der Lehrer</i> (de leraar) → <i>die Lehrerin</i> (de lerares)</li>
      <li><i>der Arzt</i> (de arts) → <i>die Ärztin</i> (met Umlaut!)</li>
      <li><i>der Verkäufer</i> (de verkoper) → <i>die Verkäuferin</i></li>
      <li><i>der Polizist</i> (de politieagent) → <i>die Polizistin</i></li>
      <li><i>der Informatiker</i> (de IT'er) → <i>die Informatikerin</i></li>
      <li><i>der Krankenpfleger</i> (de verpleger) → <i>die Krankenschwester / Krankenpflegerin</i></li>
    </ul>

    <h4>2. Sprachmittel: Praten over toekomstplannen</h4>
    <div class="formule-box">
      <b>Zinnen over de toekomst:</b><br>
      • <i>Was möchtest du später werden?</i> — Wat wil je later worden?<br>
      • <i>Ich möchte <b>als</b> Arzt / Journalistin arbeiten.</i> — Ik wil als arts / journaliste werken (let op: in het Duits zonder 'een'!).<br>
      • <i>Nach der Schule möchte ich ein Praktikum machen.</i> — Na school wil ik een stage doen.<br>
      • <i>Ich will an der Universität studieren.</i> — Ik wil aan de universiteit studeren.<br>
      • <i>Ich interessiere mich für Technik und Sprachen.</i> — Ik interesseer me voor techniek en talen.<br>
      • <i>Mein Traumberuf ist Ingenieur.</i> — Mijn droomberoep is ingenieur.
    </div>

    <h4>3. Het werkwoord 'studieren' vs. 'lernen'</h4>
    <p>Let op dit belangrijke verschil:</p>
    <ul>
      <li><b>studieren:</b> Uitsluitend gebruikt voor een studie aan een hogeschool of universiteit (<i>Ich studiere Medizin</i>).</li>
      <li><b>lernen:</b> Leren voor een toets of op school (<i>Ich lerne Deutsch für die Klassenarbeit</i>).</li>
    </ul>
  """,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Hoe zeg je in correct Duits: 'Ik wil later als leraar werken'?",
      "opties": ["Ich möchte später als Lehrer arbeiten.", "Ich will später als ein Lehrer arbeiten.", "Ich möchte als der Lehrer schaffen.", "Ich will später arbeiten wie Lehrer."],
      "antwoord": 0,
      "uitleg": "In het Duits gebruik je 'als + beroep' zonder lidwoord (als Lehrer)."
    },
    {
      "type": "mc",
      "vraag": "Wat is de vrouwelijke vorm van 'der Arzt' (de arts)?",
      "opties": ["die Ärztin", "die Arztin", "die Arzterin", "die Frauarzt"],
      "antwoord": 0,
      "uitleg": "De vrouwelijke vorm van 'der Arzt' is 'die Ärztin' (met Umlaut en de uitgang -in)."
    },
    {
      "type": "mc",
      "vraag": "Wanneer gebruik je in het Duits het werkwoord 'studieren'?",
      "opties": ["Alleen als je een opleiding volgt aan een hogeschool of universiteit.", "Als je huiswerk maakt voor wiskunde.", "Als je woordjes leert voor Duits.", "Als je op de basisschool zit."],
      "antwoord": 0,
      "uitleg": "'Studieren' betekent studeren aan een universiteit/hogeschool. Voor schoolwerk gebruik je 'lernen'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de term 'das Praktikum'?",
      "opties": ["de stage", "het proefwerk", "de vakantiebaan", "het eindexamen"],
      "antwoord": 0,
      "uitleg": "'Das Praktikum' betekent stage lopen bij een bedrijf."
    },
    {
      "type": "waaronwaar",
      "vraag": "Vrouwelijke beroepsnamen krijgen in het Duits bijna altijd de uitgang '-in' (zoals Polizistin, Bäckerin).",
      "antwoord": True,
      "uitleg": "Waar! Vrouwelijke beroepen eindigen in het Duits op '-in'."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Duitse woord 'die Bewerbung' betekent 'de advertentie op televisie'.",
      "antwoord": False,
      "uitleg": "Onwaar! 'Die Bewerbung' betekent de sollicitatie(brief)."
    },
    {
      "type": "invoer",
      "vraag": "Wat is het Duitse woord voor 'de stage'?",
      "antwoord": "Praktikum",
      "uitleg": "Stage is in het Duits 'das Praktikum'."
    },
    {
      "type": "invoer",
      "vraag": "Wat is het Duitse woord voor 'de toekomst'?",
      "antwoord": "Zukunft",
      "uitleg": "De toekomst is in het Duits 'die Zukunft'."
    }
  ]
}

h5_2 = {
  "id": "dui-h5-2",
  "hoofdstuk": 5,
  "paragraaf": "5.2",
  "titel": "Grammatik: Starke Verben mit Vokalwechsel (a→ä, e→i/ie)",
  "korteUitleg": "Sterke werkwoorden met een klinkerwisseling in de tegenwoordige tijd bij du en er/sie/es.",
  "icoon": "📖",
  "kleur": "roze",
  "theorie": """
    <h3>5.2 Grammatik: Starke Verben mit Vokalwechsel (a→ä, e→i/ie)</h3>
    <div class="info-box">
      <b>Grammaticafocus:</b> Sterke werkwoorden die in de tegenwoordige tijd (Präsens) bij <b>du</b> en <b>er/sie/es</b> een klinkerverandering in de stam krijgen.
    </div>
    <h4>1. Klinkerwisseling van a naar ä</h4>
    <p>Bij werkwoorden met een <i>a</i> in de stam krijgt de klinker bij <code>du</code> en <code>er/sie/es</code> een <b>Umlaut (ä)</b>:</p>
    <div class="formule-box">
      <b>fahren (rijden):</b><br>
      • ich fahr<b>e</b> | wir fahr<b>en</b><br>
      • du f<b>ä</b>hr<b>st</b> | ihr fahr<b>t</b><br>
      • er/sie/es f<b>ä</b>hr<b>t</b> | sie/Sie fahr<b>en</b><br><br>
      <i>Andere a→ä werkwoorden:</i> <b>schlafen</b> (du schläfst, er schläft), <b>tragen</b> (du trägst, er trägt), <b>waschen</b> (du wäschst), <b>laufen</b> (du läufst, er läuft).
    </div>

    <h4>2. Klinkerwisseling van e naar i</h4>
    <p>Bij werkwoorden met een korte <i>e</i> in de stam verandert de klinker bij <code>du</code> en <code>er/sie/es</code> in een <b>i</b>:</p>
    <div class="formule-box">
      <b>helfen (helpen):</b><br>
      • ich helf<b>e</b> | wir helf<b>en</b><br>
      • du h<b>i</b>lf<b>st</b> | ihr helf<b>t</b><br>
      • er/sie/es h<b>i</b>lf<b>t</b> | sie/Sie helf<b>en</b><br><br>
      <i>Andere e→i werkwoorden:</i> <b>sprechen</b> (du sprichst, er spricht), <b>geben</b> (du gibst, er gibt), <b>treffen</b> (du triffst, er trifft), <b>essen</b> (du isst, er isst).
    </div>

    <h4>3. Klinkerwisseling van e naar ie (lange klank)</h4>
    <p>Bij een lange <i>e</i> verandert de klinker in <b>ie</b>:</p>
    <ul>
      <li><b>lesen (lezen):</b> ich lese, du l<b>ie</b>st, er l<b>ie</b>st, wir lesen, ihr lest, sie lesen</li>
      <li><b>sehen (zien):</b> ich sehe, du s<b>ie</b>hst, er s<b>ie</b>ht, wir sehen, ihr seht, sie sehen</li>
    </ul>
    <p><i>Let op:</i> Bij <code>ich</code>, <code>wir</code>, <code>ihr</code> en <code>sie/Sie</code> verandert de stamklinker <b>NOOIT</b>!</p>
  """,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm: 'Lukas ____ (lezen) jeden Tag die Zeitung.'",
      "opties": ["liest", "lest", "leset", "leest"],
      "antwoord": 0,
      "uitleg": "Bij 'er' (Lukas) verandert 'e' naar 'ie': 'er liest'."
    },
    {
      "type": "mc",
      "vraag": "Vul aan: '____ du morgen mit dem Zug nach Köln?' (fahren)",
      "opties": ["Fährst", "Fahrst", "Fahrt", "Fähren"],
      "antwoord": 0,
      "uitleg": "Bij 'du' krijgt fahren een Umlaut: 'du fährst'."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm van 'helfen': 'Er ____ mir bei den Hausaufgaben.'",
      "opties": ["hilft", "helft", "helfen", "hilfst"],
      "antwoord": 0,
      "uitleg": "Bij 'er' verandert de e naar een i: 'er hilft'."
    },
    {
      "type": "mc",
      "vraag": "Wat is de juiste vorm bij 'ihr' voor het werkwoord 'sehen'?",
      "opties": ["ihr seht", "ihr sieht", "ihr sehet", "ihr siehst"],
      "antwoord": 0,
      "uitleg": "Bij 'ihr' is er GEEN klinkerwisseling: gewoon stam + t = 'ihr seht'."
    },
    {
      "type": "waaronwaar",
      "vraag": "De klinkerwisseling (a→ä en e→i/ie) vindt alleen plaats bij de vormen van 'du' en 'er/sie/es'.",
      "antwoord": True,
      "uitleg": "Waar! Alleen in de 2e en 3e persoon enkelvoud (du en er/sie/es) treedt de verandering op."
    },
    {
      "type": "waaronwaar",
      "vraag": "Bij 'wir' verandert het werkwoord spreken naar 'wir sprichen'.",
      "antwoord": False,
      "uitleg": "Onwaar! Bij 'wir' blijft de stam ongewijzigd: 'wir sprechen'."
    },
    {
      "type": "invoer",
      "vraag": "Vul de juiste vorm van 'geben' in: 'Er ____ mir einen Apfel.'",
      "antwoord": "gibt",
      "uitleg": "Bij 'er' verandert de stam naar i: 'er gibt'."
    },
    {
      "type": "invoer",
      "vraag": "Vul de juiste vorm van 'schlafen' in: 'Das Kind ____ schon.'",
      "antwoord": "schläft",
      "uitleg": "Bij 'das Kind' (er/sie/es) krijgt schlafen een Umlaut: 'schläft'."
    }
  ]
}

h5_3 = {
  "id": "dui-h5-3",
  "hoofdstuk": 5,
  "paragraaf": "5.3",
  "titel": "Aussprache, Lesen & Landeskunde: Klanken & Schulsysteem",
  "korteUitleg": "Uitspraak van g en j, en Landeskunde over het Duitse schoolsysteem (Gymnasium, Realschule, Hauptschule, Duale Ausbildung).",
  "icoon": "🎓",
  "kleur": "roze",
  "theorie": """
    <h3>5.3 Aussprache, Lesen & Landeskunde: Klanken & Schulsysteem</h3>
    <div class="info-box">
      <b>Thema's:</b> Uitspraak van de letters <i>g</i> en <i>j</i>, en Landeskunde over het onderwijssysteem in Duitsland.
    </div>
    <h4>1. Aussprache: g en j</h4>
    <ul>
      <li><b>De Duitse g:</b> Klinkt aan het begin en midden van een woord altijd als een harde 'g' (zoals in het Engelse <i>good</i> of Franse <i>garçon</i>, nooit als de zachte Nederlandse g!). Bijv. <i>gut</i>, <i>Garten</i>, <i>gehen</i>.</li>
      <li><b>-ig aan het einde van een woord:</b> Spreek je in het Standaardduits uit als een zachte <b>'ich'</b> (bijv. <i>richtig</i> = 'richtich', <i>fertig</i> = 'fertich', <i>zwanzig</i> = 'zwanzich').</li>
      <li><b>De Duitse j:</b> Klinkt altijd als de Nederlandse 'j' in 'ja' (in <i>Jahr</i>, <i>Jugend</i>, <i>Jacke</i>).</li>
    </ul>

    <h4>2. Landeskunde: Das deutsche Schulsystem</h4>
    <p>Het schoolsysteem in Duitsland verschilt wezenlijk van het Nederlandse:</p>
    <div class="formule-box">
      <b>De schooltypes in Duitsland:</b><br>
      • <b>Grundschule (groep 1 t/m 4):</b> Basisschool voor alle kinderen tot ongeveer 10 jaar.<br>
      • <b>Hauptschule:</b> Praktijkgericht onderwijs ter voorbereiding op een vakopleiding.<br>
      • <b>Realschule:</b> Middelbaar algemeen onderwijs (vergelijkbaar met HAVO/VMBO-t).<br>
      • <b>Gymnasium:</b> VWO-niveau, afgesloten met het <b>Abitur</b> (het diploma dat toegang geeft tot de universiteit).<br>
      • <b>Gesamtschule:</b> Brede scholengemeenschap waar alle niveaus gecombineerd worden.<br>
      • <b>Duales Ausbildungssystem:</b> Een wereldwijd geprezen systeem waarbij jongeren leren op een vakschool (<i>Berufsschule</i>) combineren met betaald werken in een leerbedrijf.
    </div>

    <h4>3. Het Duitse Cijfersysteem (Noten)</h4>
    <p>In Duitsland lopen schoolcijfers van <b>1 (beste)</b> tot <b>6 (slechtste)</b>:</p>
    <ul>
      <li><b>1 = sehr gut</b> (uitmuntend / 9-10)</li>
      <li><b>2 = gut</b> (goed / 8)</li>
      <li><b>3 = befriedigend</b> (voldoende / 6-7)</li>
      <li><b>4 = ausreichend</b> (net voldoende / 5,5)</li>
      <li><b>5 = mangelhaft</b> (onvoldoende / 4)</li>
      <li><b>6 = ungenügend</b> (zeer slecht / 1-3)</li>
    </ul>
  """,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat is in het Duitse cijfersysteem het allerhoogste cijfer?",
      "opties": ["1 (sehr gut)", "10 (uitmuntend)", "6 (sehr gut)", "5 (ausgezeichnet)"],
      "antwoord": 0,
      "uitleg": "In Duitsland is 1 het hoogste cijfer (sehr gut) en 6 het laagste cijfer (ungenügend)."
    },
    {
      "type": "mc",
      "vraag": "Hoe spreek je het woordeinde '-ig' uit in woorden als 'richtig' of 'fertig'?",
      "opties": ["Als een zachte 'ich'-klank", "Als 'ik'", "Als 'ing'", "Als 'isj'"],
      "antwoord": 0,
      "uitleg": "In het Standaardduits spreek je de uitgang '-ig' uit als '-ich' (bijv. 'richtich')."
    },
    {
      "type": "mc",
      "vraag": "Hoe heet het eindexamendiploma van het Duitse Gymnasium dat toegang geeft tot de universiteit?",
      "opties": ["Das Abitur", "Der Realschulabschluss", "Das Diplom", "Die Matura"],
      "antwoord": 0,
      "uitleg": "Het eindexamen en diploma van het Gymnasium in Duitsland heet het 'Abitur'."
    },
    {
      "type": "mc",
      "vraag": "Wat houdt het 'Duale Ausbildungssystem' in Duitsland in?",
      "opties": ["Leren op een vakschool combineren met praktijkervaring in een leerbedrijf.", "Twee talen tegelijk leren op school.", "Online lessen volgen vanuit huis.", "Twee jaar lang verplicht in het leger dienen."],
      "antwoord": 0,
      "uitleg": "Het 'Duale System' combineert theorie op de Berufsschule met praktijkwerk bij een werkgever."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een cijfer 5 (mangelhaft) is in Duitsland een ruime voldoende.",
      "antwoord": False,
      "uitleg": "Onwaar! Cijfer 5 is een dikke onvoldoende (4 is de grens voor voldoende)."
    },
    {
      "type": "waaronwaar",
      "vraag": "De 'Grundschule' in Duitsland duurt in de meeste deelstaten 4 jaar.",
      "antwoord": True,
      "uitleg": "Waar! Na groep 4 (ongeveer 10 jaar oud) stromen Duitse leerlingen al door naar het voortgezet onderwijs."
    },
    {
      "type": "invoer",
      "vraag": "Hoe heet het Duitse vwo-diploma?",
      "antwoord": "Abitur",
      "uitleg": "Het diploma heet het 'Abitur'."
    },
    {
      "type": "invoer",
      "vraag": "Wat is het Duitse schoolcijfer voor 'sehr gut' (zeer goed)?",
      "antwoord": "1",
      "uitleg": "Het beste cijfer in Duitsland is een 1."
    }
  ]
}

# H6.1, H6.2, H6.3
h6_1 = {
  "id": "dui-h6-1",
  "hoofdstuk": 6,
  "paragraaf": "6.1",
  "titel": "Wortschatz & Sprachmittel: In Aktion, Notfälle & Ehrenamt",
  "korteUitleg": "Hulpdiensten, noodgevallen, vrijwilligerswerk, goede doelen en eerste hulp in het Duits.",
  "icoon": "🚑",
  "kleur": "geel",
  "theorie": """
    <h3>6.1 Wortschatz & Sprachmittel: In Aktion, Notfälle & Ehrenamt</h3>
    <div class="info-box">
      <b>Kernbegrippen:</b> der Notfall (het noodgeval), die Hilfe (de hulp), der Unfall (het ongeluk), der Notruf (de noodoproep), die Rettung / retten (de redding / redden), die Feuerwehr (de brandweer), der Feuerwehrmann / die Feuerwehrfrau (de brandweerman/vrouw), die Polizei (de politie), der Rettungswagen / Krankenwagen (de ambulance), das Ehrenamt / ehrenamtlich (het vrijwilligerswerk / vrijwillig), die Organisation (de organisatie), spenden (doneren/schenken), die Umwelt schützen (het milieu beschermen), helfen (helpen).
    </div>
    <h4>1. Ein Notfall melden (De 5 W-vragen bij een noodoproep)</h4>
    <p>Als je in Duitsland het alarmnummer <b>112</b> belt, beantwoord je de <b>5 W-Fragen</b>:</p>
    <div class="formule-box">
      <b>Die 5 W-Fragen bei einem Notruf:</b><br>
      1. <b>Wo</b> ist der Unfallort? (Waar is het gebeurd?)<br>
      2. <b>Was</b> ist geschehen? (Wat is er gebeurd?)<br>
      3. <b>Wie viele</b> Verletzte gibt es? (Hoeveel gewonden zijn er?)<br>
      4. <b>Welche</b> Verletzungen liegen vor? (Welke verwondingen zijn er?)<br>
      5. <b>Warten</b> auf Rückfragen! (Wacht op vragen van de meldkamer, hang niet direct op!)
    </div>

    <h4>2. Sprachmittel: Om hulp vragen & aanbieden</h4>
    <ul>
      <li><i>Hilfe! Rufen Sie bitte sofort einen Krankenwagen!</i> — Help! Belt u alstublieft direct een ambulance!</li>
      <li><i>Es gab einen schweren Unfall auf der Kreuzung.</i> — Er was een zwaar ongeluk op de kruising.</li>
      <li><i>Kann ich Ihnen helfen?</i> — Kan ik u helpen?</li>
      <li><i>Keine Panik, die Rettungskräfte sind schon unterwegs.</i> — Geen paniek, de hulpdiensten zijn al onderweg.</li>
      <li><i>Ich engagiere mich ehrenamtlich für den Tierschutz.</i> — Ik zet me vrijwillig in voor dierenbescherming.</li>
    </ul>

    <h4>3. Vrijwilligerswerk (Das Ehrenamt) in Duitsland</h4>
    <p>In Duitsland is het <b>Ehrenamt</b> erg populair. Miljoenen burgers zetten zich vrijwillig in bij:</p>
    <ul>
      <li><b>Freiwillige Feuerwehr:</b> In de meeste Duitse dorpen en kleinere steden bestaat de brandweer volledig uit vrijwilligers.</li>
      <li><b>THW (Technisches Hilfswerk):</b> Civiele bescherming bij overstromingen, stormen en rampen.</li>
      <li><b>DRK (Deutsches Rotes Kreuz):</b> Eerste hulp, bloeddonaties en noodopvang.</li>
    </ul>
  """,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat betekent de term 'ehrenamtlich arbeiten' in het Duits?",
      "opties": ["Als vrijwilliger werken (zonder betaling voor een goed doel).", "In de politiek werken.", "Heel veel geld verdienen met overwerk.", "Directeur zijn van een groot bedrijf."],
      "antwoord": 0,
      "uitleg": "'Ehrenamtlich' betekent vrijwillig / onbezoldigd maatschappelijk werk doen."
    },
    {
      "type": "mc",
      "vraag": "Wat is de 5e W-regel ('Warten') bij een noodoproep naar 112?",
      "opties": ["Niet direct ophangen, maar wachten op eventuele vragen van de meldkamer.", "Wachten tot de ambulance er is voor je belt.", "Wachten met reanimeren.", "Wachten tot het ongeluk voorbij is."],
      "antwoord": 0,
      "uitleg": "De laatste 'W' staat voor 'Warten auf Rückfragen': blijf aan de lijn tot de centralist ophangt."
    },
    {
      "type": "mc",
      "vraag": "Wat is het Duitse woord voor 'de brandweer'?",
      "opties": ["die Feuerwehr", "die Polizei", "der Rettungsdienst", "das Krankenhaus"],
      "antwoord": 0,
      "uitleg": "'Die Feuerwehr' is de brandweer."
    },
    {
      "type": "mc",
      "vraag": "Hoe roep je in nood 'Help! Bel alstublieft een ambulance!'?",
      "opties": ["Hilfe! Rufen Sie bitte einen Krankenwagen!", "Hilfe! Suchen Sie einen Arzt!", "Achtung! Fahren Sie mit dem Bus!", "Hallo! Kommen Sie hierher!"],
      "antwoord": 0,
      "uitleg": "'Krankenwagen' of 'Rettungswagen' is de ambulance."
    },
    {
      "type": "waaronwaar",
      "vraag": "In veel Duitse dorpen bestaat de brandweer uit vrijwilligers van de 'Freiwillige Feuerwehr'.",
      "antwoord": True,
      "uitleg": "Waar! De vrijwillige brandweer is een enorme steunpilaar in de Duitse samenleving."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Duitse woord 'der Unfall' betekent 'de overwinning'.",
      "antwoord": False,
      "uitleg": "Onwaar! 'Der Unfall' betekent 'het ongeluk'."
    },
    {
      "type": "invoer",
      "vraag": "Wat is het Duitse woord voor 'het ongeluk'?",
      "antwoord": "Unfall",
      "uitleg": "Het ongeluk is in het Duits 'der Unfall'."
    },
    {
      "type": "invoer",
      "vraag": "Vertaal het Duitse woord voor de brandweerkazerne / brandweer: 'die ____'",
      "antwoord": "Feuerwehr",
      "uitleg": "De brandweer is 'die Feuerwehr'."
    }
  ]
}

h6_2 = {
  "id": "dui-h6-2",
  "hoofdstuk": 6,
  "paragraaf": "6.2",
  "titel": "Grammatik: Het Complete Naamvallensysteem (1e, 3e & 4e naamval)",
  "korteUitleg": "Het complete overzicht van lidwoorden en naamvallen: Nominativ, Dativ en Akkusativ herkennen en correct toepassen.",
  "icoon": "📖",
  "kleur": "geel",
  "theorie": """
    <h3>6.2 Grammatik: Het Complete Naamvallensysteem (1e, 3e & 4e naamval)</h3>
    <div class="info-box">
      <b>Grammaticafocus:</b> De synthese van de drie belangrijkste naamvallen in het Duits: 1e naamval (Nominativ - onderwerp), 3e naamval (Dativ - meewerkend voorwerp) en 4e naamval (Akkusativ - lijdend voorwerp).
    </div>
    <h4>1. De Grote Naamvallentabel (der-Gruppe)</h4>
    <div class="formule-box">
      <table style="width:100%;border-collapse:collapse;font-size:14px;">
        <tr style="border-bottom:2px solid #ccc;text-align:left;">
          <th>Naamval</th><th>Mannelijk (m)</th><th>Vrouwelijk (v)</th><th>Onzijdig (o)</th><th>Meervoud (mv)</th>
        </tr>
        <tr><td><b>1e nv (Nom)</b> - Onderwerp</td><td><b>der</b></td><td><b>die</b></td><td><b>das</b></td><td><b>die</b></td></tr>
        <tr><td><b>3e nv (Dat)</b> - Meewerkend vw</td><td><b>dem</b></td><td><b>der</b></td><td><b>dem</b></td><td><b>den</b> (+n)</td></tr>
        <tr><td><b>4e nv (Akk)</b> - Lijdend vw</td><td><b>den</b></td><td><b>die</b></td><td><b>das</b></td><td><b>die</b></td></tr>
      </table>
    </div>

    <h4>2. De ein-Gruppe (ein, kein, mein, dein, sein, ihr, unser, euer)</h4>
    <div class="formule-box">
      <table style="width:100%;border-collapse:collapse;font-size:14px;">
        <tr style="border-bottom:2px solid #ccc;text-align:left;">
          <th>Naamval</th><th>Mannelijk (m)</th><th>Vrouwelijk (v)</th><th>Onzijdig (o)</th><th>Meervoud (mv)</th>
        </tr>
        <tr><td><b>1e nv (Nom)</b></td><td>ein</td><td>eine</td><td>ein</td><td>keine / meine</td></tr>
        <tr><td><b>3e nv (Dat)</b></td><td>ein<b>em</b></td><td>ein<b>er</b></td><td>ein<b>em</b></td><td>kein<b>en</b> / mein<b>en</b> (+n)</td></tr>
        <tr><td><b>4e nv (Akk)</b></td><td>ein<b>en</b></td><td>eine</td><td>ein</td><td>keine / meine</td></tr>
      </table>
    </div>

    <h4>3. Stappenplan voor de juiste naamval</h4>
    <ol>
      <li><b>Zoek de persoonsvorm (het werkwoord).</b></li>
      <li><b>Wie of wat doet het?</b> → 1e naamval (Nominativ - onderwerp).</li>
      <li><b>Wie of wat + werkwoord + onderwerp?</b> → 4e naamval (Akkusativ - lijdend voorwerp).</li>
      <li><b>Aan wie of voor wie?</b> → 3e naamval (Dativ - meewerkend voorwerp).</li>
    </ol>
    <p><i>Voorbeeld:</i> <b>Der Junge</b> (1e nv) gibt <b>dem Mädchen</b> (3e nv) <b>einen Apfel</b> (4e nv).</p>
  """,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Kies het juiste lidwoord (3e naamval mannelijk): 'Der Arzt hilft ____ (der Mann).'",
      "opties": ["dem", "den", "der", "des"],
      "antwoord": 0,
      "uitleg": "Helfen krijgt de 3e naamval (Dativ). Het mannelijke lidwoord in de 3e naamval is 'dem'."
    },
    {
      "type": "mc",
      "vraag": "Welke vorm hoort in de 3e naamval voor een vrouwelijk woord (die Frau)?",
      "opties": ["der Frau / einer Frau", "die Frau / eine Frau", "dem Frau / einem Frau", "den Frau / einen Frau"],
      "antwoord": 0,
      "uitleg": "In de 3e naamval (Dativ) verandert 'die' in 'der' en 'eine' in 'einer'."
    },
    {
      "type": "mc",
      "vraag": "In de zin 'Die Feuerwehr rettet den Hund' staat 'den Hund' in de:",
      "opties": ["4e naamval (Akkusativ - lijdend voorwerp)", "1e naamval (Nominativ - onderwerp)", "3e naamval (Dativ - meewerkend voorwerp)", "2e naamval (Genitiv)"],
      "antwoord": 0,
      "uitleg": "Wie of wat redt de brandweer? De hond = lijdend voorwerp = 4e naamval (den Hund)."
    },
    {
      "type": "mc",
      "vraag": "Vul aan (3e naamval onzijdig): 'Ich danke ____ Kind.' (das Kind)",
      "opties": ["dem", "das", "den", "der"],
      "antwoord": 0,
      "uitleg": "Danken krijgt de 3e naamval. Het onzijdige lidwoord in de 3e naamval is 'dem'."
    },
    {
      "type": "waaronwaar",
      "vraag": "In de 3e naamval (Dativ) krijgen zowel mannelijke als onzijdige woorden het lidwoord 'dem' (of 'einem').",
      "antwoord": True,
      "uitleg": "Waar! Zowel mannelijk als onzijdig hebben 'dem' / 'einem' in de 3e naamval."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het meervoudslidwoord in de 3e naamval is 'die'.",
      "antwoord": False,
      "uitleg": "Onwaar! In de 3e naamval meervoud is het lidwoord 'den' en krijgt het zelfstandig naamwoord vaak een extra '-n'."
    },
    {
      "type": "invoer",
      "vraag": "Vul het juiste lidwoord in (1e naamval van meisje - onzijdig): '____ Mädchen spielt im Park.'",
      "antwoord": "Das",
      "uitleg": "Meisje is in het Duits onzijdig: 'das Mädchen'."
    },
    {
      "type": "invoer",
      "vraag": "Vul het juiste lidwoord in (4e naamval mannelijk): 'Wir sehen ____ Hund.' (der Hund)",
      "antwoord": "den",
      "uitleg": "Lijdend voorwerp mannelijk = 'den Hund'."
    }
  ]
}

h6_3 = {
  "id": "dui-h6-3",
  "hoofdstuk": 6,
  "paragraaf": "6.3",
  "titel": "Aussprache, Lesen & Landeskunde: Klanken & THW",
  "korteUitleg": "Uitspraak van de plofklanken p, t, k (aspiratie) en Landeskunde over civiele bescherming en hulpdiensten in Duitsland.",
  "icoon": "🚒",
  "kleur": "geel",
  "theorie": """
    <h3>6.3 Aussprache, Lesen & Landeskunde: Klanken & THW</h3>
    <div class="info-box">
      <b>Thema's:</b> De geaspireerde uitspraak van de plofklanken (Explosivlaute p, t, k) en Landeskunde over het THW en rampenbestrijding.
    </div>
    <h4>1. Aussprache: Geaspireerde plofklanken (p, t, k)</h4>
    <p>In het Duits worden de letters <b>p</b>, <b>t</b> en <b>k</b> met een lichte ademstoot (<i>Behauchung / Aspiration</i>) uitgesproken, alsof er een kleine 'h' achter staat:</p>
    <ul>
      <li><b>p</b>: in <i>Pass</i> ('p-h-as'), <i>Polizei</i>, <i>Park</i>.</li>
      <li><b>t</b>: in <i>Tag</i> ('t-h-aag'), <i>Tee</i>, <i>Telefon</i>.</li>
      <li><b>k</b>: in <i>Krankenhaus</i> ('k-h-rankenhaus'), <i>Katze</i>, <i>Kaffee</i>.</li>
    </ul>

    <h4>2. Landeskunde: Das THW (Technisches Hilfswerk)</h4>
    <div class="formule-box">
      <b>Wat is het THW?</b><br>
      • De <b>Bundesanstalt Technisches Hilfswerk (THW)</b> is de officiële civiele rampenbestrijdingsdienst van Duitsland, herkenbaar aan de opvallende <b>blauwe vrachtwagens</b>.<br>
      • Het bijzondere aan het THW is dat maar liefst <b>99% van de 80.000 medewerkers vrijwilliger</b> is!<br>
      • Het THW wordt ingezet bij zware stormen, overstromingen (zoals bij de rivier de Ahr), aardbevingen in het buitenland en het herstellen van drinkwater- en stroomvoorzieningen.<br>
      • Voor jongeren is er de <i>THW-Jugend</i>, waar tieners leren hoe ze bruggen bouwen, boten besturen en mensen redden.
    </div>

    <h4>3. Leesvaardigheid: Nieuwsberichten en Ooggetuigenverslagen</h4>
    <p>Bij het lezen van nieuwsartikelen over incidenten let je op:</p>
    <ul>
      <li><i>Die Ursache</i> = De oorzaak van het incident</li>
      <li><i>Die Feuerwehr löschte den Brand</i> = De brandweer bluste de brand</li>
      <li><i>Niemand wurde verletzt</i> = Niemand raakte gewond</li>
      <li><i>Der Sachschaden beträgt...</i> = De materiële schade bedraagt...</li>
    </ul>
  """,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat is het Technisches Hilfswerk (THW) in Duitsland?",
      "opties": ["De Duitse civiele rampenbestrijdingsdienst (met blauwe voertuigen) die voor 99% uit vrijwilligers bestaat.", "Een particuliere beveiligingsfirma in Berlijn.", "Een sportvereniging voor tieners.", "De officiële Duitse douane bij de grens."],
      "antwoord": 0,
      "uitleg": "Het THW is de federale rampenbestrijdingsorganisatie die bijna volledig op vrijwilligers draait."
    },
    {
      "type": "mc",
      "vraag": "Hoe worden de letters 'p', 't' en 'k' in het Duits uitgesproken?",
      "opties": ["Met een lichte ademstoot (aspiratie), alsof er een 'h' achter staat.", "Heel zacht en ingeslikt.", "Altijd als een stemhebbende 'b' of 'd'.", "Precies zoals in het Frans."],
      "antwoord": 0,
      "uitleg": "In het Duits zijn de stemloze plofklanken p, t en k geaspireerd (met ademstoot)."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de zin: 'Niemand wurde bei dem Unfall verletzt'?",
      "opties": ["Niemand raakte bij het ongeluk gewond.", "Iedereen is naar het ziekenhuis gebracht.", "De dader is gevlucht.", "Het ongeluk veroorzaakte veel schade."],
      "antwoord": 0,
      "uitleg": "'Verletzt werden' betekent gewond raken. 'Niemand wurde verletzt' = niemand raakte gewond."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent het Duitse woord 'die Ursache' in een nieuwsbericht?",
      "opties": ["De oorzaak", "Het gevolg", "De schade", "De dader"],
      "antwoord": 0,
      "uitleg": "'Die Ursache' betekent de oorzaak van de gebeurtenis."
    },
    {
      "type": "waaronwaar",
      "vraag": "De voertuigen van het Duitse THW zijn herkenbaar aan hun opvallende felblauwe kleur.",
      "antwoord": True,
      "uitleg": "Waar! THW-voertuigen zijn altijd blauw met witte belettering."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Duitse woord 'löschen' betekent 'aansteken van een vuur'.",
      "antwoord": False,
      "uitleg": "Onwaar! 'Löschen' betekent het blussen van een brand of wissen van data."
    },
    {
      "type": "invoer",
      "vraag": "Wat is het Duitse woord voor 'oorzaak'?",
      "antwoord": "Ursache",
      "uitleg": "De oorzaak is in het Duits 'die Ursache'."
    },
    {
      "type": "invoer",
      "vraag": "Vertaal het werkwoord 'blussen' naar het Duits: 'Die Feuerwehr konnte das Feuer schnell ____.'",
      "antwoord": "löschen",
      "uitleg": "Blussen is in het Duits 'löschen'."
    }
  ]
}

# Write all 18
all_onderwerpen = [
  ("h1_1.js", h1_1), ("h1_2.js", h1_2), ("h1_3.js", h1_3),
  ("h2_1.js", h2_1), ("h2_2.js", h2_2), ("h2_3.js", h2_3),
  ("h3_1.js", h3_1), ("h3_2.js", h3_2), ("h3_3.js", h3_3),
  ("h4_1.js", h4_1), ("h4_2.js", h4_2), ("h4_3.js", h4_3),
  ("h5_1.js", h5_1), ("h5_2.js", h5_2), ("h5_3.js", h5_3),
  ("h6_1.js", h6_1), ("h6_2.js", h6_2), ("h6_3.js", h6_3),
]

for filename, data in all_onderwerpen:
    write_onderwerp(filename, data)

print(f"\n🎉 Successfully generated all {len(all_onderwerpen)} onderwerpen for Duits!")

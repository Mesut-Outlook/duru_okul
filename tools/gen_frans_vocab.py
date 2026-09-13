# -*- coding: utf-8 -*-
import os, json, random

DATA_DIR = "/home/mesuto/Documents/PROJELER/duru_okul/havo3/frans/js/data"
os.makedirs(DATA_DIR, exist_ok=True)

def balance_mc(questions):
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

def write_examen(filename, data):
    balance_mc(data["vragen"])
    path = os.path.join(DATA_DIR, filename)
    titel = data["titel"]
    hf = data["hoofdstuk"]
    dumped = json.dumps(data, indent=2, ensure_ascii=False)
    content = "/* Proeftoets " + titel + "\n   Grandes Lignes 3 HAVO Unite " + str(hf) + " */\n"
    content += "DURU.registerExamen(" + dumped + ");\n"
    with open(path, "w", encoding="utf-8") as out:
        out.write(content)
    print("  [OK] Frans Vocab Examen saved: " + filename + " (" + str(len(data["vragen"])) + " vragen)")

# -------------------------------------------------------------
# TOETS 1: Sayfa 48 (Blok A & B)
# -------------------------------------------------------------
v1 = {
  "id": "ex-h3-frans-u1-v1",
  "hoofdstuk": 1,
  "hoofdstukTitel": "Unité 1 — Poste, like, partage",
  "titel": "Woordenschat 1 · p. 48 (blok A & B) · FR ⇄ NL",
  "vak": "Frans · HAVO 3 (U1)",
  "icoon": "🔤",
  "duurMin": 20,

  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat betekent het Franse woord <b>'le portable'</b> (p. 48)?",
      "opties": ["de mobiele telefoon", "het beeldscherm", "het toetsenbord", "de oplader"],
      "antwoord": 0,
      "uitleg": "'Le portable' is het Franse woord voor de mobiele telefoon / smartphone."
    },
    {
      "type": "mc",
      "vraag": "Wat is de juiste Franse vertaling van <b>'de rekening'</b> (p. 48)?",
      "opties": ["l'addition (v)", "le message", "la réaction", "le prix"],
      "antwoord": 0,
      "uitleg": "'L'addition' (vrouwelijk) betekent de rekening in een restaurant of café."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Franse werkwoord <b>'attendre'</b> (p. 48) betekent 'horen'.",
      "antwoord": False,
      "uitleg": "Onwaar. 'Attendre' betekent 'wachten'. 'Horen' is 'entendre'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het woord <i>'het bericht'</i> naar het Frans (p. 48): <i>J'ai envoyé un ... à mon ami.</i>",
      "antwoord": "message|le message",
      "uitleg": "'Le message' is het Franse woord voor 'het bericht'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent <b>'les réseaux sociaux'</b> (m mv, p. 48)?",
      "opties": ["de social media", "de klasgenoten", "de websites", "de contacten"],
      "antwoord": 0,
      "uitleg": "'Les réseaux sociaux' betekent de sociale media / sociale netwerken."
    },
    {
      "type": "mc",
      "vraag": "Welk Frans werkwoord betekent <b>'gebruiken'</b> (p. 48)?",
      "opties": ["utiliser", "travailler", "payer", "penser"],
      "antwoord": 0,
      "uitleg": "'Utiliser' betekent gebruiken. 'Travailler' is werken en 'payer' is betalen."
    },
    {
      "type": "waaronwaar",
      "vraag": "De uitdrukking <b>'grâce à'</b> (p. 48) betekent 'dankzij'.",
      "antwoord": True,
      "uitleg": "Waar. 'Grâce à' leidt een positieve reden in: 'dankzij'."
    },
    {
      "type": "invul",
      "vraag": "Wat betekent het Franse woord <b>'presque'</b> (p. 48) in het Nederlands?",
      "antwoord": "bijna",
      "uitleg": "'Presque' betekent 'bijna' (bijv. presque tous les jours = bijna elke dag)."
    },
    {
      "type": "mc",
      "vraag": "Wat is het tegenovergestelde van <b>'devant'</b> (voor)? Kies uit p. 48:",
      "opties": ["derrière (achter)", "près de (dichtbij)", "pourtant (toch)", "maintenant (nu)"],
      "antwoord": 0,
      "uitleg": "'Devant' betekent 'voor' en 'derrière' betekent 'achter'."
    },
    {
      "type": "mc",
      "vraag": "Hoe vertaal je <b>'nodig hebben'</b> in het Frans (p. 48)?",
      "opties": ["avoir besoin (de)", "avoir envie (de)", "avoir peur (de)", "faire attention (à)"],
      "antwoord": 0,
      "uitleg": "'Avoir besoin de' betekent 'nodig hebben' (J'ai besoin de mon portable)."
    },
    {
      "type": "waaronwaar",
      "vraag": "De woorden <b>'drôle'</b> en <b>'heureux'</b> (p. 48) betekenen exact hetzelfde.",
      "antwoord": False,
      "uitleg": "Onwaar. 'Drôle' betekent 'grappig', terwijl 'heureux' 'gelukkig' betekent."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het werkwoord <i>'stoppen'</i> naar het Frans (p. 48): <i>Il faut ... maintenant.</i>",
      "antwoord": "arrêter|arreter",
      "uitleg": "'Arrêter' betekent 'stoppen' of 'ophouden'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent <b>'les gens'</b> (m mv, p. 48)?",
      "opties": ["de mensen", "de jongens", "de ouders", "de vrienden"],
      "antwoord": 0,
      "uitleg": "'Les gens' betekent 'de mensen'."
    },
    {
      "type": "mc",
      "vraag": "Wat is de Franse vertaling van <b>'makkelijk'</b> (p. 48)?",
      "opties": ["facile", "difficile", "nouveau", "premier"],
      "antwoord": 0,
      "uitleg": "'Facile' betekent 'makkelijk'. Het tegenovergestelde is 'difficile'."
    },
    {
      "type": "waaronwaar",
      "vraag": "In het Frans betekent <b>'la tête'</b> (p. 48) 'het hoofd'.",
      "antwoord": True,
      "uitleg": "Waar. 'La tête' is het hoofd."
    },
    {
      "type": "invul",
      "vraag": "Wat betekent de uitdrukking <b>'j\'y vais'</b> (p. 48) in het Nederlands?",
      "antwoord": "ik ga weg|ik ga|ik ga ervandoor",
      "uitleg": "'J\'y vais' betekent 'ik ga weg' of 'ik ga er vandoor'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent het signaalwoord <b>'pourtant'</b> (p. 48)?",
      "opties": ["toch", "omdat", "daarom", "nooit"],
      "antwoord": 0,
      "uitleg": "'Pourtant' betekent 'toch' of 'echter'."
    },
    {
      "type": "mc",
      "vraag": "Welk Frans werkwoord betekent <b>'laten zien'</b> (p. 48)?",
      "opties": ["montrer", "garder", "télécharger", "oublier"],
      "antwoord": 0,
      "uitleg": "'Montrer' betekent 'laten zien'. 'Garder' betekent 'bewaren'."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het blauwe blokwoord <b>'le conseil'</b> (p. 48) betekent 'het advies'.",
      "antwoord": True,
      "uitleg": "Waar. 'Le conseil' is het advies of de tip."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het woord <i>'vergeten'</i> naar het Frans (p. 48): <i>N'allez pas ... votre mot de passe.</i>",
      "antwoord": "oublier",
      "uitleg": "'Oublier' betekent 'vergeten'."
    }
  ]
}

# -------------------------------------------------------------
# TOETS 2: Sayfa 49 (Blok E & F)
# -------------------------------------------------------------
v2 = {
  "id": "ex-h3-frans-u1-v2",
  "hoofdstuk": 1,
  "hoofdstukTitel": "Unité 1 — Poste, like, partage",
  "titel": "Woordenschat 2 · p. 49 (blok E & F) · FR ⇄ NL",
  "vak": "Frans · HAVO 3 (U1)",
  "icoon": "🔤",
  "duurMin": 20,
  "vragen": [

    {
      "type": "mc",
      "vraag": "Wat betekent <b>'la meilleure amie'</b> (p. 49)?",
      "opties": ["de beste vriendin", "de nieuwe klasgenote", "de zus", "de buurvrouw"],
      "antwoord": 0,
      "uitleg": "'La meilleure amie' betekent 'de beste vriendin' (mannelijk: le meilleur ami)."
    },
    {
      "type": "mc",
      "vraag": "Wat is het Franse woord voor <b>'lui'</b> (mannelijk / vrouwelijk, p. 49)?",
      "opties": ["paresseux, -euse", "timide", "égoïste", "intelligent(e)"],
      "antwoord": 0,
      "uitleg": "'Paresseux' (mannelijk) en 'paresseuse' (vrouwelijk) betekenen 'lui'."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Franse woord <b>'méchant(e)'</b> (p. 49) betekent 'lief en aardig'.",
      "antwoord": False,
      "uitleg": "Onwaar. 'Méchant(e)' betekent 'gemeen'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het woord <i>'verlegen'</i> naar het Frans (p. 49): <i>Elle n'ose pas parler, elle est ... .</i>",
      "antwoord": "timide",
      "uitleg": "'Timide' betekent 'verlegen'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent het bijwoord <b>'souvent'</b> (p. 49)?",
      "opties": ["vaak", "zelden", "nooit", "altijd"],
      "antwoord": 0,
      "uitleg": "'Souvent' betekent 'vaak'."
    },
    {
      "type": "mc",
      "vraag": "Hoe zeg je <b>'een keer per week'</b> in het Frans (p. 49)?",
      "opties": ["une fois par semaine", "par an", "en moyenne", "tous les jours"],
      "antwoord": 0,
      "uitleg": "'Une fois par semaine' betekent 'een keer per week'."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Franse werkwoord <b>'bavarder'</b> (p. 49) betekent 'kletsen'.",
      "antwoord": True,
      "uitleg": "Waar. 'Bavarder' betekent gezellig praten / kletsen."
    },
    {
      "type": "invul",
      "vraag": "Vul het juiste werkwoord in (sporten, p. 49): <i>J'aime ... du sport le week-end.</i>",
      "antwoord": "faire",
      "uitleg": "'Faire du sport' is de vaste Franse uitdrukking voor sporten."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent het Franse woord <b>'l'argent'</b> (m, p. 49)?",
      "opties": ["het geld / het zilver", "het goud", "de prijs", "de schat"],
      "antwoord": 0,
      "uitleg": "'L'argent' betekent 'het geld' én 'het zilver'. 'L'or' is goud."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste Franse vertaling voor <b>'duur'</b> (mannelijk en vrouwelijk, p. 49):",
      "opties": ["cher, chère", "pauvre", "mieux", "américain(e)"],
      "antwoord": 0,
      "uitleg": "'Cher' (m) en 'chère' (v) betekenen 'duur'."
    },
    {
      "type": "waaronwaar",
      "vraag": "In het Frans betekent het telwoord <b>'cent'</b> (p. 49) 'duizend'.",
      "antwoord": False,
      "uitleg": "Onwaar. 'Cent' is 100 (honderd). 'Mille' is 1000 (duizend)."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het getal <b>'mille'</b> (p. 49) naar het Nederlands (in letters of cijfers):",
      "antwoord": "duizend|1000",
      "uitleg": "'Mille' is duizend (1000)."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent het Franse werkwoord <b>'savoir'</b> (p. 49)?",
      "opties": ["weten", "verkopen", "bestaan", "bewijzen"],
      "antwoord": 0,
      "uitleg": "'Savoir' betekent 'weten' (bijv. Je sais = Ik weet het)."
    },
    {
      "type": "mc",
      "vraag": "Welk Frans werkwoord betekent <b>'verkopen'</b> (p. 49)?",
      "opties": ["vendre", "payer", "exister", "admirer"],
      "antwoord": 0,
      "uitleg": "'Vendre' betekent 'verkopen'."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Franse woord <b>'mieux'</b> (p. 49) betekent 'beter'.",
      "antwoord": True,
      "uitleg": "Waar. 'Mieux' betekent 'beter'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het woord <i>'de wedstrijd'</i> naar het Frans (p. 49): <i>Il participe à un grand ... .</i>",
      "antwoord": "concours|le concours",
      "uitleg": "'Le concours' is de wedstrijd of competitie."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent het Franse woord <b>'le cerveau'</b> (p. 49)?",
      "opties": ["de hersenen", "de bezoeker", "het hart", "de smaak"],
      "antwoord": 0,
      "uitleg": "'Le cerveau' betekent 'de hersenen'."
    },
    {
      "type": "mc",
      "vraag": "Welk werkwoord betekent <b>'vieren'</b> (p. 49)?",
      "opties": ["fêter", "compter", "prouver", "admirer"],
      "antwoord": 0,
      "uitleg": "'Fêter' betekent 'vieren' (zoals in: fêter un anniversaire)."
    },
    {
      "type": "waaronwaar",
      "vraag": "De uitdrukking <b>'chez des amis'</b> (p. 49) betekent 'bij vrienden thuis'.",
      "antwoord": True,
      "uitleg": "Waar. 'Chez' betekent 'bij ... thuis'."
    },
    {
      "type": "invul",
      "vraag": "Wat betekent de uitdrukking <b>'en moyenne'</b> (p. 49) in het Nederlands?",
      "antwoord": "gemiddeld",
      "uitleg": "'En moyenne' betekent 'gemiddeld'."
    }
  ]
}

# -------------------------------------------------------------
# TOETS 3: Sayfa 50 (Phrases-clés C & G)
# -------------------------------------------------------------
v3 = {
  "id": "ex-h3-frans-u1-v3",
  "hoofdstuk": 1,
  "hoofdstukTitel": "Unité 1 — Poste, like, partage",
  "titel": "Woordenschat 3 · p. 50 (phrases-clés C & G) · FR ⇄ NL",
  "vak": "Frans · HAVO 3 (U1)",
  "icoon": "💬",
  "duurMin": 20,
  "vragen": [

    {
      "type": "mc",
      "vraag": "Hoe vraag je in het Frans: <b>'Wat is de wificode?'</b> (p. 50)?",
      "opties": ["Quel est le code WiFi ?", "Où est le WiFi ?", "Tu as du WiFi ?", "Pourquoi pas de WiFi ?"],
      "antwoord": 0,
      "uitleg": "'Quel est le code WiFi ?' is de letterlijke zin uit C: Parler des réseaux sociaux."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent: <b>'C\'est ... et le mot de passe c\'est ...'</b> (p. 50)?",
      "opties": ["Dat is ... en het wachtwoord is ...", "Dat is mijn gebruikersnaam en e-mail", "Hier is de link en de website", "Dit is mijn telefoonnummer"],
      "antwoord": 0,
      "uitleg": "'Le mot de passe' is het wachtwoord."
    },
    {
      "type": "waaronwaar",
      "vraag": "De vraag <b>'Tu publies beaucoup de photos ?'</b> (p. 50) betekent 'Verwijder je veel foto\'s?'.",
      "antwoord": False,
      "uitleg": "Onwaar. 'Publier' betekent posten of plaatsen."
    },
    {
      "type": "invul",
      "vraag": "Vul het werkwoord in (volgen, p. 50): <i>Tu ... Théo Gordy sur les réseaux sociaux ?</i>",
      "antwoord": "suis",
      "uitleg": "'Tu suis' komt van suivre (volgen): Tu suis Théo Gordy ?"
    },
    {
      "type": "mc",
      "vraag": "Wat betekent het antwoord: <b>'Non, je ne suis pas de stars.'</b> (p. 50)?",
      "opties": ["Nee, ik volg geen sterren (beroemdheden).", "Nee, ik ben zelf geen ster.", "Nee, ik hou niet van muziek.", "Nee, ik heb geen vrienden."],
      "antwoord": 0,
      "uitleg": "'Je ne suis pas de stars' betekent 'ik volg geen sterren' (suivre = volgen)."
    },
    {
      "type": "mc",
      "vraag": "Hoe vraag je: <b>'Wat post je nog meer?'</b> in het Frans (p. 50)?",
      "opties": ["Qu'est-ce que tu publies d'autre ?", "Pourquoi tu publies ça ?", "Quand tu publies une photo ?", "Avec qui tu publies ?"],
      "antwoord": 0,
      "uitleg": "'Qu'est-ce que tu publies d'autre ?' betekent 'Wat post/publiceer je nog meer?'."
    },
    {
      "type": "waaronwaar",
      "vraag": "De zin <b>'Je publie aussi des stories'</b> (p. 50) betekent 'Ik post ook stories'.",
      "antwoord": True,
      "uitleg": "Waar. 'Aussi' betekent 'ook'."
    },
    {
      "type": "invul",
      "vraag": "Vul het ontbrekende woord in voor <i>'Natuurlijk'</i> (p. 50): <i>... sûr, mon compte c'est @duru.</i>",
      "antwoord": "Bien|bien",
      "uitleg": "'Bien sûr' betekent 'natuurlijk'."
    },
    {
      "type": "mc",
      "vraag": "Hoe vraag je: <b>'Wie is je beste vriend?'</b> (p. 50)?",
      "opties": ["Qui est ton meilleur ami ?", "Où est ton meilleur ami ?", "Comment va ton meilleur ami ?", "Quel âge a ton meilleur ami ?"],
      "antwoord": 0,
      "uitleg": "'Qui est ton meilleur ami ?' vraagt naar wie je beste vriend is."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de zin: <b>'Je le connais depuis dix ans.'</b> (p. 50)?",
      "opties": ["Ik ken hem sinds tien jaar.", "Ik zie hem over tien dagen.", "Hij is tien jaar oud.", "We wonen al tien jaar samen."],
      "antwoord": 0,
      "uitleg": "'Depuis dix ans' betekent 'sinds tien jaar'."
    },
    {
      "type": "waaronwaar",
      "vraag": "In de zin <b>'J\'ai rencontré Max au club de sport'</b> (p. 50) heeft de ontmoeting op school plaatsgevonden.",
      "antwoord": False,
      "uitleg": "Onwaar. 'Au club de sport' is op de sportclub."
    },
    {
      "type": "invul",
      "vraag": "Vul het vraagwoord in (Waarom, p. 50): <i>... c'est ton meilleur ami ?</i>",
      "antwoord": "Pourquoi|pourquoi",
      "uitleg": "'Pourquoi' betekent 'waarom'."
    },
    {
      "type": "mc",
      "vraag": "Vertaal: <b>'Il est sympa et on peut parler de tout.'</b> (p. 50):",
      "opties": ["Hij is aardig en we kunnen over alles praten.", "Hij is stil en praat nooit over school.", "Hij is verlegen maar speelt graag mee.", "Hij is gemeen en wil niet luisteren."],
      "antwoord": 0,
      "uitleg": "'Parler de tout' betekent praten over alles."
    },
    {
      "type": "mc",
      "vraag": "Hoe zeg je: <b>'We spelen graag samen online.'</b> in het Frans (p. 50)?",
      "opties": ["On aime jouer en ligne ensemble.", "On déteste les jeux en ligne.", "On joue seulement le week-end.", "On ne joue jamais ensemble."],
      "antwoord": 0,
      "uitleg": "'On aime jouer en ligne ensemble' is de juiste zin uit sectie G."
    },
    {
      "type": "waaronwaar",
      "vraag": "De uitdrukking <b>'On se voit presque tous les jours'</b> (p. 50) betekent 'We zien elkaar bijna elke dag'.",
      "antwoord": True,
      "uitleg": "Waar. 'Tous les jours' = elke dag, 'presque' = bijna."
    },
    {
      "type": "invul",
      "vraag": "Wat betekent het woord <b>'ensemble'</b> in <i>'On aime jouer en ligne ensemble'</i> (p. 50)?",
      "antwoord": "samen",
      "uitleg": "'Ensemble' betekent 'samen'."
    },
    {
      "type": "mc",
      "vraag": "Wat antwoord je als iemand vraagt: <i>'Tu suis Théo Gordy ?'</i> en je kijkt zijn video's (p. 50)?",
      "opties": ["Oui, je regarde ses vidéos.", "Non, je supprime son compte.", "Je ne le connais pas du tout.", "Il habite trop loin."],
      "antwoord": 0,
      "uitleg": "Het voorbeeldantwoord op p. 50 is: 'Oui, je regarde ses vidéos'."
    },
    {
      "type": "mc",
      "vraag": "Hoe zeg je: <b>'Ja, en ik post ook video\'s.'</b> (p. 50)?",
      "opties": ["Oui, et je publie aussi des vidéos.", "Oui, maar je regarde des photos.", "Non, je préfère écouter la radio.", "Je n'ai pas de compte vidéo."],
      "antwoord": 0,
      "uitleg": "'Publier aussi des vidéos' betekent ook video's posten/publiceren."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het vraagwoord <b>'Qui'</b> in <i>'Qui est ton meilleur ami ?'</i> betekent 'Wat'.",
      "antwoord": False,
      "uitleg": "Onwaar. 'Qui' betekent 'wie'. 'Wat' is 'Qu'est-ce que' of 'Que'."
    },
    {
      "type": "invul",
      "vraag": "Vul het ontbrekende woord in: <i>On se voit presque tous les ... (dagen, p. 50).</i>",
      "antwoord": "jours",
      "uitleg": "'Tous les jours' betekent alle dagen / elke dag."
    }
  ]
}

# -------------------------------------------------------------
# TOETS 4: Sayfa 51 (Grammaire & Woordvorming D & H)
# -------------------------------------------------------------
v4 = {
  "id": "ex-h3-frans-u1-v4",
  "hoofdstuk": 1,
  "hoofdstukTitel": "Unité 1 — Poste, like, partage",
  "titel": "Woordenschat 4 · p. 51 (bijvoeglijke naamwoorden & -re werkwoorden) · FR ⇄ NL",
  "vak": "Frans · HAVO 3 (U1)",
  "icoon": "⚙️",
  "duurMin": 20,
  "vragen": [

    {
      "type": "mc",
      "vraag": "Wat is de vrouwelijke vorm van het bijvoeglijk naamwoord <b>'italien'</b> (p. 51)?",
      "opties": ["italienne", "italieuse", "italie", "italive"],
      "antwoord": 0,
      "uitleg": "Bijvoeglijke naamwoorden op -ien krijgen in het vrouwelijk -ienne: italien -> italienne."
    },
    {
      "type": "mc",
      "vraag": "Wat is de vrouwelijke vorm van <b>'heureux'</b> (gelukkig, p. 51)?",
      "opties": ["heureuse", "heureusse", "heureuxte", "heureuve"],
      "antwoord": 0,
      "uitleg": "Bijvoeglijke naamwoorden op -eux krijgen in het vrouwelijk -euse: heureux -> heureuse."
    },
    {
      "type": "waaronwaar",
      "vraag": "De vrouwelijke vorm van <b>'sportif'</b> is volgens de regel op pagina 51 <b>'sportive'</b> (-if wordt -ive).",
      "antwoord": True,
      "uitleg": "Waar. Bijvoeglijke naamwoorden op -if worden -ive: sportif -> sportive."
    },
    {
      "type": "invul",
      "vraag": "Wat is de onregelmatige vrouwelijke vorm van <b>'nouveau'</b> (nieuw, p. 51)?",
      "antwoord": "nouvelle",
      "uitleg": "Nouveau wordt in het vrouwelijk 'nouvelle' (J'ai une nouvelle copine)."
    },
    {
      "type": "mc",
      "vraag": "Wat is de vrouwelijke vorm van <b>'vieux'</b> (oud, p. 51)?",
      "opties": ["vieille", "vieuse", "vieuxe", "vieillarde"],
      "antwoord": 0,
      "uitleg": "Vieux heeft de onregelmatige vrouwelijke vorm 'vieille'."
    },
    {
      "type": "mc",
      "vraag": "Wat is de vrouwelijke vorm van <b>'beau'</b> (mooi, p. 51)?",
      "opties": ["belle", "beause", "beauté", "beauve"],
      "antwoord": 0,
      "uitleg": "Beau wordt in het vrouwelijk 'belle'."
    },
    {
      "type": "waaronwaar",
      "vraag": "In het Frans staat het bijvoeglijk naamwoord <b>'jeune'</b> (jong, p. 51) meestal VÓÓR het zelfstandig naamwoord (zoals: <i>C'est un jeune influenceur</i>).",
      "antwoord": True,
      "uitleg": "Waar. Bon, grand, petit, joli, jeune, vieux, nouveau staan gewoonlijk vóór het zelfstandig naamwoord."
    },
    {
      "type": "invul",
      "vraag": "Vul de juiste vrouwelijke vorm in van <i>bon</i> (p. 51): <i>C'est une ... idée !</i>",
      "antwoord": "bonne",
      "uitleg": "De vrouwelijke vorm van bon is bonne (met dubbel n)."
    },
    {
      "type": "mc",
      "vraag": "Waar hoort het bijvoeglijk naamwoord <b>'français'</b> te staan in: <i>C'est un YouTubeur ...</i> (p. 51)?",
      "opties": ["ACHTER het zelfstandig naamwoord (C'est un YouTubeur français)", "VÓÓR het zelfstandig naamwoord (C'est un français YouTubeur)", "Helemaal aan het begin van de zin", "Dat maakt in het Frans niets uit"],
      "antwoord": 0,
      "uitleg": "Nationaliteiten staan in het Frans altijd achter het zelfstandig naamwoord: un YouTubeur français."
    },
    {
      "type": "mc",
      "vraag": "Welke vaste uitgangen horen bij regelmatige werkwoorden op <b>-re</b> (zoals <i>répondre</i>, p. 51)?",
      "opties": ["-s, -s, -, -ons, -ez, -ent", "-e, -es, -e, -ons, -ez, -ent", "-is, -is, -it, -issons, -issez, -issent", "-x, -x, -t, -ons, -ez, -ent"],
      "antwoord": 0,
      "uitleg": "De stam van een -re werkwoord krijgt: je -s, tu -s, il/elle/on -, nous -ons, vous -ez, ils/elles -ent."
    },
    {
      "type": "waaronwaar",
      "vraag": "Bij <b>il/elle/on</b> krijgt een regelmatig -re werkwoord een extra <b>-t</b> (zoals: <i>il répond-t</i>, p. 51).",
      "antwoord": False,
      "uitleg": "Onwaar. Bij il/elle/on is er GEEN uitgang; er blijft alleen de stam op -d over: il répond, il attend, il vend."
    },
    {
      "type": "invul",
      "vraag": "Vervoeg <b>répondre</b> voor <i>je</i> (p. 51): <i>Je ... au message de mon prof.</i>",
      "antwoord": "réponds|reponds",
      "uitleg": "Je réponds (stam répond + s)."
    },
    {
      "type": "mc",
      "vraag": "Vervoeg <b>attendre</b> (wachten) voor <i>nous</i> (p. 51):",
      "opties": ["nous attendons", "nous attendez", "nous attendent", "nous attends"],
      "antwoord": 0,
      "uitleg": "Nous attendons (stam attend + ons)."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent het regelmatige -re werkwoord <b>'perdre'</b> (p. 51)?",
      "opties": ["verliezen", "antwoorden", "wachten", "horen"],
      "antwoord": 0,
      "uitleg": "'Perdre' betekent 'verliezen' (zoals in: perdre son portable)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het werkwoord <b>'entendre'</b> (p. 51) betekent 'verkopen'.",
      "antwoord": False,
      "uitleg": "Onwaar. 'Entendre' betekent 'horen'. 'Verkopen' is 'vendre'."
    },
    {
      "type": "invul",
      "vraag": "Vervoeg <b>vendre</b> (verkopen) voor <i>ils</i> (p. 51): <i>Ils ... leur maison.</i>",
      "antwoord": "vendent",
      "uitleg": "Ils vendent (stam vend + ent)."
    },
    {
      "type": "mc",
      "vraag": "Hoe vertaal je: <b>'Hij heeft zijn mobieltje verloren'</b> in het Frans (passé composé, p. 51)?",
      "opties": ["Il a perdu son portable.", "Il est perdu son portable.", "Il perd son portable.", "Il avait perdre son portable."],
      "antwoord": 0,
      "uitleg": "Het voorbeeld op p. 51 luidt: 'Il a perdu son portable' (avoir + voltooid deelwoord op -u)."
    },
    {
      "type": "mc",
      "vraag": "Vervoeg <b>défendre</b> voor <i>vous</i> (p. 51):",
      "opties": ["vous défendez", "vous défendons", "vous défendent", "vous défends"],
      "antwoord": 0,
      "uitleg": "Bij vous is de uitgang altijd -ez: vous défendez."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het voltooid deelwoord van regelmatige werkwoorden op -re eindigt in de regel op een <b>-u</b> (zoals <i>perdu, attendu, répondu</i>, p. 51).",
      "antwoord": True,
      "uitleg": "Waar. Regelmatige werkwoorden op -re vormen het voltooid deelwoord op -u: perdre -> perdu, répondre -> répondu."
    },
    {
      "type": "invul",
      "vraag": "Vul het voltooid deelwoord in van <b>attendre</b> (p. 51): <i>J'ai ... pendant dix minutes. (ik heb gewacht)</i>",
      "antwoord": "attendu",
      "uitleg": "Het voltooid deelwoord van attendre is attendu."
    }
  ]
}

# -------------------------------------------------------------
# TOETS 5: Sayfa 48-51 Büyük Seviye Ölçüm Sınavı (Mix)
# -------------------------------------------------------------
v5 = {
  "id": "ex-h3-frans-u1-v5",
  "hoofdstuk": 1,
  "hoofdstukTitel": "Unité 1 — Poste, like, partage",
  "titel": "Eindtoets woordenschat Unité 1 (p. 48-51, mix)",
  "vak": "Frans · HAVO 3 (U1)",
  "icoon": "🏆",
  "duurMin": 25,
  "vragen": [

    {
      "type": "mc",
      "vraag": "Wat betekent <b>'le commentaire'</b> (p. 48)?",
      "opties": ["het commentaar / de reactie", "het e-mailbericht", "de accountnaam", "de internetlink"],
      "antwoord": 0,
      "uitleg": "'Le commentaire' is het commentaar of een geplaatste reactie onder een post."
    },
    {
      "type": "mc",
      "vraag": "Wat is het Franse woord voor <b>'de tijd'</b> (p. 48)?",
      "opties": ["le temps", "la tête", "le truc", "le prix"],
      "antwoord": 0,
      "uitleg": "'Le temps' betekent zowel 'de tijd' als 'het weer'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het woord <i>'de app'</i> naar het Frans (p. 48): <i>J'ai téléchargé une nouvelle ... .</i>",
      "antwoord": "appli|l'appli",
      "uitleg": "'L'appli' (vrouwelijk) is het gangbare Franse woord voor de applicatie / app."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de uitdrukking <b>'avoir besoin de'</b> (p. 48)?",
      "opties": ["nodig hebben", "zin hebben in", "bang zijn voor", "trots zijn op"],
      "antwoord": 0,
      "uitleg": "'Avoir besoin de' betekent 'nodig hebben'."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Franse woord <b>'vieux'</b> (p. 48) betekent 'jong'.",
      "antwoord": False,
      "uitleg": "Onwaar. 'Vieux' betekent 'oud'. 'Jong' is 'jeune'."
    },
    {
      "type": "invul",
      "vraag": "Wat betekent het Franse woord <b>'drôle'</b> (p. 48) in het Nederlands?",
      "antwoord": "grappig|komisch",
      "uitleg": "'Drôle' betekent 'grappig' (synoniem met 'marrant')."
    },
    {
      "type": "mc",
      "vraag": "Hoe zeg je <b>'duizend'</b> in het Frans (p. 49)?",
      "opties": ["mille", "cent", "un million", "dix"],
      "antwoord": 0,
      "uitleg": "'Mille' is duizend (1000). 'Cent' is honderd (100)."
    },
    {
      "type": "mc",
      "vraag": "Wat is de Franse vertaling van <b>'de beste vriendin'</b> (p. 49)?",
      "opties": ["la meilleure amie", "le meilleur ami", "la nouvelle copine", "la petite sœur"],
      "antwoord": 0,
      "uitleg": "'La meilleure amie' is de beste vriendin."
    },
    {
      "type": "waaronwaar",
      "vraag": "Iemand die <b>'égoïste'</b> is (p. 49) denkt voornamelijk aan zichzelf.",
      "antwoord": True,
      "uitleg": "Waar. 'Égoïste' betekent 'egoïstisch'."
    },
    {
      "type": "invul",
      "vraag": "Vul het juiste werkwoord in (televisie kijken, p. 49): <i>Elle préfère ... la télé.</i>",
      "antwoord": "regarder",
      "uitleg": "'Regarder la télé' betekent televisie kijken."
    },
    {
      "type": "mc",
      "vraag": "Welk Frans werkwoord betekent <b>'weten'</b> (p. 49)?",
      "opties": ["savoir", "vendre", "dire", "penser"],
      "antwoord": 0,
      "uitleg": "'Savoir' betekent 'weten'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de vraag: <b>'Pourquoi c\'est ton meilleur ami ?'</b> (p. 50)?",
      "opties": ["Waarom is het je beste vriend?", "Wie is je beste vriend?", "Hoe heet je beste vriend?", "Waar woont je beste vriend?"],
      "antwoord": 0,
      "uitleg": "'Pourquoi' betekent 'waarom'."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Franse woord <b>'Bienvenue'</b> (p. 48) betekent 'tot ziens'.",
      "antwoord": False,
      "uitleg": "Onwaar. 'Bienvenue' betekent 'welkom'."
    },
    {
      "type": "invul",
      "vraag": "Vul het ontbrekende woord in voor <i>'wachtwoord'</i> (p. 50): <i>Quel est ton ... de passe ?</i>",
      "antwoord": "mot",
      "uitleg": "'Le mot de passe' is het wachtwoord."
    },
    {
      "type": "mc",
      "vraag": "Hoe vertaal je het Nederlandse woord <b>'samen'</b> naar het Frans (p. 50)?",
      "opties": ["ensemble", "souvent", "pourtant", "presque"],
      "antwoord": 0,
      "uitleg": "'Ensemble' betekent 'samen' (bijv. On aime jouer en ligne ensemble)."
    },
    {
      "type": "mc",
      "vraag": "Wat is de vrouwelijke vorm van <b>'bon'</b> (goed/lekker, p. 51)?",
      "opties": ["bonne", "bonse", "bonte", "bonive"],
      "antwoord": 0,
      "uitleg": "De vrouwelijke vorm van 'bon' is 'bonne'."
    },
    {
      "type": "waaronwaar",
      "vraag": "In de zin <i>'C\'est un beau garçon'</i> staat het bijvoeglijk naamwoord <b>'beau'</b> vóór het zelfstandig naamwoord (p. 51).",
      "antwoord": True,
      "uitleg": "Waar. 'Beau' hoort bij de uitzonderingen die vóór het zelfstandig naamwoord staan."
    },
    {
      "type": "invul",
      "vraag": "Vervoeg <b>répondre</b> voor <i>tu</i> (p. 51): <i>Tu ... rapidement à mes messages ?</i>",
      "antwoord": "réponds|reponds",
      "uitleg": "Bij 'tu' krijgt een -re werkwoord de uitgang -s: tu réponds."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent het Franse zelfstandig naamwoord <b>'le cerveau'</b> (p. 49)?",
      "opties": ["de hersenen", "de wedstrijd", "de bezoeker", "het hart"],
      "antwoord": 0,
      "uitleg": "'Le cerveau' betekent 'de hersenen'."
    },
    {
      "type": "mc",
      "vraag": "Hoe vraag je in het Frans informeel: <b>'Heb je Insta?'</b> (p. 50)?",
      "opties": ["Tu as Insta ?", "Où est Insta ?", "Tu vends Insta ?", "Tu penses à Insta ?"],
      "antwoord": 0,
      "uitleg": "'Tu as Insta ?' is de letterlijke vraag uit sectie C van pagina 50."
    }
  ]
}

if __name__ == "__main__":
    write_examen("examen_u1_vocab_1.js", v1)
    write_examen("examen_u1_vocab_2.js", v2)
    write_examen("examen_u1_vocab_3.js", v3)
    write_examen("examen_u1_vocab_4.js", v4)
    write_examen("examen_u1_vocab_5.js", v5)
    print("\n🎉 Alle 5 Unité 1 Vocabulaire Toetsen succesvol aangemaakt!")

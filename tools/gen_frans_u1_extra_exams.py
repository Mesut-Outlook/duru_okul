#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate 5 Additional French Vocabulary Exams for Unité 1 (HAVO 3):
- examen_u1_vocab_6.js: Woordenschat 6 · Signaalwoorden, Voorzetsels, Getallen & Tijd (p. 48-49)
- examen_u1_vocab_7.js: Woordenschat 7 · Karaktereigenschappen, Mensen & Vriendschap (p. 48-49)
- examen_u1_vocab_8.js: Woordenschat 8 · Werkwoorden, Apparaten & Communicatie (p. 48-51)
- examen_u1_vocab_9.js: Woordenschat 9 · Phrases-clés C & G & Social Media Context (p. 50)
- examen_u1_vocab_10.js: Woordenschat 10 · Examentraining HAVO 3 Unité 1 (Grote Mix Toets)
"""
import os, json, random, re

DATA_DIR = "/home/mesuto/Documents/PROJELER/duru_okul/havo3/frans/js/data"
os.makedirs(DATA_DIR, exist_ok=True)

def balance_mc(questions):
    mc_indices = [i for i, q in enumerate(questions) if q.get("type") == "mc"]
    rnd = random.Random(questions[0].get("vraag", "") if questions else "")
    target_pattern = []
    while len(target_pattern) < len(mc_indices):
        blok = [0, 1, 2, 3]
        rnd.shuffle(blok)
        target_pattern += blok
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
    content = f"/* Proeftoets {titel}\n   Grandes Lignes 3 HAVO Unite {hf} */\n"
    content += f"DURU.registerExamen({dumped});\n"
    with open(path, "w", encoding="utf-8") as out:
        out.write(content)
    print(f"  [OK] Frans Vocab Examen saved: {filename} ({len(data['vragen'])} vragen)")

# -------------------------------------------------------------
# TOETS 6: Signaalwoorden, Voorzetsels, Getallen & Tijd (p. 48-49)
# -------------------------------------------------------------
v6 = {
  "id": "ex-h3-frans-u1-v6",
  "hoofdstuk": 1,
  "hoofdstukTitel": "Unité 1 — Poste, like, partage",
  "titel": "Woordenschat 6 · Signaalwoorden, Voorzetsels & Tijd · FR ⇄ NL",
  "vak": "Frans · HAVO 3 (U1)",
  "icoon": "⏱️",
  "duurMin": 20,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat betekent het Franse signaalwoord <b>'pourtant'</b> in de zin: <i>Il a un portable, pourtant il n'envoie jamais de message</i> (p. 48)?",
      "opties": ["toch / echter", "daarom / aldus", "omdat / want", "nooit / nergens"],
      "antwoord": 0,
      "uitleg": "'Pourtant' betekent 'toch' of 'echter' en geeft een tegenstelling aan."
    },
    {
      "type": "mc",
      "vraag": "Welk Frans voorzetsel betekent <b>'achter'</b> (tegenovergestelde van devant, p. 48)?",
      "opties": ["derrière", "devant", "près de", "dans"],
      "antwoord": 0,
      "uitleg": "'Derrière' betekent 'achter'. 'Devant' betekent 'voor'."
    },
    {
      "type": "waaronwaar",
      "vraag": "De Franse uitdrukking <b>'grâce à'</b> (p. 48) betekent 'ondanks'.",
      "antwoord": False,
      "uitleg": "Onwaar. 'Grâce à' betekent 'dankzij' (bijv. grâce aux réseaux sociaux)."
    },
    {
      "type": "invul",
      "vraag": "Vul het juiste Franse woord in voor <i>dichtbij</i> (p. 48): <i>J'habite ... de mon collège.</i>",
      "antwoord": "près|pres",
      "uitleg": "'Près de' betekent 'dichtbij'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de Franse tijdsaanduiding <b>'une fois par semaine'</b> (p. 49)?",
      "opties": ["een keer per week", "zeven dagen per maand", "een keer per jaar", "elke dag van de week"],
      "antwoord": 0,
      "uitleg": "'Une fois par semaine' betekent 'een keer per week' ('semaine' = week)."
    },
    {
      "type": "mc",
      "vraag": "Vertaal het Franse telwoord <b>'cent'</b> (p. 49) naar het Nederlands:",
      "opties": ["honderd", "duizend", "tien", "miljoen"],
      "antwoord": 0,
      "uitleg": "'Cent' is honderd (100). 'Mille' is duizend (1000)."
    },
    {
      "type": "waaronwaar",
      "vraag": "De uitdrukking <b>'en moyenne'</b> (p. 49) betekent 'in het midden van de week'.",
      "antwoord": False,
      "uitleg": "Onwaar. 'En moyenne' is een vaste wiskundige term en betekent 'gemiddeld'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het signaalwoord <i>bijna</i> naar het Frans (p. 48): <i>Il est ... minuit, je dois me coucher.</i>",
      "antwoord": "presque",
      "uitleg": "'Presque' betekent 'bijna' (bijv. presque tous les jours = bijna elke dag)."
    },
    {
      "type": "mc",
      "vraag": "Hoeveel is <b>'un million'</b> in cijfers geschreven (p. 49)?",
      "opties": ["1.000.000", "100.000", "1.000", "10.000.000"],
      "antwoord": 0,
      "uitleg": "'Un million' is één miljoen (1.000.000)."
    },
    {
      "type": "mc",
      "vraag": "Welke Franse uitdrukking betekent <b>'per jaar'</b> (p. 49)?",
      "opties": ["par an", "par semaine", "par mois", "par jour"],
      "antwoord": 0,
      "uitleg": "'Par an' betekent 'per jaar' ('an' = jaar)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Franse voorzetsel <b>'devant'</b> (p. 48) geeft een plaats aan en betekent 'voor'.",
      "antwoord": True,
      "uitleg": "Waar. 'Devant' betekent 'voor' (in de ruimte), zoals in 'devant l'école'."
    },
    {
      "type": "invul",
      "vraag": "Vul het ontbrekende Franse woord in voor <i>nu</i> (p. 48): <i>Je dois éteindre mon écran ... .</i>",
      "antwoord": "maintenant",
      "uitleg": "'Maintenant' is het Franse woord voor 'nu'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de tijdsuitdrukking <b>'tous les jours'</b> in Unité 1 (p. 50)?",
      "opties": ["elke dag / alle dagen", "alleen op schooldagen", "om de twee weken", "in het weekend"],
      "antwoord": 0,
      "uitleg": "'Tous les jours' betekent 'alle dagen' oftewel 'elke dag'."
    },
    {
      "type": "mc",
      "vraag": "Welk Frans bijwoord van frequentie betekent <b>'vaak'</b> (p. 49)?",
      "opties": ["souvent", "toujours", "jamais", "rarement"],
      "antwoord": 0,
      "uitleg": "'Souvent' betekent 'vaak'. 'Toujours' betekent 'altijd' en 'jamais' betekent 'nooit'."
    },
    {
      "type": "waaronwaar",
      "vraag": "In het Frans betekent <b>'le temps'</b> (p. 48) uitsluitend 'het horloge'.",
      "antwoord": False,
      "uitleg": "Onwaar. 'Le temps' betekent 'de tijd' of 'het weer'. Een horloge is 'une montre'."
    },
    {
      "type": "invul",
      "vraag": "Welk getal ontbreekt in letters (duizend, p. 49): <i>Cette vidéo a dépassé ... vues sur TikTok.</i>",
      "antwoord": "mille",
      "uitleg": "'Mille' is het Franse getal voor duizend (1000)."
    },
    {
      "type": "mc",
      "vraag": "Wat is het juiste antoniem (tegenovergestelde) van <b>'derrière'</b> (achter) op pagina 48?",
      "opties": ["devant", "près de", "sous", "sur"],
      "antwoord": 0,
      "uitleg": "'Devant' (voor) is het tegenovergestelde van 'derrière' (achter)."
    },
    {
      "type": "mc",
      "vraag": "Hoe vertaal je: <i>'Grâce aux réseaux sociaux, je reste en contact avec mes amis'</i> (p. 48)?",
      "opties": ["Dankzij de sociale netwerken blijf ik in contact met mijn vrienden.", "Ondanks de sociale media spreek ik mijn vrienden nooit.", "Vanwege het internet heb ik geen vrienden meer.", "Zonder sociale netwerken kan ik mijn vrienden niet bellen."],
      "antwoord": 0,
      "uitleg": "'Grâce aux' betekent 'dankzij de' en 'rester en contact' betekent 'in contact blijven'."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Franse woordje <b>'maintenant'</b> (p. 48) betekent 'soms'.",
      "antwoord": False,
      "uitleg": "Onwaar. 'Maintenant' betekent 'nu'. 'Soms' is 'parfois' of 'quelquefois'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het woord <i>vaak</i> naar het Frans (p. 49): <i>Nous bavardons ... pendant la récréation.</i>",
      "antwoord": "souvent",
      "uitleg": "'Souvent' betekent 'vaak'."
    }
  ]
}

# -------------------------------------------------------------
# TOETS 7: Karaktereigenschappen, Mensen & Vriendschap (p. 48-49)
# -------------------------------------------------------------
v7 = {
  "id": "ex-h3-frans-u1-v7",
  "hoofdstuk": 1,
  "hoofdstukTitel": "Unité 1 — Poste, like, partage",
  "titel": "Woordenschat 7 · Karaktereigenschappen & Vriendschap · FR ⇄ NL",
  "vak": "Frans · HAVO 3 (U1)",
  "icoon": "🤝",
  "duurMin": 20,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Iemand die niet makkelijk praat en snel bloost noem je in het Frans (p. 49):",
      "opties": ["timide", "égoïste", "bavard", "drôle"],
      "antwoord": 0,
      "uitleg": "'Timide' betekent 'verlegen'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent het Franse zelfstandig naamwoord <b>'la tête'</b> (p. 48)?",
      "opties": ["het hoofd", "de hand", "het hart", "de stem"],
      "antwoord": 0,
      "uitleg": "'La tête' betekent 'het hoofd'."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een persoon die <b>'paresseux'</b> is (p. 49) staat 's ochtends graag heel vroeg op om hard te trainen.",
      "antwoord": False,
      "uitleg": "Onwaar. 'Paresseux' betekent 'lui' (iemand die niet van werken of inspanning houdt)."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het bijvoeglijk naamwoord <i>slim / intelligent</i> naar het Frans in de vrouwelijke vorm (p. 49): <i>Elle réussit tous ses examens, elle est très ... .</i>",
      "antwoord": "intelligente",
      "uitleg": "De vrouwelijke vorm van 'intelligent' krijgt een -e: 'intelligente'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de Franse eigenschap <b>'méchant(e)'</b> (p. 49)?",
      "opties": ["gemeen / vals", "aardig / attent", "eerlijk / betrouwbaar", "nieuwsgierig"],
      "antwoord": 0,
      "uitleg": "'Méchant' (vrouwelijk: méchante) betekent 'gemeen'."
    },
    {
      "type": "mc",
      "vraag": "Iemand met <b>'le sens de l'humour'</b> (p. 48) bezit:",
      "opties": ["een goed gevoel voor humor", "een grote muziekkennis", "een snelle internetverbinding", "veel volgers op social media"],
      "antwoord": 0,
      "uitleg": "'Le sens de l'humour' betekent letterlijk 'het gevoel voor humor'."
    },
    {
      "type": "waaronwaar",
      "vraag": "In het Frans zijn de woorden <b>'marrant'</b> en <b>'drôle'</b> (p. 48-49) synoniemen van elkaar.",
      "antwoord": True,
      "uitleg": "Waar. Zowel 'marrant' als 'drôle' betekent 'grappig'."
    },
    {
      "type": "invul",
      "vraag": "Vul de mannelijke vorm in van het woord <i>lui</i> (p. 49): <i>Il passe tout son samedi sur le canapé, il est ... .</i>",
      "antwoord": "paresseux",
      "uitleg": "'Paresseux' is de mannelijke vorm voor 'lui' (vrouwelijk: paresseuse)."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent <b>'les gens'</b> in de zin: <i>Beaucoup de gens partagent des vidéos en ligne</i> (p. 48)?",
      "opties": ["de mensen", "de leraren", "de buren", "de kinderen"],
      "antwoord": 0,
      "uitleg": "'Les gens' (mannelijk meervoud) betekent 'de mensen'."
    },
    {
      "type": "mc",
      "vraag": "Wat is de juiste vrouwelijke vorm van <b>'paresseux'</b> (p. 49)?",
      "opties": ["paresseuse", "paresseuxte", "paressante", "paresse"],
      "antwoord": 0,
      "uitleg": "Bijvoeglijke naamwoorden op -eux worden -euse: paresseux -> paresseuse."
    },
    {
      "type": "waaronwaar",
      "vraag": "Iemand die <b>'égoïste'</b> is (p. 49) deelt altijd al zijn bezittingen en denkt nooit aan zichzelf.",
      "antwoord": False,
      "uitleg": "Onwaar. Een 'égoïste' is egoïstisch en denkt juist voornamelijk aan zichzelf."
    },
    {
      "type": "invul",
      "vraag": "Vertaal de activiteit <i>kletsen</i> naar het Franse werkwoord in het hele werkwoord (p. 49): <i>Nous aimons ... pendant la pause.</i>",
      "antwoord": "bavarder",
      "uitleg": "'Bavarder' betekent kletsen / babbelen."
    },
    {
      "type": "mc",
      "vraag": "Hoe zeg je <b>'mijn beste vriend'</b> (mannelijk) in het Frans (p. 49)?",
      "opties": ["mon meilleur ami", "la meilleure amie", "mon nouveau copain", "mon cher voisin"],
      "antwoord": 0,
      "uitleg": "'Mon meilleur ami' is de mannelijke vorm (vrouwelijk: ma meilleure amie)."
    },
    {
      "type": "mc",
      "vraag": "Welke Franse uitdrukking betekent <b>'nodig hebben'</b> in: <i>J'ai besoin de calme</i> (p. 48)?",
      "opties": ["avoir besoin de", "avoir peur de", "avoir envie de", "avoir l'air de"],
      "antwoord": 0,
      "uitleg": "'Avoir besoin de' betekent 'nodig hebben'."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Franse woord <b>'la meilleure amie'</b> (p. 49) verwijst naar een jongen die je beste vriend is.",
      "antwoord": False,
      "uitleg": "Onwaar. 'La meilleure amie' is vrouwelijk (de beste vriendin); voor een jongen gebruik je 'le meilleur ami'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het woord <i>gemeen</i> naar het Frans (mannelijke vorm, p. 49): <i>Ce personnage dans le film est très ... .</i>",
      "antwoord": "méchant|mechant",
      "uitleg": "'Méchant' betekent 'gemeen' (vrouwelijk: méchante)."
    },
    {
      "type": "mc",
      "vraag": "Waar hebben de vrienden elkaar ontmoet in de zin: <i>'J'ai rencontré Lucas au club de sport'</i> (p. 49-50)?",
      "opties": ["op de sportclub", "op het schoolplein", "in het ziekenhuis", "bij vrienden thuis"],
      "antwoord": 0,
      "uitleg": "'Au club de sport' betekent 'op de sportclub'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent <b>'chez des amis'</b> in: <i>Samedi soir, nous allons dormir chez des amis</i> (p. 49)?",
      "opties": ["bij vrienden (thuis)", "zonder vrienden", "met vreemde mensen", "op het sportveld"],
      "antwoord": 0,
      "uitleg": "'Chez des amis' betekent 'bij vrienden thuis' ('chez' = bij ... thuis)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Franse werkwoord <b>'bavarder'</b> (p. 49) betekent 'vechten met klasgenoten'.",
      "antwoord": False,
      "uitleg": "Onwaar. 'Bavarder' betekent 'kletsen' of 'gezellig praten'."
    },
    {
      "type": "invul",
      "vraag": "Vul het Franse woord in voor <i>de mensen</i> (p. 48): <i>Tous les ... regardent le spectacle.</i>",
      "antwoord": "gens",
      "uitleg": "'Les gens' betekent 'de mensen'."
    }
  ]
}

# -------------------------------------------------------------
# TOETS 8: Werkwoorden, Apparaten & Communicatie (p. 48-51)
# -------------------------------------------------------------
v8 = {
  "id": "ex-h3-frans-u1-v8",
  "hoofdstuk": 1,
  "hoofdstukTitel": "Unité 1 — Poste, like, partage",
  "titel": "Woordenschat 8 · Werkwoorden & Communicatie · FR ⇄ NL",
  "vak": "Frans · HAVO 3 (U1)",
  "icoon": "💻",
  "duurMin": 20,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat betekent het Franse werkwoord <b>'utiliser'</b> (p. 48)?",
      "opties": ["gebruiken", "repareren", "verkopen", "verliezen"],
      "antwoord": 0,
      "uitleg": "'Utiliser' betekent 'gebruiken' (bijv. utiliser une application)."
    },
    {
      "type": "mc",
      "vraag": "Welk werkwoord betekent <b>'vergeten'</b> in: <i>N'oublie pas de recharger ton portable</i> (p. 48)?",
      "opties": ["oublier", "arrêter", "garder", "montrer"],
      "antwoord": 0,
      "uitleg": "'Oublier' betekent 'vergeten'. 'Arrêter' betekent 'stoppen'."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Franse werkwoord <b>'télécharger'</b> (p. 48) betekent een foto of bestand downloaden.",
      "antwoord": True,
      "uitleg": "Waar. 'Télécharger' betekent 'downloaden' (of uploaden)."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het Franse werkwoord <i>denken</i> (p. 48) in de ik-vorm: <i>Je ... que c'est une excellente idée.</i>",
      "antwoord": "pense",
      "uitleg": "'Penser' betekent 'denken' (je pense = ik denk)."
    },
    {
      "type": "mc",
      "vraag": "Wat is de betekenis van het Franse werkwoord <b>'montrer'</b> (blauw blok, p. 48)?",
      "opties": ["laten zien / tonen", "verbergen / verstoppen", "verwijderen", "tekenen"],
      "antwoord": 0,
      "uitleg": "'Montrer' betekent 'laten zien' of 'tonen'."
    },
    {
      "type": "mc",
      "vraag": "Welk Frans werkwoord betekent <b>'bewaren'</b> (blauw blok, p. 48)?",
      "opties": ["garder", "donner", "oublier", "perdre"],
      "antwoord": 0,
      "uitleg": "'Garder' betekent 'bewaren' of 'houden'."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Franse werkwoord <b>'payer'</b> (p. 48) betekent 'bedanken'.",
      "antwoord": False,
      "uitleg": "Onwaar. 'Payer' betekent 'betalen' (bijv. payer l'addition). 'Bedanken' is 'remercier'."
    },
    {
      "type": "invul",
      "vraag": "Vul het juiste werkwoord in (stoppen, p. 48): <i>Tu dois ... de regarder ton écran tard le soir.</i>",
      "antwoord": "arrêter|arreter",
      "uitleg": "'Arrêter' betekent 'stoppen' of 'ophouden'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent het regelmatige -re werkwoord <b>'entendre'</b> (p. 51)?",
      "opties": ["horen", "wachten", "verkopen", "antwoorden"],
      "antwoord": 0,
      "uitleg": "'Entendre' betekent 'horen'. Verwar dit niet met 'attendre' (wachten)!"
    },
    {
      "type": "mc",
      "vraag": "Vervoeg <b>vendre</b> (verkopen) voor <i>nous</i> (p. 51):",
      "opties": ["nous vendons", "nous vendez", "nous vendent", "nous vends"],
      "antwoord": 0,
      "uitleg": "Stam 'vend' + uitgang '-ons' = 'nous vendons'."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het werkwoord <b>'savoir'</b> (p. 49) betekent 'schrijven'.",
      "antwoord": False,
      "uitleg": "Onwaar. 'Savoir' betekent 'weten' (bijv. je sais = ik weet het). 'Schrijven' is 'écrire'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het werkwoord <i>antwoorden</i> in het hele werkwoord naar het Frans (p. 51): <i>Il faut ... rapidement à ce mail.</i>",
      "antwoord": "répondre|repondre",
      "uitleg": "'Répondre' is het regelmatige -re werkwoord voor 'antwoorden'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent het werkwoord <b>'fêter'</b> in: <i>Nous allons fêter la fin des examens</i> (p. 49)?",
      "opties": ["vieren", "vergeten", "herhalen", "studeren"],
      "antwoord": 0,
      "uitleg": "'Fêter' betekent 'vieren' (zoals in 'fêter un anniversaire')."
    },
    {
      "type": "mc",
      "vraag": "Welke Franse zin betekent: <b>'Ik heb mijn mobieltje verloren'</b> (passé composé, p. 51)?",
      "opties": ["J'ai perdu mon portable.", "Je suis perdu mon portable.", "J'avais perdre mon portable.", "Je perds mon portable."],
      "antwoord": 0,
      "uitleg": "Passé composé van perdre: avoir (j'ai) + voltooid deelwoord op -u (perdu) = 'J'ai perdu mon portable'."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het werkwoord <b>'exister'</b> (p. 49) betekent 'bestaan'.",
      "antwoord": True,
      "uitleg": "Waar. 'Exister' betekent 'bestaan' (bijv. ce site n'existe plus)."
    },
    {
      "type": "invul",
      "vraag": "Vervoeg <b>attendre</b> voor <i>il</i> in de tegenwoordige tijd (p. 51): <i>Il ... le bus devant l'école.</i>",
      "antwoord": "attend",
      "uitleg": "Bij il/elle/on heeft een -re werkwoord géén uitgang; er blijft alleen de stam op -d over: 'il attend'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent <b>'travailler'</b> in: <i>Mon père travaille dans un bureau</i> (p. 48)?",
      "opties": ["werken", "reizen", "slapen", "ontspannen"],
      "antwoord": 0,
      "uitleg": "'Travailler' betekent 'werken'."
    },
    {
      "type": "mc",
      "vraag": "Welk Frans werkwoord betekent <b>'zeggen'</b> (p. 48)?",
      "opties": ["dire", "penser", "écouter", "regarder"],
      "antwoord": 0,
      "uitleg": "'Dire' betekent 'zeggen' (bijv. Qu'est-ce que tu dis ?)."
    },
    {
      "type": "waaronwaar",
      "vraag": "De passé composé van regelmatige -re werkwoorden zoals <i>perdre</i> wordt gevormd met het hulpwerkwoord <b>être</b> (zoals in: <i>Il est perdu son portable</i>).",
      "antwoord": False,
      "uitleg": "Onwaar. Regelmatige werkwoorden op -re vormen de passé composé met 'avoir': 'Il a perdu son portable'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het werkwoord <i>betalen</i> in het hele werkwoord naar het Frans (p. 48): <i>Qui va ... l'addition au café ?</i>",
      "antwoord": "payer",
      "uitleg": "'Payer' betekent 'betalen'."
    }
  ]
}

# -------------------------------------------------------------
# TOETS 9: Phrases-clés C & G & Social Media Context (p. 50)
# -------------------------------------------------------------
v9 = {
  "id": "ex-h3-frans-u1-v9",
  "hoofdstuk": 1,
  "hoofdstukTitel": "Unité 1 — Poste, like, partage",
  "titel": "Woordenschat 9 · Phrases-clés C & G (Dialogen & Socials) · FR ⇄ NL",
  "vak": "Frans · HAVO 3 (U1)",
  "icoon": "📱",
  "duurMin": 20,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Iemand vraagt: <i>Tu as Insta ?</i> Wat is het juiste voorbeeldantwoord uit de phrases-clés (p. 50)?",
      "opties": ["Bien sûr, mon compte c'est @alex.", "Non, j'ai oublié mon adresse.", "Oui, le train arrive à dix heures.", "C'est un secret d'État."],
      "antwoord": 0,
      "uitleg": "Het vaste voorbeeldantwoord op p. 50 luidt: 'Bien sûr, mon compte c'est ...'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de vraag: <b>'Quel est le code WiFi ?'</b> als je die in een café stelt (p. 50)?",
      "opties": ["Wat is de wificode?", "Werkt de computer?", "Waar kan ik mijn telefoon opladen?", "Hoeveel kost een kopje koffie?"],
      "antwoord": 0,
      "uitleg": "'Quel est le code WiFi ?' vraagt letterlijk naar de code voor het draadloze internet."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Franse antwoord <b>'Je ne suis pas de stars'</b> (p. 50) betekent 'Ik ben zelf geen filmster'.",
      "antwoord": False,
      "uitleg": "Onwaar. 'Je ne suis pas' komt hier van het werkwoord 'suivre' (volgen): 'Ik volg geen sterren'."
    },
    {
      "type": "invul",
      "vraag": "Vul het Franse woord in voor <i>sinds / al</i> in een tijdsduur (p. 50): <i>Je connais mon meilleur ami ... trois ans.</i>",
      "antwoord": "depuis",
      "uitleg": "'Depuis' betekent 'sinds' of 'al gedurende'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de uitdrukking: <b>'on peut parler de tout'</b> (p. 50)?",
      "opties": ["we kunnen over alles praten", "we spreken nooit met elkaar", "we mogen niet praten in de les", "iedereen praat tegelijkertijd"],
      "antwoord": 0,
      "uitleg": "'Parler de tout' betekent letterlijk 'over alles praten'."
    },
    {
      "type": "mc",
      "vraag": "Hoe zeg je in het Frans: <b>'Ik post ook stories'</b> (p. 50)?",
      "opties": ["Je publie aussi des stories.", "Je supprime mes stories.", "Je ne regarde jamais de stories.", "J'ai oublié mes stories."],
      "antwoord": 0,
      "uitleg": "'Je publie aussi des stories' betekent 'ik post/plaats ook stories'."
    },
    {
      "type": "waaronwaar",
      "vraag": "In de zin <b>'On aime jouer en ligne ensemble'</b> (p. 50) betekent 'en ligne' dat je offline een bordspel speelt.",
      "antwoord": False,
      "uitleg": "Onwaar. 'En ligne' betekent 'online' via het internet."
    },
    {
      "type": "invul",
      "vraag": "Vul de juiste persoonsvorm in van het werkwoord <i>publier</i> (posten/plaatsen, p. 50): <i>Tu ... beaucoup de photos sur ton profil ?</i>",
      "antwoord": "publies",
      "uitleg": "Bij 'tu' eindigt een regelmatig werkwoord op -er op -es: 'tu publies'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de vraag: <b>'Qu\'est-ce que tu publies d\'autre ?'</b> (p. 50)?",
      "opties": ["Wat post je nog meer?", "Waarom post je niets?", "Wanneer heb je dat gepost?", "Wie heeft die reactie geplaatst?"],
      "antwoord": 0,
      "uitleg": "'Qu'est-ce que tu publies d'autre ?' betekent 'Wat post/publiceer je nog meer?'."
    },
    {
      "type": "mc",
      "vraag": "Hoe vraag je in het Frans aan iemand: <b>'Volg je Théo Gordy ?'</b> (p. 50)?",
      "opties": ["Tu suis Théo Gordy ?", "Tu aimes Théo Gordy ?", "Tu connais Théo Gordy ?", "Tu cherches Théo Gordy ?"],
      "antwoord": 0,
      "uitleg": "'Tu suis' (van het werkwoord suivre) betekent 'jij volgt'."
    },
    {
      "type": "waaronwaar",
      "vraag": "De zin <b>'C\'est ... et le mot de passe c\'est ...'</b> (p. 50) geeft de gebruikersnaam en het wachtwoord van een account of wifi aan.",
      "antwoord": True,
      "uitleg": "Waar. 'Le mot de passe' is het wachtwoord."
    },
    {
      "type": "invul",
      "vraag": "Vul de juiste voorzetselcombinatie in voor <i>op de sportclub</i> (p. 49-50): <i>J'ai rencontré Lucas ... club de sport.</i>",
      "antwoord": "au",
      "uitleg": "'Au club de sport' (à + le = au) betekent 'op de sportclub'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de Franse zin: <b>'Je le connais depuis dix ans'</b> (p. 50)?",
      "opties": ["Ik ken hem sinds tien jaar.", "Hij is tien jaar oud.", "Ik spreek hem over tien dagen.", "We hebben elkaar tien keer gezien."],
      "antwoord": 0,
      "uitleg": "'Depuis dix ans' betekent 'sinds tien jaar'."
    },
    {
      "type": "mc",
      "vraag": "Welk antwoord past logisch bij de vraag: <i>Pourquoi c'est ton meilleur ami ?</i> (p. 50)?",
      "opties": ["Il est sympa et on peut parler de tout.", "Il habite dans une autre ville.", "Il a perdu son portable.", "Il déteste les jeux vidéo."],
      "antwoord": 0,
      "uitleg": "'Il est sympa et on peut parler de tout' is de voorbeeldreden uit sectie G op pagina 50."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het werkwoord <b>'suivre'</b> in <i>'Tu suis cette influenceuse ?'</i> betekent 'blokkeren'.",
      "antwoord": False,
      "uitleg": "Onwaar. 'Suivre' betekent 'volgen'."
    },
    {
      "type": "invul",
      "vraag": "Vul het Franse woord in voor <i>account</i> (p. 50): <i>Mon ... sur Instagram s'appelle @duru.</i>",
      "antwoord": "compte|mon compte",
      "uitleg": "'Le compte' is het Franse woord voor 'het account'."
    },
    {
      "type": "mc",
      "vraag": "Hoe zeg je in het Frans tegen iemand: <b>'Veel plezier!'</b> (p. 48)?",
      "opties": ["Amuse-toi bien !", "À plus !", "Bienvenue !", "J'y vais !"],
      "antwoord": 0,
      "uitleg": "'Amuse-toi bien !' betekent 'veel plezier!'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de informele Franse afscheidsgroet <b>'à plus'</b> (p. 48)?",
      "opties": ["tot later / doei", "tot gisteren", "vaarwel voor altijd", "goedemorgen"],
      "antwoord": 0,
      "uitleg": "'À plus' (afkorting van 'à plus tard') betekent 'tot later'."
    },
    {
      "type": "waaronwaar",
      "vraag": "De begroeting <b>'Bienvenue'</b> (p. 48) betekent in het Frans 'Goedenacht'.",
      "antwoord": False,
      "uitleg": "Onwaar. 'Bienvenue' betekent 'welkom'. 'Goedenacht' is 'bonne nuit'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal de uitdrukking <i>tot later</i> naar het Frans (p. 48): <i>Je dois partir maintenant, ... !</i>",
      "antwoord": "à plus|a plus",
      "uitleg": "'À plus' betekent 'tot later'."
    }
  ]
}

# -------------------------------------------------------------
# TOETS 10: Grote Examentraining HAVO 3 Unité 1 (Mix p. 48-51)
# -------------------------------------------------------------
v10 = {
  "id": "ex-h3-frans-u1-v10",
  "hoofdstuk": 1,
  "hoofdstukTitel": "Unité 1 — Poste, like, partage",
  "titel": "Woordenschat 10 · Grote Examentraining Unité 1 (HAVO 3 Mix)",
  "vak": "Frans · HAVO 3 (U1)",
  "icoon": "🎓",
  "duurMin": 25,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat betekent het woord <b>'l'addition'</b> (v) wanneer je iets drinkt op een Frans terras (p. 48)?",
      "opties": ["de rekening", "het drankje", "het menu", "de ober"],
      "antwoord": 0,
      "uitleg": "'L'addition' is het Franse woord voor de rekening in een horecagelegenheid."
    },
    {
      "type": "mc",
      "vraag": "Wat is volgens pagina 51 de vrouwelijke vorm van het bijvoeglijk naamwoord <b>'sportif'</b>?",
      "opties": ["sportive", "sportieuse", "sportife", "sportif"],
      "antwoord": 0,
      "uitleg": "Bijvoeglijke naamwoorden die eindigen op -if worden in het vrouwelijk -ive: sportif -> sportive."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Franse woord <b>'l'argent'</b> (m, p. 49) kan zowel 'het geld' als 'het zilver' betekenen.",
      "antwoord": True,
      "uitleg": "Waar. 'L'argent' heeft in het Frans beide betekenissen (geld én het edelmetaal zilver)."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het zelfstandig naamwoord <i>de reactie</i> naar het Frans (p. 48): <i>J'ai laissé une ... sous sa photo.</i>",
      "antwoord": "réaction|reaction|la réaction",
      "uitleg": "'La réaction' betekent 'de reactie'."
    },
    {
      "type": "mc",
      "vraag": "Welk Frans zelfstandig naamwoord betekent <b>'de hersenen'</b> (blauw blok, p. 49)?",
      "opties": ["le cerveau", "le cœur", "le concours", "le conseil"],
      "antwoord": 0,
      "uitleg": "'Le cerveau' betekent 'de hersenen'."
    },
    {
      "type": "mc",
      "vraag": "Waar hoort de nationaliteit te staan in het Frans: <i>un YouTubeur ... (Frans)</i> (p. 51)?",
      "opties": ["ACHTER het zelfstandig naamwoord: un YouTubeur français", "VÓÓR het zelfstandig naamwoord: un français YouTubeur", "Dat mag je in het Frans zelf kiezen", "Vooraan in de zin als eerste woord"],
      "antwoord": 0,
      "uitleg": "Nationaliteiten staan in het Frans altijd achter het zelfstandig naamwoord: 'un YouTubeur français'."
    },
    {
      "type": "waaronwaar",
      "vraag": "De vrouwelijke vorm van het onregelmatige bijvoeglijk naamwoord <b>'vieux'</b> is volgens pagina 51 'vieuse'.",
      "antwoord": False,
      "uitleg": "Onwaar. 'Vieux' heeft de onregelmatige vrouwelijke vorm 'vieille' (bijv. une vieille maison)."
    },
    {
      "type": "invul",
      "vraag": "Wat is de vrouwelijke vorm van het onregelmatige bijvoeglijk naamwoord <b>'nouveau'</b> (p. 51)?",
      "antwoord": "nouvelle",
      "uitleg": "De vrouwelijke vorm van 'nouveau' is 'nouvelle' (une nouvelle copine)."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent het Franse woord <b>'le concours'</b> (blauw blok, p. 49)?",
      "opties": ["de wedstrijd / de competitie", "het schoolgebouw", "het concert", "de prijsuitreiking"],
      "antwoord": 0,
      "uitleg": "'Le concours' betekent 'de wedstrijd' of 'de competitie'."
    },
    {
      "type": "mc",
      "vraag": "Hoe zeg je in het Frans gebiedend: <b>'Geef mij'</b> (p. 48)?",
      "opties": ["Donne-moi", "Prends-moi", "Dis-moi", "Montre-moi"],
      "antwoord": 0,
      "uitleg": "'Donne-moi' (van donner) betekent 'geef mij' (bijv. Donne-moi ton portable)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Franse woord <b>'impossible'</b> (p. 49) betekent 'buitengewoon eenvoudig'.",
      "antwoord": False,
      "uitleg": "Onwaar. 'Impossible' betekent 'onmogelijk'."
    },
    {
      "type": "invul",
      "vraag": "Vervoeg <b>répondre</b> voor <i>nous</i> (p. 51): <i>Nous ... toujours immédiatement aux messages.</i>",
      "antwoord": "répondons|repondons",
      "uitleg": "Nous répondons (stam répond + ons)."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de vaste Franse uitdrukking <b>'faire attention à'</b> (blauw blok, p. 48)?",
      "opties": ["opletten / oppassen met", "bang zijn voor", "plezier hebben in", "haast hebben bij"],
      "antwoord": 0,
      "uitleg": "'Faire attention à' betekent 'opletten' of 'voorzichtig zijn met'."
    },
    {
      "type": "mc",
      "vraag": "Wat is de juiste Franse vertaling van <b>'het goud'</b> (p. 49)?",
      "opties": ["l'or", "l'argent", "le prix", "le truc"],
      "antwoord": 0,
      "uitleg": "'L'or' (mannelijk) betekent 'het goud'. 'L'argent' is 'het zilver' of 'het geld'."
    },
    {
      "type": "waaronwaar",
      "vraag": "In de zin <i>'C\'est une belle photo'</i> staat het bijvoeglijk naamwoord <b>'belle'</b> correct VÓÓR het zelfstandig naamwoord (p. 51).",
      "antwoord": True,
      "uitleg": "Waar. Beau/belle hoort bij de categorie bijvoeglijke naamwoorden die vóór het zelfstandig naamwoord staan."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het woord <i>het advies</i> naar het Frans (blauw blok, p. 48): <i>Mon père m'a donné un bon ... .</i>",
      "antwoord": "conseil|le conseil",
      "uitleg": "'Le conseil' betekent 'het advies'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent het Franse woord <b>'le parfum'</b> in de context van ijsjes of desserts (p. 49)?",
      "opties": ["de smaak", "de geur van bloemen", "de prijs van het ijsje", "de verpakking"],
      "antwoord": 0,
      "uitleg": "In de context van eten en ijs (p. 49) betekent 'le parfum' 'de smaak' (bijv. vanille of chocolade)."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de vorm <b>'j\'ai vu'</b> in: <i>J'ai vu cette vidéo hier soir</i> (p. 48)?",
      "opties": ["ik heb gezien", "ik heb gehoord", "ik heb gezegd", "ik heb verloren"],
      "antwoord": 0,
      "uitleg": "'J'ai vu' is de passé composé van voir: 'ik heb gezien'."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Franse bijvoeglijk naamwoord <b>'pauvre'</b> (p. 49) betekent 'rijk en welvarend'.",
      "antwoord": False,
      "uitleg": "Onwaar. 'Pauvre' betekent 'arm'. Het tegenovergestelde is 'riche' (rijk)."
    },
    {
      "type": "invul",
      "vraag": "Vul de juiste vorm van <i>avoir</i> in (nodig hebben, p. 48): <i>J'... besoin de mon dictionnaire de français.</i>",
      "antwoord": "ai",
      "uitleg": "'Avoir besoin de': bij 'je' wordt het 'J'ai besoin de'."
    }
  ]
}

if __name__ == "__main__":
    write_examen("examen_u1_vocab_6.js", v6)
    write_examen("examen_u1_vocab_7.js", v7)
    write_examen("examen_u1_vocab_8.js", v8)
    write_examen("examen_u1_vocab_9.js", v9)
    write_examen("examen_u1_vocab_10.js", v10)
    print("\n🎉 Extra 5 Unité 1 Vocabulaire Toetsen succesvol aangemaakt!")

#!/usr/bin/env python3
"""
Generate Frans Unité 7 Proeftoetsen (5 exams x 20 questions = 100 questions)
Grandes Lignes 3 HAVO - Unité 7: À tout prix!
"""
import os, json

DATA_DIR = "/home/mesuto/Documents/PROJELER/duru_okul/havo3/frans/js/data"
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

def write_examen(filename, data):
    balance_mc(data["vragen"])
    path = os.path.join(DATA_DIR, filename)
    content = f"""/* Proeftoets {data['titel']}
   Grandes Lignes 3 HAVO Unité {data['hoofdstuk']} */
DURU.registerExamen({json.dumps(data, indent=2, ensure_ascii=False)});
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  [✓] Frans Examen saved: {filename}")

# EXAMEN 31: Vocabulaire U7 (Geld, Zakgeld, Prijzen & Bijbaantjes)
ex31 = {
  "id": "ex-h3-frans-31",
  "hoofdstuk": 7,
  "hoofdstukTitel": "Unité 7 — À tout prix!",
  "titel": "Toets 1 — Vocabulaire: Geld, Zakgeld, Sparen & Bijbaantjes",
  "vak": "Frans · HAVO 3 (U7)",
  "icoon": "💶",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Wat betekent de term <b>'l'argent de poche'</b>?", "opties": ["zakgeld", "contant geld", "spaargeld bij de bank", "een lening"], "antwoord": 0, "uitleg": "'L'argent de poche' is zakgeld."},
    {"type": "mc", "vraag": "Vertaal naar het Nederlands: <b>'économiser de l'argent'</b>:", "opties": ["geld sparen", "geld uitgeven", "geld lenen", "geld verliezen"], "antwoord": 0, "uitleg": "'Économiser' betekent sparen / bezuinigen."},
    {"type": "waaronwaar", "vraag": "In het Frans betekent <b>'dépenser de l'argent'</b> geld verdienen met een bijbaantje.", "antwoord": False, "uitleg": "Onwaar. 'Dépenser' betekent geld uitgeven. Verdienen is 'gagner de l'argent'."},
    {"type": "invul", "vraag": "Vertaal het woord <i>bijbaantje</i> naar het Frans: <i>Je cherche un petit ... pour les vacances.</i>", "antwoord": "boulot|job|travail", "uitleg": "'Un petit boulot' (of un job) is een bijbaantje."},
    {"type": "mc", "vraag": "Wat betekent <b>'gagner sa vie'</b>?", "opties": ["zijn eigen geld / de kost verdienen", "een loterij winnen", "op vakantie gaan", "een diploma behalen"], "antwoord": 0, "uitleg": "'Gagner sa vie' betekent zijn eigen brood / geld verdienen."},
    {"type": "waaronwaar", "vraag": "Het Franse woord <b>'le prix'</b> betekent zowel de prijs van een product als een hoofdprijs/award.", "antwoord": True, "uitleg": "Waar. 'Le prix' = de prijs."},
    {"type": "invul", "vraag": "Vertaal naar het Frans (goedkoop): <i>Ce smartphone n'est pas cher, il est très ... .</i>", "antwoord": "bon marché|bon marche|économique|economique", "uitleg": "'Bon marché' betekent goedkoop / voordelig."},
    {"type": "mc", "vraag": "Wat betekent <b>'une réduction de 20%'</b>?", "opties": ["een korting van 20%", "een prijsverhoging van 20%", "een rentevergoeding", "een administratieve boete"], "antwoord": 0, "uitleg": "'Une réduction' is een korting."},
    {"type": "mc", "vraag": "Wat is <b>'un compte bancaire'</b>?", "opties": ["een bankrekening", "een creditcardschuld", "een kassabon", "een geldbuidel"], "antwoord": 0, "uitleg": "'Un compte bancaire' is een bankrekening."},
    {"type": "waaronwaar", "vraag": "Het werkwoord <b>'emprunter'</b> betekent 'geld uitlenen aan iemand anders'.", "antwoord": False, "uitleg": "Onwaar. 'Emprunter' betekent lenen van iemand. Uitlenen is 'prêter'."},
    {"type": "invul", "vraag": "Vertaal het werkwoord <i>kopen</i> naar het Frans: <i>Je veux ... un nouveau vélo.</i>", "antwoord": "acheter", "uitleg": "'Acheter' = kopen."},
    {"type": "mc", "vraag": "Wat betekent <b>'vendre en ligne'</b>?", "opties": ["online verkopen (bijv. op Marktplaats of Vinted)", "gratis weggeven", "een advertentie verwijderen", "een pakket ophalen"], "antwoord": 0, "uitleg": "'Vendre' betekent verkopen."},
    {"type": "open", "vraag": "Leg in het Nederlands uit wat het verschil is tussen de werkwoorden <i>'prêter'</i> en <i>'emprunter'</i>.", "sleutelwoorden": ["prêter/uitlenen/geven", "emprunter/lenen/krijgen/ontvangen"], "minTreffers": 2, "modelantwoord": "'Prêter' betekent 'uitlenen' (aan iemand geven), terwijl 'emprunter' 'lenen' (van iemand ontvangen) betekent.", "uitleg": "Prêter = uitlenen; emprunter = lenen."},
    {"type": "mc", "vraag": "Wat is <b>'une publicité'</b> (of 'une pub')?", "opties": ["een reclame / advertentie", "een openbaar park", "een overheidsgebouw", "een krantenartikel"], "antwoord": 0, "uitleg": "'La pub' (publicité) is reclame."},
    {"type": "waaronwaar", "vraag": "De uitdrukking <b>'faire des économies'</b> betekent 'bezuinigen / geld sparen'.", "antwoord": True, "uitleg": "Waar. 'Faire des économies' = sparen."},
    {"type": "invul", "vraag": "Vertaal naar het Frans (betalen): <i>Vous pouvez ... par carte bancaire.</i>", "antwoord": "payer", "uitleg": "'Payer' = betalen."},
    {"type": "mc", "vraag": "Wat betekent <b>'coûter les yeux de la tête'</b> in het Frans?", "opties": ["peperduur zijn (een fortuin kosten)", "heel goedkoop zijn", "gratis worden aangeboden", "moeilijk te vinden zijn"], "antwoord": 0, "uitleg": "Franse uitdrukking voor 'ontzettend duur zijn'."},
    {"type": "waaronwaar", "vraag": "Het woord <b>'la monnaie'</b> betekent kleingeld / wisselgeld.", "antwoord": True, "uitleg": "Waar. 'La monnaie' = muntgeld / wisselgeld (of munteenheid)."},
    {"type": "invul", "vraag": "Vertaal het woord <i>rijk</i> naar het Frans: <i>Ce footballeur est très ... .</i>", "antwoord": "riche", "uitleg": "'Riche' = rijk (tegenovergestelde van pauvre = arm)."},
    {"type": "mc", "vraag": "Wat is <b>'le salaire'</b>?", "opties": ["het loon / salaris", "het zakgeld", "de belasting", "de winkelprijs"], "antwoord": 0, "uitleg": "'Le salaire' is het salaris / loon."}
  ]
}

# EXAMEN 32: Grammaire U7 (Le comparatif & le superlatif: plus...que, moins...que, meilleur)
ex22_comparatif = {
  "id": "ex-h3-frans-32",
  "hoofdstuk": 7,
  "hoofdstukTitel": "Unité 7 — À tout prix!",
  "titel": "Toets 2 — Grammaire: Trappen van Vergelijking (Comparatif & Superlatif)",
  "vak": "Frans · HAVO 3 (U7)",
  "icoon": "📊",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Hoe zeg je <i>'duurder dan'</i> in het Frans?", "opties": ["plus cher que", "moins cher que", "aussi cher que", "le plus cher"], "antwoord": 0, "uitleg": "Plus + adjectif + que = meer ... dan (plus cher que)."},
    {"type": "mc", "vraag": "Hoe zeg je <i>'minder duur dan'</i>?", "opties": ["moins cher que", "plus cher que", "aussi cher que", "le moins cher"], "antwoord": 0, "uitleg": "Moins + adjectif + que = minder ... dan."},
    {"type": "waaronwaar", "vraag": "De constructie <b>'aussi ... que'</b> betekent <i>'even ... als / net zo ... als'</i> (bijv. <i>aussi rapide que</i>).", "antwoord": True, "uitleg": "Waar. 'Aussi grand que' = even groot als."},
    {"type": "invul", "vraag": "Vul aan (beter dan): <i>Ce smartphone est ... que l'ancien modèle.</i>", "antwoord": "meilleur", "uitleg": "In het Frans zeg je niet 'plus bon' maar 'meilleur' (beter)."},
    {"type": "mc", "vraag": "Waarom is <i>'plus bon que'</i> fout in het Frans?", "opties": ["Omdat 'bon' een onregelmatige vergrotende trap heeft: 'meilleur'", "Omdat 'bon' alleen voor dieren wordt gebruikt", "Omdat 'plus' nooit met bijvoeglijke naamwoorden samengaat", "Omdat 'que' achterwege moet blijven"], "antwoord": 0, "uitleg": "Net als in het Nederlands (niet 'goeder' maar 'beter') is het in het Frans 'meilleur'."},
    {"type": "waaronwaar", "vraag": "De overtreffende trap <i>'de duurste'</i> is <b>le plus cher / la plus chère</b>.", "antwoord": True, "uitleg": "Waar. Le/la/les plus + adjectief = de meest / -ste."},
    {"type": "invul", "vraag": "Vul aan voor een vergelijking (even snel als): <i>Le train est ... rapide que la voiture.</i>", "antwoord": "aussi", "uitleg": "Aussi rapide que = even snel als."},
    {"type": "mc", "vraag": "Vervoeg <b>acheter</b> voor <i>je</i>:", "opties": ["j'achète", "j'achete", "j'achètes", "j'achetons"], "antwoord": 0, "uitleg": "J'achète (met een è accent grave voor de uitspraak)."},
    {"type": "mc", "vraag": "Wat is het vrouwelijk van <b>meilleur</b>?", "opties": ["meilleure", "meilleuse", "meilleur", "mieux"], "antwoord": 0, "uitleg": "Meilleur (mannelijk) -> meilleure (vrouwelijk enkelvoud)."},
    {"type": "waaronwaar", "vraag": "De overtreffende trap <i>'de beste'</i> voor een vrouwelijk woord is <b>la meilleure</b>.", "antwoord": True, "uitleg": "Waar. Bijv. 'la meilleure solution' (de beste oplossing)."},
    {"type": "invul", "vraag": "Vervoeg <b>payer</b> bij <i>nous</i>: <i>Nous ... par carte bancaire.</i>", "antwoord": "payons", "uitleg": "Nous payons."},
    {"type": "mc", "vraag": "Kies de juiste vertaling van: <i>'Mijn zus is jonger dan ik'</i>:", "opties": ["Ma sœur est plus jeune que moi.", "Ma sœur est moins jeune que moi.", "Ma sœur est aussi jeune que moi.", "Ma sœur est la plus jeune de moi."], "antwoord": 0, "uitleg": "'Plus jeune que moi' = jonger dan ik."},
    {"type": "open", "vraag": "Vertaal de volgende zin naar correct Frans met een vergelijking: <i>'Deze jurk is mooier dan die broek.'</i>", "sleutelwoorden": ["robe", "plus belle/plus jolie", "que", "pantalon"], "minTreffers": 2, "modelantwoord": "Cette robe est plus belle que ce pantalon.", "uitleg": "'Cette robe est plus belle que ce pantalon.'"},
    {"type": "mc", "vraag": "Vervoeg <b>vendre</b> (verkopen) bij <i>il/elle</i>:", "opties": ["vend", "vends", "vendons", "vendent"], "antwoord": 0, "uitleg": "Il/elle vend (regelmatig werkwoord op -re: je vends, tu vends, il vend)."},
    {"type": "waaronwaar", "vraag": "Voor een klinker verandert <b>'que'</b> in <b>'qu\''</b> (bijv. <i>plus grand qu'avant</i>).", "antwoord": True, "uitleg": "Waar. Que wordt qu' voor een klinker."},
    {"type": "invul", "vraag": "Vul de overtreffende trap in (de snelste): <i>Le TGV est le train le ... rapide de France.</i>", "antwoord": "plus", "uitleg": "Le plus rapide = de snelste."},
    {"type": "mc", "vraag": "Wat betekent <b>'le moins cher'</b>?", "opties": ["de goedkoopste / minst dure", "de allerduurste", "even duur", "onbetaalbaar"], "antwoord": 0, "uitleg": "Le moins cher = het minst duur / de goedkoopste."},
    {"type": "waaronwaar", "vraag": "De vorm van <b>acheter</b> bij <i>nous</i> is <b>nous achètons</b> met een accent grave.", "antwoord": False, "uitleg": "Onwaar. Bij 'nous' en 'vous' blijft het zonder accent: nous achetons, vous achetez."},
    {"type": "invul", "vraag": "Vervoeg <b>acheter</b> voor <i>ils/elles</i>: <i>Ils ... des baskets neuves.</i>", "antwoord": "achètent|achetent", "uitleg": "Ils achètent (met accent grave)."},
    {"type": "mc", "vraag": "Welke zin is grammaticaal 100% juist?", "opties": ["Cette pizza est meilleure que celle d'hier.", "Cette pizza est plus bonne que celle d'hier.", "Cette pizza est aussi bonne de celle d'hier.", "Cette pizza est le plus bonne."], "antwoord": 0, "uitleg": "Meilleure que (vrouwelijk)."}
  ]
}

# EXAMEN 33: Stones & Communication U7 (Onderhandelen, Prijzen & Solliciteren)
ex33 = {
  "id": "ex-h3-frans-33",
  "hoofdstuk": 7,
  "hoofdstukTitel": "Unité 7 — À tout prix!",
  "titel": "Toets 3 — Communication: Onderhandelen, Prijzen & Bijbaantjes",
  "vak": "Frans · HAVO 3 (U7)",
  "icoon": "💬",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Hoe vraag je op een rommelmarkt (vide-greniers) of er iets van de prijs af kan?", "opties": ["Vous pouvez me faire un petit prix / une réduction ?", "Donnez-moi cet objet gratuitement !", "Votre prix est une arnaque !", "Je vais appeler la police."], "antwoord": 0, "uitleg": "'Vous pouvez me faire un prix ?' is de gangbare vriendelijke vraag."},
    {"type": "mc", "vraag": "Wat zeg je als je wilt solliciteren naar een bijbaantje als oppas of vakkenvuller?", "opties": ["Bonjour, je cherche un petit boulot pour les week-ends.", "Je refuse de travailler chez vous.", "Combien d'argent vous me donnez sans travailler ?", "Où puis-je dormir pendant mon travail ?"], "antwoord": 0, "uitleg": "'Je cherche un petit boulot' (Ik zoek een bijbaantje)."},
    {"type": "waaronwaar", "vraag": "In Frankrijk is een <b>'vide-greniers'</b> of <b>'brocante'</b> een rommelmarkt / vrijmarkt.", "antwoord": True, "uitleg": "Waar. 'Vide-greniers' betekent letterlijk 'zolderleegverkoop' (rommelmarkt)."},
    {"type": "invul", "vraag": "Vul aan om te vragen <i>'Hoeveel kost dit?'</i>: <i>Ça ... combien ?</i>", "antwoord": "coûte|coute|fait", "uitleg": "'Ça coûte combien ?' of 'Ça fait combien ?'."},
    {"type": "mc", "vraag": "Wat antwoordt de verkoper als een prijs niet onderhandelbaar is?", "opties": ["Désolé, le prix est fixe / non négociable.", "Prenez-le pour un centime.", "Je vous donne de l'argent.", "C'est gratuit pour vous."], "antwoord": 0, "uitleg": "'Le prix est fixe' (vaste prijs)."},
    {"type": "waaronwaar", "vraag": "De uitdrukking <b>'C'est une bonne affaire !'</b> betekent dat je een heel goede deal / koopje hebt gedaan.", "antwoord": True, "uitleg": "Waar. 'Une bonne affaire' = een goede deal / koopje."},
    {"type": "invul", "vraag": "Vertaal naar het Frans (korting): <i>Avez-vous une ... pour les étudiants ?</i>", "antwoord": "réduction|reduction|remise", "uitleg": "'Une réduction' = een korting."},
    {"type": "mc", "vraag": "Hoe vraag je of je met pin/kaart kunt betalen?", "opties": ["Est-ce que je peux payer par carte bancaire ?", "Où est votre portefeuille ?", "Pourquoi je dois payer ?", "Prenez-vous des chèques en bois ?"], "antwoord": 0, "uitleg": "'Payer par carte bancaire' = betalen met pinpas."},
    {"type": "mc", "vraag": "Wat betekent <b>'Je n'ai pas assez d'argent sur moi'</b>?", "opties": ["Ik heb niet genoeg geld bij me", "Ik ben al mijn geld kwijt", "Ik wil niet betalen", "Mijn geld is nep"], "antwoord": 0, "uitleg": "'Pas assez d'argent' = niet genoeg geld."},
    {"type": "waaronwaar", "vraag": "De uitdrukking <b>'C'est trop cher pour mon budget'</b> betekent dat het binnen je budget past.", "antwoord": False, "uitleg": "Onwaar. Het betekent dat het te duur is voor je budget."},
    {"type": "invul", "vraag": "Vertaal het woord <i>koopje</i> naar het Frans in twee woorden: <i>C'est une bonne ... !</i>", "antwoord": "affaire", "uitleg": "Une bonne affaire."},
    {"type": "mc", "vraag": "Hoe vraag je naar het uurloon bij een bijbaantje?", "opties": ["Quel est le salaire horaire (par heure) ?", "Combien d'heures dure une journée ?", "Pourquoi le travail est difficile ?", "Quand fermez-vous ?"], "antwoord": 0, "uitleg": "'Le salaire horaire' = het uurloon."},
    {"type": "open", "vraag": "Schrijf een korte reactie op een online advertentie waarin je interesse toont in een tweedehands fiets en vraagt of de prijs bespreekbaar is.", "sleutelwoorden": ["vélo/velo", "intéressé/interesse/disponible", "prix/négociable/negociable/réduction"], "minTreffers": 2, "modelantwoord": "Bonjour, je suis très intéressé par votre vélo. Le prix est-il négociable ?", "uitleg": "'Je suis intéressé par votre vélo. Le prix est-il négociable ?'"},
    {"type": "mc", "vraag": "Wat betekent <b>'Faites-moi une offre'</b>?", "opties": ["Doe mij een bod", "Betaal direct de hoofdprijs", "Verlaat de winkel", "Koop twee artikelen"], "antwoord": 0, "uitleg": "'Faire une offre' = een bod doen."},
    {"type": "waaronwaar", "vraag": "Het woord <b>'l'argent de poche'</b> betekent 'spaargeld van je pensioen'.", "antwoord": False, "uitleg": "Onwaar. 'L'argent de poche' is zakgeld voor jongeren."},
    {"type": "invul", "vraag": "Vul aan: <i>Je reçois vingt euros d'argent de poche par ... . (per maand)</i>", "antwoord": "mois", "uitleg": "Par mois = per maand (par semaine = per week)."},
    {"type": "mc", "vraag": "Wat betekent <b>'C'est donné à ce prix-là !'</b>?", "opties": ["Het is bijna gratis / spotgoedkoop voor die prijs!", "Het is veel te duur", "Het is gestolen", "Het is niet te koop"], "antwoord": 0, "uitleg": "'C'est donné' = het is een weggevertje / spotgoedkoop."},
    {"type": "waaronwaar", "vraag": "In Frankrijk is <b>'le pourboire'</b> niet wettelijk verplicht, maar wel gewaardeerd bij goede service.", "antwoord": True, "uitleg": "Waar. Fooi is vrijwillig in Frankrijk."},
    {"type": "invul", "vraag": "Vertaal het woord <i>gratis</i> naar het Frans: <i>La livraison est ... .</i>", "antwoord": "gratuite|gratuit", "uitleg": "Gratuit / gratuite."},
    {"type": "mc", "vraag": "Wat betekent <b>'vendre à perte'</b>?", "opties": ["met verlies verkopen", "met veel winst verkopen", "illegaal handelen", "ruilen zonder geld"], "antwoord": 0, "uitleg": "'À perte' = met verlies."}
  ]
}

# EXAMEN 34: Leesvaardigheid U7 (Advertenties, Zakgeld-enquêtes & Webshops)
ex34 = {
  "id": "ex-h3-frans-34",
  "hoofdstuk": 7,
  "hoofdstukTitel": "Unité 7 — À tout prix!",
  "titel": "Toets 4 — Leesvaardigheid: Advertenties, Consumenten & Zakgeld-enquêtes",
  "vak": "Frans · HAVO 3 (U7)",
  "icoon": "📖",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Lees het onderzoeksresultaat: <i>'Selon une enquête récente, les adolescents français de 14 ans reçoivent en moyenne 30 euros d'argent de poche par mois, principalement dépensés en sorties et en vêtements.'</i><br>Hoeveel zakgeld krijgen Franse 14-jarigen gemiddeld per maand?", "opties": ["30 euro per maand", "100 euro per maand", "10 euro per week", "Helemaal niets"], "antwoord": 0, "uitleg": "'30 euros d'argent de poche par mois'."},
    {"type": "mc", "vraag": "Lees de advertentie: <i>'À vendre : Console de jeux PS5 en parfait état avec deux manettes et trois jeux. Prix : 350€ à débattre.'</i><br>Wat betekent 'Prix à débattre'?", "opties": ["De vraagprijs is onderhandelbaar", "De prijs staat 100% vast", "De console is gratis af te halen", "Alleen te ruilen tegen een fiets"], "antwoord": 0, "uitleg": "'À débattre' (of à négocier) = onderhandelbaar."},
    {"type": "waaronwaar", "vraag": "In de advertentie <i>'Vends vélo de course vintage, très peu servi, comme neuf'</i> is de fiets nauwelijks gebruikt en zo goed als nieuw.", "antwoord": True, "uitleg": "Waar. 'Très peu servi, comme neuf' = nauwelijks gebruikt, als nieuw."},
    {"type": "invul", "vraag": "Wat betekent het Franse woord <b>'en moyenne'</b> in statistieken?", "antwoord": "gemiddeld|in doorsnee", "uitleg": "'En moyenne' = gemiddeld."},
    {"type": "mc", "vraag": "Lees de waarschuwing: <i>'Attention aux arnaques sur Internet : ne payez jamais par virement direct sans garantie de livraison.'</i><br>Waarvoor waarschuwt dit consumentenbericht?", "opties": ["Voor online oplichting / internetfraude", "Voor te snelle internetverbindingen", "Voor goedkope computerschermen", "Voor gratis bezorging"], "antwoord": 0, "uitleg": "'Une arnaque' is een oplichting / fraude."},
    {"type": "waaronwaar", "vraag": "Het Franse woord <b>'une arnaque'</b> betekent een geweldig koopje.", "antwoord": False, "uitleg": "Onwaar. 'Une arnaque' is een oplichting / scam."},
    {"type": "invul", "vraag": "Vertaal het woord <b>'l'argent'</b> naar het Nederlands:", "antwoord": "geld|het geld|zilver", "uitleg": "L'argent = geld (of zilver)."},
    {"type": "mc", "vraag": "Lees de vacature: <i>'Recherche baby-sitter sérieux pour garder deux enfants de 6 et 8 ans les mercredis après-midi. Rémunération : 12€/heure.'</i><br>Wat is de vergoeding per uur voor de oppas?", "opties": ["12 euro per uur", "6 euro per uur", "20 euro per uur", "Gratis vrijwilligerswerk"], "antwoord": 0, "uitleg": "'12€/heure' (twaalf euro per uur)."},
    {"type": "mc", "vraag": "Wat betekent het signaalwoord <b>'pourtant'</b>?", "opties": ["toch / nochtans / echter", "daarom", "allereerst", "plotseling"], "antwoord": 0, "uitleg": "'Pourtant' drukt een tegenstelling uit (toch / desalniettemin)."},
    {"type": "waaronwaar", "vraag": "In de zin <i>'Ce magasin propose des facilités de paiement en trois fois sans frais'</i> kun je in 3 termijnen betalen zonder extra rentekosten.", "antwoord": True, "uitleg": "Waar. 'En 3 fois sans frais' = renteloos in 3 termijnen betalen."},
    {"type": "invul", "vraag": "Wat betekent <b>'économiser'</b> in: <i>'J'économise pour acheter une guitare'</i>?", "antwoord": "sparen|geld sparen|bezuinigen", "uitleg": "'Économiser' = sparen."},
    {"type": "mc", "vraag": "Lees het artikel over jongeren en geld: <i>'De plus en plus de jeunes utilisent des applications bancaires mobiles pour gérer leur budget de manière autonome.'</i><br>Waarvoor gebruiken steeds meer jongeren mobiele bank-apps?", "opties": ["Om zelfstandig hun budget en uitgaven te beheren", "Om computerspelletjes te downloaden", "Om huiswerk te maken", "Om contact te leggen met buitenlandse scholen"], "antwoord": 0, "uitleg": "'Gérer leur budget de manière autonome' = zelfstandig hun budget beheren."},
    {"type": "open", "vraag": "Lees: <i>'Pour financer leur voyage scolaire à Rome, les élèves ont vendu des gâteaux et organisé une tombola.'</i><br>Welke twee acties hebben de leerlingen ondernomen om hun schoolreis te financieren?", "sleutelwoorden": ["taarten/cakes/gebak/gâteaux", "tombola/loterij"], "minTreffers": 2, "modelantwoord": "Ze hebben taarten/gebak verkocht en een tombola (loterij) georganiseerd.", "uitleg": "Vente de gâteaux en tombola."},
    {"type": "mc", "vraag": "Wat betekent <b>'une tombola'</b>?", "opties": ["een loterij met prijzen", "een voetbalwedstrijd", "een sponsorloop", "een schoolconcert"], "antwoord": 0, "uitleg": "'Une tombola' is een loterij."},
    {"type": "waaronwaar", "vraag": "Het Franse woord <b>'le pouvoir d'achat'</b> betekent koopkracht.", "antwoord": True, "uitleg": "Waar. 'Le pouvoir d'achat' is de koopkracht van consumenten."},
    {"type": "invul", "vraag": "Wat betekent het signaalwoord <b>'donc'</b> in een conclusie?", "antwoord": "dus|daarom", "uitleg": "'Donc' betekent dus / bijgevolg."},
    {"type": "mc", "vraag": "Lees het advies: <i>'Avant d'acheter un produit cher, comparez toujours les prix sur plusieurs sites Internet.'</i><br>Wat moet je altijd doen voor een dure aankoop?", "opties": ["Prijzen vergelijken op verschillende websites", "Direct het eerste aanbod accepteren", "Geld lenen bij vrienden", "De aankoop contant betalen"], "antwoord": 0, "uitleg": "'Comparez les prix sur plusieurs sites'."},
    {"type": "waaronwaar", "vraag": "Het woord <b>'les frais de port'</b> betekent havenkosten.", "antwoord": False, "uitleg": "Onwaar. 'Les frais de port' zijn de verzendkosten / bezorgkosten bij een bestelling."},
    {"type": "invul", "vraag": "Vertaal het woord <i>verzendkosten</i>: <i>Les frais de ... sont offerts dès 40€.</i>", "antwoord": "port|livraison", "uitleg": "Frais de port / frais de livraison."},
    {"type": "mc", "vraag": "Wat is de hoofdboodschap van een tekst over <i>'Comment bien gérer son premier salaire'</i>?", "opties": ["Praktische tips geven om verstandig om te gaan met je eerste salaris en vaste lasten", "Uitleggen waarom werken zinloos is", "Jongeren stimuleren om al hun geld in één dag uit te geven", "De geschiedenis van de Franse bankbiljetten"], "antwoord": 0, "uitleg": "Verstandig beheer van je eerste inkomsten."}
  ]
}

# EXAMEN 35: Eindtoets Unité 7 (Mix & Examentraining)
ex35 = {
  "id": "ex-h3-frans-35",
  "hoofdstuk": 7,
  "hoofdstukTitel": "Unité 7 — À tout prix!",
  "titel": "Toets 5 — Unité 7 Eindtoets (Mix & Examentraining)",
  "vak": "Frans · HAVO 3 (U7)",
  "icoon": "🏆",
  "duurMin": 30,
  "vragen": [
    {"type": "mc", "vraag": "Wat betekent <b>'l'argent de poche'</b>?", "opties": ["zakgeld", "contant geld", "spaargeld bij de bank", "de rekening"], "antwoord": 0, "uitleg": "L'argent de poche = zakgeld."},
    {"type": "mc", "vraag": "Hoe zeg je <i>'beter dan'</i> in het Frans?", "opties": ["meilleur que", "plus bon que", "aussi bon que", "le plus bon"], "antwoord": 0, "uitleg": "Meilleur que (onregelmatig)."},
    {"type": "waaronwaar", "vraag": "Het Franse woord <b>'une réduction'</b> betekent een korting.", "antwoord": True, "uitleg": "Waar. Une réduction = een korting."},
    {"type": "invul", "vraag": "Vervoeg <b>acheter</b> bij <i>je</i>: <i>J'... un livre de français.</i>", "antwoord": "achète|achete", "uitleg": "J'achète (met accent grave)."},
    {"type": "mc", "vraag": "Wat is de juiste vorm van de overtreffende trap (de mooiste): <i>C'est la robe la ... (mooi) du magasin.</i>", "opties": ["plus belle", "plus beau", "meilleure", "plus grande"], "antwoord": 0, "uitleg": "La robe la plus belle (vrouwelijk enkelvoud)."},
    {"type": "waaronwaar", "vraag": "Het werkwoord <b>'économiser'</b> betekent 'veel geld verspillen'.", "antwoord": False, "uitleg": "Onwaar. 'Économiser' betekent geld sparen / bezuinigen."},
    {"type": "invul", "vraag": "Vertaal het woord <i>bijbaantje</i> naar het Frans: <i>J'ai trouvé un petit ... pour l'été.</i>", "antwoord": "boulot|job|travail", "uitleg": "Un petit boulot."},
    {"type": "mc", "vraag": "Wat betekent <b>'Ça coûte les yeux de la tête'</b>?", "opties": ["Het is ontzettend duur", "Het is spotgoedkoop", "Het is gratis", "Het is lelijk"], "antwoord": 0, "uitleg": "Peperduur zijn."},
    {"type": "mc", "vraag": "Vervoeg <b>vendre</b> bij <i>ils/elles</i>:", "opties": ["vendent", "vendons", "vendez", "vend"], "antwoord": 0, "uitleg": "Ils vendent."},
    {"type": "waaronwaar", "vraag": "De constructie <b>'moins cher que'</b> betekent 'minder duur dan / goedkoper dan'.", "antwoord": True, "uitleg": "Waar. Moins cher que = minder duur dan."},
    {"type": "invul", "vraag": "Vul aan (even groot als): <i>Lucas est ... grand que son frère.</i>", "antwoord": "aussi", "uitleg": "Aussi grand que = even groot als."},
    {"type": "mc", "vraag": "Wat betekent <b>'une bonne affaire'</b>?", "opties": ["een goede deal / een koopje", "een dure vergissing", "een faillissement", "een gesloten winkel"], "antwoord": 0, "uitleg": "Une bonne affaire = een koopje."},
    {"type": "open", "vraag": "Leg uit waarom de zin <i>'Ce vélo est plus bon que le mien'</i> fout is in het Frans en verbeter de zin.", "sleutelwoorden": ["plus bon/fout/onjuist/niet correct", "meilleur/meilleur que"], "minTreffers": 2, "modelantwoord": "'Plus bon' bestaat niet in het Frans; de correcte vorm is 'Ce vélo est meilleur que le mien.'", "uitleg": "Plus bon -> meilleur."},
    {"type": "mc", "vraag": "Kies de juiste vorm van <b>payer</b>: <i>Nous ... (betalen) l'addition au serveur.</i>", "opties": ["payons", "paient", "payez", "paie"], "antwoord": 0, "uitleg": "Nous payons."},
    {"type": "waaronwaar", "vraag": "Het Franse woord <b>'une arnaque'</b> betekent een betrouwbare transactie.", "antwoord": False, "uitleg": "Onwaar. 'Une arnaque' is een oplichting / scam."},
    {"type": "invul", "vraag": "Vertaal het woord <i>wisselgeld / kleingeld</i>: <i>Gardez la ... ! (Houd het wisselgeld maar)</i>", "antwoord": "monnaie", "uitleg": "La monnaie."},
    {"type": "mc", "vraag": "Wat betekent <b>'Prix à débattre'</b> in een advertentie?", "opties": ["De prijs is bespreekbaar / onderhandelbaar", "De vaste prijs moet direct contant betaald worden", "Er mag niet geboden worden", "Het product is gratis"], "antwoord": 0, "uitleg": "Prijs is onderhandelbaar."},
    {"type": "waaronwaar", "vraag": "Het woord <b>'gratuit'</b> betekent dat je ervoor moet betalen.", "antwoord": False, "uitleg": "Onwaar. 'Gratuit' betekent gratis."},
    {"type": "invul", "vraag": "Vul de overtreffende trap in (de beste): <i>C'est la ... solution. (vrouwelijk van meilleur)</i>", "antwoord": "meilleure", "uitleg": "La meilleure solution."},
    {"type": "mc", "vraag": "Wat betekent <b>'gagner de l'argent'</b>?", "opties": ["geld verdienen (of winnen)", "geld verliezen", "geld lenen", "schulden maken"], "antwoord": 0, "uitleg": "Gagner de l'argent = geld verdienen / winnen."}
  ]
}

write_examen("examen_31.js", ex31)
write_examen("examen_32.js", ex22_comparatif)
write_examen("examen_33.js", ex33)
write_examen("examen_34.js", ex34)
write_examen("examen_35.js", ex35)
print("Frans Unité 7 exams (31 to 35) generated successfully!")

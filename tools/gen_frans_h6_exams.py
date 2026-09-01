#!/usr/bin/env python3
"""
Generate Frans Unité 6 Proeftoetsen (5 exams x 20 questions = 100 questions)
Grandes Lignes 3 HAVO - Unité 6: C'est moi
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

# EXAMEN 26: Vocabulaire U6 (Uiterlijk, Kleding, Haar & Karakter)
ex26 = {
  "id": "ex-h3-frans-26",
  "hoofdstuk": 6,
  "hoofdstukTitel": "Unité 6 — C'est moi",
  "titel": "Toets 1 — Vocabulaire: Uiterlijk, Kleding, Mode & Karakter",
  "vak": "Frans · HAVO 3 (U6)",
  "icoon": "👗",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Wat betekent het Franse woord <b>'les vêtements'</b>?", "opties": ["de kleding / kledingstukken", "de schoenen", "de brillen", "de sieraden"], "antwoord": 0, "uitleg": "'Les vêtements' betekent de kleding."},
    {"type": "mc", "vraag": "Vertaal naar het Nederlands: <b>'Elle a les cheveux bouclés'</b>:", "opties": ["Zij heeft krullend haar", "Zij heeft steil blond haar", "Zij heeft kort zwart haar", "Zij heeft een paardenstaart"], "antwoord": 0, "uitleg": "'Les cheveux bouclés' betekent krullend haar (lisses = steil)."},
    {"type": "waaronwaar", "vraag": "In het Frans betekent <b>'les yeux marron'</b> bruine ogen.", "antwoord": True, "uitleg": "Waar. 'Marron' betekent kastanjebruin en verandert nooit van vorm."},
    {"type": "invul", "vraag": "Vertaal het kledingstuk <i>trui</i> naar het Frans: <i>En hiver, je porte un ... chaud.</i>", "antwoord": "pull|sweat|pull-over", "uitleg": "'Un pull' (of pull-over) is een trui."},
    {"type": "mc", "vraag": "Wat betekent de karaktereigenschap <b>'travailleur / travailleuse'</b>?", "opties": ["ijverig / hardwerkend", "lui", "verlegen", "onbeleefd"], "antwoord": 0, "uitleg": "'Travailleur' betekent hardwerkend / ijverig."},
    {"type": "waaronwaar", "vraag": "Het woord <b>'les baskets'</b> betekent in het Frans gymschoenen / sneakers.", "antwoord": True, "uitleg": "Waar. 'Des baskets' zijn sportschoenen / sneakers."},
    {"type": "invul", "vraag": "Vertaal het woord <i>jurk</i> naar het Frans: <i>Elle a acheté une jolie ... rouge.</i>", "antwoord": "robe", "uitleg": "'Une robe' is een jurk."},
    {"type": "mc", "vraag": "Wat betekent <b>'porter des lunettes'</b>?", "opties": ["een bril dragen", "een horloge dragen", "een hoed ophebben", "oorbellen dragen"], "antwoord": 0, "uitleg": "'Des lunettes' is een bril."},
    {"type": "mc", "vraag": "Wat is de betekenis van <b>'timide'</b>?", "opties": ["verlegen / bedeesd", "spraakzaam", "grappig", "ongeduldig"], "antwoord": 0, "uitleg": "'Timide' betekent verlegen."},
    {"type": "waaronwaar", "vraag": "Het Franse woord <b>'la taille'</b> betekent zowel iemands lichaamslengte als de kledingmaat.", "antwoord": True, "uitleg": "Waar. 'La taille' = lengte of kledingmaat (bijv. taille M, taille 38)."},
    {"type": "invul", "vraag": "Vertaal het woord <i>broek</i> naar het Frans: <i>Ce ... est trop grand pour moi.</i>", "antwoord": "pantalon|jean", "uitleg": "'Un pantalon' is een broek."},
    {"type": "mc", "vraag": "Wat betekent <b>'avoir les cheveux roux'</b>?", "opties": ["rood / rossig haar hebben", "blond haar hebben", "donkerbruin haar hebben", "grijs haar hebben"], "antwoord": 0, "uitleg": "'Roux' (vrouwelijk: rousse) betekent roodharig / rossig."},
    {"type": "open", "vraag": "Beschrijf in het Frans kort het uiterlijk van een meisje met blond haar en blauwe ogen.", "sleutelwoorden": ["elle a", "cheveux/blonds", "yeux/bleus"], "minTreffers": 2, "modelantwoord": "Elle a les cheveux blonds et les yeux bleus.", "uitleg": "'Elle a les cheveux blonds et les yeux bleus.'"},
    {"type": "mc", "vraag": "Wat betekent de eigenschap <b>'drôle'</b> of <b>'marrant'</b>?", "opties": ["grappig / komisch", "serieus", "boos", "saai"], "antwoord": 0, "uitleg": "'Drôle' en 'marrant' betekenen grappig."},
    {"type": "waaronwaar", "vraag": "De uitdrukking <b>'être à la mode'</b> betekent 'ouderwets gekleed zijn'.", "antwoord": False, "uitleg": "Onwaar. 'Être à la mode' betekent in de mode / hip zijn."},
    {"type": "invul", "vraag": "Vertaal het woord <i>jas / jack</i> naar het Frans: <i>Mets ton ... , il fait froid dehors.</i>", "antwoord": "manteau|blouson|veste", "uitleg": "'Un manteau' (winterjas) of 'un blouson' (jack)."},
    {"type": "mc", "vraag": "Wat betekent <b>'la pointure'</b>?", "opties": ["de schoenmaat", "de broeklengte", "de hoedmaat", "de ringmaat"], "antwoord": 0, "uitleg": "'La pointure' is specifiek de schoenmaat (taille = kledingmaat)."},
    {"type": "waaronwaar", "vraag": "Het woord <b>'sympa'</b> (sympathique) betekent aardig / vriendelijk.", "antwoord": True, "uitleg": "Waar. 'Sympa' betekent sympathiek / aardig."},
    {"type": "invul", "vraag": "Vertaal het woord <i>blouse / overhemd</i> naar het Frans: <i>Il porte une ... blanche.</i>", "antwoord": "chemise", "uitleg": "'Une chemise' is een overhemd / blouse."},
    {"type": "mc", "vraag": "Wat betekent <b>'ressembler à quelqu'un'</b>?", "opties": ["op iemand lijken", "met iemand ruziën", "iemand ontmoeten", "iemand bellen"], "antwoord": 0, "uitleg": "'Ressembler à' betekent op iemand lijken."}
  ]
}

# EXAMEN 27: Grammaire U6 (L'adjectif: vrouwelijk, meervoud & plaats in de zin)
ex27 = {
  "id": "ex-h3-frans-27",
  "hoofdstuk": 6,
  "hoofdstukTitel": "Unité 6 — C'est moi",
  "titel": "Toets 2 — Grammaire: Bijvoeglijk Naamwoord (Mannelijk/Vrouwelijk & Plaats)",
  "vak": "Frans · HAVO 3 (U6)",
  "icoon": "📐",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Wat is de regelmatige regel om een bijvoeglijk naamwoord <b>vrouwelijk</b> te maken in het Frans?", "opties": ["Je voegt een -e toe aan het mannelijk enkelvoud (bijv. grand -> grande)", "Je voegt een -s toe", "Je haalt de laatste letter weg", "Het woord verandert nooit"], "antwoord": 0, "uitleg": "Regel: mannelijk + -e = vrouwelijk (petit -> petite, intelligent -> intelligente)."},
    {"type": "mc", "vraag": "Wat is het vrouwelijk van <b>beau</b> (mooi)?", "opties": ["belle", "beaue", "beauté", "bel"], "antwoord": 0, "uitleg": "Beau -> belle (mannelijk voor klinker: bel; vrouwelijk: belle)."},
    {"type": "waaronwaar", "vraag": "De meeste bijvoeglijke naamwoorden (zoals kleuren en nationaliteiten) staan in het Frans <b>achter</b> het zelfstandig naamwoord.", "antwoord": True, "uitleg": "Waar. Bijv. 'une robe rouge', 'un élève français'. Kleuren en nationaliteiten staan altijd erachter."},
    {"type": "invul", "vraag": "Wat is het vrouwelijk van <b>nouveau</b> (nieuw)?: <i>C'est une ... école.</i>", "antwoord": "nouvelle", "uitleg": "Nouveau -> nouvelle."},
    {"type": "mc", "vraag": "Welke bijvoeglijke naamwoorden staan meestal <b>vóór</b> het zelfstandig naamwoord (de BAGS-regel)?", "opties": ["beau, bon, grand, petit, jeune, vieux, nouveau", "bleu, rouge, noir, vert, blanc", "français, anglais, espagnol, hollandais", "facile, difficile, intéressant, rapide"], "antwoord": 0, "uitleg": "Korte gangbare adjectieven van schoonheid, leeftijd, goedheid en grootte staan vóór het zelfstandig naamwoord."},
    {"type": "waaronwaar", "vraag": "Het vrouwelijk van <b>vieux</b> (oud) is <b>vielle</b>.", "antwoord": False, "uitleg": "Onwaar. Het is <b>vieille</b> (met twee i's: v-i-e-i-l-l-e)."},
    {"type": "invul", "vraag": "Maak het bijvoeglijk naamwoord vrouwelijk: <i>Lucas est créatif, mais Sarah est très ... .</i>", "antwoord": "créative|creative", "uitleg": "Woorden op -if worden -ive: créatif -> créative, sportif -> sportive."},
    {"type": "mc", "vraag": "Wat is het meervoud van <b>un beau chapeau</b>?", "opties": ["de beaux chapeaux", "des beaus chapeaus", "de belles chapeaux", "des beau chapeaux"], "antwoord": 0, "uitleg": "Beau -> beaux en chapeau -> chapeaux (woorden op -eau krijgen een -x in het meervoud)."},
    {"type": "mc", "vraag": "Wat is het vrouwelijk van <b>blanc</b> (wit)?", "opties": ["blanche", "blanque", "blance", "blanchie"], "antwoord": 0, "uitleg": "Blanc -> blanche."},
    {"type": "waaronwaar", "vraag": "De kleurnaam <b>marron</b> (en orange) krijgt nooit een extra -e of -s in het vrouwelijk of meervoud.", "antwoord": True, "uitleg": "Waar. 'Marron' en 'orange' zijn onveranderlijk (des yeux marron, des chaussures orange)."},
    {"type": "invul", "vraag": "Maak de zin passend (meervoud): <i>Ce sont de ... (petit) maisons.</i>", "antwoord": "petites", "uitleg": "Maisons is vrouwelijk meervoud -> petites."},
    {"type": "mc", "vraag": "Kies de juiste combinatie: <i>Une ... (groot) fille avec des yeux ... (blauw).</i>", "opties": ["grande / bleus", "grand / bleu", "grande / bleues", "grand / bleus"], "antwoord": 0, "uitleg": "Grande (vrouwelijk enkelvoud, staat vooraan) + bleus (mannelijk meervoud bij 'les yeux')."},
    {"type": "open", "vraag": "Leg uit waarom in het Frans de zin <i>'J'ai acheté une voiture rouge'</i> de kleur achter 'voiture' heeft staan, terwijl in het Nederlands 'rode auto' vooraan staat.", "sleutelwoorden": ["kleur/kleuren/couleur", "achter/na/achteraan/zelfstandig naamwoord"], "minTreffers": 1, "modelantwoord": "In het Frans worden kleuren altijd áchter het zelfstandig naamwoord geplaatst (une voiture rouge).", "uitleg": "Kleuren staan in het Frans standaard achter het zelfstandig naamwoord."},
    {"type": "mc", "vraag": "Wat is het vrouwelijk van <b>gentil</b> (aardig)?", "opties": ["gentille", "gentile", "gentieuse", "gentillement"], "antwoord": 0, "uitleg": "Gentil -> gentille (dubbele l + e)."},
    {"type": "waaronwaar", "vraag": "Het bijvoeglijk naamwoord <b>long</b> (lang) wordt in het vrouwelijk <b>longue</b> (met -ue).", "antwoord": True, "uitleg": "Waar. Long -> longue (bijv. une longue robe)."},
    {"type": "invul", "vraag": "Wat is het vrouwelijk van <b>bon</b> (goed/lekker)?: <i>C'est une ... idée.</i>", "antwoord": "bonne", "uitleg": "Bon -> bonne (dubbele n + e)."},
    {"type": "mc", "vraag": "Welke zin is grammaticaal correct geschreven?", "opties": ["Il habite dans une belle grande maison.", "Il habite dans une maison grande belle.", "Il habite dans une beau grand maison.", "Il habite dans un belle maison grand."], "antwoord": 0, "uitleg": "Belle en grande staan beide vóór 'maison'."},
    {"type": "waaronwaar", "vraag": "Bijvoeglijke naamwoorden die in het mannelijk al eindigen op een <b>-e</b> (zoals <i>timide, sympa, facile</i>) krijgen in het vrouwelijk geen extra -e.", "antwoord": True, "uitleg": "Waar. Il est timide / elle est timide blijft hetzelfde."},
    {"type": "invul", "vraag": "Vul aan (meervoud van gros): <i>Ce sont de ... (dik/groot) chiens.</i>", "antwoord": "gros", "uitleg": "Woorden op -s veranderen niet in het mannelijk meervoud (un gros chien / des gros chiens)."},
    {"type": "mc", "vraag": "Wat is het vrouwelijk van <b>heureux</b> (gelukkig)?", "opties": ["heureuse", "heureusse", "heureux", "heureue"], "antwoord": 0, "uitleg": "Woorden op -eux worden -euse in het vrouwelijk: heureux -> heureuse, sérieux -> sérieuse."}
  ]
}

# EXAMEN 28: Stones & Communication U6 (Kleding passen, winkelen & stijladvies)
ex28 = {
  "id": "ex-h3-frans-28",
  "hoofdstuk": 6,
  "hoofdstukTitel": "Unité 6 — C'est moi",
  "titel": "Toets 3 — Communication: Kleding passen, Schoenmaat & Stijladvies",
  "vak": "Frans · HAVO 3 (U6)",
  "icoon": "🛍️",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Hoe vraag je in een kledingwinkel waar de paskamers zijn?", "opties": ["Où sont les cabines d'essayage, s'il vous plaît ?", "Où est la porte de sortie ?", "Pourquoi les vêtements sont chers ?", "Puis-je couper ce pantalon ?"], "antwoord": 0, "uitleg": "'Les cabines d'essayage' zijn de paskamers."},
    {"type": "mc", "vraag": "Wat vraag je als je een broek in een grotere maat wilt passen?", "opties": ["Avez-vous ce pantalon dans une taille au-dessus (plus grande) ?", "Le pantalon est très moche.", "Je veux acheter le magasin.", "Où avez-vous fabriqué ce pantalon ?"], "antwoord": 0, "uitleg": "'Une taille au-dessus' = een maatje groter."},
    {"type": "waaronwaar", "vraag": "De vraag <i>'Quelle est votre pointure ?'</i> vraagt naar je kledingmaat voor een trui.", "antwoord": False, "uitleg": "Onwaar. 'La pointure' is de schoenmaat. Kledingmaat is 'la taille'."},
    {"type": "invul", "vraag": "Vul aan om te vragen <i>'Mag ik dit passen?'</i>: <i>Puis-je ... cette veste ?</i>", "antwoord": "essayer", "uitleg": "'Essayer' betekent passen (kleding/schoenen)."},
    {"type": "mc", "vraag": "Hoe zeg je dat een kledingstuk je heel goed staat?", "opties": ["Ce pull te va très bien !", "Ce pull est trop sale.", "Enlève ce pull immédiatement.", "Ce pull n'a pas de manches."], "antwoord": 0, "uitleg": "'Ça te va très bien' betekent 'Het staat je heel goed'."},
    {"type": "waaronwaar", "vraag": "De uitdrukking <b>'C'est trop serré'</b> betekent dat het kledingstuk veel te strak zit.", "antwoord": True, "uitleg": "Waar. 'Serré' = strak (trop large = te wijd)."},
    {"type": "invul", "vraag": "Vul het woord in voor <i>kleur</i>: <i>Vous avez cette chemise en une autre ... ?</i>", "antwoord": "couleur", "uitleg": "'Une couleur' = een kleur."},
    {"type": "mc", "vraag": "Wat antwoord je als de verkoopster vraagt: <i>'Je peux vous aider ?'</i> en je wilt alleen even rondkijken?", "opties": ["Non merci, je regarde seulement pour l'instant.", "Donnez-moi tout de suite la caisse.", "Je déteste votre magasin.", "Appelez le directeur."], "antwoord": 0, "uitleg": "'Je regarde seulement' = ik kijk alleen even rond."},
    {"type": "mc", "vraag": "Wat betekent <b>'C'est en solde'</b>?", "opties": ["Het is in de uitverkoop / afgeprijsd", "Het is uitverkocht", "Het is kapot", "Het is tweedehands"], "antwoord": 0, "uitleg": "'Les soldes' is de uitverkoop / sale."},
    {"type": "waaronwaar", "vraag": "De zin <i>'Je fais du 38'</i> betekent dat je schoenmaat 38 of kledingmaat 38 hebt.", "antwoord": True, "uitleg": "Waar. 'Faire du [maat]' geeft je maat aan."},
    {"type": "invul", "vraag": "Vertaal het woord <i>duur</i> naar het Frans: <i>Cette robe est beaucoup trop ... .</i>", "antwoord": "chère|chere|cher", "uitleg": "'Cher / chère' = duur."},
    {"type": "mc", "vraag": "Hoe vraag je naar de prijs van een paar schoenen?", "opties": ["Combien coûtent ces baskets ?", "Pourquoi ces baskets sont neuves ?", "Où sont fabriquées ces baskets ?", "Qui porte ces baskets ?"], "antwoord": 0, "uitleg": "'Combien coûtent...' vraagt naar de prijs."},
    {"type": "open", "vraag": "Schrijf een korte zin in het Frans waarin je aan de verkoper vraagt of ze deze trui in maat M (moyen) hebben.", "sleutelwoorden": ["avez-vous/vous avez", "pull", "taille/m"], "minTreffers": 2, "modelantwoord": "Bonjour, avez-vous ce pull en taille M, s'il vous plaît ?", "uitleg": "'Avez-vous ce pull en taille M, s'il vous plaît ?'."},
    {"type": "mc", "vraag": "Wat betekent <b>'Je le prends'</b> aan het einde van het passen?", "opties": ["Ik neem het / Ik koop het", "Ik leg het terug", "Ik vind het lelijk", "Ik heb geen geld"], "antwoord": 0, "uitleg": "'Je le prends' = ik neem het (koop het)."},
    {"type": "waaronwaar", "vraag": "In Frankrijk betekent <b>'payer par carte bancaire (CB)'</b> betalen met pinpas / creditcard.", "antwoord": True, "uitleg": "Waar. CB (carte bancaire) is de bankpas."},
    {"type": "invul", "vraag": "Vul het woord in voor <i>contant geld</i>: <i>Je préfère payer en ... .</i>", "antwoord": "espèces|liquide|especes", "uitleg": "'En espèces' of 'en liquide' = contant."},
    {"type": "mc", "vraag": "Wat betekent <b>'C'est trop large pour moi'</b>?", "opties": ["Het is te wijd / te groot voor mij", "Het is te kort", "Het is te duur", "Het is niet mijn kleur"], "antwoord": 0, "uitleg": "'Large' betekent wijd / ruim."},
    {"type": "waaronwaar", "vraag": "Het woord <b>'le ticket de caisse'</b> is de kassabon die je nodig hebt voor ruilen.", "antwoord": True, "uitleg": "Waar. 'Le ticket de caisse' = de kassabon."},
    {"type": "invul", "vraag": "Vertaal het werkwoord <i>ruilen</i> naar het Frans: <i>Je voudrais ... cet article avec mon ticket.</i>", "antwoord": "échanger|echanger", "uitleg": "'Échanger' = ruilen."},
    {"type": "mc", "vraag": "Wat betekent <b>'Satisfait ou remboursé'</b>?", "opties": ["Niet tevreden, geld terug", "Geen ruiling mogelijk", "Alleen contant betalen", "Defecte goederen"], "antwoord": 0, "uitleg": "'Remboursé' = geld terugbetaald."}
  ]
}

# EXAMEN 29: Leesvaardigheid U6 (Modeblogs, Kledingcatalogi & Persoonlijkheidstests)
ex29 = {
  "id": "ex-h3-frans-29",
  "hoofdstuk": 6,
  "hoofdstukTitel": "Unité 6 — C'est moi",
  "titel": "Toets 4 — Leesvaardigheid: Modeblogs, Webshops & Karaktertests",
  "vak": "Frans · HAVO 3 (U6)",
  "icoon": "📖",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Lees de productomschrijving: <i>'Veste en jean 100% coton bio. Coupe décontractée, idéale pour la mi-saison. Lavable en machine à 30°C.'</i><br>Van welk materiaal is deze spijkerjas gemaakt?", "opties": ["100% biologisch katoen", "100% polyester", "Echt leer", "Wol"], "antwoord": 0, "uitleg": "'100% coton bio' = 100% biologisch katoen."},
    {"type": "mc", "vraag": "Lees de blogpost: <i>'La tendance cet automne : les pulls oversize aux couleurs vives comme le jaune moutarde et le vert émeraude.'</i><br>Wat is volgens de modeblogger de trend dit najaar?", "opties": ["Oversized truien in felle kleuren", "Strakke zwarte leren jacks", "Alleen witte overhemden", "Zomershorts"], "antwoord": 0, "uitleg": "'Pulls oversize aux couleurs vives'."},
    {"type": "waaronwaar", "vraag": "De vermelding <b>'Livraison gratuite dès 50€ d'achat'</b> betekent dat de verzending gratis is bij bestellingen vanaf 50 euro.", "antwoord": True, "uitleg": "Waar. 'Livraison gratuite' = gratis bezorging."},
    {"type": "invul", "vraag": "Wat betekent het Franse woord <b>'la livraison'</b> in een webshop?", "antwoord": "de bezorging|bezorging|levering|verzending", "uitleg": "'La livraison' = de bezorging / levering."},
    {"type": "mc", "vraag": "Lees de karaktertest: <i>'Si tu préfères écouter tes amis et les aider sans chercher à être le centre de l'attention, tu es quelqu'un de généreux et modeste.'</i><br>Welke karaktereigenschappen horen bij dit profiel?", "opties": ["Vrijgevig / behulpzaam en bescheiden", "Agressief en luidruchtig", "Lui en ongeïnteresseerd", "Gierig en jaloers"], "antwoord": 0, "uitleg": "'Généreux et modeste'."},
    {"type": "waaronwaar", "vraag": "Het woord <b>'le coton'</b> betekent katoen.", "antwoord": True, "uitleg": "Waar. Le coton = katoen."},
    {"type": "invul", "vraag": "Wat betekent het Franse woord <b>'la laine'</b>?", "antwoord": "wol|de wol", "uitleg": "'La laine' = wol."},
    {"type": "mc", "vraag": "Lees de voorwaarden: <i>'Retours gratuits sous 30 jours à compter de la date de réception du colis.'</i><br>Binnen hoeveel dagen kun je het pakket gratis retourneren?", "opties": ["Binnen 30 dagen", "Binnen 7 dagen", "Binnen 1 jaar", "Niet mogelijk"], "antwoord": 0, "uitleg": "'Sous 30 jours' = binnen 30 dagen."},
    {"type": "mc", "vraag": "Wat betekent het signaalwoord <b>'en effet'</b>?", "opties": ["inderdaad / immers", "nooit", "ondanks dat", "misschien"], "antwoord": 0, "uitleg": "'En effet' bevestigt een eerdere stelling (inderdaad / immers)."},
    {"type": "waaronwaar", "vraag": "In de zin <i>'Ce pantalon est fabriqué à partir de matières recyclées'</i> is de broek gemaakt van gerecyclede materialen.", "antwoord": True, "uitleg": "Waar. 'Matières recyclées' = gerecyclede grondstoffen."},
    {"type": "invul", "vraag": "Wat betekent <b>'le cuir'</b> in: <i>'Une veste en cuir véritable'</i>?", "antwoord": "leer|het leer", "uitleg": "'Le cuir' = leer."},
    {"type": "mc", "vraag": "Lees de recensie: <i>'La couleur sur la photo ne correspond pas à la réalité, le t-shirt est beaucoup plus foncé en vrai.'</i><br>Wat is het probleem volgens de klant?", "opties": ["De kleur van het t-shirt is in het echt veel donkerder dan op de foto", "Het t-shirt heeft een scheur", "De maat is veel te klein", "Het pakket is nooit bezorgd"], "antwoord": 0, "uitleg": "'Beaucoup plus foncé en vrai' = veel donkerder in het echt."},
    {"type": "open", "vraag": "Lees: <i>'Pour bien entretenir vos baskets blanches, nettoyez-les avec un chiffon humide et évitez absolument le sèche-linge.'</i><br>Wat moet je absoluut vermijden volgens dit onderhoudsadvies?", "sleutelwoorden": ["wasdroger/droger/droogtrommel/sèche-linge/seche linge"], "minTreffers": 1, "modelantwoord": "De wasdroger (le sèche-linge) moet absoluut vermeden worden.", "uitleg": "'Évitez absolument le sèche-linge' (wasdroger vermijden)."},
    {"type": "mc", "vraag": "Wat betekent <b>'foncé'</b> en <b>'clair'</b> bij kleuren?", "opties": ["donker en licht (bijv. bleu foncé / bleu clair)", "duur en goedkoop", "mat en glanzend", "modern en klassiek"], "antwoord": 0, "uitleg": "Foncé = donker, clair = licht."},
    {"type": "waaronwaar", "vraag": "Het Franse woord <b>'le modèle'</b> betekent het model / ontwerp van een kledingstuk.", "antwoord": True, "uitleg": "Waar. Le modèle = het model."},
    {"type": "invul", "vraag": "Wat is het Franse woord voor <i>streepjes / gestreept</i>: <i>Une marinière à ... .</i>", "antwoord": "rayures", "uitleg": "'À rayures' = gestreept."},
    {"type": "mc", "vraag": "Lees de advertentie: <i>'Boutique éco-responsable : donnez une seconde vie à vos vêtements d'occasion.'</i><br>Wat voor soort winkel is dit?", "opties": ["Een tweedehandswinkel / vintage kledingzaak", "Een luxe bontwinkel", "Een stomerij", "Een schoenenfabriek"], "antwoord": 0, "uitleg": "'Vêtements d'occasion' zijn tweedehands kleren."},
    {"type": "waaronwaar", "vraag": "De uitdrukking <b>'d'occasion'</b> betekent 'gloednieuw uit de fabriek'.", "antwoord": False, "uitleg": "Onwaar. 'D'occasion' betekent tweedehands."},
    {"type": "invul", "vraag": "Vertaal het woord <i>'nieuw'</i> naar het Frans (mannelijk enkelvoud): <i>J'ai acheté un ... sac.</i>", "antwoord": "nouveau", "uitleg": "Un nouveau sac."},
    {"type": "mc", "vraag": "Wat is de hoofdboodschap van een artikel over <i>'La fast-fashion et son impact environnemental'</i>?", "opties": ["De negatieve gevolgen van goedkope wegwerpmode voor het milieu", "Waarom merkkleding zo goedkoop moet zijn", "Hoe je zo snel mogelijk kleding koopt", "De geschiedenis van de Franse naaimachine"], "antwoord": 0, "uitleg": "Het artikel analyseert de milieuschade van snelle wegwerpmode."}
  ]
}

# EXAMEN 30: Eindtoets Unité 6 (Mix & Examentraining)
ex30 = {
  "id": "ex-h3-frans-30",
  "hoofdstuk": 6,
  "hoofdstukTitel": "Unité 6 — C'est moi",
  "titel": "Toets 5 — Unité 6 Eindtoets (Mix & Examentraining)",
  "vak": "Frans · HAVO 3 (U6)",
  "icoon": "🏆",
  "duurMin": 30,
  "vragen": [
    {"type": "mc", "vraag": "Wat is het vrouwelijk enkelvoud van <b>beau</b>?", "opties": ["belle", "beaue", "bel", "belles"], "antwoord": 0, "uitleg": "Beau -> belle."},
    {"type": "mc", "vraag": "Wat betekent <b>'les cabines d'essayage'</b>?", "opties": ["de paskamers in een kledingwinkel", "de toiletten", "de kassa's", "de etalages"], "antwoord": 0, "uitleg": "Paskamers."},
    {"type": "waaronwaar", "vraag": "De kleurnaam <b>marron</b> krijgt in het meervoud nooit een -s (bijv. <i>des yeux marron</i>).", "antwoord": True, "uitleg": "Waar. Marron en orange zijn onveranderlijk."},
    {"type": "invul", "vraag": "Vertaal het woord <i>schoenmaat</i> naar het Frans: <i>Quelle est votre ... ?</i>", "antwoord": "pointure", "uitleg": "La pointure = de schoenmaat."},
    {"type": "mc", "vraag": "Kies de juiste combinatie: <i>Elle porte une ... (mooi) robe ... (rood).</i>", "opties": ["belle / rouge", "beau / rouge", "belle / rougee", "rouge / belle"], "antwoord": 0, "uitleg": "Belle staat vooraan (BAGS) en rouge staat erachter (kleur)."},
    {"type": "waaronwaar", "vraag": "Het vrouwelijk van <b>vieux</b> (oud) is <b>vieille</b>.", "antwoord": True, "uitleg": "Waar. Vieux -> vieille (bijv. une vieille maison)."},
    {"type": "invul", "vraag": "Maak het adjectief vrouwelijk: <i>Il est sportif, elle est ... .</i>", "antwoord": "sportive", "uitleg": "Sportif -> sportive."},
    {"type": "mc", "vraag": "Wat betekent <b>'Ça te va très bien'</b>?", "opties": ["Het staat je heel goed", "Het is te duur voor jou", "Het zit veel te strak", "Het is niet jouw stijl"], "antwoord": 0, "uitleg": "Ça te va très bien = het staat je geweldig."},
    {"type": "mc", "vraag": "Wat betekent <b>'avoir les cheveux bouclés'</b>?", "opties": ["krullend haar hebben", "steil haar hebben", "kaal zijn", "rood haar hebben"], "antwoord": 0, "uitleg": "Cheveux bouclés = krullend haar."},
    {"type": "waaronwaar", "vraag": "Het meervoud van <b>un nouveau manteau</b> is <b>de nouveaux manteaux</b>.", "antwoord": True, "uitleg": "Waar. Nouveau -> nouveaux en manteau -> manteaux."},
    {"type": "invul", "vraag": "Wat is het vrouwelijk van <b>blanc</b> (wit)?: <i>Une chemise ... .</i>", "antwoord": "blanche", "uitleg": "Blanc -> blanche."},
    {"type": "mc", "vraag": "Wat is het verschil tussen <b>la taille</b> en <b>la pointure</b>?", "opties": ["Taille is kledingmaat / lengte en pointure is schoenmaat", "Taille is schoenmaat en pointure is kledingmaat", "Er is geen verschil", "Pointure is alleen voor hoeden"], "antwoord": 0, "uitleg": "Taille = kledingmaat, pointure = schoenmaat."},
    {"type": "open", "vraag": "Leg uit hoe je in een Franse winkel vraagt of je een jas mag passen en waar de paskamers zijn.", "sleutelwoorden": ["essayer/veste/manteau", "cabines/essayage/où/ou"], "minTreffers": 2, "modelantwoord": "Bonjour, puis-je essayer cette veste ? Où sont les cabines d'essayage, s'il vous plaît ?", "uitleg": "'Puis-je essayer cette veste ? Où sont les cabines d'essayage ?'."},
    {"type": "mc", "vraag": "Kies de juiste vorm: <i>Ce sont des filles très ... (intelligent).</i>", "opties": ["intelligentes", "intelligents", "intelligente", "intelligent"], "antwoord": 0, "uitleg": "Filles is vrouwelijk meervoud -> intelligentes."},
    {"type": "waaronwaar", "vraag": "Het Franse woord <b>'les soldes'</b> betekent de paskamer.", "antwoord": False, "uitleg": "Onwaar. 'Les soldes' is de uitverkoop / sale."},
    {"type": "invul", "vraag": "Vertaal het woord <i>vriendelijk / aardig</i> naar het Frans: <i>Elle est très ... .</i>", "antwoord": "gentille|sympa|sympathique", "uitleg": "Gentille of sympa."},
    {"type": "mc", "vraag": "Wat betekent <b>'C'est trop serré'</b>?", "opties": ["Het zit te strak", "Het is te wijd", "Het is te lang", "Het is te licht"], "antwoord": 0, "uitleg": "Trop serré = te strak."},
    {"type": "waaronwaar", "vraag": "Bijvoeglijke naamwoorden van nationaliteit (zoals <i>français, néerlandais</i>) staan in het Frans achter het zelfstandig naamwoord.", "antwoord": True, "uitleg": "Waar. Un livre français, un fromage néerlandais."},
    {"type": "invul", "vraag": "Vertaal naar het Frans (broek): <i>J'aime ce ... noir.</i>", "antwoord": "pantalon|jean", "uitleg": "Un pantalon."},
    {"type": "mc", "vraag": "Wat is het vrouwelijk van <b>bon</b>?", "opties": ["bonne", "bone", "bonte", "bonnesse"], "antwoord": 0, "uitleg": "Bon -> bonne."}
  ]
}

write_examen("examen_26.js", ex26)
write_examen("examen_27.js", ex27)
write_examen("examen_28.js", ex28)
write_examen("examen_29.js", ex29)
write_examen("examen_30.js", ex30)
print("Frans Unité 6 exams (26 to 30) generated successfully!")

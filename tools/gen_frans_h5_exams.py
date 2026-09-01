#!/usr/bin/env python3
"""
Generate Frans Unité 5 Proeftoetsen (5 exams x 20 questions = 100 questions)
Grandes Lignes 3 HAVO - Unité 5: Au resto!
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

# EXAMEN 21: Vocabulaire U5 (Eten & Drinken, Restaurant, Boodschappen & Menukaart)
ex21 = {
  "id": "ex-h3-frans-21",
  "hoofdstuk": 5,
  "hoofdstukTitel": "Unité 5 — Au resto!",
  "titel": "Toets 1 — Vocabulaire: Eten & Drinken, Restaurant & Menukaart",
  "vak": "Frans · HAVO 3 (U5)",
  "icoon": "🍽️",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Wat betekent <b>'l'addition'</b> in een Frans restaurant?", "opties": ["de rekening", "het voorgerecht", "de fooi", "het menu"], "antwoord": 0, "uitleg": "'L'addition' is de rekening in een restaurant."},
    {"type": "mc", "vraag": "Wat is <b>'le plat principal'</b> op een menukaart?", "opties": ["het hoofdgerecht", "het voorgerecht", "het toetje / dessert", "de drankjeskaart"], "antwoord": 0, "uitleg": "'Le plat principal' is het hoofdgerecht."},
    {"type": "waaronwaar", "vraag": "Het Franse woord <b>'l'entrée'</b> betekent op de menukaart het toetje / dessert.", "antwoord": False, "uitleg": "Onwaar. 'L'entrée' is het voorgerecht. Het nagerecht is 'le dessert'."},
    {"type": "invul", "vraag": "Vertaal naar het Frans (ontbijt): <i>Le matin, je prends mon petit-... .</i>", "antwoord": "déjeuner|dejeuner", "uitleg": "'Le petit-déjeuner' is het ontbijt."},
    {"type": "mc", "vraag": "Wat is <b>'une carafe d'eau'</b> in Frankrijk?", "opties": ["een karaf gratis kraanwater op tafel", "een fles dure frisdrank", "een kop warme thee", "een glas sinaasappelsap"], "antwoord": 0, "uitleg": "In Franse restaurants is 'une carafe d'eau' (kraanwater) gratis."},
    {"type": "waaronwaar", "vraag": "Het woord <b>'le pourboire'</b> betekent 'de fooi voor de ober/serveerster'.", "antwoord": True, "uitleg": "Waar. 'Un pourboire' is de fooi."},
    {"type": "invul", "vraag": "Vertaal het woord <i>ober / kelner</i> naar het Frans: <i>Le ... prend notre commande.</i>", "antwoord": "serveur|garçon|garcon", "uitleg": "'Le serveur' (of le garçon) is de ober."},
    {"type": "mc", "vraag": "Wat betekent <b>'faire les courses'</b>?", "opties": ["boodschappen doen (in de supermarkt/op de markt)", "een hardloopwedstrijd rennen", "de auto wassen", "koken voor vrienden"], "antwoord": 0, "uitleg": "'Faire les courses' is boodschappen doen."},
    {"type": "mc", "vraag": "Wat is <b>'le déjeuner'</b>?", "opties": ["de warme middagmaaltijd / lunch", "het ontbijt", "het avondeten", "een tussendoortje"], "antwoord": 0, "uitleg": "'Le déjeuner' is de lunch / middagmaaltijd."},
    {"type": "waaronwaar", "vraag": "Het Franse woord <b>'les boissons'</b> betekent 'de toetjes'.", "antwoord": False, "uitleg": "Onwaar. 'Les boissons' zijn de drankjes (boire = drinken)."},
    {"type": "invul", "vraag": "Vertaal het woord <i>vlees</i> naar het Frans: <i>Je suis végétarien, je ne mange pas de ... .</i>", "antwoord": "viande", "uitleg": "'La viande' is vlees."},
    {"type": "mc", "vraag": "Wat betekent <b>'un légume'</b>?", "opties": ["een groente", "een stuk fruit", "een soort kaas", "een toetje"], "antwoord": 0, "uitleg": "'Un légume' is een groente."},
    {"type": "open", "vraag": "Noem de drie gangen van een traditioneel Frans driegangenmenu in de juiste volgorde in het Frans.", "sleutelwoorden": ["entrée/entree", "plat/principal", "dessert"], "minTreffers": 3, "modelantwoord": "1. L'entrée (voorgerecht), 2. Le plat principal (hoofdgerecht), 3. Le dessert (nagerecht).", "uitleg": "Volgorde: l'entrée -> le plat principal -> le dessert."},
    {"type": "mc", "vraag": "Wat betekent <b>'le dîner'</b>?", "opties": ["het avondeten", "het ontbijt", "de snack", "de koffiepauze"], "antwoord": 0, "uitleg": "'Le dîner' is het avondeten."},
    {"type": "waaronwaar", "vraag": "Het Franse woord <b>'le pain'</b> betekent brood (zoals een baguette).", "antwoord": True, "uitleg": "Waar. 'Le pain' is brood."},
    {"type": "invul", "vraag": "Vertaal naar het Frans (kaas): <i>La France est célèbre pour son ... .</i>", "antwoord": "fromage", "uitleg": "'Le fromage' is kaas."},
    {"type": "mc", "vraag": "Wat betekent <b>'avoir faim'</b> en <b>'avoir soif'</b>?", "opties": ["honger hebben en dorst hebben", "haast hebben en warm zijn", "koud zijn en moe zijn", "boos zijn en blij zijn"], "antwoord": 0, "uitleg": "Avoir faim = honger hebben; avoir soif = dorst hebben."},
    {"type": "waaronwaar", "vraag": "De uitdrukking <b>'Bon appétit !'</b> betekent 'Eet smakelijk!'.", "antwoord": True, "uitleg": "Waar. 'Bon appétit !' betekent eet smakelijk."},
    {"type": "invul", "vraag": "Vertaal het woord <i>smaak / lekker</i>: <i>C'est très ... ! (heel lekker)</i>", "antwoord": "bon|délicieux|delicieux", "uitleg": "'C'est très bon' of 'C'est délicieux'."},
    {"type": "mc", "vraag": "Wat is <b>'une formule midi'</b> in een Franse bistro?", "opties": ["een voordelig lunchmenu met vaste gerechten", "een reserveringsformulier", "een kookrecept", "een bezorgdienst"], "antwoord": 0, "uitleg": "'Une formule' is een voordelig keuzemenu (bijv. entrée + plat)."}
  ]
}

# EXAMEN 22: Grammaire U5 (L'article partitif: du, de la, de l', des & ontkenning met de/d')
ex22 = {
  "id": "ex-h3-frans-22",
  "hoofdstuk": 5,
  "hoofdstukTitel": "Unité 5 — Au resto!",
  "titel": "Toets 2 — Grammaire: Delend Lidwoord (du, de la, de l', des) & Hoeveelheden",
  "vak": "Frans · HAVO 3 (U5)",
  "icoon": "🧀",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Welk delend lidwoord gebruik je voor een mannelijk woord in het enkelvoud (zoals <i>fromage</i>)?", "opties": ["du", "de la", "de l'", "des"], "antwoord": 0, "uitleg": "Du + mannelijk enkelvoud: du fromage, du pain."},
    {"type": "mc", "vraag": "Welk delend lidwoord hoort bij een vrouwelijk woord (zoals <i>salade</i>)?", "opties": ["de la", "du", "de l'", "des"], "antwoord": 0, "uitleg": "De la + vrouwelijk enkelvoud: de la salade, de la viande."},
    {"type": "waaronwaar", "vraag": "Voor een woord dat begint met een klinker of stomme h gebruik je <b>de l'</b> (bijv. <i>de l'eau</i>).", "antwoord": True, "uitleg": "Waar. De l'eau, de l'huile."},
    {"type": "invul", "vraag": "Vul het juiste delend lidwoord in: <i>Au petit-déjeuner, je mange ... pain avec du beurre.</i>", "antwoord": "du", "uitleg": "Pain is mannelijk: du pain."},
    {"type": "mc", "vraag": "Wat gebeurt er met <i>du, de la, de l', des</i> in een ontkennende zin (bijv. <i>Je ne mange pas ... viande</i>)?", "opties": ["Het verandert altijd in 'de' (of 'd' voor een klinker)", "Het blijft ongewijzigd 'du' of 'de la'", "Het verandert in 'un' of 'une'", "Het vervalt helemaal zonder woord"], "antwoord": 0, "uitleg": "Na een ontkenning verandert het delend lidwoord altijd in 'de' / 'd'': pas de viande, pas d'eau."},
    {"type": "waaronwaar", "vraag": "Na woorden van hoeveelheid (zoals <i>un kilo de, beaucoup de, un peu de</i>) gebruik je altijd <b>de / d'</b> zonder lidwoord.", "antwoord": True, "uitleg": "Waar. Beaucoup de sucre, un kilo de pommes."},
    {"type": "invul", "vraag": "Vul de ontkenning aan: <i>Je ne bois pas ... café le soir.</i>", "antwoord": "de", "uitleg": "Na 'pas' gebruik je 'de': pas de café."},
    {"type": "mc", "vraag": "Vervoeg <b>boire</b> (drinken) voor <i>nous</i>:", "opties": ["buvons", "boivons", "boisons", "boivent"], "antwoord": 0, "uitleg": "Nous buvons (je bois, tu bois, il boit, nous buvons, vous buvez, ils boivent)."},
    {"type": "mc", "vraag": "Wat is de juiste vorm van <b>boire</b> bij <i>ils/elles</i>?", "opties": ["boivent", "buvent", "boivons", "bois"], "antwoord": 0, "uitleg": "Ils/elles boivent."},
    {"type": "waaronwaar", "vraag": "De zin <i>'J'aime le chocolat'</i> gebruikt het bepaald lidwoord (le) omdat het over een algemene voorkeur/smaak gaat.", "antwoord": True, "uitleg": "Waar. Bij werkwoorden van voorkeur (aimer, adorer, détester, préférer) gebruik je le/la/les, niet du/de la."},
    {"type": "invul", "vraag": "Vul aan (een fles water): <i>Je voudrais une bouteille ... eau minérale.</i>", "antwoord": "d'|d", "uitleg": "Une bouteille d'eau (hoeveelheid + d' voor klinker)."},
    {"type": "mc", "vraag": "Kies de juiste combinatie: <i>Je veux ... (wat) frites et ... (wat) poulet.</i>", "opties": ["des / du", "de la / des", "du / des", "les / le"], "antwoord": 0, "uitleg": "Des frites (meervoud) + du poulet (mannelijk enkelvoud)."},
    {"type": "open", "vraag": "Leg het verschil uit tussen <i>'Je mange du gâteau'</i> en <i>'J'aime le gâteau'</i>.", "sleutelwoorden": ["du/deel/stuk/portie/eten", "le/algemeen/voorkeur/houden van"], "minTreffers": 2, "modelantwoord": "'Je mange du gâteau' betekent dat je een deel/portie taart eet (delend lidwoord), terwijl 'J'aime le gâteau' betekent dat je in het algemeen van taart houdt (bepaald lidwoord).", "uitleg": "Delend lidwoord du = een onbepaalde hoeveelheid; le = in het algemeen na aimer."},
    {"type": "mc", "vraag": "Vervoeg <b>vouloir</b> (willen) bij <i>tu</i>:", "opties": ["veux", "veut", "voulons", "voulez"], "antwoord": 0, "uitleg": "Tu veux (je veux, tu veux, il veut, nous voulons, vous voulez, ils veulent)."},
    {"type": "waaronwaar", "vraag": "Het meervoudige delend lidwoord is <b>des</b> (bijv. <i>des fraises</i> = wat aardbeien).", "antwoord": True, "uitleg": "Waar. Des fraises, des légumes."},
    {"type": "invul", "vraag": "Vul het juiste woord in: <i>Il y a trop ... sel dans cette soupe. (te veel zout)</i>", "antwoord": "de", "uitleg": "Trop de + zelfstandig naamwoord."},
    {"type": "mc", "vraag": "Kies de juiste vorm: <i>Nous ... (boire) du jus d'orange tous les matins.</i>", "opties": ["buvons", "boivons", "boisons", "buvez"], "antwoord": 0, "uitleg": "Nous buvons."},
    {"type": "waaronwaar", "vraag": "De zin <i>'Elle n'a pas de sucre'</i> betekent dat ze geen suiker heeft.", "antwoord": True, "uitleg": "Waar. Pas de sucre = geen suiker."},
    {"type": "invul", "vraag": "Vul aan met het juiste delend lidwoord: <i>Tu prends ... confiture sur ta tartine ? (vrouwelijk)</i>", "antwoord": "de la", "uitleg": "De la confiture (vrouwelijk enkelvoud)."},
    {"type": "mc", "vraag": "Welke zin is grammaticaal correct?", "opties": ["Je voudrais un peu de sucre dans mon thé.", "Je voudrais un peu du sucre dans mon thé.", "Je voudrais un peu des sucre dans mon thé.", "Je voudrais un peu le sucre dans mon thé."], "antwoord": 0, "uitleg": "Un peu de + zelfstandig naamwoord (zonder lidwoord)."}
  ]
}

# EXAMEN 23: Stones & Communication U5 (Bestellen in een restaurant, vragen naar de rekening)
ex23 = {
  "id": "ex-h3-frans-23",
  "hoofdstuk": 5,
  "hoofdstukTitel": "Unité 5 — Au resto!",
  "titel": "Toets 3 — Communication: Bestellen in een Restaurant & Boodschappen doen",
  "vak": "Frans · HAVO 3 (U5)",
  "icoon": "💬",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Hoe vraag je beleefd om de rekening aan de ober?", "opties": ["L'addition, s'il vous plaît !", "Donnez-moi votre argent !", "Combien coûte le restaurant ?", "Où est la caisse de secours ?"], "antwoord": 0, "uitleg": "'L'addition, s'il vous plaît !' is de vaste uitdrukking."},
    {"type": "mc", "vraag": "Wat zegt de ober als hij de bestelling komt opnemen?", "opties": ["Vous avez choisi ? / Vous désirez ?", "Pourquoi vous êtes assis ici ?", "Partez rapidement.", "Payez avant de manger."], "antwoord": 0, "uitleg": "'Vous avez choisi ?' (Heeft u gekozen?) of 'Vous désirez ?' (Wat wenst u?)."},
    {"type": "waaronwaar", "vraag": "Om een tafel te reserveren zeg je: <i>'Je voudrais réserver une table pour quatre personnes.'</i>", "antwoord": True, "uitleg": "Waar. Dit is de juiste beleefde reserveringszin."},
    {"type": "invul", "vraag": "Vul aan om beleefd te bestellen: <i>Je ... le steak-frites, s'il vous plaît. (Ik wil graag)</i>", "antwoord": "voudrais|aimerais", "uitleg": "'Je voudrais' (conditionnel de politesse) = ik zou graag willen."},
    {"type": "mc", "vraag": "Hoe vraag je wat de dagschotel is?", "opties": ["Quel est le plat du jour ?", "Quel jour sommes-nous ?", "Où cuisine le chef ?", "Combien pèse la table ?"], "antwoord": 0, "uitleg": "'Le plat du jour' is de dagschotel."},
    {"type": "waaronwaar", "vraag": "Als de ober vraagt <i>'Et comme boisson ?'</i> vraagt hij wat je als toetje wilt.", "antwoord": False, "uitleg": "Onwaar. 'Comme boisson' vraagt wat je wilt drinken."},
    {"type": "invul", "vraag": "Vul het woord in voor <i>voorgerecht</i>: <i>Comme ..., je prends la soupe à l'oignon.</i>", "antwoord": "entrée|entree", "uitleg": "Comme entrée = als voorgerecht."},
    {"type": "mc", "vraag": "Wat zeg je als je wilt aangeven dat je vlees doorbakken / medium gebakken wilt?", "opties": ["À point (medium) / Bien cuit (doorbakken)", "Très froid / Surgelé", "En morceaux / Haché", "Sans sel / Sans goût"], "antwoord": 0, "uitleg": "Saignant (rood), à point (medium), bien cuit (doorbakken)."},
    {"type": "mc", "vraag": "Hoe meld je beleefd dat er een vork of mes ontbreekt op tafel?", "opties": ["Excusez-moi, il me manque une fourchette / un couteau.", "Le restaurant est sale.", "Où sont les assiettes du voisin ?", "Donnez-moi une autre table immédiatement."], "antwoord": 0, "uitleg": "'Il me manque...' betekent 'ik mis / er ontbreekt...'."},
    {"type": "waaronwaar", "vraag": "De vraag <i>'C'est à emporter ou à consommer sur place ?'</i> betekent 'Is het om mee te nemen of om hier op te eten?'.", "antwoord": True, "uitleg": "Waar. À emporter = meenemen; sur place = ter plekke consumeren."},
    {"type": "invul", "vraag": "Vul het ontbrekende woord in: <i>À ..., s'il vous plaît ! (Om mee te nemen)</i>", "antwoord": "emporter", "uitleg": "À emporter."},
    {"type": "mc", "vraag": "Hoe vraag je op de markt naar de prijs van aardbeien?", "opties": ["Combien coûtent les fraises au kilo ?", "Pourquoi les fraises sont rouges ?", "Où poussent vos fraises ?", "Avez-vous mangé les fraises ?"], "antwoord": 0, "uitleg": "'Combien coûtent... au kilo ?' vraagt de kiloprijs."},
    {"type": "open", "vraag": "Schrijf een korte dialoog waarin je een drankje en een hoofdgerecht bestelt bij de ober in een Frans restaurant.", "sleutelwoorden": ["voudrais/prends", "eau/coca/boisson/jus", "plat/steak/poulet/pizza/pâtes", "s'il vous plaît/merci"], "minTreffers": 2, "modelantwoord": "Bonjour, je voudrais une carafe d'eau et le poulet-frites, s'il vous plaît.", "uitleg": "Gebruik 'Je voudrais [drankje] et [gerecht], s'il vous plaît.'"},
    {"type": "mc", "vraag": "Wat antwoord je als de ober vraagt: <i>'Tout s'est bien passé ?'</i> en het eten was heerlijk?", "opties": ["Oui, c'était délicieux, merci beaucoup !", "Non, c'était froid et affreux.", "Je refuse de payer.", "Où sont les toilettes ?"], "antwoord": 0, "uitleg": "'C'était délicieux, merci beaucoup !'."},
    {"type": "waaronwaar", "vraag": "Het Franse woord <b>'l'assiette'</b> betekent het glas.", "antwoord": False, "uitleg": "Onwaar. 'L'assiette' is het bord. Een glas is 'le verre'."},
    {"type": "invul", "vraag": "Vertaal het woord <i>glas</i> naar het Frans: <i>Un ... d'eau, s'il vous plaît.</i>", "antwoord": "verre", "uitleg": "'Un verre d'eau' = een glas water."},
    {"type": "mc", "vraag": "Wat betekent <b>'Gardez la monnaie'</b> als je contant betaalt?", "opties": ["Houd het wisselgeld maar (als fooi)", "Ik heb niet genoeg geld", "Wissel dit briefje alstublieft", "Geef mij al het geld terug"], "antwoord": 0, "uitleg": "'Gardez la monnaie' = houd het wisselgeld maar."},
    {"type": "waaronwaar", "vraag": "In Frankrijk is <b>'le service compris'</b> (bediening inbegrepen) standaard opgenomen in de menuprijzen.", "antwoord": True, "uitleg": "Waar. Service is altijd inbegrepen in Franse horecaprijzen."},
    {"type": "invul", "vraag": "Vertaal naar het Frans (lepel): <i>Une ... à soupe, s'il vous plaît.</i>", "antwoord": "cuillère|cuillere", "uitleg": "'La cuillère' = de lepel."},
    {"type": "mc", "vraag": "Wat betekent <b>'Je suis allergique aux arachides (cacahuètes)'</b>?", "opties": ["Ik ben allergisch voor pinda's", "Ik hou erg van noten", "Mag ik extra saus", "Ik wil een vegetarisch menu"], "antwoord": 0, "uitleg": "Allergie voor pinda's / noten."}
  ]
}

# EXAMEN 24: Leesvaardigheid U5 (Menukaarten, Recepten & Restaurantrecensies)
ex24 = {
  "id": "ex-h3-frans-24",
  "hoofdstuk": 5,
  "hoofdstukTitel": "Unité 5 — Au resto!",
  "titel": "Toets 4 — Leesvaardigheid: Menukaarten, Recepten & Recensies",
  "vak": "Frans · HAVO 3 (U5)",
  "icoon": "📖",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Lees het menu: <i>'Menu Découverte à 22€ : Salade de chèvre chaud OU Soupe à l'oignon + Pavé de saumon OU Steak frites + Mousse au chocolat OU Tarte aux pommes.'</i><br>Welke twee keuzes heeft de gast als voorgerecht?", "opties": ["Warme geitenkaassalade OF uiensoep", "Zalm OF biefstuk", "Chocolademousse OF appeltaart", "Frietjes OF stokbrood"], "antwoord": 0, "uitleg": "Voorgerecht (entrée): 'Salade de chèvre chaud OU Soupe à l'oignon'."},
    {"type": "mc", "vraag": "Lees de recensie: <i>'Service rapide et souriant, les plats sont faits maison avec des produits frais du terroir. Je recommande les yeux fermés !'</i><br>Wat is het oordeel van de klant?", "opties": ["Uiterst positief: snelle bediening en verse huisgemaakte streekproducten", "Zeer negatief: traag en eten smaakte niet vers", "Te duur voor wat je krijgt", "De ober was onvriendelijk"], "antwoord": 0, "uitleg": "'Recommander les yeux fermés' is een Franse uitdrukking voor een absolute aanrader."},
    {"type": "waaronwaar", "vraag": "De vermelding <b>'fait maison'</b> op een Franse menukaart betekent dat het gerecht vers in het restaurant zelf is bereid.", "antwoord": True, "uitleg": "Waar. 'Fait maison' is een officieel Frans kwaliteitslabel voor huisgemaakt eten."},
    {"type": "invul", "vraag": "Wat betekent het Franse woord <b>'frais'</b> in: <i>'Poissons frais du jour'</i>?", "antwoord": "vers|dagvers", "uitleg": "'Frais' betekent vers."},
    {"type": "mc", "vraag": "Lees het recept voor pannenkoeken: <i>'Mélangez 250g de farine, 3 œufs, 500ml de lait et une pincée de sel. Laissez reposer la pâte 30 minutes.'</i><br>Hoe lang moet het beslag rusten?", "opties": ["30 minuten", "2 uur", "5 minuten", "De hele nacht"], "antwoord": 0, "uitleg": "'Laissez reposer la pâte 30 minutes'."},
    {"type": "waaronwaar", "vraag": "Het Franse woord <b>'la farine'</b> betekent boter.", "antwoord": False, "uitleg": "Onwaar. 'La farine' is meel / bloem. Boter is 'le beurre'."},
    {"type": "invul", "vraag": "Vertaal het ingrediënt <b>'les œufs'</b> naar het Nederlands:", "antwoord": "eieren|de eieren|ei", "uitleg": "Les œufs = de eieren."},
    {"type": "mc", "vraag": "Lees de mededeling: <i>'Cuisine ouverte sans interruption de 12h à 23h tous les week-ends.'</i><br>Wat betekent 'sans interruption'?", "opties": ["Doorlopend geopend zonder middagsluiting", "Alleen open tussen 12 en 13 uur", "Alleen afhalen mogelijk", "Geopend op afspraak"], "antwoord": 0, "uitleg": "'Sans interruption' betekent continu doorlopend open."},
    {"type": "mc", "vraag": "Wat betekent het signaalwoord <b>'d'abord'</b> in een kookinstructie?", "opties": ["eerst / om te beginnen", "tenslotte", "nooit", "ongeveer"], "antwoord": 0, "uitleg": "'D'abord' = eerst."},
    {"type": "waaronwaar", "vraag": "In de zin <i>'Plat végétarien adapté aux personnes intolérantes au gluten'</i> is het gerecht geschikt voor mensen met glutenintolerantie.", "antwoord": True, "uitleg": "Waar. 'Adapté aux personnes intolérantes au gluten'."},
    {"type": "invul", "vraag": "Wat betekent het Franse woord <b>'le sucre'</b>?", "antwoord": "suiker|de suiker", "uitleg": "'Le sucre' = de suiker."},
    {"type": "mc", "vraag": "Lees de recensie: <i>'Très déçu. Nous avons attendu plus d'une heure pour recevoir nos plats froids. À éviter !'</i><br>Waarom raadt de bezoeker het restaurant af?", "opties": ["Ze moesten meer dan een uur wachten en kregen koude gerechten", "De muziek stond te zacht", "De porties waren veel te groot", "Er was geen parkeerplek"], "antwoord": 0, "uitleg": "'Plus d'une heure d'attente' en 'plats froids'."},
    {"type": "open", "vraag": "Lees: <i>'Menu enfant (-12 ans) à 9,50€ : Nuggets de poulet ou burger + frites + sirop à l'eau + glace vanille ou crêpe au sucre.'</i><br>Welke twee toetjes kan een kind kiezen?", "sleutelwoorden": ["glace/vanille/ijs/vanille-ijs", "crêpe/crepe/suiker/pannekoek/pannenkoek"], "minTreffers": 2, "modelantwoord": "Vanille-ijs (glace vanille) of een suikerpannenkoek (crêpe au sucre).", "uitleg": "Dessertkeuze: glace vanille of crêpe au sucre."},
    {"type": "mc", "vraag": "Wat betekent <b>'À éviter'</b> aan het eind van een restaurantrecensie?", "opties": ["Te vermijden / Afrader", "Zeer aanbevolen", "Kom vroeg", "Goede prijs-kwaliteit"], "antwoord": 0, "uitleg": "'À éviter' betekent te vermijden / afrader."},
    {"type": "waaronwaar", "vraag": "Het Franse woord <b>'le sel'</b> betekent peper.", "antwoord": False, "uitleg": "Onwaar. 'Le sel' is zout. Peper is 'le poivre'."},
    {"type": "invul", "vraag": "Wat betekent <b>'le poivre'</b> in het Nederlands?", "antwoord": "peper|de peper", "uitleg": "'Le poivre' = peper."},
    {"type": "mc", "vraag": "Lees de aanbieding: <i>'Happy Hour de 17h à 19h : un verre acheté = un verre offert !'</i><br>Wat houdt de aanbieding in?", "opties": ["Bij aankoop van één drankje krijg je het tweede drankje gratis", "Alle drankjes kosten 1 euro", "Gratis hapjes voor iedereen", "Drankjes zijn verboden voor 19 uur"], "antwoord": 0, "uitleg": "'Un verre acheté = un verre offert' (1 kopen = 1 gratis)."},
    {"type": "waaronwaar", "vraag": "Het Franse werkwoord <b>'goûter'</b> betekent 'proeven'.", "antwoord": True, "uitleg": "Waar. 'Goûter' = proeven (ook 'het vieruurtje' voor kinderen)."},
    {"type": "invul", "vraag": "Vertaal het woord <i>'smaak'</i> of <i>'parfum (van ijs)'</i>: <i>Quels ... de glace avez-vous ?</i>", "antwoord": "parfums|goûts|gouts", "uitleg": "Parfums de glace (ijssmaken)."},
    {"type": "mc", "vraag": "Wat is het doel van een artikel getiteld: <i>'Les secrets de la baguette de tradition française'</i>?", "opties": ["Uitleggen waarom het traditionele Franse stokbrood zo bijzonder en uniek is", "Reclame maken voor voorverpakt toastbrood", "Mensen afraden om brood te eten", "De sluiting van dorpsbakkerijen aankondigen"], "antwoord": 0, "uitleg": "Het artikel bespreekt de traditie van het ambachtelijke Franse stokbrood."}
  ]
}

# EXAMEN 25: Eindtoets Unité 5 (Mix & Examentraining)
ex25 = {
  "id": "ex-h3-frans-25",
  "hoofdstuk": 5,
  "hoofdstukTitel": "Unité 5 — Au resto!",
  "titel": "Toets 5 — Unité 5 Eindtoets (Mix & Examentraining)",
  "vak": "Frans · HAVO 3 (U5)",
  "icoon": "🏆",
  "duurMin": 30,
  "vragen": [
    {"type": "mc", "vraag": "Wat betekent <b>'l'addition'</b>?", "opties": ["de rekening in een café/restaurant", "het dagmenu", "de fooi", "het reserveringsboek"], "antwoord": 0, "uitleg": "L'addition = de rekening."},
    {"type": "mc", "vraag": "Kies het juiste delend lidwoord: <i>Je voudrais ... (wat) eau minérale, s'il vous plaît.</i>", "opties": ["de l'", "du", "de la", "des"], "antwoord": 0, "uitleg": "De l'eau (begint met een klinker)."},
    {"type": "waaronwaar", "vraag": "In een ontkennende zin verandert <i>du, de la, des</i> altijd in <b>de / d'</b> (bijv. <i>Je ne veux pas de dessert</i>).", "antwoord": True, "uitleg": "Waar. Na ontkenning altijd 'de' of 'd''. "},
    {"type": "invul", "vraag": "Vervoeg <b>boire</b> bij <i>nous</i>: <i>Nous ... du jus de pomme.</i>", "antwoord": "buvons", "uitleg": "Nous buvons."},
    {"type": "mc", "vraag": "Hoe vraag je beleefd om de menukaart?", "opties": ["La carte, s'il vous plaît !", "Donnez-moi votre assiette !", "Où sont les couteaux ?", "Combien coûte le cuisinier ?"], "antwoord": 0, "uitleg": "'La carte, s'il vous plaît !'."},
    {"type": "waaronwaar", "vraag": "Het Franse woord <b>'le plat principal'</b> betekent het nagerecht.", "antwoord": False, "uitleg": "Onwaar. 'Le plat principal' is het hoofdgerecht."},
    {"type": "invul", "vraag": "Vul aan (geen melk): <i>Il n'y a plus ... lait dans le frigo.</i>", "antwoord": "de", "uitleg": "Plus de lait (ontkenning/hoeveelheid + de)."},
    {"type": "mc", "vraag": "Vervoeg <b>vouloir</b> voor <i>je</i>:", "opties": ["veux", "veut", "voulons", "voulez"], "antwoord": 0, "uitleg": "Je veux (ik wil / ik zou graag willen)."},
    {"type": "mc", "vraag": "Wat is <b>'le pourboire'</b>?", "opties": ["de fooi", "de menukaart", "de soep", "het bestek"], "antwoord": 0, "uitleg": "Le pourboire = de fooi."},
    {"type": "waaronwaar", "vraag": "De zin <i>'Je prends du poulet et des frites'</i> gebruikt het delend lidwoord correct.", "antwoord": True, "uitleg": "Waar. Du poulet (mannelijk) en des frites (meervoud)."},
    {"type": "invul", "vraag": "Vertaal het woord <i>lunch / middagmaaltijd</i> naar het Frans: <i>À midi, je prends le ... .</i>", "antwoord": "déjeuner|dejeuner", "uitleg": "Le déjeuner."},
    {"type": "mc", "vraag": "Wat betekent <b>'fait maison'</b>?", "opties": ["huisgemaakt / vers bereid door het restaurant", "kant-en-klaar ingekocht", "alleen thuis te bezorgen", "bereid door de gast zelf"], "antwoord": 0, "uitleg": "Fait maison = huisgemaakt."},
    {"type": "open", "vraag": "Leg uit hoe je in het Frans vraagt of je een tafeltje voor twee personen kunt krijgen bij het raam.", "sleutelwoorden": ["table", "deux/2/personnes", "fenêtre/fenetre/près/pres"], "minTreffers": 2, "modelantwoord": "Bonjour, une table pour deux personnes près de la fenêtre, s'il vous plaît.", "uitleg": "Une table pour deux près de la fenêtre, s'il vous plaît."},
    {"type": "mc", "vraag": "Kies de juiste combinatie: <i>Elle mange ... (wat) salade et boit ... (wat) thé.</i>", "opties": ["de la / du", "du / de la", "des / de l'", "la / le"], "antwoord": 0, "uitleg": "De la salade (vrouwelijk) + du thé (mannelijk)."},
    {"type": "waaronwaar", "vraag": "Het Franse woord <b>'les légumes'</b> betekent fruit.", "antwoord": False, "uitleg": "Onwaar. 'Les légumes' zijn groenten. Fruit is 'les fruits'."},
    {"type": "invul", "vraag": "Vul het woord in voor <i>mes</i>: <i>Il me manque un ... pour couper la viande.</i>", "antwoord": "couteau", "uitleg": "Un couteau = een mes."},
    {"type": "mc", "vraag": "Wat betekent <b>'avoir soif'</b>?", "opties": ["dorst hebben", "honger hebben", "moe zijn", "koud zijn"], "antwoord": 0, "uitleg": "Avoir soif = dorst hebben."},
    {"type": "waaronwaar", "vraag": "Na woorden van hoeveelheid (zoals <i>un kilo de</i>) gebruik je nooit <i>du</i> of <i>de la</i>.", "antwoord": True, "uitleg": "Waar. Na hoeveelheden staat altijd alleen 'de/d''. "},
    {"type": "invul", "vraag": "Vertaal naar het Frans (vork): <i>Une ... , s'il vous plaît.</i>", "antwoord": "fourchette", "uitleg": "La fourchette = de vork."},
    {"type": "mc", "vraag": "Vervoeg <b>boire</b> bij <i>ils/elles</i>:", "opties": ["boivent", "buvons", "buvent", "boit"], "antwoord": 0, "uitleg": "Ils/elles boivent."}
  ]
}

write_examen("examen_21.js", ex21)
write_examen("examen_22.js", ex22)
write_examen("examen_23.js", ex23)
write_examen("examen_24.js", ex24)
write_examen("examen_25.js", ex25)
print("Frans Unité 5 exams (21 to 25) generated successfully!")

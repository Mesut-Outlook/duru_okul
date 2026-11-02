#!/usr/bin/env python3
"""Gedeeld schrijfdeel voor geschiedenis H1 konu-toetsen (examen_36…45) — gen_geschiedenis_h1_{a,b,c}.py."""
import json, os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_economie_extra import M, W, I, O, plaats, langste_aandeel  # noqa: F401 (M/W/I/O voor de data-scripts)

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'havo3', 'geschiedenis', 'js', 'data')

# Opus-denetimi 2026-11-01: dar konulu testlerde aynı testin başka sorusu cevabı veriyordu; teori dışı ayrıntı; haksız open.
CORRECTIES = {
    (36, 2): M("Waarom hadden de spoorwegen behoefte aan één landelijke tijd?", "Voor een strakke dienstregeling",
               ["Om fabrieken langer open te houden", "Om de zonnetijd overal in te voeren", "Om de telegraafdraden overbodig te maken"],
               "Met elke plaats een andere tijd was geen strakke dienstregeling te maken (§1.1)."),
    (36, 8): M("Wat hadden de stationsklokken van 1846 en de tijdzones van 1891 gemeen?", "Beide hielpen het treinverkeer",
               ["Beide waren een gevolg van de oorlog", "Beide begonnen in Nederland", "Beide bespaarden veel steenkool"],
               "De klokken en de tijdzones kwamen er door de spoorwegen en het internationale treinverkeer (§1.1)."),
    (36, 16): I("Europa werd in 1891 verdeeld in ____ tijdzones.", "drie|3", "West-, Midden- en Oost-Europese tijd: drie zones (§1.1)."),
    (36, 17): I("Pas in het jaar ____ kwam in Nederland de Midden-Europese tijd, tijdens de Duitse bezetting.", "1940", "De Midden-Europese tijd kwam tijdens de bezetting van 1940 (§1.1)."),
    (36, 19): I("De zomertijd van 1916 moest kolen en ____ besparen.", "energie", "Duitsland en Oostenrijk wilden kolen en energie sparen voor de oorlogsvoering (§1.1)."),
    (37, 3): M("Welke jaren horen bij la belle époque?", "1890–1914", ["1870–1900", "1900–1918", "1914–1918"],
               "La belle époque liep van 1890 tot het uitbreken van de oorlog in 1914 (§1.1)."),
    (37, 12): W("Met de stopwatch van 1896 kon men tijden alleen in hele minuten meten.", False,
                "Niet waar. De stopwatch mat tot op tienden van seconden (§1.1)."),
    (37, 13): W("In la belle époque werden de werkdagen langer en de lonen lager.", False,
                "Niet waar. De werkdagen werden korter en de lonen hoger (§1.1)."),
    (37, 16): I("Boeken van Tolstoi, Hugo en ____ hoorden bij de cultuur van la belle époque.", "Dickens", "Tolstoi, Hugo en Dickens worden genoemd bij toerisme en cultuur (§1.1)."),
    (37, 17): I("Mensen zochten lichaamsbeweging omdat ze steeds vaker op ____ werkten.", "kantoor|een kantoor", "De moderne samenleving: werken op kantoor en daarom sport zoeken (§1.1)."),
    (37, 18): I("De stopwatch mat tijden tot op ____ van seconden.", "tienden|tiende", "De pas uitgevonden stopwatch mat in tienden van seconden (§1.1)."),
    (37, 19): I("La belle époque betekent letterlijk 'het mooie ____'.", "tijdperk", "De Fransen noemden de periode achteraf 'het mooie tijdperk' (§1.1)."),
    (37, 20): O("Leg uit wat er in la belle époque veranderde voor het werk én voor de gezondheid.", ["werkdagen/lonen", "hygiëne/ziektes"], 2,
                "Werkdagen werden korter en lonen hoger, en door betere hygiëne waren er minder ziektes.",
                "Kortere werkdagen en hogere lonen, betere hygiëne en minder ziektes (§1.1)."),
    (38, 8): M("Hoe snel raakte heel Europa in oorlog na de oorlogsverklaring aan Servië?", "Binnen een week", ["Binnen een jaar", "Binnen drie maanden", "Binnen een dag"],
               "Door het netwerk van bondgenootschappen raakte heel Europa binnen een week in oorlog (§1.2)."),
    (38, 12): W("Duitsland en Oostenrijk-Hongarije stonden in de oorlog tegenover elkaar.", False,
                "Niet waar. Beide hoorden bij de Centralen (§1.2)."),
    (38, 16): I("Het geheime netwerk van afspraken tussen landen (als X wordt aangevallen, helpt Y) noemen we de ____.", "bondgenootschappen|bondgenootschap", "Die afspraken zorgden ervoor dat een conflict zich snel uitbreidde (§1.2)."),
    (38, 18): I("Princip schoot in Sarajevo ook de vrouw van de troonopvolger dood. Zij heette ____.", "Sophie", "Frans Ferdinand en zijn vrouw Sophie werden doodgeschoten (§1.2)."),
    (38, 19): I("Wie soldaten bewondert en militaire waarden verheerlijkt, hangt het ____ aan.", "militarisme", "Militarisme is de verheerlijking van het leger, soldaten en militaire waarden (§1.2)."),
    (38, 20): O("Leg uit hoe de twee oorzaken die met trots op het eigen volk en met het opbouwen van legers te maken hebben de spanning rond 1914 verhoogden.",
                ["nationalisme/superieur/eigen land", "wapenwedloop/modernste/sterkste/race"], 2,
                "Door nationalisme geloofde elk land superieur te zijn, en door de wapenwedloop probeerden landen het modernste leger op te bouwen.",
                "Nationalisme en de wapenwedloop verhoogden de spanning tussen de landen (§1.2)."),
    (39, 3): M("Waardoor kwamen aan het Westfront miljoenen soldaten om?", "Machinegeweren, granaten en gifgas",
               ["Tanks, duikboten en honger", "Sneeuw, kou en ziektes", "Vliegtuigen, kanonnen en sabels"],
               "Miljoenen soldaten kwamen om door machinegeweren, granaten en gifgas (§1.2)."),
    (39, 6): M("Waar vonden de dodenmarsen van de Armeense genocide plaats?", "In de woestijn van Syrië en Irak",
               ["In de bergen van Servië en Bosnië", "Op de vlakten van Polen en Litouwen", "In de loopgraven van het Westfront"],
               "De dodenmarsen waren in de woestijn van Syrië en Irak (§1.2)."),
    (39, 13): W("De Duitse opmars in het westen werd gestopt bij de Belgische kust.", False,
                "Niet waar. De opmars werd gestopt aan de rivier de Marne (§1.2)."),
    (39, 17): I("Aan de rivier de ____ werd de Duitse opmars gestopt.", "Marne", "Aan de Marne werd de Duitse opmars gestopt (§1.2)."),
    (39, 18): I("Volgens het Schlieffenplan moest Frankrijk in ____ weken verslagen zijn.", "7|zeven", "Het plan ging uit van 7 weken, daarna moesten de troepen naar Rusland (§1.2)."),
    (39, 19): I("De deportatie van de Armeniërs begon in ____ 1915.", "april", "Vanaf april 1915 volgden deportatie en executie (§1.2)."),
    (40, 7): M("Arbeiders en soldaten richten in 1917 een raad op die een fabriek gaat besturen. Hoe heet zo’n raad?", "Een sovjet",
               ["Een Doema", "Een Okhrana", "Een bolsjewiek"],
               "Sovjets waren raden van arbeiders en soldaten die fabrieken en legeronderdelen bestuurden (§1.3)."),
    (40, 9): M("Wat hadden de protesten van 1905 en de stakingen van 1917 met elkaar gemeen?", "Beide keren kwamen hongerige mensen in verzet door een oorlog",
               ["Beide keren greep Lenin de macht", "Beide keren werd Rusland een republiek", "Beide keren verloor de tsaar zijn troon"],
               "In 1905 volgde het protest op een verloren oorlog, in 1917 op honger en verliezen door de Eerste Wereldoorlog (§1.3)."),
    (41, 9): M("Welke reeks namen van de Russische stad klopt van oud naar nieuw?", "Sint-Petersburg, Petrograd, Leningrad, Sint-Petersburg",
               ["Leningrad, Petrograd, Sint-Petersburg, Leningrad", "Sint-Petersburg, Leningrad, Petrograd, Sint-Petersburg", "Petrograd, Sint-Petersburg, Leningrad, Petrograd"],
               "De stad heette 1703 Sint-Petersburg, 1914 Petrograd, 1924 Leningrad en sinds 1991 weer Sint-Petersburg (§1.3)."),
    (41, 19): I("Bij de communistische symbolen stond de hamer voor de arbeiders en de ____ voor de boeren.", "sikkel", "Hamer en sikkel waren de symbolen van arbeiders en boeren (§1.3)."),
    (42, 4): M("Welke bepaling trof Duitsland vooral in de portemonnee?", "De herstelbetalingen",
               ["Het verbod op vliegtuigen", "De alleenschuld voor de oorlog", "Het verlies van Oost-Pruisen"],
               "Herstelbetalingen betekenden miljarden goudmarken aan schadevergoeding (§1.4)."),
    (42, 9): M("Wat hadden de Volkenbond en het recht van volkeren op een eigen staat gemeen?", "Beide gingen terug op ideeën van de Amerikaanse president",
               ["Beide werden bedacht door de Britse premier Lloyd George", "Beide waren zware straffen voor het verslagen Duitsland", "Beide werden meteen goedgekeurd door het Amerikaanse Congres"],
               "Wilson nam het initiatief tot de Volkenbond en bepleitte het zelfbeschikkingsrecht (§1.4)."),
    (43, 4): M("Waarom was de Griekse landing in Smyrna in 1919 voor Turken zo bedreigend?", "De Geallieerden wilden Turks gebied verdelen",
               ["De Grieken steunden Mustafa Kemal", "De Grieken wilden de republiek uitroepen", "De Grieken wilden Kemal president maken"],
               "De Geallieerden wilden Anatolië verdelen en de Grieken landden in Smyrna (§1.4)."),
    (43, 10): M("Een Griekse familie die generaties in Turkije woonde, moet in 1923 verhuizen. Waarop is dat gebaseerd?", "Het verdrag van Lausanne en de verplichte volkenruil",
                ["Het Verdrag van Versailles en de herstelbetalingen", "Het besluit over de mandaatgebieden van de Volkenbond", "Het zelfbeschikkingsrecht van president Wilson"],
                "Het verdrag van Lausanne regelde de verplichte volkenruil (§1.4)."),
    (43, 15): W("Joegoslavië was een nieuwe Balkanstaat voor onder meer Serviërs, Kroaten en Slovenen.", True,
                "Waar. Het koninkrijk Joegoslavië was bedoeld voor Serviërs, Kroaten, Slovenen en Bosniërs (§1.4)."),
    (43, 18): I("Uit Oostenrijk-Hongarije werden Tsjecho-Slowakije en ____ losgemaakt.", "Hongarije", "Tsjecho-Slowakije en Hongarije werden losgemaakt van Oostenrijk-Hongarije (§1.4)."),
    (43, 19): I("Kemal maakte een einde aan de oude vorm van bestuur door het ____ af te schaffen.", "sultanaat", "Kemal schafte het sultanaat af voordat de Republiek werd uitgeroepen (§1.4)."),
    (44, 2): M("Hoe werden de Belgische vluchtelingen in Nederland opgevangen?", "In scholen, tenten en gezinnen",
               ["In leegstaande fabrieken in de grote steden", "In kampen die door de Duitse bezetter werden beheerd", "In speciale kazernes van het Nederlandse leger"],
               "De vluchtelingen kregen onderdak in scholen, tenten en bij gezinnen (§1.5)."),
    (44, 11): W("Het Nederlandse leger stond de hele oorlog paraat aan de grenzen.", True,
                "Waar. Het leger hield de hele oorlog 200.000 militairen paraat (§1.5)."),
    (44, 14): W("Door de handelsblokkade en de duikbootoorlog kwamen er steeds minder goederen Nederland binnen.", True,
                "Waar. Blokkade en duikbootoorlog zorgden voor minder aanvoer en dus schaarste (§1.5)."),
    (44, 16): I("Het verdelen van schaarse producten door de overheid heet het ____.", "distributiestelsel|distributiesysteem|distributie", "Via het distributiestelsel verdeelde de overheid brood, vlees, koffie en steenkool (§1.5)."),
    (44, 17): I("Door de blokkade kwamen er steeds minder goederen binnen in de haven van ____.", "Rotterdam", "Er kwamen steeds minder goederen Rotterdam binnen (§1.5)."),
    (44, 18): I("Aan de Draad des Doods kwamen honderden mensen om door ____.", "elektrocutie|elektriciteit", "Het hekwerk stond onder hoogspanning; honderden mensen kwamen om door elektrocutie (§1.5)."),
    (44, 19): I("Het oproepen en paraat houden van het leger noemen we ____.", "mobilisatie|mobiliseren", "Nederland hield tijdens de oorlog 200.000 militairen paraat: de mobilisatie (§1.5)."),
    (45, 9): M("Welke politieke richting vertegenwoordigde Pieter Jelles Troelstra?", "Het socialisme",
               ["Het conservatisme", "Het liberalisme", "Het communisme"], "Troelstra was een socialistisch leider (§1.5)."),
    (45, 11): W("De kunstbeweging De Stijl werd opgericht in 1914, bij het begin van de oorlog.", False,
                "Niet waar. De Stijl werd opgericht in 1917 (§1.5)."),
    (45, 12): W("Duizenden mensen gingen in november 1918 de straat op om Troelstra's oproep te steunen.", False,
                "Niet waar. Troelstra kreeg amper steun; de betogers steunden juist de koningin (§1.5)."),
    (45, 14): W("In de Grondwetsherziening van 1917 werden twee politieke kwesties in één keer opgelost.", True,
                "Waar. De kiesrechtkwestie en de schoolstrijd werden samen opgelost (§1.5)."),
    (45, 19): I("Gerrit Rietveld was niet alleen meubelmaker, maar ook ____.", "architect", "Rietveld wordt meubelmaker en architect genoemd (§1.5)."),
}


def schrijf(examens, seed):
    """examens = {nr: (paragraaf, titel, icoon, [vragen])}; schrijft examen_<nr>.js."""
    rng = random.Random(seed)
    for nr, (par, titel, icoon, vr) in examens.items():
        vr = [CORRECTIES.get((nr, i), v) for i, v in enumerate(vr, 1)]
        t = [v["type"] for v in vr]
        assert (t.count("mc"), t.count("waaronwaar"), t.count("invul"), t.count("open")) == (10, 5, 4, 1), (nr, t)
        assert sum(v["type"] == "waaronwaar" and v["antwoord"] is False for v in vr) >= 2, nr
        vr = plaats([dict(v) for v in vr], rng)
        n, tot = langste_aandeel(vr)
        assert n / tot <= 0.4, f"examen_{nr}: juiste optie {n}/{tot} keer langste"
        for i, v in enumerate(vr, 1):
            vr[i - 1] = {"id": f"ex{nr}_v{i}", **v}
        ex = {
            "id": f"ex-h3-geschiedenis-{nr}",
            "titel": titel,
            "vak": "Geschiedenis · Hoofdstuk 1",
            "hoofdstuk": 1,
            "hoofdstukTitel": "Hoofdstuk 1 — De Eerste Wereldoorlog (1900–1920)",
            "paragraaf": par,
            "icoon": icoon,
            "duurMin": 20,
            "vragen": vr,
        }
        kop = f"/* =========================================================\n   Duru's Geschiedenis (HAVO 3) — {titel}\n   ========================================================= */\n"
        with open(os.path.join(ROOT, f"examen_{nr}.js"), 'w', encoding='utf-8') as f:
            f.write(kop + "DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")
        print(f"examen_{nr}: 20 vragen, juiste optie langste {n}/{tot}")

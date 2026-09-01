#!/usr/bin/env python3
import os
import json

BASE_DIR = "/home/mesuto/Documents/PROJELER/duru_okul/havo3/engels"
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

def write_examen(filename, data):
    balance_mc(data["vragen"])
    path = os.path.join(DATA_DIR, filename)
    content = f"""/* Proeftoets {data['titel']}
   Stepping Stones 3 HAVO Hoofdstuk {data['hoofdstuk']} */
DURU.registerExamen({json.dumps(data, indent=2, ensure_ascii=False)});
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  [✓] Examen saved: {filename}")

# EXAMEN 11: H3 Theme Words (Inventions & Tech) (20 questions)
ex11 = {
  "id": "ex-h3-eng-11",
  "hoofdstuk": 3,
  "hoofdstukTitel": "Hoofdstuk 3 — Science & technology",
  "titel": "Toets 1 — Theme Words: Inventions, AI & Modern Gadgets",
  "vak": "Engels · HAVO 3 (H3)",
  "icoon": "🔬",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "What is the crucial distinction between <b>discover</b> and <b>invent</b>?", "opties": ["Discover means finding something already existing in nature; invent means creating a new device or process", "Discover is used only for software apps; invent is used for biological plants", "There is no difference in modern science", "Invent means finding ancient fossils in rocks"], "antwoord": 0, "uitleg": "Ontdekken is iets bestaands vinden; uitvinden is iets nieuws ontwerpen."},
    {"type": "mc", "vraag": "What does <b>AI</b> stand for?", "opties": ["Artificial Intelligence", "Automated Information", "Advanced Invention", "Applied Industry"], "antwoord": 0, "uitleg": "Artificial Intelligence is Kunstmatige Intelligentie."},
    {"type": "waaronwaar", "vraag": "A <b>rechargeable</b> battery must be discarded immediately after its initial charge runs out.", "antwoord": False, "uitleg": "Onwaar. Een oplaadbare batterij kan vele malen opnieuw opgeladen worden."},
    {"type": "invul", "vraag": "Fill in the noun for <i>doorbraak</i>: <i>Genetic researchers achieved a medical ... in vaccine design.</i>", "antwoord": "breakthrough", "uitleg": "Breakthrough is een wetenschappelijke doorbraak."},
    {"type": "mc", "vraag": "Which adjective describes a device that accomplishes its purpose with minimal waste of energy or time?", "opties": ["Efficient", "Defective", "Clunky", "Hazardous"], "antwoord": 0, "uitleg": "Efficient betekent energiezuinig en doelmatig."},
    {"type": "waaronwaar", "vraag": "A <b>sensor</b> is an electronic component that detects changes in light, temperature, or motion.", "antwoord": True, "uitleg": "Waar. Een sensor registreert fysieke signalen."},
    {"type": "invul", "vraag": "Fill in the verb (ontdekken): <i>Alexander Fleming ... penicillin by accident in 1928.</i>", "antwoord": "discovered", "uitleg": "Discovered (ontdekte)."},
    {"type": "mc", "vraag": "What does <b>Virtual Reality (VR)</b> technology provide?", "opties": ["An interactive, computer-generated 3D simulated environment", "A high-speed wired printer network", "A mechanical typewriting machine", "A paper-based compass"], "antwoord": 0, "uitleg": "VR biedt een immersieve virtuele 3D-wereld."},
    {"type": "mc", "vraag": "What is a <b>gadget</b>?", "opties": ["A small, handy electronic device or mechanical tool with a practical purpose", "A heavy piece of industrial factory machinery", "A large historical stone monument", "An ancient handwritten document"], "antwoord": 0, "uitleg": "A gadget is een handig technologisch apparaatje."},
    {"type": "waaronwaar", "vraag": "An <b>algorithm</b> is a set of step-by-step mathematical rules followed by computers to solve problems.", "antwoord": True, "uitleg": "Waar. Een algoritme is een stappenplan voor computers."},
    {"type": "invul", "vraag": "Fill in the noun (innovatie / vernieuwing): <i>Technological ... drives modern economic growth.</i>", "antwoord": "innovation", "uitleg": "Innovation is innovatie."},
    {"type": "mc", "vraag": "What does <b>automated</b> mean when describing a modern warehouse?", "opties": ["Operated largely by computerized machines and robots without human manual labor", "Powered entirely by steam and coal", "Closed to all electrical power", "Managed by horses and carriages"], "antwoord": 0, "uitleg": "Automated betekent geautomatiseerd met robots."},
    {"type": "open", "vraag": "Explain how artificial intelligence (AI) can assist doctors in diagnosing medical conditions.", "sleutelwoorden": ["scans/x-rays/images/faster/patterns/accurate/detect"], "minTreffers": 1, "modelantwoord": "AI can quickly analyze thousands of medical scans and data to detect disease patterns faster and accurately.", "uitleg": "AI kan medische scans en data razendsnel analyseren op afwijkingen."},
    {"type": "mc", "vraag": "Which device converts sunlight directly into electrical energy?", "opties": ["A solar cell / solar panel", "A wind turbine", "A diesel engine", "A water pump"], "antwoord": 0, "uitleg": "Solar panels zetten zonlicht om in elektriciteit."},
    {"type": "waaronwaar", "vraag": "Alexander Graham Bell is widely recognized for discovering the planet Mars.", "antwoord": False, "uitleg": "Onwaar. Bell vond de telefoon uit (telephone), niet de planeet Mars."},
    {"type": "invul", "vraag": "Fill in the noun for <i>laboratorium</i>: <i>Chemists wear protective goggles inside the science ... .</i>", "antwoord": "laboratory|lab", "uitleg": "Laboratory (of lab) is een laboratorium."},
    {"type": "mc", "vraag": "What is <b>robotics</b>?", "opties": ["The branch of technology dealing with the design, construction, and operation of robots", "The study of ancient rock formations", "The art of painting with watercolors", "The practice of planting organic trees"], "antwoord": 0, "uitleg": "Robotics is de robotica."},
    {"type": "waaronwaar", "vraag": "A smartphone combines the functions of a phone, camera, internet browser, and computer in one pocket device.", "antwoord": True, "uitleg": "Waar. Smartphones zijn multifunctionele apparaten."},
    {"type": "invul", "vraag": "Fill in the missing word: <i>Smartwatches are popular wearable ... .</i>", "antwoord": "devices|gadgets", "uitleg": "Wearable devices / gadgets."},
    {"type": "mc", "vraag": "Which phrase describes a major scientific test conducted under controlled conditions?", "opties": ["An experiment", "A vacation", "A translation", "A festival"], "antwoord": 0, "uitleg": "An experiment is een wetenschappelijk experiment."}
  ]
}

# EXAMEN 12: H3 Grammar (Present Perfect vs Past Simple) (20 questions)
ex12 = {
  "id": "ex-h3-eng-12",
  "hoofdstuk": 3,
  "hoofdstukTitel": "Hoofdstuk 3 — Science & technology",
  "titel": "Toets 2 — Grammar: Present Perfect vs. Past Simple",
  "vak": "Engels · HAVO 3 (H3)",
  "icoon": "⌛",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Which sentence correctly uses the <b>Present Perfect</b> for an unfinished life experience?", "opties": ["I have visited London three times in my life.", "I visited London three times in my life so far.", "I was visiting London in 2020 already.", "I am visit London three times."], "antwoord": 0, "uitleg": "Present Perfect (have visited) voor levenservaringen tot nu toe."},
    {"type": "mc", "vraag": "Choose the correct signal word: <i>Have the engineers completed the drone test ...?</i>", "opties": ["yet", "yesterday", "ago", "last week"], "antwoord": 0, "uitleg": "'Yet' staat aan het einde van vraagzinnen in de Present Perfect."},
    {"type": "waaronwaar", "vraag": "When an exact finished time in the past is mentioned (e.g. <i>in 1989</i>), you must use the Present Perfect.", "antwoord": False, "uitleg": "Onwaar. Bij een afgesloten tijdstip gebruik je de Past Simple."},
    {"type": "invul", "vraag": "Fill in <i>for</i> or <i>since</i>: <i>Google has operated as a major search engine ... 1998.</i>", "antwoord": "since", "uitleg": "Since voor een specifiek jaartal (startpunt)."},
    {"type": "mc", "vraag": "Choose the correct verb: <i>Tim Berners-Lee ... (to invent) the World Wide Web in 1989.</i>", "opties": ["invented", "has invented", "have invented", "is inventing"], "antwoord": 0, "uitleg": "'In 1989' is een afgesloten tijdstip -> Past Simple (invented)."},
    {"type": "waaronwaar", "vraag": "The word <b>just</b> in Present Perfect sentences indicates that the action happened very recently.", "antwoord": True, "uitleg": "Waar. 'Just' betekent zojuist / net."},
    {"type": "invul", "vraag": "Fill in the Present Perfect of <i>(to build)</i>: <i>The robotics team ... a self-driving prototype.</i>", "antwoord": "has built", "uitleg": "The team (it) -> has built."},
    {"type": "mc", "vraag": "Which question demonstrates the correct word order in the Present Perfect?", "opties": ["Have you ever programmed a mobile app before?", "Did you ever programmed an app?", "Are you ever program an app?", "Have you ever program an app?"], "antwoord": 0, "uitleg": "Have + you + ever + voltooid deelwoord (programmed)."},
    {"type": "mc", "vraag": "Why is <i>'She has bought this laptop yesterday'</i> incorrect?", "opties": ["Yesterday indicates a finished past time, which strictly requires the Past Simple 'bought'", "Bought cannot be used with laptop", "She requires have instead of has", "Yesterday must be placed between has and bought"], "antwoord": 0, "uitleg": "Yesterday vereist de Past Simple: 'She bought this laptop yesterday'."},
    {"type": "waaronwaar", "vraag": "The preposition <b>for</b> is used with a period of duration (e.g. <i>for three years</i>).", "antwoord": True, "uitleg": "Waar. 'For' geeft een tijdsduur aan."},
    {"type": "invul", "vraag": "Fill in <i>for</i> or <i>since</i>: <i>They have tested the new software ... two hours.</i>", "antwoord": "for", "uitleg": "For two hours (tijdsduur)."},
    {"type": "mc", "vraag": "Choose the correct verb form: <i>Look! The battery has ... (to run) out of power.</i>", "opties": ["run", "ran", "running", "runs"], "antwoord": 0, "uitleg": "Voltooid deelwoord van run is run (run - ran - run)."},
    {"type": "open", "vraag": "Explain the difference between losing keys in the past versus currently missing keys.", "sleutelwoorden": ["finished/yesterday/earlier", "result/current/still/missing/now"], "minTreffers": 1, "modelantwoord": "'I lost my keys' is past, while 'I have lost my keys' has a direct result in the present (they are still missing now).", "uitleg": "De Present Perfect toont een direct resultaat in het heden (ik ben ze nu nog kwijt)."},
    {"type": "mc", "vraag": "Which sentence indicates that an action already happened earlier than expected?", "opties": ["We have already installed the security update.", "We have not installed the update yet.", "We will install the update next year.", "We install the update yesterday."], "antwoord": 0, "uitleg": "'Already' geeft aan dat iets al gebeurd is."},
    {"type": "waaronwaar", "vraag": "The past participle (3e rijtje) of the irregular verb <i>write</i> is <i>wrote</i>.", "antwoord": False, "uitleg": "Onwaar. Write -> wrote (past simple) -> written (past participle)."},
    {"type": "invul", "vraag": "Fill in the negative Present Perfect of <i>(to see)</i>: <i>I ... this new VR headset yet.</i>", "antwoord": "have not seen|haven't seen", "uitleg": "I have not seen / haven't seen."},
    {"type": "mc", "vraag": "Choose the correct verb pair: <i>My brother ... (to start) coding when he was eight, and he ... (to create) dozens of games since then.</i>", "opties": ["started / has created", "has started / created", "starts / was creating", "started / created"], "antwoord": 0, "uitleg": "'When he was eight' = Past Simple (started); 'since then' = Present Perfect (has created)."},
    {"type": "waaronwaar", "vraag": "In the sentence <i>'She has worked here since Monday'</i>, she still works there today.", "antwoord": True, "uitleg": "Waar. Present Perfect met 'since' loopt door tot in het heden."},
    {"type": "invul", "vraag": "Fill in the missing word: <i>Have you ... flown in a helicopter?</i>", "antwoord": "ever", "uitleg": "'Ever' (ooit) in vraagzinnen."},
    {"type": "mc", "vraag": "What is the past participle of <b>to go</b> when someone has left and returned?", "opties": ["Been", "Gone", "Went", "Goes"], "antwoord": 0, "uitleg": "'Been' als iemand gegaan en teruggekeerd is ('gone' als diegene er nu nog is)."}
  ]
}

# EXAMEN 13: H3 Stones & Tech Explanations (20 questions)
ex13 = {
  "id": "ex-h3-eng-13",
  "hoofdstuk": 3,
  "hoofdstukTitel": "Hoofdstuk 3 — Science & technology",
  "titel": "Toets 3 — Stones & Skills: Explaining Tech & Instructions",
  "vak": "Engels · HAVO 3 (H3)",
  "icoon": "⚙️",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "Which phrase is used to explain the main purpose of an invention?", "opties": ["This device is designed to measure heart rate during exercise.", "This device was painted by an artist in Paris.", "This device dislikes cold water.", "This device is asleep right now."], "antwoord": 0, "uitleg": "'This device is designed to...' legt het gebruiksdoel uit."},
    {"type": "mc", "vraag": "What is the best sequencing word to begin a technical instruction manual?", "opties": ["First of all / Firstly,", "Finally / In conclusion,", "Suddenly / Out of nowhere,", "Meanwhile / Later,"], "antwoord": 0, "uitleg": "'First of all' leidt de eerste stap in."},
    {"type": "waaronwaar", "vraag": "The word <b>drawback</b> is a synonym for an important technical advantage.", "antwoord": False, "uitleg": "Onwaar. Drawback is een nadeel of minpunt."},
    {"type": "invul", "vraag": "Fill in the missing word: <i>This wireless feature ... users to stream music without cables.</i>", "antwoord": "enables|allows", "uitleg": "Enables / allows (stelt gebruikers in staat)."},
    {"type": "mc", "vraag": "What does a product's <b>user interface (UI)</b> refer to?", "opties": ["The visual screen, buttons, and menus through which a user controls the software", "The cardboard box in which the product is shipped", "The credit card receipt from the shop", "The electrical voltage in the wall outlet"], "antwoord": 0, "uitleg": "De gebruikersinterface (UI) omvat schermen en knoppen."},
    {"type": "waaronwaar", "vraag": "In technical writing, the word <i>cons</i> refers to the negative aspects or disadvantages of a product.", "antwoord": True, "uitleg": "Waar. Cons zijn nadelen."},
    {"type": "invul", "vraag": "Fill in the sequencing connector: <i>First insert the battery; ..., turn on the power switch.</i>", "antwoord": "then|next|after that", "uitleg": "Then / next / after that verbindt de stappen."},
    {"type": "mc", "vraag": "How do you state a product's major advantage in a review?", "opties": ["The greatest benefit of this laptop is its ultra-fast processor.", "The price is too high for students.", "The screen cracked immediately.", "The manual is missing."], "antwoord": 0, "uitleg": "'The greatest benefit of...' benadrukt het grootste voordeel."},
    {"type": "mc", "vraag": "Which phrase provides a balanced summary in a tech review?", "opties": ["Overall, despite the high price, the outstanding build quality makes it worth buying.", "Throw this product into the garbage immediately.", "Never buy any electronics online.", "I don't understand how batteries work."], "antwoord": 0, "uitleg": "Een afgewogen oordeel weegt prijs en kwaliteit tegen elkaar af."},
    {"type": "waaronwaar", "vraag": "The term <i>plug-and-play</i> means a device requires five hours of complex manual wiring before use.", "antwoord": False, "uitleg": "Onwaar. Plug-and-play betekent direct klaar voor gebruik zonder moeilijke installatie."},
    {"type": "invul", "vraag": "Complete the phrase: <i>The only ... is that the battery drains rather quickly.</i>", "antwoord": "downside|drawback|disadvantage", "uitleg": "Downside / drawback / disadvantage is het nadeel."},
    {"type": "mc", "vraag": "How do you ask for technical assistance politely in an electronics store?", "opties": ["Could you explain how to set up the Bluetooth pairing mode?", "Fix this now!", "Why is technology so complicated?", "Give me a free smartphone!"], "antwoord": 0, "uitleg": "Beleefde vraag om technische hulp."},
    {"type": "open", "vraag": "List one significant positive benefit and one limitation of using AI in homework assignments.", "sleutelwoorden": ["explains/helps/ideas/fast/support", "lazy/inaccurate/mistakes/reliance/cheat"], "minTreffers": 1, "modelantwoord": "A benefit is that AI explains difficult concepts quickly; a limitation is that students might rely on it too much and not think for themselves.", "uitleg": "Een voordeel is snelle uitleg; een nadeel is luiheid of minder zelfstandig nadenken."},
    {"type": "mc", "vraag": "What is the meaning of <b>compatible</b> in computer hardware?", "opties": ["Able to function or communicate with other devices without conflict", "Expensive and fragile", "Broken and defective", "Made entirely of green plastic"], "antwoord": 0, "uitleg": "Compatible betekent uitwisselbaar en compatibel met andere apparaten."},
    {"type": "waaronwaar", "vraag": "The phrase <i>'Step-by-step instructions'</i> means instructions presented in a clear, sequential order.", "antwoord": True, "uitleg": "Waar. Stapsgewijze instructies volgen elkaar logisch op."},
    {"type": "invul", "vraag": "Complete the instructional step: <i>..., restart the computer to complete the installation.</i>", "antwoord": "finally|lastly", "uitleg": "'Finally' sluit de instructiereeks af."},
    {"type": "mc", "vraag": "Which phrase describes an app that is intuitive and easy to navigate?", "opties": ["Highly user-friendly", "Extremely confusing", "Completely unresponsive", "Totally obsolete"], "antwoord": 0, "uitleg": "User-friendly betekent gebruiksvriendelijk."},
    {"type": "waaronwaar", "vraag": "A <b>prototype</b> is the final mass-produced version of a product sold in millions of retail stores.", "antwoord": False, "uitleg": "Onwaar. Een prototype is een eerste testmodel."},
    {"type": "invul", "vraag": "Complete the review sentence: <i>I would highly ... this noise-cancelling headset to frequent travelers.</i>", "antwoord": "recommend", "uitleg": "'Highly recommend' betekent van harte aanbevelen."},
    {"type": "mc", "vraag": "What does <b>obsolete</b> mean regarding technology?", "opties": ["No longer produced or used, out of date", "Extremely modern and high-tech", "Rechargeable via solar energy", "Waterproof and durable"], "antwoord": 0, "uitleg": "Obsolete betekent verouderd en achterhaald."}
  ]
}

# EXAMEN 14: H3 Reading & Science Texts (20 questions)
ex14 = {
  "id": "ex-h3-eng-14",
  "hoofdstuk": 3,
  "hoofdstukTitel": "Hoofdstuk 3 — Science & technology",
  "titel": "Toets 4 — Reading Skills: Scientific Breakthroughs & Tech Texts",
  "vak": "Engels · HAVO 3 (H3)",
  "icoon": "📰",
  "duurMin": 25,
  "vragen": [
    {"type": "mc", "vraag": "What is the main goal of an informative scientific article?", "opties": ["To explain research findings, discoveries, and their real-world impact clearly to readers", "To sell fictional comic books", "To write rhyming poetry about machines", "To complain about laboratory budgets"], "antwoord": 0, "uitleg": "Een populairwetenschappelijk artikel legt ontdekkingen helder uit."},
    {"type": "mc", "vraag": "What does the term <b>renewable</b> imply in energy technology?", "opties": ["A resource naturally replenished on a human timescale, like wind or solar", "An energy source that produces heavy black smoke", "Fuel that can only be bought once a century", "Electricity that only works at night"], "antwoord": 0, "uitleg": "Hernieuwbare bronnen raken nooit op."},
    {"type": "waaronwaar", "vraag": "In a scientific text, diagrams and data graphs provide visual evidence supporting the written explanations.", "antwoord": True, "uitleg": "Waar. Grafieken en schema's ondersteunen de tekstuele uitleg."},
    {"type": "invul", "vraag": "Fill in the scientific noun (doorbraak): <i>The discovery of CRISPR gene editing was a monumental ... in biotechnology.</i>", "antwoord": "breakthrough", "uitleg": "Breakthrough is een doorbraak."},
    {"type": "mc", "vraag": "What is a <b>hypothesis</b> in scientific methodology?", "opties": ["A proposed testable explanation made on the basis of limited initial evidence", "A finished textbook published by Oxford University", "A mathematical guarantee of 100% truth", "An expensive laboratory microscope"], "antwoord": 0, "uitleg": "Een hypothese is een toetsbare veronderstelling."},
    {"type": "waaronwaar", "vraag": "Scientific peer review means articles are evaluated by independent experts in the same field before publication.", "antwoord": True, "uitleg": "Waar. Peer review waarborgt de wetenschappelijke kwaliteit."},
    {"type": "invul", "vraag": "Fill in the noun (gegevens / data): <i>Researchers collected massive amounts of digital ... for the climate model.</i>", "antwoord": "data", "uitleg": "Data betekent gegevens."},
    {"type": "mc", "vraag": "Which phrase describes a major concern about autonomous artificial intelligence?", "opties": ["Ethical dilemmas regarding privacy, algorithmic bias, and job automation", "Smartphones running out of screen wallpapers", "Headphones having different colors", "Keyboards needing cleaning"], "antwoord": 0, "uitleg": "Ethische vraagstukken rond privacy en werkgelegenheid."},
    {"type": "mc", "vraag": "What does <b>bionic</b> mean in modern prosthetics?", "opties": ["Having artificial body parts enhanced by electromechanical components", "Made exclusively of wood and cotton", "Painted in bright green colors", "Controlled by acoustic whistles"], "antwoord": 0, "uitleg": "Bionisch combineert biologie en elektronica."},
    {"type": "waaronwaar", "vraag": "A technological breakthrough always causes immediate harm to every person on Earth.", "antwoord": False, "uitleg": "Onwaar. Veel doorbraken genezen ziektes en verbeteren de levensstandaard."},
    {"type": "invul", "vraag": "Fill in the verb: <i>Scientists ... (to conduct) hundreds of lab experiments to verify the result.</i>", "antwoord": "conducted|carried out", "uitleg": "'Conducted experiments' (voerden experimenten uit)."},
    {"type": "mc", "vraag": "Why are subheadings effective in long science articles?", "opties": ["They divide complex content into manageable subtopics, helping readers navigate information", "They make the article appear shorter than it actually is", "They replace the need for full sentences", "They translate technical nouns into German"], "antwoord": 0, "uitleg": "Tussenkopjes structureren complexe materie."},
    {"type": "open", "vraag": "Why is it important for readers to verify the credibility of a news article found online?", "sleutelwoorden": ["misinformation/fake/accurate/reliable/facts/trusted/evidence"], "minTreffers": 1, "modelantwoord": "Verifying the source prevents the spread of fake news and ensures that the scientific information is accurate and trustworthy.", "uitleg": "Het controleren van bronnen voorkomt desinformatie en waarborgt betrouwbaarheid."},
    {"type": "mc", "vraag": "What does <b>cutting-edge technology</b> mean?", "opties": ["The most advanced, innovative stage in the development of a technology", "Dangerous sharp knives used in kitchens", "Outdated machines from the 19th century", "Wooden tools used in gardening"], "antwoord": 0, "uitleg": "Cutting-edge betekent hypermodern en baanbrekend."},
    {"type": "waaronwaar", "vraag": "The word <b>nanotechnology</b> deals with manipulating matter on an atomic and molecular scale.", "antwoord": True, "uitleg": "Waar. Nanotechnologie opereert op atomaire schaal."},
    {"type": "invul", "vraag": "Complete the phrase: <i>This groundbreaking invention could pave the ... for clean fusion energy.</i>", "antwoord": "way", "uitleg": "'Pave the way' betekent de weg vrijmaken voor."},
    {"type": "mc", "vraag": "What is the tone of an academic research summary?", "opties": ["Formal, objective, and evidence-based", "Informal, sarcastic, and humorous", "Emotional and superstitious", "Aggressive and argumentative"], "antwoord": 0, "uitleg": "Wetenschappelijke samenvattingen zijn formeel en objectief."},
    {"type": "waaronwaar", "vraag": "An <b>innovator</b> is a person who introduces new methods, ideas, or products.", "antwoord": True, "uitleg": "Waar. Een innovator brengt vernieuwing."},
    {"type": "invul", "vraag": "Fill in the missing word: <i>Modern smartphones are powered by high-capacity ... batteries.</i>", "antwoord": "rechargeable|lithium", "uitleg": "Rechargeable batteries."},
    {"type": "mc", "vraag": "What is meant by <b>cybersecurity</b>?", "opties": ["The practice of protecting systems, networks, and programs from digital attacks", "Locking the front door of an office building at night", "Wearing safety goggles during physics class", "Cleaning computer keyboards with wet wipes"], "antwoord": 0, "uitleg": "Cybersecurity beschermt netwerken en data tegen digitale aanvallen."}
  ]
}

# EXAMEN 15: H3 Hoofdstuk Eindtoets (Mix & Sınav Simülasyonu) (20 questions)
ex15 = {
  "id": "ex-h3-eng-15",
  "hoofdstuk": 3,
  "hoofdstukTitel": "Hoofdstuk 3 — Science & technology",
  "titel": "Toets 5 — Hoofdstuk 3 Eindtoets (Mix & Examen)",
  "vak": "Engels · HAVO 3 (H3)",
  "icoon": "🏆",
  "duurMin": 30,
  "vragen": [
    {"type": "mc", "vraag": "What is the key difference between <b>invent</b> and <b>discover</b>?", "opties": ["Invent means designing something new; discover means finding something already in existence", "Invent is used only for nature; discover is for computers", "There is no difference in modern dictionaries", "Discover requires a laboratory building"], "antwoord": 0, "uitleg": "Invent = iets nieuws ontwerpen; discover = iets bestaands ontdekken."},
    {"type": "mc", "vraag": "Choose the correct sentence in the <b>Present Perfect</b>:", "opties": ["Scientists have recently discovered a new species of deep-sea bacteria.", "Scientists discovered a new species in 2020 already.", "Scientists has discovered a new species right now.", "Scientists are discover a new species."], "antwoord": 0, "uitleg": "Scientists (meervoud) -> have discovered."},
    {"type": "waaronwaar", "vraag": "A <b>sensor</b> is a mechanical clock that only shows the time in London.", "antwoord": False, "uitleg": "Onwaar. Een sensor meet fysieke signalen zoals warmte en beweging."},
    {"type": "invul", "vraag": "Fill in <i>since</i> or <i>for</i>: <i>Apple has produced the iPad ... more than a decade.</i>", "antwoord": "for", "uitleg": "'For' bij een tijdsduur (more than a decade)."},
    {"type": "mc", "vraag": "Which phrase describes a technological setback or disadvantage?", "opties": ["A major drawback / downside", "A brilliant breakthrough", "A cutting-edge feature", "A user-friendly layout"], "antwoord": 0, "uitleg": "Drawback of downside betekent nadeel."},
    {"type": "waaronwaar", "vraag": "In the sentence <i>'Steve Jobs founded Apple in 1976'</i>, the Past Simple is used because 'in 1976' is a finished past time.", "antwoord": True, "uitleg": "Waar. 'In 1976' is een afgesloten tijdstip."},
    {"type": "invul", "vraag": "Fill in the noun (kunstmatige intelligentie): <i>Autonomous vehicles rely on sophisticated ... algorithms.</i>", "antwoord": "AI|artificial intelligence", "uitleg": "AI / Artificial Intelligence."},
    {"type": "mc", "vraag": "What is the primary function of a <b>prototype</b>?", "opties": ["An early sample or model built to test a concept or process before mass production", "A plastic trophy awarded at gaming conventions", "A customer receipt for buying headphones", "A password used to reset a router"], "antwoord": 0, "uitleg": "Een prototype is een vroeg testmodel."},
    {"type": "mc", "vraag": "Choose the correct verb form: <i>Have you ... (to charge) your mobile phone yet?</i>", "opties": ["charged", "charging", "charge", "did charge"], "antwoord": 0, "uitleg": "Have + you + charged."},
    {"type": "waaronwaar", "vraag": "A <b>rechargeable</b> battery must be replaced with a brand-new one every single evening.", "antwoord": False, "uitleg": "Onwaar. Oplaadbare batterijen kunnen honderden keren herladen worden."},
    {"type": "invul", "vraag": "Fill in the missing word: <i>This device is ... to track your sleep quality.</i>", "antwoord": "designed|engineered", "uitleg": "'Designed to' (ontworpen om)."},
    {"type": "mc", "vraag": "What does <b>virtual reality (VR)</b> simulate?", "opties": ["An artificial 3D sensory environment created by computer software", "An analog telephone call across town", "A traditional printed newspaper layout", "A mechanical wall clock pendulum"], "antwoord": 0, "uitleg": "VR simuleert een 3D virtuele wereld."},
    {"type": "open", "vraag": "Why is high battery capacity considered an essential quality for modern electronic gadgets?", "sleutelwoorden": ["portability/hours/usage/long/without/recharge"], "minTreffers": 1, "modelantwoord": "High battery capacity allows users to use their portable devices all day long without needing frequent recharging.", "uitleg": "Lange accuduur zorgt voor continu gebruik zonder steeds te hoeven opladen."},
    {"type": "mc", "vraag": "Which negative statement in the Present Perfect is grammatically correct?", "opties": ["I haven't tested the new update yet.", "I didn't tested the update yet.", "I not have tested the update.", "I haven't test the update yet."], "antwoord": 0, "uitleg": "Haven't + voltooid deelwoord (tested) + yet."},
    {"type": "waaronwaar", "vraag": "The word <b>gadget</b> refers to small, practical electronic devices like smart bands, earphones, and drones.", "antwoord": True, "uitleg": "Waar. Gadgets zijn handige compacte apparaten."},
    {"type": "invul", "vraag": "Fill in the noun (doorbraak): <i>Solar efficiency reached a historic ... this year.</i>", "antwoord": "breakthrough", "uitleg": "Breakthrough is doorbraak."},
    {"type": "mc", "vraag": "Which phrase concludes a tech review with a final recommendation?", "opties": ["Overall, I would strongly recommend this device for students.", "First, insert the micro USB cable.", "Why is the LED blinking blue?", "This product is made of glass."], "antwoord": 0, "uitleg": "'Overall, I would strongly recommend...' vormt het eindoordeel."},
    {"type": "waaronwaar", "vraag": "The past participle of <i>to see</i> is <i>saw</i>.", "antwoord": False, "uitleg": "Onwaar. See -> saw (past simple) -> seen (past participle)."},
    {"type": "invul", "vraag": "Complete the phrase: <i>This app ... you to control room temperature remotely.</i>", "antwoord": "allows|enables", "uitleg": "Allows / enables (maakt het mogelijk)."},
    {"type": "mc", "vraag": "What does <b>cutting-edge</b> mean in modern technology?", "opties": ["Highly advanced and state-of-the-art", "Extremely old-fashioned and clumsy", "Dangerous and razor-sharp", "Cheap and easily broken"], "antwoord": 0, "uitleg": "Cutting-edge betekent hypermodern en toonaangevend."}
  ]
}

write_examen("examen_11.js", ex11)
write_examen("examen_12.js", ex12)
write_examen("examen_13.js", ex13)
write_examen("examen_14.js", ex14)
write_examen("examen_15.js", ex15)
print("Hoofdstuk 3 exams (11 to 15) generated successfully!")

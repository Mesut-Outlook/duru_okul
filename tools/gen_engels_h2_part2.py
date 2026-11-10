#!/usr/bin/env python3
"""Engels HAVO 3 (Stepping Stones 3) · Hoofdstuk 2 Crime · PART TWO — 3x Grammar (active vs passive) + 3x Woorden.
Schrijft havo3/engels/js/data/examen_59..64.js (ex-h3-eng-59..64). Bron: inbox/2026-2027/engels/engels_h02_crime.ocr.txt
(Part two p.A106-A121, Grammar 6 p.A118-119 / p.A127, Vocabulary p.A124-A125). Zodra Duru een toets gemaakt heeft: id-inhoud niet meer wijzigen."""
import json, os, random, re, subprocess, difflib, glob
from gen_engels_h1_boek import M, W, I, O, plaats, rangschik, langste_aandeel, schrijf, norm

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..', 'havo3', 'engels', 'js', 'data')

# ================= GRAMMAR A — regel + present simple / past simple passive =================
G1 = rangschik(
    [M("When is the passive voice used, according to the grammar box?", "When it is not known or not important who does the action",
       ["When the focus is on the person who is doing the action", "When the sentence is about something in the past", "When the verb is a form of to be"],
       "Passive = focus on the action; used when the doer is unknown or unimportant (Grammar 6, boek p.A119)."),
     M("What do you add when you change an active sentence into the passive?", "A form of to be + the past participle",
       ["A form of to do + the infinitive", "A form of to have + the -ing form", "A form of will + the past participle"],
       "Passive = to be + past participle of the main verb (boek p.A119)."),
     M("Spot the passive: in which sentence does a form of <i>to be</i> + past participle appear?", "The suitcase was found by a guard.",
       ["The guard found the suitcase in the car park.", "The guard is looking for a missing suitcase.", "The guard has found the suitcase already."],
       "was found = was + past participle: passive (boek p.A119)."),
     M("Which sentence is the passive of <i>The judge reads the verdict.</i>?", "The verdict is read by the judge.",
       ["The verdict was read by the judge.", "The verdict is reading by the judge.", "The verdict reads the judge."],
       "Present simple passive: is/are + past participle (boek p.A119)."),
     M("Which sentence is the passive of <i>Someone stole my bike.</i> (past simple)?", "My bike was stolen.",
       ["My bike is stolen.", "My bike was stole.", "My bike has been stolen."],
       "Past simple passive: was/were + past participle (boek p.A119)."),
     M("What becomes the subject when you turn <i>The lawyers questioned the witness</i> into the passive?", "The witness",
       ["The lawyers", "The questioning", "The court"],
       "The object of the active sentence becomes the subject of the passive sentence (boek p.A119)."),
     M("In which sentence is the subject the one who does the action (active)?", "The suspect hid the knife.",
       ["The knife was hidden in the garden.", "The knife is hidden in the garden.", "The knife has been hidden by the suspect."],
       "Here the subject (the suspect) does the action: active voice (boek p.A119)."),
     M("Pick the sentence without a grammar mistake.", "The shops are locked at six o'clock every evening.",
       ["The shops locked at six o'clock every evening.", "The shops are lock at six o'clock every evening.", "The shops be locked at six o'clock every evening."],
       "Plural subject: are + past participle (boek p.A119)."),
     M("Why is the passive used in <i>My wallet was stolen on the bus</i>?", "Because the speaker does not know who took it",
       ["Because the speaker took the wallet himself", "Because the action happens in the present tense", "Because wallets are always the subject here"],
       "Passive voice is used when it is not known who does the action (boek p.A119).")],
    [W("In a passive sentence, the object of the active sentence becomes the subject.", True,
       "Waar. 'The object becomes the subject' (boek p.A119)."),
     W("You make the passive with <i>to have</i> + past participle, e.g. <i>The door has locked</i>.", False,
       "Niet waar. Passive = a form of to be + past participle (boek p.A119)."),
     W("Grammar 6: with the passive the focus is on the action instead of on the doer.", True,
       "Waar. 'The passive voice is used when the focus is on the action' (boek p.A119)."),
     W("In <i>The window is broken (by him)</i>, the part <i>by him</i> must always be there.", False,
       "Niet waar. The doer is put in brackets: you can leave it out (boek p.A119)."),
     W("<i>The cake was eaten</i> is a past simple passive sentence.", True,
       "Waar. was + past participle = past simple passive (boek p.A119).")],
    [I("Complete the passive (present simple): <i>Every night the shop ____ (to lock) by the owner.</i>", "is locked",
       "Singular subject, present simple: is + past participle (boek p.A119)."),
     I("Complete the passive (past simple): <i>The burglar ____ (to arrest) last night.</i>", "was arrested",
       "Last night = past simple: was + arrested (boek p.A119)."),
     I("Active: <i>The guard checks the bags.</i> Passive: <i>The bags ____ by the guard.</i>", "are checked",
       "Plural subject, present simple: are + past participle (boek p.A119)."),
     I("Complete the passive (past simple): <i>Two cars ____ (to steal) in our street last week.</i>", "were stolen",
       "Plural subject, past simple: were + past participle (boek p.A119)."),
     I("Complete the passive (present simple): <i>The Crown Jewels ____ (to keep) in the Tower of London today.</i>", "are kept",
       "Plural subject, present simple: are + kept (boek p.A119).")],
    O("Rewrite in the passive voice: <i>The police found the stolen car.</i>",
      ["was found/been found/is found"], 1,
      "The stolen car was found (by the police).",
      "Past simple passive: object becomes subject + was found (boek p.A119).")
)

# ================= GRAMMAR B — continuous & perfect passives =================
G2 = rangschik(
    [M("Which sentence is the passive of <i>The police are questioning the suspect.</i>?", "The suspect is being questioned by the police.",
       ["The suspect is questioned by the police.", "The suspect has been questioned by the police.", "The suspect is being question by the police."],
       "Present continuous passive: is/are being + past participle (boek p.A119)."),
     M("Which sentence is the passive of <i>The guards were watching the building.</i>?", "The building was being watched by the guards.",
       ["The building was watched by the guards.", "The building were being watched by the guards.", "The building had been watched by the guards."],
       "Past continuous passive: was/were being + past participle (boek p.A119)."),
     M("Which sentence is the passive of <i>The detective has solved the case.</i>?", "The case has been solved by the detective.",
       ["The case was been solved by the detective.", "The case has solved by the detective.", "The case is being solved by the detective."],
       "Present perfect passive: has/have been + past participle (boek p.A119)."),
     M("Which sentence is the passive of <i>The thieves had opened the safe.</i>?", "The safe had been opened by the thieves.",
       ["The safe has been opened by the thieves.", "The safe was being opened by the thieves.", "The safe had opened by the thieves."],
       "Past perfect passive: had been + past participle (boek p.A119)."),
     M("Which tense is the passive sentence <i>The window has been repaired</i>?", "present perfect",
       ["present simple", "past perfect", "past continuous"],
       "has been + past participle = present perfect passive (boek p.A119)."),
     M("Which form completes the sentence? <i>The shop ____ by two men when the alarm went off.</i>", "was being robbed",
       ["has been robbed", "is being robbed", "had robbed"],
       "A moment in the past that was going on: was being + past participle (boek p.A119)."),
     M("Choose the sentence that has the past perfect passive form.", "The money had been hidden under the floor.",
       ["The money was hidden under the floor.", "The money has been hidden under the floor.", "The money is being hidden under the floor."],
       "had been + hidden = past perfect passive (boek p.A119)."),
     M("Which form completes the sentence? <i>Right now a museum ____ by the police, so you cannot go in.</i>", "is being searched",
       ["was searched", "has been searched", "is searched"],
       "Right now = present continuous passive: is being + past participle (boek p.A119)."),
     M("Pick the sentence without a mistake in the verb form.", "The report has been written by an officer.",
       ["The report have been written by an officer.", "The report has be written by an officer.", "The report has been wrote by an officer."],
       "Singular subject: has been + past participle (boek p.A119).")],
    [W("In the present continuous passive you use <i>being</i> after <i>am</i>, <i>is</i> or <i>are</i>.", True,
       "Waar. is/are being + past participle (boek p.A119)."),
     W("The present perfect passive is made with <i>was/were</i> + the past participle.", False,
       "Niet waar. Present perfect passive = has/have been + past participle (boek p.A119)."),
     W("The past perfect passive always contains <i>had been</i>.", True,
       "Waar. had been + past participle (boek p.A119)."),
     W("<i>The suspect is being questioned</i> is a sentence in the present perfect.", False,
       "Niet waar. is being + past participle = present continuous passive (boek p.A119)."),
     W("For a plural subject, <i>has been solved</i> becomes <i>have been solved</i>.", True,
       "Waar. The cases have been solved (boek p.A119).")],
    [I("Complete the passive: <i>Don't enter! The evidence ____ (to examine) at the moment.</i>", "is being examined",
       "At the moment = present continuous passive: is being + past participle (boek p.A119)."),
     I("Complete the passive: <i>By eight o'clock the whole street ____ (to evacuate).</i>", "had been evacuated",
       "By eight o'clock (earlier past moment) = past perfect passive (boek p.A119)."),
     I("Complete the passive: <i>Three cars ____ (to steal) since Monday.</i>", "have been stolen",
       "Since Monday = present perfect passive: have been + stolen (boek p.A119)."),
     I("Complete the passive: <i>The police arrived while the suspect ____ (to interview) by a reporter.</i>", "was being interviewed",
       "'While' + a longer action in the past = past continuous passive (boek p.A119)."),
     I("Active: <i>The lawyers have prepared the defence.</i> Passive: <i>The defence ____ by the lawyers.</i>", "has been prepared",
       "Present perfect passive: has been + past participle (boek p.A119).")],
    O("Rewrite in the passive voice: <i>The police are searching the house.</i>",
      ["is being searched/are being searched"], 1,
      "The house is being searched (by the police).",
      "Present continuous passive: is being + past participle (boek p.A119).")
)

# ================= GRAMMAR C — omzetten, by-agent, gemengd =================
G3 = rangschik(
    [M("Which sentence is the passive of <i>A gang raided the post office.</i>?", "The post office was raided by a gang.",
       ["The post office raided by a gang.", "The post office is raided by a gang.", "A gang was raided by the post office."],
       "Past simple: was + past participle; the object becomes the subject (boek p.A119)."),
     M("Which active sentence matches <i>The letter had been delivered by a neighbour.</i>?", "A neighbour had delivered the letter.",
       ["A neighbour has delivered the letter.", "A neighbour delivered the letter.", "The letter had delivered a neighbour."],
       "had been delivered = past perfect passive, so the active is had delivered (boek p.A119)."),
     M("Why can <i>by someone</i> be left out of <i>My phone has been stolen (by someone)</i>?", "Because the doer is unknown, so it adds nothing",
       ["Because the passive never has a by-part", "Because by can only be used with the past simple", "Because the subject stays the same"],
       "The doer is put in brackets: you may leave it out if it is unknown or unimportant (boek p.A119)."),
     M("One passive sentence contains a mistake. Which one?", "The cars was parked outside by the guards.",
       ["The cars were parked outside by the guards.", "The car was parked outside by a guard.", "The cars are parked outside by the guards."],
       "Plural subject needs were/are: The cars were parked (boek p.A119)."),
     M("Which sentence puts the focus on who does the action?", "The mayor opened the new police station.",
       ["The new police station was opened yesterday.", "The new police station has been opened.", "The new police station is being opened."],
       "Active voice = focus on who is doing the action (boek p.A119)."),
     M("Which form completes the sentence? <i>The thieves ____ before they could escape.</i>", "were caught",
       ["was caught", "have caught", "were catching"],
       "Plural subject, past simple passive: were + past participle (boek p.A119)."),
     M("Turn <i>A detective is following the thieves.</i> into the passive. Which sentence is right?", "The thieves are being followed by a detective.",
       ["The thieves are followed by a detective.", "The thieves were being followed by a detective.", "A detective is being followed by the thieves."],
       "Present continuous passive: are being + past participle (boek p.A119)."),
     M("Which tense is the passive sentence <i>Many crimes are never reported</i>?", "present simple",
       ["present continuous", "past simple", "present perfect"],
       "are + past participle = present simple passive (boek p.A119)."),
     M("In <i>The jewels were guarded by a man called Talbot Edwards</i>, who guarded the jewels?", "Talbot Edwards",
       ["The jewels", "Colonel Blood", "King Charles II"],
       "The by-part names the doer (text on boek p.A106; grammar p.A119).")],
    [W("<i>The passive of 'The guard was checking the bags' is 'The bags were being checked by the guard.'</i>", True,
       "Waar. Past continuous passive: were being + past participle (boek p.A119)."),
     W("When you change an active sentence into the passive, the subject of the active sentence stays the subject.", False,
       "Niet waar. The object becomes the subject (boek p.A119)."),
     W("You can leave out <i>by</i> + the doer when it is unknown or not important.", True,
       "Waar. The doer is put in brackets (by me), (by them) (boek p.A119)."),
     W("<i>The car is stolen last night</i> is a correct passive sentence.", False,
       "Niet waar. Last night = past: The car was stolen last night (boek p.A119)."),
     W("In the active voice the focus is on who is doing the action.", True,
       "Waar. 'The active voice is used when the focus is on who is doing the action' (boek p.A119).")],
    [I("Active: <i>Two guards escorted the prisoner.</i> Passive: <i>The prisoner ____ by two guards.</i>", "was escorted",
       "Past simple passive: was + past participle (boek p.A119)."),
     I("Active: <i>The mayor has signed the new law.</i> Passive: <i>The new law ____ by the mayor.</i>", "has been signed",
       "Present perfect passive: has been + past participle (boek p.A119)."),
     I("Active: <i>A lawyer is defending the suspect.</i> Passive: <i>The suspect ____ by a lawyer.</i>", "is being defended",
       "Present continuous passive: is being + past participle (boek p.A119)."),
     I("Active: <i>The police had interviewed all the neighbours.</i> Passive: <i>All the neighbours ____ by the police.</i>", "had been interviewed",
       "Past perfect passive: had been + past participle (boek p.A119)."),
     I("Active: <i>Burglars rob thousands of homes every year.</i> Passive: <i>Thousands of homes ____ every year.</i>", "are robbed",
       "Present simple passive, plural: are + past participle (boek p.A119).")],
    O("Rewrite in the passive voice and say in one sentence why <i>by someone</i> can be left out: <i>Someone stole my bike last night.</i>",
      ["was stolen", "unknown/not known/not important/don't know/doesn't matter/do not know"], 2,
      "My bike was stolen last night. The doer is unknown, so by someone is not needed.",
      "Past simple passive; the doer is left out when it is unknown or not important (boek p.A119).")
)

# ================= WOORDEN A — Theme words Part two (Caution and warning, boek p.A115 / A125) =================
V1 = rangschik(
    [M("A newsreader says <i>hulpdiensten</i> in Dutch. What is the English term?", "emergency services", ["paramedics", "premises", "witnesses"],
       "Emergency services = hulpdiensten; paramedics = hulpverleners (Theme words, boek p.A125)."),
     M("A person who stands by and watches an incident is a <i>toeschouwer</i>. English?", "onlooker", ["witness", "victim", "suspect"],
       "Onlooker = toeschouwer (boek p.A125)."),
     M("Which English word means <i>gebouw en terrein</i>?", "premises", ["crime scene", "courtroom", "warehouse"],
       "Premises = gebouw en terrein (boek p.A125)."),
     M("Fraudsters try <i>iemand oplichten</i>. Which English verb fits?", "to scam", ["to mug", "to harass", "to secure"],
       "To scam = oplichten; to mug = overvallen (boek p.A125)."),
     M("<i>That email looks authentic, but the source looks <b>fishy</b>.</i> What does <b>fishy</b> mean?", "verdacht, bedenkelijk",
       ["gevaarlijk, giftig", "verboden, strafbaar", "onschuldig, betrouwbaar"],
       "Fishy = verdacht, bedenkelijk (Stone 4, boek p.A114 / p.A125)."),
     M("<i>Visitors may not enter the <b>restricted</b> zones.</i> What does <b>restricted</b> mean?", "verboden",
       ["onveilig", "beschadigd", "verlaten"],
       "Restricted = verboden: 'not to enter the restricted zones' (Stone 4, boek p.A114)."),
     M("Which English verb means <i>alarmeren</i>?", "to alert", ["to disturb", "to secure", "to accuse"],
       "To alert = alarmeren; to disturb = (ver)storen (boek p.A125)."),
     M("<i>Two boys tried to <b>mug</b> an old man outside the bank.</i> What does <b>to mug</b> mean?", "overvallen",
       ["uitlachen", "achtervolgen", "aanspreken"],
       "To mug = overvallen (boek p.A125)."),
     M("<i>The <b>paramedics</b> arrived within five minutes.</i> What are <b>paramedics</b>?", "hulpverleners",
       ["hulpdiensten", "toeschouwers", "bewakers"],
       "Paramedics = hulpverleners; emergency services = hulpdiensten (boek p.A125).")],
    [W("The English verb <i>to disturb</i> means <i>(ver)storen</i> in Dutch.", True,
       "Waar. To disturb = (ver)storen (boek p.A125)."),
     W("Learning corner: <i>to secure</i> = <i>beschuldigen</i>.", False,
       "Niet waar. To secure = veiligstellen; beschuldigen = to accuse (boek p.A125)."),
     W("The English word <i>onlooker</i> means <i>slachtoffer</i> in Dutch.", False,
       "Niet waar. Onlooker = toeschouwer; slachtoffer = victim (boek p.A125)."),
     W("To <i>scam</i> someone means <i>iemand oplichten</i>.", True,
       "Waar. To scam = oplichten (boek p.A125)."),
     W("<i>Emergency services</i> are called <i>hulpdiensten</i> in Dutch.", True,
       "Waar. Emergency services = hulpdiensten (boek p.A125).")],
    [I("Fill in the English noun for <i>dreiging</i>: <i>The anonymous letter was seen as a serious ____ to the school.</i>", "threat",
       "Threat = dreiging (boek p.A125)."),
     I("Fill in the English verb for <i>evacueren</i>: <i>Because of the fire, the staff had to ____ the premises without delay.</i>", "evacuate",
       "To evacuate = evacueren (Stone 4, boek p.A114)."),
     I("Fill in the English verb for <i>spijt hebben</i>: <i>I ____ telling him my secret. I wish I had kept quiet.</i>", "regret",
       "To regret = spijt hebben (boek p.A125)."),
     I("Fill in the English verb for <i>laten weten</i>: <i>You must ____ the school if your child is ill.</i>", "notify|inform",
       "To notify = laten weten (boek p.A125)."),
     I("Fill in the English noun for <i>onruststoker</i>: <i>He is a real ____: he starts a fight at every match.</i>", "troublemaker",
       "Troublemaker = onruststoker (boek p.A125).")],
    O("Translate into English: <i>De hulpdiensten moeten de toeschouwers waarschuwen.</i>",
      ["emergency services", "onlookers/onlooker/bystanders/spectators", "warn/alert"], 2,
      "The emergency services must warn the onlookers.",
      "Emergency services = hulpdiensten; onlooker = toeschouwer; to warn/alert = waarschuwen/alarmeren (boek p.A125).")
)

# ================= WOORDEN B — F Listening + Theme words =================
V2 = rangschik(
    [M("Children under ten must be supervised by a <i>volwassene</i>. English word?", "adult", ["teenager", "pupil", "student"],
       "Adult = volwassene (Vocabulary F Listening, boek p.A125)."),
     M("<i>The judge asked him to state his <b>case</b>.</i> What does <b>case</b> mean here?", "zaak",
       ["koffer", "bewijs", "straf"],
       "Case = zaak (Vocabulary F Listening, boek p.A125)."),
     M("Which English verb means <i>betrekken</i> (bij iets)?", "to involve", ["to prevent", "to escape", "to accuse"],
       "To involve = betrekken: 'A teacher tries to involve all children in class' (boek p.A125)."),
     M("<i>She works at the police station as a <b>PC</b>.</i> What is a <b>PC</b>?", "politieagent",
       ["rechercheur", "bewaker", "rechter"],
       "PC = police constable = politieagent (boek p.A125; listening to the youth police p.A108)."),
     M("<i>The bars on the windows <b>prevent</b> inmates from escaping.</i> What does <b>to prevent</b> mean?", "voorkomen",
       ["toelaten", "veroorzaken", "aanmoedigen"],
       "To prevent = voorkomen (boek p.A125; Vocabulary p.A109)."),
     M("The film showed too much <i>geweld</i>. Which English noun is that?", "violence", ["riot", "assault", "burglary"],
       "Violence = geweld: 'Where does his anger and violence come from?' (boek p.A125)."),
     M("The police arrested the <i>onruststoker</i> at the match. English word?", "troublemaker", ["onlooker", "perpetrator", "intruder"],
       "Troublemaker = onruststoker (Theme words, boek p.A125)."),
     M("<i>The police had to <b>evacuate</b> the whole building.</i> What does <b>to evacuate</b> mean?", "evacueren",
       ["doorzoeken", "afsluiten", "beschadigen"],
       "To evacuate = evacueren (Stone 4, boek p.A114 / p.A125)."),
     M("The sirens must <i>alarmeren</i> the villagers. Which English verb fits?", "to alert", ["to scam", "to mug", "to regret"],
       "To alert = alarmeren (Theme words, boek p.A125).")],
    [W("The English word <i>drugs</i> can be translated as <i>verdovende middelen</i>.", True,
       "Waar. Drugs = verdovende middelen (boek p.A125)."),
     W("Learning corner: <i>to involve</i> is translated as <i>voorkomen</i>.", False,
       "Niet waar. To involve = betrekken; voorkomen = to prevent (boek p.A125)."),
     W("A <i>social worker</i> is called a <i>maatschappelijk werker</i> in Dutch.", True,
       "Waar. Social worker = maatschappelijk werker (boek p.A125)."),
     W("Learning corner: <i>case</i> is translated as <i>bezit</i>.", False,
       "Niet waar. Case = zaak; bezit = possession (boek p.A125)."),
     W("<i>To mess around</i> means <i>rotzooien</i>, as in <i>My brothers mess around a lot</i>.", True,
       "Waar. To mess around = er een zooitje van maken, rotzooien (boek p.A125).")],
    [I("Fill in the English verb for <i>vernietigen</i>: <i>Be careful, the fire could ____ the whole archive.</i>", "destroy",
       "To destroy = vernietigen (boek p.A125)."),
     I("Fill in the English verb for <i>reageren</i>: <i>How did the suspect ____ when he heard the news?</i>", "react",
       "To react = reageren (boek p.A125)."),
     I("Fill in the English noun for <i>bezit</i>: <i>He was fined for the ____ of a stolen phone.</i>", "possession",
       "Possession = bezit (boek p.A125; Vocabulary p.A109)."),
     I("Fill in the English noun for <i>onderwijs</i>: <i>My mum works in ____ as a biology teacher.</i>", "education",
       "Education = onderwijs (boek p.A125)."),
     I("Fill in the English noun for <i>oordeel</i>: <i>You shouldn't pass ____ before you have heard both sides.</i>", "judgment|judgement",
       "Judgment = oordeel: 'You shouldn't pass judgment too quickly' (boek p.A109 / p.A125).")],
    O("Translate into English: <i>De politieagent kon het geweld voorkomen.</i>",
      ["police constable/PC/police officer/policeman", "violence", "prevent"], 2,
      "The police constable could prevent the violence.",
      "Politieagent = PC / police officer; geweld = violence; voorkomen = to prevent (boek p.A125).")
)

# ================= WOORDEN C — G Reading + Theme words =================
V3 = rangschik(
    [M("<i>Tara was unable to <b>conceal</b> her sadness.</i> What does <b>to conceal</b> mean?", "verbergen",
       ["uitleggen", "opmerken", "beschrijven"],
       "To conceal = verbergen (Vocabulary G Reading, boek p.A125)."),
     M("<i>Someone ate my chocolate. Do you know who the <b>culprit</b> is?</i> What does <b>culprit</b> mean?", "dader",
       ["getuige", "slachtoffer", "rechter"],
       "Culprit = dader (boek p.A125)."),
     M("An <i>uitgebreid</i> explanation is a long and detailed one. English adjective?", "elaborate", ["specific", "simultaneous", "wealthy"],
       "Elaborate = uitgebreid: 'an elaborate explanation' (boek p.A125)."),
     M("<i>The <b>maid</b> was accused of stealing money.</i> What is a <b>maid</b>?", "dienstmeisje",
       ["verpleegster", "kokkin", "serveerster"],
       "Maid = dienstmeisje (boek p.A125; text Shanghai 1943 p.A111)."),
     M("<i>Our class held a <b>mock</b> court case about the stolen painting.</i> What does <b>mock</b> mean?", "nep-, namaak-",
       ["officieel, echt", "geheim, privé", "lang, uitgebreid"],
       "Mock = nep-, namaak-: a mock trial (boek p.A125)."),
     M("The game has many <i>nieuwigheden</i>. Which English noun belongs here?", "novelty", ["prop", "plot", "remark"],
       "Novelty = nieuwigheid (boek p.A125; text p.A111: 'all these novelties of the game')."),
     M("<i>The <b>plot</b> of the film was so exciting!</i> What does <b>plot</b> mean?", "verhaallijn",
       ["rekwisiet", "personage", "plaats van handeling"],
       "Plot = verhaallijn (boek p.A125)."),
     M("Which English word means <i>rekwisiet</i> (theatervoorwerp)?", "prop", ["plot", "mock", "maid"],
       "Prop = rekwisiet: 'Props ... can really help bring the experience alive' (boek p.A111 / p.A125)."),
     M("<i>Don't miss <b>rehearsal</b> too often because the play opens soon.</i> What is a <b>rehearsal</b>?", "repetitie",
       ["voorstelling", "toneelstuk", "kostuum"],
       "Rehearsal = repetitie (boek p.A125).")],
    [W("The book list gives <i>rijk</i> as the Dutch word for <i>wealthy</i>.", True,
       "Waar. Wealthy = rijk (boek p.A125)."),
     W("The book list gives <i>verbergen</i> as the Dutch word for <i>to remark</i>.", False,
       "Niet waar. To remark = opmerken; verbergen = to conceal (boek p.A125)."),
     W("Learning corner: <i>murder</i> is translated as <i>moord</i>.", True,
       "Waar. Murder = moord (boek p.A125)."),
     W("Learning corner: <i>prop</i> is translated as <i>verhaallijn</i>.", False,
       "Niet waar. Prop = rekwisiet; verhaallijn = plot (boek p.A125)."),
     W("Learning corner: <i>novelty</i> is translated as <i>nieuwigheid</i>.", True,
       "Waar. Novelty = nieuwigheid (boek p.A125).")],
    [I("Fill in the English adverb for <i>tegelijkertijd</i>: <i>I asked the question, but Joanne and Christy answered ____.</i>", "simultaneously",
       "Simultaneously = tegelijkertijd (boek p.A125)."),
     I("Fill in the English word for <i>bedoeld zijn</i>: <i>Sports are ____ for pleasure but also to keep you healthy.</i>", "intended",
       "To be intended (for) = bedoeld zijn (boek p.A125)."),
     I("Fill in the English adverb for <i>specifiek</i>: <i>This book was ____ written for older children.</i>", "specifically",
       "Specifically = specifiek, in het bijzonder (boek p.A125)."),
     I("Fill in the English verb for <i>oplichten</i>: <i>Be careful: criminals try to ____ elderly people by phone.</i>", "scam",
       "To scam = oplichten (Theme words, boek p.A125)."),
     I("Fill in the English plural noun for <i>gebouw en terrein</i>: <i>All visitors must leave the ____ before six o'clock.</i>", "premises",
       "Premises = gebouw en terrein (Theme words, boek p.A125).")],
    O("Translate into English: <i>De dader verborg het rekwisiet.</i>",
      ["culprit/perpetrator", "concealed/hid/hidden", "prop"], 2,
      "The culprit concealed the prop.",
      "Dader = culprit; verbergen = to conceal; rekwisiet = prop (boek p.A125).")
)

EXAMENS = {
    59: ("Part two · Grammar A — active vs passive: regel, present & past simple (boek)", "✏️", G1),
    60: ("Part two · Grammar B — passive: continuous & perfect tenses (boek)", "✏️", G2),
    61: ("Part two · Grammar C — active ⇄ passive omzetten & gemengd (boek)", "✏️", G3),
    62: ("Part two · Woorden A — Theme words: caution & warning (boek)", "📖", V1),
    63: ("Part two · Woorden B — Listening-woorden + Theme words (boek)", "🔤", V2),
    64: ("Part two · Woorden C — Reading-woorden + Theme words (boek)", "🔎", V3),
}


def bestaande():
    js = ("global.DURU={register:o=>(o.vragen||[]).forEach(v=>out.push(v.vraag)),registerExamen:o=>o.vragen.forEach(v=>out.push(v.vraag))};"
          "const out=[];const d=process.argv[1];const eigen=new Set(process.argv.slice(2));"
          "for(const f of require('fs').readdirSync(d))if(/^(examen_|h\\d)/.test(f)&&!eigen.has(f)){try{require(d+'/'+f)}catch(e){}}"
          "console.log(JSON.stringify(out))")
    eigen = [f'examen_{n}.js' for n in EXAMENS]
    return [norm(x) for x in json.loads(subprocess.check_output(['node', '-e', js, os.path.abspath(ROOT)] + eigen))]


FOUT = []


def controleer(vr, oud, nr):
    for v in vr:
        q = norm(v["vraag"])
        r = max((difflib.SequenceMatcher(None, q, o).ratio() for o in oud), default=0)
        if r >= 0.8:
            print(f"examen_{nr}: lijkt op bestaande vraag ({r:.2f}): {v['vraag']}"); FOUT.append(1)
        if v["type"] == "invul":
            for a in v["antwoord"].split('|'):
                if norm(a) in q:
                    print(f"examen_{nr}: antwoord in vraag: {v['vraag']}"); FOUT.append(1)


def main():
    global FOUT
    rng = random.Random(os.path.basename(__file__))
    oud = bestaande()
    eigen = []
    for nr, (titel, icoon, vr) in EXAMENS.items():
        assert len(vr) == 20, (nr, len(vr))
        vr = plaats([dict(v) for v in vr], rng)
        n, tot = langste_aandeel(vr)
        assert n / tot <= 0.4, f"examen_{nr}: juiste optie {n}/{tot} keer langste"
        controleer(vr, oud, nr)
        controleer(vr, eigen, nr)  # geen kopie tussen mijn eigen toetsen
        if FOUT: continue
        if FOUT: continue
        eigen += [norm(v["vraag"]) for v in vr]
        ex = {"id": f"ex-h3-eng-{nr}", "hoofdstuk": 2, "hoofdstukTitel": "Hoofdstuk 2 — Crime",
              "titel": titel, "vak": "Engels · HAVO 3 (H2)", "icoon": icoon, "duurMin": 25, "vragen": vr}
        schrijf(os.path.join(ROOT, f'examen_{nr}.js'),
                f"/* {titel}\n   Stepping Stones 3 HAVO Hoofdstuk 2 — gegenereerd door tools/gen_engels_h2_part2.py, uit het boek */\n",
                "DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")
        print(f"examen_{nr}: 20 vragen, juiste optie langste {n}/{tot}")


if __name__ == '__main__':
    main()

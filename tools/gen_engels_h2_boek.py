#!/usr/bin/env python3
"""Engels HAVO 3 · Stepping Stones 3 HAVO · Hoofdstuk 2 Crime — 5 extra proeftoetsen STRIKT uit het boek.
Schrijft havo3/engels/js/data/examen_36..40.js (ex-h3-eng-36..40; titels "Toets 6..10 — ... (boek)").
Bron: inbox/2026-2027/engels/engels_h02_crime.{pdf,ocr.txt}; paginanummers = OCR-markers (boek p.A<n>).
mc-volgorde willekeurig (geseed), opnieuw geschud tot gate-regels 3/16/17 kloppen.
Zodra Duru een toets gemaakt heeft: id-inhoud niet meer wijzigen (nieuwe toets = nieuwe id)."""
import json, os, random, re, glob, difflib

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'havo3', 'engels', 'js', 'data')


def M(vraag, goed, fout, uitleg, niveau=None):
    d = {"type": "mc", "vraag": vraag, "_goed": goed, "_fout": fout, "uitleg": uitleg}
    if niveau:
        d["niveau"] = niveau
    return d


def W(vraag, antwoord, uitleg, niveau=None):
    d = {"type": "waaronwaar", "vraag": vraag, "antwoord": antwoord, "uitleg": uitleg}
    if niveau:
        d["niveau"] = niveau
    return d


def I(vraag, antwoord, uitleg):
    return {"type": "invul", "vraag": vraag, "antwoord": antwoord, "uitleg": uitleg}


def Iv(vraag, antwoord, uitleg, niveau=2):
    return {"type": "invoer", "niveau": niveau, "vraag": vraag, "antwoord": antwoord, "uitleg": uitleg}


def O(vraag, sleutels, min_, model, uitleg):
    return {"type": "open", "vraag": vraag, "sleutelwoorden": sleutels, "minTreffers": min_,
            "modelantwoord": model, "uitleg": uitleg}


def plaats(vragen, rng):
    """Schud mc-opties tot: <=40% op een index, geen periode 2-4, <60% '+1'-stappen."""
    mcs = [v for v in vragen if v["type"] == "mc"]
    for _ in range(5000):
        pos = [rng.randrange(len(v["_fout"]) + 1) for v in mcs]
        if max(pos.count(i) for i in set(pos)) / len(pos) > 0.4:
            continue
        if len(pos) < 6:
            break
        if any(all(a == pos[i - p] for i, a in enumerate(pos) if i >= p) for p in (2, 3, 4)):
            continue
        n = max(len(v["_fout"]) + 1 for v in mcs)
        if sum(pos[i + 1] == (pos[i] + 1) % n for i in range(len(pos) - 1)) / (len(pos) - 1) >= 0.6:
            continue
        break
    else:
        raise SystemExit("geen geldige volgorde gevonden")
    for v, p in zip(mcs, pos):
        opties = list(v.pop("_fout"))
        rng.shuffle(opties)
        opties.insert(p, v.pop("_goed"))
        v["opties"], v["antwoord"] = opties, p
    return vragen


def langste_aandeel(vragen):
    mcs = [v for v in vragen if v["type"] == "mc"]
    n = sum(all(len(o) < len(v["opties"][v["antwoord"]]) for i, o in enumerate(v["opties"]) if i != v["antwoord"]) for v in mcs)
    return n, len(mcs)




def schrijf(pad, kop, obj):
    with open(pad, 'w', encoding='utf-8') as f:
        f.write(kop)
        f.write(obj)


PATROON = "MWMIMWMIMWMIMWIMWIOM"  # 9 mc, 5 waaronwaar, 5 invul, 1 open — gemengd


def rangschik(ms, ws, ins, o):
    assert (len(ms), len(ws), len(ins)) == (9, 5, 5), (len(ms), len(ws), len(ins))
    it = {"M": iter(ms), "W": iter(ws), "I": iter(ins), "O": iter([o])}
    return [next(it[c]) for c in PATROON]


TOETSEN = {}

# ---------------------------------------------------------------- Toets 6: woordentoets NL -> EN
T6M = [
    M("Which English word means <b>beroving</b> (Dutch)?", "robbery", ["burglary", "assault", "riot"],
      "Robbery = beroving; burglary = inbraak, assault = aanval, riot = rel (boek p. A124)."),
    M("Which English word means <b>dader</b> (Dutch)?", "perpetrator", ["offence", "intruder", "victim"],
      "Perpetrator = dader; offence = overtreding, intruder = indringer, victim = slachtoffer (boek p. A124)."),
    M("Which English verb means <b>zakkenrollen</b> (Dutch)?", "to pickpocket", ["to shoplift", "to trespass", "to mug"],
      "To pickpocket = zakkenrollen; to shoplift = winkeldiefstal plegen, to mug = overvallen (boek p. A124)."),
    M("Which English word means <b>vonnis</b> (Dutch)?", "sentence", ["verdict", "conviction", "trial"],
      "Sentence = vonnis; verdict = uitspraak, conviction = veroordeling, trial = rechtszaak (boek p. A124)."),
    M("Which English word means <b>plaats delict</b> (Dutch)?", "crime scene", ["courtroom", "premises", "emergency services"],
      "Crime scene = plaats delict; courtroom = rechtszaal, premises = gebouw en terrein (boek p. A124)."),
    M("Which English verb means <b>ontsnappen</b> (Dutch)?", "to escape", ["to evacuate", "to escalate", "to alert"],
      "To escape = ontsnappen; to evacuate = evacueren, to escalate = uit de hand lopen, to alert = alarmeren (boek p. A124)."),
    M("Which English verb means <b>beschuldigen</b> (Dutch)?", "to accuse", ["to harass", "to threaten", "to notify"],
      "To accuse = beschuldigen; to harass = lastigvallen, to threaten = bedreigen, to notify = laten weten (boek p. A124)."),
    M("Which English adjective means <b>roekeloos</b> (Dutch)?", "reckless", ["aggressive", "armed", "vulnerable"],
      "Reckless = roekeloos; aggressive = agressief, armed = bewapend, vulnerable = kwetsbaar (boek p. A124)."),
    M("Which English words mean <b>hulpdiensten</b> (Dutch)?", "emergency services", ["paramedics", "onlooker", "troublemaker"],
      "Emergency services = hulpdiensten; paramedics = hulpverleners, onlooker = toeschouwer, troublemaker = onruststoker (boek p. A124)."),
]
T6W = [
    W("<b>Verdict</b> means 'uitspraak' (of a court) in Dutch.", True,
      "Waar. Verdict = uitspraak; sentence = vonnis (boek p. A124)."),
    W("<b>Intruder</b> is the English word for 'toeschouwer'.", False,
      "Niet waar. Intruder = indringer; toeschouwer = onlooker (boek p. A124)."),
    W("<b>To testify</b> means 'getuigen' in Dutch.", True,
      "Waar. To testify = getuigen; witness = getuige (boek p. A124)."),
    W("<b>To regret</b> means 'beschuldigen' in Dutch.", False,
      "Niet waar. To regret = spijt hebben (van); beschuldigen = to accuse (boek p. A124)."),
    W("<b>Premises</b> means 'gebouw en terrein' in Dutch.", True,
      "Waar. Premises = gebouw en terrein (boek p. A124)."),
]
T6I = [
    I("Fill in the English verb for <i>lastigvallen</i>: <i>Some boys began to ____ the girl on her way home.</i>", "harass",
      "To harass = lastigvallen (boek p. A124)."),
    I("Fill in the English adjective for <i>dronken</i>: <i>The driver was ____ and could not walk in a straight line.</i>", "intoxicated",
      "Intoxicated = dronken (boek p. A124)."),
    I("Fill in the English noun for <i>hulpverleners</i>: <i>The ____ gave first aid to the injured man.</i>", "paramedics|paramedic",
      "Paramedics = hulpverleners (boek p. A124)."),
    I("Fill in the English verb for <i>veiligstellen</i>: <i>The police had to ____ the area before the crowd arrived.</i>", "secure",
      "To secure = veiligstellen (boek p. A124)."),
    I("Fill in the English verb for <i>zich op verboden terrein begeven</i>: <i>The sign says: do not ____ on this land.</i>", "trespass",
      "To trespass = (zich) op verboden terrein begeven (boek p. A124)."),
]
T6O = O("Name these three courtroom roles in English: (1) the person who leads the court case and gives the verdict, (2) the person who speaks for someone in court (Dutch: advocaat), (3) the person who tells the court what he or she saw (Dutch: getuige).",
        ["judge", "lawyer", "witness"], 3,
        "(1) the judge, (2) the lawyer, (3) the witness.",
        "Theme words 'In the courtroom': judge = rechter, lawyer = advocaat, witness = getuige (boek p. A124).")
TOETSEN[36] = ("Toets 6 — Woordentoets NL → EN: Crime & Courtroom (boek)", "🧠", T6M, T6W, T6I, T6O)

# ---------------------------------------------------------------- Toets 7: woorden EN -> NL en in context
T7M = [
    M("What does <b>to hijack</b> mean in Dutch?", "kapen", ["aankunnen", "verbeteren", "aansturen"],
      "'The terrorists were able to hijack the airplane' — to hijack = kapen (boek p. A125)."),
    M("What does <b>hectic</b> mean in Dutch? <i>Work has been so hectic lately that I've had to work overtime.</i>", "gejaagd, hectisch", ["gewelddadig", "buitenwijk", "kwetsbaar"],
      "Hectic = gejaagd, hectisch (boek p. A125)."),
    M("<i>Sarah lives in a <b>suburb</b> of London as housing is extremely expensive in the city.</i> What does suburb mean?", "buitenwijk", ["busje", "voertuig", "cursus"],
      "Suburb = buitenwijk (boek p. A125)."),
    M("<i>The witnesses saw who fired the gunshots, but they were too afraid to <b>report</b> it.</i> Which Dutch word fits report here?", "aangeven", ["volgen", "kapen", "terugkrijgen"],
      "In this sentence, to report = aangeven (boek p. A125)."),
    M("What does <b>possession</b> mean in Dutch? <i>He was arrested for possession of illegal substances.</i>", "bezit", ["geweld", "oordeel", "zaak"],
      "Possession = bezit; violence = geweld, judgment = oordeel, case = zaak (boek p. A125)."),
    M("Choose the English word that completes the sentence: <i>The bars on the windows of the prison are to ____ inmates from escaping.</i>", "prevent", ["react", "involve", "destroy"],
      "To prevent = voorkomen (boek p. A125)."),
    M("<i>The <b>plot</b> of the film was so exciting! I couldn't wait for the next twist!</i> What does plot mean?", "verhaallijn", ["moord", "repetitie", "rekwisiet, theatervoorwerp"],
      "Plot = verhaallijn; murder = moord, rehearsal = repetitie, prop = rekwisiet (boek p. A126)."),
    M("<i>We're having a <b>mock</b> trial in law class tomorrow.</i> What does mock mean here?", "nep-, namaak-", ["uitgebreid", "rijk", "specifiek, in het bijzonder"],
      "Mock = nep-, namaak- (a mock trial is not a real trial) (boek p. A126)."),
    M("What does <b>to conceal</b> mean in Dutch? <i>Tara was unable to conceal the sadness about her grandma passing away.</i>", "verbergen", ["opmerken", "betrekken", "vernietigen"],
      "To conceal = verbergen; to remark = opmerken, to involve = betrekken, to destroy = vernietigen (boek p. A126)."),
]
T7W = [
    W("<b>Wealthy</b> means 'rijk' in Dutch.", True, "Waar. Wealthy = rijk; wealth = rijkdom (boek p. A125-A126)."),
    W("<b>To destroy</b> means 'verbeteren' in Dutch.", False, "Niet waar. To destroy = vernietigen; verbeteren = to improve (boek p. A125)."),
    W("<b>Novelty</b> means 'nieuwigheid' in Dutch.", True, "Waar. Novelty = nieuwigheid (boek p. A126)."),
    W("<b>To remark</b> means 'terugkrijgen' in Dutch.", False, "Niet waar. To remark = opmerken; terugkrijgen = to recover (boek p. A125-A126)."),
    W("<b>Simultaneously</b> means 'tegelijkertijd' in Dutch.", True, "Waar. Simultaneously = tegelijkertijd (boek p. A126)."),
]
T7I = [
    I("Fill in the English verb for <i>terugkrijgen</i>: <i>Mum searched the whole house to ____ her missing keys.</i>", "recover",
      "To recover = terugkrijgen (boek p. A125)."),
    I("Fill in the English noun for <i>repetitie</i>: <i>Don't miss ____ too often because the opening of the play is soon!</i>", "rehearsal",
      "Rehearsal = repetitie (boek p. A126)."),
    I("Fill in the English noun for <i>volwassene</i>: <i>Children under the age of 10 must be supervised by an ____.</i>", "adult",
      "Adult = volwassene (boek p. A125)."),
    I("Fill in the English noun for <i>krantenkop</i>: <i>The newspaper ____ on 21 July 1969 read: Man walks on the moon.</i>", "headline",
      "Headline = krantenkop (boek p. A124)."),
    I("Fill in the English noun for <i>rechtszaak</i>: <i>They filed a ____ against him and he is being sued for stealing jewellery.</i>", "lawsuit",
      "Lawsuit = rechtszaak (boek p. A124)."),
]
T7O = O("Translate into English: <i>De dader probeerde zijn geheim te verbergen.</i>",
        ["culprit/perpetrator/offender", "conceal/hide", "secret"], 2,
        "The culprit tried to conceal his secret.",
        "Dader = culprit (of perpetrator); verbergen = to conceal (boek p. A124-A126).")
TOETSEN[37] = ("Toets 7 — Woorden EN → NL en in context (boek)", "📖", T7M, T7W, T7I, T7O)

# ---------------------------------------------------------------- Toets 8: grammatica
T8M = [
    M("Which sentence is in the <b>past perfect</b>?", "The burglar had left before the police arrived.",
      ["The burglar left before the police arrived.", "The burglar was leaving before the police arrived.", "The burglar has left before the police arrived."],
      "Past perfect = had + voltooid deelwoord: 'had left' (boek p. A102)."),
    M("How do you form the <b>past perfect</b>?", "had + past participle",
      ["have/has + past participle", "was/were + past participle", "had + infinitive"],
      "Past perfect = had + past participle, regular and irregular verbs (boek p. A102, grammar 4 p. A127)."),
    M("Choose the correct form: <i>When the police arrived, the thieves ____ (to disappear) already.</i>", "had disappeared",
      ["disappeared", "have disappeared", "were disappearing"],
      "An action that was finished before another action in the past: had + past participle (boek p. A102)."),
    M("Which of these is a <b>signal word</b> of the past perfect, according to the book?", "as soon as",
      ["ago", "tomorrow", "every day"],
      "Signal words: when, before, as soon as, after (boek p. A102)."),
    M("Which sentence uses the prepositions of time and place correctly?", "The robbery took place in March at the bank.",
      ["The robbery took place on March at the bank.", "The robbery took place at March at the bank.", "The robbery took place in March on the bank."],
      "In + months; at + a specific location such as the bank (boek p. A104 / grammar 5 p. A127)."),
    M("According to the book, which preposition do you use with <b>months, years, seasons and parts of the day</b>?", "in",
      ["on", "at", "during"],
      "In: in February, in spring, in 2019, in the morning (boek p. A104)."),
    M("Which of these sentences is passive, not active?", "The statue was damaged by vandals.",
      ["Vandals damaged the statue.", "Vandals were damaging the statue.", "Vandals have damaged the statue."],
      "Passive = a form of to be + past participle: 'was damaged' (boek p. A118-A119)."),
    M("Change the sentence into the passive voice: <i>The police have arrested the suspect.</i>", "The suspect has been arrested by the police.",
      ["The suspect was arrested by the police.", "The suspect had been arrested by the police.", "The suspect has arrested by the police."],
      "Present perfect passive: have/has been + past participle ('has been arrested') (boek p. A119)."),
    M("Change the sentence into the passive voice: <i>The detective is questioning the witness.</i>", "The witness is being questioned by the detective.",
      ["The witness is questioned by the detective.", "The witness was being questioned by the detective.", "The witness has been questioned by the detective."],
      "Present continuous passive: is/are being + past participle (boek p. A119)."),
]
T8W = [
    W("You use the past perfect for an action that was finished <i>before</i> another action in the past.", True,
      "Waar. 'The thief had escaped before they entered the house.' (boek p. A102)."),
    W("In <i>After he had burnt the evidence, he threw the ashes into the bin</i>, the action 'threw' happened first.", False,
      "Niet waar. 'Had burnt' (past perfect) happened first; 'threw' (past simple) came after (boek p. A102)."),
    W("You use <b>at</b> with days and dates (for example: at Saturday, at 1 January).", False,
      "Niet waar. With days and dates you use 'on': on Saturday, on 1 January (boek p. A104)."),
    W("In the passive voice the focus is on the action, not on who does it.", True,
      "Waar. Active = focus on the subject; passive = focus on the action (boek p. A118-A119)."),
    W("The passive of <i>The police had found the weapon</i> is <i>The weapon had been found by the police</i>.", True,
      "Waar. Past perfect passive: had been + past participle (boek p. A119)."),
]
T8I = [
    I("Fill in the past perfect of (to finish): <i>My sister ____ her homework before dinner started.</i>", "had finished",
      "Past perfect: had + past participle (boek p. A102)."),
    I("Fill in the missing words (preposition + noun): <i>I left my notes ____ (thuis).</i>", "at home",
      "At is used for specific locations: at home (boek p. A104)."),
    I("Fill in the missing words (preposition + day): <i>We have a game ____ (zaterdag).</i>", "on saturday",
      "On is used for days and dates: on Saturday (boek p. A104)."),
    I("Fill in the passive (past simple) of (to steal): <i>The painting ____ last night.</i>", "was stolen",
      "Past simple passive: was/were + past participle (boek p. A119)."),
    I("Fill in the passive (present perfect) of (to arrest): <i>The suspect ____ by the police.</i>", "has been arrested",
      "Present perfect passive: has/have been + past participle (boek p. A119)."),
]
T8O = O("Explain in your own words when you use the passive voice instead of the active voice.",
        ["action", "not known/unknown/not important/don't know/doesn't matter", "focus"], 2,
        "You use the passive voice when the focus is on the action and it is not known or not important who does it.",
        "Passive: focus on the action; used when it is not known or not important who or what does the action (boek p. A119).")
TOETSEN[38] = ("Toets 8 — Grammatica: Past perfect, prepositions & passive (boek)", "✍️", T8M, T8W, T8I, T8O)

# ---------------------------------------------------------------- Toets 9: Stones + teksten
T9M = [
    M("You are at the police station. Which sentence from <b>Stone 3</b> starts your report?", "I'd like to report a crime.",
      ["I'd like to warn you about a crime.", "You should dial 112 immediately.", "Could you describe in detail what happened?"],
      "Stone 3 Reporting a crime: 'I'd like to report a crime.' The question 'Could you describe...' is what the police asks (boek p. A98)."),
    M("Which sentence from Stone 3 means <i>Ik zag dat hij het gebouw binnenging nadat hij het slot had beschadigd</i>?", "I saw that he entered the gym after he had damaged the lock.",
      ["I saw that he had entered the gym after he damaged the lock.", "I saw that he entered the gym before he had damaged the lock.", "I saw that he entered the gym after he damaged the lock."],
      "Stone 3: past simple for the later action ('entered'), past perfect for the earlier one ('had damaged') (boek p. A98)."),
    M("Which sentence from Stone 4 means <i>Je kunt beter de weg vrijmaken voor de hulpverleners</i>?", "You'd better clear the way for the paramedics.",
      ["You'd better keep your distance from the paramedics.", "You'd better follow the instructions of the paramedics.", "You'd better warn the paramedics about pickpockets."],
      "Stone 4: 'You'd better clear the way for the paramedics on duty.' (boek p. A114)."),
    M("Your friend gets a strange message. Which sentence from <b>Stone 4</b> is the best warning?", "Don't respond to that message, because the source looks fishy.",
      ["I think this text message is legit, so click on the unfamiliar link.", "The park is perfect for relaxing, but beware of phishing.", "People were ordered to evacuate the premises."],
      "Stone 4: 'Don't respond to that message, because the source looks fishy.' (fishy = verdacht) (boek p. A114)."),
    M("In the text <i>Helicopter force fights South Africa's carjacking epidemic</i>: how soon are pilots expected to take off after a car is reported stolen?", "within ten minutes",
      ["within an hour", "within thirty seconds", "within two hours"],
      "'Pilots are expected to take off within ten minutes.' (boek p. A94)."),
    M("According to the carjacking text, why did robbers switch to hijacking?", "Better car security made stealing a parked car take longer",
      ["Hijacking is cheaper and easier than buying a new car in town", "Parked cars are always guarded by private guards", "The police no longer chase hijackers there"],
      "'Hijacking is in part a reaction to improved car security... it takes much longer to steal a parked vehicle.' (boek p. A95)."),
    M("In the text about Colonel Blood: how did Blood and his 'wife' get into Talbot Edwards' apartment?", "She pretended to fall ill, so Talbot let them rest there",
      ["They said they were guards sent by the king himself", "They bought the keys to the apartment from Talbot's family", "Talbot invited them to stay for dinner and a game"],
      "'Blood's wife pretended to fall ill. Feeling sorry for them, Talbot let them rest in his apartment.' (boek p. A106)."),
    M("What happened to Colonel Blood after the attack?", "King Charles II made him a spy and he was never punished",
      ["He was sentenced to life in prison for attacking Talbot", "He was executed in public at the Tower of London for the attack", "He escaped to Ireland and was never found by the king"],
      "'King Charles II... made him a spy. Amazingly, Blood was never punished for his crime.' (boek p. A106)."),
    M("In the excerpt from <i>Who Could That Be at This Hour?</i>: what has been stolen from Mrs Murphy Sallis' home?", "A small shiny black wooden statue of the Bombinating Beast",
      ["A priceless painting of the lighthouse near her house", "A large silver tray with the cookies from the plate", "A heavy golden clock from the library mantel above"],
      "A small statue the size of a bottle of milk, made of shiny black wood: the Bombinating Beast (boek p. A131-A132)."),
]
T9W = [
    W("In Stone 4, <i>In the event of a dangerous situation</i> is a way to say 'in geval van een gevaarlijke situatie'.", True,
      "Waar. In the event of / in case of = in geval van (boek p. A114, A126)."),
    W("According to the carjacking text, the number of carjackings in South Africa is going down because of GPS trackers.", False,
      "Niet waar. Despite the measures, 'the number of car jackings has been on the rise' (boek p. A95)."),
    W("In the murder mystery game <i>Shanghai 1943</i>, the murderer is one of the players.", True,
      "Waar. The game 'makes the murderer one of your party' (boek p. A111)."),
    W("In <i>Shanghai 1943</i> every player is allowed to lie about the secrets they were given.", False,
      "Niet waar. 'Only the murderer is allowed to lie' (boek p. A111)."),
    W("In the excerpt, Theodora thinks the burglar came in through the ceiling, but Lemony points out that they came in through a pair of double doors.", True,
      "Waar. 'We got in through a pair of double doors,' I said (boek p. A132)."),
]
T9I = [
    I("Fill in the missing word (Stone 3): <i>Last night, I noticed someone acting ____ at the rear entrance of the gym.</i>", "suspiciously",
      "Stone 3: 'I noticed someone acting suspiciously at the rear entrance of the gym.' (boek p. A98)."),
    I("Fill in the missing word (Stone 4): <i>In case of an ____, you should dial 112 immediately.</i>", "emergency",
      "Stone 4: 'In case of an emergency, you should dial 112 immediately.' (boek p. A114)."),
    I("Fill in the missing word (Stone 4): <i>You should keep your ____ from police officers on the scene.</i>", "distance",
      "Stone 4: 'You should keep your distance from police officers on the scene.' (boek p. A114)."),
    I("Fill in the missing word (Stone 4): <i>The audience was told to ____ the premises without delay.</i>", "evacuate",
      "Stone 4: 'The audience was told to evacuate the premises without delay.' (boek p. A114)."),
    I("Fill in the missing word (Stone 4): <i>That email looks authentic, but always ____ of phishing.</i>", "beware",
      "Stone 4: 'That email looks authentic, but always beware of phishing.' (boek p. A114)."),
]
T9O = O("In English: what is a <b>mock trial</b> at school and what do the students do? (See the text 'School court in session!')",
        ["fake/pretend/not real/role", "judge/lawyer/witness/suspect/jury", "case/theft/crime"], 2,
        "A mock trial is a fake trial: students play the roles of judge, lawyer and witness and try a case, for example a theft.",
        "Mock trial = nep-rechtszaak: leerlingen spelen de rollen en behandelen een zaak, bijvoorbeeld de diefstal van een handtas (boek p. A93).")
TOETSEN[39] = ("Toets 9 — Stones & teksten: Reporting a crime, warning people (boek)", "🗣️", T9M, T9W, T9I, T9O)

# ---------------------------------------------------------------- Toets 10: eindtoets
T10M = [
    M("Which English word means <b>toeschouwer</b> (Dutch)?", "onlooker", ["victim", "witness", "lawyer"],
      "Onlooker = toeschouwer; victim = slachtoffer, witness = getuige, lawyer = advocaat (boek p. A124)."),
    M("What does <b>to scam</b> mean in Dutch?", "oplichten", ["overvallen", "openbreken", "lastigvallen"],
      "To scam = oplichten; to mug = overvallen, to force (open) = openbreken, to harass = lastigvallen (boek p. A124)."),
    M("Choose the correct form: <i>The detective ____ (to check) the lock before he walked into the room.</i>", "had checked",
      ["has checked", "was checking", "had check"],
      "'Before' + an earlier action: past perfect = had + past participle (boek p. A102)."),
    M("Which sentence uses the prepositions correctly?", "My phone was stolen on the bus at 5 pm.",
      ["My phone was stolen in the bus at 5 pm.", "My phone was stolen on the bus in 5 pm.", "My phone was stolen at the bus on 5 pm."],
      "On + public transport; at + a specific time of day (boek p. A104)."),
    M("Which sentence is the passive form of <i>The thieves stole three paintings</i>?", "Three paintings were stolen by the thieves.",
      ["Three paintings have been stolen by the thieves.", "Three paintings was stolen by the thieves.", "Three paintings were being stolen by the thieves."],
      "Past simple passive: was/were + past participle; the subject is plural, so 'were stolen' (boek p. A119)."),
    M("Which sentence from Stone 3 describes what vandals did?", "Some vandals covered the statue with offensive words.",
      ["Some vandals covered the statue by offensive words.", "Some vandals threatened the statue with offensive words.", "Some vandals broke into the statue with offensive words."],
      "Stone 3: 'Some vandals covered the building/statue with graffiti/offensive words.' (boek p. A98)."),
    M("<i>You are not permitted to park your vehicle here. If you do, you may be <b>fined</b>.</i> What does fined mean?", "beboet",
      ["beschuldigd", "vrijgelaten", "overvallen"],
      "To fine = beboeten (boek p. A124-A125)."),
    M("From what age can you play the game <i>Shanghai 1943</i> in Singapore?", "16 and older", ["10 and older", "18 and older", "21 and older"],
      "'AGE: 16 and older' (boek p. A111)."),
    M("What is the purpose of the <b>job vacancy</b> next to the carjacking text?", "To find a new pilot for the helicopter company Henley Air",
      ["To sell GPS tracking devices to car owners", "To warn drivers about carjackers", "To offer driving lessons to young people"],
      "The vacancy is a job advertisement for a vehicle recovery pilot at Henley Air; the main text informs (boek p. A95)."),
]
T10W = [
    W("<b>Fishy</b> can mean 'verdacht, bedenkelijk' in Dutch.", True, "Waar. Fishy = verdacht, bedenkelijk (boek p. A124)."),
    W("<b>Reckless</b> means 'verantwoordelijk' in Dutch.", False,
      "Niet waar. Reckless = roekeloos; (ir)responsible = (on)verantwoordelijk (boek p. A124)."),
    W("The past perfect is formed with <i>has/have</i> + past participle.", False,
      "Niet waar. Past perfect = had + past participle; has/have is the present perfect (boek p. A102)."),
    W("In <i>The thief had escaped before they entered the house</i>, the verb 'entered' is in the past simple.", True,
      "Waar. 'Had escaped' = past perfect (earlier action); 'entered' = past simple (boek p. A102)."),
    W("According to the text, Colonel Blood attacked Talbot Edwards and was never punished for his crime.", True,
      "Waar. 'Amazingly, Blood was never punished for his crime.' (boek p. A106)."),
]
T10I = [
    I("Fill in the English noun for <i>onruststoker</i>: <i>The school sent the ____ home after he started a fight.</i>", "troublemaker",
      "Troublemaker = onruststoker (boek p. A124)."),
    I("Fill in the English verb for <i>bedreigen</i>: <i>The man began to ____ the shop assistant with a knife.</i>", "threaten",
      "To threaten = bedreigen (boek p. A124)."),
    I("Fill in the past perfect of (to leave): <i>The thief ____ the building before the alarm went off.</i>", "had left",
      "Past perfect: had + past participle (boek p. A102)."),
    I("Fill in the passive (past simple) of (to arrest): <i>Two men ____ at the station last night.</i>", "were arrested",
      "Past simple passive, plural subject: were + past participle (boek p. A119)."),
    I("Fill in the missing word (Stone 4): <i>In the ____ of a dangerous situation, follow the instructions of the school staff.</i>", "event",
      "Stone 4: 'In the event of a dangerous situation, follow the instructions of the school staff.' (boek p. A114)."),
]
T10O = O("Last Friday evening, a man was climbing through your neighbour's window. You phone the police. What do you say? Write 2 sentences in English and use Stone 3.",
         ["report/incident", "saw/noticed", "suspicious/suspiciously/broke in/force/forced/after he had"], 2,
         "I'd like to report a crime. Last night I noticed a man acting suspiciously at my neighbour's house; I saw that he entered the house after he had forced the window.",
         "Stone 3 Reporting a crime: 'I'd like to report a crime', 'I noticed someone acting suspiciously', 'I saw that he entered ... after he had forced the door open' (boek p. A98).")
TOETSEN[40] = ("Toets 10 — Hoofdstuk 2 Eindtoets: woorden, grammatica, Stones & teksten (boek)", "🏆", T10M, T10W, T10I, T10O)


def norm(s):
    return re.sub(r'[^a-z0-9 ]+', '', re.sub(r'<[^>]+>', '', s).lower().replace("'", '')).strip()


def bestaande():
    """Vraagteksten van examen_6..10 en h2_1..3 (niet herhalen)."""
    texts = []
    for f in [f'examen_{n}.js' for n in range(6, 11)] + [f'h2_{n}.js' for n in range(1, 4)]:
        txt = open(os.path.join(ROOT, f), encoding='utf-8').read()
        texts += [json.loads('"' + m + '"') for m in re.findall(r'"vraag": "((?:[^"\\]|\\.)*)"', txt)]
    return [norm(t) for t in texts]


def controleer(nr, vr, oud):
    for v in vr:
        n = norm(v["vraag"])
        for o in oud:
            r = difflib.SequenceMatcher(None, n, o).ratio()
            assert r < 0.8, f"examen_{nr}: lijkt op bestaande vraag ({r:.2f}): {v['vraag']} <> {o}"
        if v["type"] == "invul":
            for a in v["antwoord"].split('|'):
                assert norm(a) not in n, f"examen_{nr}: antwoord in vraag: {v['vraag']}"
        if v["type"] == "waaronwaar":
            assert v["uitleg"].startswith(("Waar.", "Niet waar.")), v["uitleg"]
            assert v["uitleg"].startswith("Waar.") == v["antwoord"], v["vraag"]
        if v["type"] == "open":
            assert v["minTreffers"] <= len(v["sleutelwoorden"])
    assert sum(v["type"] == "waaronwaar" and not v["antwoord"] for v in vr) >= 2
    assert len(vr) == 20 and len({norm(v["vraag"]) for v in vr}) == 20


def volgorde(v):
    k = ["type", "vraag", "opties", "antwoord", "sleutelwoorden", "minTreffers", "modelantwoord", "uitleg"]
    return {x: v[x] for x in k if x in v}


def main():
    rng = random.Random('gen_engels_h2_boek')
    oud = bestaande()
    for nr, (titel, icoon, ms, ws, ins, o) in TOETSEN.items():
        vr = rangschik([dict(x) for x in ms], [dict(x) for x in ws], [dict(x) for x in ins], dict(o))
        vr = [volgorde(v) for v in plaats(vr, rng)]
        n, tot = langste_aandeel(vr)
        assert n / tot <= 0.4, f"examen_{nr}: juiste optie {n}/{tot} keer langste"
        controleer(nr, vr, oud)
        ex = {"id": f"ex-h3-eng-{nr}", "hoofdstuk": 2, "hoofdstukTitel": "Hoofdstuk 2 — Crime", "titel": titel,
              "vak": "Engels · HAVO 3 (H2)", "icoon": icoon, "duurMin": 25, "vragen": vr}
        schrijf(os.path.join(ROOT, f'examen_{nr}.js'),
                f"/* Proeftoets {titel}\n   Stepping Stones 3 HAVO Hoofdstuk 2 — gegenereerd door tools/gen_engels_h2_boek.py, uit het boek */\n",
                "DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")
        print(nr, titel, f"langste {n}/{tot}")


if __name__ == '__main__':
    main()

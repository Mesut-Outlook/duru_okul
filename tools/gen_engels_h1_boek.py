#!/usr/bin/env python3
"""Engels HAVO 3 (Stepping Stones 3) · Hoofdstuk 1 The world around you — 5 extra proeftoetsen STRIKT uit het boek.
Schrijft havo3/engels/js/data/examen_31..35.js (ex-h3-eng-31..35 = Toets 6..10). Bron: inbox/2026-2027/engels/engels_h01_*.
Paginanummers 'A..' = OCR-markers (boek p.A36-83). Zodra Duru een toets gemaakt heeft: id-inhoud niet meer wijzigen."""
import json, os, random, re, subprocess, difflib

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..', 'havo3', 'engels', 'js', 'data')


def M(vraag, goed, fout, uitleg):
    assert len(fout) == 3, vraag
    return {"type": "mc", "vraag": vraag, "_goed": goed, "_fout": fout, "uitleg": uitleg}


def W(vraag, antwoord, uitleg):
    assert uitleg.startswith("Waar." if antwoord else "Niet waar."), vraag
    return {"type": "waaronwaar", "vraag": vraag, "antwoord": antwoord, "uitleg": uitleg}


def I(vraag, antwoord, uitleg):
    assert "____" in vraag, vraag
    return {"type": "invul", "vraag": vraag, "antwoord": antwoord, "uitleg": uitleg}


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


PATROON = ['mc', 'mc', 'W', 'I', 'mc', 'W', 'I', 'mc', 'mc', 'W', 'I', 'mc', 'O', 'mc', 'W', 'I', 'mc', 'W', 'I', 'mc']


def rangschik(mcs, ws, ivs, o):
    assert (len(mcs), len(ws), len(ivs)) == (9, 5, 5), (len(mcs), len(ws), len(ivs))
    assert sum(not w["antwoord"] for w in ws) >= 2
    bron = {'mc': iter(mcs), 'W': iter(ws), 'I': iter(ivs), 'O': iter([o])}
    return [next(bron[t]) for t in PATROON]


def schrijf(pad, kop, obj):
    with open(pad, 'w', encoding='utf-8') as f:
        f.write(kop)
        f.write(obj)


# ============ Toets 6 — Woordentoets NL -> EN (Theme words + woordenlijsten, boek p.A76-A77) ============
T6 = rangschik(
    [M("Which English Theme word means <i>kinderachtig</i>?", "childish", ["sensible", "sincere", "stubborn"],
       "Childish = kinderachtig (Theme words, Describing people, boek p.A76)."),
     M("Which English Theme word means <i>buitenbeentje</i>?", "outcast", ["peer", "colleague", "companion"],
       "Outcast = buitenbeentje; peer = leeftijdsgenoot, colleague = collega, companion = kameraad (boek p.A76)."),
     M("Which English Theme phrase means <i>het uitmaken</i>?", "to break up", ["to lose touch with", "to blend in", "to share with"],
       "To break up = het uitmaken; to lose touch with = contact verliezen met (boek p.A76)."),
     M("Which English Theme phrase means <i>Raad eens?</i>?", "Guess what?", ["You know what?", "Are you serious?", "No way!"],
       "Guess what? = Raad eens?; You know what? = Weet je wat? (boek p.A76)."),
     M("Which English Theme phrase means <i>het er niet mee eens zijn</i>?", "to beg to differ", ["to object to", "to have in common", "to argue"],
       "To beg to differ = het er niet mee eens zijn; to object to = bezwaar maken tegen (boek p.A76)."),
     M("Which English Theme phrase means <i>geen sprake van</i>?", "out of the question", ["on the contrary", "to help each other out", "it depends"],
       "Out of the question = geen sprake van; on the contrary = integendeel (boek p.A76)."),
     M("Which English word means <i>aanstekelijk</i> (Vocabulary C Reading)?", "contagious", ["extensive", "uncomfortable", "inferior"],
       "Contagious = aanstekelijk: 'Yawning is highly contagious' (boek p.A77)."),
     M("Which English word means <i>noodzaak</i> (Vocabulary C Reading)?", "necessity", ["trigger", "competency", "cue"],
       "Necessity = noodzaak; trigger = aanzet, competency = bekwaamheid, cue = aanwijzing (boek p.A77)."),
     M("Which English word means <i>speels</i> (Vocabulary F Listening)?", "playful", ["silly", "thrilled", "grateful"],
       "Playful = speels: 'Our new puppy is very playful' (boek p.A77).")],
    [W("The English Theme word <i>superficial</i> means <i>oppervlakkig</i> in Dutch.", True,
       "Waar. Superficial = oppervlakkig (Theme words, boek p.A76)."),
     W("The English Theme phrase <i>to suppose</i> means <i>bezwaar maken tegen</i>.", False,
       "Niet waar. To suppose = veronderstellen; bezwaar maken tegen = to object to (boek p.A76)."),
     W("The English word <i>peer</i> means <i>collega</i> in Dutch.", False,
       "Niet waar. Peer = leeftijdsgenoot; collega = colleague (boek p.A76)."),
     W("The English Theme word <i>apparently</i> means <i>blijkbaar</i>.", True,
       "Waar. Apparently = blijkbaar (Keeping a conversation going, boek p.A76)."),
     W("The English Theme phrase <i>exactly</i> means <i>zeker weten</i>.", False,
       "Niet waar. Exactly = precies; zeker weten = for sure (boek p.A76).")],
    [I("Fill in the English Theme phrase for <i>Weet je wat?</i>: <i>____ what? I might join you for the clean-up.</i>", "you know|know",
       "You know what? = Weet je wat? (Stone 1, boek p.A50 / p.A76)."),
     I("Fill in the English Theme word: a <i>gemeenschappelijke vriend</i> is a ____ friend.", "mutual",
       "Mutual friend = gemeenschappelijke vriend (boek p.A76)."),
     I("Fill in the English noun for <i>vertrouwen</i>: <i>Their partnership was based on ____ and respect.</i>", "trust",
       "Trust = vertrouwen (puzzle Solve the puzzle, boek p.A45 / p.A76)."),
     I("Fill in the English word for <i>kennis</i> (iemand die je kent): <i>Kayleigh is not a close friend of mine, just an ____.</i>", "acquaintance",
       "Acquaintance = kennis (boek p.A44 / p.A76)."),
     I("Fill in the English Theme word for <i>hoe dan ook</i>: <i>____, it was lovely talking to you.</i>", "anyway",
       "Anyway = hoe dan ook (Stone 1, boek p.A50 / p.A76).")],
    O("Name two Theme words or phrases from the chapter that you can use to <b>disagree</b> with someone (list: Expressing (dis)agreement).",
      ["beg to differ/object to/doubt/argue", "on the contrary/out of the question/not necessarily"], 1,
      "You can say: 'I beg to differ' or 'Out of the question' / 'On the contrary'.",
      "Voor onenigheid: to beg to differ, to object to, to doubt, to argue, on the contrary, out of the question, not necessarily (boek p.A76).")
)

# ============ Toets 7 — Woorden EN -> NL in context (zinnen uit de woordenlijsten A, C, F, G) ============
T7 = rangschik(
    [M("<i>That new computer game is quite <b>addictive</b>, so I went to bed way too late!</i> What does <b>addictive</b> mean?", "verslavend",
       ["aanstekelijk", "bevredigend", "onbelangrijk"], "Addictive = verslavend (Vocabulary A Watching, boek p.A76)."),
     M("<i>Victoria says her job is financially <b>rewarding</b> but she makes long hours.</i> What does <b>rewarding</b> mean?", "bevredigend",
       ["ongemakkelijk", "minderwaardig", "onderzoekend"], "Rewarding = bevredigend (boek p.A76)."),
     M("<i>Often the <b>image</b> of motorcycle riders is that they are really tough guys.</i> What does <b>image</b> mean?", "imago",
       ["identiteit", "standpunt", "eerste indruk"], "Image = imago; identity = identiteit (boek p.A76; strategy p.A40)."),
     M("<i>I won't give you my opinion because I don't want it to <b>influence</b> your decision.</i> What does <b>influence</b> mean?", "beïnvloeden",
       ["beweren", "benadrukken", "aanmoedigen"], "Influence = beïnvloeden (boek p.A76)."),
     M("<i>Dad is <b>primarily</b> responsible for the household tasks.</i> What does <b>primarily</b> mean?", "voornamelijk",
       ["uitsluitend", "onmiddellijk", "waarschijnlijk"], "Primarily = voornamelijk (Vocabulary G Reading, boek p.A77)."),
     M("<i>Annie wears <b>goggles</b> when we go skiing, but I prefer wearing sunglasses.</i> What are <b>goggles</b>?", "(veiligheids)bril",
       ["beschermende handschoenen", "skihelm of muts", "stevige skischoenen"], "Goggles = (veiligheids)bril (boek p.A77; Vocabulary exercise p.A64)."),
     M("<i>My dog shows me <b>affection</b> by giving me a big kiss every time I get home.</i> What does <b>affection</b> mean?", "liefde, genegenheid",
       ["voldoening, tevredenheid", "bewondering, respect", "vertrouwen, loyaliteit"], "Affection = liefde, genegenheid (boek p.A77)."),
     M("<i>Pupils going on the trip are required to have their parents sign a <b>consent</b> form.</i> What does <b>consent</b> mean?", "goedkeuring",
       ["voorspelling", "registratie", "prestatie"], "Consent = goedkeuring (boek p.A77)."),
     M("<i>The mechanic gave me an <b>estimate</b> of £450 for the repair of my car.</i> What does <b>estimate</b> mean?", "schatting",
       ["definitieve rekening", "korting op reparatie", "garantie op reparatie"], "Estimate = schatting (Vocabulary C Reading, boek p.A77).")],
    [W("The English word <i>accurate</i> means <i>juiste</i> in Dutch.", True,
       "Waar. Accurate = juiste: 'If you don't enter the accurate password ...' (boek p.A77)."),
     W("The English word <i>to exclude</i> means <i>erbij horen</i>.", False,
       "Niet waar. To exclude = buitensluiten; erbij horen = to blend in (boek p.A76/A77)."),
     W("In <i>I cannot <b>stress</b> the importance of a healthy diet enough</i>, <b>to stress</b> means <i>benadrukken</i>.", True,
       "Waar. To stress = benadrukken (Vocabulary G Reading, boek p.A77)."),
     W("The English word <i>to increase</i> means <i>verlagen</i> in Dutch.", False,
       "Niet waar. To increase = verhogen, vergroten (Vocabulary F Listening, boek p.A77)."),
     W("The English word <i>pressure</i> means <i>prestatie</i> in Dutch.", False,
       "Niet waar. Pressure = druk; prestatie = accomplishment (boek p.A77).")],
    [I("Fill in the English word for <i>uitgebreid</i>: <i>Detectives are doing ____ research to find out who stole the painting.</i>", "extensive",
       "Extensive = uitgebreid (Vocabulary C Reading, boek p.A77)."),
     I("Fill in the English word for <i>vloeiend</i>: <i>Frank lived in Mexico for ten years, so he speaks Spanish ____.</i>", "fluently",
       "Fluently = vloeiend (Vocabulary F Listening, boek p.A77)."),
     I("Fill in the English word for <i>neigen</i>: <i>Sam and John ____ to be late to work.</i>", "tend",
       "To tend to = neigen (boek p.A77)."),
     I("Fill in the English word for <i>enthousiast zijn</i>: <i>I just found out I got the leading part in the play; I'm so ____!</i>", "thrilled",
       "Thrilled = enthousiast (Vocabulary G Reading, boek p.A77)."),
     I("Fill in the English word for <i>dankbaar</i>: <i>Instead of complaining all the time, you should be ____ for what you have!</i>", "grateful",
       "Grateful = dankbaar (Vocabulary F Listening, boek p.A77).")],
    O("<i>Lisa always puts me down in front of other people which makes me feel inferior.</i> Explain in English how Lisa's behaviour makes the speaker feel.",
      ["less important/worse/lower/unimportant/worth less"], 1,
      "The speaker feels less important and worse than other people.",
      "Inferior = minderwaardig: je voelt je minder dan anderen (Vocabulary C Reading, boek p.A77).")
)

# ============ Toets 8 — Grammatica (some/any/every/no-, gerund & to + infinitive, vragen & ontkenningen) ============
T8 = rangschik(
    [M("Which compound completes the sentence? <i>I can't find my sweater ____.</i>", "anywhere", ["nowhere", "somewhere", "everywhere"],
       "Voorbeeld uit het boek: 'I can't find my sweater anywhere.' (Grammar 1, boek p.A79)."),
     M("Which compound completes the sentence? <i>There was ____ in the shop when we came there.</i>", "nobody", ["somebody", "everybody", "anybody"],
       "Het boek: 'There was nobody in the shop when we came there.' (boek p.A79)."),
     M("Which compound is written as <b>two words</b>, according to the Note in Grammar 1?", "no one", ["nobody", "someone", "everyone"],
       "Note: no- + -one wordt als twee woorden geschreven: no one (boek p.A54)."),
     M("Which sentence is correct? The verb <i>to avoid</i> is followed by a gerund.", "We avoid travelling during rush hour.",
       ["We avoid to travel during rush hour.", "We avoid travel during rush hour.", "We avoid travelled during rush hour."],
       "Gerund (verb + -ing) na to avoid: 'We avoid travelling during rush hour.' (Grammar 2, boek p.A56)."),
     M("Which form completes the sentence? <i>I hope ____ a famous singer one day.</i>", "to be", ["being", "be", "been"],
       "To hope + to + infinitive: 'I hope to be a famous singer one day.' (boek p.A56)."),
     M("Which of these verbs is followed by <b>to + infinitive</b> (not by a gerund) in the book?", "to refuse", ["to avoid", "to miss", "to dislike"],
       "To hope, to ask, to refuse, to expect + to + infinitive; to (dis)like, to love, to miss, to avoid + gerund (boek p.A56/A79)."),
     M("Which question is correct (past simple, main verb <i>to tell</i>)?", "Did he tell you about the trip?",
       ["Did he told you about the trip?", "Was he tell you about the trip?", "Told he you about the trip?"],
       "Rule 2: did + onderwerp + infinitief: 'Did he tell you about the trip?' (Grammar 3, boek p.A71)."),
     M("Which negation is correct (present simple, main verb <i>to sleep</i>)?", "The cat doesn't sleep in our bed.",
       ["The cat doesn't sleeps in our bed.", "The cat isn't sleep in our bed.", "The cat not sleep in our bed."],
       "Rule 2: doesn't + infinitief: 'The cat doesn't sleep in our bed.' (boek p.A71)."),
     M("How do you form a question in the <b>present perfect</b>, according to Grammar 3?", "Rule 1: put the auxiliary verb (have) first",
       ["Rule 2: put a form of to do first", "Rule 2: put to do first and add -ing", "Rule 1: put the main verb first and add n't"],
       "Andere tijden dan present/past simple hebben altijd een hulpwerkwoord: Rule 1 (boek p.A71).")],
    [W("The compound <i>nobody</i> consists of <i>no</i> and <i>body</i> and refers to people.", True,
       "Waar. -body / -one verwijzen naar mensen (Grammar 1, boek p.A54)."),
     W("A <b>gerund</b> is a verb + -ing that is used as a noun.", True,
       "Waar. 'A verb + -ing (gerund) is a verb that is used as a noun' (Grammar 2, boek p.A56)."),
     W("After the verb <i>to avoid</i> you always use <b>to + infinitive</b>.", False,
       "Niet waar. Na to avoid volgt een gerund: 'We avoid travelling during rush hour.' (boek p.A56)."),
     W("To make a question in the past simple with the main verb <i>to find</i>, you put the main verb at the beginning (Rule 1).", False,
       "Niet waar. Bij andere werkwoorden gebruik je Rule 2: 'Did you find your book yesterday?' (boek p.A71)."),
     W("In <i>Is he doing his homework?</i> you do not need a form of to do, because <i>to be</i> is an auxiliary verb (Rule 1).", True,
       "Waar. Met to be en hulpwerkwoorden zet je dat werkwoord vooraan (Rule 1, boek p.A71).")],
    [I("Fill in the compound for <i>niets</i>: <i>There is ____ I can do about it.</i>", "nothing",
       "No- + -thing = nothing (Grammar 1, boek p.A54/A79)."),
     I("Fill in the compound for <i>iedereen</i>: <i>I think ____ was there.</i>", "everybody|everyone",
       "Every- + -body/-one (boek p.A79)."),
     I("Fill in the gerund of <i>to drive</i> after <i>to love</i>: <i>I love ____ along the coast.</i>", "driving",
       "Gerund na to love: 'I love driving along the coast.' (boek p.A79)."),
     I("Fill in <i>to refuse</i> + the correct form of <i>take</i>: <i>I refuse ____ the test.</i>", "to take",
       "To refuse + to + infinitive: 'I refuse to take the test.' (boek p.A79)."),
     I("Complete the question (to find — you): <i>____ your book yesterday?</i>", "did you find",
       "Past simple, Rule 2: 'Did you find your book yesterday?' (oefening boek p.A71).")],
    O("Explain in your own words when you add a form of <i>to do</i> to form questions and negations in the present and past simple.",
      ["main verb/other verb/other verbs", "to be/auxiliary/can/may"], 1,
      "You add to do when the sentence has another main verb; with to be or an auxiliary verb such as can you do not need it.",
      "Rule 2 geldt voor andere hoofdwerkwoorden; to be en hulpwerkwoorden (can, may) gebruiken Rule 1 (Grammar 3, boek p.A71).")
)

# ============ Toets 9 — Stones / useful phrases + teksten ============
T9 = rangschik(
    [M("Which phrase from Stone 2 do you use to politely show that you only partly agree?", "I see your point, but lots of teens just don't have the time.",
       ["That's right. I enjoyed setting up a street fair in my neighbourhood.", "Absolutely. I loved organising activities in the park.",
        "Yes, that's for sure. Are you with me on that? Absolutely!"],
       "I see your point, but ... = ik snap je punt, maar ... (Stone 2, boek p.A66)."),
     M("Which question from Stone 1 helps you to start a conversation about someone's weekend?", "How was your weekend? Did you go anywhere interesting?",
       ["Would you agree that everybody should try to join in on local activities?", "Don't you think travelling abroad makes you more sociable?",
        "Are you with me on that? Do you agree with the whole idea so far?"],
       "Stone 1, Starting and maintaining a conversation (boek p.A50/A78)."),
     M("Which phrase from Stone 1 do you use to end a conversation politely?", "Anyway, it was lovely talking to you.",
       ["Speaking of which, it was lovely talking to you today.", "That reminds me, it was lovely talking to you today.", "As a matter of fact, it was lovely talking to you."],
       "Anyway, it was lovely talking to you. / Well, nice meeting up with you. (Stone 1, boek p.A50)."),
     M("What can you add to a sentence to find out whether someone agrees with you?", "A tag question, e.g. <i>doesn't it?</i>",
       ["A gerund at the end, e.g. <i>agreeing</i>", "A compound word, e.g. <i>nobody</i> or <i>anything</i>", "A negation, e.g. <i>not at all</i> or <i>no way</i>"],
       "Tag question: 'Volunteering makes you feel like part of the community, doesn't it?' (Stone 2, boek p.A66)."),
     M("According to Professor Sophie Scott, why do we laugh more when we are in company?", "Because we want others to like us and to bond with us",
       ["Because we are afraid of the silence when we are in a group", "Because laughing makes us feel superior to the people around us", "Because we need laughing tracks to understand all the jokes"],
       "No laughing matter, paragraph 3 (boek p.A47)."),
     M("What is the best estimate of how often people laugh in social situations (No laughing matter)?", "About seven times every ten minutes",
       ["About thirty times every ten minutes", "About seven times every hour", "About once every ten minutes"],
       "'people laugh around seven times every ten minutes' (paragraph 3, boek p.A47). Dertig keer is hoeveel méér we met anderen lachen."),
     M("Why were laughing tracks added to TV comedy shows?", "At home people were no longer part of an audience and missed the cues",
       ["Comedians on screen often forgot their jokes while filming", "Theatres wanted to sell more tickets to people at home", "Viewers at home could not hear the jokes on their own TVs"],
       "Paragraph 7 (boek p.A47): thuis misten mensen de signalen (cues) van een publiek."),
     M("What is <b>sharenting</b>, according to the article <i>When teenagers realize their whole life is already online</i>?", "Parents overusing social media to share pictures of their children",
       ["Teenagers sharing pictures of their parents on private accounts", "Children asking their parents for permission before posting", "Schools and sports teams sharing homework with other parents"],
       "Sharenting = share + parenting (paragraph 3, boek p.A63)."),
     M("What does the Maori greeting <i>hongi</i> mean literally, according to the Elders?", "Sharing of breath",
       ["Sharing of food", "Respect for the land", "Welcome to the people"],
       "'the literal meaning of hongi is sharing of breath' (Countries & Cultures, boek p.A58).")],
    [W("Professor Scott says that we laugh about thirty times more when we are with other people than when we are alone.", True,
       "Waar. No laughing matter, paragraph 3 (boek p.A47)."),
     W("Megan's mother ignored her concerns and kept posting pictures of her as before.", False,
       "Niet waar. Haar moeder stemde ermee in voorzichtiger te zijn en Megan heeft vetorecht (boek p.A63)."),
     W("Alena Kravchenko washes her long hair every day.", False,
       "Niet waar. Zij wast haar haar maar één keer per drie weken (Real-life Rapunzel, boek p.A73)."),
     W("After a hongi greeting, a visitor (<i>manuhiri</i>) is considered to be <i>tangata whenua</i>, one of the people of the land.", True,
       "Waar. 'you are no longer considered to be a manuhiri but tangata whenua' (boek p.A58)."),
     W("In the poem <i>Shoulders</i>, the man's jacket says FRAGILE, HANDLE WITH CARE.", False,
       "Niet waar. 'Nowhere does his jacket say FRAGILE' - hij is niet gemarkeerd (boek p.A83).")],
    [I("Complete the Stone 2 question: <i>Would you ____ that everybody should try to join in on local activities?</i>", "agree",
       "Would you agree that ...? (Stone 2, boek p.A66)."),
     I("Complete the Stone 1 phrase: <i>In ____, I went to one last week.</i>", "fact",
       "In fact, ... = in feite (Stone 1, boek p.A50)."),
     I("Complete the sentence from the Li Ziqi interview: <i>I didn't ____ to become famous.</i>", "expect",
       "'I didn't expect to become famous.' (boek p.A70)."),
     I("Parents overusing social media to share pictures of their children is called ____.", "sharenting",
       "Sharenting (boek p.A63)."),
     I("Complete the sentence from No laughing matter: <i>Laughing is also ____: seeing someone else laugh makes you laugh too.</i>", "contagious",
       "'laughing becoming contagious' (paragraph 6, boek p.A47).")],
    O("In the article, Megan has 'veto power'. Explain in your own words what this means for her mother's online sharing.",
      ["stop/refuse/forbid/say no/block/prevent", "post/picture/photo/upload"], 1,
      "Megan can stop her mother from posting pictures of her; she can say no.",
      "Veto power = het recht om iets te verbieden: haar moeder vertelt het vooraf en Megan mag nee zeggen (boek p.A63/A65).")
)

# ============ Toets 10 — Eindtoets (mix, niveau 'Check') ============
T10 = rangschik(
    [M("Which Theme word means <i>eigenlijk</i>?", "actually", ["apparently", "anyway", "exactly"],
       "Actually = eigenlijk; apparently = blijkbaar; anyway = hoe dan ook; exactly = precies (boek p.A76)."),
     M("Complete the sentence: <i>You never get a second chance to make a good ____.</i>", "first impression",
       ["first estimate", "first accomplishment", "first trigger"],
       "Vocabulary Watching (boek p.A41): 'You never get a second chance to make a good first impression.'"),
     M("According to the strategy <i>First impressions</i>, what is the difference between image and identity?", "Identity is who you are; image is how you would like others to see you",
       ["Image is who you really are; identity is how you would like others to see you", "Image is a photo you post; identity is a video you watch",
        "Image is how others see you; identity is how you see the world"],
       "'Identity is about who you are, and image is about how you would like others to see you.' (boek p.A40)."),
     M("Which compound completes the sentence? <i>There isn't ____ we can do.</i>", "anything", ["nothing", "something", "everything"],
       "Grammar 1 (boek p.A79): 'There isn't anything we can do.' Nothing zou een dubbele ontkenning zijn."),
     M("Which form completes the sentence? <i>We miss ____ in the park.</i>", "running", ["to run", "run", "ran"],
       "To miss + gerund: 'We miss running in the park.' (Grammar 2, boek p.A79)."),
     M("Which sentence is correct?", "They weren't watching TV when I came home.",
       ["They didn't watching TV when I came home.", "They didn't were watching TV when I came home.", "They weren't watch TV when I came home."],
       "Past continuous = Rule 1: weren't + -ing (Grammar 3, boek p.A71)."),
     M("You want to know whether someone agrees with you. Which phrase from Stone 2 fits?", "Are you with me on that?",
       ["I suppose so, but I prefer to meet people in person.", "As a matter of fact, I'd love to go abroad.", "Anyway, it was lovely talking to you."],
       "Are you with me on that? (Stone 2, boek p.A66)."),
     M("According to No laughing matter, in which situation can you feel excluded?", "When everyone is laughing at a joke that you did not get",
       ["When you tell a joke and nobody around you is laughing", "When you laugh together with a group of close friends", "When you hear a laughing track on a comedy show on television"],
       "Paragraph 4 (boek p.A47): 'everyone is laughing - except for you'."),
     M("According to Barclays, how can online information be used for criminal activities?", "Criminals store a name, date of birth and address and open accounts once the person turns 18",
       ["Criminals send emails to the parents with fake photos of their own children", "Criminals post pictures of teenagers online without asking for their consent", "Criminals use geotagged photos to find out which houses are empty"],
       "Paragraph 5 (boek p.A63): identity fraud.")],
    [W("<i>Sensible</i> and <i>sensitive</i> both mean <i>gevoelig</i> in Dutch.", False,
       "Niet waar. Sensible = verstandig; sensitive = gevoelig (boek p.A76)."),
     W("The compound <i>no one</i> is written as two words.", True,
       "Waar. 'Note! The compound no- + -one is written as two words: no one.' (boek p.A54)."),
     W("The verb <i>to hope</i> is followed by a gerund (verb + -ing).", False,
       "Niet waar. To hope + to + infinitive: 'I hope to be a famous singer one day.' (boek p.A56)."),
     W("According to the strategy, <i>image</i> says something about how you would like other people to see you.", True,
       "Waar. First impressions (boek p.A40)."),
     W("To make a question in the <b>present perfect</b>, you use Rule 2 and put a form of <i>to do</i> at the beginning.", False,
       "Niet waar. Andere tijden hebben een hulpwerkwoord (have): Rule 1 (boek p.A71).")],
    [I("Fill in the English verb for <i>beweren</i>: <i>Many toothpaste brands ____ their product will give you bright white teeth.</i>", "claim",
       "To claim = beweren (Vocabulary A Watching, boek p.A76)."),
     I("Fill in <i>to refuse</i> + the correct form of <i>use</i>: <i>We refuse ____ plastic straws.</i>", "to use",
       "To refuse + to + infinitive: 'We refuse to use plastic straws.' (boek p.A56)."),
     I("Fill in the compound for <i>niemand</i>: <i>The house is empty. ____ is home.</i>", "no one|nobody",
       "No- + -one/-body: 'The house is empty. No one is home.' (boek p.A55)."),
     I("Complete the question (to be — you): <i>____ serious? That's amazing!</i>", "are you",
       "Present simple of to be = Rule 1: 'Are you serious?' (boek p.A71)."),
     I("Complete the Stone 2 phrase: <i>I ____ your point, but lots of teens just don't have the time.</i>", "see",
       "I see your point, but ... (Stone 2, boek p.A66).")],
    O("Explain in English why laughter is important for people, according to the text No laughing matter.",
      ["bond/belong/belonging/connected", "others/each other/together"], 1,
      "Laughing helps us bond with others and gives us a sense of belonging.",
      "Laughing makes us feel connected and creates a sense of belonging (paragraph 3, boek p.A47).")
)

EXAMENS = {
    31: ("Toets 6 — Woordentoets NL → EN: Theme words (boek)", "📖", T6),
    32: ("Toets 7 — Woorden EN → NL in context (boek)", "🔤", T7),
    33: ("Toets 8 — Grammatica: compounds, gerund, vragen & ontkenningen (boek)", "✏️", T8),
    34: ("Toets 9 — Stones & teksten: laughter, sharenting, hongi (boek)", "💬", T9),
    35: ("Toets 10 — Eindtoets Hoofdstuk 1 (boek)", "🏁", T10),
}


def norm(s):
    return re.sub(r'[^a-z0-9 ]', '', re.sub(r'<[^>]+>', '', s).lower()).strip()


def bestaande():
    js = ("global.DURU={register:o=>(o.vragen||[]).forEach(v=>out.push(v.vraag)),registerExamen:o=>o.vragen.forEach(v=>out.push(v.vraag))};"
          "const out=[];const fs=require('fs');const d=process.argv[1];"
          "for(const f of ['examen_1','examen_2','examen_3','examen_4','examen_5','h1_1','h1_2','h1_3'])require(d+'/'+f+'.js');"
          "console.log(JSON.stringify(out))")
    return [norm(x) for x in json.loads(subprocess.check_output(['node', '-e', js, os.path.abspath(ROOT)]))]


def controleer(vr, oud, nr):
    for v in vr:
        q = norm(v["vraag"])
        r = max((difflib.SequenceMatcher(None, q, o).ratio() for o in oud), default=0)
        assert r < 0.8, f"examen_{nr}: lijkt op bestaande vraag ({r:.2f}): {v['vraag']}"
        if v["type"] == "invul":
            for a in v["antwoord"].split('|'):
                assert norm(a) not in q.replace(norm('____'), ''), f"antwoord in vraag: {v['vraag']}"


def main():
    rng = random.Random(os.path.basename(__file__))
    oud = bestaande()
    for nr, (titel, icoon, vr) in EXAMENS.items():
        assert len(vr) == 20, (nr, len(vr))
        vr = plaats([dict(v) for v in vr], rng)
        n, tot = langste_aandeel(vr)
        assert n / tot <= 0.4, f"examen_{nr}: juiste optie {n}/{tot} keer langste"
        controleer(vr, oud, nr)
        ex = {"id": f"ex-h3-eng-{nr}", "hoofdstuk": 1, "hoofdstukTitel": "Hoofdstuk 1 — The world around you",
              "titel": titel, "vak": "Engels · HAVO 3 (H1)", "icoon": icoon, "duurMin": 25, "vragen": vr}
        schrijf(os.path.join(ROOT, f'examen_{nr}.js'),
                f"/* {titel}\n   Stepping Stones 3 HAVO Hoofdstuk 1 — gegenereerd door tools/gen_engels_h1_boek.py, uit het boek */\n",
                "DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")
        print(f"examen_{nr}: 20 vragen, juiste optie langste {n}/{tot}")


if __name__ == '__main__':
    main()

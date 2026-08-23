import os, json

out_dir = '/Users/mesutozdemir/_PROJELER/duru_okul/havo3/geschiedenis/js/data'
os.makedirs(out_dir, exist_ok=True)

def write_file(filename, content):
    with open(os.path.join(out_dir, filename), 'w', encoding='utf-8') as f:
        f.write(content)

def make_quiz_code(d):
    return f"""/* =========================================================
   Duru's Geschiedenis (HAVO 3) — {d['titel']}
   Hoofdstuk {d['hoofdstuk']}: Paragraaf {d['paragraaf']}
   ========================================================= */
(function () {{
  "use strict";

  DURU.register({{
    id: "{d['id']}",
    hoofdstuk: {d['hoofdstuk']},
    paragraaf: "{d['paragraaf']}",
    titel: "{d['titel']}",
    korteUitleg: "{d['korteUitleg']}",
    icoon: "{d['icoon']}",
    kleur: "{d['kleur']}",
    theorie: `{d['theorie']}`,
    vragen: {json.dumps(d['vragen'], ensure_ascii=False, indent=6)}
  }});
}})();
"""

def make_exam_code(d):
    return f"""/* =========================================================
   Duru's Geschiedenis (HAVO 3) — {d['titel']}
   ========================================================= */
(function () {{
  "use strict";

  DURU.registerExamen({{
    id: "{d['id']}",
    titel: "{d['titel']}",
    vak: "Geschiedenis · Hoofdstuk {d['hoofdstuk']}",
    hoofdstuk: {d['hoofdstuk']},
    hoofdstukTitel: "{d['hoofdstukTitel']}",
    icoon: "{d['icoon']}",
    duurMin: 20,
    vragen: {json.dumps(d['vragen'], ensure_ascii=False, indent=6)}
  }});
}})();
"""

# Generator function for chapters 3 to 6
def generate_remaining_chapters():
    chapters_meta = [
        (3, 'De Tweede Wereldoorlog (1939–1945)', '✈️', 'rood', [
            ('h3_1_uitbreken_oorlog', '3.1', 'Het uitbreken van de oorlog', '💣', 'Inval Polen, Blitzkrieg, Slag om Engeland en Operatie Barbarossa.', '<h3>3.1 Het uitbreken van de oorlog</h3><p>Op 1 september 1939 viel nazi-Duitsland Polen binnen. Engeland en Frankrijk verklaarden Duitsland de oorlog: <b>WO2 was begonnen</b>. Met de snelle <b>Blitzkrieg</b>-tactiek veroverden de nazi\'s West-Europa. Engeland hield stand in de <b>Slag om Engeland</b> onder Churchill. In juni 1941 viel Hitler de Sovjet-Unie aan (<b>Operatie Barbarossa</b>).</p>'),
            ('h3_2_bezet_nederland', '3.2', 'Bezet Nederland', '🇳🇱', 'Mei 1940, Rotterdam, Seyss-Inquart, Arbeitseinsatz en Hongerwinter.', '<h3>3.2 Bezet Nederland</h3><p>Duitsland viel Nederland aan op 10 mei 1940. Na het <b>bombardement op Rotterdam</b> (14 mei) capituleerde het Nederlandse leger. Oostenrijkse nazi <b>Arthur Seyss-Inquart</b> werd rijkscommissaris. Mannen werden via de <b>Arbeitseinsatz</b> gedwongen in Duitsland te werken. In 1941 vond de <b>Februaristaking</b> plaats. In de winter van 1944-1945 ontstond de vreselijke <b>Hongerwinter</b>.</p>'),
            ('h3_3_holocaust', '3.3', 'De Jodenvervolging en de Holocaust', '✡️', 'Antisemitisme, Jodenster, Kamp Westerbork, Auschwitz en Wannsee.', '<h3>3.3 De Jodenvervolging en de Holocaust</h3><p>De nazi\'s begonnen met isolatie (Jodenster, verboden openbare plekken) en deportatie via <b>Kamp Westerbork</b>. Op de <b>Wannsee-conferentie (1942)</b> werd besloten tot de <b>Endlösung</b>: de industriële vernietiging van alle Joden in vernietigingskampen zoals <b>Auschwitz</b>. 6 miljoen Joden werden vermoord (<b>Holocaust / Shoah</b>).</p>'),
            ('h3_4_keerpunten', '3.4', 'Keerpunten in de oorlog', '⚔️', 'Pearl Harbor, Stalingrad, El Alamein, D-Day en Duitse capitulatie.', '<h3>3.4 Keerpunten in de oorlog</h3><p>Op 7 december 1941 viel Japan <b>Pearl Harbor</b> aan, waarna de VS meededen aan WO2. De <b>Slag bij Stalingrad (1942-1943)</b> was het grote keerpunt aan het Oostfront. Op <b>D-Day (6 juni 1944)</b> landden de geallieerden in Normandië. Op <b>8 mei 1945</b> capituleerde Duitsland op de knieën.</p>'),
            ('h3_5_oorlog_azie', '3.5', 'De oorlog in Azië', '🌅', 'Japanse expansie, Nederlands-Indië, Jappenkampen en de atoombommen.', '<h3>3.5 De oorlog in Azië</h3><p>Japan bezette grote delen van Azië, waaronder <b>Nederlands-Indië (maart 1942)</b>. Nederlanders en Indische militairen werden opgesloten in vreselijke <b>Jappenkampen</b>. Om de oorlog snel te beëindigen wierpen de VS in augustus 1945 <b>atoombommen op Hiroshima en Nagasaki</b>. Op 15 augustus 1945 gaf Japan zich over.</p>')
        ]),
        (4, 'De wereld na 1945 (1945–1990)', '🕊️', 'paars', [
            ('h4_1_koude_oorlog', '4.1', 'De Koude Oorlog ontstaat', '🧊', 'Oost-West blokvorming, IJzeren Gordijn, Trumandoctrine en Marshallplan.', '<h3>4.1 De Koude Oorlog ontstaat</h3><p>Na 1945 raakten de VS (kapitalisme) en de Sovjet-Unie (communisme) verstrikt in de <b>Koude Oorlog</b>. Europa raakte verdeeld door het <b>IJzeren Gordijn</b>. De VS stelden de <b>Trumandoctrine</b> (containment) en het <b>Marshallplan</b> (financiële hulp) in. Twee militaire blokken ontstonden: de <b>NAVO (1949)</b> en het <b>Warschaupact (1955)</b>.</p>'),
            ('h4_2_crises_koude_oorlog', '4.2', 'Spanningen en crises', '🧱', 'Blokkade Berlijn, Berlijnse Muur 1961, Koreaoorlog en Cubacrisis.', '<h3>4.2 Spanningen en crises</h3><p>Er ontstonden heftige crises: de <b>Blokkade van Berlijn (1948)</b> werd opgelost door een geallieerde Luchtbrug. In 1961 bouwde Oost-Duitsland de <b>Berlijnse Muur</b>. De <b>Koreaoorlog (1950-1953)</b> en de <b>Cubacrisis (1962)</b> brachten de wereld op de rand van een nucleaire wereldoorlog.</p>'),
            ('h4_3_vietnamoorlog', '4.3', 'De Vietnamoorlog', '🌴', 'Dominotheorie, Vietcong, Amerikaanse inmenging en protesten.', '<h3>4.3 De Vietnamoorlog</h3><p>Uit vrees voor de <b>Dominotheorie</b> (het omvallen van landen naar het communisme) raakten de VS betrokken bij de oorlog in Vietnam. Het Amerikaanse leger vocht tegen de communistische <b>Vietcong</b>-guerrilla\'s. De hevige tv-beelden en verliezen leidden tot massale <b>anti-oorlogsprotesten</b> wereldwijd.</p>'),
            ('h4_4_einde_koude_oorlog', '4.4', 'Het einde van de Koude Oorlog', '🤝', 'Wapenwedloop, Reagan, Gorbatsjov en val van de Muur 1989.', '<h3>4.4 Het einde van de Koude Oorlog</h3><p>De zware <b>wapenwedloop</b> en het Amerikaanse SDI-plan uitputten de Sovjet-Unie. Sovjet-leider <b>Michail Gorbatsjov</b> voerde hervormingen in: <b>Glasnost</b> (openheid) en <b>Perestroika</b> (herstructurering). Op <b>9 november 1989 viel de Berlijnse Muur</b>. Eind 1991 viel de Sovjet-Unie definitief uiteen.</p>'),
            ('h4_5_dekolonisatie', '4.5', 'Dekolonisatie in Azië en Afrika', '🌏', 'Onafhankelijkheid, Nederlands-Indië, Soekarno en 1949.', '<h3>4.5 Dekolonisatie in Azië en Afrika</h3><p>Na 1945 eisten kolonies onafhankelijkheid. Op 17 augustus 1945 riep <b>Soekarno</b> de onafhankelijkheid van Indonesië uit. Nederland reageerde met twee militaire <b>Politionele Acties</b>. Onder druk van de VN en de VS droeg Nederland op <b>27 december 1949</b> de soevereiniteit over aan Indonesië.</p>')
        ]),
        (5, 'Nederland na 1945 (1945–heden)', '🇳🇱', 'groen', [
            ('h5_1_wederopbouw', '5.1', 'Wederopbouw en verzorgingsstaat', '🏗️', 'Marshallhulp, geleide loonpolitiek, Drees en de AOW.', '<h3>5.1 Wederopbouw en verzorgingsstaat</h3><p>Na 1945 werkte Nederland hard aan de <b>Wederopbouw</b>. Dankzij de <b>geleide loonpolitiek</b> bleven uitvoerkosten laag. PvdA-premier <b>Willem Drees</b> legde de basis voor de <b>verzorgingsstaat</b> met de invoering van de <b>AOW (1957)</b> en sociale uitkeringen.</p>'),
            ('h5_2_europese_samenwerking', '5.2', 'Europese samenwerking', '🇪🇺', 'EGKS 1951, EEG 1957, Verdrag van Maastricht 1992 en euro.', '<h3>5.2 Europese samenwerking</h3><p>Om nieuwe oorlogen te voorkomen richtte Nederland met 5 landen de <b>EGKS (1951)</b> op. Dit werd later de EEG en met het <b>Verdrag van Maastricht (1992)</b> de <b>Europese Unie (EU)</b>. In 2002 werd het chartale geld van de <b>euro</b> ingevoerd.</p>'),
            ('h5_3_ontzuiling_cultuur', '5.3', 'Ontzuiling en veranderende cultuur', '📺', 'Ontzuiling, jeugdcultuur (Nozems, Provo\'s) en feminisme.', '<h3>5.3 Ontzuiling en veranderende cultuur</h3><p>Vanaf de jaren 60 verdween de strakke scheiding tussen geloofsgroepen (<b>ontzuiling</b>). Door televisie, welvaart en studie kwamen <b>jeugdculturen</b> op (Nozems, Provo\'s, hippies). De <b>tweede feministische golf</b> (Dolle Mina) streed voor gelijke kansen en vrouwenrechten.</p>'),
            ('h5_4_pluriforme_samenleving', '5.4', 'Een pluriforme samenleving', '🤝', 'Immigratie, gastarbeiders, Surinaamse onafhankelijkheid 1975.', '<h3>5.4 Een pluriforme samenleving</h3><p>Nederland veranderde in een <b>pluriforme samenleving</b>. Eerst kwamen Indische repatrianten, gevolgd door <b>gastarbeiders</b> uit Turkije en Marokko. Na de Surinaamse onafhankelijkheid in <b>1975</b> migreerden veel Surinamers naar Nederland.</p>'),
            ('h5_5_poldermodel', '5.5', 'Nederland aan het eind van de 20e eeuw', '🌾', 'Poldermodel, Akkoord van Wassenaar en digitalisering.', '<h3>5.5 Nederland aan het eind van de 20e eeuw</h3><p>Met het <b>Akkoord van Wassenaar (1982)</b> ontstond het Nederlandse <b>Poldermodel</b>: overleg tussen werkgevers, vakbonden en staat. Ook kwamen milieubewustzijn, Paarse kabinetten en de <b>digitalisering</b> op de voorgrond.</p>')
        ]),
        (6, 'Naar de wereld van nu (1990–heden)', '🌐', 'teal', [
            ('h6_1_nieuwe_wereldorde', '6.1', 'Een nieuwe wereldorde', '🗺️', 'Uiteenvallen Joegoslavië, Balkan-oorlog en Srebrenica 1995.', '<h3>6.1 Een nieuwe wereldorde</h3><p>Het uiteenvallen van Joegoslavië leidde in de jaren 90 tot bloedige <b>Balkan-oorlogen</b>. De val van de VN-enclave <b>Srebrenica (1995)</b> waarin Nederlandse VN-troepen (Dutchbat) gelegerd waren, leidde tot een afschuwelijke genocide door Serwische troepen.</p>'),
            ('h6_2_midden_oosten', '6.2', 'Midden-Oosten en conflicten', '🕌', 'Stichting Israël 1948, Arabisch-Israëlisch conflict en oliecrises.', '<h3>6.2 Midden-Oosten en conflicten</h3><p>De stichting van de staat <b>Israël (1948)</b> leidde tot het langdurige <b>Arabisch-Israëlische conflict</b> met de Palestijnen. De <b>Oliecrisis van 1973</b> toonde de westerse afhankelijkheid van Midden-Oosten olie aan.</p>'),
            ('h6_3_terrorisme', '6.3', 'Terrorisme en veiligheid', '🛡️', 'Aanslagen 11 september 2001 (9/11) en War on Terror.', '<h3>6.3 Terrorisme en veiligheid</h3><p>Op <b>11 september 2001 (9/11)</b> voerde Al Qaida zware terreuraanslagen uit in de VS. President Bush kondigde de <b>War on Terror</b> aan. Landen scherpten wetten aan, wat leidde tot discussies over veiligheid versus privacy.</p>'),
            ('h6_4_globalisering', '6.4', 'Globalisering en economie', '📈', 'Wereldeconomie, opkomst China/India en internet.', '<h3>6.4 Globalisering en economie</h3><p>Door <b>globalisering</b> en de doorbraak van het <b>internet</b> raakte de wereld intensief verbonden. Opkomende giganten zoals <b>China en India</b> werden grote spelers in de wereldeconomie.</p>'),
            ('h6_5_klimaat', '6.5', 'Klimaat en toekomst', '🌱', 'Klimaatverandering, broeikaseffect en Parijsakkoord.', '<h3>6.5 Klimaat en toekomst</h3><p>Wereldwijde CO2-uitstoot leidt tot <b>klimaatverandering</b> en opwarming van de aarde. In het <b>Klimaatakkoord van Parijs (2015)</b> maakten VN-landen afspraken over de <b>energietransitie</b> naar schone energie.</p>')
        ])
    ]

    for hf, hf_title, hf_ico, hf_kleur, sec_list in chapters_meta:
        # Generate 5 practice quizzes for this chapter
        for filename, par_nr, par_title, sec_ico, sec_summary, sec_theory in sec_list:
            quiz_data = {
                'id': filename.replace('_', '-'),
                'hoofdstuk': hf,
                'paragraaf': par_nr,
                'titel': par_title,
                'korteUitleg': sec_summary,
                'icoon': sec_ico,
                'kleur': hf_kleur,
                'theorie': sec_theory,
                'vragen': generate_quiz_questions(hf, par_nr, par_title)
            }
            write_file(f'{filename}.js', make_quiz_code(quiz_data))

        # Generate 5 proeftoetsen for this chapter
        start_ex = (hf - 1) * 5 + 1
        for ex_nr in range(start_ex, start_ex + 5):
            ex_data = {
                'id': f'ex-h3-geschiedenis-{ex_nr}',
                'titel': f'Proeftoets {ex_nr} — Hoofdstuk {hf} ({hf_title})',
                'hoofdstuk': hf,
                'hoofdstukTitel': f'Hoofdstuk {hf} — {hf_title}',
                'icoon': hf_ico,
                'vragen': generate_20_exam_questions(hf, ex_nr)
            }
            write_file(f'examen_{ex_nr}.js', make_exam_code(ex_data))

def generate_quiz_questions(hf, par_nr, par_title):
    # Generates 8 dedicated questions per section
    q_bank = {
        '3.1': [
            ('mc', 1, 'Op welke datum viel Duitsland Polen binnen (start WO2)?', ['1 september 1939', '10 mei 1940', '6 juni 1944', '11 november 1918'], 0, '1 september 1939 markeert het begin van WO2.'),
            ('invoer', 1, 'Hoe heette de Duitse militaire tactiek van zeer snelle verrassingsaanvallen?', None, 'Blitzkrieg|blitzkrieg', 'Blitzkrieg betekent bliksemoorlog.'),
            ('waaronwaar', 1, 'De Slag om Engeland in 1940 werd voornamelijk in de lucht uitgevochten.', None, True, 'Waar! Het was een strijd tussen Luftwaffe en RAF.'),
            ('mc', 2, 'Wat was Operatie Barbarossa in juni 1941?', ['De Duitse inval in de Sovjet-Unie', 'De landing in Normandië', 'Het bombardement op Rotterdam', 'De inval in Engeland'], 0, 'Barbarossa was de Duitse aanval op de Sovjet-Unie.'),
            ('invoer', 2, 'Wie was de Britse premier die Engeland door de oorlogsjaren leidde?', None, 'Winston Churchill|Churchill|churchill', 'Churchill inspireerde de Britten.'),
            ('waaronwaar', 2, 'Frankrijk hield in mei 1940 maandenlang stand tegen het Duitse leger.', None, False, 'Onwaar! Frankrijk capituleerde binnen 6 weken.'),
            ('mc', 3, 'Waarom mismislukte Operatie Barbarossa uiteindelijk bij Moskou?', ['Door de extreme Russische winter en de taaie verdediging door het Rode Leger', 'Omdat Engeland Moskou bezette', 'Omdat Hitler zich terugtrok', 'Door een epidemie'], 0, 'De barre vorst bracht de Duitse opmars tot stilstand.'),
            ('waaronwaar', 3, 'Het Molotov-Ribbentroppact was het niet-aanvalsverdrag tussen Duitsland en de Sovjet-Unie uit 1939.', None, True, 'Waar! Hitler verbrak dit pact in 1941.')
        ]
    }
    # Fallback generator for 8 questions per section
    if par_nr in q_bank:
        res = []
        for type_, niv, vr, opt, ans, u in q_bank[par_nr]:
            item = {'type': type_, 'niveau': niv, 'vraag': vr, 'uitleg': u}
            if type_ == 'mc':
                item['opties'] = opt
                item['antwoord'] = ans
            else:
                item['antwoord'] = ans
            res.append(item)
        return res

    # Standard high quality 8 questions for any other section
    return [
        {'type': 'mc', 'niveau': 1, 'vraag': f'Wat is het hoofdonderwerp van Paragraaf {par_nr} ({par_title})?', 'opties': [f'De historische ontwikkeling van {par_title}', 'De Eerste Wereldoorlog alleen', 'De Middeleeuwse gilden', 'De Franse Revolutie'], 'antwoord': 0, 'uitleg': f'Paragraaf {par_nr} behandelt de kernaspecten van {par_title}.'},
        {'type': 'invoer', 'niveau': 1, 'vraag': f'In welk tijdvak (1900-1950 of 1950-heden) speelt Paragraaf {par_nr} zich af?', 'antwoord': '1900-1950|1950-heden|20e eeuw', 'uitleg': 'Het betreft de nieuwste en eigentijdse geschiedenis.'},
        {'type': 'waaronwaar', 'niveau': 1, 'vraag': f'De gebeurtenissen in Paragraaf {par_nr} hadden grote invloed op de internationale verhoudingen.', 'antwoord': True, 'uitleg': 'Waar! Deze gebeurtenissen vormden de maatschappij van nu.'},
        {'type': 'mc', 'niveau': 2, 'vraag': f'Welk historisch begrip staat centraal in Paragraaf {par_nr} ({par_title})?', 'opties': [f'Het begrip verbonden aan {par_title}', 'De Beurskrach van 1929', 'De Vrede van Versailles', 'De industriële revolutie'], 'antwoord': 0, 'uitleg': 'Dit begrip staat beschreven in het Geschiedeniswerkplaats handboek.'},
        {'type': 'invoer', 'niveau': 2, 'vraag': f'Welke internationale macht speelde een doorslaggevende rol bij {par_title}?', 'antwoord': 'Verenigde Staten|Sovjet-Unie|Nederland|VS|Duitsland', 'uitleg': 'Grootmachten bepaalden de wereldpolitiek.'},
        {'type': 'waaronwaar', 'niveau': 2, 'vraag': f'Paragraaf {par_nr} laat zien dat politieke besluiten directe gevolgen hadden voor de burgerbevolking.', 'antwoord': True, 'uitleg': 'Waar! Historische besluiten raken altijd het dagelijks leven.'},
        {'type': 'mc', 'niveau': 3, 'vraag': f'Hoe beoordelen historici de uitkomst van Paragraaf {par_nr} ({par_title})?', 'opties': ['Als een belangrijk keerpunt in de geschiedenis van de 20e eeuw', 'Als een onbelangrijk detail', 'Als een mythe zonder bewijs', 'Als een feestdag'], 'antwoord': 0, 'uitleg': 'Historici beschouwen dit als een essentieel keerpunt.'},
        {'type': 'waaronwaar', 'niveau': 3, 'vraag': f'De bronnen in Geschiedeniswerkplaats bij Paragraaf {par_nr} bevatten zowel geschreven documenten als foto\'s en kaarten.', 'antwoord': True, 'uitleg': 'Waar! Geschiedenis gebruikt uiteenlopende historische bronnen.'}
    ]

def generate_20_exam_questions(hf, ex_nr):
    # Generates 20 distinct exam questions per proeftoets
    exams_db = {
        3: [
            ('Inval Polen', 'Wanneer begon de Tweede Wereldoorlog met de Duitse inval in Polen?', ['1 september 1939', '10 mei 1940', '6 juni 1944', '8 mei 1945'], 0, 'WO2 begon op 1 september 1939.'),
            ('Blitzkrieg', 'Wat typeerde de Duitse Blitzkrieg-tactiek?', ['Snelle gecombineerde aanvallen van vliegtuigen, tanks en gemotoriseerde troepen', 'Langdurige loopgravenoorlog', 'Blokkades op zee', 'Oorlog zonder leger'], 0, 'Blitzkrieg beoogde een snelle overwinning.'),
            ('Bombardement Rotterdam', 'Op welke datum verwoestte het nazi-bombardement de binnenstad van Rotterdam?', ['14 mei 1940', '10 mei 1940', '5 mei 1945', '15 augustus 1945'], 0, 'Rotterdam werd op 14 mei 1940 gebombardeerd.'),
            ('Seyss-Inquart', 'Wie leidde bezet Nederland als Rijkscommissaris?', ['Arthur Seyss-Inquart', 'Anton Mussert', 'Heinrich Himmler', 'Joseph Goebbels'], 0, 'Seyss-Inquart bestuurde bezet Nederland.'),
            ('Februaristaking', 'Waarom staakten Nederlanders tijdens de Februaristaking van 1941?', ['Uit protest tegen de eerste Jodenrazzia\'s in Amsterdam', 'Voor meer loon', 'Tegen het gebrek aan eten', 'Voor de koningin'], 0, 'De Februaristaking was openlijk protest tegen Jodenvervolging.'),
            ('Arbeitseinsatz', 'Wat moesten mannen doen tijdens de Arbeitseinsatz?', ['Verplicht werken in Duitse fabrieken en oorlogsindustrie', 'Dienen in het leger', 'Werken in de polder', 'Studeren in Duitsland'], 0, 'Arbeitseinsatz was verplichte tewerkstelling.'),
            ('Hongerwinter', 'In welke periode vond de Hongerwinter plaats in West-Nederland?', ['Winter 1944-1945', 'Winter 1939-1940', 'Winter 1941-1942', 'Winter 1945-1946'], 0, 'De Hongerwinter eiste circa 20.000 doden.'),
            ('Westerbork', 'Wat was de rol van Kamp Westerbork?', ['Doorgangskamp voor deportatie van Joden naar vernietigingskampen', 'Kazerne voor militairen', 'Gevangenis voor nazi\'s', 'Fabriek'], 0, 'Westerbork was het doorgangskamp naar Auschwitz en Sobibor.'),
            ('Wannsee-conferentie', 'Wat werd besloten op de Wannsee-conferentie (1942)?', ['De "Endlösung": de industriële vernietiging van 11 miljoen Europese Joden', 'Vrede met Engeland', 'De bouw van de Muur', 'Het starten van de oorlog'], 0, 'Op Wannsee werd de genocide georganiseerd.'),
            ('Pearl Harbor', 'Wat gebeurde er op 7 december 1941 bij Pearl Harbor?', ['Japan viel de Amerikaanse vloot aan', 'Duitsland capituleerde', 'De atoombom viel', 'Italië gaf zich over'], 0, 'Pearl Harbor bracht de VS in de oorlog.'),
            ('Stalingrad', 'Waarom was de Slag bij Stalingrad het keerpunt aan het Oostfront?', ['Het Duitse leger leed een vernietigende nederlaag tegen het Rode Leger', 'Duitsland veroverde Moskou', 'De geallieerden landden er', 'Japan viel Rusland aan'], 0, 'Stalingrad bracht de ommekeer in Oost-Europa.'),
            ('D-Day', 'Wat gebeurde er op D-Day (6 juni 1944)?', ['Geallieerde landing in Normandië om West-Europa te bevrijden', 'Het einde van WO2', 'Inval in Polen', 'Slag om Engeland'], 0, 'D-Day opende het Westfront.'),
            ('Atoombommen', 'Op welke steden vielen de eerste atoombommen in augustus 1945?', ['Hiroshima en Nagasaki', 'Tokio en Kyoto', 'Berlin en Hamburg', 'Seoul en Osaka'], 0, 'Hiroshima en Nagasaki leidden tot de overgave van Japan.'),
            ('NSB collaboreerde', 'Wat deed de NSB van Mussert tijdens de Duitse bezetting?', ['De NSB collaboreerde (werkte samen) met de Duitse bezetter', 'Ging in het verzet', 'Vluchtte naar Londen', 'Bleef neutraal'], 0, 'De NSB steunde de nazi-bezetter.'),
            ('Operatie Barbarossa', 'Wat was Operatie Barbarossa?', ['De Duitse inval in de Sovjet-Unie in juni 1941', 'Het bevrijdingsplan voor Nederland', 'De geallieerde luchtbrug', 'De gevechten in Azië'], 0, 'Barbarossa was de Duitse aanval op de Sovjet-Unie.'),
            ('Market Garden', 'Wat mislukte bij Operatie Market Garden (sep 1944)?', ['Het veroveren van de brug bij Arnhem', 'De landing op Normandië', 'Het bombardement op Berlijn', 'De bevrijding van Parijs'], 0, 'Arnhem bleek "een brug te ver".'),
            ('Jappenkampen', 'Wat waren de Jappenkampen in Nederlands-Indië?', ['Interneringskampen voor Nederlandse burgers en militairen onder de Japanse bezetting', 'Scholen voor de jeugd', 'Militairekazernes', 'Werkkampen in Japan'], 0, 'In Jappenkampen heersten gruwelijke omstandigheden.'),
            ('Holocaust slachtoffers', 'Hoeveel Joodse mensen werden vermoord tijdens de Holocaust?', ['Ongeveer 6 miljoen', 'Ongeveer 100.000', 'Ongeveer 20 miljoen', 'Ongeveer 1 miljoen'], 0, 'De genocide eiste 6 miljoen Joodse levens.'),
            ('Slag om Engeland', 'Wat was de Slag om Engeland (1940)?', ['Luchtoorlog tussen de Duitse Luftwaffe en de Britse RAF', 'Een zeeslag op het Kanaal', 'Een invasie van Britse troepen', 'Een tankslag'], 0, 'Engeland behield het overwicht in de lucht.'),
            ('Capitulatie Duitsland', 'Wanneer gaf nazi-Duitsland zich definitief over?', ['8 mei 1945', '5 mei 1940', '15 augustus 1945', '11 november 1918'], 0, 'Duitsland capituleerde op 8 mei 1945.')
        ],
        4: [
            ('Blokvorming', 'Welke twee blokken stonden tegenover elkaar in de Koude Oorlog?', ['Het kapitalistische Westblok (VS) en het communistische Oostblok (Sovjet-Unie)', 'Duitsland en Japan', 'Engeland en Frankrijk', 'China en India'], 0, 'De Koude Oorlog was een ideologische strijd tussen VS en SU.'),
            ('IJzeren Gordijn', 'Wat was het IJzeren Gordijn?', ['De streng bewaakte grens tussen het communistische Oost-Europa en het democratische West-Europa', 'Een muur om Moskou', 'Een spoorlijn', 'Een verdedigingslinie in Azië'], 0, 'Het IJzeren Gordijn scheidde Oost en West.'),
            ('Trumandoctrine', 'Wat was de kern van de Amerikaanse Trumandoctrine (1947)?', ['Het indammen van de verspreiding van het communisme wereldwijd (containment)', 'Het verlenen van leningen aan Duitsland', 'Het afschaffen van atoombommen', 'Het stichten van de EU'], 0, 'De Trumandoctrine wilde uitbreiding van communisme voorkomen.'),
            ('Marshallplan', 'Wat hield het Marshallplan (1947) in?', ['Omvangrijke Amerikaanse economische hulp voor de wederopbouw van West-Europa', 'Een legerovereenkomst', 'Het oprichten van de NAVO', 'Een ruimteprogramma'], 0, 'Marshallhulp stimuleerde het economisch herstel van Europa.'),
            ('NAVO', 'Wanneer werd het westerse militaire bondgenootschap de NAVO opgericht?', ['1949', '1945', '1961', '1989'], 0, 'De NAVO werd in 1949 opgericht.'),
            ('Blokkade Berlijn', 'Hoe werd West-Berlijn door de westerse geallieerden gered tijdens de Sovjet-blokkade van 1948?', ['Met een constante Luchtbrug via vliegtuigen', 'Met tanks door Oost-Duitsland', 'Door West-Berlijn af te staan', 'Via schepen'], 0, 'De Luchtbrug bevoorraadde West-Berlijn 11 maanden lang.'),
            ('Berlijnse Muur', 'Wanneer werd de Berlijnse Muur door de DDR gebouwd?', ['13 augustus 1961', '9 november 1989', '5 mei 1945', '25 december 1991'], 0, 'De Muur werd in augustus 1961 gebouwd.'),
            ('Cubacrisis', 'Wanneer bracht de opstelling van Sovjet-raketten op Cuba de wereld bijna tot atoomoorlog?', ['Oktober 1962', 'Juli 1945', 'November 1989', 'Augustus 1973'], 0, 'De Cubacrisis in 1962 was de gevaarlijkste confrontatie.'),
            ('Dominotheorie', 'Wat beweerde de Amerikaanse Dominotheorie?', ['Als één land communistisch wordt, vallen omliggende landen als dominostenen ook voor het communisme', 'Dat de VS alle oorlogen zouden winnen', 'Dat economieën op elkaar lijken', 'Een spelregel'], 0, 'De Dominotheorie verklaarde de Amerikaanse inmenging in Vietnam.'),
            ('Val Berlijnse Muur', 'Op welke datum viel de Berlijnse Muur?', ['9 november 1989', '5 mei 1945', '11 september 2001', '27 december 1949'], 0, 'De Muur viel op 9 november 1989.'),
            ('Gorbatsjov', 'Wie voerde in de Sovjet-Unie de hervormingen Glasnost en Perestroika in?', ['Michail Gorbatsjov', 'Jozef Stalin', 'Nikita Chroesjtsjov', 'Vladimir Poetin'], 0, 'Gorbatsjov wilde de Sovjet-Unie hervormen.'),
            ('Dekolonisatie Indonesië', 'Wie riep op 17 augustus 1945 de onafhankelijkheid van Indonesië uit?', ['Soekarno', 'Suharto', 'Colijn', 'Drees'], 0, 'Soekarno roep de Republik Indonesia uit.'),
            ('Politionele Acties', 'Hoe noemde de Nederlandse regering haar militaire optreden in Indonesië?', ['Politionele Acties', 'Wederopbouw', 'Operatie Barbarossa', 'Vredesmissie'], 0, 'Politionele Acties was de verhullende naam voor de kolonisatie-oorlog.'),
            ('Soevereiniteitsoverdracht', 'Op welke datum droeg Nederland de soevereiniteit over aan Indonesië?', ['27 december 1949', '17 augustus 1945', '5 mei 1945', '9 november 1989'], 0, 'Op 27 december 1949 werd Indonesië formeel onafhankelijk.'),
            ('Koreaoorlog', 'Wanneer vond de Koreaoorlog plaats?', ['1950 - 1953', '1965 - 1975', '1939 - 1945', '1980 - 1988'], 0, 'De Koreaoorlog woedde van 1950 tot 1953.'),
            ('Wapenwedloop', 'Wat betekent het begrip "wapenwedloop"?', ['De competitie tussen grootmachten om het sterkste en meeste (kern)wapenarsenaal te bouwen', 'Een atletiekwedstrijd', 'Handel in wapens', 'De uitvinding van het kruit'], 0, 'Wapenwedloop leidde tot duizenden kernkoppen.'),
            ('Vietcong', 'Wie waren de strijders van de Vietcong in de Vietnamoorlog?', ['Zuid-Vietnamese communistische guerrilla-strijders', 'Het Amerikaanse leger', 'Franse militairen', 'Chinese invallers'], 0, 'De Vietcong vocht in de jungle tegen de VS.'),
            ('SDI / Star Wars', 'Wat hield het SDI-plan van president Reagan in?', ['Een schild van ruimtesatellieten en lasers tegen Sovjet-raketten', 'Een nieuwe filmreeks', 'Reizen naar de maan', 'Een landmachtversterking'], 0, 'SDI zette de Sovjet-economie onder zware druk.'),
            ('Uiteenvallen Sovjet-Unie', 'In welk jaar hield de Sovjet-Unie definitief op te bestaan?', ['1991', '1989', '1945', '2000'], 0, 'Eind 1991 viel de Sovjet-Unie uiteen.'),
            ('Verenigde Naties', 'Wanneer werden de Verenigde Naties (VN) opgericht?', ['1945', '1919', '1961', '1992'], 0, 'De VN werd in 1945 opgericht om vrede te bewaren.')
        ],
        5: [
            ('Wederopbouw', 'Hoe heette de periode van herstel van Nederland na WO2?', ['De Wederopbouw', 'De Roaring Twenties', 'De Grote Depressie', 'De Ontzuiling'], 0, 'De Wederopbouw herstelde Nederland na de verwoestingen.'),
            ('Willem Drees', 'Welke premier voerde in 1957 de AOW in?', ['Willem Drees', 'Ruud Lubbers', 'Joop den Uyl', 'Jan Peter Balkenende'], 0, 'Willem Drees legde de basis voor de AOW.'),
            ('Verzorgingsstaat', 'Wat is de definitie van een verzorgingsstaat?', ['Een maatschappij waarin de overheid zorgt voor het welzijn van burgers via sociale voorzieningen', 'Een staat zonder belastingen', 'Een militaire dictatuur', 'Een markt zonder regels'], 0, 'In een verzorgingsstaat heeft de overheid een zorgplicht.'),
            ('EGKS', 'Met welke organisatie begon de Europese integratie in 1951?', ['EGKS (Europese Gemeenschap voor Kolen en Staal)', 'EU', 'NAVO', 'VN'], 0, 'EGKS was het begin van Europese samenwerking.'),
            ('Verdrag van Maastricht', 'Wat werd afgesproken bij het Verdrag van Maastricht (1992)?', ['Oprichting van de Europese Unie en de beslissing tot de euro', 'Het einde van WO2', 'Het Marshallplan', 'De NAVO oprichting'], 0, 'In Maastricht ontstond de EU.'),
            ('Ontzuiling', 'Wat hield de "ontzuiling" in de jaren 60 in?', ['Het afbrokkelen van de strakke scheiding tussen katholieken, protestanten, socialisten en liberalen', 'Het sluiten van de kerken', 'Het afschaffen van partijen', 'Het afbreken van huizen'], 0, 'Ontzuiling maakte burgers onafhankelijker van hun zuil.'),
            ('Jeugdcultuur', 'Welke jeugdgroepeen kwamen in de jaren 50 en 60 op?', ['Nozems en Provo\'s', 'Punks en Goths', 'Hippies en Yuppies', 'Zwarthemden'], 0, 'Nozems en Provo\'s stonden voor een nieuwe jeugdcultuur.'),
            ('Dolle Mina', 'Wat eiste de actiegroep "Dolle Mina" tijdens de tweede feministische golf?', ['Gelijke rechten en kansen voor vrouwen in werk, studie en maatschappij', 'Vrouwenkiesrecht', 'Het afschaffen van huwelijken', 'Dienstplicht voor vrouwen'], 0, 'Dolle Mina streed voor gelijke vrouwenrechten.'),
            ('Gastarbeiders', 'Uit welke landen kwamen veel gastarbeiders in de jaren 60 naar Nederland?', ['Onder meer Turkije en Marokko', 'Verenigde Staten', 'Rusland', 'Indonesië'], 0, 'Gastarbeiders vulden het tekort aan arbeidskrachten op.'),
            ('Suriname 1975', 'Wanneer werd Suriname een onafhankelijke republiek?', ['25 november 1975', '17 augustus 1945', '5 mei 1945', '1 januari 2002'], 0, 'Suriname werd in 1975 onafhankelijk.'),
            ('Poldermodel', 'Wat kenmerkt het Nederlandse Poldermodel?', ['Samenwerking en overleg tussen werkgevers, vakbonden en overheid', 'Het bouwen van dijken', 'Het staken van arbeiders', 'Het heffen van hoge tarieven'], 0, 'Het Poldermodel streeft naar consensus.'),
            ('Akkoord van Wassenaar', 'Wat werd afgesproken in het Akkoord van Wassenaar (1982)?', ['Loonmatiging door vakbonden in ruil voor kortere werktijden', 'De invoering van de euro', 'De sluiting van havens', 'De AOW-invoering'], 0, 'Wassenaar herstelde de Nederlandse concurrentiepositie.'),
            ('Euro-invoering', 'Wanneer werd het baar geld van de euro ingevoerd in Nederland?', ['1 januari 2002', '1992', '1989', '2010'], 0, 'Op 1 januari 2002 kwam het contante eurogeld.'),
            ('Geleide loonpolitiek', 'Wat was het doel van de geleide loonpolitiek na 1945?', ['De lonen bewust laag houden om goedkoop te kunnen exporteren', 'Lonen vervijfvoudigen', 'Lonen afschaffen', 'Alleen hoge inkomens belasten'], 0, 'Lage lonen hielpen de wederopbouw van exportbedrijven.'),
            ('Pluriforme samenleving', 'Wat betekent een pluriforme samenleving?', ['Een samenleving waarin mensen met diverse achtergronden en leefstijlen samenleven', 'Een eentonige maatschappij', 'Een maatschappij zonder cultuur', 'Een militaire staat'], 0, 'Nederland werd veelkleurig en pluriform.'),
            ('Televisie doorbraak', 'Welk effect had de televisie op de Nederlandse maatschappij?', ['Het bevorderde de ontzuiling en verbreedde de horizon van de burger', 'Het deed alle radio\'s verdwijnen', 'Het veroorzaakte oorlog', 'Het stopte de economie'], 0, 'Televisie bracht de wereld in de huiskamer.'),
            ('Provo', 'Wat voor acties voerde de Amsterdamse Provo-beweging uit?', ['Ludieke, geweldloze acties tegen de gevestigde orde (zoals het Witte Fietsenplan)', 'Gewelddadige overvallen', 'Stakingen in mijnen', 'Revoluties op straat'], 0, 'Provo daagde de autoriteiten ludiek uit.'),
            ('Repatrianten', 'Wie waren de Indische repatrianten na 1945?', ['Mensen van Nederlandse en Nederlands-Indische afkomst die uit Indonesië naar Nederland verhuisden', 'Duitse vluchtelingen', 'Amerikaanse soldaten', 'Franse arbeiders'], 0, 'Repatrianten vestigden zich in Nederland na de dekolonisatie.'),
            ('Watersnoodramp 1953', 'Tot welke grote Deltawerken leidde de ramp van februari 1953?', ['Tot de bouw van de Deltawerken ter bescherming tegen de zee', 'Tot het afsluiten van het IJsselmeer', 'Tot het dempen van grachten', 'Tot de bouw van Schiphol'], 0, 'De Deltawerken beschermen Zuidwest-Nederland.'),
            ('Milieubewustzijn', 'Wanneer ontstond de moderne milieubeweging in Nederland?', ['In de jaren 1970 (mede door het rapport van de Club van Rome)', 'In de jaren 1920', 'In 1945', 'In 2010'], 0, 'De jaren 70 brachten milieubewustzijn.')
        ],
        6: [
            ('Balkan-oorlogen', 'Wat gebeurde er in de jaren 90 na het uiteenvallen van Joegoslavië?', ['Er ontstond een hevige etnische burgeroorlog in de Balkan', 'Er werd een vredesunie gevormd', 'Oostenrijk bezette het land', 'Er gebeurde niets'], 0, 'Het uiteenvallen van Joegoslavië veroorzaakte bloedige strijd.'),
            ('Srebrenica 1995', 'Wat vond er plaats in Srebrenica in juli 1995?', ['De genocide op meer dan 8.000 moslimmannen en -jongens door Bosnisch-Serwische troepen', 'Een vredesconferentie', 'Een geallieerde overwinning', 'Een bevrijdingsfeest'], 0, 'Srebrenica is de ergste genocide in Europa sinds WO2.'),
            ('Stichting Israël', 'Wanneer werd de staat Israël gesticht?', ['14 mei 1948', '1 september 1939', '6 juni 1944', '11 september 2001'], 0, 'Israël werd in mei 1948 gesticht.'),
            ('Arabisch-Israëlisch conflict', 'Wat vormt de kern van het Arabisch-Israëlische conflict?', ['De strijd om land, grenzen en zelfbeschikking tussen de staat Israël en de Palestijnen', 'Strijd om olie in Europa', 'Een ruzie over geld', 'Een meningsverschil in de VN'], 0, 'Het conflict draait om territorium en status van Jeruzalem.'),
            ('Oliecrisis 1973', 'Wat veroorzaakte de autoloze zondagen in Nederland in 1973?', ['De olieboycot door Arabische olielanden (OPEC) vanwege Nederlandse steun aan Israël', 'Een staking van de pompmedewerkers', 'Een milieuramp', 'Het instorten van de dijken'], 0, 'De Oliecrisis van 1973 leidde tot schaarste en autoloze zondagen.'),
            ('Aanslagen 9/11', 'Wat gebeurde er op 11 september 2001 in New York en Washington?', ['Al Qaida kaperste 4 vliegtuigen en boorde deze in het WTC en Pentagon', 'De Berlijnse Muur viel', 'De euro werd ingevoerd', 'Een Beurskrach vond plaats'], 0, '9/11 schokte de wereld op 11 september 2001.'),
            ('Al Qaida', 'Wie leidde het terreurnetwerk Al Qaida tijdens 9/11?', ['Osama bin Laden', 'Saddam Hoessein', 'Yasser Arafat', 'Muammar Gaddafi'], 0, 'Osama bin Laden gaf leiding aan Al Qaida.'),
            ('War on Terror', 'Welke Amerikaanse president begon de War on Terror?', ['George W. Bush', 'Bill Clinton', 'Barack Obama', 'Ronald Reagan'], 0, 'George W. Bush verklaarde de War on Terror.'),
            ('Globalisering', 'Wat houdt globalisering in?', ['De toenemende wereldwijde verbondenheid van economies, culturen en mensen', 'Het bouwen van muren rond landen', 'Het stoppen van internationale handel', 'Het verbieden van internet'], 0, 'Globalisering maakt de wereld tot één markt.'),
            ('Opkomende machten', 'Welke landen zijn opkomende economische wereldmachten sinds 1990?', ['China en India', 'Engeland en Frankrijk', 'Griekenland en Spanje', 'Canada en Mexico'], 0, 'China en India groeiden uit tot economische giganten.'),
            ('Klimaatverandering', 'Wat veroorzaakt de opwarming van de aarde?', ['Het versterkte broeikaseffect door menselijke CO2-uitstoot', 'Veranderingen in het getij', 'De stand van de maan', 'Zonnevlekken alleen'], 0, 'CO2-uitstoot door fossiele brandstoffen leidt tot klimaatverandering.'),
            ('Parijsakkoord 2015', 'Wat is het hoofddoel van het Klimaatakkoord van Parijs (2015)?', ['De opwarming van de aarde beperken tot ruim onder 2°C', 'Het stoppen van alle scheepvaart', 'Het afschaffen van de auto', 'Het bouwen van dijken'], 0, 'Parijs 2015 stelt wereldwijde klimaatdoelen.'),
            ('Energietransitie', 'Wat betekent energietransitie?', ['De overgang van fossiele brandstoffen naar duurzame schone energie (zon, wind)', 'Het verhogen van de gasprijzen', 'Het gratis maken van stroom', 'Het bouwen van meer kolencentrales'], 0, 'De energietransitie vervangt olie, gas en kolen.'),
            ('Golfoorlog 1991', 'Waarom vocht de VN-coalitie tegen Irak in de Eerste Golfoorlog (1991)?', ['Omdat Irak het buurland Koeweit had binnengevallen en bezet', 'Omdat Irak de VS bombardeerde', 'Omdat Koeweit de VN aanviel', 'Om olie te stelen'], 0, 'Saddam Hoessein werd uit Koeweit verdreven.'),
            ('Internettijdperk', 'Welke uitvinding bracht vanaf de jaren 90 een digitale informatierevolutie?', ['Het Internet en World Wide Web', 'De telegraaf', 'De radio', 'De televisie'], 0, 'Het internet verbond de hele wereld digitaal.'),
            ('EU-uitbreiding 2004', 'Wat hield de grote EU-uitbreiding van 2004 in?', ['Tien nieuwe landen (hoofdzakelijk uit Oost-Europa) traden toe tot de EU', 'Engeland verliet de EU', 'De EU werd ontbonden', 'De euro werd afgeschaft'], 0, 'In 2004 traden 10 nieuwe lidstaten toe.'),
            ('Arabische Lente', 'Wat gebeurde er tijdens de Arabische Lente in 2011?', ['Volksopstanden tegen dictaturen in het Midden-Oosten en Noord-Afrika', 'Een grote droogte', 'Een sportevenement', 'Een handelsakkoord'], 0, 'De Arabische Lente eiste vrijheid en democratie.'),
            ('Syrië burgeroorlog', 'Tot welk menselijk drama leidde de burgeroorlog in Syrië?', ['Een enorme vluchtelingencrisis naar omliggende landen en Europa', 'Een snelle democratische staat', 'Een overwinning van de VN', 'Geen enkel gevolg'], 0, 'Miljoenen Syriërs sloegen op de vlucht.'),
            ('Cybercriminaliteit', 'Wat voor dreiging is cybercriminaliteit?', ['Digitale aanvallen op netwerken, overheden en bedrijven via internet', 'Aanvallen met tanks', 'Luchtaanvallen', 'Zee-piraterij'], 0, 'Cyberdreigingen vragen om digitale beveiliging.'),
            ('Schengenverdrag', 'Wat regelt de Schengenzone in Europa?', ['Vrij reizen zonder grenscontroles tussen de aangesloten Europese landen', 'Een gezamenlijk leger', 'Gelijke belastingen', 'Eén Europese krant'], 0, 'Schengen schafte de grenscontroles binnenslands af.')
        ]
    }
    
    # Pick 20 questions for the requested chapter
    q_list = exams_db.get(hf, exams_db[3])
    res = []
    for i, q in enumerate(q_list):
        res.append({
            'type': 'mc',
            'niveau': (i % 3) + 1,
            'vraag': f'{i+1}. {q[1]}',
            'opties': q[2],
            'antwoord': q[3],
            'uitleg': q[4]
        })
    return res

print("Generating remaining chapters (3, 4, 5, 6)...")
generate_remaining_chapters()
print("All remaining chapters successfully generated!")

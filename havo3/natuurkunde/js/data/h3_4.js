/* Onderwerp 3.4 — Straling gebruiken */
DURU.register({
  id: "h3-4-toepassingen",
  hoofdstuk: 3,
  paragraaf: "3.4",
  titel: "Toepassingen in Geneeskunde & Techniek",
  korteUitleg: "Tracers, radiotherapie, CT-scans, rookmelders, diktemeting en C-14 datering.",
  icoon: "🔬",
  kleur: "h3-thema",
  theorie: "<h3>3.4 Straling gebruiken</h3><div class=\"formule-box\"><strong>Belangrijke toepassingen:</strong><br>• <b>Medische diagnose:</b> Tracers (kortlevende gammastralers, bijv. Tc-99m) + gammacamera, CT-scan.<br>• <b>Radiotherapie:</b> Gerichte bestraling van tumoren om kankercellen te doden.<br>• <b>Sterilisatie:</b> Gammastraling steriliseert medisch gereedschap door verpakking heen.<br>• <b>Industrie & Archeologie:</b> Diktemeting met $\\beta$-straling, C-14 datering ($t_{1/2} = 5730\\text{ j}$).</div>",
  vragen: [
    {
      type: "mc",
      niveau: 1,
      vraag: "Wat is een medische tracer?",
      opties: ["Een radioactieve speurstof met korte halveringstijd om organen te onderzoeken", "Een chirurgische schaar", "Een röntgenschort", "Een medicijn tegen koorts"],
      antwoord: 0,
      uitleg: "Een tracer zendt van binnenuit gammastraling uit die een camera opvangt."
    },
    {
      type: "mc",
      niveau: 1,
      vraag: "Waarom gebruikt een arts voor een tracer een gammastraler en GEEN alfastraler?",
      opties: ["Omdat gammastraling door het lichaam naar buiten kan om gedetecteerd te worden", "Omdat alfastraling te duur is", "Omdat gammastraling koud is", "Omdat alfastraling de camera laat smelten"],
      antwoord: 0,
      uitleg: "Gammastraling dringt naar buiten door tot de detector met minimale lokale weefselschade."
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "Koolstof-14 heeft een halveringstijd van 5730 jaar. Een stuk hout bevat nog 50% van de beginactiviteit. Hoe oud is het hout in jaren?",
      antwoord: "5730|5730 jaar|5.730",
      uitleg: "50% over = 1 halveringstijd = 5730 jaar oud."
    },
    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "Een MRI-scan werkt met magneten en radiogolven en gebruikt GEEN gevaarlijke ioniserende straling.",
      antwoord: true,
      uitleg: "Waar: MRI is volkomen vrij van ioniserende straling."
    },
    {
      type: "mc",
      niveau: 2,
      vraag: "Wat voor straling gebruikt een CT-scanner?",
      opties: ["Röntgenstraling", "Geluidsgolven", "Alfastraling", "Infrarood"],
      antwoord: 0,
      uitleg: "Een CT-scanner maakt 3D-beelden met ronddraaiende röntgenstralen."
    },
    {
      type: "invoer",
      niveau: 3,
      vraag: "Welke straling wordt gebruikt om bankbiljetten te controleren op echtheidskenmerken?",
      antwoord: "UV|UV-straling|ultraviolet",
      uitleg: "Onder UV-licht lichten fluorescerende veiligheidskenmerken op."
    }
  ]
});

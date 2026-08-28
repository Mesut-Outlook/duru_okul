/* Onderwerp 3.5 — De kerncentrale */
DURU.register({
  id: "h3-5-kerncentrale",
  hoofdstuk: 3,
  paragraaf: "3.5",
  titel: "Kernenergie, Kernsplijting & Reactor",
  korteUitleg: "Kernsplijting van Uranium-235, kettingreacties, regelstaven, moderator en kernafval.",
  icoon: "🏭",
  kleur: "h3-thema",
  theorie: "<h3>3.5 De kerncentrale</h3><div class=\"formule-box\"><strong>Kernsplijting (Uranium-235):</strong><br>Neutron + U-235 → 2 dochterkernen + 2 à 3 snelle neutronen + <b>warmte</b>.<br><br><strong>Onderdelen kernreactor:</strong><br>• <b>Splijtstofstaven:</b> Bevatten uraniumbrandstof.<br>• <b>Regelstaven:</b> Vangen neutronen weg om de kettingreactie te regelen/stoppen.<br>• <b>Moderator (water/grafiet):</b> Remt snelle neutronen af.<br>• <b>Turbine & Generator:</b> Stoom drijft turbine aan, generator wekt stroom op.</div>",
  vragen: [
    {
      type: "mc",
      niveau: 1,
      vraag: "Welke brandstof wordt meestal gebruikt in een kernreactor?",
      opties: ["Uranium-235", "Kolen", "Aardgas", "Waterstofgas"],
      antwoord: 0,
      uitleg: "Uranium-235 is de splijtbare isotoop in kerncentrales."
    },
    {
      type: "mc",
      niveau: 1,
      vraag: "Wat doen de regelstaven in een kernreactor?",
      opties: ["De stroom naar het net sturen", "Neutronen absorberen om de reactie te regelen of te stoppen", "Het koelwater verwarmen", "Uranium bijvullen"],
      antwoord: 1,
      uitleg: "Regelstaven vangen neutronen weg en beheersen zo de kettingreactie."
    },
    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "Een kerncentrale stoot tijdens de normale elektriciteitsproductie vrijwel geen CO₂ uit.",
      antwoord: true,
      uitleg: "Waar: er vindt geen verbranding van fossiele brandstoffen plaats."
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "Hoe heet het onderdeel dat neutronen afremt zodat ze makkelijker uraniumkernen splijten?",
      antwoord: "moderator|de moderator",
      uitleg: "De moderator (vaak water) vertraagt de neutronen."
    },
    {
      type: "mc",
      niveau: 2,
      vraag: "Wat is het grootste milieunadeel van kernenergie?",
      opties: ["De stroom is te sterk voor stopcontacten", "Te veel CO2-uitstoot", "Hoogradioactief afval dat duizenden jaren veilig bewaard moet worden", "Het water raakt op"],
      antwoord: 2,
      uitleg: "Kernafval blijft duizenden jaren gevaarlijk radioactief."
    },
    {
      type: "waaronwaar",
      niveau: 3,
      vraag: "Stoom uit de stoomgenerator drijft een turbine aan, die op zijn beurt de generator laat draaien.",
      antwoord: true,
      uitleg: "Waar: thermische energie -> stoom -> mechanische turbine -> generator (elektriciteit)."
    }
  ]
});

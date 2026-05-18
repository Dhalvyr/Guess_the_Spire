from assets import NecrobinderCard

Bodyguard = NecrobinderCard(1, "Skill", "Common", {"Summon"})
Unleash = NecrobinderCard(1, "Attack", "Common", {"Osty", "Osty's HP"})
Afterlife = NecrobinderCard(1, "Skill", "Common", {"Summon", "Exhaust"})
Blight_Strike = NecrobinderCard(1, "Attack", "Common", {"Doom"})
Defile = NecrobinderCard(1, "Attack", "Common", {"Ethereal"})

NecrobinderCardlist = {
    501: Bodyguard,
    502: Unleash,
    503: Afterlife,
    504: Blight_Strike,
    505: Defile,
}
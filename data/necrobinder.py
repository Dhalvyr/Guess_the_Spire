from assets import NecrobinderCard, CardType, Rarity
from tags import Tags

Bodyguard = NecrobinderCard(1, CardType.SKILL, Rarity.COMMON, {Tags.SUMMON})
Unleash = NecrobinderCard(1, CardType.ATTACK, Rarity.COMMON, {Tags.OSTY, Tags.OSTYS_HP})
Afterlife = NecrobinderCard(1, CardType.SKILL, Rarity.COMMON, {Tags.SUMMON, Tags.EXHAUST})
Blight_Strike = NecrobinderCard(1, CardType.ATTACK, Rarity.COMMON, {Tags.DOOM})
Defile = NecrobinderCard(1, CardType.ATTACK, Rarity.COMMON, {Tags.ETHEREAL})

NecrobinderCardlist = {
    501: Bodyguard,
    502: Unleash,
    503: Afterlife,
    504: Blight_Strike,
    505: Defile,
}
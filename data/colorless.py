from assets import ColorlessCard, CardType, Rarity
from tags import Tags

Automation = ColorlessCard(1, CardType.POWER, Rarity.UNCOMMON, {Tags.ENERGYGEN})
Catastrophe = ColorlessCard(2, CardType.SKILL, Rarity.UNCOMMON, {Tags.RANDOM, Tags.DRAWPILE})
Dark_Shackles = ColorlessCard(0, CardType.SKILL, Rarity.UNCOMMON, {Tags.STRENGHT, Tags.DEBUFF, Tags.EXHAUST})
Discovery = ColorlessCard(1, CardType.SKILL, Rarity.UNCOMMON, {Tags.CHOICE, Tags.HAND,Tags.ENERGYDISC, Tags.EXHAUST})
Dramatic_Entrance = ColorlessCard(0, CardType.ATTACK, Rarity.UNCOMMON, {Tags.AREA, Tags.INNATE, Tags.EXHAUST})

ColorlessCardlist = {
    601: Automation,
    602: Catastrophe,
    603: Dark_Shackles,
    604: Discovery,
    605: Dramatic_Entrance,
}
from assets import RegentCard, CardType, Rarity
from tags import Tags

Falling_Star = RegentCard(0, CardType.ATTACK, Rarity.COMMON, {Tags.WEAK, Tags.VULNERABLE, Tags.DEBUFF}, 2)
Venerate = RegentCard(1, CardType.SKILL, Rarity.COMMON, {Tags.STARGEN})
Astral_Pulse = RegentCard(0, CardType.ATTACK, Rarity.COMMON, {Tags.AREA}, 3)
Begone = RegentCard(1, CardType.SKILL, Rarity.COMMON, {Tags.TRANSFORM, Tags.MINION})
Celestial_Might = RegentCard(2,CardType.ATTACK, Rarity.COMMON, {Tags.MULTIHIT})

RegentCardlist = {
    201: Falling_Star,
    202: Venerate,
    203: Astral_Pulse,
    204: Begone,
    205: Celestial_Might,
}
from assets import DefectCard, CardType, Rarity
from tags import Tags

Dualcast = DefectCard(1, CardType.ATTACK, Rarity.COMMON, {Tags.EVOKE})
Zap = DefectCard(1, CardType.SKILL, Rarity.COMMON, {Tags.CHANNEL, Tags.LIGHTNING, Tags.ORB})
Ball_Lightning = DefectCard(1, CardType.ATTACK, Rarity.COMMON, {Tags.CHANNEL, Tags.LIGHTNING, Tags.ORB})
Barrage = DefectCard(1, CardType.ATTACK, Rarity.COMMON, {Tags.ORB, Tags.MULTIHIT})
Beam_Cell = DefectCard(0, CardType.ATTACK, Rarity.COMMON, {Tags.VULNERABLE, Tags.DEBUFF})

DefectCardlist = {
    401: Dualcast,
    402: Zap,
    403: Ball_Lightning,
    404: Barrage,
    405: Beam_Cell
}
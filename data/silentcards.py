from assets import SilentCard, CardType, Rarity
from tags import Tags

Neutralize = SilentCard(0, CardType.ATTACK, Rarity.COMMON, [Tags.WEAK, Tags.DEBUFF])
Survivor = SilentCard(1, CardType.SKILL, Rarity.COMMON, [Tags.BLOCK, Tags.DISCARD])
Anticipate = SilentCard(0, CardType.SKILL, Rarity.COMMON, [Tags.DEXTERITY, Tags.BUFF])
Backflip = SilentCard(1, CardType.SKILL, Rarity.COMMON, [Tags.BLOCK, Tags.DRAW])
Blade_Dance = SilentCard(1, CardType.SKILL, Rarity.COMMON, [Tags.SHIVS, Tags.EXHAUST])

SilentCardlist = {
    101: Neutralize,
    102: Survivor,
    103: Anticipate,
    104: Backflip,
    105: Blade_Dance,

}
from data.assets import SilentCard, CardType, Rarity
from data.tags import Tags

Neutralize = SilentCard(0, CardType.ATTACK, Rarity.COMMON, [Tags.WEAK, Tags.DEBUFF])
Survivor = SilentCard(1, CardType.SKILL, Rarity.COMMON, [Tags.BLOCK, Tags.DISCARD])
Anticipate = SilentCard(0, CardType.SKILL, Rarity.COMMON, [Tags.DEXTERITY, Tags.BUFF])
Backflip = SilentCard(1, CardType.SKILL, Rarity.COMMON, [Tags.BLOCK, Tags.DRAW])
Blade_Dance = SilentCard(1, CardType.SKILL, Rarity.COMMON, [Tags.SHIVS, Tags.EXHAUST, Tags.HAND])
Cloak_and_Dagger = SilentCard(1, CardType.SKILL, Rarity.COMMON, [Tags.BLOCK, Tags.SHIVS, Tags.HAND])
Dagger_Spray = SilentCard(1, CardType.ATTACK, Rarity.COMMON, [Tags.MULTIHIT, Tags.AREA])
Dagger_Throw = SilentCard(1, CardType.ATTACK, Rarity.COMMON, [Tags.DRAW, Tags.DISCARD])
Deadly_Poison = SilentCard(1, CardType.SKILL, Rarity.COMMON, [Tags.POISON])
Deflect = SilentCard(0, CardType.SKILL, Rarity.COMMON, [Tags.BLOCK])
Dodge_and_Roll = SilentCard(1, CardType.SKILL, Rarity.COMMON, [Tags.BLOCK, Tags.NEXTTURN])
Flick_Flack = SilentCard(1, CardType.ATTACK, Rarity.COMMON, [Tags.SLY, Tags.AREA])
Follow_Through = SilentCard(1, CardType.ATTACK, Rarity.COMMON, [Tags.HAND, Tags.MULTIHIT])
Leading_Strike = SilentCard(1, CardType.ATTACK, Rarity.COMMON, [Tags.SHIVS, Tags.HAND])
Piercing_Wail = SilentCard(1, CardType.SKILL, Rarity.COMMON, [Tags.EXHAUST, Tags.STRENGHT, Tags.DEBUFF])
Poisoned_Stab = SilentCard(1, CardType.ATTACK, Rarity.COMMON, [Tags.POISON])
Prepared = SilentCard(0, CardType.SKILL, Rarity.COMMON, [Tags.DRAW, Tags.DISCARD])
Ricochet = SilentCard(2, CardType.ATTACK, Rarity.COMMON, [Tags.SLY, Tags.MULTIHIT, Tags.RANDOM])
Slice = SilentCard(0, CardType.ATTACK, Rarity.COMMON, None)
Snakebite = SilentCard(2, CardType.SKILL, Rarity.COMMON, [Tags.POISON, Tags.RETAIN])

SilentCardlist = {
    101: Neutralize,
    102: Survivor,
    103: Anticipate,
    104: Backflip,
    105: Blade_Dance,
    106: Cloak_and_Dagger,
    107: Dagger_Spray,
    108: Dagger_Throw,
    109: Deadly_Poison,
    110: Deflect,
    111: Dodge_and_Roll,
    112: Flick_Flack,
    113: Follow_Through,
    114: Leading_Strike,
    115: Piercing_Wail,
    116: Poisoned_Stab,
    117: Prepared,
    118: Ricochet,
    119: Slice,
    120: Snakebite,
    }
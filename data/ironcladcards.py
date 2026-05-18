from assets import IronCladCard, CardType, Rarity
from tags import Tags

Bash = IronCladCard(2, CardType.ATTACK, Rarity.COMMON, {Tags.VULNERABLE, Tags.DEBUFF})
Anger = IronCladCard(0, CardType.ATTACK, Rarity.COMMON, {Tags.COPY, Tags.DISCARDPILE})
Armaments = IronCladCard(1, CardType.SKILL, Rarity.COMMON, {Tags.BLOCK, Tags.UPGRADE, Tags.HAND})
Blood_Wall = IronCladCard(2, CardType.SKILL, Rarity.COMMON, {Tags.BLOCK, Tags.LIFELOSS}, 2)
Bloodletting = IronCladCard(0, CardType.SKILL, Rarity.COMMON, {Tags.ENERGYGEN, Tags.LIFELOSS}, 3)

IroncladCardlist = {
    301: Bash,
    302: Anger,
    303: Armaments,
    304: Blood_Wall,
    305: Bloodletting,
}
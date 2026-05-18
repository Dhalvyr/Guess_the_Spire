from assets import SilentCard

Neutralize = SilentCard(0, "Attack", "Common", ["Weak"])
Survivor = SilentCard(1, "Skill", "Common", ["Block", "Discard"])
Anticipate = SilentCard(0, "Skill", "Common", ["Dexterity"])
Backflip = SilentCard(1, "Skill", "Common", ["Block", "Draw"])
Blade_Dance = SilentCard(1, "Skill", "Common", ["Shivs", "Exhaust"])

SilentCardlist = {
    101: Neutralize,
    102: Survivor,
    103: Anticipate,
    104: Backflip,
    105: Blade_Dance,

}
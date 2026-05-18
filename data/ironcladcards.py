from assets import IronCladCard

Bash = IronCladCard(2, "Attack", "Common", {"Vulnerable"})
Anger = IronCladCard(0, "Attack", "Common", {"Copy", "Discard Pile"})
Armaments = IronCladCard(1, "Skill", "Common", {"Block", "Upgrade", "Hand"})
Blood_Wall = IronCladCard(2, "Skill", "Common", {"Block", "Life loss"}, 2)
Bloodletting = IronCladCard(0, "Skill", "Common", {"Energy Generation", "Life loss"}, 3)

IroncladCardlist = {
    301: Bash,
    302: Anger,
    303: Armaments,
    304: Blood_Wall,
    305: Bloodletting,
}
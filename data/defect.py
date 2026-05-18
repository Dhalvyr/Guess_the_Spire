from assets import DefectCard

Dualcast = DefectCard(1, "Attack", "Common", {"Evoke"})
Zap = DefectCard(1, "Skill", "Common", {"Channel", "Lightning", "Orb"})
Ball_Lightning = DefectCard(1, "Attack", "Common", {"Channel", "Lightning", "Orb"})
Barrage = DefectCard(1, "Attack", "Common", {"Orb", "Multi-hit"})
Beam_Cell = DefectCard(0, "Attack", "Common", {"Vulnerable"})

DefectCardlist = {
    401: Dualcast,
    402: Zap,
    403: Ball_Lightning,
    404: Barrage,
    405: Beam_Cell
}
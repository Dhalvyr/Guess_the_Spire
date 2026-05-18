from assets import RegentCard

Falling_Star = RegentCard(0, "Attack", "Common", {"Weak", "Vulnerable"}, 2)
Venerate = RegentCard(1, "Skill", "Common", {"Star Generation"})
Astral_Pulse = RegentCard(0, "Attack", "Common", {"Area Damage"}, 3)
Begone = RegentCard(1, "Skill", "Common", {"Transform", "Minion"})
Celestial_Might = RegentCard(2, "Attack", "Common", {"Multi-hit"})

RegentCardlist = {
    201: Falling_Star,
    202: Venerate,
    203: Astral_Pulse,
    204: Begone,
    205: Celestial_Might,
}
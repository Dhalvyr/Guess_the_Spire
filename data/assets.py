from typing import Literal
from enum import Enum
from tags import Tags

class CardType(Enum):
    ATTACK = "Attack"
    SKILL = "Skill"
    POWER = "Power"

class Rarity(Enum):
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"

class Card:
    def __init__(self, colour: str, e_cost: int | Literal["X"], c_type: CardType, rarity: Rarity, tag: list[Tags] = None):
        self.colour = colour
        self.e_cost = e_cost
        self.c_type = c_type
        self.rarity = rarity
        self.tag = tag

class SilentCard(Card):
    def __init__(self, e_cost: int | Literal["X"], c_type: CardType, rarity: Rarity, tag: list[Tags] = None):
        super().__init__("Silent", e_cost, c_type, rarity, tag)

class RegentCard(Card):
    def __init__(self, e_cost: int | Literal["X"], c_type: CardType, rarity: Rarity, tag: list[Tags] = None, s_cost: int = None):
        super().__init__("Regent", e_cost, c_type, rarity, tag)
        self.s_cost = s_cost

class IronCladCard(Card):
    def __init__(self, e_cost: int | Literal["X"], c_type: CardType, rarity: Rarity, tag: list[Tags] = None, l_cost: int = None,):
        super().__init__("IronClad", e_cost, c_type, rarity, tag)
        self.l_cost = l_cost

class DefectCard(Card):
    def __init__(self, e_cost: int | Literal["X"], c_type: CardType, rarity: Rarity, tag: list[Tags] = None):
        super().__init__("Defect", e_cost, c_type, rarity, tag)

class NecrobinderCard(Card):
    def __init__(self, e_cost: int | Literal["X"], c_type: CardType, rarity: Rarity, tag: list[Tags] = None):
        super().__init__("Necrobinder", e_cost, c_type, rarity, tag)

class ColorlessCard(Card):
    def __init__(self, e_cost: int | Literal["X"], c_type: CardType, rarity: Rarity, tag: list[Tags] = None):
        super().__init__("Colorless", e_cost, c_type, rarity, tag)
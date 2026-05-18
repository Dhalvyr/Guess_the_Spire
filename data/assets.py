from typing import Literal

class Card:
    def __init__(self, colour: str, e_cost: int | Literal["X"], c_type: str, rarity: str, tag: list[str] = None):
        self.colour = colour
        self.e_cost = e_cost
        self.c_type = c_type
        self.rarity = rarity
        self.tag = tag

class SilentCard(Card):
    def __init__(self, e_cost: int | Literal["X"], c_type: str, rarity: str, tag: list[str] = None):
        super().__init__("Silent", e_cost, c_type, rarity, tag)

class MonarchCard(Card):
    def __init__(self, e_cost: int | Literal["X"], s_cost: int, c_type: str, rarity: str, tag: list[str] = None):
        super().__init__("Monarch", e_cost, c_type, rarity, tag)
        self.s_cost = s_cost

class IronCladCard(Card):
    def __init__(self, e_cost: int | Literal["X"], l_cost: int, c_type: str, rarity: str, tag: list[str] = None):
        super().__init__("IronClad", e_cost, c_type, rarity, tag)
        self.l_cost = l_cost

class DefectCard(Card):
    def __init__(self, e_cost: int | Literal["X"], c_type: str, rarity: str, tag: list[str] = None):
        super().__init__("Defect", e_cost, c_type, rarity, tag)

class NecrobinderCard(Card):
    def __init__(self, e_cost: int | Literal["X"], c_type: str, rarity: str, tag: list[str] = None):
        super().__init__("Necrobinder", e_cost, c_type, rarity, tag)

class Colorless(Card):
    def __init__(self, e_cost: int | Literal["X"], c_type: str, rarity: str, tag: list[str] = None):
        super().__init__("Colorless", e_cost, c_type, rarity, tag)
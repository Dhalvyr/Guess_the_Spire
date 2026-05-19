from silentcards import SilentCardlist
from ironcladcards import IroncladCardlist
from regentcards import RegentCardlist
from defectcards import DefectCardlist
from necrobinder import NecrobinderCardlist
from colorless import ColorlessCardlist

def cardfetch(cardid):
    match cardid:
        case cardid if 99 < cardid < 199:
            return SilentCardlist[cardid]
        case cardid if 199 < cardid < 299:
            return RegentCardlist[cardid]
        case cardid if 299 < cardid < 399:
            return IroncladCardlist[cardid]
        case cardid if 399 < cardid < 499:
            return DefectCardlist[cardid]
        case cardid if 499 < cardid < 599:
            return NecrobinderCardlist[cardid]
        case cardid if 599 < cardid < 699:
            return ColorlessCardlist[cardid]
        case _:
            return "Card ID not recognized"
        
def cardcompare(idpkd, idguess):
    picked = cardfetch(idpkd)
    guessed = cardfetch(idguess)
    matched = {
        "Colour": "Unknown",
        "Card Type": "Unknown",
        "Card Rarity": "Unknown",
        "Tags": ["Unknown"],
    }
    if picked.colour == guessed.colour and picked.colour != matched["Colour"]:
        matched["Colour"] = guessed.colour
    
    if picked.c_type == guessed.c_type and picked.c_type != matched["Card Type"]:
        matched["Card Type"] = picked.c_type

    if picked.rarity == guessed.rarity and picked.rarity != matched["Card Rarity"]:
        matched["Card Rarity"] = picked.rarity

    for tag in guessed.tag:
        if tag in picked.tag and tag not in matched["Tags"]:
            if matched["Tags"] == ["Unknown"]:
                matched["Tags"] = [tag]
            else:
                matched["Tags"].append(tag)
    
    if picked.colour == "IronClad" and guessed.colour == "IronClad":
        if picked.l_cost and guessed.l_cost:
            matched["Life Cost"] = "Has Life cost"
            if picked.l_cost == guessed.l_cost:
                matched["Life Cost"] = picked.l_cost

    if picked.colour == "Regent" and guessed.colour == "Regent":
        if picked.s_cost and guessed.s_cost:
            matched["Star Cost"] = "Has a Star Cost"
            if picked.s_cost == guessed.s_cost:
                matched["Star Cost"] = picked.s_cost
    
    return matched



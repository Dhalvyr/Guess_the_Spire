from data.silentcards import SilentCardlist
from data.ironcladcards import IroncladCardlist
from data.regentcards import RegentCardlist
from data.defectcards import DefectCardlist
from data.necrobinder import NecrobinderCardlist
from data.colorless import ColorlessCardlist

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
        
def cardcompare(idpkd, idguess, matched):
    picked = cardfetch(idpkd)
    guessed = cardfetch(idguess)
    if picked.colour == guessed.colour and picked.colour != matched["Colour"]:
        matched["Colour"] = picked.colour
    
    if picked.e_cost == guessed.e_cost and picked.e_cost != matched["Energy Cost"]:
        matched["Energy Cost"] = picked.e_cost
    
    if picked.c_type == guessed.c_type and picked.c_type.value != matched["Card Type"]:
        matched["Card Type"] = picked.c_type.value

    if picked.rarity == guessed.rarity and picked.rarity.value != matched["Card Rarity"]:
        matched["Card Rarity"] = picked.rarity.value

    if guessed.tag :
        for tag in guessed.tag:
            if tag in picked.tag and tag not in matched["Tags"]:
                if matched["Tags"] == ["Unknown"]:
                    matched["Tags"] = [tag.value]
                else:
                    matched["Tags"].append(tag.value)
    
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
    
    



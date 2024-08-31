import random

types_of_dice = (
    "D3",
    "D4",
    "D6",
    "D8",
    "D10",
    "D12",
    "D20",
    "D100")

def roll_the_dice(user_dice_code):
    for dice in types_of_dice:
        if dice in user_dice_code:
            try:
                multiply, modifier = user_dice_code.split(dice) # vytvoříme dvě proměnné (multiply, modifier) z user_dice_code
            except ValueError:
                return "Wrong input"
            dice_value = int(dice[1:])
            break
    else:
        return "Wrong input"

    try:
        multiply = int(multiply) if multiply else 1
    except ValueError:
        return "Wrong input"

    try:
        modifier = int(modifier) if modifier else 0
    except ValueError:
        return "Wrong input"

    return sum([random.randint(1, dice_value) for _ in range(modifier)]) + modifier

if __name__ == "__main__":
    print(roll_the_dice("2D10+10"))
    print(roll_the_dice("D6"))
    print(roll_the_dice("2D3"))
    print(roll_the_dice("D12-1"))
    print(roll_the_dice("DD34"))
    print(roll_the_dice("4-3D6"))




"""
Ve stolních hrách a hrách RPG z papíru a pera se používá mnoho typů kostek, nejen ty dobře známé kostkové.
Jednou z nejoblíbenějších kostek jsou například desetistěnné nebo dokonce stostěnné!
Protože se kostkami ve hrách často hází, psát pokaždé "např. hoď dvěma desetistěnnými kostkami a k výsledku
přičti 20" by bylo nudné, složité a plýtvalo by se obrovským množstvím papíru.
V takových situacích se používá kód "hod 2D10+20".

Kód pro takovou kostku má následující vzorec:
xDy+z
 - y - typ kostky, kterou chcete použít (např. D6, D10).
 - x - počet hozených kostek; pro jeden hod se tento parametr vynechává,
 - z - modifikátor - číslo, které se přičte (nebo odečte) k výsledku hodu (nepovinné).

Příklady:
 - 2D10+10: hod 2 kostkami D10, k výsledku přičtěte 10.
 - D6: jeden hod kostkou.
 - 2D3: hod 2 třístrannými kostkami.
 - D12-1: hoďte jednou kostkou D12 a od výsledku odečtěte 1.

Napište funkci, která:
 - převzít takový kód jako řetězec v parametru,
 - rozpoznat všechna vstupní data:
    - typ kostek
    - počet rolí
    - modifikátor
 - vrátí příslušnou zprávu, pokud je zadaný řetězec neplatný
 - simulovat hody a vrátit výsledek

Typy kostek používaných ve hrách: D3, D4, D6, D8, D10, D12, D20, D100. 
"""
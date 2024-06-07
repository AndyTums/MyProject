from typing import Union


def mask_account_card(number: int | str) -> str:
    """Маскирует номер карты"""
    number_lower = number.lower()
    if "счет" in number_lower:
        return "Счет" + " " + 2 * "*" + number[-4:]
    else:
        return number[0:-12] + 2 * "*" + " " + 4 * "*" + " " + number[-4:]



from typing import Union


def get_mask_card_number(number: int | str) -> str:
    """Маскирует номер карты"""
    inter = str(number)
    mask_number = inter[:7] + 2 * "*" + " " + 4 * "*" + " " + inter[-4:]

    return mask_number


def get_mask_account(account: int) -> str:
    """Маскирует номер счета"""
    inter = str(account)
    mask_account = 2 * "*" + inter[-4:]

    return mask_account

print(get_mask_card_number("7000 7922 8960 6361"))
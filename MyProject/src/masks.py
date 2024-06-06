from typing import Union


def get_mask_card_number(number: int) -> str:
    """Маскирует номер карты"""
    inter = str(number)
    mask_number = inter[:6] + 6 * "*" + inter[-4:]

    return mask_number


def get_mask_account(account: int) -> str:
    """Маскирует номер счета"""
    inter = str(account)
    mask_account = 2 * "*" + inter[-4:]

    return mask_account

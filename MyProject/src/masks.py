def get_mask_card_number(number: str) -> str:
    """Маскирует номер карты"""
    mask_number = number[:7] + 2 * "*" + " " + 4 * "*" + " " + number[-4:]

    return mask_number


def get_mask_account(account: str) -> str:
    """Маскирует номер счета"""
    inter = str(account)
    mask_account = 2 * "*" + inter[-4:]

    return mask_account

from masks import get_mask_account
from masks import get_mask_card_number


def mask_account_card(number: str) -> str:
    """Маскирует номер карты и счета"""
    number_lower = number.lower()
    if "счет" in number_lower:
        return get_mask_account(number)
    else:
        return get_mask_card_number(number)


def get_data(dat: str) -> str:
    """Возращает строку с датой"""
    return dat[8:10] + "." + dat[5:7] + "." + dat[0:4]

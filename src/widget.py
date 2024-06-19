from masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    """Маскирует номер карты и счета"""
    number_lower = number.lower()
    if "счет" in number_lower:
        return get_mask_account(number)
    else:
        return get_mask_card_number(number)


def get_data(dat: str) -> str:
    """Возращает строку с датой"""
    interger = str(dat)
    if len(interger) < 10:
        return "Ошибка, повторите ввод данных."
    return interger[8:10] + "." + interger[5:7] + "." + interger[0:4]

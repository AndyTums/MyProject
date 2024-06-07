def mask_account_card(number: str) -> str:
    """Маскирует номер карты"""
    number_lower = number.lower()
    if "счет" in number_lower:
        return "Счет" + " " + 2 * "*" + number[-4:]
    else:
        return number[0:-12] + 2 * "*" + " " + 4 * "*" + " " + number[-4:]


def get_data(dat: str) -> str:
    """Возращает строку с датой"""
    return dat[8:10] + "." + dat[5:7] + "." + dat[0:4]

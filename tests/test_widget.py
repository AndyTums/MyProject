import pytest
from src.widget import mask_account_card, get_data


@pytest.mark.parametrize(
    "inter, out",
    [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
     ("Счет 73654108430135874305", "Счет **4305")],)
def test_mask_account(inter, out):
    assert mask_account_card(inter) == out


def test_get_data(testing):
    assert get_data(testing) == "11.07.2018"

    assert get_data("") == "Ошибка, повторите ввод данных."

    assert get_data(1) == "Ошибка, повторите ввод данных."

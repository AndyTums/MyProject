import pytest


@pytest.fixture
def coll():
    return ["mom", "like", "apple"]


@pytest.fixture
def testing_masks():
    return "Maestro 1596837868705199"


@pytest.fixture
def testing_card_number():
    return "Счет 73654108430135874305"


@pytest.fixture
def testing():
    return "2018-07-11T02:26:18.671407"

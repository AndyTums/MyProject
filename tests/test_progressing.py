import pytest
from src.processing import filter_by_state


@pytest.mark.parametrize(
    "list_info, result",
    [
        ([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}], []),
        ([{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}], []),
        (
            [{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}],
            [{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}])])
def test_filter_state(list_info, result):
    assert filter_by_state(list_info) == result

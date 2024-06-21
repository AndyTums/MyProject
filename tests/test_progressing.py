import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "list_info, result",
    [
        ([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}], []),
        ([{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}], []),
        (
            [{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}],
            [{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}],
        ),
    ],
)
def test_filter_state(list_info, result):
    assert filter_by_state(list_info) == result


@pytest.mark.parametrize(
    "test_list, results",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        )
    ],
)
=======
@pytest.mark.parametrize("test_list, results",
                         [
                             ([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                               {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}],
                              [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                               {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}])])
def test_sort_by_data(test_list, results):
    assert sort_by_date(test_list) == results


def testing_sort_data(test_sort):
    assert sort_by_date(test_sort) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


def testing_filter_state(test_sort):
    assert filter_by_state(test_sort) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                          {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

from typing import Any


def filter_by_state(transactions: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """Возвращает список, где state = новому значению."""
    new_list = []
    for key in transactions:
        if key.get("state") == state:
            new_list.append(key)

    return new_list


def sort_by_date(lists: list, sorts: bool = True) -> list:
    """Сортировка словарей по дате."""
    return sorted(lists, key=lambda x: x.get("date"), reverse=sorts)


print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]))

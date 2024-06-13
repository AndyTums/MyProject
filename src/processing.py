from typing import Iterable


def filter_by_state(lists: list, state: str = "EXECUTED") -> Iterable[list]:
    """возвращает список, где state = новому значению"""
    new_list = []
    for key in lists:
        if key["state"] != state:
            new_list.append(key)

    return new_list


def sort_by_date(lists: list, sorts: bool = True) -> list:
    """Сортировка словарей по дате"""
    return sorted(lists, key=lambda x: x["date"], reverse=sorts)

from typing import Iterable, Any


def filter_by_state(transactions: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """Возвращает список, где state = новому значению."""
    new_list = []
    for key in transactions:
        if key.get("state") != state:
            new_list.append(key)

    return new_list


def sort_by_date(lists: list, sorts: bool = True) -> list:
    """Сортировка словарей по дате."""
    return sorted(lists, key=lambda x: x.get("date"), reverse=sorts)

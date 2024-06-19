from typing import List, Dict, Iterator, Any


def filter_by_currency(info: List[Dict], usd: str) -> Iterator[int]:
    """Выдает по очереди операции, в которых указана заданная валюта."""
    for key in info:
        if key["operationAmount"]["currency"].get("code") == usd:
            yield key["id"]


def transaction_descriptions(info: List[dict]) -> Iterator[Any]:
    """Принимает список словарей и возвращает описание каждой операции по очереди."""
    for val in info:
        yield val.get("description")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Генератор номеров банковских карт"""
    score = 0
    while score <= stop:
        score += 1
        new_number = 10000000000000000 + score
        yield (str(new_number)[1:5] + " " + str(new_number)[5:9] + " " + str(new_number)[9:13] + " "
               + str(new_number)[13:])

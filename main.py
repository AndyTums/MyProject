from typing import Iterable

import random
from typing import Iterable, Any



def repeating_letter(lists: Iterable[str]) -> Iterable[str]:
    """Функция выводит список слов с одинаковыми первыми и последними символами"""
    new_list = []
    for i in lists:
        if len(i) == 0 and isinstance(i, int):
            continue
        if i[0] == i[-1]:
            new_list.append(i)

    return new_list


def multiplying_numbers(lists: list[int]) -> int:
    """Функция возвращает произведение наибольших чисел из списка"""
    if len(lists) < 2:
        return 0
    else:
        nums = []
        maxim_1 = max(lists)
        nums.append(maxim_1)
        lists.remove(maxim_1)
        maxim_2 = max(lists)
        nums.append(maxim_2)
        mult = nums[0] * nums[1]

        return mult

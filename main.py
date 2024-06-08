from typing import Iterable, Any


def repeating_letter(lists: Iterable[str]) -> Iterable[str]:
    """Функция выводит список слов с одинаковыми первыми и последними символами"""
    new_list = []
    for i in lists:
        if len(i) == 0:
            continue
        if i[0] == i[-1]:
            new_list.append(i)

    return new_list


def multiplying_numbers(lists: Any) -> Any:
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


# site = os.getcwd()
# print(site)
# val_files = 0
# val_dict = 0
# files = os.listdir(site)
# print(files)
# for i in files:
#     if i is os.path.isfile(site):
#         val_files += 1
#     if i is os.path.isdir(site):
#         val_dict += 1
#
# print(val_files, val_dict)

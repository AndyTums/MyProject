import json


def read_file(filename: str = None) -> list:
    """Функция считывающая информацию JSON формата с заданного файла"""
    try:
        with open(filename, encoding="utf-8") as file:
            reading = json.load(file)
            return reading
    except:
        return []


transaction = (read_file("../data/operations.json"))
print(transaction)

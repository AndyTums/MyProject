import os
from dotenv import load_dotenv
import requests
from src.utils import transaction


def check_currency(transaction: list) -> str:
    amount = float(transaction[1]["operationAmount"]["amount"])  # получение числа траты
    currency = transaction[1]["operationAmount"]["currency"]["code"]  # получениу валюты
    if currency != "RUB":
        load_dotenv()
        API_TOKEN = os.getenv("API_TOKEN")
        url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={currency}"

        payload = {}
        headers = {"apikey": f"{API_TOKEN}"}

        response = requests.request("GET", url, headers=headers, data=payload)

        status_code = response.status_code
        result = response.json()

        convert_currency = result["rates"]["RUB"]
        convert_in_RUB = round(convert_currency * amount, 2)

        return convert_in_RUB
    return amount


print(check_currency(transaction))

# changer = "EUR"
# url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={changer}"
#
# payload = {}
# headers = {"apikey": "gjNxAIKjq5NO1nguawomfeozZHln23Pf"}
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# status_code = response.status_code
# result = response.text
#
# print(result)

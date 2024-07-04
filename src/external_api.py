import os
from dotenv import load_dotenv
import requests


def check_currency(transaction):
    amount = float(transaction["operationAmount"]["amount"])  # получение суммы траты
    currency = transaction["operationAmount"]["currency"]["code"]  # получение валюты
    if currency != "RUB":
        load_dotenv()
        API_TOKEN = os.getenv("API_TOKEN")
        url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={currency}"

        payload = {}
        headers = {"apikey": f"{API_TOKEN}"}

        response = requests.get(url, headers=headers, data=payload)

        # status_code = response.status_code
        # result = response.json()
        #
        # convert_currency = result["rates"]["RUB"]
        # convert_in_RUB = round(convert_currency * amount, 2)
        # return response.json()
        return round(response.json()["rates"]["RUB"] * amount, 2)
    return amount

# transaction = {
#     "id": 41428829,
#     "state": "EXECUTED",
#     "date": "2019-07-03T18:35:29.512364",
#     "operationAmount": {
#       "amount": "8221.37",
#       "currency": {
#         "name": "USD",
#         "code": "USD"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "MasterCard 7158300734726758",
#     "to": "Счет 35383033474447895560"
#   }
#
# print(check_currency(transaction))


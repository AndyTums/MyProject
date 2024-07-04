from unittest.mock import Mock, patch

import requests

from src.external_api import check_currency


@patch("requests.get")
def test_check_currency(mock_get):
    mock_get.return_value.json.return_value = 731698.54 # тут пытался получить и словарь в функции return response.json()
    assert check_currency(transaction) == 731698.54
    mock_get.assert_called_once_with("https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base=USD")

transaction = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }
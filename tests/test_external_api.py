from unittest.mock import MagicMock, patch

from src.external_api import check_currency

transaction = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
        "amount": "8221.37",
        "currency": {
            "name": "USD",
            "code": "USD"
        }}}


@patch("requests.get")
def test_check_currency(mock_get):
    mock_response = MagicMock()
    mock_response.json = {'success': True, 'timestamp': 1720199764, 'base': 'USD', 'date': '2024-07-05',
                          'rates': {'RUB': 88.000037}}
    mock_get.return_value = mock_response

import os

import pytest
from src.decorators import my_function


def test_in_file():
    """Тест декоратора log"""
    with pytest.raises(ZeroDivisionError):
        my_function(10, 0)
    log_file = os.path.join(os.path.dirname(__file__), "mylog.txt")
    with open(log_file, "r") as file:
        log_test = file.read()
        assert log_test == "my function error:division by zero. Input: ((10, 0), {})"

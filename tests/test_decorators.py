import pytest
from src.decorators import my_function


def test_log():
    with pytest.raises(ZeroDivisionError):
        my_function(1, 0)

        assert my_function(10, 2) == 5


def test_log_caps(capsys):
    my_function(10, 2)
    captured = capsys.readouterr()
    assert captured.out == ""

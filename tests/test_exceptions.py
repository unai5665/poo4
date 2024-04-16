import pytest

def test_exception():
    a = 0
    b = 10
    with pytest.raises(ZeroDivisionError):
        b / a
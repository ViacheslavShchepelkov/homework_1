import pytest
from src.phone import Phone


@pytest.fixture
def my_phone():
    return Phone('IPhone_14', 100000, 500, 2)


def test_repr(my_phone):
    assert repr(my_phone) == "Phone('IPhone_14', 100000, 500, 2)"


def test_str(my_phone):
    assert str(my_phone) == 'IPhone_14'
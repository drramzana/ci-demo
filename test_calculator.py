import pytest
from calculator import add, divide


def test_add():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-1, 1) == 0


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)


def test_subtract_positive():
    assert sub(3,2) == 1

def test_subtract_negative():
    assert sub(-3,2) == -5

def test_subtract_zero():
    assert sub(0,2) == -2

def test_multiply_positive():
    assert multiply(6,2)==12

def test_multiply_negative():
    assert multiply(-3,-2)==6

def test_multiply_zero():
    assert multiply(0,2)==0

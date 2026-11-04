
# def test_greater():
#     num = 100
#     assert num > 50

# def test_greater_equal():
#     num = 100
#     assert num >= 100

# def test_less():
#     num = 100
#     assert num < 200


import pytest

@pytest.mark.great
def test_greater():
    num = 100
    assert num > 50

@pytest.mark.great
def test_greater_equal():
    num = 100
    assert num >= 100

def test_less():
    num = 100
    assert num < 200



def test_addition():
    assert 10 + 20 == 30

def test_subtraction():
    assert 50 - 20 == 30

def test_multiplication():
    assert 5 * 4 == 20

def test_division():
    assert 20 / 5 == 4

def test_string_equality():
    assert "pytest" == "pytest"

def test_list_length():
    numbers = [10, 20, 30, 40]
    assert len(numbers) == 4

def test_list_contains():
    numbers = [10, 20, 30, 40]
    assert 30 in numbers

def test_boolean_value():
    assert 10 > 5

def test_not_equal():
    assert 10 != 20

def test_zero():
    assert 5 - 5 == 0



import pytest

@pytest.fixture
def sample_number():
    return 100

def test_greater(sample_number):
    assert sample_number > 50

def test_less(sample_number):
    assert sample_number < 200


def test_number_is_integer(sample_number):
    assert isinstance(sample_number, int)

def test_number_is_positive(sample_number):
    assert sample_number > 0

def test_number_is_even(sample_number):
    assert sample_number % 2 == 0

def test_number_is_not_zero(sample_number):
    assert sample_number != 0


def test_intentional_failure():
    assert 10 > 20


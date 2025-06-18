#tests/test_generate_prime_factors.py
import pytest

def valueerror_test():
    """Asserts that a value error is raised when a data type that is not an integer is called"""
    with pytest.raises(ValueError,int):
        raise ValueError('Value must be an integer.')


def one_is_call():
    """Asserts that 1 returns an empty list"""
    assert 1 == " "

def two_is_called():
    """Asserts that 2 returns [2]"""
    assert 2 == [2]

def three_is_called():
    """Asserts that 3 returns [3]"""
    assert 3 == [3]

def four_is_called():
    """Asserts that 4 returns [2, 2]"""
    assert 4 == [2, 2]

def six_is_called():
    """Asserts that 6 returns [2,3]"""
    assert 6 == [2,3]

def eight_is_called():
    """Asserts that 8 returns [2, 2, 2]"""
    assert 8 == [2, 2, 2]

def nine_is_called():
    """Asserts that 9 returns [3, 3]"""
    assert 9 == [3, 3]
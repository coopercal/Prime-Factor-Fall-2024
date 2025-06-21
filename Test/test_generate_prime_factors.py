#tests/test_generate_prime_factors.py
import pytest

from prime import generate_prime_factors


def test_ValueError():
    """Asserts that a value error is raised when a data type that is not an integer is called"""
    with pytest.raises(ValueError):
        generate_prime_factors(3.0)

def test_oneIsCalled():
    """Asserts that 1 returns an empty list"""
    assert generate_prime_factors(1) == " "

def test_twoIsCalled():
    """Asserts that 2 returns [2]"""
    assert generate_prime_factors(2) == [2]

def test_threeIsCalled():
    """Asserts that 3 returns [3]"""
    assert generate_prime_factors(3) == [3]

def test_fourIsCalled():
    """Asserts that 4 returns [2, 2]"""
    assert generate_prime_factors(4) == [2, 2]

def test_sixIsCalled():
    """Asserts that 6 returns [2,3]"""
    assert generate_prime_factors(6) == [2,3]

def test_eightIsCalled():
    """Asserts that 8 returns [2, 2, 2]"""
    assert generate_prime_factors(8) == [2, 2, 2]

def test_nineIsCalled():
    """Asserts that 9 returns [3, 3]"""
    assert generate_prime_factors(9) == [3, 3]
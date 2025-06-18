#tests/test_generate_prime_factors.py
import pytest

def valueerror_test():
    """Asserts that a value error is raised when a data type that is not an integer is called"""
    with pytest.raises(ValueError,int):
        raise ValueError('Value must be an integer.')


def one_is_call():
    """Asserts that 1 returns an empty list"""
    assert 1 == " "

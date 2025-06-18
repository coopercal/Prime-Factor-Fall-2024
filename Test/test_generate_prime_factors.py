#tests/test_generate_prime_factors.py
import pytest

from pytest import raises

from prime import generate_prime_factors


def ValueError_Test():
    """Asserts that a value error is raised when a data type that is not an integer is called"""
    with raises(ValueError):
        generate_prime_factors()
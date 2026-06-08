from pytest.test_fibonacci import fib
import pytest 

def test_fib_negatvie_raises_value_error():
    with pytest.raises(ValueError):
        fib(-1)

@pytest.mark.parametrize(
    'n, expected', 
    [
        (0,0), 
        (1,1),
        (2,1),
        (3, 2),
        (30, 832040)
    ]
)

def test_fib_known_values(n, expected):
    assert fib(n) == expected

def test_fib_recurrence_property():
    for n in range(2, 10):
        assert fib(n) == fib(n - 1) + fib(n - 2)

def test_fib_larger_input():
    assert fib(30) == 832040


## second solution 

import pytest

from fibonacci import fib


def test_base_case():
    assert fib(0) == 0
    assert fib(1) == 1


def test_higher_numbers():
    assert fib(10) == 55
    assert fib(30) == 832040


def test_negative_number():
    with pytest.raises(ValueError):
        fib(-1)
import pytest

from numbers_to_dec import list_to_decimal


def test_negative_number():
    with pytest.raises(ValueError):
        list_to_decimal([1, -2, 3])


def test_not_int_type():
    with pytest.raises(TypeError):
        list_to_decimal(['a', 'b', 5])


def test_not_int_val():
    with pytest.raises(TypeError):
        list_to_decimal([3.6, 5, 6])


def test_with_other_val():
    with pytest.raises(TypeError):
        list_to_decimal([6, 2, True])


def test_returns_decimal_number():
    assert list_to_decimal([1, 7, 5]) == 175


def test_ignores_leading_zeroes():
    assert list_to_decimal([0, 3, 1, 2]) == 312
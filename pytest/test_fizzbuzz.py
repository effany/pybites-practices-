from fizzbuzz import fizzbuzz

def test_3_and_5_returns_fizz_buzz():
    assert fizzbuzz(15) == 'Fizz Buzz'

def test_3_returns_fizz():
    assert fizzbuzz(3) == 'Fizz'

def test_5_returns_buzz():
    assert fizzbuzz(5) == 'Buzz'

def test_other_number_returns_number():
    assert fizzbuzz(7) == 7
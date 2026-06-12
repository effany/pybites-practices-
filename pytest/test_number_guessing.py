from number_guessing import GuessGame, InvalidNumber
import pytest

@pytest.fixture
def number():
    return GuessGame(10, max_guesses=5)

def test_invalidate_number():
    with pytest.raises(InvalidNumber):
        GuessGame('not a number')

def test_negative_number():
    with pytest.raises(InvalidNumber):
        GuessGame(-2)

def test_over_max_number():
    with pytest.raises(InvalidNumber):
        GuessGame(20)

def test_guess_number(capsys, monkeypatch):
    game = GuessGame(13, max_guesses=5)
    answers = iter([2, 14, 13])
    monkeypatch.setattr('builtins.input', lambda: next(answers))
    game()
    captured = capsys.readouterr()
    assert 'Too low' in captured.out
    assert 'Too high' in captured.out
    assert 'You guessed it!' in captured.out 

def test_failed_to_guess(capsys, monkeypatch):
    game = GuessGame(9, max_guesses=2)
    answers = iter([5, 12, 13])
    monkeypatch.setattr('builtins.input', lambda: next(answers))
    game()
    captured = capsys.readouterr()
    assert 'Sorry, the number was 9' in captured.out
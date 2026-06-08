from workout import print_workout_days

def test_existing_workout(capsys):
    print_workout_days("upper body #1")
    captured = capsys.readouterr()
    assert captured.out == 'Mon\n'

def test_no_match(capsys):
    print_workout_days("yoga")
    captured = capsys.readouterr()
    assert captured.out == "No matching workout\n"
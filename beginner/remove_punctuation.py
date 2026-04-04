import string

def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    return "".join(char for char in input_string if char not in string.punctuation)

print(remove_punctuation('bla, hey bla cool! @ miaw'))
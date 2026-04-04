import string
def count_indents(text: str) -> int:
    """
    Count and return the number of leading white space characters (' ').
    """
    counter = 0
    for char in text:
        if char != " ":
            break
        else:
            counter += 1

    return counter
    

def count_indents(text: str) -> int:
    return len(text) - len(text.lstrip(' '))
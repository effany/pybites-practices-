import string

def validate_pangram(sentence: str) -> bool:
    """Check if a sentence is a pangram
    A pangram is a sentence containing every letter in the English alphabet.
    The input `sentence` should be a string containing only English letters.
    The function returns True if the sentence is a pangram, and False otherwise.
    """
    lower_case_sentence = set([char.lower() for char in sentence if char != " "])
    sorted_sentence = "".join(sorted(lower_case_sentence))
    if sorted_sentence == string.ascii_lowercase:
        return True
    else:
        return False



if __name__ == "__main__":
    result = validate_pangram("The quick brown fox jumps over a lazy dog")
    result2 = validate_pangram("PYBITES IS A COMMUNITY OF PYTHON CODERS")
    print(result2)

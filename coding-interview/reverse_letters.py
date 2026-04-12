import string as s

def reverse_letters(string: str) -> str:
    """Reverse letters in a string but keep the order of the non-letters the same"""
    string_array = [char for char in string]
    rev_array = string_array[::-1] 
    rev_array_sanitize = [char for char in rev_array if char in s.ascii_letters]
    for i, char in enumerate(string_array):
        if char in s.ascii_letters:
            continue
        else:
            rev_array_sanitize.insert(i, char)
    return "".join(rev_array_sanitize)
            

def reverse_letters_method_2(string: str) -> str:
    letters = [c for c in string if c in s.ascii_letters]
    result = list(string)
    print(result)
    for i, char in enumerate(result):
        if char in s.ascii_letters:
            result[i] = letters.pop()
    print("".join(result))
    return "".join(result)

if __name__ == "__main__":
    result = reverse_letters('a-bC-dEf-ghIj')
    result2 = reverse_letters_method_2('a-bC-dEf-ghIj')
    print(result2)
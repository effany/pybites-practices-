import string

def convert_string_to_index(input_value: str | list[str]) -> list[int]:
    if input_value == "":
        return []
    elif isinstance(input_value, str):
        list_to_process = input_value.replace(" ", "").split(',')
    else:
        list_to_process = input_value

    result = []
    for i in list_to_process:
        if ":" in i:
            start, end = i.split(":")
            result.extend(range(letter_to_index(start), letter_to_index(end) + 1))
        else:
            result.append(letter_to_index(i))
    return result

def letter_to_index(s):
    result = 0
    for char in s:
        result = result * 26 + (string.ascii_uppercase.index(char) + 1)
    return result - 1


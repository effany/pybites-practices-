IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names):
    names_array = []
    for name in names:
        if name[0] == IGNORE_CHAR or any(char.isdigit() for char in name):
            continue
        elif name[0] == QUIT_CHAR:
            break
        elif len(names_array) < MAX_NAMES:
            names_array.append(name)
    return names_array

        

filter_names(['tim', 'amber', 'ana', 'c1ndy', 'sara', 'molly', 'henry'])
from typing import List

EAST = "E"
WEST = "W"


def search_apartment(buildings: List[int], direction: str) -> List[int]:
    """
    Find and return the indices of those building with
    the desired view: EAST (E) or WEST (W).

    See sample inputs / outputs below and in the tests.
    """
    new_list = []
    
    index_collection = []
    if direction == 'W':
        new_list.append(buildings[0])
        index_collection.append(0)
        for index, b in enumerate(buildings):
            if max(new_list) >= b:
                continue
            else:
                new_list.append(b)
                index_collection.append(index)
    elif direction == 'E':
        for index, b in enumerate(reversed(buildings)):
            real_index = len(buildings) - 1 - index
            if not new_list or b > max(new_list):
                index_collection.append(real_index)
                new_list.append(b)
        index_collection.reverse()
    return index_collection




if __name__ == "__main__":
    A = [3, 5, 4, 4, 7, 1, 3, 2]  # central tallest
    B = [1, 1, 1, 1, 1, 2]  # almost flat
    #
    #  W <-                    ->  E(ast)
    #
    print(search_apartment(A, "W"))  # [0, 1, 4]
    print(search_apartment(A, "E"))  # [4, 6, 7]
    print(search_apartment(B, "W"))  # [0, 5]
    print(search_apartment(B, "E"))  # [5]
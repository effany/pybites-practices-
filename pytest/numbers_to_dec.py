from typing import List


def list_to_decimal(nums: List[int]) -> int:
    """Accept a list of positive integers in the range(0, 10)
    and return an integer where each int of the given list represents
    decimal place values from first element to last.
    """
    for num in nums:
        if isinstance(num, bool) or not isinstance(num, int):
            raise TypeError
        if num not in range(0, 10):
            raise ValueError

    return int("".join(map(str, nums)))

IMPOSSIBLE = 'Mission impossible. No one can contribute.'


def max_fund(village):
    """Find a contiguous subarray with the largest sum."""
    # Hint: while iterating, you could save the best_sum collected so far
    # return total, starting, ending
    if not village:
        print(IMPOSSIBLE)
        return (0, 0, 0)

    best_total = float('-inf')
    current_total = 0
    current_start = 0
    best_start = 0
    best_end = 0

    for index, house in enumerate(village):
        if current_total <= 0:
            current_total = house
            current_start = index
        else:
            current_total += house

        if current_total > best_total:
            best_total = current_total
            best_start = current_start
            best_end = index

    if best_total <= 0:
        print(IMPOSSIBLE)
        return (0, 0, 0)

    return best_total, best_start + 1, best_end + 1



community = [3, 2, 6,  4, 7,  5, -8, -9, 3,  8,  4, -12, 3, -10, -15,
             2, 6, -10, 6, 3, -1,  5, -5, -8, 11, 7, -9, -5,  -6, -2,
             7, 8, 11, 8,  6, -1, -6,  9, 8, 6, -3, 4,  -8, 3, -4, 1,
             2, 8, -2, 9, -3, 8, -10,  -8,  5,  -4, -6,  5, -1, 4, 2,
             2, 7,  3, -2, 5, 1, 4, -7, 5, 8, 4, 2, 10, -24, -10, -9,
             -2, 1, 6, 1,  3, -44, 3, 6, -1, 9, -6, 5, 4, 3, 6, -1,
             0, 11, 4, 8, 16, -33, 8, -2, 4, 5, 3, 2, -8, -7, -5,
             0, 2, 5, -2, 4, 1, 2, 4, 2, -5, 7, 4, 5, -2, 7, 5, -8]

print(max_fund(community))
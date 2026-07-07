DOWN, UP, LEFT, RIGHT = '⇓', '⇑', '⇐', '⇒'
START_VALUE = 1

def print_sequence_route(grid, start_coordinates=None):
    """Receive grid string, convert to 2D matrix of ints, find the
       START_VALUE coordinates and move through the numbers in order printing
       them.  Each time you turn append the grid with its corresponding symbol
       (DOWN / UP / LEFT / RIGHT). See the TESTS for more info."""
    matrix = []
    for line in grid.strip().splitlines():
        row = []
        for token in line.split():
            if token.isdigit():
                row.append(int(token))
        if row:
            matrix.append(row)

    if not matrix:
        return

    max_value = max(max(row) for row in matrix)
    nums = [i + 1 for i in range(1, max_value)]
    segments = []
    for i in range(1, len(matrix)):
        # i is amount of number per segment
        seg1 = nums[:i]
        nums = nums[i:]
        seg2 = nums[:i]
        segments.append(seg1)
        segments.append(seg2)
        nums = nums[i:]
    
    directions = [DOWN, LEFT, UP, RIGHT]
    
    for i in range(len(segments)):
        first_dir = directions[0]
        segments[i].append(directions[0])
        directions.pop(0)
        directions.append(first_dir)
    
    segments[0].insert(0, 1)

    # Remaining values belong to the final line and have no direction arrow.
    if nums:
        segments.append(nums)

    for seg in segments:
        print(" ".join(map(str, seg)))
   

## solution 2

from collections import namedtuple
import re

DOWN, UP, LEFT, RIGHT = '⇓', '⇑', '⇐', '⇒'
START_VALUE = 1

Move = namedtuple('Move', 'axis direction offset')
# x = vertical (first list), y = horizontal (move in row = nested list)
POSSIBLE_MOVES = [Move('|', DOWN, (1, 0)),
                  Move('|', UP, (-1, 0)),
                  Move('-', LEFT, (0, -1)),
                  Move('-', RIGHT, (0, 1))]


def _make_grid(grid):
    """Turn grid string into 2D array of ints"""
    for row in grid.strip().splitlines():
        if not row[0].isdigit():
            continue
        yield [int(n) for n in re.split(r'[- ]+', row)]


def _get_starting_point(grid):
    """Get coordinates of starting point (cell with START_VALUE)"""
    for x, row in enumerate(grid):
        for y, val in enumerate(row):
            if val == START_VALUE:
                return (x, y)
    raise RuntimeError(f'{START_VALUE} not found in grid')


def print_sequence_route(grid, start_coordinates=None):
    """Receive grid string, convert to 2D matrix of ints, find the
       START_VALUE coordinates and move through the numbers in order printing
       them.  Each time you turn append the grid with its corresponding symbol
       (DOWN / UP / LEFT / RIGHT). See the TESTS for more info."""
    if isinstance(grid, str):
        grid = list(_make_grid(grid))

    if start_coordinates is None:
        start_coordinates = _get_starting_point(grid)

    size_grid = sum(len(row) for row in grid)
    vertical, horizontal = start_coordinates

    previous_value, previous_move = START_VALUE, None
    print(START_VALUE, end=' ')

    while True:
        for move in POSSIBLE_MOVES:
            axis, direction, (vert_move, hor_move) = move
            try:
                new_value = grid[vertical + vert_move][horizontal + hor_move]
            except IndexError:  # grid boundaries
                continue

            if new_value - previous_value == 1:
                if previous_move and previous_move.axis != move.axis:
                    print(move.direction)
                print(new_value, end=' ')

                vertical += vert_move
                horizontal += hor_move
                previous_value, previous_move = new_value, move

        if new_value == size_grid:  # end grid
            break          
                
    


small_grid = """
21 - 22 - 23 - 24 - 25
 |
20    7 -  8 -  9 - 10
 |    |              |
19    6    1 -  2   11
 |    |         |    |
18    5 -  4 -  3   12
 |                   |
17 - 16 - 15 - 14 - 13
"""

intermediate_grid = """
43 - 44 - 45 - 46 - 47 - 48 - 49
 |
42   21 - 22 - 23 - 24 - 25 - 26
 |    |                        |
41   20    7 -  8 -  9 - 10   27
 |    |    |              |    |
40   19    6    1 -  2   11   28
 |    |    |         |    |    |
39   18    5 -  4 -  3   12   29
 |    |                   |    |
38   17 - 16 - 15 - 14 - 13   30
 |                             |
37 - 36 - 35 - 34 - 33 - 32 - 31
"""


if __name__ == '__main__':
    print_sequence_route(intermediate_grid)
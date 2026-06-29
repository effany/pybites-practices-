from collections import deque


def count_islands(grid):
    """
    Input: 2D matrix, each item is [x, y] -> row, col.
    Output: number of islands, or 0 if found none.
    Notes: island is denoted by 1, ocean by 0 islands is counted by continuously
        connected vertically or horizontally  by '1's.
    It's also preferred to check/mark the visited islands:
    - eg. using the helper function - mark_islands().
    """
    if not grid or not grid[0]:
        return 0

    islands = 0

    for r_index, row in enumerate(grid):
        for c_index, col in enumerate(row):
            if col == 1:
                islands += 1
                mark_islands(r_index, c_index, grid)
    return islands





def mark_islands(i, j, grid):
    """
    Input: the row, column and grid
    Output: None. Just mark the visited islands as in-place operation.
    """
    num_of_rows = len(grid)
    num_of_cols = len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    if grid[i][j] != 1:
        return

    queue = deque([(i, j)])
    grid[i][j] = '#'

    while queue:
        cell = queue.popleft()
        for dr, dc in directions:
            neighbor = (cell[0] + dr, cell[1] + dc)
            if (0 <= neighbor[0] < num_of_rows and 0 <= neighbor[1] < num_of_cols
                    and grid[neighbor[0]][neighbor[1]] == 1):
                grid[neighbor[0]][neighbor[1]] = '#'
                queue.append(neighbor)


grid = [[1, 0, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 0],
        [1, 0, 0, 1]]


print(count_islands(grid))
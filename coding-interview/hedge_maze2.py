from typing import List, Tuple
from collections import deque


DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def hedge_maze(maze: List[List[str]], entrance: Tuple[int, int]) -> int:
    """Finds the shortest distance from the entrance to the nearest exit in a maze."""
    rows = len(maze)
    cols = len(maze[0])
    r, c = entrance

    if not (0 <= r < rows and 0 <= c < cols) or maze[r][c] == "+":
        raise ValueError

    queue = deque([(r, c, 0)])
    visited = {(r, c)}

    while queue:
        row, col, steps = queue.popleft()
        for dr, dc in DIRECTIONS:
            nr, nc = row + dr, col + dc
            if not (0 <= nr < rows and 0 <= nc < cols):
                continue
            if (nr, nc) in visited or maze[nr][nc] != ".":
                continue
            if nr == 0 or nr == rows - 1 or nc == 0 or nc == cols - 1:
                return steps + 1
            visited.add((nr, nc))
            queue.append((nr, nc, steps + 1))

    return -1
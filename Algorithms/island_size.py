# Hint:
# You can define a helper funtion: get_others(map, row, col) to assist you.
# Then in the main island_size function just call it when traversing the map.
from collections import deque

def get_others(map_, r, c):
    """Go through the map and check the size of the island
       (= summing up all the 1s that are part of the island)

       Input - the map, row, column position
       Output - return connected land cells as coordinates
    """
    if not map_ or not map_[0]:
        return set()

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    total_rows = len(map_)
    total_cols = len(map_[0])

    if not (0 <= r < total_rows and 0 <= c < total_cols):
        return set()
    if map_[r][c] != 1:
        return set()

    visited = {(r, c)}
    queue = deque([(r, c)])
    
    while queue:
        cell = queue.popleft()
        for dr, dc in directions:
            neighbor = (cell[0] + dr, cell[1] + dc)
            if (0 <= neighbor[0] < total_rows and 0 <= neighbor[1] < total_cols
                    and map_[neighbor[0]][neighbor[1]] == 1 and neighbor not in visited):
                queue.append(neighbor)
                visited.add(neighbor)
    return visited


def island_size(map_):
    """Hint: use the get_others helper

    Input: the map
    Output: the perimeter of the island
    """
    perimeter = 0
    start_points = []
    # your code here
    for r_index, r in enumerate(map_[0]):
        for c_index, c in enumerate(map_[1]):
            if map_[r_index][c_index] == 1:
                start_points.append((r_index, c_index))
    
    if len(start_points) == 0:
        return 0
    
    cells = list(get_others(map_, start_points[0][0], start_points[0][1]))

    print(cells)
    for cell in cells:
        touch_side = 0
        neighbors = [(cell[0] -1, cell[1]), (cell[0] + 1, cell[1]), (cell[0], cell[1] + 1), (cell[0], cell[1] - 1 )]
        for i in neighbors:
            if i in cells and map_[i[0]][i[1]] == 1:
                touch_side += 1
        perimeter += (4 - touch_side)
        

    return perimeter


rectangle = [[0, 1, 1, 0],
             [0, 1, 1, 0],
             [0, 1, 1, 0],
             [0, 1, 1, 0]]

small = [[0, 0, 0],
         [0, 1, 0],
         [0, 0, 0]]

empty = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

whole = [[1, 1, 1],
         [1, 0, 1],
         [1, 1, 1]]

# print(island_size(rectangle))
# print(island_size(empty))
print(island_size(small))
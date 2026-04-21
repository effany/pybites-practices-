from typing import List, Tuple


DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

## down, up , right, left

maze = [
    ["+1", "+2", ".3", "+4"],
    [".5", ".6", ".7" ,"+8"],
    ["+9", "+10", "+11", ".12"]
    ]

# maze = [
#     ["+", "+", ".", "+"],
#     [".", ".", "." ,"+"],
#     ["+", "+", "+", "."]
#     ]

def hedge_maze(maze: List[List[str]], entrance: Tuple[int, int]) -> int:
    org_pos = (entrance[0], entrance[1])
    print('org_pos', org_pos)
    """Finds the shortest distance from the entrance to the nearest exit in a maze."""
    availables = check_availability(entrance, org_pos)
    print(availables)
    while len(availables) > 0:
        for pose in availables:
            print('pose', pose[0], pose[1])
            new_entrance = pose
            availables = check_availability(new_entrance, org_pos)
            print('new', availables)

def check_availability(entrance, org_pos):
    current_row = entrance[0] 
    current_col = entrance[1]
    current_pos = maze[current_row][current_col]
    right = current_col + DIRECTIONS[2][1]
    left = current_col + DIRECTIONS[3][1]
    up = current_row + DIRECTIONS[0][0]
    down = current_row + DIRECTIONS[1][0]
    available_poses = []
    if '+' not in current_pos:
        right_pos = maze[current_row][right]
        left_pos = maze[current_row][left]
        up_pos = maze[up][current_col]
        down_pos = maze[down][current_col]
        poses_to_check = [
            (right_pos, (current_row, right)),
            (left_pos, (current_row, left)),
            (up_pos, (up, current_col)),
            (down_pos, (down, current_col))
        ]
        
        for value, position in poses_to_check:
            if '.' in value:
                available_poses.append(position)
        if org_pos in available_poses:
            available_poses = available_poses.remove(org_pos)
        print('availables', available_poses)
        if len(available_poses)  > 0:
            return available_poses
        else:
            return []

hedge_maze(maze, (1,2))
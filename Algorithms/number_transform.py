from collections import deque
def num_ops(n):
    """
    Input: an integer number, the target number
    Output: the minimum number of operations required to reach to n from 1.

    Two operations rules:
    1.  multiply by 2
    2.  int. divide by 3

    The base number is 1. Meaning the operation will always start with 1
    These rules can be run in any order, and can be run independently.

    [Hint] the data structure is the key to solve it efficiently.
    """
    # you code
    
    current_num = 1
    queue = deque([(current_num, 0)])
    visited = set()
    visited.add(1)
    ops_num = 0
    while queue:
        current = queue.popleft()
        current_num = current[0]
        ops_num = current[1]
        if current_num == n:
            return ops_num
        neighbor1 = current_num * 2
        neighbor2 = current_num // 3
        neighbors = [neighbor1, neighbor2]

        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, ops_num + 1))
    return ops_num

print(num_ops(15))
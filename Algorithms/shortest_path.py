import heapq


def shortest_path(graph, start, end):
    """
       Input: graph: a dictionary of dictionary
              start: starting city   Ex. a
              end:   target city     Ex. b

       Output: tuple of (distance, [path of cites])
       Ex.   (distance, ['a', 'c', 'd', 'b])
    """
    cost_table = {}
    prev = {}

    for city in graph:
        cost_table[city] = float("inf")
    cost_table[start] = 0

    changed = True

    while changed:
        changed = False
        for current in graph:
            print(current)
            if cost_table[current] == float("inf"):
                continue

            for neighbor, edge_cost in graph[current].items():
                new_cost = cost_table[current] + edge_cost
                if new_cost < cost_table[neighbor]:
                    cost_table[neighbor] = new_cost
                    prev[neighbor] = current
                    changed = True
    print('cost_table:', cost_table)

    path = [end]
    while path[-1] != start:
        path.append(prev[path[-1]])
    path.reverse()

    return cost_table[end], path

        


simple = {
          'a': {'b': 2, 'c': 4, 'e': 1},
          'b': {'a': 2, 'd': 3},
          'c': {'a': 4, 'd': 6},
          'd': {'c': 6, 'b': 3, 'e': 2},
          'e': {'a': 1, 'd': 2}
          }

print(shortest_path(simple, "a", "d"))
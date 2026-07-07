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

    for key, value in graph.items(): 
        cost_table[key] = float('inf')
        visited = [start]
        cost = 0
        if end in graph[key]:
            print(graph[key])
            cost += graph[key][end]
        else:
            pass
        print(cost)
    
            
        


simple = {
          'a': {'b': 2, 'c': 4, 'e': 1},
          'b': {'a': 2, 'd': 3},
          'c': {'a': 4, 'd': 6},
          'd': {'c': 6, 'b': 3, 'e': 2},
          'e': {'a': 1, 'd': 2}
          }

shortest_path(simple, 'a', 'd')
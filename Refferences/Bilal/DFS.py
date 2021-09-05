"""
DFS.py
Author: Jagrut Gala
Date: 10-07-2021
Practical: 1
Objective: Demonstrate DFS Algorithm
"""

def dfs(graph, start):
    visited, stack = [], [start]
    while stack:
        vertex = stack.pop()
        print(vertex, end=" ")
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(graph[vertex] - set(visited))
    return visited

def dfsRecursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for next in graph[start] - visited:
        dfsRecursive(graph, next, visited)
    return visited

big_graph= {
    "a": set(["k", "c", "l"]),
    "b": set(["k", "j"]),
    "c": set(["a"]),
    "d": set(["k", "g"]),
    "e": set(["j"]),
    "f": set(["h", "i"]),
    "g": set(["d", "f"]),
    "h": set(["f"]),
    "i": set(["f"]),
    "j": set(["b", "e"]),
    "k": set(["a", "b", "d"]),
    "l": set(["a"]),
}

dfs(big_graph, 'a')
print()
dfsRecursive(big_graph, 'a')

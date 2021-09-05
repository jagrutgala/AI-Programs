"""
bfs.py
Author: Jagrut Gala
Date: 17-07-2021
Practical: 2
Objective: Demostrate BFS Algorithm
"""
def bfs(visit_complete, graph, current_node):
    visit_complete.append(current_node)
    queue = []
    queue.append(current_node)

    while queue:
        s = queue.pop(0)
        print(s)

        for neighbour in graph[s]:
            if neighbour not in visit_complete:
                visit_complete.append(neighbour)
                queue.append(neighbour)

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

bfs([], big_graph, 'a')
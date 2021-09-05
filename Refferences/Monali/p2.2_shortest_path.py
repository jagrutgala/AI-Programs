"""
p2.2_shortest_path.py
Author: Jagrut Gala
Date: 17-07-2021
Practical: 2
Objective: Demonstrate BFS Algorithm and Shortest Path.
"""

def bfs(graph, start):
    visited= list()
    track= [start]
    while track:
        vertex= track.pop(0)
        print(vertex)
        if(vertex not in visited):
            visited.append(vertex)
            for i in graph[vertex]:
                track.append(i)

tree = { # abcde
    'a': set(['b', 'c']),
    'b': set(['a', 'd', 'e']),
    'c': set(['a']),
    'd': set(['b']),
    'e': set(['b', 'c', 'd'])
    }
bfs(tree, 'a')


graph = {
    'A': ['B', 'C', "D"],
    'B': ['E', "F"],
    'C': ['G', "I"],
    'D': ["I"],
    'E': [],
    "F": [],
    'G': [],
    "I": []
}

# Heather Fryling
# 3/8/2021

from digraph import *
from collections import deque

def bfs_shortest_path(g, start):
    q = deque()
    q.append(start)
    visited = set({})
    visited.add(start)
    distances = {}
    distances[start] = 0
    while(q):
        curr = q.popleft()
        for neighbor in g.graph[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
                distances[neighbor] = distances[curr] + 1
    return distances


g = DiGraph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(4, 3)
print(bfs_shortest_path(g, 1))
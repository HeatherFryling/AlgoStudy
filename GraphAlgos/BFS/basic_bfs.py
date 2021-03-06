# Heather Fryling
# 3/5/20201
# Implementation of basic bfs.

from digraph import *
from collections import deque

def bfs(g, start):
    visited = set({})
    traversal = []
    q = deque()
    q.append(start)
    visited.add(start)
    while len(q) != 0:
        u = q.popleft()
        traversal.append(u)
        for v in g.graph[u]:
            if v not in visited:
                q.append(v)
                visited.add(v)
    return traversal

g = DiGraph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(4, 3)
print(g)
print(bfs(g, 1))
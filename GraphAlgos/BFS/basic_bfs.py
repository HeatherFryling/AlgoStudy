# Heather Fryling
# 3/5/20201
# Implementation of basic bfs.

from digraph import *
from collections import deque

# PURPOSE
# Perform a breadth-first traversal of a directed graph in adjacency list
# format from a given starting point and return the traversal as a list.
# SIGNATURE
# bfs :: Digraph, Integer, Set, List => List
# TIME COMPLEXITY
# O(m)
# SPACE COMPLEXITY
# O(n) -- for the traversal array and the visited array
def bfs(g, start, visited, traversal):
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

# PURPOSE
# Perform a breadth-first search of a given directed graph in adjacency list
# format. Be sure to traverse all vertices by looping over all possible
# starting points. Return a list containing the node labels in order of
# traversal.
# SIGNATURE
# bfs_all :: Digraph => List
# TIME COMPLEXITY
# O(n + m) -- loop over very node and every edge
# SPACE COMPLEXITY
# O(n) -- for the visited and traversal arrays.
def bfs_all(g):
    traversal = []
    visited = set({})
    for start in g.graph.keys():
        if start not in visited:
            bfs(g, start, visited, traversal)
    return traversal
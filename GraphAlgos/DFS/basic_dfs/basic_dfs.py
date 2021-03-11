# Heather Fryling
# 3/10/2021

from collections import deque
from digraph import *

# PURPOSE
# Traverse a graph in a depth-first manner and return the traversal.
# SIGNATURE
# dfs_recursive :: DiGraph, Integer => List
# TIME COMPLEXITY
# O(m) -- checking each edge in the traversal.
# SPACE COMPLEXITY
# O(n) -- the traversal list has an entry for each vertex, as does visited.
def dfs_recursive(g, start):
    traversal = []
    visited = set({})
    dfs_helper(g, start, visited, traversal)
    return traversal

# PURPOSE
# Helper method for dfs implemented recursively.
# SIGNATURE
# dfs_helper :: DiGraph, Integer, Set, List => None
def dfs_helper(g, vertex, visited, traversal):
    visited.add(vertex)
    traversal.append(vertex)
    for u in g.graph[vertex]:
        if u not in visited:
            dfs_helper(g, u, visited, traversal)

# PURPOSE
# Traverse a graph in a depth-first manner and return the traversal.
# SIGNATURE
# dfs_recursive :: DiGraph, Integer => List
# TIME COMPLEXITY
# O(m) -- checking each edge in the traversal.
# SPACE COMPLEXITY
# O(n) -- the traversal list has an entry for each vertex.
def dfs_iterative(g, start):
    traversal = []
    visited = set({})
    stack = deque()
    stack.append(start)
    visited.add(start)
    while stack:
        v = stack.pop()
        traversal.append(v)
        for u in g.graph[v]:
            if u not in visited:
                visited.add(u)
                stack.append(u)
    return traversal
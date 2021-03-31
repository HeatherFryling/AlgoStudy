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

# PURPOSE
# Traverse all edges of a digraph in adjacency list representation via DFS and
# return the traversal.
# SIGNATURE
# dfs_all : DiGraph => List
# TIME COMPLEXITY
# O(m + n) -- checks all edges and all vertices once.
# SPACE COMPLEXITY
# O(n) -- an entry for each vertex in visited and traversal.
def dfs_all(g):
    traversal = []
    visited = set({})
    for u in g.graph.keys():
        if u not in visited:
            dfs_helper(g, u, visited, traversal)
    return traversal

g = DiGraph()
g.add_edge('A', 'B')
g.add_edge('A', 'E')
g.add_edge('B', 'C')
g.add_edge('B', 'E')
g.add_edge('C', 'F')
g.add_edge('C', 'B')
g.add_edge('D', 'G')
g.add_edge('D', 'H')
g.add_edge('E', 'F')
g.add_edge('E', 'B')
g.add_edge('F', 'I')
g.add_edge('F', 'E')
g.add_edge('G', 'H')
g.add_edge('G', 'D')
g.add_edge('H', 'D')
g.add_edge('H', 'G')
print(dfs_all(g))
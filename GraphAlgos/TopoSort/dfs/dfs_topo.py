# Heather Fryling
# 3/11/2021

from digraph import DiGraph

# PURPOSE
# Given a starting node, use dfs to construct a topological sort in 
# reverse order.
# SIGNATURE
# dfs_topo :: DiGraph, Integer, Set, List => None
def dfs_topo(g, u, visited, topo_sorted):
    visited.add(u)
    for v in g.graph[u]:
        if v not in visited:
            dfs_topo(g, v, visited, topo_sorted)
    topo_sorted.append(u)

# PURPOSE
# Given a DiGraph, construct and return a topological sort using dfs.
# SIGNATURE
# dfs_topo_all :: DiGraph => List
# TIME COMPLEXITY
# O(m + n) -- outer loop loops over all nodes, recursion checks all edges
# SPACE COMPLEXITY
# O(n) -- visited and topo_sorted have an entry for each node.
def dfs_topo_all(g):
    visited = set({})
    topo_sorted = []
    for u in g.graph.keys():
        if u not in visited:
            dfs_topo(g, u, visited, topo_sorted)
    topo_sorted.reverse()
    return topo_sorted
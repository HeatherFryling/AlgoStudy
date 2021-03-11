# Heather Fryling
# 3/11/2021

from collections import deque
from digraph import DiGraph

# PURPOSE
# Helper function to calculate the in-degree of all vertices in a directed
# graph in adjacency list format.
# SIGNATURE
# calc_in_degree: Digraph => Dictionary
def calc_in_degree(g):
    in_degree = {}
    for u in g.graph.keys():
        in_degree[u] = 0
    for u in g.graph.keys():
        for v in g.graph[u]:
            in_degree[v] = in_degree[v] + 1
    return in_degree

# PURPOSE
# Used bfs to calculate a topological ordering of a digraph, g.
# SIGNATURE
# bfs_topo :: DiGraph => List
# TIME COMPLEXITY
# O(n + m) -- checks every node and every edge.
# SPACE COMPLEXITY
# O(n) -- for topo_sorted and in_degree.
def bfs_topo(g):
    in_degree = calc_in_degree(g)
    topo_sorted = []
    q = deque()
    for u in g.graph.keys():
        if in_degree[u] == 0:
            q.append(u)
    while(q):
        u = q.popleft()
        topo_sorted.append(u)
        for v in g.graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)
    return topo_sorted

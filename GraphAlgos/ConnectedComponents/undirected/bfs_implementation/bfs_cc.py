# Heather Fryling
# 3/10/2021

from collections import deque
from graph import *

# PURPOSE
# Starting from vertex u, perform a bfs, labeling each vertex reachable from
# u with cc_num.
# SIGNATURE
# bfs_cc :: Graph, Integer, Set, Dictionary, Integer => None
def bfs_cc(g, u, visited, cc, cc_num):
    q = deque()
    q.append(u)
    visited.add(u)
    cc[u] = cc_num
    while q:
        v = q.popleft()
        for w in g.graph[v]:
            if w not in visited:
                q.append(w)
                visited.add(w)
                cc[w] = cc_num

# PURPOSE
# Calculate the connected component of each vertex in an undirected graph
# using breadth-first search.
# SIGNATURE
# bfs_cc_all :: Graph => Dictionary
# TIME COMPLEXITY
# O(m + n)
# SPACE COMPLEXITY
# O(n)
def bfs_cc_all(g):
    visited = set({})
    cc = {}
    cc_num = 1
    for u in g.graph.keys():
        if u not in visited:
            bfs_cc(g, u, visited, cc, cc_num)
            cc_num += 1
    return cc




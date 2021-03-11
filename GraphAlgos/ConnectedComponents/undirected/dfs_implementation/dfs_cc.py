# Heather Fryling
# 3/10/2021

from graph import *

# PURPOSE
# Using dfs, calculate all members of connected component cc_num in given a
# starting vertex, u, a set of previously visited vertices, a dictionary to
# store the cc_num, and the cc_num.
# SIGNATURE
# dfs_cc : Graph, Integer, Set, Dictionary, Integer => None
def dfs_cc(g, u, visited, cc, cc_num):
    visited.add(u)
    cc[u] = cc_num
    for v in g.graph[u]:
        if v not in visited:
            dfs_cc(g, v, visited, cc, cc_num)

# PURPOSE
# Given an undirected graph, calculate all its connected components and return
# a dictionary mapping each vertex to its connected component number.
# SIGNATURE
# dfs_cc_all : Graph => Dictionary
# TIME COMPLEXITY
# O(n + m) -- checks every vertex and every edge.
# SPACE COMPLEXITY
# O(n) -- visited and cc structures have entries for each vertex.
def dfs_cc_all(g):
    visited = set({})
    cc = {}
    cc_num = 1
    for u in g.graph.keys():
        if u not in visited:
            dfs_cc(g, u, visited, cc, cc_num)
            cc_num += 1
    return cc



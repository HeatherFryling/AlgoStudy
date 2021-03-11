# Heather Fryling
# 3/10/2021

from digraph import *

COLORS = ["WHITE", "GREY", "BLACK"]

# PURPOSE
# Given a digraph, return True if it contains a cycle, false otherwise.
# SIGNATURE
# dfs_cycle_detection :: DiGraph => Boolean
# TIME COMPLEXITY
# O(m + n) -- checks all edges and all vertices.
# SPACE COMPLEXITY
# O(n) -- color dictionary with an entry for each vertex.
def dfs_cycle_detection(g):
    color = {}
    for vertex in g.graph.keys():
        color[vertex] = COLORS[0]
    for u in g.graph.keys():
        if color[u] == COLORS[0]:
            cycle_detected = dfs_cycle_helper(g, u, color)
            if cycle_detected:
                return True
    return False

# PURPOSE
# Helper method for dfs_cycle_detection for recursion.
# SIGNATURE
# dfs_cycle_helper :: DiGraph, Integer, List => Boolean
def dfs_cycle_helper(g, u, color):
    color[u] = COLORS[1]
    for v in g.graph[u]:
        if color[v] == COLORS[0]:
            if dfs_cycle_helper(g, v, color):
                # Cycle detected deeper into the graph.
                return True
        if color[v] == COLORS[1]:
            return True
    color[u] = COLORS[2]
    return False

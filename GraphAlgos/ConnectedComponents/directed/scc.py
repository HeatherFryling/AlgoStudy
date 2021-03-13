# Heather Fryling
# 3/12/2021

from digraph import DiGraph

# PURPOSE
# Create and return a reversed copy of the given DiGraph.
# SIGNATURE
# g_rev :: DiGraph => DiGraph
# TIME COMPLEXITY
# O(n + m) -- the loop covers all vertices and all edges.
# SPACE COMPLEXITY
# O(n + m) -- a second graph is allocated and returned.
def g_rev(g):
    rev = DiGraph()
    for u in g.graph.keys():
        for v in g.graph[u]:
            rev.add_edge(v, u)
    return rev

# PURPOSE
# Calculate a topological sort of the given Digraph, g.
# SIGNATURE
# dfs_rev_topo :: DiGraph => List
# TIME COMPLEXITY
# O(m + n)
# SPACE COMPLEXITY
# O(n)
def dfs_topo(g):
    topo = []
    visited = set({})
    for u in g.graph.keys():
        if u not in visited:
            topo_helper(g, u, topo, visited)
    topo.reverse()
    return topo

# PURPOSE
# Helper function for dfs_topo to update visited and topo in 
# recursive calls.
# SIGNATURE
# topo_helper :: DiGraph, Integer, List, Set => None
def topo_helper(g, u, topo, visited):
    visited.add(u)
    for v in g.graph[u]:
        if v not in visited:
            topo_helper(g, v, topo, visited)
    topo.append(u)

# PURPOSE
# Calculate the strongly connected components of a directed graph, g. Return
# a list of the sets that comprise the SCCs.
# SIGNATURE
# calculate_sccs : DiGraph => List[Set]
# TIME COMPLEXITY
# O(n + m) -- several loops over all edges and all vertices.
# SPACE COMPLEXITY
# O(n + m) -- we allocate an entire second graph.
def calculate_sccs(g):
    rev_g = g_rev(g)
    # The magical ordering that will make calculate SCCs one at a time,
    # starting with the sink scc and moving backward toward the source.
    # The source scc of g_rev is the sink scc of g. It is guaranteed to
    # be in the first position in the toposort of g_rev, and subsequent sccs
    # are guaranteed to be next, ignoring already visited vertices.
    magical_ordering = dfs_topo(rev_g)
    visited = set({})
    sccs = []
    for u in magical_ordering:
        if u not in visited:
            curr_scc = set({})
            dfs_scc(g, u, visited, curr_scc)
            sccs.append(curr_scc)
    return sccs

def dfs_scc(g, u, visited, curr_scc):
    visited.add(u)
    curr_scc.add(u)
    for v in g.graph[u]:
        if v not in visited:
            dfs_scc(g, v, visited, curr_scc)

g = DiGraph()
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 1)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(5, 4)
g.add_edge(4, 6)
g.add_edge(6, 7)
g.add_edge(6, 8)
g.add_edge(7, 8)
g.add_edge(8, 9)
g.add_edge(9, 6)

rev_g = DiGraph()
rev_g.add_edge(2, 1)
rev_g.add_edge(3, 2)
rev_g.add_edge(1, 3)
rev_g.add_edge(4, 3)
rev_g.add_edge(5, 4)
rev_g.add_edge(4, 5)
rev_g.add_edge(6, 4)
rev_g.add_edge(7, 6)
rev_g.add_edge(8, 6)
rev_g.add_edge(8, 7)
rev_g.add_edge(9, 8)
rev_g.add_edge(6, 9)

func_reversed = g_rev(g)

print(calculate_sccs(g))
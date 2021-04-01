# Heather Fryling
# 3/31/2021

from union_find import UnionFind
from graph import Graph

# PURPOSE
# Given a graph in adjacency list format, apply Kruskals algorithm to
# output the minimum spanning tree of the graph.
# SIGNATURE
# kruskals :: Graph, Dictionary => Set
# TIME COMPLEXITY
# O(mlogm) -- Running time is dominated by sorting the edges.
# SPACE COMPLEXITY
# O(m + n) -- for edges and mst and uf
def kruskals(g, weights):
    edges = list(weights.keys())
    edges.sort(key= lambda edge : weights[edge])
    mst = set({})
    uf = UnionFind(list(g.graph.keys()))
    for edge in edges:
        u = edge[0]
        v = edge[1]
        set_u = uf.find(u)
        set_v = uf.find(v)
        if set_u != set_v:
            mst.add(edge)
            uf.union(set_u, set_v)
    return mst

g1_custom = Graph()
g1_custom.add_edge(1, 2)
g1_custom.add_edge(1, 3)
g1_custom.add_edge(1, 4)
g1_custom.add_edge(2, 4)
g1_custom.add_edge(3, 4)

weights1_custom = {}
weights1_custom[(1, 2)] = 1
weights1_custom[(2, 1)] = 1
weights1_custom[(1, 3)] = 2
weights1_custom[(3, 1)] = 2
weights1_custom[(1, 4)] = 2
weights1_custom[(4, 1)] = 2
weights1_custom[(2, 4)] = 4
weights1_custom[(4, 2)] = 4
weights1_custom[(3, 4)] = 3
weights1_custom[(4, 3)] = 3

print(kruskals(g1_custom, weights1_custom))

g2_custom = Graph()
g2_custom.add_edge('a', 'b')
g2_custom.add_edge('a', 'c')
g2_custom.add_edge('a', 'd')
g2_custom.add_edge('b', 'd')
g2_custom.add_edge('c', 'd')

weights2_custom = {}
weights2_custom[('a', 'b')] = 1
weights2_custom[('b', 'a')] = 1
weights2_custom[('a', 'c')] = 4
weights2_custom[('c', 'a')] = 4
weights2_custom[('a', 'd')] = 3
weights2_custom[('d', 'a')] = 3
weights2_custom[('b', 'd')] = 2
weights2_custom[('d', 'b')] = 2
weights2_custom[('c', 'd')] = 5
weights2_custom[('d', 'c')] = 5

print(kruskals(g2_custom, weights2_custom))
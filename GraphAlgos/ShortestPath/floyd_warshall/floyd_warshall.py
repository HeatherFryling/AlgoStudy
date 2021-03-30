# Heather Fryling
# 3/30/2021

# PURPOSE
# Given a graph in adjacency matrix format, return a matrix of the lengths
# of all possible paths. Negative edge lengths are ok. Cycles are ok.
# Negative cycles are not.
# To detect negative cycles, we would need a 3d matrix and another check
# in the algorithm.
# SIGNATURE
# floyd_warshall :: Graph (adjacency matrix) => List[List]
# TIME COMPLEXITY
# O(n^3) -- triple for loop.
# SPACE COMPLEXITY
# O(n^2) -- distance matrix.
def floyd_warshall(g):
    n = len(g[0])
    dist = [row[:] for row in g]
    for k in range(n):
        for u in range(n):
            for v in range(n):
                dist[u][v] = min(dist[u][v], dist[u][k] + dist[k][v])
    return dist

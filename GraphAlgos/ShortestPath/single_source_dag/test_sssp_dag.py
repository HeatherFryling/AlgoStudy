from sssp_dag import *

def test_in_degree():
    g = DiGraph()
    g.add_edge(4, 2)
    g.add_edge(4, 1)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 5)
    g.add_edge(1, 5)
    ans = {4: 0, 2: 1, 1: 1, 3: 2, 5: 2}
    assert(ans == calc_in_degree(g))

def test_bfs_topo():
    g = DiGraph()
    g.add_edge(4, 2)
    g.add_edge(4, 1)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 5)
    g.add_edge(1, 5)
    ans1 = [4, 1, 2, 3, 5]
    ans2 = [4, 2, 1, 3, 5]
    assert(ans1 == bfs_topo(g) or ans2 == bfs_topo(g))

def test_sssp_dag():
    g = DiGraph()
    g.add_edge(4, 2)
    g.add_edge(4, 1)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 5)
    g.add_edge(1, 5)
    cost = {}
    cost[(4, 2)] = 1
    cost[(4, 1)] = 3
    cost[(1, 3)] = 1
    cost[(2, 3)] = 2
    cost[(3, 5)] = 4
    cost[(1, 5)] = 3

    ans1 = {4: float('inf'), 2: float('inf'), 1: 0, 3: 1, 5: 3}
    assert(ans1 == sssp_dag(g, 1, cost))
    ans2 = {4: float('inf'), 2: 0, 1: float('inf'), 3: 2, 5: 6}
    assert(ans2 == sssp_dag(g, 2, cost))
    ans3 = {4: float('inf'), 2: float('inf'), 1: float('inf'), 3: 0, 5: 4}
    assert(ans3 == sssp_dag(g, 3, cost))
    ans4 = {4: 0, 2: 1, 1: 3, 3: 3, 5: 6}
    assert(ans4 == sssp_dag(g, 4, cost))
    ans5 = {4: float('inf'), 2: float('inf'), 1: float('inf'), 3: float('inf'), 5: 0}
    assert(ans5 == sssp_dag(g, 5, cost))
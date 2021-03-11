from bfs_topo import *

def test_calc_in_degree():
    g = DiGraph()
    g.add_edge(2, 1)
    g.add_edge(2, 3)
    g.add_edge(1, 4)
    g.add_edge(3, 4)
    g.add_edge(3, 5)
    g.add_edge(4, 5)
    assert({2: 0, 1: 1, 3: 1, 4: 2, 5: 2} == calc_in_degree(g))

def test_bfs_topo():
    g = DiGraph()
    g.add_edge(2, 1)
    g.add_edge(2, 3)
    g.add_edge(1, 4)
    g.add_edge(3, 4)
    g.add_edge(3, 5)
    g.add_edge(4, 5)
    assert([2, 1, 3, 4, 5] == bfs_topo(g))
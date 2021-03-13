from scc import *

def test_rev_g():
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

    assert(rev_g == func_reversed)

def test_dfs_topo():
    g = DiGraph()
    g.add_edge(2, 1)
    g.add_edge(2, 3)
    g.add_edge(1, 4)
    g.add_edge(3, 4)
    g.add_edge(3, 5)
    g.add_edge(4, 5)
    assert([2, 3, 1, 4, 5] == dfs_topo(g))
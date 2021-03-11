from basic_dfs import *

def test_recursive():
    g = DiGraph()
    g.add_edge(1, 3)
    g.add_edge(1, 2)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    g.add_edge(3, 6)
    g.add_edge(4, 5)
    g.add_edge(5, 6)
    ans_rec = [1, 2, 4, 5, 6, 3]
    assert(ans_rec == dfs_recursive(g, 1))

def test_iterative():
    g = DiGraph()
    g.add_edge(1, 3)
    g.add_edge(1, 2)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    g.add_edge(3, 6)
    g.add_edge(4, 5)
    g.add_edge(5, 6)
    ans_it = [1, 3, 6, 4, 5, 2]
    assert(ans_it == dfs_iterative(g, 1))



from digraph import *

def test_add_edge():
    g = DiGraph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(4, 3)
    assert({2, 3} == g.graph[1])
    assert({3, 4} == g.graph[2])
    assert({3} == g.graph[4])
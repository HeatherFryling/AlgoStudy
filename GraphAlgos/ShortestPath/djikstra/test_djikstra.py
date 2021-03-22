from djikstra import *

def test_djikstra():
    g = DiGraph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 5)
    g.add_edge(4, 2)
    g.add_edge(4, 1)
    g.add_edge(4, 6)
    g.add_edge(5, 4)
    g.add_edge(5, 6)

    weights = {}
    weights[(1, 2)] = 3
    weights[(1, 3)] = 2
    weights[(2, 3)] = 1
    weights[(3, 5)] = 4
    weights[(4, 2)] = 2
    weights[(4, 1)] = 3
    weights[(4, 6)] = 7
    weights[(5, 4)] = 5
    weights[(5, 6)] = 1

    assert({1: 3, 2: 2, 3: 3, 5: 7, 4: 0, 6: 7} == djikstra(g, weights, 4))
from dfs_cycle_detection import *

def test_dfs_cycle_detection():
    has_cycle = DiGraph()
    has_cycle.add_edge(1, 2)
    has_cycle.add_edge(3, 4)
    has_cycle.add_edge(4, 5)
    has_cycle.add_edge(5, 3)
    assert(True == dfs_cycle_detection(has_cycle))

    no_cycle = DiGraph()
    no_cycle.add_edge(1, 2)
    no_cycle.add_edge(1, 3)
    no_cycle.add_edge(3, 4)
    no_cycle.add_edge(3, 5)
    assert(False == dfs_cycle_detection(no_cycle))
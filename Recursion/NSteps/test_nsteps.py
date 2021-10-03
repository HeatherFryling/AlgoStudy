from nsteps import *

def test_nsteps():
    assert([[]] == nsteps(0))
    assert([[0]] == nsteps(1))
    assert([[0, 1], [0]] == nsteps(2))
    assert([[0, 1, 2], [0, 1], [0, 2], [0]] == nsteps(3))
    assert([[0, 1, 2, 3], [0, 1, 2], [0, 1, 3], [0, 1], [0, 2, 3], [0, 2], [0, 3]] == nsteps(4))
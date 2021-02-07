from edit_distance import *

def test_edit_distance():
    # Testing with a deletion
    start1 = "hello"
    target1 = "hell"
    assert(1 == edit_distance(start1, target1))

    # Testing replacement
    start2 = "rabbit"
    target2 = "bunny"
    assert(6 == edit_distance(start2, target2))

    # Testing insert
    start3 = "bunny"
    target3 = "rabbit"
    assert(6 == edit_distance(start3, target3))

def test_edit_distance_top_down():
    # Testing with a deletion
    start1 = "hello"
    target1 = "hell"
    assert(1 == edit_distance_top_down(start1, target1))

    # Testing replacement
    start2 = "rabbit"
    target2 = "bunny"
    assert(6 == edit_distance_top_down(start2, target2))

    # Testing insert
    start3 = "bunny"
    target3 = "rabbit"
    assert(6 == edit_distance_top_down(start3, target3))
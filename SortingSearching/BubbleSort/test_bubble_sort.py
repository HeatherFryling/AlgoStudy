from bubble_sort import bubble_sort

def test_bubble_sort():
    test1 = [1, 2, 3, 4, 5]
    test2 = [5, 4, 3, 2, 1]
    test3 = [1, 3, 4, 2, 5]
    test4 = [1, 3, 4, 2, 5, 5]

    ans1 = sorted(test1)
    ans2 = sorted(test2)
    ans3 = sorted(test3)
    ans4 = sorted(test4)
    
    bubble_sort(test1)
    bubble_sort(test2)
    bubble_sort(test3)
    bubble_sort(test4)

    assert(ans1 == test1)
    assert(ans2 == test2)
    assert(ans3 == test3)
    assert(ans4 == test4)
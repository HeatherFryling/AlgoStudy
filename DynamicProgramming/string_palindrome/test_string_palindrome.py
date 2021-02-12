from string_palindrome import *

def test_is_palindrome_table():
    test1 = "banana"
    table1 = is_palindrome_table(test1)
    ans_table1 = [[True, False, False, False, False, False], [False, True, False, \
        True, False, True], [False, False, True, False, True, False], [False, \
            False, False, True, False, True], [False, False, False, False, True, \
                False], [False, False, False, False, False, True]]
    assert(ans_table1 == table1)

    test2 = "bath"
    table2 = is_palindrome_table(test2)
    ans_table2 = [[True, False, False, False], [False, True, False, \
        False], [False, False, True, False], [False, False, False, True]]
    assert(ans_table2 == table2)

    test3 = "anna"
    table3 = is_palindrome_table(test3)
    print_table(table3)
    ans_table3 = [[True, False, False, True], [False, True, True, False], \
        [False, False, True, False], [False, False, False, True]]
    assert(ans_table3 == table3)

def test_string_paldindrome_iterative():
    test1 = "banana"
    assert(2 == string_palindrome(test1))

    test2 = "bath"
    assert(4 == string_palindrome(test2))

    test3 = "anna"
    assert(1 == string_palindrome(test3))

def test_string_paldindrome_recursive():
    test1 = "banana"
    assert(2 == string_pal_top_down(test1))

    test2 = "bath"
    assert(4 == string_pal_top_down(test2))

    test3 = "anna"
    assert(1 == string_pal_top_down(test3))
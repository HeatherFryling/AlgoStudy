from all_substrings import *

def test_all_substrings():
    s = "Hello"
    ans = ['H', 'He', 'Hel', 'Hell', 'Hello', 'e', 
           'el', 'ell', 'ello', 'l', 'll', 'llo', 
           'l', 'lo', 'o']
    assert(ans == all_substrings(s))

def test_all_recursive_substrings():
    s = "Hello"
    ans = ['H', 'He', 'Hel', 'Hell', 'Hello', 'e', 
           'el', 'ell', 'ello', 'l', 'll', 'llo', 
           'l', 'lo', 'o']
    assert(ans == all_recursive_substrings(s))
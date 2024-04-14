"""
Given a positive integer n, you have to make a pile of n levels of stones.
The first level has n stones.
The number of stones in the next level is:
- the next odd number if n is odd.
- the next even number if n is even.
Return the number of stones in each level in a list, where element at index
i represents the number of stones in the level (i+1).

Examples:
>>> make_a_pile(3)
[3, 5, 7]
"""

def make_a_pile(n):
    return [n + 2*i for i in range(n)]

def test_make_a_pile(): # pragma: no cover
    global make_a_pile
    assert make_a_pile(0) == [], "Test case 1 failed"
    assert make_a_pile(1) == [1], "Test case 2 failed"
    assert make_a_pile(5) == [5, 7, 9, 11, 13], "Test case 3 failed"
if __name__ == "__main__": # pragma: no cover
    test_make_a_pile()

"""
You are given an array arr of integers and you need to return
sum of magnitudes of integers multiplied by product of all signs
of each number in the array, represented by 1, -1 or 0.
Note: return None for empty arr.

Example:
>>> prod_signs([1, 2, 2, -4]) == -9
>>> prod_signs([0, 1]) == 0
>>> prod_signs([]) == None
"""

def prod_signs(arr):
    if not arr: return None
    prod = 0 if 0 in arr else (-1) ** len(list(filter(lambda x: x < 0, arr)))
    return prod * sum([abs(i) for i in arr])

def test_prod_signs(): # pragma: no cover
    global prod_signs

    assert prod_signs([1, 2, 2, -4]) == -9, "Test case 1 failed"
    assert prod_signs([0, 1]) == 0, "Test case 2 failed"
    assert prod_signs([]) == None, "Test case 3 failed"
    assert prod_signs([-2, -3]) == 5, "Test case 4 failed"
    assert prod_signs([5, 5, 5, 5, 5]) == 25, "Test case 5 failed"
    assert prod_signs([-1, -1, -1, -1]) == 4, "Test case 6 failed"

if __name__ == "__main__": # pragma: no cover
    test_prod_signs()

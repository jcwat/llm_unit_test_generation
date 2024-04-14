"""Given a non-empty list of integers lst. add the even elements that are at odd indices..


Examples:
add([4, 2, 6, 7]) ==> 2 
"""

def add(lst):
    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i]%2 == 0])

def test_add(): # pragma: no cover
    global add
    assert add([4, 2, 6, 7]) == 2, "Test case 1 failed: add([4, 2, 6, 7]) should return 2"
    assert add([1, 3, 5]) == 0, "Test case 2 failed: add([1, 3, 5]) should return 0"
    assert add([0, 4, 2, 3, 5, 8, 10]) == 12, "Test case 3 failed: add([0, 4, 2, 3, 5, 8, 10]) should return 12"
    assert add([2]) == 0, "Test case 4 failed: add([2]) should return 0"
    assert approx_equal(add([3.5, 4.0, 2.5, 2.0]), 2.0), "Test case 5 failed: add([3.5, 4.0, 2.5, 2.0]) should return 2.0"

def approx_equal(a, b, tol=1e-5):
    return abs(a - b) < tol

if __name__ == "__main__": # pragma: no cover
    test_add()

"""Given a non-empty list of integers lst. add the even elements that are at odd indices..


Examples:
add([4, 2, 6, 7]) ==> 2 
"""

def add(lst):
    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i]%2 == 0])

def test_add(): # pragma: no cover
    global add
    assert add([4, 2, 6, 7]) == 2, "Test case 1 failed"
    assert add([1, 3, 5]) == 0, "Test case 2 failed"
    assert add([2, 4, 6, 8, 10]) == 12, "Test case 3 failed"
    assert add([-2, -4, -6, -8, -10]) == -12, "Test case 4 failed"
    assert add([0, 2, 4, 6, 8, 10]) == 6, "Test case 5 passed"
    assert abs(add([0.1, 2.00001, 4.00001, 6.00001, 8.00001, 10.00001]) - 12.00002) <= 1e-5, "Test case 6 failed"

if __name__ == "__main__": # pragma: no cover
    test_add()

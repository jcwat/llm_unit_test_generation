"""Given a non-empty list of integers lst. add the even elements that are at odd indices..


Examples:
add([4, 2, 6, 7]) ==> 2 
"""

def add(lst):
    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i]%2 == 0])

def test_add(): # pragma: no cover
    global add
    assert add([4, 2, 6, 7]) == 2, "Test case 1 failed"
    assert add([3, 5, 7, 9]) == 0, "Test case 2 failed"
    assert add([1, 2, 3, 4, 5, 6]) == 8, "Test case 3 failed"
    assert add([10, 20, 30, 40, 50]) == 60, "Test case 4 failed"

if __name__ == "__main__": # pragma: no cover
    test_add()

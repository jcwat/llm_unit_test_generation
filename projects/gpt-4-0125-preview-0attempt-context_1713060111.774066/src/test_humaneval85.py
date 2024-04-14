"""Given a non-empty list of integers lst. add the even elements that are at odd indices..


Examples:
add([4, 2, 6, 7]) ==> 2 
"""

def add(lst):
    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i]%2 == 0])

def test_add_even_elements_odd_indices(): # pragma: no cover
    global add
    assert add([4, 2, 6, 7]) == 2, "Test case 1 failed: Expected sum of even elements at odd indices to be 2"
    assert add([1, 3, 5]) == 0, "Test case 2 failed: Expected sum of even elements at odd indices to be 0 for all odd list"
    assert add([2, 4, 6, 8, 10]) == 12, "Test case 3 failed: Expected sum of even elements at odd indices to be 12"
    assert add([-2, 4, -6, 8, -10, 12]) == 12, "Test case 4 failed: Expected sum of even elements at odd indices to be 12 including negatives"
    assert add([0, 1, 0, 3, 0, 5, 0]) == 0, "Test case 5 failed: Expected sum of even elements at odd indices to be 0 including zeros"

if __name__ == "__main__": # pragma: no cover
    test_add_even_elements_odd_indices()

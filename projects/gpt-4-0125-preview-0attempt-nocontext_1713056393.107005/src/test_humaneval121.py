"""Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.


Examples
solution([5, 8, 7, 1]) ==> 12
solution([3, 3, 3, 3, 3]) ==> 9
solution([30, 13, 24, 321]) ==>0
"""

def solution(lst):
    return sum([x for idx, x in enumerate(lst) if idx%2==0 and x%2==1])

def test_solution(): # pragma: no cover
    global test_solution, solution
    assert solution([5, 8, 7, 1]) == 12, "Test case 1 failed"
    assert solution([3, 3, 3, 3, 3]) == 9, "Test case 2 failed"
    assert solution([30, 13, 24, 321]) == 0, "Test case 3 failed"
    assert solution([1, 2, 3, 4, 5, 6, 7]) == 16, "Test case 4 failed"
    assert solution([10, 21, 32, 43, 54, 65]) == 0, "Test case 5 failed"

if __name__ == "__main__": # pragma: no cover
    test_solution()

"""Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.


Examples
solution([5, 8, 7, 1]) ==> 12
solution([3, 3, 3, 3, 3]) ==> 9
solution([30, 13, 24, 321]) ==>0
"""

def solution(lst):
    return sum([x for idx, x in enumerate(lst) if idx%2==0 and x%2==1])

def test_solution(): # pragma: no cover
    global test_solution
    
    # Test case 1
    lst1 = [1, 2, 3, 4, 5]
    assert solution(lst1) == 6, "Test case 1 failed"
    
    # Test case 2
    lst2 = [2, 4, 6, 8, 10]
    assert solution(lst2) == 0, "Test case 2 failed"
    
    # Test case 3
    lst3 = [1, 3, 5, 7, 9]
    assert solution(lst3) == 25, "Test case 3 failed"

if __name__ == "__main__": # pragma: no cover
    test_solution()

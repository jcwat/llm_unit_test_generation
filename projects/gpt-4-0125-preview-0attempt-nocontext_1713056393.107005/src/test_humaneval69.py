'''
You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
zero, and has a frequency greater than or equal to the value of the integer itself. 
The frequency of an integer is the number of times it appears in the list.
If no such a value exist, return -1.
Examples:
search([4, 1, 2, 2, 3, 1]) == 2
search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
search([5, 5, 4, 4, 4]) == -1
'''

def search(lst):
    frq = [0] * (max(lst) + 1)
    for i in lst:
        frq[i] += 1;

    ans = -1
    for i in range(1, len(frq)):
        if frq[i] >= i:
            ans = i
    
    return ans

def test_search(): # pragma: no cover
    global search
    assert search([4, 1, 2, 2, 3, 1]) == 2, "Test case 1 failed"
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3, "Test case 2 failed"
    assert search([5, 5, 4, 4, 4]) == -1, "Test case 3 failed"
    assert search([1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4]) == 4, "Test case 4 failed"
    assert search([10, 10, 10, 10, 10]) == 10, "Test case 5 failed"
    assert search([1]) == 1, "Test case 6 failed"

if __name__ == "__main__": # pragma: no cover
    test_search()

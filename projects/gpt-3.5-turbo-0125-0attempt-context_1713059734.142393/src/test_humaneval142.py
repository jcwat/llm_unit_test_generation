""""
This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 

Examples:
For lst = [1,2,3] the output should be 6
For lst = []  the output should be 0
For lst = [-1,-5,2,-1,-5]  the output should be -126
"""



def sum_squares(lst):
    result =[]
    for i in range(len(lst)):
        if i %3 == 0:
            result.append(lst[i]**2)
        elif i % 4 == 0 and i%3 != 0:
            result.append(lst[i]**3)
        else:
            result.append(lst[i])
    return sum(result)

def test_sum_squares(): # pragma: no cover
    global math
    assert sum_squares([1, 2, 3]) == 6, "Test case 1 failed"
    assert sum_squares([]) == 0, "Test case 2 failed"
    assert sum_squares([-1, -5, 2, -1, -5]) == -126, "Test case 3 failed"
    assert sum_squares([3, 9, 2, 6, 12, 5, 1, 4]) == 504, "Test case 4 failed"

if __name__ == "__main__": # pragma: no cover
    test_sum_squares()

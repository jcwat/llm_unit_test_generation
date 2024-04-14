'''
Write a function that accepts two lists of strings and returns the list that has 
total number of chars in the all strings of the list less than the other list.

if the two lists have the same number of chars, return the first list.

Examples
total_match([], []) ➞ []
total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']
total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']
total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']
total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
'''

def total_match(lst1, lst2):
    l1 = 0
    for st in lst1:
        l1 += len(st)
    
    l2 = 0
    for st in lst2:
        l2 += len(st)
    
    if l1 <= l2:
        return lst1
    else:
        return lst2

def test_total_match(): # pragma: no cover
    global total_match, math

    # Testing for total_match([], [])
    assert total_match([], []) == [], "Test case 1 failed"

    # Testing for total_match(['hi', 'admin'], ['hI', 'Hi'])
    assert total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi'], "Test case 2 failed"

    # Testing for total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project'])
    assert total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin'], "Test case 3 failed"

    # Testing for total_match(['hi', 'admin'], ['hI', 'hi', 'hi'])
    assert total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi'], "Test case 4 failed"

    # Testing for total_match(['4'], ['1', '2', '3', '4', '5'])
    assert total_match(['4'], ['1', '2', '3', '4', '5']) == ['4'], "Test case 5 failed"

if __name__ == "__main__": # pragma: no cover
    test_total_match()

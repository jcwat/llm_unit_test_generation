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
    global total_match

    # Test case 1: sum of lengths of lst1 is less than or equal to sum of lengths of lst2
    lst1 = ['apple', 'banana', 'cherry']
    lst2 = ['orange', 'strawberry']
    assert total_match(lst1, lst2) == lst1, "Test case 1 failed"

    # Test case 2: sum of lengths of lst1 is greater than sum of lengths of lst2
    lst1 = ['apple', 'banana']
    lst2 = ['orange', 'strawberry', 'kiwi']
    assert total_match(lst1, lst2) == lst2, "Test case 2 failed"

if __name__ == "__main__": # pragma: no cover
    test_total_match()

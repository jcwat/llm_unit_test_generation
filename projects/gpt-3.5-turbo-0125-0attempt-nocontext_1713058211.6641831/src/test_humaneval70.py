'''
Given list of integers, return list in strange order.
Strange sorting, is when you start with the minimum value,
then maximum of the remaining integers, then minimum and so on.

Examples:
strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
strange_sort_list([]) == []
'''

def strange_sort_list(lst):
    res, switch = [], True
    while lst:
        res.append(min(lst) if switch else max(lst))
        lst.remove(res[-1])
        switch = not switch
    return res

def test_strange_sort_list(): # pragma: no cover
    global strange_sort_list
    
    assert strange_sort_list([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 9, 1, 6, 2, 5, 3, 5, 4, 5, 3], "Test case 1 failed"
    assert strange_sort_list([8, 6, 7, 5, 3, 0, 9]) == [0, 9, 3, 8, 5, 7, 6], "Test case 2 failed"
    assert strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3], "Test case 3 failed"

if __name__ == "__main__": # pragma: no cover
    test_strange_sort_list()

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
    assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3], "Test case 1 failed"
    assert strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5], "Test case 2 failed"
    assert strange_sort_list([]) == [], "Test case 3 failed"
    assert strange_sort_list([10, 2, 7, 3]) == [2, 10, 3, 7], "Test case 4 failed"
    assert strange_sort_list([1]) == [1], "Test case 5 failed"

if __name__ == "__main__": # pragma: no cover
    test_strange_sort_list()

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

    # Test empty list
    assert strange_sort_list([]) == [], "Failed on empty list case"

    # Test list with all elements the same
    assert strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5], "Failed on all elements the same case"

    # Test normal list
    assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3], "Failed on normal list case"

    # Test list with negative numbers
    assert strange_sort_list([-3, 0, 10, -5, 7]) == [-5, 10, -3, 7, 0], "Failed on list with negative numbers case"

if __name__ == "__main__": # pragma: no cover
    test_strange_sort_list()

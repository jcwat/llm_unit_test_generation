"""
You are given a 2 dimensional data, as a nested lists,
which is similar to matrix, however, unlike matrices,
each row may contain a different number of columns.
Given lst, and integer x, find integers x in the list,
and return list of tuples, [(x1, y1), (x2, y2) ...] such that
each tuple is a coordinate - (row, columns), starting with 0.
Sort coordinates initially by rows in ascending order.
Also, sort coordinates of the row by columns in descending order.

Examples:
get_row([
  [1,2,3,4,5,6],
  [1,2,3,4,1,6],
  [1,2,3,4,5,1]
], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
get_row([], 1) == []
get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]
"""

def get_row(lst, x):
    coords = [(i, j) for i in range(len(lst)) for j in range(len(lst[i])) if lst[i][j] == x]
    return sorted(sorted(coords, key=lambda x: x[1], reverse=True), key=lambda x: x[0])

def test_get_row(): # pragma: no cover
    global test_get_row

    lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert get_row(lst, 5) == [(1, 1)], "Test case 1 failed"

    lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert get_row(lst, 3) == [(0, 2)], "Test case 2 failed"

    lst = [[1, 2, 3], [4, 5, 3], [7, 8, 9]]
    assert get_row(lst, 3) == [(1, 2), (0, 2)], "Test case 3 failed"
    
if __name__ == "__main__": # pragma: no cover
    test_get_row()

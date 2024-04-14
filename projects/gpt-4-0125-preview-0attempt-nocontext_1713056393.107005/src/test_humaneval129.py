"""
Given a grid with N rows and N columns (N >= 2) and a positive integer k, 
each cell of the grid contains a value. Every integer in the range [1, N * N]
inclusive appears exactly once on the cells of the grid.

You have to find the minimum path of length k in the grid. You can start
from any cell, and in each step you can move to any of the neighbor cells,
in other words, you can go to cells which share an edge with you current
cell.
Please note that a path of length k means visiting exactly k cells (not
necessarily distinct).
You CANNOT go off the grid.
A path A (of length k) is considered less than a path B (of length k) if
after making the ordered lists of the values on the cells that A and B go
through (let's call them lst_A and lst_B), lst_A is lexicographically less
than lst_B, in other words, there exist an integer index i (1 <= i <= k)
such that lst_A[i] < lst_B[i] and for any j (1 <= j < i) we have
lst_A[j] = lst_B[j].
It is guaranteed that the answer is unique.
Return an ordered list of the values on the cells that the minimum path go through.

Examples:

Input: grid = [ [1,2,3], [4,5,6], [7,8,9]], k = 3
Output: [1, 2, 1]

Input: grid = [ [5,9,3], [4,1,6], [7,8,2]], k = 1
Output: [1]
"""

def minPath(grid, k):
    n = len(grid)
    val = n * n + 1
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                temp = []
                if i != 0:
                    temp.append(grid[i - 1][j])

                if j != 0:
                    temp.append(grid[i][j - 1])

                if i != n - 1:
                    temp.append(grid[i + 1][j])

                if j != n - 1:
                    temp.append(grid[i][j + 1])

                val = min(temp)

    ans = []
    for i in range(k):
        if i % 2 == 0:
            ans.append(1)
        else:
            ans.append(val)
    return ans

def test_minPath(): # pragma: no cover
    global minPath

    # Test case 1
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 3
    expected = [1, 2, 1]
    assert minPath(grid, k) == expected, "Test case 1 failed"

    # Test case 2
    grid = [[5, 9, 3], [4, 1, 6], [7, 8, 2]]
    k = 1
    expected = [1]
    assert minPath(grid, k) == expected, "Test case 2 failed"

    # Test case 3
    grid = [[10, 12, 5], [15, 11, 8], [9, 14, 6]]
    k = 2
    expected = [5, 6]
    assert minPath(grid, k) == expected, "Test case 3 failed"

    # Test case 4
    grid = [[3, 1], [4, 2]]
    k = 4
    expected = [1, 2, 1, 2]
    assert minPath(grid, k) == expected, "Test case 4 failed"

if __name__ == "__main__": # pragma: no cover
    test_minPath()

import math
"""
You are given a rectangular grid of wells. Each row represents a single well,
and each 1 in a row represents a single unit of water.
Each well has a corresponding bucket that can be used to extract water from it, 
and all buckets have the same capacity.
Your task is to use the buckets to empty the wells.
Output the number of times you need to lower the buckets.

Example 1:
Input: 
grid : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
bucket_capacity : 1
Output: 6

Example 2:
Input: 
grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
bucket_capacity : 2
Output: 5

Example 3:
Input: 
grid : [[0,0,0], [0,0,0]]
bucket_capacity : 5
Output: 0

Constraints:
* all wells have the same length
* 1 <= grid.length <= 10^2
* 1 <= grid[:,1].length <= 10^2
* grid[i][j] -> 0 | 1
* 1 <= capacity <= 10
"""

def max_fill(grid, capacity):
    return sum([math.ceil(sum(arr)/capacity) for arr in grid])

def test_max_fill(): # pragma: no cover
    global test_max_fill, math
    assert max_fill([[1, 2, 3], [4, 5, 6]], 3) == 4, "Test case 1 failed"
    assert max_fill([[1, 1, 1], [2, 2, 2], [3, 3, 3]], 2) == 3, "Test case 2 failed"
    assert max_fill([[1, 3, 5], [2, 4, 6]], 5) == 2, "Test case 3 failed"
if __name__ == "__main__": # pragma: no cover
    test_max_fill()

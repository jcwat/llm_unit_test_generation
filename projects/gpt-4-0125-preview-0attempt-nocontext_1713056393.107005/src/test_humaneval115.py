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
    global test_max_fill, math, max_fill
    # Example 1
    grid1 = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
    capacity1 = 1
    expected1 = 6
    assert math.isclose(max_fill(grid1, capacity1), expected1, rel_tol=1e-5), f"Test case 1 failed: expected {expected1}, got {max_fill(grid1, capacity1)}"
    
    # Example 2
    grid2 = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
    capacity2 = 2
    expected2 = 5
    assert math.isclose(max_fill(grid2, capacity2), expected2, rel_tol=1e-5), f"Test case 2 failed: expected {expected2}, got {max_fill(grid2, capacity2)}"
    
    # Example 3
    grid3 = [[0,0,0], [0,0,0]]
    capacity3 = 5
    expected3 = 0
    assert math.isclose(max_fill(grid3, capacity3), expected3, rel_tol=1e-5), f"Test case 3 failed: expected {expected3}, got {max_fill(grid3, capacity3)}"

if __name__ == "__main__": # pragma: no cover
    test_max_fill()

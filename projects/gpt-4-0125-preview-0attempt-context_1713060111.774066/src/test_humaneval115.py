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
    global max_fill, math
    # Test case 1
    grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
    capacity = 1
    assert max_fill(grid, capacity) == 6, "Test case 1 failed"

    # Test case 2
    grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
    capacity = 2
    assert max_fill(grid, capacity) == 5, "Test case 2 failed"

    # Test case 3
    grid = [[0,0,0], [0,0,0]]
    capacity = 5
    assert max_fill(grid, capacity) == 0, "Test case 3 failed"

    # Test with larger numbers and decimals
    grid = [[1,1,1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1,1,1]]
    capacity = 3
    assert abs(max_fill(grid, capacity) - 7) <= 1e-5, "Test case with large numbers and decimals failed"

if __name__ == "__main__": # pragma: no cover
    test_max_fill()

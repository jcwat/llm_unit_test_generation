"""
"Given an array representing a branch of a tree that has non-negative integer nodes
your task is to pluck one of the nodes and return it.
The plucked node should be the node with the smallest even value.
If multiple nodes with the same smallest even value are found return the node that has smallest index.

The plucked node should be returned in a list, [ smalest_value, its index ],
If there are no even values or the given array is empty, return [].

Example 1:
Input: [4,2,3]
Output: [2, 1]
Explanation: 2 has the smallest even value, and 2 has the smallest index.

Example 2:
Input: [1,2,3]
Output: [2, 1]
Explanation: 2 has the smallest even value, and 2 has the smallest index. 

Example 3:
Input: []
Output: []

Example 4:
Input: [5, 0, 3, 0, 4, 2]
Output: [0, 1]
Explanation: 0 is the smallest value, but  there are two zeros,
 so we will choose the first zero, which has the smallest index.

Constraints:
* 1 <= nodes.length <= 10000
* 0 <= node.value
"""

def pluck(arr):
    if(len(arr) == 0): return []
    evens = list(filter(lambda x: x%2 == 0, arr))
    if(evens == []): return []
    return [min(evens), arr.index(min(evens))]

def test_pluck(): # pragma: no cover
    global pluck

    # Test empty input
    assert pluck([]) == [], "Test case 1 failed"

    # Test input with no even numbers
    assert pluck([1, 3, 5, 7]) == [], "Test case 2 failed"

    # Test input with even numbers
    assert pluck([2, 8, 4, 6, 1, 7]) == [2, 0], "Test case 3 failed"
    assert pluck([3, 4, 7, 10, 2]) == [2, 4], "Test case 4 failed"
if __name__ == "__main__": # pragma: no cover
    test_pluck()

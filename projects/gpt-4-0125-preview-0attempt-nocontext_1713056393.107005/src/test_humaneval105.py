"""
Given an array of integers, sort the integers that are between 1 and 9 inclusive,
reverse the resulting array, and then replace each digit by its corresponding name from
"One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

For example:
  arr = [2, 1, 1, 4, 5, 8, 2, 3]   
-> sort arr -> [1, 1, 2, 2, 3, 4, 5, 8] 
-> reverse arr -> [8, 5, 4, 3, 2, 2, 1, 1]
  return ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]

  If the array is empty, return an empty array:
  arr = []
  return []

  If the array has any strange number ignore it:
  arr = [1, -1 , 55] 
-> sort arr -> [-1, 1, 55]
-> reverse arr -> [55, 1, -1]
  return = ['One']
"""

def by_length(arr):
    dic = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }
    sorted_arr = sorted(arr, reverse=True)
    new_arr = []
    for var in sorted_arr:
        try:
            new_arr.append(dic[var])
        except:
            pass
    return new_arr

def test_by_length(): # pragma: no cover
    global test_by_length
    
    # Test case 1
    arr = [2, 1, 1, 4, 5, 8, 2, 3]
    expected = ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
    result = by_length(arr)
    assert result == expected, f"Test case 1 failed: expected {expected}, got {result}"
    
    # Test case 2
    arr = []
    expected = []
    result = by_length(arr)
    assert result == expected, f"Test case 2 failed: expected {expected}, got {result}"
    
    # Test case 3
    arr = [1, -1 , 55]
    expected = ['One']
    result = by_length(arr)
    assert result == expected, f"Test case 3 failed: expected {expected}, got {result}"
    
    # Test case 4 - including numbers outside the 1-9 range to confirm they are ignored
    arr = [10, 0, 11, 8, 3]
    expected = ["Eight", "Three"]
    result = by_length(arr)
    assert result == expected, f"Test case 4 failed: expected {expected}, got {result}"
    
    # Test case 5 - single number in range
    arr = [5]
    expected = ["Five"]
    result = by_length(arr)
    assert result == expected, f"Test case 5 failed: expected {expected}, got {result}"

if __name__ == "__main__": # pragma: no cover
    test_by_length()

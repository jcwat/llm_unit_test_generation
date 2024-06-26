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
    global by_length

    input_arr = [4, 2, 7, 5, 3, 10]
    expected_output = ["Seven", "Five", "Four", "Three", "Two"]
    assert by_length(input_arr) == expected_output, "Test case 1 failed"

    input_arr = [6, 2, 3, 9, 5, 7]
    expected_output = ["Nine", "Seven", "Six", "Five", "Three", "Two"]
    assert by_length(input_arr) == expected_output, "Test case 2 failed"

    input_arr = [1, 2, 3, 4, 5, 6]
    expected_output = ["Six", "Five", "Four", "Three", "Two", "One"]
    assert by_length(input_arr) == expected_output, "Test case 3 failed"

if __name__ == "__main__": # pragma: no cover
    test_by_length()

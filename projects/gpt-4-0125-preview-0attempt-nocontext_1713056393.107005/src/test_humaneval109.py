"""We have an array 'arr' of N integers arr[1], arr[2], ..., arr[N].The
numbers in the array will be randomly ordered. Your task is to determine if
it is possible to get an array sorted in non-decreasing order by performing 
the following operation on the given array:
You are allowed to perform right shift operation any number of times.

One right shift operation means shifting all elements of the array by one
position in the right direction. The last element of the array will be moved to
the starting position in the array i.e. 0th index. 

If it is possible to obtain the sorted array by performing the above operation
then return True else return False.
If the given array is empty then return True.

Note: The given list is guaranteed to have unique elements.

For Example:

move_one_ball([3, 4, 5, 1, 2])==>True
Explanation: By performin 2 right shift operations, non-decreasing order can
 be achieved for the given array.
move_one_ball([3, 5, 4, 1, 2])==>False
Explanation:It is not possible to get non-decreasing order for the given
array by performing any number of right shift operations.

"""

def move_one_ball(arr):
    if len(arr)==0:
      return True
    sorted_array=sorted(arr)
    my_arr=[]
    
    min_value=min(arr)
    min_index=arr.index(min_value)
    my_arr=arr[min_index:]+arr[0:min_index]
    for i in range(len(arr)):
      if my_arr[i]!=sorted_array[i]:
        return False
    return True

def test_move_one_ball(): # pragma: no cover
    global move_one_ball
    # Test case: Expected True
    assert move_one_ball([3, 4, 5, 1, 2]) == True, "Test case 1 failed"
    # Test case: Expected False
    assert move_one_ball([3, 5, 4, 1, 2]) == False, "Test case 2 failed"
    # Test case: Expected True for already sorted array
    assert move_one_ball([1, 2, 3, 4, 5]) == True, "Test case 3 failed"
    # Test case: Expected True for empty array
    assert move_one_ball([]) == True, "Test case 4 failed"
    # Test case: Expected True for single element array
    assert move_one_ball([1]) == True, "Test case 5 failed"
    # Test case: Expected True when only one right shift is needed
    assert move_one_ball([5, 1, 2, 3, 4]) == True, "Test case 6 failed"

if __name__ == "__main__": # pragma: no cover
    test_move_one_ball()

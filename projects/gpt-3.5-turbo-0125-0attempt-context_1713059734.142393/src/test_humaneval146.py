"""Write a function that takes an array of numbers as input and returns 
the number of elements in the array that are greater than 10 and both 
first and last digits of a number are odd (1, 3, 5, 7, 9).
For example:
specialFilter([15, -73, 14, -15]) => 1 
specialFilter([33, -2, -3, 45, 21, 109]) => 2
"""

def specialFilter(nums):
    
    count = 0
    for num in nums:
        if num > 10:
            odd_digits = (1, 3, 5, 7, 9)
            number_as_string = str(num)
            if int(number_as_string[0]) in odd_digits and int(number_as_string[-1]) in odd_digits:
                count += 1
        
    return count 

def test_specialFilter(): # pragma: no cover
    global specialFilter

    assert specialFilter([15, -73, 14, -15]) == 1, "Test case 1 failed"
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2, "Test case 2 failed"
    assert specialFilter([12, 14, 16, 18, 20]) == 0, "Test case 3 failed"
    assert specialFilter([-33, -25, -19, 33, 57]) == 2, "Test case 4 failed"

if __name__ == "__main__": # pragma: no cover
    test_specialFilter()

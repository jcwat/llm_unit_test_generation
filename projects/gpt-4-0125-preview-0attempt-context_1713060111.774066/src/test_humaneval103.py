"""You are given two positive integers n and m, and your task is to compute the
average of the integers from n through m (including n and m). 
Round the answer to the nearest integer and convert that to binary.
If n is greater than m, return -1.
Example:
rounded_avg(1, 5) => "0b11"
rounded_avg(7, 5) => -1
rounded_avg(10, 20) => "0b1111"
rounded_avg(20, 33) => "0b11010"
"""

def rounded_avg(n, m):
    if m < n:
        return -1
    summation = 0
    for i in range(n, m+1):
        summation += i
    return bin(round(summation/(m - n + 1)))

def test_rounded_avg(): # pragma: no cover
    global test_rounded_avg, round, bin
    
    assert rounded_avg(1, 5) == bin(round(15/5)), "Test case 1 failed" 
    assert rounded_avg(7, 5) == -1, "Test case 2 failed"  
    assert rounded_avg(10, 20) == bin(round(165/11)), "Test case 3 failed"  
    assert rounded_avg(20, 33) == bin(round(438/14)), "Test case 4 failed" 
    assert rounded_avg(100, 100) == bin(100), "Test case 5 failed" 

if __name__ == "__main__": # pragma: no cover
    test_rounded_avg()

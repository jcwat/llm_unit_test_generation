"""
Given a positive integer n, return a sorted list that has the odd numbers in collatz sequence.

The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined
as follows: start with any positive integer n. Then each term is obtained from the 
previous term as follows: if the previous term is even, the next term is one half of 
the previous term. If the previous term is odd, the next term is 3 times the previous
term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

Note: 
1. Collatz(1) is [1].
2. returned list sorted in increasing order.

For example:
get_odd_collatz(5) returns [1, 5] # The collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the odd numbers are only 1, and 5.
"""

def get_odd_collatz(n):
    if n%2==0:
        odd_collatz = [] 
    else:
        odd_collatz = [n]
    while n > 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = n*3 + 1
            
        if n%2 == 1:
            odd_collatz.append(int(n))

    return sorted(odd_collatz)

def test_get_odd_collatz(): # pragma: no cover
    global get_odd_collatz
    assert get_odd_collatz(1) == [1], "Test case 1 failed"
    assert get_odd_collatz(5) == [1, 5], "Test case 2 failed"
    assert sorted(get_odd_collatz(6)) == [1, 3, 19], "Test case 3 failed"
    assert get_odd_collatz(7) == [1, 5, 7, 11, 13, 17, 21, 23], "Test case 4 failed"
    assert get_odd_collatz(10) == [1, 3, 5, 7, 13, 21], "Test case 5 failed" 
    assert get_odd_collatz(22) == [1, 3, 5, 7, 11, 13, 17, 21, 33, 35, 43], "Test case 6 failed"
    assert get_odd_collatz(11) == [1, 3, 5, 7, 11, 17, 21, 27, 35], "Test case 7 failed"
    assert sorted(get_odd_collatz(6)) == [1, 3, 19], "Fix applied for test case 3"

if __name__ == "__main__": # pragma: no cover
    test_get_odd_collatz()

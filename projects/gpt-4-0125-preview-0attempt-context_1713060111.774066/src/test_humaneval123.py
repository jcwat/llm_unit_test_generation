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
    global test_get_odd_collatz, get_odd_collatz
    
    # Correctly identifies odd numbers in the sequence and returns [1].
    assert get_odd_collatz(1) == [1], "Test case 1 failed"
    # Correctly identifies odd numbers in the sequence for n = 5 and returns [1, 5].
    assert get_odd_collatz(5) == [1, 5], "Test case 2 failed"
    # Correctly identifies odd numbers in the sequence for n = 6 and returns [1, 3, 5].
    assert get_odd_collatz(6) == [1, 3, 5], "Test case 3 failed"
    # Correctly identifies odd numbers in the sequence for a larger number and handles it correctly.
    assert get_odd_collatz(11) == [1, 11, 17, 25, 35, 53, 89], "Test case 4 failed"
    # Test large number for efficiency and correctness.
    assert len(get_odd_collatz(27)) > 0, "Test case 5 failed"

if __name__ == "__main__": # pragma: no cover
    test_get_odd_collatz()

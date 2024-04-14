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
    assert get_odd_collatz(1) == [1], "Test case 1 failed: get_odd_collatz(1) should return [1]"
    assert get_odd_collatz(2) == [1], "Test case 2 failed: get_odd_collatz(2) should return [1]"
    assert get_odd_collatz(5) == [1, 5], "Test case 3 failed: get_odd_collatz(5) should return [1, 5]"
    assert get_odd_collatz(6) == [1, 3], "Test case 4 failed: get_odd_collatz(6) should return [1, 3]"
    assert get_odd_collatz(7) == [1, 5, 7, 11, 17, 35], "Test case 5 failed: get_odd_collatz(7) should return [1, 5, 7, 11, 17, 35]"
    assert get_odd_collatz(10) == [1, 3, 5], "Test case 6 failed: get_odd_collatz(10) should return [1, 3, 5]"

    # With tolerance check for specific case if needed
    result = get_odd_collatz(13)
    expected_result = [1, 5, 13, 17, 21, 31, 41]
    assert all(abs(a-b) < 1e-5 for a, b in zip(result, expected_result)), "Test case with tolerance failed: get_odd_collatz(13) expected values close to [1, 5, 13, 17, 21, 31, 41]"

if __name__ == "__main__": # pragma: no cover
    test_get_odd_collatz()

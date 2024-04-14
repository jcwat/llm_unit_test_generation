"""Given a positive integer N, return the total sum of its digits in binary.

Example
For N = 1000, the sum of digits will be 1 the output should be "1".
For N = 150, the sum of digits will be 6 the output should be "110".
For N = 147, the sum of digits will be 12 the output should be "1100".

Variables:
@N integer
 Constraints: 0 ≤ N ≤ 10000.
Output:
 a string of binary number
"""

def solve(N):
    return bin(sum(int(i) for i in str(N)))[2:]

def test_solve(): # pragma: no cover
    global solve
    assert solve(1000) == '1', "Test case 1 failed: solve(1000) should return '1'"
    assert solve(150) == '110', "Test case 2 failed: solve(150) should return '110'"
    assert solve(147) == '1100', "Test case 3 failed: solve(147) should return '1100'"
    assert solve(0) == '0', "Test case 4 failed: solve(0) should return '0'"
    assert solve(9) == '1001', "Test case 5 failed: solve(9) should return '1001'"

if __name__ == "__main__": # pragma: no cover
    test_solve()

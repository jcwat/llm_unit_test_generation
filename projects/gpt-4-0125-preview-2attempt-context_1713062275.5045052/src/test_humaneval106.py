""" Implement the function f that takes n as a parameter,
and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
or the sum of numbers from 1 to i otherwise.
i starts from 1.
the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
Example:
f(5) == [1, 2, 6, 24, 15]
"""

def f(n):
    ret = []
    for i in range(1,n+1):
        if i%2 == 0:
            x = 1
            for j in range(1,i+1): x *= j
            ret += [x]
        else:
            x = 0
            for j in range(1,i+1): x += j
            ret += [x]
    return ret

def test_f(): # pragma: no cover
    global test_f
    assert f(5) == [1, 2, 6, 24, 15], "Test case 1 failed"
    assert f(0) == [], "Test case 2 failed"
    assert f(1) == [1], "Test case 3 failed"
    assert f(3) == [1, 2, 6], "Test case 4 failed"
    result = f(10)
    expected = [1, 2, 6, 24, 15, 720, 21, 40320, 36, 362880]
    assert result == expected, "Test case 5 failed"

    # Floating point comparison with tolerance
    assert abs(f(2)[1] - 2) < 1e-5, "Test case 6 failed"

if __name__ == "__main__": # pragma: no cover
    test_f()

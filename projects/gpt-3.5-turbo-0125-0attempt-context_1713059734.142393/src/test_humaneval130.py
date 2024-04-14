"""Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
the last couple centuries. However, what people don't know is Tribonacci sequence.
Tribonacci sequence is defined by the recurrence:
tri(1) = 3
tri(n) = 1 + n / 2, if n is even.
tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
For example:
tri(2) = 1 + (2 / 2) = 2
tri(4) = 3
tri(3) = tri(2) + tri(1) + tri(4)
   = 2 + 3 + 3 = 8 
You are given a non-negative integer number n, you have to a return a list of the 
first n + 1 numbers of the Tribonacci sequence.
Examples:
tri(3) = [1, 3, 2, 8]
"""

def tri(n):
    if n == 0:
        return [1]
    my_tri = [1, 3]
    for i in range(2, n + 1):
        if i % 2 == 0:
            my_tri.append(i / 2 + 1)
        else:
            my_tri.append(my_tri[i - 1] + my_tri[i - 2] + (i + 3) / 2)
    return my_tri

def test_tri(): # pragma: no cover
    global tri
    assert tri(0) == [1], "Test case n=0 failed"
    assert tri(1) == [1, 3], "Test case n=1 failed"
    assert tri(2) == [1, 3, 2], "Test case n=2 failed"
    assert tri(3) == [1, 3, 2, 8], "Test case n=3 failed"
    assert tri(4) == [1, 3, 2, 8, 14], "Test case n=4 failed"

if __name__ == "__main__": # pragma: no cover
    test_tri()

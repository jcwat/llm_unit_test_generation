""" Return list of prime factors of given integer in the order from smallest to largest.
Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
Input number should be equal to the product of all factors
>>> factorize(8)
[2, 2, 2]
>>> factorize(25)
[5, 5]
>>> factorize(70)
[2, 5, 7]
"""
from typing import List


def factorize(n: int) -> List[int]:
    import math
    fact = []
    i = 2
    while i <= int(math.sqrt(n) + 1):
        if n % i == 0:
            fact.append(i)
            n //= i
        else:
            i += 1

    if n > 1:
        fact.append(n)
    return fact

def test_factorize(): # pragma: no cover
    global test_factorize, math
    assert factorize(8) == [2, 2, 2], "Test case 1 failed"
    assert factorize(25) == [5, 5], "Test case 2 failed"
    assert factorize(70) == [2, 5, 7], "Test case 3 failed"
    assert factorize(7) == [7], "Test case 4 failed"
if __name__ == "__main__": # pragma: no cover
    test_factorize()

"""Implement a function that takes an non-negative integer and returns an array of the first n
integers that are prime numbers and less than n.
for example:
count_up_to(5) => [2,3]
count_up_to(11) => [2,3,5,7]
count_up_to(0) => []
count_up_to(20) => [2,3,5,7,11,13,17,19]
count_up_to(1) => []
count_up_to(18) => [2,3,5,7,11,13,17]
"""

def count_up_to(n):
    primes = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes


def test_count_up_to(): # pragma: no cover
    global count_up_to
    assert count_up_to(5) == [2, 3], "Test for n=5 failed"
    assert count_up_to(11) == [2, 3, 5, 7], "Test for n=11 failed"
    assert count_up_to(0) == [], "Test for n=0 failed"
    assert count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19], "Test for n=20 failed"
    assert count_up_to(1) == [], "Test for n=1 failed"
    assert count_up_to(18) == [2, 3, 5, 7, 11, 13, 17], "Test for n=18 failed"

if __name__ == "__main__": # pragma: no cover
    test_count_up_to()

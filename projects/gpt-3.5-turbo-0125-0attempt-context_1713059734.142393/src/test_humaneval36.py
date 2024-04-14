"""Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
>>> fizz_buzz(50)
0
>>> fizz_buzz(78)
2
>>> fizz_buzz(79)
3
"""


def fizz_buzz(n: int):
    ns = []
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            ns.append(i)
    s = ''.join(list(map(str, ns)))
    ans = 0
    for c in s:
        ans += (c == '7')
    return ans

def test_fizz_buzz(): # pragma: no cover
    global fizz_buzz, math
    assert fizz_buzz(50) == 0, "Test case with input 50 failed"
    assert fizz_buzz(78) == 2, "Test case with input 78 failed"
    assert fizz_buzz(79) == 3, "Test case with input 79 failed"
if __name__ == "__main__": # pragma: no cover
    test_fizz_buzz()

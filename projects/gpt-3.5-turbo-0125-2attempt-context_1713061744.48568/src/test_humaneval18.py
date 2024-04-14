""" Find how many times a given substring can be found in the original string. Count overlaping cases.
>>> how_many_times('', 'a')
0
>>> how_many_times('aaa', 'a')
3
>>> how_many_times('aaaa', 'aa')
3
"""


def how_many_times(string: str, substring: str) -> int:
    times = 0

    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            times += 1

    return times

def test_how_many_times(): # pragma: no cover
    global how_many_times
    assert how_many_times('', 'a') == 0, "Test case 1 failed"
    assert how_many_times('aaa', 'a') == 3, "Test case 2 failed"
    assert how_many_times('aaaa', 'aa') == 3, "Test case 3 failed"

if __name__ == "__main__": # pragma: no cover
    test_how_many_times()

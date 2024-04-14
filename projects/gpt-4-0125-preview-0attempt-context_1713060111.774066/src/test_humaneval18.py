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
    global test_how_many_times, how_many_times
    assert how_many_times('', 'a') == 0, "Test case 1 failed: Searching within an empty string should return 0."
    assert how_many_times('aaa', 'a') == 3, "Test case 2 failed: 'a' occurs 3 times in 'aaa'."
    assert how_many_times('aaaa', 'aa') == 3, "Test case 3 failed: 'aa' overlaps and occurs 3 times in 'aaaa'."
    assert how_many_times('abc', 'd') == 0, "Test case 4 failed: 'd' does not occur in 'abc'."
    assert how_many_times('abcabcabc', 'abc') == 3, "Test case 5 failed: 'abc' occurs 3 times in 'abcabcabc'."
    assert how_many_times('ababa', 'aba') == 2, "Test case 6 failed: 'aba' overlaps and occurs 2 times in 'ababa'."

if __name__ == "__main__": # pragma: no cover
    test_how_many_times()

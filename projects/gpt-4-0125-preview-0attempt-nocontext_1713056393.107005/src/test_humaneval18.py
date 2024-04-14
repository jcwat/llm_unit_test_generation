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
    assert how_many_times('', 'a') == 0, "Test case with empty string failed"
    assert how_many_times('aaa', 'a') == 3, "Test case with single character substring failed"
    assert how_many_times('aaaa', 'aa') == 3, "Test case with overlapping substrings failed"
    assert how_many_times('abcabcabc', 'abc') == 3, "Test case with non-overlapping substrings failed"
    assert how_many_times('ababa', 'aba') == 2, "Test case with complex overlapping failed"
    assert how_many_times('abc', 'd') == 0, "Test case with no occurrences failed"

if __name__ == "__main__": # pragma: no cover
    test_how_many_times()

""" Filter an input list of strings only for ones that contain given substring
>>> filter_by_substring([], 'a')
[]
>>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
['abc', 'bacd', 'array']
"""
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

def test_filter_by_substring(): # pragma: no cover
    global filter_by_substring, List

    # Test case 1: substring exists in all strings
    strings1 = ["banana", "apple", "cherry"]
    substring1 = "a"
    expected_output1 = strings1
    assert filter_by_substring(strings1, substring1) == expected_output1, "Test case 1 failed"

    # Test case 2: substring doesn't exist in any string
    strings2 = ["dog", "cat", "elephant"]
    substring2 = "z"
    expected_output2 = []
    assert filter_by_substring(strings2, substring2) == expected_output2, "Test case 2 failed"

    # Test case 3: substring exists in some strings
    strings3 = ["hello", "world", "python"]
    substring3 = "o"
    expected_output3 = ["hello", "world"]
    assert filter_by_substring(strings3, substring3) == expected_output3, "Test case 3 failed"

if __name__ == "__main__": # pragma: no cover
    test_filter_by_substring()

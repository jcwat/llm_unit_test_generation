""" Return list of all prefixes from shortest to longest of the input string
>>> all_prefixes('abc')
['a', 'ab', 'abc']
"""
from typing import List


def all_prefixes(string: str) -> List[str]:
    result = []

    for i in range(len(string)):
        result.append(string[:i+1])
    return result

def test_all_prefixes(): # pragma: no cover
    global all_prefixes
    assert all_prefixes("abc") == ["a", "ab", "abc"], "Test case 1 failed"
    assert all_prefixes("") == [], "Test case 2 failed"
    assert all_prefixes("a") == ["a"], "Test case 3 failed"
    assert all_prefixes("abcd") == ["a", "ab", "abc", "abcd"], "Test case 4 failed"

if __name__ == "__main__": # pragma: no cover
    test_all_prefixes()

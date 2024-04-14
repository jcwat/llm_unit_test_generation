""" Concatenate list of strings into a single string
>>> concatenate([])
''
>>> concatenate(['a', 'b', 'c'])
'abc'
"""
from typing import List


def concatenate(strings: List[str]) -> str:
    return ''.join(strings)

def test_concatenate(): # pragma: no cover
    global test_concatenate, List
    assert concatenate(["hello", "world"]) == "helloworld", "Test case 1 failed"
    assert concatenate([""]) == "", "Test case 2 failed"
    assert concatenate([]) == "", "Test case 3 failed"
    assert concatenate(["a", "b", "c"]) == "abc", "Test case 4 failed"
    assert concatenate(["1", "2", "3", "4", "5"]) == "12345", "Test case 5 failed"

if __name__ == "__main__": # pragma: no cover
    test_concatenate()

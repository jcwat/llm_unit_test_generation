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
    assert concatenate([]) == "", "Test case 1 failed: empty list should return empty string"
    assert concatenate(['a', 'b', 'c']) == 'abc', "Test case 2 failed: ['a', 'b', 'c'] should return 'abc'"
    assert concatenate(['hello', ' ', 'world']) == 'hello world', "Test case 3 failed: ['hello', ' ', 'world'] should return 'hello world'"
    assert concatenate(['1', '2', '3']) == '123', "Test case 4 failed: ['1', '2', '3'] should return '123'"
    assert concatenate(['', '']) == '', "Test case 5 failed: ['', ''] should return ''"

if __name__ == "__main__": # pragma: no cover
    test_concatenate()

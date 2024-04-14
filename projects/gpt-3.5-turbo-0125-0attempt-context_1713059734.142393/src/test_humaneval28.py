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
    global concatenate, List
    
    assert concatenate([]) == '', "Test case failed for empty list"
    assert concatenate(['a', 'b', 'c']) == 'abc', "Test case failed for ['a', 'b', 'c']"
    assert concatenate(['hello', 'world']) == 'helloworld', "Test case failed for ['hello', 'world']"
    assert concatenate(['cat', 'dog', 'rabbit']) == 'catdograbbit', "Test case failed for ['cat', 'dog', 'rabbit']"

if __name__ == "__main__": # pragma: no cover
    test_concatenate()

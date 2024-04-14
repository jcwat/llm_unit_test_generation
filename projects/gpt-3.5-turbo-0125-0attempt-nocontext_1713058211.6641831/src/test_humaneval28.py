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
    assert concatenate(['hello', 'world']) == 'helloworld', "Test case 1 failed"
    assert concatenate(['python', 'is', 'awesome']) == 'pythonisawesome', "Test case 2 failed"
    assert concatenate(['unit', 'testing', 'is', 'important']) == 'unittestingisimportant', "Test case 3 failed"
if __name__ == "__main__": # pragma: no cover
    test_concatenate()

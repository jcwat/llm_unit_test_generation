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
    assert concatenate([]) == '', "Empty list concatenation failed"
    assert concatenate(['a', 'b', 'c']) == 'abc', "Concatenation failed"
    assert concatenate(['hello', 'world']) == 'helloworld', "Concatenation with multiple strings failed"
    assert concatenate(['123', '456', '789']) == '123456789', "Concatenation with numeric strings failed"
if __name__ == "__main__": # pragma: no cover
    test_concatenate()

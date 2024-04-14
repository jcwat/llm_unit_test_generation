from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)

def test_concatenate(): # pragma: no cover
    assert  concatenate([]) == ''
    assert  concatenate(['x', 'y', 'z']) == 'xyz'
    assert  concatenate(['x', 'y', 'z', 'w', 'k']) == 'xyzwk'


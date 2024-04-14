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
    global all_prefixes, List
    assert all_prefixes('abc') == ['a', 'ab', 'abc'], "Test case 1 failed"
    assert all_prefixes('hello') == ['h', 'he', 'hel', 'hell', 'hello'], "Test case 2 failed"
    assert all_prefixes('12345') == ['1', '12', '123', '1234', '12345'], "Test case 3 failed"

if __name__ == "__main__": # pragma: no cover
    test_all_prefixes()

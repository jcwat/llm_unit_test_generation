""" For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
>>> flip_case('Hello')
'hELLO'
"""


def flip_case(string: str) -> str:
    return string.swapcase()

def test_flip_case(): # pragma: no cover
    global flip_case
    assert flip_case('Hello') == 'hELLO', "Test case 1 failed: flip_case('Hello') should return 'hELLO'"
    assert flip_case('hELLO') == 'Hello', "Test case 2 failed: flip_case('hELLO') should return 'Hello'"
    assert flip_case('123abcABC') == '123ABCabc', "Test case 3 failed: flip_case('123abcABC') should return '123ABCabc'"
    assert flip_case('') == '', "Test case 4 failed: flip_case('') should return '' (empty string)"
    assert flip_case('!@#$%^&*()') == '!@#$%^&*()', "Test case 5 failed: flip_case('!@#$%^&*()') should return '!@#$%^&*()' (same string)"

if __name__ == "__main__": # pragma: no cover
    test_flip_case()

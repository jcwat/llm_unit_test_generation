""" For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
>>> flip_case('Hello')
'hELLO'
"""


def flip_case(string: str) -> str:
    return string.swapcase()

def test_flip_case(): # pragma: no cover
    global test_flip_case
    assert flip_case("Hello World") == "hELLO wORLD", "Test case 1 failed"
    assert flip_case("123abc") == "123ABC", "Test case 2 failed"
    assert flip_case("iNvIsIbLe") == "InViSiBlE", "Test case 3 failed"
if __name__ == "__main__": # pragma: no cover
    test_flip_case()

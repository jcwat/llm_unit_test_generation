""" For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
>>> flip_case('Hello')
'hELLO'
"""


def flip_case(string: str) -> str:
    return string.swapcase()

def test_flip_case(): # pragma: no cover
    global flip_case

    assert flip_case("Hello") == "hELLO", "Test case 1 failed"
    assert flip_case("Python") == "pYTHON", "Test case 2 failed"
    assert flip_case("tEsT") == "TeSt", "Test case 3 failed"

if __name__ == "__main__": # pragma: no cover
    test_flip_case()



def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return string.swapcase()

def test_flip_case(): # pragma: no cover
    assert  flip_case('') == ''
    assert  flip_case('Hello!') == 'hELLO!'
    assert  flip_case('These violent delights have violent ends') == 'tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS'


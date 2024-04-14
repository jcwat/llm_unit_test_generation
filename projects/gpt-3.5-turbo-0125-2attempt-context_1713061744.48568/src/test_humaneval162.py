"""
Given a string 'text', return its md5 hash equivalent string.
If 'text' is an empty string, return None.

>>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
"""

def string_to_md5(text):
    import hashlib
    return hashlib.md5(text.encode('ascii')).hexdigest() if text else None

def test_string_to_md5(): # pragma: no cover
    global hashlib, string_to_md5

    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62', "Test case 1 failed"
    assert string_to_md5('') == None, "Test case 2 failed"
    assert string_to_md5('1234567890') == 'e807f1fcf82d132f9bb018ca6738a19f', "Test case 3 failed"

if __name__ == "__main__": # pragma: no cover
    test_string_to_md5()

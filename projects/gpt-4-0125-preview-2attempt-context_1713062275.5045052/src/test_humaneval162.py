"""
Given a string 'text', return its md5 hash equivalent string.
If 'text' is an empty string, return None.

>>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
"""

def string_to_md5(text):
    import hashlib
    return hashlib.md5(text.encode('ascii')).hexdigest() if text else None

def test_string_to_md5(): # pragma: no cover
    global test_string_to_md5, hashlib
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62', "Test case 1 failed"
    assert string_to_md5('') is None, "Test case 2 failed"
    assert string_to_md5('123') == '202cb962ac59075b964b07152d234b70', "Test case 3 failed"

if __name__ == "__main__": # pragma: no cover
    test_string_to_md5()

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

    assert string_to_md5("") is None, "Empty string case failed"
    assert string_to_md5("test") == "098f6bcd4621d373cade4e832627b4f6", "Test case 1 failed"
    assert string_to_md5("hello world") == "fc5e038d38a57032085441e7fe7010b0", "Test case 2 failed"

if __name__ == "__main__": # pragma: no cover
    test_string_to_md5()

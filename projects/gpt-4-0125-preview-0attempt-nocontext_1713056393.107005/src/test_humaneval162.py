"""
Given a string 'text', return its md5 hash equivalent string.
If 'text' is an empty string, return None.

>>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
"""

def string_to_md5(text):
    import hashlib
    return hashlib.md5(text.encode('ascii')).hexdigest() if text else None

def test_string_to_md5(): # pragma: no cover
    global string_to_md5, hashlib
    # Test non-empty string
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62', "Test case 1 failed: non-empty string should match the known MD5 hash."
    # Test empty string
    assert string_to_md5('') is None, "Test case 2 failed: empty string should return None."
    # Test different non-empty string
    assert string_to_md5('Python') == 'd1fb13c9441c730097cdfdd1a5a3df3a', "Test case 3 failed: non-empty string 'Python' should match its known MD5 hash."
    
if __name__ == "__main__": # pragma: no cover
    test_string_to_md5()

"""Create a function encrypt that takes a string as an argument and
returns a string encrypted with the alphabet being rotated. 
The alphabet should be rotated in a manner such that the letters 
shift down by two multiplied to two places.
For example:
encrypt('hi') returns 'lm'
encrypt('asdfghjkl') returns 'ewhjklnop'
encrypt('gf') returns 'kj'
encrypt('et') returns 'ix'
"""

def encrypt(s):
    d = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    for c in s:
        if c in d:
            out += d[(d.index(c)+2*2) % 26]
        else:
            out += c
    return out

def test_encrypt(): # pragma: no cover
    global test_encrypt
    assert encrypt('hi') == 'lm', "Test case 'hi' failed"
    assert encrypt('asdfghjkl') == 'ewhjklnop', "Test case 'asdfghjkl' failed"
    assert encrypt('gf') == 'kj', "Test case 'gf' failed"
    assert encrypt('et') == 'ix', "Test case 'et' failed"
    # Testing edge cases
    assert encrypt('z') == 'd', "Test case 'z' failed"
    assert encrypt('y') == 'c', "Test case 'y' failed"
    # Testing non-alphabet characters
    assert encrypt('!@#') == '!@#', "Test case '!@#' failed"
    # Testing uppercase (should not be converted, as per function specification)
    assert encrypt('A') == 'A', "Test case 'A' failed"

if __name__ == "__main__": # pragma: no cover
    test_encrypt()

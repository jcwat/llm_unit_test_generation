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
    global encrypt
    
    assert encrypt('hi') == 'lm', "Test case 1 failed"
    assert encrypt('asdfghjkl') == 'ewhjklnop', "Test case 2 failed"
    assert encrypt('gf') == 'kj', "Test case 3 failed"
    assert encrypt('et') == 'ix', "Test case 4 failed"
    assert encrypt('xyz') == 'bcd', "Test case 5 failed"
    
if __name__ == "__main__": # pragma: no cover
    test_encrypt()

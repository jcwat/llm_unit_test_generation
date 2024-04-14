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
    assert encrypt('hi') == 'lm', "Encrypting 'hi' should return 'lm'"
    assert encrypt('asdfghjkl') == 'ewhjklnop', "Encrypting 'asdfghjkl' should return 'ewhjklnop'"
    assert encrypt('gf') == 'kj', "Encrypting 'gf' should return 'kj'"
    assert encrypt('et') == 'ix', "Encrypting 'et' should return 'ix'"
    assert encrypt('z') == 'd', "Encrypting 'z' should return 'd'"
    assert encrypt('yz') == 'cd', "Encrypting 'yz' should return 'cd'"
    assert encrypt('') == '', "Encrypting an empty string should return an empty string"
    assert encrypt('123') == '123', "Encrypting '123' should return '123' since it contains no alphabets"

if __name__ == "__main__": # pragma: no cover
    test_encrypt()

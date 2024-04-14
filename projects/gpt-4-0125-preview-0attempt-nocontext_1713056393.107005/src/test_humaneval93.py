"""
Write a function that takes a message, and encodes in such a 
way that it swaps case of all letters, replaces all vowels in 
the message with the letter that appears 2 places ahead of that 
vowel in the english alphabet. 
Assume only letters. 

Examples:
>>> encode('test')
'TGST'
>>> encode('This is a message')
'tHKS KS C MGSSCGG'
"""

def encode(message):
    vowels = "aeiouAEIOU"
    vowels_replace = dict([(i, chr(ord(i) + 2)) for i in vowels])
    message = message.swapcase()
    return ''.join([vowels_replace[i] if i in vowels else i for i in message])

def test_encode(): # pragma: no cover
    global encode
    assert encode('test') == 'TGST', "Test case 1 failed"
    assert encode('This is a message') == 'tHKS KS C MGSSCGG', "Test case 2 failed"
    assert encode('HELLO') == 'hKLLQ', "Test case 3 failed"
    assert encode('world') == 'WQRLD', "Test case 4 failed"
    assert encode('aEiOu') == 'cGkQy', "Test case 5 failed"

if __name__ == "__main__": # pragma: no cover
    test_encode()

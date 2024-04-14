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
    # Test case 1: Normal sentence
    assert encode('test') == 'TGST', "Test case 1 failed"
    # Test case 2: Sentence with spaces and mixed case
    assert encode('This is a message') == 'tHKS KS C MGSSCGG', "Test case 2 failed"
    # Test case 3: All vowels
    assert encode('aeiouAEIOU') == 'cgkqCGKQ', "Test case 3 failed"
    # Test case 4: No vowels
    assert encode('bcdfgBCDFG') == 'bcdfgBCDFG', "Test case 4 failed"
    # Test case 5: Empty string
    assert encode('') == '', "Test case 5 failed"

if __name__ == "__main__": # pragma: no cover
    test_encode()

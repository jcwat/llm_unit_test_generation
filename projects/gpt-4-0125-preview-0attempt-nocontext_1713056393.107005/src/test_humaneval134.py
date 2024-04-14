'''
Create a function that returns True if the last character
of a given string is an alphabetical character and is not
a part of a word, and False otherwise.
Note: "word" is a group of characters separated by space.

Examples:
check_if_last_char_is_a_letter("apple pie") ➞ False
check_if_last_char_is_a_letter("apple pi e") ➞ True
check_if_last_char_is_a_letter("apple pi e ") ➞ False
check_if_last_char_is_a_letter("") ➞ False 
'''

def check_if_last_char_is_a_letter(txt):
 
    check = txt.split(' ')[-1]
    return True if len(check) == 1 and (97 <= ord(check.lower()) <= 122) else False

def test_check_if_last_char_is_a_letter(): # pragma: no cover
    global check_if_last_char_is_a_letter
    assert check_if_last_char_is_a_letter("apple pie") == False, "Test case 1 failed"  
    assert check_if_last_char_is_a_letter("apple pi e") == True, "Test case 2 failed"
    assert check_if_last_char_is_a_letter("apple pi e ") == False, "Test case 3 failed"
    assert check_if_last_char_is_a_letter("") == False, "Test case 4 failed"  
    assert check_if_last_char_is_a_letter("a") == True, "Test case 5 failed"
    assert check_if_last_char_is_a_letter(" ") == False, "Test case 6 failed"
    assert check_if_last_char_is_a_letter("abc d") == False, "Test case 7 failed"
    assert check_if_last_char_is_a_letter("1 2 3") == False, "Test case 8 failed"

if __name__ == "__main__": # pragma: no cover
    test_check_if_last_char_is_a_letter()

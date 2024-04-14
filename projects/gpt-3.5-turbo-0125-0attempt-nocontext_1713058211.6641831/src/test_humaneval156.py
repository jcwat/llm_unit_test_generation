"""
Given a positive integer, obtain its roman numeral equivalent as a string,
and return it in lowercase.
Restrictions: 1 <= num <= 1000

Examples:
>>> int_to_mini_roman(19) == 'xix'
>>> int_to_mini_roman(152) == 'clii'
>>> int_to_mini_roman(426) == 'cdxxvi'
"""

def int_to_mini_roman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90,  
           100, 400, 500, 900, 1000] 
    sym = ["I", "IV", "V", "IX", "X", "XL",  
           "L", "XC", "C", "CD", "D", "CM", "M"] 
    i = 12
    res = ''
    while number: 
        div = number // num[i] 
        number %= num[i] 
        while div: 
            res += sym[i] 
            div -= 1
        i -= 1
    return res.lower()

def test_int_to_mini_roman(): # pragma: no cover
    global int_to_mini_roman
    assert int_to_mini_roman(3) == 'iii', "Test case 1 failed"
    assert int_to_mini_roman(4) == 'iv', "Test case 2 failed"
    assert int_to_mini_roman(9) == 'ix', "Test case 3 failed"
    assert int_to_mini_roman(58) == 'lviii', "Test case 4 failed"
    assert int_to_mini_roman(1994) == 'mcmxciv', "Test case 5 failed"
if __name__ == "__main__": # pragma: no cover
    test_int_to_mini_roman()

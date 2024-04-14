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
    assert int_to_mini_roman(19) == 'xix', "Test case 1 failed - 19 should be xix"
    assert int_to_mini_roman(152) == 'clii', "Test case 2 failed - 152 should be clii"
    assert int_to_mini_roman(426) == 'cdxxvi', "Test case 3 failed - 426 should be cdxxvi"
    assert int_to_mini_roman(1) == 'i', "Test case 4 failed - 1 should be i"
    assert int_to_mini_roman(1000) == 'm', "Test case 5 failed - 1000 should be m"

if __name__ == "__main__": # pragma: no cover
    test_int_to_mini_roman()

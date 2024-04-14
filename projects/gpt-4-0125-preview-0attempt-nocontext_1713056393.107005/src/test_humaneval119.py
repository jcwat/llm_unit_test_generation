'''
You are given a list of two strings, both strings consist of open
parentheses '(' or close parentheses ')' only.
Your job is to check if it is possible to concatenate the two strings in
some order, that the resulting string will be good.
A string S is considered to be good if and only if all parentheses in S
are balanced. For example: the string '(())()' is good, while the string
'())' is not.
Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

Examples:
match_parens(['()(', ')']) == 'Yes'
match_parens([')', ')']) == 'No'
'''

def match_parens(lst):
    def check(s):
        val = 0
        for i in s:
            if i == '(':
                val = val + 1
            else:
                val = val - 1
            if val < 0:
                return False
        return True if val == 0 else False

    S1 = lst[0] + lst[1]
    S2 = lst[1] + lst[0]
    return 'Yes' if check(S1) or check(S2) else 'No'

def test_match_parens(): # pragma: no cover
    global match_parens
    # Test case where concatenation in any order results in a balanced string
    assert match_parens(['()(', ')']) == 'Yes', "Test case 1 failed: Expected 'Yes' for ['()(', ')']"

    # Test case where no concatenation results in a balanced string
    assert match_parens([')', ')']) == 'No', "Test case 2 failed: Expected 'No' for [')', ')']"

    # Test case where only one specific order results in a balanced string
    assert match_parens(['(', ')(']) == 'Yes', "Test case 3 failed: Expected 'Yes' for ['(', ')(']"

    # Test case with empty strings
    assert match_parens(['', '']) == 'Yes', "Test case 4 failed: Expected 'Yes' for ['', '']"

    # Test case where both strings are already balanced
    assert match_parens(['()', '()']) == 'Yes', "Test case 5 failed: Expected 'Yes' for ['()', '()']"

    # Test case with complex strings concatenation
    assert match_parens(['())(', '(()']) == 'Yes', "Test case 6 failed: Expected 'Yes' for ['())(', '(()']"

if __name__ == "__main__": # pragma: no cover
    test_match_parens()

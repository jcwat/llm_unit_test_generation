""" Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
separate those group into separate strings and return the list of those.
Separate groups are balanced (each open brace is properly closed) and not nested within each other
Ignore any spaces in the input string.
>>> separate_paren_groups('( ) (( )) (( )( ))')
['()', '(())', '(()())']
"""
from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    current_string = []
    current_depth = 0

    for c in paren_string:
        if c == '(':
            current_depth += 1
            current_string.append(c)
        elif c == ')':
            current_depth -= 1
            current_string.append(c)

            if current_depth == 0:
                result.append(''.join(current_string))
                current_string.clear()

    return result

def test_separate_paren_groups(): # pragma: no cover
    global separate_paren_groups

    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())'], "Test case 1 failed"
    assert separate_paren_groups('()') == ['()'], "Test case 2 failed"
    assert separate_paren_groups('((()))') == ['((()))'], "Test case 3 failed"
    assert separate_paren_groups('(( )() )') == ['( )()', '()'], "Test case 4 failed"
if __name__ == "__main__": # pragma: no cover
    test_separate_paren_groups()

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

 # pragma: no cover
def test_separate_paren_groups():
    global separate_paren_groups, List

    # Test case 1: Single group
    assert separate_paren_groups("(abc)") == ["(abc)"], "Test case 1 failed"

    # Test case 2: Multiple groups
    assert separate_paren_groups("(abc(def)ghi(jkl)mno)") == ["(abc(def)ghi(jkl)mno)"], "Test case 2 failed"

    # Test case 3: Nested groups
    assert separate_paren_groups("(a(b(c)d)e)") == ["(a(b(c)d)e)"], "Test case 3 failed"

    # Test case 4: No groups
    assert separate_paren_groups("abc") == [], "Test case 4 failed"

if __name__ == "__main__": # pragma: no cover
    test_separate_paren_groups()

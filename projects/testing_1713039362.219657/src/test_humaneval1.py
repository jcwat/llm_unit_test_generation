from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
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
    # Test empty string
    assert separate_paren_groups('') == [], "Test case 1 failed: Empty string should return an empty list."
    
    # Test string with single group of parentheses
    assert separate_paren_groups('()') == ['()'], "Test case 2 failed: Single group of parentheses not correctly identified."
    
    # Test string with multiple groups, no nesting
    assert separate_paren_groups('()()') == ['()', '()'], "Test case 3 failed: Multiple groups without nesting not correctly identified."
    
    # Test string with nested groups
    assert separate_paren_groups('(())') == ['(())'], "Test case 4 failed: Nested groups not correctly identified."
    
    # Test string with complex nesting and multiple groups
    assert separate_paren_groups('(())(()(()))()') == ['(())', '(()(()))', '()'], "Test case 5 failed: Complex nesting and multiple groups not correctly identified."
    
    # Test string with spaces
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())'], "Test case 6 failed: Spaces not correctly ignored."
    
if __name__ == "__main__": # pragma: no cover
    test_separate_paren_groups()

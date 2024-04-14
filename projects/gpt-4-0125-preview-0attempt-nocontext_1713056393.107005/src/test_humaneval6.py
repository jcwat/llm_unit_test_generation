""" Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
For each of the group, output the deepest level of nesting of parentheses.
E.g. (()()) has maximum two levels of nesting while ((())) has three.

>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
"""
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    def parse_paren_group(s):
        depth = 0
        max_depth = 0
        for c in s:
            if c == '(':
                depth += 1
                max_depth = max(depth, max_depth)
            else:
                depth -= 1

        return max_depth

    return [parse_paren_group(x) for x in paren_string.split(' ') if x]

def test_parse_nested_parens(): # pragma: no cover
    global parse_nested_parens

    # Test 1: Test for multiple groups with different nestings
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3], "Test case 1 failed"

    # Test 2: Single group with deep nesting
    assert parse_nested_parens('(((())))') == [4], "Test case 2 failed"

    # Test 3: Empty string should return an empty list
    assert parse_nested_parens('') == [], "Test case 3 failed"

    # Test 4: Spaces in between should be ignored, empty groups not counted
    assert parse_nested_parens('  (()())    ((()))     ()    ((())()())  ') == [2, 3, 1, 3], "Test case 4 failed"

if __name__ == "__main__": # pragma: no cover
    test_parse_nested_parens()

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
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3], "Test case 1 failed"
    assert parse_nested_parens('') == [], "Test case 2 failed"
    assert parse_nested_parens('((( ))) (((()))) (()) ()') == [3, 4, 2, 1], "Test case 3 fixed"
    assert parse_nested_parens('()') == [1], "Test case 4 failed"
    assert parse_nested_parens('(((())))') == [4], "Test case 5 failed"
    assert parse_nested_parens('((())()) (()) (((()))(()))') == [3, 2, 4], "Test case 6 failed"

if __name__ == "__main__": # pragma: no cover
    test_parse_nested_parens()

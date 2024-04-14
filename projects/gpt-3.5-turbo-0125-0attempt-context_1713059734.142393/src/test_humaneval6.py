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
    global parse_nested_parens, List

    # Test case 1: Multiple groups with different depths
    input1 = "(()()) ((())) () ((())()())"
    expected_output1 = [2, 3, 1, 3]
    assert parse_nested_parens(input1) == expected_output1, "Test case 1 failed"

    # Test case 2: Empty string
    input2 = ""
    expected_output2 = []
    assert parse_nested_parens(input2) == expected_output2, "Test case 2 failed"

    # Test case 3: Single group with maximum depth
    input3 = "((((()))))"
    expected_output3 = [6]
    assert parse_nested_parens(input3) == expected_output3, "Test case 3 failed"

if __name__ == "__main__": # pragma: no cover
    test_parse_nested_parens()

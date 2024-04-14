"""
Given a string text, replace all spaces in it with underscores, 
and if a string has more than 2 consecutive spaces, 
then replace all consecutive spaces with - 

fix_spaces("Example") == "Example"
fix_spaces("Example 1") == "Example_1"
fix_spaces(" Example 2") == "_Example_2"
fix_spaces(" Example   3") == "_Example-3"
"""

def fix_spaces(text):
    new_text = ""
    i = 0
    start, end = 0, 0
    while i < len(text):
        if text[i] == " ":
            end += 1
        else:
            if end - start > 2:
                new_text += "-"+text[i]
            elif end - start > 0:
                new_text += "_"*(end - start)+text[i]
            else:
                new_text += text[i]
            start, end = i+1, i+1
        i+=1
    if end - start > 2:
        new_text += "-"
    elif end - start > 0:
        new_text += "_"
    return new_text

def test_fix_spaces(): # pragma: no cover
    global fix_spaces
    assert fix_spaces("Example") == "Example", "Test case 1 failed: 'Example' should not change."
    assert fix_spaces("Example 1") == "Example_1", "Test case 2 failed: Single space should become an underscore."
    assert fix_spaces(" Example 2") == "_Example_2", "Test case 3 failed: Leading and single internal spaces should become underscores."
    assert fix_spaces(" Example   3") == "_Example-3", "Test case 4 failed: More than two consecutive spaces should become a single dash."
    assert fix_spaces("  Example    4   ") == "_Example-4_", "Test case 5 failed: Leading, trailing, and internal long spaces not handled correctly."
    assert fix_spaces("Example") == "Example", "Test case 6 failed: No spaces case should return the original string."
    assert fix_spaces("      ") == "-", "Test case 7 failed: Only spaces should return a single dash."
    assert fix_spaces("Example     ") == "Example-", "Test case 8 failed: Trailing long spaces should become a single dash."

if __name__ == "__main__": # pragma: no cover
    test_fix_spaces()

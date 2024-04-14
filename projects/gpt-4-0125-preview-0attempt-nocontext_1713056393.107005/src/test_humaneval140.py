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
    assert fix_spaces("Example") == "Example", "Single word with no spaces should remain unchanged."
    assert fix_spaces("Example 1") == "Example_1", "Single space should be replaced with underscore."
    assert fix_spaces(" Example 2") == "_Example_2", "Leading space should be replaced with underscore."
    assert fix_spaces("Example   3") == "Example-3", "Consecutive spaces more than 2 should be replaced with dash."
    assert fix_spaces("  Example 4  ") == "_Example_4_", "Leading and trailing spaces should be handled correctly."
    assert fix_spaces("Example    5") == "Example-5", "Multiple spaces (more than 2) should be replaced with just one dash."
    assert fix_spaces("") == "", "Empty string should remain unchanged."
    assert fix_spaces(" ") == "_", "Single space should become single underscore."
    assert fix_spaces("  ") == "__", "Two spaces should become two underscores."
    assert fix_spaces("   ") == "-", "Three spaces should become one dash."

if __name__ == "__main__": # pragma: no cover
    test_fix_spaces()

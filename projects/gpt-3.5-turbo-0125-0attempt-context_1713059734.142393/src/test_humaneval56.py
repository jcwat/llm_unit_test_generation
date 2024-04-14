""" brackets is a string of "<" and ">".
return True if every opening bracket has a corresponding closing bracket.

>>> correct_bracketing("<")
False
>>> correct_bracketing("<>")
True
>>> correct_bracketing("<<><>>")
True
>>> correct_bracketing("><<>")
False
"""


def correct_bracketing(brackets: str):
    depth = 0
    for b in brackets:
        if b == "<":
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return False
    return depth == 0

def test_correct_bracketing(): # pragma: no cover
    global correct_bracketing
    
    assert correct_bracketing("<") == False, "Test case 1 failed"
    assert correct_bracketing("<>") == True, "Test case 2 failed"
    assert correct_bracketing("<<><>>") == True, "Test case 3 failed"
    assert correct_bracketing("><<>") == False, "Test case 4 failed"

if __name__ == "__main__": # pragma: no cover
    test_correct_bracketing()

"""I think we all remember that feeling when the result of some long-awaited
event is finally known. The feelings and thoughts you have at that moment are
definitely worth noting down and comparing.
Your task is to determine if a person correctly guessed the results of a number of matches.
You are given two arrays of scores and guesses of equal length, where each index shows a match. 
Return an array of the same length denoting how far off each guess was. If they have guessed correctly,
the value is 0, and if not, the value is the absolute difference between the guess and the score.


example:

compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) -> [0,0,0,0,3,3]
compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) -> [4,4,1,0,0,6]
"""

def compare(game,guess):
    return [abs(x-y) for x,y in zip(game,guess)]

def test_compare(): # pragma: no cover
    global compare
    assert compare([1,2,3,4,5,1], [1,2,3,4,2,-2]) == [0,0,0,0,3,3], "Test case 1 failed"
    assert compare([0,5,0,0,0,4], [4,1,1,0,0,-2]) == [4,4,1,0,0,6], "Test case 2 failed"
    assert compare([], []) == [], "Test case 3 failed"
    assert compare([10, 20, 30], [10, 20, 30]) == [0, 0, 0], "Test case 4 failed"
    assert compare([1], [0]) == [1], "Test case 5 failed"

if __name__ == "__main__": # pragma: no cover
    test_compare()

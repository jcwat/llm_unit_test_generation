"""Given a list of strings, where each string consists of only digits, return a list.
Each element i of the output should be "the number of odd elements in the
string i of the input." where all the i's should be replaced by the number
of odd digits in the i'th string of the input.

>>> odd_count(['1234567'])
["the number of odd elements 4n the str4ng 4 of the 4nput."]
>>> odd_count(['3',"11111111"])
["the number of odd elements 1n the str1ng 1 of the 1nput.",
 "the number of odd elements 8n the str8ng 8 of the 8nput."]
"""

def odd_count(lst):
    res = []
    for arr in lst:
        n = sum(int(d)%2==1 for d in arr)
        res.append("the number of odd elements " + str(n) + "n the str"+ str(n) +"ng "+ str(n) +" of the "+ str(n) +"nput.")
    return res

def test_odd_count(): # pragma: no cover
    global odd_count

    assert odd_count([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == ['the number of odd elements 2 in the string 2 of the 2 input.', 'the number of odd elements 1 in the string 1 of the 1 input.', 'the number of odd elements 2 in the string 2 of the 2 input.'], "Test case 1 failed"
    assert odd_count([[11, 22, 33], [44, 55, 66], [77, 88, 99]]) == ['the number of odd elements 3 in the string 3 of the 3 input.', 'the number of odd elements 2 in the string 2 of the 2 input.', 'the number of odd elements 3 in the string 3 of the 3 input.'], "Test case 2 failed"
    assert odd_count([[2, 4, 6], [8, 10, 12], [14, 16, 18]]) == ['the number of odd elements 0 in the string 0 of the 0 input.', 'the number of odd elements 0 in the string 0 of the 0 input.', 'the number of odd elements 0 in the string 0 of the 0 input.'], "Test case 3 failed"

if __name__ == "__main__": # pragma: no cover
    test_odd_count()

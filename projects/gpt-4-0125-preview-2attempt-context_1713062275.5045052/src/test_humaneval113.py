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
    global test_odd_count, odd_count
    input1 = ['1234567']
    expected_output1 = ["the number of odd elements 4n the str4ng 4 of the 4nput."]
    assert odd_count(input1) == expected_output1, f"Test case 1 failed: expected {expected_output1}, got {odd_count(input1)}"

    input2 = ['3', "11111111"]
    expected_output2 = ["the number of odd elements 1n the str1ng 1 of the 1nput.",
                        "the number of odd elements 8n the str8ng 8 of the 8nput."]
    assert odd_count(input2) == expected_output2, f"Test case 2 failed: expected {expected_output2}, got {odd_count(input2)}"

    input3 = ['246', '13579']
    expected_output3 = ["the number of odd elements 0n the str0ng 0 of the 0nput.",
                        "the number of odd elements 5n the str5ng 5 of the 5nput."]
    assert odd_count(input3) == expected_output3, f"Test case 3 failed: expected {expected_output3}, got {odd_count(input3)}"

if __name__ == "__main__": # pragma: no cover
    test_odd_count()

"""You will be given a number in decimal form and your task is to convert it to
binary format. The function should return a string, with each character representing a binary
number. Each character in the string will be '0' or '1'.

There will be an extra couple of characters 'db' at the beginning and at the end of the string.
The extra characters are there to help with the format.

Examples:
decimal_to_binary(15)   # returns "db1111db"
decimal_to_binary(32)   # returns "db100000db"
"""

def decimal_to_binary(decimal):
    return "db" + bin(decimal)[2:] + "db"

def test_decimal_to_binary(): # pragma: no cover
    global decimal_to_binary
    assert decimal_to_binary(10) == 'db1010db', "Test case 1 failed"
    assert decimal_to_binary(5) == 'db101db', "Test case 2 failed"
    assert decimal_to_binary(16) == 'db10000db', "Test case 3 failed"
if __name__ == "__main__": # pragma: no cover
    test_decimal_to_binary()

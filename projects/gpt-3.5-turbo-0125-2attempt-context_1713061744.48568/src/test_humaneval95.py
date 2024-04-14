"""
Given a dictionary, return True if all keys are strings in lower 
case or all keys are strings in upper case, else return False.
The function should return False is the given dictionary is empty.
Examples:
check_dict_case({"a":"apple", "b":"banana"}) should return True.
check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True.
"""

def check_dict_case(dict):
    if len(dict.keys()) == 0:
        return False
    else:
        state = "start"
        for key in dict.keys():

            if isinstance(key, str) == False:
                state = "mixed"
                break
            if state == "start":
                if key.isupper():
                    state = "upper"
                elif key.islower():
                    state = "lower"
                else:
                    break
            elif (state == "upper" and not key.isupper()) or (state == "lower" and not key.islower()):
                    state = "mixed"
                    break
            else:
                break
        return state == "upper" or state == "lower" 

def test_check_dict_case(): # pragma: no cover
    global check_dict_case

    # Test case 1: All keys are strings in lower case
    input_dict1 = {"a": "apple", "b": "banana", "c": "cherry"}
    assert check_dict_case(input_dict1) == True, "Test case 1 failed"

    # Test case 2: All keys are strings in upper case
    input_dict2 = {"NAME": "Alice", "AGE": "30", "CITY": "New York"}
    assert check_dict_case(input_dict2) == True, "Test case 2 failed"

    # Test case 3: Mixed case keys
    input_dict3 = {"Name": "Bob", "AGE": "25", "City": "Chicago"}
    assert check_dict_case(input_dict3) == False, "Test case 3 failed"

    # Test case 4: Empty dictionary
    input_dict4 = {}
    assert check_dict_case(input_dict4) == False, "Test case 4 failed"

if __name__ == "__main__": # pragma: no cover
    test_check_dict_case()
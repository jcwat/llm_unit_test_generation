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
    global test_check_dict_case, check_dict_case
    # Test case when all keys are lower case
    assert check_dict_case({"a":"apple", "b":"banana"}) == True, "Test case 1 failed"
    
    # Test case when keys are mixed case
    assert check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) == False, "Test case 2 failed"
    
    # Test case when not all keys are strings
    assert check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) == False, "Test case 3 failed"
    
    # Test case when all keys are upper case
    assert check_dict_case({"STATE":"NC", "ZIP":"12345"}) == True, "Test case 4 failed"
    
    # Test case when dictionary is empty
    assert check_dict_case({}) == False, "Test case 5 failed"
    
    # Test case with mixed keys that are not strictly upper or lower case
    assert check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) == False, "Test case 6 failed"
    
if __name__ == "__main__": # pragma: no cover
    test_check_dict_case()

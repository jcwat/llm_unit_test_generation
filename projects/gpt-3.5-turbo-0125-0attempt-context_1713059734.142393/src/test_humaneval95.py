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
    
    assert check_dict_case({"a":"apple", "b":"banana"}) == True, "Test case 1 failed"
    assert check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) == False, "Test case 2 failed"
    assert check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) == False, "Test case 3 failed"
    assert check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) == False, "Test case 4 failed"
    assert check_dict_case({"STATE":"NC", "ZIP":"12345"}) == True, "Test case 5 failed"
    
if __name__ == "__main__": # pragma: no cover
    test_check_dict_case()

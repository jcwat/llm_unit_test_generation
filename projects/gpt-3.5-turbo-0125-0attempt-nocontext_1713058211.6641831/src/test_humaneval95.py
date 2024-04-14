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
    
    # Test case when the dictionary is empty
    assert check_dict_case({}) == False, "Empty dictionary test case failed"
    
    # Test case with keys in uppercase
    assert check_dict_case({"KEY1": 1, "KEY2": 2}) == True, "Uppercase keys test case failed"
    
    # Test case with keys in lowercase
    assert check_dict_case({"key1": 1, "key2": 2}) == True, "Lowercase keys test case failed"
    
    # Test case with mixed keys
    assert check_dict_case({"Key1": 1, "KEY2": 2}) == False, "Mixed keys test case failed"
    
    # Test case with a mix of keys in a dictionary containing both uppercase and lowercase keys
    assert check_dict_case({"Key1": 1, "key2": 2}) == False, "Mixed keys test case failed"

if __name__ == "__main__": # pragma: no cover
    test_check_dict_case()

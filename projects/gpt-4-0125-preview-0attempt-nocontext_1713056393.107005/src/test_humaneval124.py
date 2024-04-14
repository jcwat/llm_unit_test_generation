"""You have to write a function which validates a given date string and
returns True if the date is valid otherwise False.
The date is valid if all of the following rules are satisfied:
1. The date string is not empty.
2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
3. The months should not be less than 1 or higher than 12.
4. The date should be in the format: mm-dd-yyyy

for example: 
valid_date('03-11-2000') => True

valid_date('15-01-2012') => False

valid_date('04-0-2040') => False

valid_date('06-04-2020') => True

valid_date('06/04/2020') => False
"""

def valid_date(date):
    try:
        date = date.strip()
        month, day, year = date.split('-')
        month, day, year = int(month), int(day), int(year)
        if month < 1 or month > 12:
            return False
        if month in [1,3,5,7,8,10,12] and day < 1 or day > 31:
            return False
        if month in [4,6,9,11] and day < 1 or day > 30:
            return False
        if month == 2 and day < 1 or day > 29:
            return False
    except:
        return False

    return True

def test_valid_date(): # pragma: no cover
    global test_valid_date, valid_date
    
    # Test cases for the valid_date function
    assert valid_date('03-11-2000') == True, "Test case 1 failed: '03-11-2000' should be valid"
    assert valid_date('15-01-2012') == False, "Test case 2 failed: '15-01-2012' should be invalid - incorrect format"
    assert valid_date('04-0-2040') == False, "Test case 3 failed: '04-0-2040' should be invalid - day cannot be zero"
    assert valid_date('06-04-2020') == True, "Test case 4 failed: '06-04-2020' should be valid"
    assert valid_date('06/04/2020') == False, "Test case 5 failed: '06/04/2020' should be invalid - incorrect separator"
    assert valid_date('02-29-2001') == False, "Test case 6 failed: '02-29-2001' should be invalid - not a leap year"
    assert valid_date('02-29-2004') == True, "Test case 7 failed: '02-29-2004' should be valid - leap year"
    assert valid_date('04-31-2021') == False, "Test case 8 failed: '04-31-2021' should be invalid - April has 30 days"
    assert valid_date('') == False, "Test case 9 failed: Empty string should be invalid"
    assert valid_date('12-25-2020') == True, "Test case 10 failed: '12-25-2020' should be valid"

if __name__ == "__main__": # pragma: no cover
    test_valid_date()

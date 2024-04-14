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
    global valid_date
    # Test cases for valid dates
    assert valid_date('03-11-2000') == True, "Test case for valid date 03-11-2000 failed"
    assert valid_date('06-04-2020') == True, "Test case for valid date 06-04-2020 failed"
    # Test cases for invalid dates and formats
    assert valid_date('15-01-2012') == False, "Test case for invalid date 15-01-2012 failed"
    assert valid_date('04-0-2040') == False, "Test case for invalid format 04-0-2040 failed"
    assert valid_date('06/04/2020') == False, "Test case for wrong format 06/04/2020 failed"
    # Edge cases for date validation
    assert valid_date('02-29-2020') == True, "Test case for leap year 02-29-2020 failed"
    assert valid_date('02-30-2020') == False, "Test case for invalid leap day 02-30-2020 failed"
    assert valid_date('') == False, "Test case for empty input failed"
    assert valid_date('11-31-2020') == False, "Test case for invalid November date 11-31-2020 failed"

if __name__ == "__main__": # pragma: no cover
    test_valid_date()

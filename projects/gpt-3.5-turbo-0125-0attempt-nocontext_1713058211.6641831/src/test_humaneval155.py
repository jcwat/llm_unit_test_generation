"""Given an integer. return a tuple that has the number of even and odd digits respectively.

 Example:
even_odd_count(-12) ==> (1, 1)
even_odd_count(123) ==> (1, 2)
"""

def even_odd_count(num):
    even_count = 0
    odd_count = 0
    for i in str(abs(num)):
        if int(i)%2==0:
            even_count +=1
        else:
            odd_count +=1
    return (even_count, odd_count)

def test_even_odd_count(): # pragma: no cover
    global even_odd_count
    assert even_odd_count(123456) == (3, 3), "Test case 1 failed"
    assert even_odd_count(111222333444) == (6, 6), "Test case 2 failed"
    assert even_odd_count(-987654321) == (4, 5), "Test case 3 failed"
if __name__ == "__main__": # pragma: no cover
    test_even_odd_count()

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
    
    assert even_odd_count(-12) == (1, 1), "Test case 1 failed"
    assert even_odd_count(123) == (1, 2), "Test case 2 failed"
    assert even_odd_count(24680) == (5, 0), "Test case 3 failed"
    assert even_odd_count(13579) == (0, 5), "Test case 4 failed"
if __name__ == "__main__": # pragma: no cover
    test_even_odd_count()

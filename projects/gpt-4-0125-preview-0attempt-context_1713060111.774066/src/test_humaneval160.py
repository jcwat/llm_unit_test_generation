"""
Given two lists operator, and operand. The first list has basic algebra operations, and 
the second list is a list of integers. Use the two given lists to build the algebric 
expression and return the evaluation of this expression.

The basic algebra operations:
Addition ( + ) 
Subtraction ( - ) 
Multiplication ( * ) 
Floor division ( // ) 
Exponentiation ( ** ) 

Example:
operator['+', '*', '-']
array = [2, 3, 4, 5]
result = 2 + 3 * 4 - 5
=> result = 9

Note:
The length of operator list is equal to the length of operand list minus one.
Operand is a list of of non-negative integers.
Operator list has at least one operator, and operand list has at least two operands.

"""

def do_algebra(operator, operand):
    expression = str(operand[0])
    for oprt, oprn in zip(operator, operand[1:]):
        expression+= oprt + str(oprn)
    return eval(expression)

def test_do_algebra(): # pragma: no cover
    global test_do_algebra, do_algebra
    assert do_algebra(['+'], [2, 3]) == 5, "Test case 1 failed"
    assert do_algebra(['+', '*'], [2, 3, 4]) == 14, "Test case 2 failed"
    assert abs(do_algebra(['*', '-', '+'], [3, 2, 4, 1]) - 5) <= 1e-5, "Test case 3 failed"
    assert do_algebra(['**', '//', '+'], [2, 3, 4, 5]) == 10, "Test case 4 failed"

if __name__ == "__main__": # pragma: no cover
    test_do_algebra()

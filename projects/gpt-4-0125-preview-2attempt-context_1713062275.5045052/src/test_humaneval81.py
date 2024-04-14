"""It is the last week of the semester and the teacher has to give the grades
to students. The teacher has been making her own algorithm for grading.
The only problem is, she has lost the code she used for grading.
She has given you a list of GPAs for some students and you have to write 
a function that can output a list of letter grades using the following table:
 GPA   |Letter grade
  4.0A+
> 3.7A 
> 3.3A- 
> 3.0B+
> 2.7B 
> 2.3B-
> 2.0C+
> 1.7C
> 1.3C-
> 1.0D+ 
> 0.7D 
> 0.0D-
  0.0E


Example:
grade_equation([4.0, 3, 1.7, 2, 3.5]) ==> ['A+', 'B', 'C-', 'C', 'A-']
"""

def numerical_letter_grade(grades):

   
    letter_grade = []
    for gpa in grades:
        if gpa == 4.0:
            letter_grade.append("A+")
        elif gpa > 3.7:
            letter_grade.append("A")
        elif gpa > 3.3:
            letter_grade.append("A-")
        elif gpa > 3.0:
            letter_grade.append("B+")
        elif gpa > 2.7:
            letter_grade.append("B")
        elif gpa > 2.3:
            letter_grade.append("B-")
        elif gpa > 2.0:
            letter_grade.append("C+")
        elif gpa > 1.7:
            letter_grade.append("C")
        elif gpa > 1.3:
            letter_grade.append("C-")
        elif gpa > 1.0:
            letter_grade.append("D+")
        elif gpa > 0.7:
            letter_grade.append("D")
        elif gpa > 0.0:
            letter_grade.append("D-")
        else:
            letter_grade.append("E")
    return letter_grade

def test_numerical_letter_grade(): # pragma: no cover
    global numerical_letter_grade
    assert numerical_letter_grade([4.0, 3.5, 1.7, 2.0, 3.8]) == ['A+', 'A-', 'C-', 'C+', 'A'], "Test case 1 failed"
    assert numerical_letter_grade([2.8, 1.9, 0, 4.0]) == ['B', 'C-', 'E', 'A+'], "Test case 2 failed"
    assert numerical_letter_grade([3.1, 2.3, 0.9, 3.75]) == ['B+', 'B-', 'D-', 'A'], "Test case 3 failed"
    # Tests with borderline values
    assert numerical_letter_grade([3.0, 2.7, 1.3, 0.7, 0.1]) == ['B+', 'B', 'C-', 'D', 'D-'], "Borderline values test failed"

if __name__ == "__main__": # pragma: no cover
    test_numerical_letter_grade()

#python code to calculate  Avg without using sun and len function.
total_grade=0
num_of_student=0
grade1=input('Enter the grades of students:').split(',')
grade2=map(int,grade1)
list_integers=list(grade2)
print(list_integers)

for grade in list_integers:
    total_grade=total_grade+grade
print(f'The total grade is :{total_grade}')

for item in list_integers:
    num_of_student=num_of_student+1
print(f'The total number of student is {num_of_student}')

Avg=round(total_grade/num_of_student,2)
print(f'The Avg grade of student is {Avg} .')


'''
Manually : we have a list of Grades/
2nd way.
------------------------------------------------------------------------------
'''

grades=[43,45,66,78,85,90]
total_grade=0
student_count=0

avg=round(sum(grades)/len(grades),2)
print(f'The avg is {avg}')

for item in grades:
    total_grade= item + total_grade
print(f'The total sum of grade is {total_grade} .')
# This is caalculating Sum.

for students in grades:
    student_count=student_count+1
print(f'The student count is {student_count}') 
# This is counting Number of students.


avg_grade= round(total_grade/student_count,2)
print(f'The average grade is {avg_grade} .')
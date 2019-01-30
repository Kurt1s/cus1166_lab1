from mymodules.models import Student
from mymodules.math_utils import average_grade
students = []

students.append(Student("Tom", 89))
students.append(Student("Joe", 14))
students.append(Student("Laura", 35))
students.append(Student("Mike", 95))
students.append(Student("Chris", 36))
students.append(Student("Kim", 85))
students.append(Student("Ann", 52))
students.append(Student("Mia", 44))
students.append(Student("Neo", 55))
students.append(Student("Lin", 100))

for student in students:
    student.print_student_info()

print("The average grade of the students is " + str(average_grade(students)))
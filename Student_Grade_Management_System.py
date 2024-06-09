"""
Practice Problem: Student Grade Management System
You need to create a simple student grade management system. This system should allow you to:

Add new students and their grades.
Calculate the average grade for a student.
Find the student with the highest grade.
Print a list of all students with their grades.
Instructions:
Create a list to store student records. Each record should be a dictionary with keys 'name' and 'grades', where 'grades' is a list of integers.
Implement the following functions:
add_student(students, name): Adds a new student with an empty list of grades.
add_grade(students, name, grade): Adds a grade to the list of grades for a specific student.
calculate_average_grade(students, name): Calculates the average grade for a specific student.
find_highest_grade(students): Finds the student with the highest average grade.
print_students(students): Prints a list of all students and their grades.
"""


students=[]

def add_student(students, name):
    students.append({'name':name, 'grades': []})

def add_grade(students, name, grade):
    for student in students:
        if student['name']==name:
            student['grades'].append(grade)
            break

def calculate_avg(students, name):
    for student in students:
        if student['name'] == name:
            grades = student['grades']
            if grades:
                return sum(grades) / len(grades)
            else:
                return 0
    return None

def find_highest_grade(students):
    highest_avg=-1
    highest_student = None
    for student in students:
        avg = calculate_avg(students, student['name'])
        if avg > highest_avg:
            highest_avg = avg
            highest_student = student['name']
    return highest_student

def print_student(students):
    for student in students:
        print(f"student : {student['name']}, Grades: {student['grades']}")


add_student(students, 'Alice')
add_student(students, 'Bob')
add_grade(students, 'Alice', 85)
add_grade(students, 'Alice', 90)
add_grade(students, 'Bob', 78)
add_grade(students, 'Bob', 82)
print_student(students)
print(f"Alice's average grade: {calculate_avg(students, 'Alice')}")
print(f"The student with the highest average grade is: {find_highest_grade(students)}")
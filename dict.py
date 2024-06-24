students = {'name':'ann', 'surname':'jonas', 'age':26}
# print(students.keys())
# print(students.values())

students = [
        {'name':'ann', 'surname':'jonas', 'age':26},
        {'name':'john', 'surname':'michael', 'age':13},
        {'name':'sam', 'surname':'smith', 'age':34},
        {'name':'samantha', 'surname':'dilan', 'age':45},
        {'name':'sandra', 'surname':'swift', 'age':23},
        {'name':'inna', 'surname':'williams', 'age':27},
            ]
# print(students[2]['age'])
students[2]['age']=65

# for student in students:
#     if student['age']<20:
#         print(f"the student {student['name']} {student['surname']} is {student['age']} years old and is a teenager")
#     elif student['age']>=20 and student['age'] < 35:
#         print(f"the student {student['name']} {student['surname']} is {student['age']} years old and is aan adult")
#     else:
#         print(f"the student {student['name']} {student['surname']} is {student['age']} years old and is a I guess also adult or pensioneer")

students.append({'name':'marco', 'surname':'picaso', 'age':20})
# print(students[-1])
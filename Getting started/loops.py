#FOR LOOPS

# monday_temperatures = [9.1, 8.8, 7.5]

# for temp in monday_temperatures:
#     print(round(temp))

# for letter in 'hello':
#     print(letter.title())

# student_grades = {'Mary': 9.1, 'Sim': 8.8, 'Joe': 7.5}

# for grade in student_grades.items():
#     print(grade)

# for grade in student_grades.values():
#     print(grade)

# for student in student_grades.keys():
#     print(student)

# for student, grade in student_grades.items():
#     print(f'{student} has the grade {grade}')

#WHILE LOOPS

# a = 3

# while a > 0:
#     print(1)

# username = ''

# while username != 'pypy':
#     username = input('Enter username: ')

while True:
    username = input('Enter username: ')
    if username == 'pypy':
        break
    else:
        continue
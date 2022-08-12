def add_student(group, student):
    # перевірка чи вже є такий студент в групі
    valid = False
    search_student_gbn(group, student)
    if valid or len(group) == 0:
        group.append(student)
    else:
        print('Couldn\'t add student. Enter another grade book number!!!!!!!!!')


def print_group(group):
    print('Grade_BN\t\tSurName\t\tFirstName\t\tGrade_level')
    for i in range(len(group)):
        for j in range(len(group[0])):
            print(group[i][j], end='\t|\t')
        print()


def print_student(group, grade_book_number):
    for i in range(len(group)):
        if group[i][0] == grade_book_number:
            print(f'Прізвище: {group[i][1]}, Імʼя: {group[i][2]}, Середній бал: {group[i][3]}')


def update_student(group, grade_book_number, grade_level):
    for i in range(len(group)):
        if group[i][0] == grade_book_number:
            group[i] = (group[i][0], group[i][1], group[i][2], grade_level)


def search_student_gbn(group, student):
    valid = True

    if len(group) >= 1:
        for i in range(len(group)):
            if group[i][0] == student[0]:
                valid = False

    return valid


def search_student_gbn1(group, student_gbn):
    valid = True
    for i in range(len(group)):
        if group[i][0] == student_gbn:
            valid = False

    return valid


def search_student_last_name(group, last_name):
    valid = True
    for i in range(len(group)):
        if group[i][1] == last_name:
            valid = False

    return valid


def search_student_first_name(group, first_name):
    valid = True
    for i in range(len(group)):
        if group[i][3] == first_name:
            valid = False

    return valid


def search_student_grade_level(group, grade_level):
    valid = True
    for i in range(len(group)):
        if group[i][4] == grade_level:
            valid = False

    return valid


def search_student_delete_update(group, student_gbn):
    position = None
    for i in range(len(group)):
        if group[i][0] == student_gbn:
            position = i
            break

    return position


def show_options():
    print()
    print(f'1. Create\t\t2. Find student\t\t3. Update')
    print(f'4. Delete\t\t5. Show group\t\t6. Exit')
    print()


def show_options_create():
    print()
    print(f'1. Create\t\t2. Show group\t\t3. Exit')
    print()


def check_number(parametr):
    valid = False
    if parametr.isnumeric():
        valid = True

    return valid


group = []
len_group = 0
stop_program = True
while stop_program:
    while len_group != 1:
        show_options_create()
        action = int(input('Enter number from 1 to 3: '))
        if action == 1:
            print('Add student')
            student_gbn = int(input('Enter grade book number: '))
            student_ln = input('Enter last name: ')
            student_fn = input('Enter first name: ')
            student_gl = float(input('Enter grade level: '))
            student = (student_gbn, student_ln, student_fn, student_gl)
            add_student(group, student)
            print(f'Student \'{student_ln} {student_fn}\' is added successfully')
            len_group = 1
        elif action == 2:
            print('The group is empty')
            print_group(group)
        elif action == 3:
            print('Exit')
            stop_program = False
    else:
        show_options()
        action = int(input('Enter a number from 1 to 6: '))
        if action == 1:
            print('Add student')
            student_gbn = int(input('Enter grade book number: '))
            if search_student_gbn1(group, student_gbn):
                student_ln = input('Enter last name: ')
                student_fn = input('Enter first name: ')
                student_gl = float(input('Enter grade level: '))
                student = (student_gbn, student_ln, student_fn, student_gl)
                group.append(student)
                print(f'Student \'{student_ln} {student_fn}\' added successfully')
            else:
                print('Couldn\'t add student. Enter another grade book number')
        elif action == 2:
            grade_bn = int(input('Enter grade book number: '))
            position = search_student_delete_update(group, grade_bn)
            print(f'Student with grade book number {grade_bn} is \'{group[position][1]} {group[position][2]}\'')
        elif action == 3:
            student_gbn = int(input('Enter grade book number: '))
            position = search_student_delete_update(group, student_gbn)
            new_grade_level = float(input('Enter new average level: '))
            print(f'Ready to update student \'{group[position][1]} {group[position][2]}\'?')
            answer = input('Y/N: ').upper()
            if answer == 'Y':
                group[position] = (group[position][0], group[position][1], group[position][2], new_grade_level)
                print(f'Student \'{group[position][1]} {group[position][2]}\' was successfully updated')
            else:
                print(f'Student {group[position][1]} {group[position][2]} isn\'t updated')
        elif action == 4:
            student_gbn = int(input('Enter grade book number: '))
            position = search_student_delete_update(group, student_gbn)
            print(f'Ready to delete student \'{group[position][1]} {group[position][2]}\'?')
            answer = input('Y/N: ').upper()
            if answer == 'Y':
                del_student = group.pop(position)
                print(f'Student \'{del_student[1]} {del_student[2]}\' was successfully removed')
            else:
                print(f'Student {group[position][1]} {group[position][2]} isn\'t removed')
        elif action == 5:
            print_group(group)
        elif action == 6:
            print('Exit')
            stop_program = False

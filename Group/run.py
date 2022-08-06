from student import Student
from group import Group
from aspirant import Aspirant


# function show menu
def show_options():
    print()
    print(f'1. Create\t\t2. Show student\t\t3. Show group')
    print(f'4. Upgrade\t\t5. Delete\t\t\t6. Exit')
    print()


#function enter students data
def enter_data_student():
    gbn = int(input('Enter a number of grade book: '))
    last_name = input('Enter last name: ')
    first_name = input('Enter first name: ')
    date_of_birth = input('Enter date of birth: ')
    average_level = float(input('Enter average level: '))

    return (gbn, last_name, first_name, date_of_birth, average_level)


#method enter grade book number
def enter_gbn():
    grade_bn = int(input('Enter a number of grade book: '))

    return grade_bn


#method enter average level
def enter_average_level():
    average_level = float(input('Enter a new grade level: '))

    return average_level


new_group = Group()
ns1 = Student(101, 'Vovk', 'Roman', 1992, 4.3)
ns2 = Student(102, 'Tuz', 'Andriy', 1991, 4.8)
new_group.add_student(ns1)
new_group.add_student(ns2)


run = True

while run:
    show_options()
    action = input('Enter a number from 1 to 6: ')
    if action == '1':  #enter new student
        student = enter_data_student()
        new_student = Student(student[0], student[1], student[2], student[3], student[4])
        a = new_group.add_student(new_student)
        if a:
            print('Student added succesfully')
        else:
            print('Enter another grade book number!')
    elif action == '2':  #print student
        grade_book_number = input('Enter number of grade book: ')
        print(new_group.show_student(grade_book_number))
    elif action == '3':  #print group
        for s in new_group:
            print(s)
    elif action == '4':  #upgrade student
        grade_book_number = enter_gbn()
        new_average_level = enter_average_level()
        new_group.upgrade_student(grade_book_number, new_average_level)
    elif action == '5':  #delete student
        grade_book_number = enter_gbn()
        d = new_group.delete_student(grade_book_number)
        if d:
            print('Student delete succesfully')
        else:
            print(f'Student\'s not found')
    elif action == '6':  #exit
        print('Exit')
        run = False
    else:
        print('Enter a number, please!')
        continue

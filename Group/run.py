from aspirant import Student
from group import Group
from aspirant import Aspirant


# function show menu
def show_options():
    print()
    print(f'1. Create\t\t2. Show student\t\t3. Show group')
    print(f'4. Upgrade\t\t5. Add aspirant\t\t6. Delete')
    print(f'7. Exit')
    print()


#function enter student data
def enter_data_student():
    gbn = int(input('Enter a number of grade book: '))
    last_name = input('Enter last name: ')
    first_name = input('Enter first name: ')
    year_of_birth = input('Enter year of birth: ')
    average_level = float(input('Enter average level: '))

    return (gbn, last_name, first_name, year_of_birth, average_level)


#function enter aspirant data
def enter_data_aspirant():
    gbn = int(input('Enter a number of grade book: '))
    last_name = input('Enter last name: ')
    first_name = input('Enter first name: ')
    year_of_birth = input('Enter year of birth: ')
    average_level = float(input('Enter average level: '))
    name_science_work = input('Enter name of science work: ')

    return (gbn, last_name, first_name, year_of_birth, average_level, name_science_work)


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
na1 = Aspirant(103, 'Kot', 'Anna', 1987, 4.6, 'Automatic control system STI')
new_group.add_student(ns1)
new_group.add_student(ns2)
new_group.add_student(na1)


run = True

while run:
    show_options()
    action = input('Enter a number from 1 to 7: ')
    if action == '1':  #enter new student
        student = enter_data_student()
        new_student = Student(student[0], student[1], student[2], student[3], student[4])
        s = new_group.add_student(new_student)
        if s:
            print('Student added successfully')
        else:
            print('Enter another grade book number!')
    elif action == '2':  #print student
        grade_book_number = int(input('Enter number of grade book: '))
        print(new_group.show_student(grade_book_number))
    elif action == '3':  #print group
        for s in new_group:
            print(s)
    elif action == '4':  #upgrade student
        grade_book_number = enter_gbn()
        new_average_level = enter_average_level()
        new_group.upgrade_student(grade_book_number, new_average_level)
    elif action == '5':#aspirant
        aspirant = enter_data_aspirant()
        new_aspirant = Aspirant(aspirant[0], aspirant[1], aspirant[2], aspirant[3], aspirant[4], aspirant[5])
        a = new_group.add_student(new_aspirant)
        if a:
            print('Aspirant added successfully')
        else:
            print('Enter another grade book number!')
    elif action == '6':  #delete student
        grade_book_number = enter_gbn()
        d = new_group.delete_student(grade_book_number)
        if d:
            print('Student delete successfully')
        else:
            print(f'Student\'s not found')
    elif action == '7':  #exit
        print('Exit')
        run = False
    else:
        print('Enter a number, please!')
        continue

class Group:
    def __init__(self):
        self.students = dict()
        self.current_position = 0

    def add_student(self, student):
        self.students[student.grade_book_number] = student

    def upgrade_student(self, grade_book_number, new_average_level):
        self.students.update(self, grade_book_number, new_average_level)

    def __str__(self):
        return f'{self.students}'

    def show_student(self, grade_book_number):
        return self.students[grade_book_number]

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_position >= len(self.students):
            raise StopIteration

        current_student = self.students
        self.current_position += 1

        return current_student


class Student:
    def __init__(self, grade_book_number, last_name, first_name, date_of_birth, average_level):
        self.grade_book_number = grade_book_number
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.average_level = average_level

    def __str__(self):
        return f'{self.grade_book_number} - {self.last_name} {self.first_name}, AL: {self.average_level}'


def show_options():
    print()
    print(f'1. Create\t\t2. Show student\t\t3. Update')
    print(f'4. Delete\t\t5. Show group\t\t6. Exit')
    print()


def enter_data_student():
    grade_book_number = int(input('Enter a number of grade book: '))
    last_name = input('Enter last name: ')
    first_name = input('Enter first name: ')
    date_of_birth = input('Enter date of birth: ')
    average_level = float(input('Enter average level: '))

    return grade_book_number, last_name, first_name, date_of_birth, average_level


def enter_gbn():
    grade_book_number = int(input('Enter a number of grade book: '))

    return grade_book_number


new_group = Group()
run = True

while run:
    show_options()
    action = input('Enter a number from 1 to 6: ')
    if action == '1':
        student = enter_data_student()
        new_student = Student(student[0], student[1], student[2], student[3], student[4])
        new_group.add_student(new_student)
        print(new_student)
        print(new_group)
    elif action == '2':
        grade_book_number = int(input('Enter number of grade book: '))
        print(new_group.show_student(grade_book_number))
    elif action == '3':
        enter_gbn()

    elif action == '4':
        pass
    elif action == '5':
        for s in new_group:
            print(s)
    elif action == '6':
        print('Exit')
        run = False
    else:
        continue

'''s1 = Student(101, 'dfg', 'sfsdf', '14/08/92', 4.3)
new_group.add_student(s1)
print(new_group.get(101))'''
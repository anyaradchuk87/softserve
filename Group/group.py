from groupiterator import GroupIterator


class Group:
    #constructor object
    def __init__(self):
        self.students = dict()

    #method add
    def add_student(self, student):
        if student.grade_book_number in self.students:
            return False

        self.students[student.grade_book_number] = student

        return True


    #method upgrade
    def upgrade_student(self, grade_book_number, new_average_level):
        if grade_book_number not in self.students:
            return False

        self.students[grade_book_number].average_level = new_average_level

        return True


    # method delete
    def delete_student(self, grade_book_number):
        if grade_book_number not in self.students:
            return False

        del self.students[grade_book_number]

        return True

    #method print
    def __str__(self):
        result = 'Group: '
        for s in self.students.values():
            result += f'\n\t{s}'

        return result

    #method show
    def show_student(self, grade_book_number):
        return self.students[grade_book_number]

    #metod iterator
    def __iter__(self):
        return GroupIterator(self.students.values())

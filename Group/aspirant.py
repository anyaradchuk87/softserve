from student import Student

class Aspirant(Student):
    def __init__(self, grade_book_number, last_name, first_name, date_of_birth, average_level, scientic_work):
        self.scientic_work = scientic_work
        Student.__init__(self, grade_book_number, last_name, first_name, average_level)

    def __str__(self):
        return f'{self.grade_book_number} - {self.last_name} {self.first_name}, AL: {self.average_level}, SW: {self.scientic_work}'

from student import Student

class Aspirant(Student):
    def __init__(self, grade_book_number, last_name, first_name, year_of_birth, average_level, name_scientic_work):
        self.name_scientic_work = name_scientic_work
        Student.__init__(self, grade_book_number, last_name, first_name, year_of_birth, average_level)

    def __str__(self):
        return super().__str__() + f', SW: {self.name_scientic_work}'

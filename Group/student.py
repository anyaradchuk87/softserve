class Student:
    #constructor object
    def __init__(self, grade_book_number, last_name, first_name, year_of_birth, average_level):
        self.grade_book_number = grade_book_number
        self.last_name = last_name
        self.first_name = first_name
        self.year_of_birth = year_of_birth
        self.average_level = average_level

    #method print
    def __str__(self):
        return f'{self.grade_book_number} - {self.last_name} {self.first_name}, AL: {self.average_level}'

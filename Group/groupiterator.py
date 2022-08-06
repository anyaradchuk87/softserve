class GroupIterator:
    #object constructor
    def __init__(self, students):
        self.source = list(students)
        self.current_position = 0

    #method iterator
    def __next__(self):
        if self.current_position >= len(self.source):
            raise StopIteration
        current_student = self.source[self.current_position]
        self.current_position += 1

        return current_student

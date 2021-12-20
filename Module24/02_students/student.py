class Student:

    def __init__(self, surname, name, num_of_group, marks):
        self.surname = surname
        self.name = name
        self.num_of_group = num_of_group
        self.marks = marks

    def rating(self):
        self.rating = sum(self.marks) / len(self.marks)
        return self.rating

    def __str__(self):
        return '{} {} {} {}'.format(self.surname, self.name, self.num_of_group, self.rating)

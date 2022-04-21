class Person:
    """Класс Person, аттрибуты: имя, фамилия, возраст"""

    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def age(self):
        return self.__age

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @surname.setter
    def surname(self, new_surname):
        self.__surname = new_surname

    @age.setter
    def age(self, new_age):
        self.__age = new_age

    def __str__(self):
        return f'Name: {self.__name}\
    Surname: {self.__surname}\
    Age: {self.__age}'


def person_input():
    name = input('Name: ')
    surname = input('Surname: ')
    age = int(input('Age: '))
    return name, surname, age


persons = [Person(*person_input()) for _ in range(3)]

increasing = sorted(persons, key=lambda x: x.age)
decreasing = sorted(persons, key=lambda x: -x.age)

for person in increasing:
    print(person)

for person in decreasing:
    print(person)

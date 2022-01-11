class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def __str__(self):
        return f'Меня зовут {self.__name} {self.__surname}. Мой возраст - {self.__age}'

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_surname(self, surname):
        self.__surname = surname

    def set_age(self, age):
        self.__age = age


class Employee(Person):
    def salary_calculation(self):
        pass

    def __str__(self):
        return super().__str__() + f'\nМоя зарплата {self.salary_calculation()}'


class Manager(Employee):
    def salary_calculation(self):
        return 13000


class Agent(Employee):
    sales = 0

    def salary_calculation(self):
        return round(5000 + 0.05 * self.sales, 2)


class Worker(Employee):
    working_hours = 0

    def salary_calculation(self):
        return round(100 * self.working_hours, 2)

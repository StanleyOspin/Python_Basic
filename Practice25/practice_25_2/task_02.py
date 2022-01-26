class Human():
    __counter = 0

    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)
        Human.__counter += 1

    def __str__(self):
        return 'Я {}, мне {} лет.'.format(self.__name, self.__age)

    def set_name(self, name):
        if name.isalpha():
            self.__name = name
        else:
            raise ValueError('Имя должно состоять только из букв.')

    def set_age(self, age):
        if age in range(0, 100):
            self.__age = age
        else:
            raise ValueError('Возраст должен быть числом в диапазоне от 0 до 100')

    def get_counter(self):
        return self.__counter

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


mike = Human('Mike', 20)

paul = Human('Paul', 10)
print(mike)
new_age = 25
mike.set_age(new_age)
print(mike)
print(paul)
print(mike.get_counter())
mike._Human__age = 30
print(mike._Human__age)
paul._Human__age = 15
print(paul._Human__age)

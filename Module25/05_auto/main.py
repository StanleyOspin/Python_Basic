from math import cos, sin


class Auto:

    def __init__(self, x, y, angle):
        self.set_coordinates(x, y, angle)

    def move(self, dist):
        self.__x = self.__x + dist * cos(self.__angle)
        self.__y = self.__y + dist * sin(self.__angle)
        # TODO хорошей практикой является объявление всех используемых атрибутов экземпляра класса в методе __init__
        #  тоже , присвойте им (инициализируйте) некие начальные значения, например 0

    def __str__(self):
        return f'Текущие координаты автомобиля: x = {self.__x}, y = {self.__y}'

    def set_coordinates(self, x, y, angle):
        self.__x = x
        self.__y = y
        self.__angle = angle  # TODO и этот атрибут не забыть объявить и в __init__

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_angle(self):
        return self.__angle


class Bus(Auto):

    def __init__(self, x, y, angle, people=0, money=0):
        super().__init__(x, y, angle)
        self.__people = people
        self.__money = money

    def enter(self, n):
        self.__people += n

    def exit(self, n):
        if self.__people > 0:
            if self.__people >= n:
                self.__people = 0
        else:
            self.__people -= n

    def move(self, dist):
        super().move(dist)
        self.__money += self.__people * dist

    def __str__(self):
        return f'Текущие координаты автобуса: x: {bus.get_x()}, y: {bus.get_y()}.\nВыручка {self.__money} рублей, количество пассажиров {self.__people}.'


car = Auto(x=10, y=10, angle=5)
car.move(1000)
print(car)

bus = Bus(x=1, y=1, angle=1)
bus.enter(10)
bus.move(2000)
print(bus)

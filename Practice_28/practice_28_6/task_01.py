from abc import ABC
from abc import abstractmethod
from random import choice


class Transport(ABC):
    """Абстрактный базовый класс Транспорт"""
    """Аргументы и аттрибуты: color - str и speed - int."""

    def __init__(self, color: str = '', speed: int = 0) -> None:
        self.__color = color
        self.__speed = speed

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color) -> None:
        self.__color = color

    @property
    def speed(self) -> int:
        return self.__speed

    @speed.setter
    def speed(self, speed) -> None:
        self.__speed = speed

    @abstractmethod
    def move(self) -> None:
        pass

    @abstractmethod
    def signal(self):
        pass


class PlayMusicMixin:
    """Класс примесь."""

    def play(self, melody) -> None:
        self.melody = melody
        print(f'Сейчас играет мелодия {self.melody}')


class Car(Transport):
    """Car, родительский класс Transport"""

    def move(self):
        print(f'{self.color} автомобиль, едет по земле со скоростью {self.speed} км/ч!')

    def signal(self):
        print('Signal switched on at this moment!')


car = Car(color='Черный', speed=150)
car.move()


class Boat(Transport):
    """Boat - родительский класс Transport"""

    def move(self) -> None:
        print(f'{self.color} лодка идет по воде со скоростью {self.speed} км/ч.')

    def signal(self) -> None:
        print(f'На {self.color} включена сирена!')


boat = Boat(color='Красная', speed=60)
boat.move()


class Amphibian(Transport, PlayMusicMixin):
    """Amphibian - родительский класс Transport и PlayMusicMixin"""
    can_move_on = ('земле', 'воде')

    def __init__(self, color: str = '', speed: int = 0, melody: str = '') -> None:
        super().__init__(color, speed)

    def move(self):
        move_on = choice(self.can_move_on)
        print(f'{self.color} амфибия двигается по {move_on} со скоростью {self.speed} км/ч')

    def signal(self):
        print('Signal switched on at this moment!')


amphibian = Amphibian(color='Белая', speed=60)
amphibian.move()
amphibian.play('Черные глаза')
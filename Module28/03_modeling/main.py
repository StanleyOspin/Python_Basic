import math
from abc import ABC, abstractmethod


class Figure(ABC):
    """Абстрактный базовый класс Figure"""
    """Аргументы и аттрибуты: height-int, base-int"""

    def __init__(self, height: int, base: int) -> None:
        self.__height = height
        self.__base = base

    @property
    def height(self) -> int and float:
        return self.__height

    @height.setter
    def height(self, height) -> None:
        self.__height = height

    @property
    def base(self) -> int and float:
        return self.__base

    @base.setter
    def base(self, base) -> None:
        self.__base = base

    @abstractmethod
    def square_of_figure(self):
        pass

    @abstractmethod
    def perimeter_of_figure(self):
        pass


class Triangle(Figure):
    """Kласс Triangle"""
    """Аттрибут класса высота - height: int, основание - base: int"""

    def __init__(self, height: int, base: int) -> None:
        super().__init__(height, base)

    def square_of_figure(self) -> int or float:
        triangle_square = (self.base / 2) * self.height
        return triangle_square

    def perimeter_of_figure(self) -> int or float:
        triangle_perimeter = 2 * (math.sqrt(self.base ** 2 - self.height ** 2) + 2 * self.base)
        return triangle_perimeter


class Square(Figure):
    """'Класс Square"""
    """Аттрибут класса сторона - base: int"""

    def __init__(self, base: int) -> None:
        super().__init__(base, base)

    def square_of_figure(self) -> int or float:
        area_of_square = self.base ** 2
        return area_of_square

    def perimeter_of_figure(self) -> int or float:
        perimeter = self.base * 4
        return perimeter


class Cube(Square):
    """Класс Cube, родительский класс Square"""

    def __init__(self, base: int) -> None:
        super().__init__(base)
        self.__square_cube = [Square.square_of_figure(self) for _ in range(6)]

    def cube_square_calculation(self):
        total_square = 0
        for square in self.__square_cube:
            total_square += square
        return total_square

    def __str__(self):
        return 'Total square of cube = {}'.format(self.cube_square_calculation())


class Pyramid(Triangle):
    """Класс Pyramid, родительский класс Triangle"""

    def __init__(self, height: int, base: int) -> None:
        super().__init__(height, base)
        self.__pyramid_square = [Triangle.square_of_figure(self) if i < 4 else self.base_square() for i in range(5)]

    def base_square(self) -> int:
        base_square = self.base ** 2
        return base_square

    def pyramid_square_calculation(self) -> int:
        total_square = 0
        for surface in self.__pyramid_square:
            total_square += surface
        return total_square

    def __str__(self):
        return 'Total square of pyramid = {}'.format(self.pyramid_square_calculation())


cube = Cube(base=5)
print(cube.__str__())

pyramid = Pyramid(height=5, base=5)
print(pyramid.__str__())

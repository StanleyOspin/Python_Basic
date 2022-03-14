import math


class MyMath:

    @classmethod
    def circle_len(cls, radius: int) -> int or float:
        return 2 * math.pi * radius

    @classmethod
    def circle_sq(cls, radius: int) -> int or float:
        return math.pi * radius ** 2

    @classmethod
    def cube_volume(cls, edge: int) -> int or float:
        return edge ** 3

    @classmethod
    def sphere_sq(cls, radius: int) -> int or float:
        return math.pi * 4 * (radius ** 2)


res_1 = MyMath.circle_len(radius=5)

res_2 = MyMath.circle_sq(radius=6)

print(res_1)

print(res_2)

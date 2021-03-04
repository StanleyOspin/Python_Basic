import math


def check_point(x, y, r):
    hypotenuse = math.sqrt(x ** 2 + y ** 2)
    if hypotenuse <= r:
        print('\nМонетка где-то рядом')
    else:
        print('\nМонетки в области нет')


print('Введите координаты монетки:')
x = float(input('X: '))
y = float(input('Y: '))
r = float(input('Введите радиус: '))
check_point(x, y, r)

from circle import Circle

circle_1 = Circle(0, 0, 3)
circle_2 = Circle(4, 4, 2)
print('Площадь окружности: ', circle_1.circle_square())
print('Длина окружности: ', circle_1.circle_length())
print('Окружность увеличена в k раз: ', circle_1.increase_k_times(5))
circle_1.intersection(circle_2)

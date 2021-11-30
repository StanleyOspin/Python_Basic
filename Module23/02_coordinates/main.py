import os
import random


def function_1(x, y):
    x += random.randint(0, 10)

    y += random.randint(0, 5)

    return x / y


def function_2(x, y):
    x -= random.randint(0, 10)

    y -= random.randint(0, 5)

    return y / x


file_path_coordinates = os.path.abspath('coordinates.txt')
file_path_result = os.path.abspath('result.txt')

with open(file_path_coordinates, 'r') as coordinates_file:
    for i_line in coordinates_file:
        try:
            nums_list = i_line.split()
            res_1 = function_1(int(nums_list[0]), int(nums_list[1]))
            res_2 = function_2(int(nums_list[0]), int(nums_list[1]))
            number = random.randint(0, 100)
            file_result = open(file_path_result, 'a')
            my_list = sorted([res_1, res_2, number])
            file_result.write(' '.join([str(i) for i in my_list]) + '\n')

        except SyntaxError:
            print('Ошибка синтаксиса')
        except ZeroDivisionError:
            print('На ноль делить нельзя')
        except TypeError:
            print('В файл можно записывать только строки')

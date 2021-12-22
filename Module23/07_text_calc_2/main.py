import os

PATH_TO_CALC = os.path.abspath('calc.txt')

total_sum = 0
count = 0


def string_validation(i_line):
    operators = ('//', '/', '*', '+', '-', '%')
    string = i_line.split()
    if not string[0].isdigit():
        raise ValueError
    elif not string[1] in operators:
        raise ValueError
    elif not string[2].isdigit():
        raise ValueError
    else:
        return string


def calculation(string):
    if string[1] == '//':
        result = int(string[0]) // int(string[2])
    if string[1] == '/':
        result = int(string[0]) / int(string[2])
    elif string[1] == '*':
        result = int(string[0]) * int(string[2])
    elif string[1] == '+':
        result = int(string[0]) + int(string[2])
    elif string[1] == '-':
        result = int(string[0]) - int(string[2])
    elif string[1] == '%':
        result = int(string[0]) % int(string[2])
    elif not string:
        result = 0

    return result


with open(PATH_TO_CALC, 'r') as calc_file:
    for i_line in calc_file:
        if i_line == 0:
            raise IndexError
        try:
            count += 1
            string = string_validation(i_line)
            total_sum += calculation(string)

        except IndexError:
            continue
        except ValueError:
            print('Обнаружена ошибка в строке №{0}:'.format(count), i_line)
            request = input('Хотите исправить? ')
            if request == 'да':
                i_line = input('Введите исправленную строку: ')
                string = string_validation(i_line)
                total_sum += calculation(string)
    print('Сумма: ', total_sum)



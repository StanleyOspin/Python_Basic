import os


def calculation(i_line):
    if i_line[1] == '//':
        result = int(i_line[0]) // int(i_line[2])
    if i_line[1] == '/':
        result = int(i_line[0]) / int(i_line[2])
    elif i_line[1] == '*':
        result = int(i_line[0]) * int(i_line[2])
    elif i_line[1] == '+':
        result = int(i_line[0]) + int(i_line[2])
    elif i_line[1] == '-':
        result = int(i_line[0]) - int(i_line[2])
    elif i_line[1] == '%':
        result = int(i_line[0]) % int(i_line[2])

    return result


total_sum = 0
count = 0
cursor = 0
path_to_calc = os.path.abspath('calc.txt')
with open(path_to_calc, 'r') as calc_file:
    for i_line in calc_file:
        count += 1
        string = i_line.split()

        try:
            total_sum += calculation(string)
        except (ZeroDivisionError, UnboundLocalError, IndexError):
            print('Обнаружена ошибка в строке №{0}:'.format(count), i_line)

            request = input('Хотите исправить? ')
            if request == 'да':
                correct_string = input('Введите исправленную строку: ')

                with open(path_to_calc, 'a') as calc_file:
                    calc_file.write('\n' + str(correct_string))

    print('Сумма: ', total_sum)

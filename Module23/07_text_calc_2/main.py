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
position = 0
path_to_calc = os.path.join('Practice_23_4', 'home_work_23', 'calc.txt')
with open(path_to_calc, 'r') as calc_file:
    for i_line in calc_file:
        count += 1
        position += len(i_line)
        string = i_line.split()

        try:
            total_sum += calculation(string)
        except (ZeroDivisionError, UnboundLocalError, IndexError):
            print('Обнаружена ошибка в строке №{0}:'.format(count), i_line)
            print(position - (len(i_line) - 1))
            request = input('Хотите исправить? ')
            if request == 'да':
                correct_string = input('Введите исправленную строку: ')

                with open(path_to_calc, 'r+') as calc_file:
                    calc_file.seek(position - (len(i_line) - 2))
                    calc_file.write(str(correct_string) + '\n')

    print('Сумма: ', total_sum)

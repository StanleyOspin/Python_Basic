import os


def calculation(i_line):
    # TODO если в i_line пустая строка надо вернуть 0
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
        # TODO нужно пропускать пустые строки
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
                # TODO а) это не требуется заданием, а требуется добавить результат исправленной строк и в total_sum
                #  б) что если новое выражение будет с ошибкой? создайте функцию которая принимает строку из файла и,
                #  если она валидна возвращает её, или если не валидна запрашивает в цикле пользователя пока он либо не
                #  введет валидную замену либо если он откажется - возвращает пустую строку
    print('Сумма: ', total_sum)

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
path_to_calc = os.path.abspath('calc.txt')
with open(path_to_calc, 'r') as calc_file:
    for i_line in calc_file:
        count += 1
        string = i_line.split()

        try:
            total_sum += calculation(string)
        except ZeroDivisionError:
            print('На ноль делить нельзя')
        except UnboundLocalError:
            print('В строке {0} не возможно выполнить операцию'.format(
                count))
        except IndexError:
            print('В строке {0} не хватает данных для выполнения операции'.format(count))

    print('Сумма: ', total_sum)

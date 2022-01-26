import os


class DivisionError(Exception):
    pass


path = os.path.abspath('numbers.txt')
count = 0
with open(path, 'r') as file:
    for string in file:
        count += 1
        string = string.split()
        try:

            if int(string[0]) >= int(string[1]):
                result = int(string[0]) / int(string[1])
                path_results = os.path.abspath('results.txt')
                with open(path_results, 'a', encoding='utf-8') as results_file:
                    results_file.write(str(result) + '\n')
            else:
                raise DivisionError

        except:
            print('Есть некорректные данные, см. файл exceptions.txt'.format(string[0], string[1]))
            path_exceptions = os.path.abspath('exceptions.txt')

            with open(path_exceptions, 'a', encoding='utf-8') as exceptions_file:
                exceptions_file.write(
                    'В строке №{} цифра {} меньше чем цифра {}  \n'.format(count, string[0], string[1]))

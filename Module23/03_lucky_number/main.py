import os
import random

path_to_numbers = os.path.abspath('numbers.txt')
numbers_sum = 0
exceptions = (IndexError, KeyError, NameError, ZeroDivisionError, AttributeError, SyntaxError, IndentationError, ValueError)
# TODO Превышего ограничение в 120 символов, переформатируйте код
count = 0

with open(path_to_numbers, 'w') as numbers_file:
    while numbers_sum < 777:
        try:  # TODO по заданию только бросаем исключение, без его обработки
            number = int(input('Введите число: '))
            count += 1
            numbers_sum += number

            if count == random.randint(1, 13):
                raise random.choice(exceptions)

            numbers_file.write(str(number) + '\n')
        except (
                IndexError, KeyError, NameError, ZeroDivisionError, AttributeError, SyntaxError, IndentationError,
                ValueError):
            print('Ooops, random exception occurred!!!')
            break

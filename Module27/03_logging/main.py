from typing import Callable, Any
import functools
import datetime


def logging(function: Callable) -> Callable:
    'logging это функция - декоратор, которая отвечает за логирование декорируемых функций.'
    # TODO Аналогично предыдущему
    @functools.wraps(function)
    def wrapper(*args, **kwargs) -> Any:
        try:
            result = function(*args, **kwargs)
            print(result)  # TODO это значение надо возвращать с помощью return
        except Exception as error:
            now = datetime.datetime.now()
            dt = now.strftime("%d/%m/%Y, %H:%M:%S")
            errors = ('<{}> <{}>  <{}>\n'.format(function.__name__, error, dt))
            with open('function_errors.log', 'a', encoding='utf8') as file:
                file.write(errors)

    return wrapper


@logging
def squares(number: int) -> str:
    'squares - это функция, которая находит и возвращает сумму квадратов для каждого числа number' \
    'в диапазоне от 0 до 1000'
    # TODO Аналогично предыдущему
    square_sum = 0
    for _ in range(number):
        square_sum += sum([number ** 2 for number in range(1000)])

    return 'Сумма квадратов числа: {number} равна {square_sum}'.format(number=number, square_sum=square_sum)


@logging
def division(value_1: int, value_2: int) -> int:  # TODO измените на float
    'division - это функция деления одного целого числа на другое целое число.'
    # TODO Аналогично предыдущему
    return value_1 / value_2  # TODO результат этого оператора деления всегда типа float


squares(10)
print(squares.__doc__)
print()
division(10, 0)
print(division.__doc__)
print()
print(logging.__doc__)

from typing import Callable, Any
import functools


def counter(function: Callable) -> Callable:
    'Декоратор, считающий и выводящий количество вызовов декорируемой функции.'
    function.__invocation_count__ = 0

    @functools.wraps(function)
    def wrapper(*args, **kwargs) -> Any:
        function.__invocation_count__ += 1
        result = function(*args, **kwargs)
        print('{} была вызвана: {} раз(а)'.format(function.__name__, function.__invocation_count__))
        return result

    return wrapper


@counter
def squares(number: int) -> str:
    'squares - это функция, которая находит и возвращает сумму квадратов для каждого числа'\
        'number в диапазоне от 0 до 1000.'
    square_sum = 0
    for _ in range(number):
        square_sum += sum([number ** 2 for number in range(1000)])

    return 'Сумма квадратов числа: {number} равна {square_sum}'.format(number=number, square_sum=square_sum)


squares(10)
squares(10)

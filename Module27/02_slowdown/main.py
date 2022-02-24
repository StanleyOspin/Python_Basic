from typing import Callable, Any
import functools
import time


def make_slow(function: Callable) -> Callable:
    'make_slow это функция - декоратор, которая ждёт 1 секунду,'\
            'прежде чем вызвать декорируемую функцию.'
    # TODO Аналогично предыдущему
    @functools.wraps(function)
    def wrapper(*args, **kwargs) -> Any:
        time.sleep(1)
        result = function(*args, **kwargs)
        print(result)  # TODO это значение надо возвращать с помощью return

    return wrapper


@make_slow
def squares(number: int) -> str:
    'squares - это функция, которая находит и возвращает сумму квадратов'\ 
    'для каждого числа number в диапазоне от 0 до 1000.'
    # TODO Аналогично предыдущему
    square_sum = 0
    for _ in range(number):
        square_sum += sum([number ** 2 for number in range(1000)])

    return 'Сумма квадратов числа: {number} равна {square_sum}'.format(number=number, square_sum=square_sum)


squares(10)
print()
print(make_slow.__doc__)
print()
print(squares.__doc__)

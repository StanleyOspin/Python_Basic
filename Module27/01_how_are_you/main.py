from typing import Callable, Any
import functools


def how_are_you(function: Callable) -> Callable:
    'how_are_you - это функция - декоратор, который Ваня написал от скуки'

    @functools.wraps(function)
    def wrapper(*args, **kwargs) -> Any:
        question = input('Как дела? ')
        if question:
            print('А у меня не очень! Ладно, держи свою функцию.')
            result = function(*args, **kwargs)
            print(result)

    return wrapper


@how_are_you
def squares(number: int) -> str:
    'squares - функция находит и возвращает сумму квадратов для каждого числа number'\ 
    'в диапазоне от 0 до 1000.'
    square_sum = 0
    for _ in range(number):
        square_sum += sum([number ** 2 for number in range(1000)])

    return 'Сумма квадратов числа: {number} равна {square_sum}'.format(number=number, square_sum=square_sum)


squares(10)
print(how_are_you.__doc__)
print(squares.__doc__)

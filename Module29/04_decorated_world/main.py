from typing import Callable
import functools


def decorator_with_args_for_any_decorator(decorator) -> Callable:
    """Функция - декоратор для декораторов.
       Она должна декорировать другую функцию, которая должна быть
       декоратором и даёт возможность любому декоратору принимать
        произвольные аргументы.
    """

    def decorator_maker(*args, **kwargs) -> Callable:
        """Функия - декоратор, который принимает как аргумент только
           функцию, но сохраняет все аргументы, переданные своему
           создателю"""

        def decorator_wrapper(function) -> Callable:
            """Функия - обертка декоратора, возвращает то, что вернет
               decorated_decorator.
            """
            print(f'Переданные арги и кварги в декоратор: {args}, {kwargs}')

            return decorator(function, *args, **kwargs)

        return decorator_wrapper

    return decorator_maker


@decorator_with_args_for_any_decorator
def decorated_decorator(function: Callable, *args, **kwargs) -> Callable:
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return result

    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)

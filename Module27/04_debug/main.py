from typing import Callable, Any
import functools


def debug(function: Callable) -> Callable:
    """debug - это функция декоратор который при каждом вызове декорируемой функции выводит её имя\
(вместе со всеми передаваемыми аргументами), а затем — какое значение она возвращает."""

    @functools.wraps(function)
    def wrapper(*args, **kwargs) -> Any:
        print('Вызывается {}({})'.format(function.__name__, ', '.join(
            list(f'{arg}' for arg in args) + list(f"{k}={v}" for k, v in kwargs.items()))))

        result = function(*args, **kwargs)
        print("'{}' вернула значение'{}'".format(
            function.__name__, result
        ))
        print(result)
        return result

    return wrapper


@debug
def greeting(name: str, age: int = None) -> str:
    """Функция, выводящее приветствие при передаче в качестве аргумента только имени, если помимо имени передали возраст,\
выводит текст о вашем возрасте."""
    if age:

        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)

    else:

        return "Привет, {name}!".format(name=name)


greeting("Том")

greeting("Миша", age=100)

greeting(name="Катя", age=16)

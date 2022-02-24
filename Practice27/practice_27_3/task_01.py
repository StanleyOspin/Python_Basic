from typing import Callable, Any


def decorator(function: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        function(*args, **kwargs)
        function(*args, **kwargs)

    return wrapper


@decorator
def greeting(name: str) -> str:
    print('Привет, {name}!'.format(name=name))


greeting('Tom')

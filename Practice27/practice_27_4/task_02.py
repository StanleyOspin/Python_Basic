from typing import Callable, Dict

PLAGGINS: Dict[str, Callable] = {}


def register(function: Callable) -> Callable:
    PLAGGINS[function.__name__] = function
    return function


@register
def say_hello(name: str) -> str:
    return 'Hello {name}!'.format(name=name)


@register
def say_goodbye(name: str) -> str:
    return 'Goodbye {name}!'.fomat(name=name)


print(PLAGGINS)
print(say_hello('Tom'))

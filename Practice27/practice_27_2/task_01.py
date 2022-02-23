from typing import Callable


def func_1(x: int) -> int:
    return x + 10


def func_2(func: Callable, *args, **kwargs) -> int:
    result = func_1(*args, **kwargs)
    return result ** 2


print(func_2(func_1, 9))

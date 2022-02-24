import time
from typing import Callable


def func_1(x: int) -> int:
    return x + 10


def func_2(func: Callable, *args, **kwargs) -> int:
    result = func_1(*args, **kwargs)
    return result ** 2


def timer(func: Callable, *args, **kwargs):
    started_at = time.time()
    result = func(*args, **kwargs)
    ended_at = time.time()
    runtime = round(ended_at - started_at, 5)
    print('Время работы функции: {} секунд(ы)'.format(runtime))
    return result


f_1 = timer(func_1, 9)
print(f_1)
f_2 = timer(func_2, 9, 9)
print(f_2)

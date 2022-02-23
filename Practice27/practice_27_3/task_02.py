import time
import requests

from typing import Callable


def timer(function: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> None:
        start = time.time()
        opened = function(*args, **kwargs)
        end = time.time()
        runtime = end - start
        print('Время выполненния функции {}: {} секунд(ы)'.format(function, round(runtime, 4)))
        return opened

    return wrapper


@timer
def openpage(url: str) -> str:
    webpage = requests.get(url)
    return webpage.text


site = openpage('https://google.com')
print()
print(site)

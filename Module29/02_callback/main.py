import functools
from typing import Callable


def callback(parametr: str) -> Callable:
    def call_function(function: Callable) -> Callable:
          # TODO тут надо добавить в "глобальный" словарь запись вида "урл: функция-обработчик"
        app[parametr] = function()
        @functools.wraps(function)
        def wrapper(*args, **kwargs):

            return function(*args, **kwargs)

        return wrapper

    return call_function


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


app = {}  # TODO оставьте переменную равной пустом словарю, а заполнить словарь должен именно декоратор
route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')

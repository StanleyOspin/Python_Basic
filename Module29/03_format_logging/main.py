from typing import Callable
from datetime import datetime
import time


def timer(cls, function: Callable, date_format: str) -> Callable:
    """Декоратор timer - передает формат вывода 
        даты и времени логирования в декоратор
        log_methods
   """

    def wrapped(*args, **kwargs):
        format = date_format
        for symbol in format:
            if symbol.isalpha():
                format = format.replace(symbol, '%' + symbol)

        print(
            f"Запускается '{cls.__name__}.{function.__name__}'. Дата и время запуска: {datetime.now().strftime(format)}")
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print(f"Завершение '{cls.__name__}.{function.__name__}', время работы = {round(end - start, 3)} сек.")
        return result

    return wrapped


def log_methods(date_format: str) -> Callable:
    """
    Декоратор, который
    логирует
    все
    методы
    декорируемого
    класса.
    """
    
    def decorate(cls):
        for method in dir(cls):
            if not method.startswith('__'):
                current_method = getattr(cls, method)
                decorated_method = timer(cls, current_method, date_format)
                setattr(cls, method, decorated_method)
        return cls

    return decorate
    
    
@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('Тут метод test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Тут метод test_sum_1 у наследника")

    def test_sum_2(self):
        print("Тут метод test_sum_2 у наследника")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result
    
    
my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()

import re
from typing import List

if __name__ == '__main__':
    data = input('Пример перечня: ').split()
    privat = r'\w\d{3}\w{2}\d{2,3}'
    taxi = r'\w{2}\d{3}\d{2,3}'
    privat_numbers: List[str] = list(filter(lambda x: re.fullmatch(privat, x), data))
    taxi_numbers: List[str] = list(filter(lambda x: re.fullmatch(taxi, x), data))

    print('Список номеров частных автомобилей:', privat_numbers)
    print('Список номеров такси:', taxi_numbers)

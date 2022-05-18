import re
import itertools
from typing import List

if __name__ == '__main__':
    user_input = input('Введите список номеров через запятую: ').split(',')
    pattern = r'\b[8-9]\d{9}'
    numbers_check: List[str] = list(
        map(lambda x: 'всё в порядке' if re.fullmatch(pattern, x) else 'не подходит', user_input))
    order: List[str] = ['первый номер', 'второй номер', 'третий номер']
    result = zip(itertools.cycle(order), numbers_check)
    for item in result:
        print('{}: {}'.format(item[0], item[1]))

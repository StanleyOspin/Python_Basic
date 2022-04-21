from typing import List

numbers: List[int] = sorted(list(map(int, input('Введите числа: ').split())))
print(numbers)
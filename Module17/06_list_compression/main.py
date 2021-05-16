import random


def compressed(list):
    for i in numbers:
        if i == 0:
            numbers.remove(i)
            numbers.append(0)
    return numbers


numbers = [random.randint(0, 10) for item in range(20)]
print('Список с нулевыми элементами в конце массива', compressed(numbers))
numbers = [item for item in compressed(numbers) if item != 0]
print('Сжатый список', numbers)

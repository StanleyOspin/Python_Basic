length = int(input('Введите длину списка: '))
numbers_list = [(1 if item % 2 == 0 else item % 5) for item in range(length)]
print('Результат:', numbers_list)

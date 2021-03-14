numbers = []
n = int(input('Введите число N: '))

for i in range(1, n + 1, 2):
    numbers.append(i)

for number in numbers:
    print(number, end=' ')

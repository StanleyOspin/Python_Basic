import random

sticks = int(input('Кол-во палок: '))
throws = int(input('Кол-во бросков: '))
row = ['|'] * sticks
print()
for i in range(throws):
    left, right = random.randint(1, sticks), random.randint(1, sticks)
    if right < left:
        left, right = right, left
    print('Бросок', i + 1, '.', 'Сбиты палки с номера', left, 'по номер', right)
    for j in range(left - 1, right):
        row[j] = '.'
print()
print('Результат:', ''.join(row))

n = int(input('Кол-во клеток: '))
cells = []

for i in range(n):
    print('Эффективность', i + 1, 'клетки:', end=' ')
    efficiency = int(input())
    cells.append(efficiency)

print('\nНеподходящие значения: ', end='')
for index in range(len(cells)):
    if cells[index] < index:
        print(cells[index], end=' ')
